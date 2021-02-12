from helpers import System

os = System.Os()

def zsh_installation():
  print("{} Iniciando instalação do ZSH... {}".format("-=" * 12, "=-" * 12))

  try:
    # apt returns sudo apt
    os.apt("install zsh")
    zshVersion = os.zsh_version()

    if zshVersion != 0:
      raise Exception('Ocorreu um erro inesperado na instalação do ZSH...')

    print('ZSH instalado com sucesso!')

    return oh_my_zsh_installation()
  except Exception:
    print(Exception)
    return os.exit()

def oh_my_zsh_installation():
  print("{} Iniciando instalação do Oh My ZSH... {}".format("-=" * 12, "=-" * 12))

  try:
    ohMyZsh = os.curl_oh_my_zsh()

    if ohMyZsh != 0:
      raise Exception('Ocorreu um erro inesperado na instalação do Oh My Zsh...')

    print('Oh My ZSH instalado com sucesso!')

    return spaceship_installation()
  except Exception:
    print(Exception)
    return os.exit()

def spaceship_installation():
  print("{} Iniciando instalação do Spaceship... {}".format("-=" * 12, "=-" * 12))  

  try:
    spaceship = os.git_clone("https://github.com/denysdovhan/spaceship-prompt.git", '"$ZSH_CUSTOM/themes/spaceship-prompt"')

    if spaceship != 0:
      raise Exception('Ocorreu um erro inesperado na instalação do Spaceship...')

    symbolicLink = os.create_symbolic_link()

    if symbolicLink != 0:
      raise Exception('Falha ao criar link simbólico')

    print('Spaceship instalado com sucesso! \n')
    print('Copie tudo que esta dentro do arquivo .zshrc e cole no arquivo /home/user/.zshrc')

  except Exception:
    print(Exception)
    return os.exit()