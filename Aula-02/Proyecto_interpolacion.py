# importamos la interpolación de Langrange del módulo de interpolación de Scipy
from scipy.interpolate import lagrange
# importamos la librería Matplotlib con un alias
import matplotlib.pyplot as plt
# importamos la librería Numpy con un alias
import numpy as np
# importamos la librería Pandas con el alias pd, para realizar el dataframe
import pandas as pd

# Guardamos los valores a usar en vectores.
# Range of motion
beta = np.linspace(20, 180, 9, dtype = int)
beta = list(beta)
teta = np.linspace(170, 90, 9, dtype = int)
teta = list(teta)
porCycle = [5.6, 11.1, 16.7, 22.2, 27.8, 33.3, 38.9, 44.4, 50.0]
# optimized for Straightness
separator1 = ['!', '!', '!', '!', '!', '!', '!', '!', '!']
MinimumDeltaCy = [0.00001, 0.0004, 0.00027, 0.001, 0.004, 0.010, 0.023, 0.047, 0.096]
deltaV = [0.38, 1.53, 3.48, 6.27, 9.90, 14.68, 20.48, 27.15, 35.31]
Vx = [1.436, 1.504, 1.565, 1.611, 1.646, 1.679, 1.702, 1.717, 1.725]
Link1_2 = [2.975, 2.950, 2.900, 2.825, 2.725, 2.625, 2.500, 2.350, 2.200]
Link3_2 = [3.963, 3.925, 3.850, 3.738, 3.588, 3.438, 3.250, 3.025, 2.800]
LinkDeltaX_2 = [0.601, 1.193, 1.763, 2.299, 2.790, 3.238, 3.623, 3.933, 4.181]
# optimized for Constant Velocity
separator2 = ['!', '!', '!', '!', '!', '!', '!', '!', '!']
MinimumDeltaVx = [0.006, 0.038, 0.106, 0.340, 0.910, 1.885, 3.327, 5.878, 9.299]
deltaCy = [0.137, 0.274, 0.387, 0.503, 0.640, 0.752, 0.888, 1.067, 1.446]
Vx_b = [1.045, 1.124, 1.178, 1.229, 1.275, 1.319, 1.347, 1.361, 1.374]
Link1_2_b = [2.075, 2.050, 2.025, 1.975, 1.900, 1.825, 1.750, 1.675, 1.575]
Link3_2_b = [2.613, 2.575, 2.538, 2.463, 2.350, 2.238, 2.125, 2.013, 1.863]
LinkDeltaX_2_b = [0.480, 0.950, 1.411, 1.845, 2.237, 2.600, 2.932, 3.232, 3.456]

df = pd.DataFrame({'deltaBeta':beta, 'tetaStart':teta, "(%) of Cycle":porCycle, ' ' : separator1, 'Minimum delta Cy (%)': MinimumDeltaCy, 'Delta V (%)': deltaV, 'Vx': Vx, 'L1/L2': Link1_2, 'L3/L2': Link3_2, 'delatX/L2': LinkDeltaX_2, '  ' : separator1, 'Minimum delta Vx': MinimumDeltaVx, 'Delta Cy (%)': deltaCy, 'Vx ': Vx_b, 'L1/L2 ': Link1_2_b, 'L3/L2 ': Link3_2_b, 'delatX/L2 ': LinkDeltaX_2_b})
print(df)

# Calculamos la interpolacion de cada punto
# Range of motion
i_teta = lagrange(beta,teta)
i_porCycle = lagrange(beta,porCycle)
# optimized for Straightness
i_MinimumDeltaCy = lagrange(beta,MinimumDeltaCy)
i_deltaV = lagrange(beta,deltaV)
i_Vx = lagrange(beta,Vx)
i_Link1_2 = lagrange(beta,Link1_2)
i_Link3_2 = lagrange(beta,Link3_2)
i_LinkDeltaX_2 = lagrange(beta,LinkDeltaX_2)
# optimized for Constant Velocity
i_MinimumDeltaVx = lagrange(beta,MinimumDeltaVx)
i_deltaCy = lagrange(beta,deltaCy)
i_Vx_b = lagrange(beta,Vx_b)
i_Link1_2_b = lagrange(beta,Link1_2_b)
i_Link3_2_b = lagrange(beta,Link3_2_b)
i_LinkDeltaX_2_b = lagrange(beta,LinkDeltaX_2_b)

