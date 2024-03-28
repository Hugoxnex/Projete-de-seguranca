import subprocess

# Função para auditar configurações de segurança
def audit_security_config():
    print("Auditando configurações de segurança...\n")

    # Verificar permissões de arquivos e diretórios
    print("Verificando permissões de arquivos e diretórios:")
    subprocess.run(["find", "/etc", "-type", "f", "-perm", "/o+w", "-ls"], check=True)
    subprocess.run(["find", "/etc", "-type", "d", "-perm", "/o+w", "-ls"], check=True)

    # Verificar configurações de firewall
    print("\nVerificando configurações de firewall:")
    subprocess.run(["iptables", "-L"], check=True)

    # Verificar configurações de usuário e grupo
    print("\nVerificando configurações de usuário e grupo:")
    subprocess.run(["cat", "/etc/passwd"], check=True)
    subprocess.run(["cat", "/etc/group"], check=True)

    # Verificar configurações de SSH
    print("\nVerificando configurações de SSH:")
    subprocess.run(["cat", "/etc/ssh/sshd_config"], check=True)

    # Verificar configurações de sudoers
    print("\nVerificando configurações de sudoers:")
    subprocess.run(["visudo", "-c"], check=True)

# Chamar a função principal
if __name__ == "_main_":
    audit_security_config()