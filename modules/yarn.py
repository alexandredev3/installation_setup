from helpers import System

os = System.Os()

def yarn_installation():
  print("{} Iniciando instalação do Yarn... {}".format("-=" * 12, "=-" * 12))

  try:
    os.apt("update")

    yarn = os.apt("install --no-install-recommends yarn")

    if yarn != 0:
      raise Exception('Ocorreu um erro inesperado na instalação do Yarn...')

    os.export('PATH="$PATH:/opt/yarn-1.22.5/bin"')
    os.export('PATH="$PATH:`yarn global bin`"')

    yarnVersion = os.yarn_version()

    print('Yarn instalado com sucesso!')
  except Exception:
    print(Exception)
    return os.exit()