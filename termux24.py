import time
import os
import sys
import subprocess
import threading
import readline
import signal

def cmd_help():
    print("Comandos disponiveis:")
    print("  .status  - ver status do sistema")
    print("  .mem     - ver uso de memoria")
    print("  .kill    - matar processos python")
    print("  .restart - reiniciar sistema")
    print("  .exit    - sair")
    print("  .help    - mostrar isso")

def cmd_status():
    os.system('termux-battery-status')
    os.system('termux-wake-status')

def cmd_mem():
    os.system('free -h')

def cmd_kill():
    os.system('pkill -f python')

def cmd_restart():
    os.system('termux-wake-lock')
    os.system('python keep_alive.py &')

def main():
    print("Sistema iniciado. Digite .help para comandos")
    
    while True:
        try:
            comando = input("> ")
            
            if comando == ".help":
                cmd_help()
            elif comando == ".status":
                cmd_status()
            elif comando == ".mem":
                cmd_mem()
            elif comando == ".kill":
                cmd_kill()
            elif comando == ".restart":
                cmd_restart()
            elif comando == ".exit":
                break
            elif comando.startswith("."):
                print("Comando nao encontrado. Use .help")
            
            time.sleep(1)
            
        except KeyboardInterrupt:
            print("\nUse .exit para sair")
        except Exception as e:
            print(f"Erro: {e}")

def background():
    while True:
        subprocess.run(['termux-wake-lock'])
        os.system('nohup python -c "import time; time.sleep(999999)" > /dev/null 2>&1 &')
        time.sleep(60)

if __name__ == "__main__":
    t = threading.Thread(target=background)
    t.daemon = True
    t.start()
    
    main()
