from src.data_loader import load_data
from src.feature_engineering import generate_features
from src.train_ai import load_model
from src.signal_generator import generate_signal
from src.telegram_bot import send_signal

def main():
    data = load_data()
    features = generate_features(data)
    model = load_model()
    signal = generate_signal(model, features)
    send_signal(signal)

if __name__ == "__main__":
    main()
