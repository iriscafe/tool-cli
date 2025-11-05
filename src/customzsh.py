import subprocess
import sys
import os
import random
import importlib.util
from pathlib import Path

CUSTOM_FILES_DIR = Path(__file__).parent / "custom-files"

# Cores disponíveis para escolha aleatória
AVAILABLE_COLORS = ['laranja', 'rosa', 'azul', 'verde', 'amarelo', 'roxo']


def _load_create_file_module():
    """Carrega o módulo create-file-p10k dinamicamente."""
    script_path = Path(__file__).parent / "create-file-p10k.py"
    spec = importlib.util.spec_from_file_location("create_file_p10k", script_path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def color_terminal(color_template):

    try:
        # Validar que a cor é um nome válido (não número)
        if color_template:
            color_lower = color_template.lower()
            # Se for "random", escolher uma cor aleatória
            if color_lower == "random":
                color_template = random.choice(AVAILABLE_COLORS)
            # Verificar se é um número (não permitido)
            elif color_template.isdigit():
                raise ValueError(f"Cor inválida: '{color_template}'. Use apenas nomes de cores: {', '.join(AVAILABLE_COLORS)} ou 'random'")
            # Verificar se é uma cor válida
            elif color_lower not in [c.lower() for c in AVAILABLE_COLORS]:
                raise ValueError(f"Cor inválida: '{color_template}'. Cores disponíveis: {', '.join(AVAILABLE_COLORS)} ou 'random'")
        
        create_file_mod = _load_create_file_module()
        
        # Gerar nome do arquivo baseado na cor
        output_file = f'{color_template}-p10k.zsh'
        output_path = CUSTOM_FILES_DIR / output_file
        
        # Gerar o arquivo p10k.zsh usando o script
        create_file_mod.create_p10k_file(color_template, output_file=str(output_path))
        
        # Copiar o arquivo gerado para ~/.p10k.zsh
        destination = os.path.expanduser("~/.p10k.zsh")
        
        if not output_path.exists():
            print(f"Erro: Arquivo não foi gerado: {output_path}", file=sys.stderr)
            raise FileNotFoundError(f"Arquivo não foi gerado: {output_path}")
        
        subprocess.check_output(
            ["cp", str(output_path), destination], 
            stderr=subprocess.STDOUT
        )
        
        try:
            output_path.unlink()
        except OSError as e:
            print(f"Aviso: Não foi possível remover o arquivo temporário {output_path}: {e}", file=sys.stderr)
        
        # Recarregar o zshrc
        zshrc_path = os.path.expanduser("~/.zshrc")
        subprocess.check_output(
            f'source "{zshrc_path}"',
            shell=True,
            executable="/bin/zsh",
            stderr=subprocess.STDOUT
        )
        
        # Mostrar mensagem de sucesso
        print(f"Terminal configurado com a cor: {color_template}")
        
        return b""
        
    except subprocess.CalledProcessError as e:
        print(f"Erro ao executar custom zsh: {e.output.decode('utf-8')}", file=sys.stderr)
        raise
    except FileNotFoundError as e:
        print(f"Erro: {e}", file=sys.stderr)
        raise
    except Exception as e:
        print(f"Erro inesperado: {e}", file=sys.stderr)
        raise
