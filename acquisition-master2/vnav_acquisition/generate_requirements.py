import pkg_resources
import subprocess

def generate_requirements():
    try:
        # Mevcut yüklenen paketleri al
        installed_packages = subprocess.check_output([ 
            "pip", "freeze"
        ]).decode("utf-8")

        # Dosyaya yaz
        with open("requirements.txt", "w") as f:
            f.write(installed_packages)

        print("✅ requirements.txt başarıyla oluşturuldu!")

    except Exception as e:
        print(f"❌ Hata oluştu: {e}")

if __name__ == "__main__":
    generate_requirements()
