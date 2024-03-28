import subprocess

# Função para bloquear IP suspeito usando iptables
def block_ip(ip_address):
    print(f"Bloqueando IP suspeito: {ip_address}")
    subprocess.run(["iptables", "-A", "INPUT", "-s", ip_address, "-j", "DROP"], check=True)

# Função para reiniciar um serviço comprometido
def restart_service(service_name):
    print(f"Reiniciando serviço comprometido: {service_name}")
    subprocess.run(["systemctl", "restart", service_name], check=True)

# Função para enviar notificação de incidente por e-mail
def send_notification(email_address, subject, message):
    print(f"Enviando notificação de incidente para: {email_address}")
    # Aqui você pode adicionar a lógica para enviar e-mail com os detalhes do incidente

# Função para responder a incidentes de segurança
def respond_to_incidents():
    print("Iniciando resposta a incidentes de segurança...\n")

    # Exemplo de ações em resposta a incidentes
    # Se detectar um IP suspeito, bloqueie-o
    block_ip("192.168.1.100")

    # Se detectar um serviço comprometido, reinicie-o
    restart_service("apache2")

    # Se detectar um incidente, envie uma notificação por e-mail
    incident_subject = "ALERTA: Atividade suspeita detectada no servidor"
    incident_details = "Detectada atividade suspeita no servidor. Tomou as seguintes ações em resposta: bloqueei um IP suspeito e reiniciei o serviço Apache."
    send_notification("admin@example.com", incident_subject, incident_details)

    print("\nResposta a incidentes de segurança concluída.")

# Chame a função principal
if __name__ == "_main_":
    respond_to_incidents()