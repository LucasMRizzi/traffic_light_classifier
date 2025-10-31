# 🧠 Projeto classificação de semáforos com YOLO

Este projeto utiliza o modelo **YOLO (You Only Look Once)** para detectar objetos em imagens — neste caso, aplicado à detecção de semáforos.  
O objetivo é desenvolver, treinar e avaliar uma rede neural capaz de identificar padrões visuais com alta precisão.

---

## 📋 Sumário

- [1. Pré-requisitos](#1--pré-requisitos)
- [2. Estrutura do Projeto](#2--estrutura-do-projeto)
- [3. Como Rodar o Projeto](#3--como-rodar-o-projeto)
- [4. Dataset](#4-dataset)

---

## 1. 🧩 Pré-requisitos

Antes de iniciar, certifique-se de ter instalado:

- **Python 3.11+**
- **pip** atualizado
- **Virtualenv** (opcional, mas recomendado)
- **YOLOv8** (via Ultralytics)
- **PyTorch** compatível com sua versão do CUDA
- CUDA Toolkit instalado (necessário apenas se for usar GPU)
- Dependências listadas em `requirements.txt`

Instale as dependências com:
```bash
pip install -r requirements.txt
```

---

## 2. 📂 Estrutura do Projeto

```bash
├── data/
│   ├── README.md          # Instruções sobre onde obter os dados
│   ├── train/             # Imagens e labels de treino
│   ├── valid/             # Imagens e labels de validação
│   ├── test/              # Imagens de teste
│   └── data.yaml          # Configuração do dataset YOLO
│ 
├── notebooks/
│   └── model_train.ipynb   # Notebook de treinamento
│
├── src/
│   ├── detect.py          # Script de detecção
│   └── utils/             # Funções auxiliares
│
├── weights/
│   └── best.pt            # Resultado do treinamento
│
├── requirements.txt
├── .gitignore
└── README.md
```

---


## 3. 🚀 Como Rodar o Projeto

### 1 - Clone o repositório
```bash
git clone https://github.com/LucasMRizzi/traffic_light_classifier
cd nome-do-projeto
```
### 2 - Crie o ambiente virtual (recomendado)
```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```
### 3 - Instale as dependências
```bash
pip install -r requirements.txt

```
### 4 - Treine o modelo (opcional)
```bash
yolo task=detect mode=train model=yolov8l.pt data=data/data.yaml epochs=50
```

### 5 - Rodando o modelo
```bash
python src/video_recognizer.py
```

---

## 4. Dataset

Os arquivos de imagem não estão inclusos neste repositório.
Eles podem ser baixados no Google Drive:

👉 [Link para o Dataset](https://drive.google.com/drive/folders/1339TI4yWAzAqONhsjsg_7Dn-lC9qltqU?usp=sharing)  



