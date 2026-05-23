import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Thermal system parameters
K = 0.1
T0 = 100
T_ambient = 25

time_span = [0, 50]

def thermal_decay_ode(t, T):
    dT_by_dt = -K * (T-T_ambient)
    return dT_by_dt

t_eval = np.linspace(0, 50, 500)

solution = solve_ivp(thermal_decay_ode,[time_span[0], time_span[-1]],[T0],t_eval=t_eval)

plt.plot(solution.t, solution.y[0])
plt.axhline(y=T_ambient, color='gray', linestyle='--', linewidth=1)

plt.xlabel('Time (s)')
plt.ylabel('Temperature (C)')
plt.title("Thermal system response")
plt.grid(True)

plt.show()

np.savetxt('thermal_python.csv',
           np.column_stack([solution.t, solution.y[0]]),
           delimiter=',',
           header='time,temperature')
