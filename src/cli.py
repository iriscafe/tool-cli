import argparse
import sys
from . import customzsh
from . import gitcommands

class CustomHelpFormatter(argparse.RawTextHelpFormatter):
    def format_help(self):
        
        help_text = []
        prog = self._prog
        help_text.append(f"uso: {prog} COMANDO [ARGUMENTOS]")
        help_text.append("")
        
        help_text.append("cli totalmente egoísta para facilitar minha vida")
        help_text.append("")
        
        help_text.append("COMANDO")
        help_text.append("  color-terminal COR         - configura o terminal com a cor especificada")
        help_text.append("                              cores: laranja, rosa, azul, verde, amarelo, roxo")
        help_text.append("                              ou 'random' para cor aleatória")
        help_text.append("  git-update-branches        - atualiza suas branches locais removendo as órfãs")
        help_text.append("                              e deixando apenas as que existem remotamente")
        help_text.append("")
        help_text.append("  se o comando que procura não existe é porque não preciso ainda")
        help_text.append("")
        
        help_text.append("opções:")
        help_text.append("  -h, --help                 mostra esta mensagem de ajuda e sai")
        help_text.append("")
        
        help_text.append("Exemplos:")
        help_text.append("  lino-ci color-terminal rosa")
        help_text.append("  lino-ci color-terminal laranja")
        help_text.append("  lino-ci color-terminal random")
        help_text.append("  lino-ci git-update-branches")
        
        return '\n'.join(help_text)

def execute_command(command, color_template=None):
    
    normalized_command = command.replace('_', '-')
    
    try:
        match normalized_command:
            case "color-terminal":
                result = customzsh.color_terminal(color_template)
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
  lino-ci color-terminal rosa
  lino-ci color-terminal laranja
  lino-ci color-terminal random
  lino-ci git-update-branches"""
    )

    parser.add_argument(
        "command",
        choices=["color-terminal", "git-update-branches"],
        metavar="COMANDO",
        help=argparse.SUPPRESS
    )
    
    parser.add_argument(
        "color_template",
        nargs='?',
        default=None,
        metavar="COR",
        help="Cores disponíveis (laranja, rosa, azul, verde, amarelo, roxo ou 'random')"
    )
    
    return parser


def main():
    parser = create_parser()
    args = parser.parse_args()
    
    match args.command:
        case "color-terminal":
            match args.color_template:
                case None:
                    print("Erro: color-terminal requer uma cor como argumento", file=sys.stderr)
                    print("Cores disponíveis: laranja, rosa, azul, verde, amarelo, roxo", file=sys.stderr)
                    print("Ou use 'random' para cor aleatória", file=sys.stderr)
                    sys.exit(1)
                case _:
                    pass
        case "git-update-branches":
            match args.color_template:
                case None:
                    pass
                case _:
                    print(f"Erro: argumento extra '{args.color_template}' não esperado para comando '{args.command}'", file=sys.stderr)
                    parser.print_usage()
                    sys.exit(1)
    
    exit_code = execute_command(args.command, args.color_template)
    sys.exit(exit_code)
