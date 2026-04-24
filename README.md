# 🤖 JARVIS - Assistente Virtual Inteligente

Bem-vindo ao projeto **JARVIS**, um assistente virtual completo construído com Python, OpenAI e recursos de reconhecimento de voz. Este projeto evolui através de 4 versões, cada uma adicionando funcionalidades mais avançadas.

---

## 📺 Tutoriais em Vídeo

Acompanhe o desenvolvimento completo do projeto através dos nossos tutoriais no YouTube:

- **Versão 1** - Conceitos Básicos: [Assistir Tutorial](https://www.youtube.com/watch?v=2_VAtNsemRY)
- **Versão 2** - Full-Duplex Audio: FEITO
- **Versão 3** - OpenAI TTS: FEITO
- **Versão 4** - Memória e Tools: FEITO
- **Versão 5** - Em breve
---

## 🚀 Recursos por Versão

### 📦 Versão 1 - JARVIS Básico

**Arquivo:** `main_v1.py`

A versão mais simples do JARVIS, ideal para iniciantes entenderem os conceitos fundamentais:

✨ **Funcionalidades:**

- 🎤 Reconhecimento de voz via Google Speech Recognition
- 🗣️ Síntese de voz com pyttsx3
- 🤖 Integração com OpenAI GPT para respostas inteligentes
- 🎚️ Calibração automática do microfone
- 💬 Loop de conversação básico

**Conceitos Aprendidos:**

- Speech Recognition básico
- Text-to-Speech local
- API da OpenAI
- Gerenciamento de ambiente (.env)

---

### 🔄 Versão 2 - Full-Duplex com PyAudio

**Arquivo:** `main_v2.py`

Evolução significativa com capacidade de interromper o JARVIS enquanto ele fala:

✨ **Funcionalidades:**

- 🎧 **Full-Duplex:** Detecta quando você fala mesmo durante a resposta
- ⚡ Sistema de interrupção inteligente
- 🎮 Audio com Pygame (mais controle sobre reprodução)
- 📊 Monitoramento de áudio em tempo real com PyAudio
- 🧵 Threading para operações paralelas
- 🔇 Detecção de níveis de áudio ambiente

**Novos Conceitos:**

- PyAudio para captura em tempo real
- Threading e sincronização
- Pygame para controle de áudio
- Interrupção por detecção de voz

---

### 🎙️ Versão 3 - OpenAI TTS de Alta Qualidade

**Arquivo:** `main_v3.py`

Melhora significativa na qualidade da voz usando o TTS da OpenAI:

✨ **Funcionalidades:**

- 🎵 **OpenAI TTS:** Vozes naturais e expressivas
- 🔊 Modelos: `tts-1` (rápido) ou `tts-1-hd` (alta qualidade)
- 🎭 Múltiplas vozes: alloy, echo, fable, onyx, nova, shimmer
- 💾 Cache de áudio temporário
- ⚡ Mantém full-duplex da v2

**Novos Conceitos:**

- OpenAI Text-to-Speech API
- Manipulação de arquivos de áudio temporários
- Diferentes perfis de voz

---

### 🧠 Versão 4 - Memória Persistente + Sistema de Tools

**Arquivo:** `main_v4.py`

A versão mais completa com memória entre sessões e capacidade de usar ferramentas:

✨ **Funcionalidades:**

- 💾 **Memória Persistente:** SQLite guarda todo o histórico
- 👤 **Personalização:** Lembra seu nome e preferências
- 🌅 **Saudações Contextuais:** Bom dia/tarde/noite personalizadas
- 🛠️ **Sistema de Tools:**
  - 🌦️ Clima em tempo real
  - ⏰ Hora e data
  - 🔍 Busca na web (Perplexity AI)
  - 📁 Sistema de arquivos
  - 💾 Gerenciamento de memória
- 🔄 Histórico entre sessões
- 📊 Exportação de conversas
- 🎯 Orquestrador inteligente de ferramentas

**Estrutura de Tools:**

```
tools/
├── __init__.py
├── README.md
├── orquestrador_tools.py  # Gerenciador central
├── clima.py               # API OpenWeather
├── hora.py                # Data/hora
├── buscar_web.py          # Perplexity AI
├── sistema_arquivos.py    # Operações de arquivo
└── jarvis_memoria.py      # Gerenciamento SQLite
```

**Novos Conceitos:**

- Banco de dados SQLite
- Sistema de plugins/tools
- Function calling da OpenAI
- Persistência de dados
- Arquitetura modular

---

## 🛠️ Instalação

### Pré-requisitos

- Python 3.8+
- Microfone funcional
- Chaves de API (OpenAI e opcionalmente Perplexity)

### Passo a Passo

1. **Clone o repositório:**

```bash
git clone https://github.com/eai-academy/jarvis-tutorial.git
cd jarvis-tutorial
```

2. **Instale as dependências:**

```bash
pip install -r requirements.txt
```

3. **Configure as variáveis de ambiente:**

Crie um arquivo `.env` na raiz do projeto:

```env
OPENAI_API_KEY=sua_chave_openai
OPENAI_MODEL=gpt-4o-mini
PERPLEXITY_API_KEY=sua_chave_perplexity  # Opcional (v4)
OPENWEATHER_API_KEY=sua_chave_openweather # Opcional (v4)
```

4. **Execute a versão desejada:**

```bash
# Versão 1 - Básico
python main_v1.py

# Versão 2 - Full-Duplex
python main_v2.py

# Versão 3 - OpenAI TTS
python main_v3.py

# Versão 4 - Completa
python main_v4.py
```

---

## 📋 Dependências Principais

- **openai** - API da OpenAI (GPT + TTS)
- **SpeechRecognition** - Reconhecimento de voz
- **pyttsx3** - Text-to-Speech local (v1-v2)
- **PyAudio** - Captura de áudio em tempo real (v2-v4)
- **pygame** - Controle de reprodução de áudio (v2-v4)
- **python-dotenv** - Gerenciamento de variáveis de ambiente
- **requests** - Requisições HTTP
- **numpy** - Processamento de sinais de áudio
- **perplexityai** - Busca web avançada (v4)

---

## 🎯 Como Usar

### Comandos Básicos (Todas as Versões)

- Fale naturalmente com o JARVIS
- Diga "sair", "tchau" ou "adeus" para encerrar
- O JARVIS responde a qualquer pergunta via GPT

### Recursos Específicos v4

- **Memória:** "O que conversamos antes?"
- **Clima:** "Como está o clima em São Paulo?"
- **Hora:** "Que horas são?"
- **Busca:** "Busque informações sobre Python"
- **Arquivos:** "Crie um arquivo teste.txt"

---

## 🗺️ Evolução do Projeto

```
v1: Básico
  ↓
v2: + Full-Duplex
  ↓
v3: + OpenAI TTS
  ↓
v4: + Memória + Tools
```

Cada versão mantém as funcionalidades da anterior e adiciona novas capacidades.

---

## 📚 Estrutura do Projeto

```
jarvis-tutorial/
│
├── main_v1.py              # Versão 1 - Básico
├── main_v2.py              # Versão 2 - Full-Duplex
├── main_v3.py              # Versão 3 - OpenAI TTS
├── main_v4.py              # Versão 4 - Completa
│
├── tools/                  # Sistema de ferramentas (v4)
│   ├── __init__.py
│   ├── orquestrador_tools.py
│   ├── clima.py
│   ├── hora.py
│   ├── buscar_web.py
│   ├── sistema_arquivos.py
│   ├── jarvis_memoria.py
│   └── README.md
│
├── requirements.txt        # Dependências
├── .env                    # Configurações (não versionado)
├── .gitignore
└── README.md              # Este arquivo
```

---

## 🔑 Obtendo Chaves de API

### OpenAI (Obrigatória)

1. Acesse: https://platform.openai.com/
2. Crie uma conta
3. Vá em "API Keys"
4. Crie uma nova chave

### Perplexity AI (Opcional - v4)

1. Acesse: https://www.perplexity.ai/
2. Crie uma conta
3. Gere uma API key

### OpenWeather (Opcional - v4)

1. Acesse: https://openweathermap.org/api
2. Crie uma conta gratuita
3. Gere uma API key

---

## 🐛 Solução de Problemas

### Erro no PyAudio (Windows)

```bash
pip install pipwin
pipwin install pyaudio
```

### Erro no PyAudio (Linux)

```bash
sudo apt-get install portaudio19-dev python3-pyaudio
pip install pyaudio
```

### Erro no PyAudio (Mac)

```bash
brew install portaudio
pip install pyaudio
```

### Microfone não detectado

- Verifique permissões do sistema
- Teste com outro software de gravação
- Ajuste o `PAUSA_SILENCIO` no código

---

## 🤝 Contribuindo

Contribuições são bem-vindas! Sinta-se à vontade para:

- Reportar bugs
- Sugerir novas funcionalidades
- Melhorar a documentação
- Criar novas tools para a v4

---

## 📄 Licença

Este projeto é para fins educacionais. Use livremente para aprender e criar seus próprios assistentes!

---

## 👨‍💻 Autor

**EAI Academy**

- YouTube: [EAI Academy](https://www.youtube.com/@eaiacademy)
- GitHub: [eai-academy](https://github.com/eai-academy)

---

## ⭐ Apoie o Projeto

Se este projeto te ajudou, deixe uma ⭐ no repositório e se inscreva no canal do YouTube!

---

**Divirta-se construindo seu próprio JARVIS! 🚀**
