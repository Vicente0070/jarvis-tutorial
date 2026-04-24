Título: 0001_adicionar_input_texto — Permitir executar JARVIS por texto (CLI)

Resumo:
- Adicionar um modo de execução por texto para JARVIS, permitindo usar teclado/terminal ao invés do microfone e TTS. Útil para desenvolvimento, servidores sem áudio e testes.

Motivação / Por que:
- Facilita debugging e desenvolvimento sem dependências de áudio.
- Permite automação e uso remoto (via SSH) mais facilmente.

Escopo (dentro / fora):
- Dentro: adicionar um novo entrypoint CLI (ex.: `jarvis_cli.py` ou flag `--text` em `main_v4.py`), refatorar entrada para aceitar uma fonte (áudio ou texto).
- Fora: alterar comportamento TTS (manter como opção), reescrever orquestrador ou tools existentes.

Passos (alto nível):
1. Criar `jarvis_cli.py` (ou modificar `main_v4.py`) para parsear argumentos: `--text` (modo texto), `--history N` (quantidade de mensagens a carregar), `--no-tts`.
2. Extrair da classe JarvisComMemoria a dependência explícita do microfone: permitir injetar um `input_provider` que tenha método `get_command()`.
   - Criar `TextInputProvider` com `get_command()` lendo `input()` do usuário.
   - Preservar `AudioInputProvider` (comportamento atual) ou adaptar `ouvir()` para implementar a interface.
3. Ajustar `executar()` para usar `input_provider.get_command()` em vez de chamar `self.ouvir()` diretamente.
4. Atualizar README com instruções de execução em modo texto.
5. Testes manuais: executar `python jarvis_cli.py --text` e verificar fluxo de conversação por texto (com e sem ferramentas).

Arquivos sugeridos para alteração:
- main_v4.py: linhas relacionadas ao método `ouvir` (305–326), `executar` (488–575) e inicialização (84–110)
- adicionar `jarvis_cli.py` como novo entrypoint
- atualizar README.md: seção execução

Critérios de aceitação:
- Comando `python jarvis_cli.py --text` inicia JARVIS em modo texto.
- Entrada por teclado substitui o fluxo de áudio, e respostas do JARVIS aparecem no terminal.
- Persistência de memória e uso de ferramentas permanecem funcionais.

Riscos e mitigação:
- Risco: acoplamento forte entre `ouvir()` e outras partes; mitigação: mínima e incremental refactor com testes manuais.
- Risco: regressão no modo áudio — manter testes manuais para ambos os modos.

Notas de implementação:
- Evitar grandes refactors; prefira injeção de dependência simples.
- Manter prints e logs curtos.
- Caso aprove, implemento o plano em pequenos commits e peço sua revisão antes de push.
