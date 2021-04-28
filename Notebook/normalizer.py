def normalize(data, mean, std):
    z = (data - mean)/std
    return z
