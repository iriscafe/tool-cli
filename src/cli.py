import argparse
import sys
from . import customzsh
from . import gitcommands

class CustomHelpFormatter(argparse.RawTextHelpFormatter):
    def format_help(self):
        
        help_text = []
        prog = self._prog
        help_text.append(f"uso: {prog} COMANDO")
        help_text.append("")
        
        help_text.append("cli totalmente egoísta para facilitar minha vida")
        help_text.append("")
        
        help_text.append("COMANDO")
        help_text.append("  pink-terminal              - configura o terminal com o tema rosa")
        help_text.append("  orange-terminal            - configura o terminal com o tema laranja")
        help_text.append("  git-update-branches        - atualiza suas branches locais removendo as órfãs")
        help_text.append("                              e deixando apenas as que existem remotamente")
        help_text.append("")
        help_text.append("  se o comando que procura não existe é porque não preciso ainda")
        help_text.append("")
        
        help_text.append("opções:")
        help_text.append("  -h, --help                 mostra esta mensagem de ajuda e sai")
        help_text.append("")
        
        help_text.append("Exemplos:")
        help_text.append("  lino-ci pink-terminal")
        help_text.append("  lino-ci orange-terminal")
        help_text.append("  lino-ci git-update-branches")
        
        return '\n'.join(help_text)

def execute_command(command):
    
    normalized_command = command.replace('_', '-')
    
    try:
        match normalized_command:
            case "pink-terminal":
                result = customzsh.pink_terminal()
                print("Bem vinda de volta diva.")
                return 0
            case "orange-terminal":
                result = customzsh.orange_terminal()
                print("Laranja não é o novo rosa, espero que você fique bem.")
                return 0
            case "git-update-branches":
                result = gitcommands.git_prune_useless_branches()
                return 0
            case _:
                print(f"Comando desconhecido: {command}", file=sys.stderr)
                return 1
    except Exception as e:
        print(f"Erro ao executar {command}: {e}", file=sys.stderr)
        return 1

def create_parser():
    parser = argparse.ArgumentParser(
        description="cli totalmente egoísta para facilitar minha vida",
        prog="lino-ci",
        formatter_class=CustomHelpFormatter,
        epilog="""Exemplos:
  lino-ci pink-terminal
  lino-ci orange-terminal
  lino-ci git-update-branches"""
    )

    parser.add_argument(
        "command",
        choices=["pink-terminal", "orange-terminal","git-update-branches"],
        metavar="COMANDO",
        help=argparse.SUPPRESS
    )
    
    return parser


def main():
    parser = create_parser()
    args = parser.parse_args()
    
    exit_code = execute_command(args.command)
    sys.exit(exit_code)
