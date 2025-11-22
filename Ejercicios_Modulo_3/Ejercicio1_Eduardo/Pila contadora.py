class Stack:
    def __init__(self):
        self.__stk = []

    def push(self, val):
        self.__stk.append(val)

    def pop(self):
        if not self.__stk:
            raise IndexError("La pila está vacía, no se puede hacer pop.")
        val = self.__stk[-1]
        del self.__stk[-1]
        return val


class CountingStack(Stack):
    def __init__(self):
        super().__init__()
        self.__counter = 0

    def get_counter(self):
        return self.__counter

    def pop(self):
        try:
            # intenta hacer pop en la clase padre
            value = super().pop()
            # si funciona, incrementa contador
            self.__counter += 1
            return value
        except IndexError as e:
            # manejo del error
            print("Error:", e)
            # evita que el programa truene
            return None


# Prueba
stk = CountingStack()

for i in range(100):
    stk.push(i)
    stk.pop()

# Intento de pop extra para demostrar manejo de errores
stk.pop()  # imprime el error pero no detiene el programa

print(stk.get_counter())