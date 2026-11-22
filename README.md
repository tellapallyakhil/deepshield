# 🛡️ deepSheild (HTCS)
### Holistic Threat Command System — Multi-Modal AI Cybersecurity & Deepfake Defense Platform

[![Python 3.11+](https://img.shields.io/badge/Python-3.11%2B-blue.svg?logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/Backend-FastAPI-009688.svg?logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![Next.js 16](https://img.shields.io/badge/Frontend-Next.js%2016-black.svg?logo=next.js&logoColor=white)](https://nextjs.org/)
[![PyTorch](https://img.shields.io/badge/Deep%20Learning-PyTorch-EE4C2C.svg?logo=pytorch&logoColor=white)](https://pytorch.org/)
[![Docker](https://img.shields.io/badge/Deployment-Docker%20Compose-2496ED.svg?logo=docker&logoColor=white)](https://www.docker.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

> **deepSheild** is a production-grade enterprise **Security Operations Center (SOC) investigation platform** engineered to detect, correlate, and triage multi-vector cyber threats in real-time. It unifies **Computer Vision, Audio Biometrics, NLP, Anomaly Detection, and Tabular Machine Learning** under a single **Bayesian Risk Fusion Engine** backed by legally admissible digital forensics.

---

## 📑 Table of Contents
- [Target Domains & Engineering Competencies](#-target-domains--engineering-competencies)
- [System Architecture](#-system-architecture)
- [Multi-Modal AI Threat Engines](#-multi-modal-ai-threat-engines)
- [Digital Forensics & Chain of Custody](#-digital-forensics--chain-of-custody)
- [Tech Stack](#-tech-stack)
- [Quick Start Guide](#-quick-start-guide)
- [API Gateway Reference](#-api-gateway-reference)
- [Repository Structure](#-repository-structure)
- [Default Credentials](#-default-credentials)
- [Author & Contact](#-author--contact)

---

## 🎯 Target Domains & Engineering Competencies

This project demonstrates cross-disciplinary expertise spanning 4 primary engineering domains:

| Domain | Industry Role Alignment | Key Competencies Demonstrated |
|---|---|---|
| **🤖 Applied AI & Deep Learning** | ML Engineer / AI Researcher | Multi-modal architectures, Vision Transformers (ViT), fine-tuning EfficientNet, signal processing (librosa), DistilBERT NLP, unsupervised autoencoders, Random Forests, SHAP interpretability. |
| **🔒 Cybersecurity & SOC Operations** | Security Analyst / Threat Intel / SecOps | Threat correlation, phishing pretext analysis, malicious lexical heuristics, network flow anomaly detection (CIC-IDS2017), incident triage. |
| **⚖️ Digital Forensics & Incident Response (DFIR)** | Digital Forensics Engineer | Cryptographic evidence hashing (SHA-256), immutable audit logs, tamper-evident chains of custody, legal admissibility standards. |
| **💻 Full-Stack & Distributed Systems** | Full-Stack / Backend Engineer | Asynchronous worker architecture (Celery + Redis), FastAPI REST APIs, SQLAlchemy 2.0 ORM, PostgreSQL, Next.js 16 (React 19, TypeScript, Tailwind v4), Docker multi-service containerization. |

---

## 🏗️ System Architecture

```text
                               ┌───────────────────────────────────────────────────┐
                               │             Next.js 16 Web Dashboard              │
                               │  (Case Workbench • Telemetry • Forensics Room)     │
                               └─────────────────────────┬─────────────────────────┘
                                                         │ Reverse Proxy (JSON / REST)
                                                         ▼
                               ┌───────────────────────────────────────────────────┐
                               │               FastAPI Gateway (v1)                │
                               │    (OAuth2 + JWT Guard • Evidence Hashing)        │
                               └───┬─────────────┬─────────────┬─────────────┬─────┘
                                   │             │             │             │
        ┌──────────────────────────┴─┐       ┌───┴──────────┐  │        ┌────┴──────────────────────┐
        │  PostgreSQL Database (v15) │       │ Redis Broker │  │        │  Multi-Modal ML Engines   │
        │  • Cases & Evidence Tables │       │  (Port 6379) │  │        │                           │
        │  • Cryptographic AuditLog  │       └──────┬───────┘  │        │  1. ViT + EfficientNet-B4 │
        │  • ML Inferences & Scores  │              │          │        │  2. Biometric Audio (F0)  │
        └────────────────────────────┘              ▼          │        │  3. DistilBERT Phishing   │
                                             ┌──────────────┐  │        │  4. Random Forest URL     │
                                             │Celery Worker │◄─┘        │  5. PyTorch Autoencoder   │
                                             │ (Async Queue)│           └─────────────┬─────────────┘
                                             └──────────────┘                         │
                                                                                      ▼
                                                                        ┌───────────────────────────┐
                                                                        │  Bayesian Threat Fusion   │
                                                                        │ (Critical • High • Low)   │
                                                                        └───────────────────────────┘
```

---

## 🧠 Multi-Modal AI Threat Engines

deepSheild implements 5 specialized AI detectors orchestrated by an enterprise Risk Fusion Engine:

### 1. 🎭 Deepfake Video Authenticity Engine
- **Backbone**: Google Vision Transformer (`ViT-B/16`) + Custom Fine-Tuned `EfficientNet-B4` Ensemble.
- **Preprocessing**: Facial alignment and MTCNN bounding-box tracking with adaptive face crop margins and cinematic frame extraction.
- **Signals Analyzed**: Sub-surface skin micro-texture (Laplacian variance), boundary blending gradients, facial landmark stability across temporal strides.
- **Performance**: High sensitivity on FaceForensics++ benchmarks and synthetic AI films (`Oneiric`) with zero false positives on authentic mobile recordings.

### 2. 🎙️ Synthetic Voice Clone Analyzer
- **Backbone**: Biometric Acoustic Pitch & Vocoder Phase Analyzer.
- **Signals Analyzed**: Fundamental frequency ($F_0$) standard deviation, micro-jitter & shimmer, vocoder phase quantization (spectral flatness), high-frequency roll-off (<2500 Hz), and 13-channel MFCC delta dynamics.
- **Output**: Synthetic probability + auto-generated acoustic Mel-spectrogram heatmaps.

### 3. 📧 Phishing Email & Pretexting Engine
- **Backbone**: Hybrid `DistilBERT` sequence classification + RFC 5322 header heuristic engine.
- **Signals Analyzed**: Free email domain masking, SPF/DKIM validation failures, urgency keyword heuristics (`suspended`, `verify`, `action required`), and malicious attachment vectors.
- **Explainability**: Integrated **SHAP (SHapley Additive exPlanations)** attributing word-level impact scores to suspicious tokens.

### 4. 🌐 Malicious URL Classifier
- **Backbone**: High-performance Random Forest classifier trained on 100,000+ samples (PhishTank + Alexa Top 1M) with **99.66% accuracy**.
- **Features Extracted**: Shannon entropy across hostname/path, IP address presence, brand typosquatting, subdomain depth, high-risk TLD filtering (`.xyz`, `.top`, `.tk`), and `@` destination obscuration.

### 5. 🛡️ Network Intrusion Detection (IDS)
- **Backbone**: PyTorch Deep Bottleneck Autoencoder ($7 \to 16 \to 8 \to 4 \to 8 \to 16 \to 7$).
- **Methodology**: Unsupervised reconstruction error (Mean Squared Error). Trained on normal flow baseline distributions; anomalous patterns (DDoS, SYN floods, exfiltration bursts) exhibit high reconstruction loss.

### 6. ⚡ HTCS Threat Fusion Engine
- **Methodology**: Probabilistic Bayesian weighted risk aggregation:
  $$\text{Risk Score} = \frac{\sum_{i} w_i \cdot r_i}{\sum_i w_i} \times 100$$
- **Weights**: Network Anomaly (0.35), Deepfake Video (0.20), Synthetic Voice (0.15), Malicious URL (0.15), Phishing Email (0.15).
- **Triage Tiers**: Categorizes combined threat into `Safe`, `Low`, `Medium`, `High`, or `Critical` with correlated incident alert summaries.

---

## ⚖️ Digital Forensics & Chain of Custody

Every piece of evidence uploaded to deepSheild adheres to formal forensic standards:
1. **Cryptographic Hashing**: Automatic SHA-256 computation upon file intake.
2. **Immutable Audit Trails**: Every analyst action (`UPLOAD_EVIDENCE`, `RUN_DETECTION`, `TRIGGER_FUSION`, `RESOLVE_CASE`) creates a timestamped record in the `AuditLog` table.
3. **Forensic Room UI**: Dedicated Chain of Custody dashboard displaying UTC timestamps, actor IDs, evidence IDs, and cryptographically verified hashes ready for incident reporting.

---

## 💻 Tech Stack

- **Frontend**: Next.js 16, React 19, TypeScript, Tailwind CSS v4, Lucide Icons, Axios.
- **Backend**: FastAPI, Python 3.11, Pydantic v2, SQLAlchemy 2.0.
- **Machine Learning**: PyTorch, Torchvision, Transformers (HuggingFace), Scikit-Learn, Librosa, MTCNN, OpenCV, SHAP.
- **Distributed Tasks & Data**: PostgreSQL 15, Redis 7, Celery 5.4.
- **DevOps**: Docker, Docker Compose, Git.

---

## 🚀 Quick Start Guide

### Option 1: One-Command Docker Setup (Recommended)

1. **Clone the repository**:
   ```bash
   git clone https://github.com/tellapallyakhil/deepshield.git
   cd deepshield
   ```

2. **Launch all containers**:
   ```bash
   docker-compose up -d --build
   ```

3. **Access services**:
   - 🖥️ **SOC Command Dashboard**: [`http://localhost:3000`](http://localhost:3000)
   - 📖 **Interactive Swagger Docs**: [`http://localhost:8000/docs`](http://localhost:8000/docs)
   - ⚡ **API Gateway**: [`http://localhost:8000`](http://localhost:8000)

---

### Option 2: Local Development Setup (Without Docker)

<details>
<summary>Click to view manual step-by-step setup</summary>

#### Backend:
```bash
cd backend
python -m venv venv
# On Windows:
.\venv\Scripts\activate
# On Linux/macOS:
source venv/bin/activate

pip install -r requirements.txt
uvicorn app.main:app --host 127.0.0.1 --port 8000 --reload
```

#### Frontend:
```bash
cd frontend
npm install
npm run dev
```
</details>

---

## 🔑 Default Credentials

The platform seeds a default administrative analyst account on first boot:

| Field | Value |
|---|---|
| **Username / Email** | `admin` *(or `admin@deepsheild.com`)* |
| **Password** | `admin123` |
| **Role** | `admin` (Full SOC Access) |

---

## 📡 API Gateway Reference

| Method | Endpoint | Description |
|---|---|---|
| `POST` | `/api/v1/auth/login` | OAuth2 password bearer token issuance |
| `GET` | `/api/v1/cases/stats/overview` | Live database SOC threat telemetry |
| `POST` | `/api/v1/cases` | Open new incident investigation case |
| `POST` | `/api/v1/deepfake/upload` | Ingest video and execute ViT + EfficientNet inference |
| `POST` | `/api/v1/voice/upload` | Ingest audio and execute biometric vocoder analysis |
| `POST` | `/api/v1/url/scan` | Lexical & structural heuristic/RF URL scanner |
| `POST` | `/api/v1/email/analyze` | DistilBERT NLP + RFC header analysis |
| `POST` | `/api/v1/network/analyze` | Autoencoder intrusion anomaly reconstruction |
| `POST` | `/api/v1/fusion/aggregate/{id}` | Compute holistic Bayesian risk score for case |
| `GET` | `/api/v1/forensics/case/{id}/chain-of-custody` | Fetch cryptographic audit trail and evidence hashes |

---

## 📂 Repository Structure

```text
deepSheild/
├── backend/
│   ├── app/
│   │   ├── api/             # REST Routers (auth, cases, deepfake, voice, email, url, network, fusion, forensics)
│   │   ├── core/            # Security, JWT tokens, Settings & environment config
│   │   ├── db/              # SQLAlchemy database models, session factories
│   │   ├── ml/              # Multi-modal detection engines & trained model weights
│   │   │   ├── deepfake/    # ViT + EfficientNet ensemble & MTCNN preprocessor
│   │   │   ├── voice/       # Biometric acoustic F0 & spectral analyzer
│   │   │   ├── email/       # DistilBERT classifier, RFC rules & SHAP
│   │   │   ├── url/         # Random Forest lexical classifier & features
│   │   │   ├── network/     # PyTorch deep autoencoder IDS
│   │   │   └── fusion/      # Bayesian threat weighting pipeline
│   │   └── worker/          # Celery background workers and task definitions
│   ├── Dockerfile           # Optimized Python 3.11 container build
│   └── requirements.txt     # Locked production dependencies
├── frontend/
│   ├── src/
│   │   ├── app/             # Next.js 16 App Router pages (Dashboard, Cases, Forensics, Login)
│   │   ├── components/ui/   # Reusable accessible UI components
│   │   └── lib/             # AuthContext, Axios 401 interceptor, utility helpers
│   ├── Dockerfile.dev       # Development container definition
│   └── package.json         # React 19, Tailwind CSS v4, Lucide dependencies
├── docker-compose.yml       # 5-service orchestration (DB, Redis, API, Worker, Web)
├── generate_deck.py         # Automated 16:9 presentation slide builder
├── package_project.py       # Production packaging utility
└── README.md                # Project documentation
```

---

## 👤 Author & Contact

**Akhil Tellapally**
- **GitHub**: [@tellapallyakhil](https://github.com/tellapallyakhil)
- **Repository**: [https://github.com/tellapallyakhil/deepshield](https://github.com/tellapallyakhil/deepshield)

---

### 📄 License
This project is open-source and available under the [MIT License](LICENSE).
