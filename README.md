# Tool CLI - Cliris

CLI para facilitar minha vida toda vez que eu mudar de notebook.

## Requisitos

- Python 3.10+
- **zsh instalado** - Terminal shell necessário para executar os comandos
- **Powerlevel10k instalado** - Framework de prompt para zsh (p10k)
  - Para instalar o Powerlevel10k, consulte a [documentação oficial](https://github.com/romkatv/powerlevel10k)
  - O Powerlevel10k deve estar configurado no seu `~/.zshrc`

## Instalação

### Instalação Local (Desenvolvimento)

Para instalar o pacote localmente em modo de desenvolvimento:

```bash
pip3 install -e .
```

Isso criará o comando `cliris` no seu sistema. Se o comando não for encontrado, você pode:

**Opção 1: Adicionar ao PATH**

Adicione o diretório do Python ao seu PATH. No `~/.zshrc` (ou `~/.bash_profile`):

```bash
export PATH="/Library/Frameworks/Python.framework/Versions/3.12/bin:$PATH"
```

Depois recarregue:
```bash
source ~/.zshrc
```

**Opção 2: Usar o caminho completo**

Use o caminho completo onde o script foi instalado (geralmente algo como `/Library/Frameworks/Python.framework/Versions/3.12/bin/cliris`)

### Instalação Normal

```bash
pip3 install .
```

## Uso

Depois de instalar, você pode usar o comando `cliris` de qualquer lugar:

```bash
cliris pink-terminal
cliris orange-terminal
cliris git-update-branches
```

## Comandos Disponíveis

- `pink-terminal` - Aplica o tema rosa no terminal (Powerlevel10k)
- `orange-terminal` - Aplica o tema laranja no terminal (Powerlevel10k)
- `git-update-branches` - atualiza suas branches locais removendo as órfãs e 
deixando apenas as que existem remotamente
