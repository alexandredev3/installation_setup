from helpers import System

os = System.Os()

def nvm_installation():
  print("{} Iniciando instalação do NVM... {}".format("-=" * 12, "=-" * 12))

  try:
    nvm = os.curl("-o-", "https://raw.githubusercontent.com/nvm-sh/nvm/v0.37.0/install.sh", "$SHELL")

    if nvm != 0:
      raise Exception('Ocorreu um erro inesperado na instalação do NVM...')

    print('NVM instalado com sucesso!')
  except Exception:
    print(Exception)
    return os.exit()