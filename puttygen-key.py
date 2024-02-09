# Usage: $ python convert_ppk_to_openssh.py input.ppk output.pem
import subprocess
import argparse

def convert_ppk_to_openssh(ppk_file, openssh_file):
    try:
        # Ejecuta el comando puttygen desde el script
        subprocess.run(['puttygen', ppk_file, '-O', 'private-openssh', '-o', openssh_file])

        print(f"Conversión exitosa. Clave privada OpenSSH guardada en: {openssh_file}")

    except Exception as e:
        print(f"Error durante la conversión: {str(e)}")

if __name__ == "__main__":
    # Configuración del parser de argumentos de la línea de comandos
    parser = argparse.ArgumentParser(description="Convertir clave privada PPK a formato OpenSSH")
    parser.add_argument("ppk_file", help="Archivo de clave privada PPK")
    parser.add_argument("openssh_file", help="Archivo de salida para la clave privada OpenSSH")

    # Parsea los argumentos
    args = parser.parse_args()

    # Llama a la función para realizar la conversión
    convert_ppk_to_openssh(args.ppk_file, args.openssh_file)
