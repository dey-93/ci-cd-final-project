try:
    from service import *  # reexporta si tienes paquete service
except Exception:
    def suma(a, b):  # fallback si no hay service
        return a + b
