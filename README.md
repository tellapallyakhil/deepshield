# 🛡️ deepSheild (HTCS)
### Holistic Threat Command System — Multi-Modal AI Cybersecurity & Deepfake Defense Platform

[![Python 3.11+](https://img.shields.io/badge/Python-3.11%2B-blue.svg?logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/Backend-FastAPI-009688.svg?logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![Next.js 16](https://img.shields.io/badge/Frontend-Next.js%2016-black.svg?logo=next.js&logoColor=white)](https://nextjs.org/)
[![PyTorch](https://img.shields.io/badge/Deep%20Learning-PyTorch-EE4C2C.svg?logo=pytorch&logoColor=white)](https://pytorch.org/)
[![Docker](https://img.shields.io/badge/Deployment-Docker%20Compose-2496ED.svg?logo=docker&logoColor=white)](https://www.docker.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**deepSheild (HTCS)** is an enterprise Security Operations Center (SOC) investigation platform engineered to detect, correlate, and triage multi-vector cyber attacks in real-time. By bridging deep learning and digital forensics, the platform unifies **Computer Vision, Audio Biometrics, NLP, Anomaly Detection, and Lexical Intelligence** under an adaptive **Bayesian Threat Fusion Engine**.

---

## 📑 Table of Contents
- [Executive Overview](#-executive-overview)
- [System Architecture](#-system-architecture)
- [Multi-Modal Threat Detection Engines](#-multi-modal-threat-detection-engines)
- [Digital Forensics & Chain of Custody](#-digital-forensics--chain-of-custody)
- [Tech Stack](#-tech-stack)
- [Quick Start Guide](#-quick-start-guide)
- [API Gateway Reference](#-api-gateway-reference)
- [Repository Structure](#-repository-structure)
- [Default Credentials](#-default-credentials)
- [Author & Contact](#-author--contact)

---

## 💡 Executive Overview

Modern cyber threat actors rarely operate in single silos—sophisticated phishing campaigns combine deepfake executive video calls, synthetic voice clones, credential harvesting domains, and network infiltration attempts. 

Existing SOC tooling treats these events as disconnected alerts. **deepSheild** solves this by providing:
1. **Multi-Modal Detection**: Ingests video, audio, text, URLs, and network flow telemetry within a single unified analyst workbench.
2. **Explainable AI (XAI)**: Provides transparent signals rather than black-box labels (SHAP word impacts, Mel-spectrogram acoustic heatmaps, and facial bounding-box tracking).
3. **Probabilistic Risk Fusion**: Synthesizes cross-vector signals into a unified Bayesian threat score ($0-100\%$) with automated severity tiering.
4. **Legally Admissible Forensics**: Built-in SHA-256 evidence hashing and immutable audit logging for incident response compliance.

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

## 🧠 Multi-Modal Threat Detection Engines

| Vector | Model / Backbone | Target Signals & Methodology | Benchmark / Accuracy |
|---|---|---|---|
| **🎭 Deepfake Video** | Google ViT-B/16 + EfficientNet-B4 Ensemble | Sub-surface facial micro-texture, boundary blending gradients, facial landmark stability | FaceForensics++ (400 videos) + 140k benchmark |
| **🎙️ Voice Clone** | Biometric Acoustic Pitch & Vocoder Phase Analyzer | Fundamental frequency ($F_0$) variation, vocoder phase quantization (spectral flatness), high-frequency roll-off | ASVspoof 2021 + HiFi-GAN baseline |
| **📧 Phishing Email** | DistilBERT + RFC Header Heuristics | Spoofed sender domains, SPF/DKIM verification, credential harvesting pretexting, SHAP interpretability | Enron + Phishing corpus |
| **🌐 Malicious URL** | Random Forest Classifier + Heuristic Engine | Shannon entropy, typosquatting, suspicious TLDs (`.xyz`, `.top`), IP-host routing, destination obfuscation | **99.66% Acc** (PhishTank + Alexa 1M) |
| **🛡️ Network IDS** | Deep PyTorch Autoencoder ($7 \to 16 \to 8 \to 4 \to 8 \to 16 \to 7$) | Unsupervised reconstruction error (MSE) on flow duration, packet rates, and volumetric byte distributions | CIC-IDS2017 baseline (500k flows) |
| **⚡ Risk Fusion** | Bayesian Threat Aggregation | Dynamic weight-normalized multi-vector threat probability synthesis | Automated triage (`Critical`, `High`, `Low`) |

---

## ⚖️ Digital Forensics & Chain of Custody

deepSheild implements institutional-grade digital chain of custody for all ingested evidence:
- **Cryptographic Hashing**: Instant SHA-256 digest calculated at upload time to guarantee non-repudiation.
- **Immutable Audit Logging**: Every system action (`UPLOAD_EVIDENCE`, `RUN_DETECTION`, `TRIGGER_FUSION`, `CASE_CREATE`) generates a permanent row in the `AuditLog` table.
- **Chain of Custody UI**: Visual audit trail tracking analyst ID, action type, target ID, and UTC timestamps formatted for forensic admissibility.

---

## 💻 Tech Stack

- **Frontend**: Next.js 16 (App Router), React 19, TypeScript, Tailwind CSS v4, Lucide Icons, Axios.
- **Backend & ML**: FastAPI, Python 3.11, Pydantic v2, SQLAlchemy 2.0, PyTorch, Torchvision, Transformers (HuggingFace), Scikit-Learn, Librosa, MTCNN, OpenCV, SHAP.
- **Storage & Infrastructure**: PostgreSQL 15, Redis 7, Celery 5.4, Docker, Docker Compose.

---

## 🚀 Quick Start Guide

### Option 1: Multi-Container Docker Deployment (Recommended)

1. **Clone the repository**:
   ```bash
   git clone https://github.com/tellapallyakhil/deepshield.git
   cd deepshield
   ```

2. **Launch services with Docker Compose**:
   ```bash
   docker-compose up -d --build
   ```

3. **Open the platform**:
   - 🖥️ **SOC Analyst Dashboard**: [`http://localhost:3000`](http://localhost:3000)
   - 📖 **Interactive Swagger API Docs**: [`http://localhost:8000/docs`](http://localhost:8000/docs)
   - ⚡ **API Gateway**: [`http://localhost:8000`](http://localhost:8000)

---

### Option 2: Local Development Setup (Manual)

<details>
<summary>Click to view manual setup instructions</summary>

#### 1. Backend Service:
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

#### 2. Frontend Web Application:
```bash
cd frontend
npm install
npm run dev
```
</details>

---

## 🔑 Default Credentials

A default administrator analyst account is automatically seeded on first launch:

| Field | Value |
|---|---|
| **Username / Email** | `admin` *(or `admin@deepsheild.com`)* |
| **Password** | `admin123` |
| **Role** | `admin` (Full SOC Access) |

---

## 📡 API Gateway Reference

| Method | Endpoint | Description |
|---|---|---|
| `POST` | `/api/v1/auth/login` | Authenticates analyst and issues OAuth2 JWT bearer token |
| `GET` | `/api/v1/cases/stats/overview` | Retrieves live database SOC threat telemetry and scan metrics |
| `POST` | `/api/v1/cases` | Creates a new security investigation case |
| `POST` | `/api/v1/deepfake/upload` | Ingests video file and runs ViT + EfficientNet frame inference |
| `POST` | `/api/v1/voice/upload` | Ingests audio file and runs biometric vocoder pitch analysis |
| `POST` | `/api/v1/url/scan` | Analyzes URL using Random Forest lexical model and heuristic rules |
| `POST` | `/api/v1/email/analyze` | Scans email text & headers via DistilBERT NLP and RFC checks |
| `POST` | `/api/v1/network/analyze` | Evaluates network flow telemetry using PyTorch Deep Autoencoder |
| `POST` | `/api/v1/fusion/aggregate/{id}` | Calculates holistic case threat risk score across all evidence |
| `GET` | `/api/v1/forensics/case/{id}/chain-of-custody` | Returns cryptographic audit trail and evidence SHA-256 hashes |

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
│   └── requirements.txt     # Production dependencies
├── frontend/
│   ├── src/
│   │   ├── app/             # Next.js 16 App Router (Dashboard, Cases, Forensics, Login)
│   │   ├── components/ui/   # Accessible UI components (Tailwind v4)
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
