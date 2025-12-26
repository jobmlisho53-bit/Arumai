def generate_features(data):
    data['hl_range'] = data['High'] - data['Low']
    data['oc_change'] = data['Close'] - data['Open']
    features = data[['Open', 'High', 'Low', 'Close', 'hl_range', 'oc_change']]
    return features
