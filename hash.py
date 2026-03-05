import hashlib

def hash(frase):
    h = hashlib.sha256()
    h.update(frase)
    print(h.hexdigest())


hash(rb'Qualquer palavra')