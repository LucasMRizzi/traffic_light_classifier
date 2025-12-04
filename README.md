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
│   └── model_train_v2.pt            # Resultado do treinamento
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
Eles podem ser baixados pelo site:

👉 [Link para o Dataset](https://universe.roboflow.com/yololearning-nuega/traffic-lights-yulcv/dataset/1)

---

## 5. Resultados

Os experimentos realizados com a arquitetura atual demonstraram um desempenho moderado, indicando oportunidades para otimização futura.

**Métricas Gerais:** O modelo atingiu um pico de Precisão de aproximadamente 60%.

**Detecção de Instâncias:** Observou-se uma dificuldade na revocação (recall). O modelo tendeu a não identificar (Falsos Negativos) diversas instâncias de semáforos presentes nas imagens, especialmente em cenários mais complexos.

**Generalização:** Embora tenha detectado os objetos mais evidentes, a consistência da detecção variou, resultando na perda de objetos menores ou parcialmente obstruídos.

### Principais Desafios Observados

**Falsos Negativos:** O modelo deixou passar semáforos em condições de iluminação variável ou quando o objeto ocupava uma área pequena da imagem (low pixel density).

**Convergência:** O treinamento estagnou na faixa de 60% de precisão, sugerindo a necessidade de ajustes nos hiperparâmetros (learning rate, momentum) ou refinamento do dataset (data augmentation).



