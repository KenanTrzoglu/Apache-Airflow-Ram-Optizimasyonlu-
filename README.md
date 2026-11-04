# Yerel Apache Airflow (RAM Optimizasyonlu & LocalExecutor)

Bu depo, Apache Airflow'u Docker Compose ile yerel geliştirme ve öğrenme amacıyla çalıştırır. `LocalExecutor` görevleri Airflow ortamında yerel olarak yürütür; Celery worker ve Redis servisi kullanılmaz. PostgreSQL Airflow metadata'sını saklar, DAG dosyaları `dags/` klasöründen okunur ve web arayüzü `http://localhost:8080` adresinde açılır.

> **Uyarı:** Bu kurulum yerel geliştirme içindir; internete açık üretim ortamı olarak tasarlanmamıştır.

---

## RAM Kullanımı

Bu Compose düzeninde Celery worker ve Redis olmadığından, Celery/Redis tabanlı bir düzene göre daha az servis çalışır ve kaynak tüketimi azalabilir. 

Bu bir sabit RAM sınırı değildir: Airflow API server, scheduler, DAG processor, triggerer ve PostgreSQL yine çalışır; görevlerin bellek kullanımı ve paralelliği toplam tüketime etki eder. Docker Desktop kaynaklarını bilgisayarınıza uygun ayarlayın ve kullanımı görmek için terminalde `docker stats` çalıştırın.

---

## Gereksinimler

- **Git**
- **Docker Desktop** kurulu ve çalışır durumda olmalı; Windows'ta Linux konteynerlerini çalıştırabilmeli.
- **GitHub deposuna erişim** (özel depolar için GitHub kimlik doğrulaması gerekir).

---

## GitHub'dan İndirip İlk Kez Çalıştırma

Komutları PowerShell'de sırayla çalıştırın. 
* `GITHUB_KLON_ADRESI` yerine GitHub'daki **Code → HTTPS** menüsünden aldığınız adresi yazın.
* `REPO_KLASORU` yerine `git clone` komutunun oluşturduğu klasör adını kullanın.

### 1. Depoyu Klonlayıp VS Code'da Açın

```powershell
git clone GITHUB_KLON_ADRESI
Set-Location .\REPO_KLASORU
code .
