import numpy as np

def calculate(list):
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")
    a = np.array(arr)
    a=a.reshape(3,3)
    result = {
    'mean': [],
    'variance': [],
    'standard deviation': [],
    'max': [],
    'min': [],
    'sum': []
    }
    result["mean"] = [a.mean(axis=0).tolist(),a.mean(axis=0).tolist(),a.mean().tolist()]
    result["variance"] = [a.var(axis=0).tolist(),a.var(axis=1).tolist(),a.var().tolist()]
    result["standard deviation"] = [a.std(axis=0).tolist(),a.std(axis=1).tolist(),a.std().tolist()]
    result["max"] = [a.max(axis=0).tolist(),a.max(axis=1).tolist(),a.max().tolist()]
    result["min"] = [a.min(axis=0).tolist(),a.min(axis=1).tolist(),a.min().tolist()]
    result["sum"] = [a.sum(axis=0).tolist(),a.sum(axis=1).tolist(),a.sum().tolist()]
    return result
