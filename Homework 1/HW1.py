import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize

fun = lambda x: (x[0] - x[2])**2 + (x[1] + x[2] - 2)**2 + (x[3] - 1)**2 + (x[4] - 1)**2
cons = ({'type': 'ineq', 'fun':lambda x: x[0] + 3*x[1]},
        {'type': 'ineq', 'fun':lambda x: x[2] + x[3] - 2*x[4]},
        {'type': 'ineq', 'fun':lambda x: -x[0] + 2 * x[1] + 2})
bnds = ((-10, 10), (-10, 10), (-10,10), (-10, 10), (-10, 10))
res = minimize(fun, (1,1,1,1,1), method='SLSQP', bounds=bnds, constraints=cons)