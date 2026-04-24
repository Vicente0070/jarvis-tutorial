Título: 0002_proximas_acoes — Próximas melhorias e tarefas

Resumo:
- Lista priorizada de ações pequenas e incrementais para consolidar o modo texto, refatorar providers, adicionar testes e preparar futuras ferramentas.

Motivação / Por que:
- Organizar trabalho em passos pequenos e revisáveis. Garantir que o modo texto e o modo áudio fiquem testáveis e mantíveis antes de adicionar novas tools.

Escopo (dentro / fora):
- Dentro: refactor leve para modularizar input/output, adicionar entrypoint unificado opcional, criar testes manuais/automatizados iniciais, documentação, e pipeline de tarefas.
- Fora: reescrever o orquestrador, criar novas tools além das já existentes, integração CI completa (opcional futuro).

Tarefas (priorizadas):
1. Refatorar inicialização (pequeno)
   - Extrair/confirmar interface de InputProvider (get_command) e OutputProvider (sintético: falar/imprimir).
   - Garantir que main_v4 e jarvis_cli usem a mesma API do construtor JarvisComMemoria.
2. Unificar CLI/entrypoint (opcional)
   - Adicionar argumento em main_v4.py para rodar em modo texto (reaproveitar jarvis_cli) — permite um único entrypoint.
3. Testes manuais (já documentados)
   - Validar checklist do README para ambos os modos.
4. Smoke tests automatizados (médio)
   - Criar scripts que executem jarvis_cli.py em modo texto com mocks para OpenAI e verifiquem saída esperada.
   - Usar pytest ou scripts shell simples. Mocking pode ser via variáveis de ambiente ou monkeypatch.
5. Tasks e rastreabilidade
   - Criar issues ou arquivos de plano (melhorias/0003...) para cada nova tool a implementar.

Arquivos sugeridos para alteração:
- main_v4.py: adaptar construtor/entrypoint
- jarvis_cli.py: manter como wrapper leve (ou apontar para main_v4)
- tools/input_providers.py: consolidar provider interfaces
- melhorias/0003_*.md futuros planos
- tests/: novo diretório para smoke tests (opcional)

Riscos e mitigação:
- Risco: regressão no modo áudio ao refatorar; mitigação: testes manuais rápidos e commits pequenos.
- Risco: dependência de APIs externas durante testes; mitigação: criar mocks/fakes para OpenAI e tools.

Critérios de aceitação:
- Plano criado e numerado em melhorias (este arquivo).
- Pequenos refactors aplicados em main_v4.py e jarvis_cli.py (antes de avançar para testes automáticos).
- Checklist README validado manualmente.

Próximo passo sugerido (opcional):
- Se aprovar, implemento a tarefa 1 (extrair OutputProvider, garantir compatibilidade) em um commit separado e retorno para revisão.

Notas:
- Mantemos commits pequenos e reversíveis.
- Antes de qualquer push para remoto, confirmarei com você.
