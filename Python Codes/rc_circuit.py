import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# RC circuit parameters
R = 1000
C = 0.001
V0 = 5

time_span = [0, 5]

def rc_ode(t, V):
    dV_by_dt = -(V / (R * C))
    return dV_by_dt

solution = solve_ivp(rc_ode, [time_span[0], time_span[-1]], [V0])

plt.plot(solution.t, solution.y[0])
plt.axhline(y=0, color='gray', linestyle='--', linewidth=1)

plt.xlabel('Time (s)')
plt.ylabel('Capacitor Voltage (V)')
plt.title('RC Circuit Response')
plt.grid(True)

plt.show()
