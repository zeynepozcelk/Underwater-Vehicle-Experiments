import pandas as pd

class PIDController:
    def __init__(self, kp, ki, kd):
        self.kp = kp
        self.ki = ki
        self.kd = kd
        self.prev_error = 0
        self.integral = 0

    def update(self, error, dt):
        self.integral += error * dt
        derivative = (error - self.prev_error) / dt
        control_output = self.kp * error + self.ki * self.integral + self.kd * derivative
        self.prev_error = error
        return control_output

# PID constants
P = 470
I = 100
D = 10
pid_controller = PIDController(P, I, D)

# Read data from file
file_path = '/path/to/Lab1_depth_time.txt'
df = pd.read_csv(file_path, delimiter='\t', header=None)
df.columns = ['Time', 'Target_Depth', 'Measured_Depth', 'PID_Result']

# Convert depths to cm
df['Target_Depth_cm'] = df['Target_Depth'] * 100
df['Measured_Depth_cm'] = df['Measured_Depth'] * 100

# Compute control signals
control_signals = []
for i in range(1, len(df)):
    dt = df['Time'][i] - df['Time'][i-1]
    error = df['Target_Depth'][i] - df['Measured_Depth'][i]
    control_signal = pid_controller.update(error, dt)
    control_signals.append(control_signal)

control_signals.insert(0, 0)
df['PID_Control_Output'] = control_signals
