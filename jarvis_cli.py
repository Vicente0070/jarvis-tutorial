import os
import argparse
from main_v4 import JarvisComMemoria


def main():
    parser = argparse.ArgumentParser(description="JARVIS - modo texto (CLI)")
    parser.add_argument("--no-tts", action="store_true", help="Desativa TTS (apenas saída por texto)")
    args = parser.parse_args()

    chave_api = os.getenv("OPENAI_API_KEY")
    if not chave_api:
        print("⚠️ Configure OPENAI_API_KEY no arquivo .env")
        return

    jarvis = JarvisComMemoria(chave_api)

    print("=" * 40)
    print("JARVIS - MODO TEXTO (CLI)")
    print("=" * 40)

    # Se não conhecemos o nome do usuário, pergunte por texto
    if not jarvis.nome_usuario:
        nome = input("Qual é o seu nome? ").strip()
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
            comando = input("Você: ").strip()
            if not comando:
                continue

            comando_lower = comando.lower()

            # Sair
            if any(p in comando_lower for p in ['sair', 'desligar', 'tchau', 'encerrar']):
                nome = jarvis.nome_usuario or "amigo"
                print(f"Até logo, {nome}! Foi um prazer conversar com você!")
                break

            # Limpar memória
            if 'limpar memória' in comando_lower or 'esquecer tudo' in comando_lower:
                confirm = input("Tem certeza que quer que eu esqueça nossas conversas anteriores? (sim/não) ").strip().lower()
                if confirm.startswith('s'):
                    jarvis.memoria.limpar_historico()
                    jarvis.historico = [{"role": "system", "content": jarvis._criar_prompt_sistema()}]
                    print("Ok, memória limpa. Começamos do zero!")
                else:
                    print("Ok, mantendo tudo guardado.")
                continue

            # Exportar histórico
            if 'exportar' in comando_lower and 'histórico' in comando_lower:
                arquivo = jarvis.memoria.exportar_historico()
                print(f"Histórico exportado para {arquivo}!")
                continue

            # Processa comando
            resposta = jarvis.pensar(comando)

            # Saída por texto (não usamos TTS neste entrypoint)
            print("JARVIS:", resposta)

    except KeyboardInterrupt:
        print("\n👋 Interrompido pelo usuário")
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
