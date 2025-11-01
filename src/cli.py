import argparse
import sys
from . import customzsh
from . import gitcommands

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
        description="cli para facilitar minha vida",
        prog="cliris"
    )

    parser.add_argument(
        "command",
        choices=["pink-terminal", "orange-terminal","git-update-branches"],
        help="se nao existe é porque não preciso ainda"
    )
    
    return parser


def main():
    parser = create_parser()
    args = parser.parse_args()
    
    exit_code = execute_command(args.command)
    sys.exit(exit_code)
