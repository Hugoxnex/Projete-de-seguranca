import subprocess
import os
import platform  # Importe o módulo platform

# Função para verificar logs do sistema por eventos incomuns
def check_system_logs():
    # Comando para verificar os logs do sistema (exemplo para sistemas baseados em Linux)
    result = subprocess.run(["journalctl", "--since", "1 hour ago"], capture_output=True, text=True)
    
    # Verifica se há eventos incomuns nos logs
    if "Error" in result.stdout or "Warning" in result.stdout:
        print("Eventos incomuns encontrados nos logs do sistema:")
        print(result.stdout)

# Função para monitorar processos em execução e identificar comportamentos suspeitos
def monitor_processes():
    # Comando para listar todos os processos em execução
    result = subprocess.run(["ps", "aux"], capture_output=True, text=True)
    
    # Analisa a saída para identificar processos suspeitos
    suspicious_processes = [line for line in result.stdout.split('\n') if "root" in line]
    
    if suspicious_processes:
        print("Processos suspeitos em execução:")
        for process in suspicious_processes:
            print(process)

# Função para verificar a integridade de arquivos críticos do sistema
def check_file_integrity():
    # Lista de arquivos críticos do sistema a serem verificados
    critical_files = ["/etc/passwd", "/etc/shadow", "/etc/sudoers"]
    
    # Verifica a integridade de cada arquivo crítico
    for file in critical_files:
        if os.path.exists(file):
            print(f"Verificando integridade do arquivo {file}")
            # Aqui você pode adicionar lógica para calcular hashes e comparar com hashes conhecidos

# Função para monitorar o tráfego de rede em busca de padrões anormais
def monitor_network_traffic():
    # Comando para visualizar o tráfego de rede (exemplo para sistemas baseados em Linux)
    result = subprocess.run(["iftop", "-n", "-N"], capture_output=True, text=True)
    
    # Verifica se há padrões anormais no tráfego de rede
    if "High traffic" in result.stdout:
        print("Padrões anormais encontrados no tráfego de rede:")
        print(result.stdout)

# Função principal
def detect_anomalies():
    print("Detectando anomalias...")

    # Verifica o sistema operacional
    system_info = platform.system()
    print("Sistema operacional:", system_info)

    # Verifica logs do sistema
    check_system_logs()

    # Monitora processos em execução
    monitor_processes()

    # Verifica integridade de arquivos críticos
    check_file_integrity()

    # Monitora tráfego de rede
    monitor_network_traffic()

# Chama a função principal se o script for executado diretamente
if __name__ == "_main_":
    detect_anomalies()