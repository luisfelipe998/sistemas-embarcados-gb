import serial
import time


def main():
    ser = serial.Serial('/dev/ttyACM0', 115200, timeout=1)
    ser.reset_input_buffer()
    
    command = ''
    while True:
        while not is_valid_command(command):
            command = input("Digite o comando desejado:\n 1. Recebe dados de temperatura e umidade.\n 2. Recebe dados de umidade.\n 3. Recebe dados de temperatura.\n > ")
            if is_valid_command(command):
                print(f"\nEnviando comando {command} via serial.")
                ser.write(command)
            else:
                print("\nComando digitado inválido. Tente novamente.\n")

        if ser.in_waiting > 0:
            data = ser.readall().decode('utf-8').rstrip()
            print(data)
            time.sleep(1)
            command = ''


def is_valid_command(command):
    return command == '1' or command == '2' or command == '3'


if __name__ == '__main__':
    try:
        main()
    except Exception as error:
        print(f"Ocorreu um erro durante a execução: {error}. Reiniciando...")
        time.sleep(2)
        main()
