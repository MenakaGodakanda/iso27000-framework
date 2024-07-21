# monitoring.py
import os

def check_services():
    services = ["ssh", "apache2"]
    for service in services:
        status = os.system(f"systemctl is-active --quiet {service}")
        if status != 0:
            print(f"Service {service} is not running")

if __name__ == "__main__":
    check_services()
