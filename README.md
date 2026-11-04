# 🚀 Yerel Apache Airflow (RAM Optimizasyonlu & LocalExecutor)

Bu proje; Apache Airflow'u Docker Compose kullanarak yerel geliştirme, test ve veri işleme amacıyla en verimli şekilde çalıştırmak üzere yapılandırılmıştır. `LocalExecutor` mimarisi kullanılarak Celery worker ve Redis gibi ekstra servislere ihtiyaç duymadan RAM tüketimi minimum seviyede tutulur.

---

## 📋 Ön Gereksinimler

Projeyi bilgisayarınızda çalıştırmadan önce aşağıdaki araçların kurulu ve hazır olduğundan emin olun:
- **Python 3.10+**
- **Git**
- **Docker Desktop** (Açık ve çalışır durumda olmalı; Windows kullanıcıları için Linux konteyner modunda aktif olmalıdır).

---

## 🛠️ Sıfırdan Kurulum ve Çalıştırma Rehberi

Projeyi klonladıktan veya ZIP olarak indirdikten sonra, VS Code içerisinde bir PowerShell terminali açarak sırasıyla aşağıdaki adımları uygulayın.

### 1. Python Sanal Ortamını (venv) Kurun ve Aktif Edin
Yerel geliştirme ortamınızın diğer projelerle çakışmaması için önce izole bir sanal ortam oluşturun:

```powershell
# Sanal ortamı oluşturun
python -m venv .venv

# Sanal ortamı aktif hale getirin (Windows PowerShell)
.venv\Scripts\Activate.ps1
