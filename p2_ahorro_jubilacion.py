# Crea un programa que ayude a una persona a calcular cuánto necesita ahorrar mensualmente para su jubilación. Solicita al usuario su edad actual, la edad a la que planea jubilarse y la cantidad deseada para la jubilación. Luego, calcula cuánto debe ahorrar mensualmente considerando un rendimiento anual esperado de la inversión. Utiliza la fórmula:
    # PMT = FV*r / ((1 + r)**n - 1) * (1 + r)**-t

# PMT es el pago mensual necesario.
# FV es la cantidad deseada para la jubilación.
# r es la tasa de interés mensual (rendimiento anual dividido por 12 y expresado en decimales).
# n es el número de pagos mensuales en la jubilación (años de jubilación multiplicados por 12).
# t es el número de años hasta la jubilación.

#Muestra el pago mensual necesario para alcanzar la meta de jubilación.

def calcular_pmt(FV, r, n, t):
    PMT = FV * r / ((1 + r)**n - 1) * (1 + r)**-t
    return PMT

FV = float(input("Ingresar la cantidad deseada para la jubilación: "))
r = float(input("Ingresar la tasa de interés mensual en decimales: "))
n = int(input("Ingresar el número de pagos mensuales en la jubilación: "))
t = int(input("Ingrese el número de años hasta la jubilación: "))

pago_m_n = calcular_pmt(FV, r, n, t)
print(f"Debers ahorrar ${pago_m_n:.2f} mensualmente para alcanzar la meta de jubilación.")
