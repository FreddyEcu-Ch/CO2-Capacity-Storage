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
    return BO_norm
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
def Co2densidad():
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
    engine = create_engine("sqlite:///CO2/CO2_EOR1.db")
    df = pd.read_sql_query("SELECT * FROM Datos", engine)
    df
    if df["Profundidad"].float > 2:
        df["Densidad_CO2"].float = 700
    else:
        df["Densidad_CO2"]= px(df["Profundidad"].float)
    return df["Densidad_CO2"]
def bachuprob():
    """
    Parameters
    :param densidad: kg/m3
    :param Rf: %
    :param OOIP: m3
    :param Bo_norm: By/Bn
    :return: Mt CO2
    """
    engine = create_engine("sqlite:///CO2/CO2_EOR1.db")
    df = pd.read_sql_query("SELECT * FROM Datos", engine)
    df
    df["Densidad_CO2"] = Co2densidad()
    BO_norm = Bo()
    df["Capacidad_CO2"] = df["Densidad_CO2"] * ((df["Rf"] * df["OOIP"])/BO_norm )
    return df

