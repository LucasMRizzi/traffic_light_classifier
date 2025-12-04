from ultralytics import YOLO


# 1. Carregue o modelo (pode ficar fora ou dentro, mas recomendo dentro)
# ... imports ...

def main():
    # Coloque sua lógica de treino aqui dentro
    model = YOLO('../weights/yolov8l.pt')  # ou o caminho do seu modelo

    results = model.train(
        data='../data/data.yaml',
        epochs=20,
        batch=8,
        imgsz=640,
        name='model_train_v2',
        device=0,  # Se tiver GPU
        workers=4  # O Windows aguenta workers se estiver no main block
    )


# 2. O BLOCO OBRIGATÓRIO PARA WINDOWS
if __name__ == '__main__':
    # Isso impede que os processos filhos rodem o treino recursivamente
    import multiprocessing

    multiprocessing.freeze_support()  # Opcional, mas boa prática no Windows

    main()