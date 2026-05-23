% Load Python data
python_data = readmatrix('thermal_python.csv');
t_python = python_data(:, 1);
T_python = python_data(:, 2);

% Load Simulink data
t_simulink = out.T_simulink.Time;
T_simulink = out.T_simulink.Data;

% Plot comparison
figure
plot(t_python, T_python, 'b-', 'LineWidth', 2)
hold on
plot(t_simulink, T_simulink, 'r--', 'LineWidth', 2)
yline(25, 'k:', 'LineWidth', 1)
legend('Python solve\_ivp', 'Simulink', 'T\_ambient = 25°C')
xlabel('Time (s)')
ylabel('Temperature (°C)')
title('Thermal Decay — Python vs Simulink')
grid on