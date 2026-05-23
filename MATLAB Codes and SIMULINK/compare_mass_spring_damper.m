% Load Python data
python_data = readmatrix('mass_spring_damper_python.csv');
t_python = python_data(:, 1);
position_python = python_data(:, 2);

% Load Simulink data
t_simulink = out.position_simulink.Time;
Position_simulink = out.position_simulink.Data;

% Plot comparison
figure
plot(t_python, position_python, 'b-', 'LineWidth', 2)
hold on
plot(t_simulink, Position_simulink, 'r--', 'LineWidth', 2)
yline(0.25, 'k:', 'LineWidth', 1)
legend('Python solve\_ivp', 'Simulink')
xlabel('Time (s)')
ylabel('Position (m)')
title('Mass Spring Damper System — Python vs Simulink')
grid on