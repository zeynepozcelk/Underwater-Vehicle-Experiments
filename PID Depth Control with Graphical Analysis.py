import pandas as pd
import matplotlib.pyplot as plt

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

# Plot data
fig, ax1 = plt.subplots(figsize=(12, 8))

# Plot depth data
ax1.plot(df['Time'], df['Measured_Depth_cm'], label='Measured Depth (cm)', color='b')
ax1.plot(df['Time'], df['Target_Depth_cm'], label='Target Depth (cm)', linestyle='--', color='r')
ax1.set_xlabel('Time (s)')
ax1.set_ylabel('Depth (cm)', color='b')
ax1.tick_params(axis='y', labelcolor='b')
ax1.legend(loc='upper left')
ax1.grid(True)

# Plot PID control output
ax2 = ax1.twinx()
ax2.plot(df['Time'], df['PID_Result'], label='PID Result', color='g')
ax2.set_ylabel('PID Output', color='g')
ax2.tick_params(axis='y', labelcolor='g')
ax2.legend(loc='upper right')

# Table of performance metrics
setpoint = 110
rise_time_threshold = setpoint * 0.9
Tr = df[df['Measured_Depth_cm'] >= rise_time_threshold].iloc[0]['Time'] if not df[df['Measured_Depth_cm'] >= rise_time_threshold].empty else None
Tp = df['Measured_Depth_cm'].idxmax() * df['Time'].diff().mean()
Mp = df['Measured_Depth_cm'].max()
ess = df.iloc[-1]['Measured_Depth_cm']
tolerance = 1.4
lower_bound = setpoint - tolerance
upper_bound = setpoint + tolerance
ts_data = df[(df['Measured_Depth_cm'] >= lower_bound) & (df['Measured_Depth_cm'] <= upper_bound)]
ts = ts_data.iloc[-1]['Time'] if not ts_data.empty else None
PO_percent = ((Mp - setpoint) / setpoint) * 100
MO = Mp - setpoint

table_data = {
    'Target (cm)': [setpoint],
    'Rise Time (s)': [Tr],
    'Peak Time (s)': [Tp],
    'Max Peak (cm)': [Mp],
    '% Overshoot': [round(PO_percent, 2)],
    'Steady State Error (cm)': [f"{ess:.1f}±{tolerance}"],
    'Settling Time (s)': [ts],
    'Max Overshoot': [round(MO, 2)]
}

table_df = pd.DataFrame(table_data)
table = plt.table(cellText=table_df.values, colLabels=table_df.columns, cellLoc='center', loc='bottom', bbox=[0, -0.4, 1, 0.3])
table.auto_set_font_size(False)
table.set_fontsize(8)

plt.subplots_adjust(left=0.2, bottom=0.5)
plt.title('Depth vs Time with PID Control')
plt.show()
