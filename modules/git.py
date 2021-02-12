from helpers import System

os = System.Os()

def __init__():
  os = System.Os()

def git_installation():
  print("{} Iniciando instalação do Git... {}".format("-=" * 12, "=-" * 12))

  try:
    # apt returns sudo apt
    os.apt("install git")
    gitVersion = os.git_version()

    if gitVersion != 0:
      raise Exception('Ocorreu um erro inesperado na instalação do Git...')

    print('Git instalado com sucesso!')
  except Exception:
    print(Exception)
    return os.exit()
