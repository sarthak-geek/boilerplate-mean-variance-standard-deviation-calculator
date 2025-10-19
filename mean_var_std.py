import numpy as np

def calculate(list):
    if len(list) != 9:
        raise ValueError("List must contain nine numbers." )
    a = np.array(list)
    a = a.reshape(3,3)
    result = {
        'mean': [a.mean(axis=0).tolist(), a.mean(axis=1).tolist(), float(a.mean())],
        'variance': [a.var(axis=0).tolist(), a.var(axis=1).tolist(), float(a.var())],
        'standard deviation': [a.std(axis=0).tolist(), a.std(axis=1).tolist(), float(a.std())],
        'max': [a.max(axis=0).tolist(), a.max(axis=1).tolist(), float(a.max())],
        'min': [a.min(axis=0).tolist(), a.min(axis=1).tolist(), float(a.min())],
        'sum': [a.sum(axis=0).tolist(), a.sum(axis=1).tolist(), float(a.sum())]
    }
    return result
