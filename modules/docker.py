from helpers import System

os = System.Os()

def docker_installation():
  print("{} Iniciando instalação do Docker e Docker... {}".format("-=" * 12, "=-" * 12))

  try:
    docker = os.apt("install \
  apt-transport-https \
  ca-certificates \
  curl \
  gnupg-agent \
  software-properties-common")

    if docker != 0:
      raise Exception('Ocorreu um erro inesperado na instalação do Docker...')

    os.curl("-fsSL", "https://download.docker.com/linux/ubuntu/gpg", "sudo apt-key add -")

    os.apt_key("0EBFCD88")

    systemArchitecture = os.system_info()

    if systemArchitecture == "x86_64":
      os.shell('sudo add-apt-repository \
   "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
   $(lsb_release -cs) \
   stable"')

      return docker_engine()
    elif systemArchitecture == "armhf":
      os.shell('sudo add-apt-repository \
   "deb [arch=armhf] https://download.docker.com/linux/ubuntu \
   $(lsb_release -cs) \
   stable"')

      return docker_engine()
    elif systemArchitecture == "arm64":
      os.shell('sudo add-apt-repository \
   "deb [arch=arm64] https://download.docker.com/linux/ubuntu \
   $(lsb_release -cs) \
   stable"')

      return docker_engine()
  
    print('Sua maquina não suporta o Docker')
  except Exception:
    print(Exception)
    return os.exit()

def docker_engine():

  try:
    os.apt("update")
    os.apt("install docker-ce docker-ce-cli containerd.io")

    docker = os.docker("run hello-world")

    if docker != 0:
      raise Exception('Ocorreu um erro inesperado na instalação do Docker...')

    print("Docker instalado com sucesso!")
    return docker_compose()
  except:
    print(Exception)
    return os.exit()

def docker_compose():
  print("{} Iniciando instalação do Docker Compose... {}".format("-=" * 12, "=-" * 12))

  try:
    compose = os.shell('sudo curl -L "https://github.com/docker/compose/releases/download/1.28.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose')

    if compose != 0:
      raise Exception('Ocorreu um erro inesperado na instalação do Docker Compose...')
      
    os.chmod("+x", "/usr/local/bin/docker-compose")
    os.shell("sudo ln -s /usr/local/bin/docker-compose /usr/bin/docker-compose")

    composeVersion = os.docker_compose_version()

    if composeVersion != 0:
      raise Exception('Docker Compose não foi instalao...')

    print("Docker Compose instalado com sucesso!")

  except:
    print(Exception)
    return os.exit()

