import os
import subprocess

def install_k3s():
    print("Installing k3s...")
    subprocess.run(["curl", "-sfL", "https://get.k3s.io", "-o", "k3s_install.sh"], check=True)
    subprocess.run(["chmod", "+x", "k3s_install.sh"], check=True)
    subprocess.run(["sudo", "./k3s_install.sh"], check=True)
    print("k3s installation complete.")

def check_k3s():
    print("Checking k3s status...")
    subprocess.run(["sudo", "k3s", "kubectl", "get", "nodes"])

if __name__ == "__main__":
    install_k3s()
    check_k3s()

