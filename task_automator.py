import psutil
import os
import platform
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--list', action='store_true', help='List processes')
    parser.add_argument('--kill', type=int, help='Kill process by PID')
    parser.add_argument('--info', action='store_true', help='Show CPU & RAM')
    parser.add_argument('--clean', action='store_true', help='Clean cache (Linux only)')
    args = parser.parse_args()

    if args.list:
        for p in psutil.process_iter(['pid', 'name']):
            print(f"{p.info['pid']:5} {p.info['name']}")
    if args.kill:
        try:
            psutil.Process(args.kill).terminate()
            print(f"Process {args.kill} killed.")
        except Exception as e:
            print(f"Error: {e}")
    if args.info:
        print("CPU:", psutil.cpu_percent(1), "% | RAM:", psutil.virtual_memory().percent, "%")
    if args.clean and platform.system() == "Linux":
        os.system("sync; echo 3 | sudo tee /proc/sys/vm/drop_caches")
        print("Cache cleared.")

if __name__ == "__main__":
    main()
