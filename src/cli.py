import argparse
import sys
from . import customzsh

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
            case _:
                print(f"Comando desconhecido: {command}", file=sys.stderr)
                return 1
    except Exception as e:
        print(f"Erro ao executar {command}: {e}", file=sys.stderr)
        return 1

def create_parser():
    parser = argparse.ArgumentParser(
        description="CLI para executar comandos Docker",
        prog="cliris"
    )

    parser.add_argument(
        "command",
        choices=["pink-terminal", "orange-terminal"],
        help="cli para facilitar minha vida"
    )
    
    return parser


def main():
    parser = create_parser()
    args = parser.parse_args()
    
    exit_code = execute_command(args.command)
    sys.exit(exit_code)
