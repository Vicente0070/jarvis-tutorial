import os
import argparse
from main_v4 import JarvisComMemoria
from tools.input_providers import TextInputProvider


def main():
    parser = argparse.ArgumentParser(description="JARVIS - modo texto (CLI)")
    parser.add_argument("--tts", action="store_true", help="Habilita TTS (reproduz áudio quando possível)")
    args = parser.parse_args()

    chave_api = os.getenv("OPENAI_API_KEY")
    if not chave_api:
        print("⚠️ Configure OPENAI_API_KEY no arquivo .env")
        return

    # Cria provider de texto e output (console), passa flag de TTS
    input_provider = TextInputProvider(prompt='Você: ')
    from tools.output_providers import ConsoleOutputProvider
    output_provider = ConsoleOutputProvider(prefix='JARVIS:')

    jarvis = JarvisComMemoria(chave_api, input_provider=input_provider, tts_enabled=args.tts)
    jarvis.output_provider = output_provider
    jarvis.input_provider = input_provider

    print("=" * 40)
    print("JARVIS - MODO TEXTO (CLI)")
    print("=" * 40)
    print(f"TTS habilitado: {'sim' if args.tts else 'não'}")

    # Se não conhecemos o nome do usuário, pergunte por texto
    if not jarvis.nome_usuario:
        # Pergunta o nome interativamente quando possível. Em ambientes sem stdin (CI/container)
        # tenta usar variável de ambiente JARVIS_NOME; se faltar, usa um padrão e prossegue.
        nome = None
        try:
            nome = input("Qual é o seu nome? ").strip()
        except EOFError:
            # Ambiente sem stdin — tenta fallback
            nome = os.getenv("JARVIS_NOME")
            if nome:
                print(f"Usando JARVIS_NOME da env: {nome}")
            else:
                nome = "amigo"
                print("Nenhum stdin disponível — usando nome padrão 'amigo'.")

        if nome:
            jarvis.nome_usuario = nome
            jarvis.memoria.salvar_nome_usuario(nome)
            jarvis.historico[0]["content"] = jarvis._criar_prompt_sistema()
            saudacao = jarvis.memoria.obter_saudacao_contextual(nome)
            print(f"{saudacao} {nome}! Prazer em te conhecer.")
    else:
        saudacao = jarvis.memoria.obter_saudacao_contextual(jarvis.nome_usuario)
        print(f"{saudacao} {jarvis.nome_usuario}! Como posso ajudar?")

    try:
        while True:
            comando = input_provider.get_command().strip()
            if not comando:
                continue

            comando_lower = comando.lower()

            # Sair
            if any(p in comando_lower for p in ['sair', 'desligar', 'tchau', 'encerrar']):
                nome = jarvis.nome_usuario or "amigo"
                resposta = f"Até logo, {nome}! Foi um prazer conversar com você!"
                # fala ou imprime conforme flag
                jarvis.falar(resposta)
                break

            # Limpar memória
            if 'limpar memória' in comando_lower or 'esquecer tudo' in comando_lower:
                confirm = input("Tem certeza que quer que eu esqueça nossas conversas anteriores? (sim/não) ").strip().lower()
                if confirm.startswith('s'):
                    jarvis.memoria.limpar_historico()
                    jarvis.historico = [{"role": "system", "content": jarvis._criar_prompt_sistema()}]
                    jarvis.falar("Ok, memória limpa. Começamos do zero!")
                else:
                    jarvis.falar("Ok, mantendo tudo guardado.")
                continue

            # Exportar histórico
            if 'exportar' in comando_lower and 'histórico' in comando_lower:
                arquivo = jarvis.memoria.exportar_historico()
                jarvis.falar(f"Histórico exportado para {arquivo}!")
                continue

            # Processa comando
            resposta = jarvis.pensar(comando)

            # Saída: fala se TTS habilitado, senão imprime
            if args.tts:
                jarvis.falar(resposta)
            else:
                print("JARVIS:", resposta)

    except (KeyboardInterrupt, EOFError):
        print("\n👋 Interrompido (KeyboardInterrupt/EOF). Encerrando.")
    finally:
        # Cleanup similar ao executar()
        try:
            resumo = jarvis.memoria.obter_resumo_historico()
            jarvis.memoria.finalizar_sessao(jarvis.sessao_id, jarvis.contador_mensagens)
            jarvis.memoria.fechar()
        except Exception:
            pass

        try:
            jarvis.orquestrador.fechar()
        except Exception:
            pass

        try:
            jarvis.pyaudio.terminate()
        except Exception:
            pass

        print("JARVIS CLI encerrado.")


if __name__ == '__main__':
    main()
