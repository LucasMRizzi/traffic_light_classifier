# 📁 Pasta de Dados (`data/`)

Esta pasta **não contém as imagens** diretamente por questões de tamanho e versionamento no Git.

## 🖼️ Onde encontrar os arquivos de imagem

Os conjuntos de dados utilizados neste projeto estão disponíveis em:

- **Google Drive:** [link para o dataset](https://drive.google.com/drive/folders/1339TI4yWAzAqONhsjsg_7Dn-lC9qltqU?usp=sharing)  
- **Roboflow:** [link para o dataset](https://universe.roboflow.com/yololearning-nuega/traffic-lights-yulcv/dataset/1)  

## 📦 Estrutura esperada

Quando baixados, os arquivos devem seguir a seguinte estrutura dentro de `data/`:
```bash
data/
├── train/
│ ├── images/
│ └── labels/
├── valid/
│ ├── images/
│ └── labels/
├── test/
│ ├── images/
│ └── labels/
└── data.yaml
```
> ⚠️ **Importante:**  
> Certifier-se de que os caminhos nos arquivos `.yaml` do YOLO apontem corretamente para estas pastas antes de treinar o modelo.