# Valor en el cual queremos interpolar
x = 55

# Evaluamos cada funcion en el punto x
# Range of motion
i_teta = i_teta(x)
i_porCycle = round(i_porCycle(x), 1)
# optimized for Straightness
i_MinimumDeltaCy = i_MinimumDeltaCy(x)
i_deltaV = round(i_deltaV(x), 2)
i_Vx = round(i_Vx(x), 3)
i_Link1_2 = round(i_Link1_2(x), 3)
i_Link3_2 = round(i_Link3_2(x), 3)
i_LinkDeltaX_2 = round(i_LinkDeltaX_2(x),3)
# optimized for Constant Velocity
i_MinimumDeltaVx = round(i_MinimumDeltaVx(x), 3)
i_deltaCy = round(i_deltaCy(x), 3)
i_Vx_b = round(i_Vx_b(x), 3)
i_Link1_2_b = round(i_Link1_2_b(x), 3)
i_Link3_2_b = round(i_Link3_2_b(x), 3)
i_LinkDeltaX_2_b = round(i_LinkDeltaX_2_b(x), 3)

for i in range(0, len(beta),1):
    #print(i)
    if beta[i] < x and beta[i+1] > x:
        # Range of motion
        beta.insert(i+1, x)
        teta.insert(i+1, i_teta)
        porCycle.insert(i+1, i_porCycle)
        # optimized for Straightness
        separator1.insert(i+1, '!')
        MinimumDeltaCy.insert(i+1, i_MinimumDeltaCy)
        deltaV.insert(i+1, i_deltaV)
        Vx.insert(i+1, i_Vx)
        Link1_2.insert(i+1, i_Link1_2)
        Link3_2.insert(i+1, i_Link3_2)
        LinkDeltaX_2.insert(i+1, i_LinkDeltaX_2)
        # optimized for Constant Velocity
        separator2.insert(i+1, '!')
        MinimumDeltaVx.insert(i+1, i_MinimumDeltaVx)
        deltaCy.insert(i+1, i_deltaCy)
        Vx_b.insert(i+1, i_Vx_b)
        Link1_2_b.insert(i+1, i_Link1_2_b)
        Link3_2_b.insert(i+1, i_Link3_2_b)
        LinkDeltaX_2_b.insert(i+1, i_LinkDeltaX_2_b)

print(' ')
df = pd.DataFrame({'deltaBeta':beta, 'tetaStart':teta, "(%) of Cycle":porCycle, ' ' : separator1, 'Minimum delta Cy (%)': MinimumDeltaCy, 'Delta V (%)': deltaV, 'Vx': Vx, 'L1/L2': Link1_2, 'L3/L2': Link3_2, 'delatX/L2': LinkDeltaX_2, '  ' : separator1, 'Minimum delta Vx': MinimumDeltaVx, 'Delta Cy (%)': deltaCy, 'Vx ': Vx_b, 'L1/L2 ': Link1_2_b, 'L3/L2 ': Link3_2_b, 'delatX/L2 ': LinkDeltaX_2_b})
print(df)

# Valor segmento rectilíneo
SegRect = 20

# Optimized for Straightness
# Calculo L2
LinkL_2 = round(SegRect/i_LinkDeltaX_2, 3)
# Calculo L3
LinkL_3 = round(i_Link3_2*LinkL_2, 3)
# Calculo L1
LinkL_1 = round(i_Link1_2*LinkL_2, 3)
# calculo eror
# Es = np.sqrt((LinkL_3**2)-((LinkL_1 + LinkL_2)**2))

print('')
print('Optimized for Straightness')
print('L2')
print(LinkL_2)
print('L3')
print(LinkL_3)
print('L1')
print(LinkL_1)

# Optimized for Constant Velocity
# Calculo L2
LinkL_2_b = round(SegRect/i_LinkDeltaX_2_b, 3)
# Calculo L3
LinkL_3_b = round(i_Link3_2_b*LinkL_2_b, 3)
# Calculo L1
LinkL_1_b = round(i_Link1_2_b*LinkL_2_b, 3)

print('')
print('Optimized for Constant Velocity')
print('L2')
print(LinkL_2_b)
print('L3')
print(LinkL_3_b)
print('L1')
print(LinkL_1_b)