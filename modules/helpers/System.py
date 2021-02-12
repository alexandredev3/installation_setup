import os

class Os:
  def __init__(self):
    self.system = os.system

  def system_info(self):
    return os.uname().machine

  def curl_oh_my_zsh(self): 
    return self.system('sh -c "$(curl -fsSL https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"')

  def apt(self, command):
    return self.system("sudo apt " + command)

  def chmod(self, permissions, directory):
    return self.system("sudo chmod " + permissions + " " + directory)

  def docker(self, command):
    return self.system("sudo docker " + command)

  def curl(self, args, link, variable):
    return self.system("sudo curl " + args + " " + link + " | " + variable)

  def shell(self, command):
    return self.system(command)

  def apt_key(self, fingerprint):
    return self.system("sudo apt-key fingerprint " + fingerprint)

  def export(self, command):
    return self.system("export " + command)

  def git_version(self):
    return self.system("git --version")

  def docker_compose_version(self):
    return self.system("docker-compose --version")

  def yarn_version(self):
    return self.system("yarn --version")

  def create_symbolic_link(self):
    return self.system('ln -s "$ZSH_CUSTOM/themes/spaceship-prompt/spaceship.zsh-theme" "$ZSH_CUSTOM/themes/spaceship.zsh-theme"')

  def zsh_version(self):
    return self.system("zsh --version")

  def git_clone(repository, directory):
    return self.system("git clone " + repository + " " + directory)

  def exit():
    return self.system("exit")