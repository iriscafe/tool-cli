# Tool CLI - Cliris

CLI para executar comandos Docker de forma simplificada.

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
cliris docker-ps
cliris docker_images
cliris docker-images
cliris docker-network
cliris docker-volume
```

A CLI aceita tanto hífen (`-`) quanto underscore (`_`) nos nomes dos comandos.

## Comandos Disponíveis

- `docker-ps` ou `docker_ps` - Lista containers em execução
- `docker-images` ou `docker_images` - Lista imagens Docker
- `docker-network` ou `docker_network` - Lista redes Docker
- `docker-volume` ou `docker_volume` - Lista volumes Docker

## Desenvolvimento

Para trabalhar no código, instale em modo de desenvolvimento:

```bash
pip install -e .
```

Qualquer mudança no código será refletida imediatamente sem precisar reinstalar.

## Requisitos

- Python 3.10+
- Docker instalado e em execução

