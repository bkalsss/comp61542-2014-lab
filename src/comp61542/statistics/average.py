
def mean(X):
    n = len(X)
    if n > 0:
        return float(sum(X)) / float(len(X))
    return 0


def median(X):
    n = len(X)
    if n == 0:
        return 0
    L = sorted(X)
    if n % 2:
        return L[n / 2]
    return mean(L[(n / 2) - 1:(n / 2) + 1])

def mode(X):
    n = len(X) 
    if n == 0: 
        return [] 
    
    d = {} 
    for item in X: 
        if d.has_key(item): 
            d[item] += 1 
        else: 
            d[item] = 1
    
    m = [] 
    frequency = None 
    for key in d.keys(): 
        if frequency == None: 
            frequency = d[key] 
            m.append(key) 
        elif frequency < d[key]: 
            m = [] 
            frequency = d[key] 
            m.append(key) 
        elif frequency == d[key]: 
            m.append(key) 
    return m