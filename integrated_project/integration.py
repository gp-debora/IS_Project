import os
import sys
from PIL import Image
import torch
from torchvision import transforms

# Adiciona o caminho para o GROMA e LION
sys.path.append(os.path.abspath("Groma"))
sys.path.append(os.path.abspath("JiuTian-LION"))

from groma.eval.run_groma import run_groma_inference
from ram.models.tag2text import tag2text
from ram.inference import inference_tag2text

# ==== Caminhos ====
IMAGE_PATH = "integrated_project/test_images/teste.jpg"
DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# ==== LION ====

def run_lion_inference(image_path):
    print("==> LION inference started")

    # Carrega modelo
    checkpoint_path = "JiuTian-LION/ram/models/ram_swin_large_14m.pth"
    model = tag2text(pretrained=False)
    model.eval()
    model = model.to(DEVICE)
    state_dict = torch.load(checkpoint_path, map_location=DEVICE)
    model.load_state_dict(state_dict, strict=False)

    # Transforma a imagem
    transform = transforms.Compose([
        transforms.Resize((384, 384)),
        transforms.ToTensor(),
        transforms.Normalize([0.485, 0.456, 0.406],
                             [0.229, 0.224, 0.225])
    ])

    # Carrega e transforma a imagem
    image = Image.open(image_path).convert("RGB")
    image_tensor = transform(image).unsqueeze(0).to(DEVICE)

    # Executa inferência
    tags, _, caption = inference_tag2text(image_tensor, model)
    print(f"[LION] Tags: {tags}")
    print(f"[LION] Caption: {caption}")
    return tags, caption

# ==== Execução ====
if __name__ == "__main__":
    if not os.path.exists(IMAGE_PATH):
        raise FileNotFoundError(f"Imagem não encontrada: {IMAGE_PATH}")

    print("Iniciando integração dos modelos LION e GROMA...")
    lion_tags, lion_caption = run_lion_inference(IMAGE_PATH)
    
    # GROMA - Usa a função importada
    groma_output = run_groma_inference(IMAGE_PATH, query="Describe the image.")

    print("\n==== Resultado Final ====")
    print("LION Tags:", lion_tags)
    print("LION Caption:", lion_caption)
    print("GROMA Output:", groma_output)
