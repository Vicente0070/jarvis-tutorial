class TextInputProvider:
    """Provedor simples de entrada por texto para Jarvis."""
    def __init__(self, prompt='Você: '):
        self.prompt = prompt

    def get_command(self):
        return input(self.prompt)


class DummyAudioProvider:
    """Placeholder para compatibilidade; não faz nada."""
    def get_command(self):
        return None
