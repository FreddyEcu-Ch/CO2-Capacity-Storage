from scipy.stats import norm
import numpy as np
import sympy as sym
import pandas as pd
from sqlalchemy import create_engine
#Distribución normal Bo
def Bo():
    BO_norm = norm.rvs(loc=1.5, scale=0.5, size=3)
    BO_norm = np.where(BO_norm < 1, 1, BO_norm)
    BO_norm = np.where(BO_norm > 2, 2, BO_norm)
    BO_norm = pd.DataFrame(BO_norm)
    BO_norm["Bo"]=BO_norm
    return BO_norm["Bo"]
#Funciones càlculo de capacidad de almacenamiento CO2
def bachu(densidad, Rf, OOIP, Bo):
    """
    Parameters
    :param densidad: kg/m3
    :param Rf: %
    :param OOIP: m3
    :param Bo: By/Bn
    :return: Mt CO2
    """
    Mco2=densidad * ((Rf * OOIP) / Bo)
    return Mco2
def Co2densidad(df):
    # INGRESO , Datos de prueba
    xi = np.array([0, 0.1, 0.2,0.3, 0.55, 0.66, 0.74,0.87, 0.9, 1.11, 1.5,1.6,1.7,1.9, 1.98,2.1, 2.2,2.3,2.4,2.47, 2.5])
    fi = np.array([0,20,40, 72,140,242, 410, 550, 570,625, 671,680,690,700,700,700,700,700,700,700,700 ])
    n = len(xi)
    x = sym.Symbol('x')
    polinomio = 0
    divisorL = np.zeros(n, dtype=float)
    for i in range(0, n, 1):
        # Termino de Lagrange
        numerador = 1
        denominador = 1
        for j in range(0, n, 1):
            if (j != i):
                numerador = numerador * (x - xi[j])
                denominador = denominador * (xi[i] - xi[j])
        terminoLi = numerador / denominador

        polinomio = polinomio + terminoLi * fi[i]
        divisorL[i] = denominador
    # simplifica el polinomio
    polisimple = polinomio.expand()

    # para evaluación numérica
    px = sym.lambdify(x, polisimple)
    df["densidad"] = 700
    return df["densidad"]
def bachuprob(df):
    df["densidad"]= Co2densidad(df)
    df["Bo_Norm"]= Bo()
    df["capacidad"]= df["densidad"]*((df["rf"]) * df["ooip"]) / df["Bo_Norm"]
    return df
def zhoca(df):
    df["Percentiles"]=[10, 50, 90]
    df["E"]=[0.1, 0.5, 0.9]
    df["densidad"] = Co2densidad(df)
    df["Bo_Norm"] = Bo()
    df["Capacidad"]= df["ooip"] * df["densidad"] * df["Bo_Norm"] * df["E"]
    return df
