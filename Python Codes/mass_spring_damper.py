import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# System parameters
M = 1
K = 4
F = 1

# Time settings
time_span = [0, 10]
t_eval = np.linspace(0, 10, 1000)

# Initial conditions
y0 = [0, 0]

def msd_ode(t, y, c):

    x1 = y[0]
    x2 = y[1]

    dx1_by_dt = x2
    dx2_by_dt = (F - x2*c - K*x1) / M
    return [dx1_by_dt, dx2_by_dt]

# Damping cases
cases = [
    (0.5, "Underdamped"),
    (4, "Critically Damped"),
    (8, "Overdamped"),
    (0, "NO Damping")
]


fig, axes = plt.subplots(2, 1, figsize=(10, 8))


for c, label in cases:

    solution = solve_ivp(msd_ode,time_span,y0,t_eval=t_eval,args=(c,))

    axes[0].plot(solution.t, solution.y[0], label=label)

    axes[1].plot(solution.t, solution.y[1], label=label)


x_ss = F / K
axes[0].axhline(x_ss, linestyle='--', label=f'Steady State = {x_ss} m')

axes[0].set_title('Mass-Spring-Damper Position Response')
axes[0].set_xlabel('Time (s)')
axes[0].set_ylabel('Position x(t) [m]')
axes[0].grid(True)
axes[0].legend()

axes[1].set_title('Mass-Spring-Damper Velocity Response')
axes[1].set_xlabel('Time (s)')
axes[1].set_ylabel('Velocity x_dot(t) [m/s]')
axes[1].grid(True)
axes[1].legend()

plt.tight_layout()
plt.show()

# Export underdamped case for comparison
solution_ud = solve_ivp(msd_ode, time_span, y0, t_eval=t_eval, args=(0.5,))
np.savetxt('msd_underdamped_python.csv',
           np.column_stack([solution_ud.t, solution_ud.y[0]]),
           delimiter=',',
           header='time,position')
