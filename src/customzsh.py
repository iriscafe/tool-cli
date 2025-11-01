import subprocess
import sys

def pink_terminal():
    try:
        return subprocess.check_output(["cp", "custom-files/pink-p10k.zsh", "~/.p10k.zsh"], stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError as e:
        print(f"Erro ao executar custom zsh: {e.output.decode('utf-8')}", file=sys.stderr)
        raise
    except FileNotFoundError:
        print("Zsh não encontrado. Certifique-se de que o Zsh está instalado.", file=sys.stderr)
        raise

def orange_terminal():
    try:
        return subprocess.check_output(["cp", "custom-files/orange-p10k.zsh", "~/.p10k.zsh"], stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError as e:
        print(f"Erro ao executar custom zsh: {e.output.decode('utf-8')}", file=sys.stderr)
        raise
    except FileNotFoundError:
        print("Zsh não encontrado. Certifique-se de que o Zsh está instalado.", file=sys.stderr)
        raise
