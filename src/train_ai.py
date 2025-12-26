import torch
import os

def load_model():
    model_path = "models/checkpoints/trained_model.pth"
    if os.path.exists(model_path):
        model = torch.load(model_path)
        model.eval()
        return model
    else:
        from torch import nn
        model = nn.Sequential(nn.Linear(6, 64), nn.ReLU(), nn.Linear(64, 2))
        return model
