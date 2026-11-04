# 🚀 Yerel Apache Airflow (RAM Optimizasyonlu & LocalExecutor)

Bu proje; Apache Airflow'u Docker Compose kullanarak yerel geliştirme, test ve veri işleme amacıyla en verimli şekilde çalıştırmak üzere yapılandırılmıştır. `LocalExecutor` mimarisi kullanılarak Celery worker ve Redis gibi ekstra servislere ihtiyaç duymadan RAM tüketimi minimum seviyede tutulur.

---

## 📋 Ön Gereksinimler

Projeyi bilgisayarınızda çalıştırmadan önce aşağıdaki araçların kurulu ve hazır olduğundan emin olun:
- **Python 3.10+**
- **Git**
- **Docker Desktop** (Windows kullanıcıları için WSL 2 tabanlı Linux konteyner modunda çalışmalıdır).

---

## 🐳 Docker Desktop'ı Başlatma ve Hazırlama

Airflow konteynerlerini çalıştırmadan önce Docker servis motorunun arka planda çalışır durumda olması gerekir.

### 1. Uygulamayı Başlatın
- Windows Başlat menüsünü açın ve **Docker Desktop** uygulamasını çalıştırın.
- Görev çubuğunun sağ altındaki (bildirim alanı) balina simgesinin kırmızı/turuncu durumdan **yeşil ("Docker Desktop is running")** haline gelmesini bekleyin.

### 2. WSL 2 ve Kaynak Ayarlarını Kontrol Edin
- Docker Desktop arayüzünde sağ üstteki **Ayarlar (Dişli çark) ⚙️** simgesine tıklayın.
- **General** sekmesinde **"Use the WSL 2 based engine"** seçeneğinin işaretli olduğundan emin olun.
- **Resources → Advanced** sekmesine girerek Airflow'un kilitlenmeden çalışabilmesi için Docker'a **en az 4 GB RAM ve 2 CPU** ayrıldığını doğrulayın. *(Değişiklik yaparsanız sağ alttan "Apply & restart" butonuna tıklayın).*

### 3. Docker Motorunun Çalıştığını Terminalden Doğrulayın
PowerShell veya komut istemcisinde şu komutu çalıştırın:

```powershell
docker info
