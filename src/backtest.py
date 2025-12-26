import pandas as pd

def backtest(data, signals):
    balance = 1000
    for i, signal in enumerate(signals):
        if signal['action'] == "BUY":
            pnl = signal['target'] - signal['entry']
        else:
            pnl = signal['entry'] - signal['target']
        balance += pnl
    return balance
