class ConsoleOutputProvider:
    """Output provider que imprime no console."""
    def __init__(self, prefix='JARVIS:'):
        self.prefix = prefix

    def speak(self, texto: str):
        print(f"{self.prefix} {texto}\n")
        # retorna False indicando que não houve interrupção
        return False
