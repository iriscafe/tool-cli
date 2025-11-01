import subprocess
import sys
import os
from pathlib import Path

# Tenta encontrar o diretório custom-files
# Quando o pacote está instalado, os arquivos estarão em src/custom-files dentro do site-packages
# Quando está em desenvolvimento, também estarão em src/custom-files
CUSTOM_FILES_DIR = Path(__file__).parent / "custom-files"

def pink_terminal():
    try:
        source = CUSTOM_FILES_DIR / "pink-p10k.zsh"
        destination = os.path.expanduser("~/.p10k.zsh")
        
        if not source.exists():
            print(f"Erro: Arquivo não encontrado: {source}", file=sys.stderr)
            raise FileNotFoundError(f"Arquivo não encontrado: {source}")
        
        subprocess.check_output(
            ["cp", str(source), destination], 
            stderr=subprocess.STDOUT
        )

        zshrc_path = os.path.expanduser("~/.zshrc")
        subprocess.check_output(
            f'source "{zshrc_path}"',
            shell=True,
            executable="/bin/zsh",
            stderr=subprocess.STDOUT
        )
        
        return b""

    except subprocess.CalledProcessError as e:
        print(f"Erro ao executar custom zsh: {e.output.decode('utf-8')}", file=sys.stderr)
        raise
    except FileNotFoundError as e:
        print(f"Erro: {e}", file=sys.stderr)
        raise

def orange_terminal():
    try:
        source = CUSTOM_FILES_DIR / "orange-p10k.zsh"
        destination = os.path.expanduser("~/.p10k.zsh")
        
        if not source.exists():
            print(f"Erro: Arquivo não encontrado: {source}", file=sys.stderr)
            raise FileNotFoundError(f"Arquivo não encontrado: {source}")

        subprocess.check_output(
            ["cp", str(source), destination], 
            stderr=subprocess.STDOUT
        )
        
        zshrc_path = os.path.expanduser("~/.zshrc")
        subprocess.check_output(
            f'source "{zshrc_path}"',
            shell=True,
            executable="/bin/zsh",
            stderr=subprocess.STDOUT
        )
        
        return b""
        
    except subprocess.CalledProcessError as e:
        print(f"Erro ao executar custom zsh: {e.output.decode('utf-8')}", file=sys.stderr)
        raise
    except FileNotFoundError as e:
        print(f"Erro: {e}", file=sys.stderr)
        raise