# Underwater Vehicle Experiments
This repository contains comprehensive documentation and detailed reports on underwater vehicle experiments focused on depth control applications using PID controllers. These experiments were meticulously conducted in the Electronics and Communications Engineering department at the University of Kocaeli, highlighting advanced control techniques and their practical implementations in underwater robotics.

## Experiments
### 1. Depth Control
This preliminary experiment involves controlling the depth of an underwater vehicle using a custom-built PID controller.

## Equipment and Software:
### Raspberry Pi 4 Model B:
- Quad-Core Broadcom BCM2711 A72 (ARM v8) 64-bit SoC
- 4GB LPDDR4 SDRAM
- Bluetooth 5.0, 2.4GHz/5.0GHz IEEE 802.11ac WiFi
- Gigabit Ethernet
- USB Ports: 2 x USB 2.0, 2 x USB 3.0
- 40-pin GPIO Header
- Dual micro HDMI ports (4Kp60 support)
- MicroSD card slot for OS and data storage
- Power input: 5V DC via USB-C connector (min 3A)
- Operating temperature: 0 to 50 °C

- Depth Sensor: Used to measure the depth of the underwater vehicle.
- Custom PID Controller: Implemented in Python to control the depth based on feedback from the depth sensor.

## Control Algorithm:
The PID controller is used to maintain the desired depth by adjusting the vehicle's buoyancy. The PID algorithm takes into account the proportional, integral, and derivative components of the error between the desired and measured depths.

### 2. PID Depth Control with Graphical Analysis
This experiment further explores the PID control mechanism applied to an underwater vehicle, assessing its effectiveness in maintaining a specified depth.

### Equipment and Software:
- Raspberry Pi 4 Model B: Same as described above.
- Depth Sensor: Same as described above.
- Custom PID Controller: Enhanced with data logging and graphical analysis capabilities.

### Experimental Design:
The experiment involves setting up the underwater vehicle with the depth sensor and the PID controller, then conducting tests to evaluate the vehicle's performance in maintaining the desired depth.

### Data Collection:
Data collected includes time, target depth, measured depth, and PID control outcomes. This data is then analyzed to evaluate the performance of the PID controller.

### Performance Metrics:
Performance indicators such as rise time, settling time, percentage overshoot, and steady-state error are evaluated.

### Graphical Analysis:
The depth control process is visualized using graphs and charts that illustrate the vehicle's behavior over time.

These experiments collectively provide valuable insights into the challenges and solutions associated with underwater depth control, offering a robust framework for further research and development in underwater robotics and control systems.
