---
title: "Coin picking robot"
tags: ["Altium", "Assembly", "Circuit Design", "Python"]
categories: ["Projects"]
github: "https://github.com/AP010307/ELEC-291-Coin-Picking-Robot"
weight: 1
---
[🔗 View on GitHub](https://github.com/AP010307/ELEC-291-Coin-Picking-Robot)
{{< figure src="top_view.jpg" alt="Robot and Remote" >}}
# Overview
I spearheaded a group of five people in an ELEC 291 project that the EFM8LB1 and ATMega32P microcontrollers to create a robot that is able to pick up 20 coins.

# Introduction
This project is the ultimatum of my ELEC 291 course, where my team was tasked with creating a robot that could pick up 20 coins. The robot was designed to be able to stay within a perimeter powered by AC signal while detecting and picking up coins using multipl solenoids. 

# Objective

The goal of this project is to build, program, and test a robot, capable of detecting and pick up coins, both autonomously and manually:    

- The project must utilize two microcontrollers (one for the robot and one for the remote). The two microcontrollers must be from different families. The list of MCUs included in the project 2 kit is as below:

    - **EFM8LB12** (C8051Fxxx family)
    - **ATMega328P** (AVR family)
    - **MSP430G2553** (MSP430 family)
    - **PIC32MX130** (PIC family)
    - **LPC824** (ARM Cortex-M0 family)


- **Both the robot and controller must be battery operated (AA and 9V)**

- **Metal detection**: using a 1mH conductor coil and other relevant electrical components to construct a Colpitts Oscillator, which will act as a metal detector. The robot must be able to detect all Canadian coins in circulation.

- Coin-picking mechanism consists of two micro servo motors and an electromagnet. The robot must be able to pick up all Canadian coins in circulation and deposit them in a container situated at the front of the robot.
- **The robot must be programmed in C**
- **Perimeter detection**: In automatic mode, the robot must operate within a 1m x 0.5m perimeter. The perimeter consists of a long rectangular wire carrying an AC signal either from a function generator or a LM-555 timer circuit. The robot must be able to detect and stay within the perimeter at any given point throughout the automatic process.
- **Automatic mode**: The robot must be able to autonomously pick up 20 coins scattered randomly within the perimeter, without having four wheels leaving said perimeter. Upon completion, the robot stopped for further commands.
- **Manual mode**: The robot must be able to pick up coins using a remote control. The remote control must be able to control the robot's movement and coin-picking mechanism. The remote control must also be able to stop the robot at any given point.
- **Remote control**: must include an LCD to display the signal “strength” coming from the coin detector, as well as a speaker that beeps whenever a coin is detected. The pitch of the speaker must correspond to the strength of the signal coming from the metal detector. A joystick is included in the project 2 kit, although any other suitable control methods are also allowed.

# Investigation
## Idea Generation

Ideas were generated and tackled base on design specifications and objectives listed above. For this project, the keys areas to focus on were:
-	Succinct integration of two different micro controller families via the C.
-	Discrete MOSFETs to drive motor logic.
-	Metal and perimeter detector circuits and logic.
-	Radio communication via the JDY-40 radio.
-	Remote must have LCD display, speaker and joystick.

Once project objectives were identified, our group investigated each aspect as a whole and attempted to come up with a solution. Progress was monitored through regular check-ins and testing to ensure succinct integration at the end.
## Investigation Design
- Our group’s first objective was deciding which microcontroller unit to use. At the end, we settled with the ATMEGA328P for the controller, and the EFM8 (included in our project 1 kit) for the robot. This decision stemmed from our extensive experience with both MCUs from previous labs and projects, as well as sufficient documentation to both (1)(2).
- For the metal detector circuit, there are multiple designs available on the Project 2 lecture slides (3). Our team built and tested all the designs and eventually settled the Colpitts Oscillator with discrete CMOS inverter. This set up ensured the most stable frequency output when a coin was detected, as well as being ergonomic enough to be incorporated into the overall robot design.

## Data Collection:
Dedicated procedures to test the metal and perimeter detector were carried out to ensure succinct operation. 
 - By placing the robot at various position and distance relative to the perimeter, the “ambient” perimeter frequency of the perimeter detector was consistently found to be around 56600Hz. We set this as our reference value. The frequency picked up by the metal detector when different types of coins were detected varied. Each coin type had a “signature” range of frequency. We later take the average of each coin type’s frequency and their difference from the ambient metal detector frequency (i.e. when nothing is in the vicinity of the metal detector) as a base to drive our metal detector logic.

 {{< figure src="frequency.jpg" alt="Different and mean frequencies of each type of coin" >}}

## Data Synthesis:
The data found regarding the frequency generated by both the metal and perimeter detector under different conditions served as an important foundation for the robot logic. The accuracy of data collected were further verified using an oscilloscope and excel arithmetic. Via C, we hardcoded the baseline frequency for both detectors. These baseline values directly control the motor that moves the robot around, as well as the coin-picking mechanism (both the servo “arm” and the electromagnet). Once sufficient data was achieved, it all came down to simple arithmetic and if-else statements in the C-language to drive the robot logic.

## Analysis of result:
Through troubleshooting and calibration, we mitigated errors due to hardware limitations and environmental factors with regards to both the metal and perimeter detector. Our analysis confirmed both apparatuses operating within acceptable error margins and frequency data used as baseline values to drive the robot logic resulted in accurate, consistent and predictable robot behavior. 

# Design

## Hardware
The robot and remote controller's hardware are as follows:
#### Robot
{{< figure src="just_robot.jpg" alt="Robot" >}}
| No. | Components         | Quantity |
|-----|--------------------|----------|
| 1   | EFM8LB12           | 1.0      |
| 2   | LTV846             | 2.0      |
| 3   | LM358P             | 1.0      |
| 4   | LM7805             | 2.0      |
| 5   | MCP1700            | 1.0      |
| 6   | FQU8P10            | 5.0      |
| 7   | FQU13N06LTU        | 6.0      |
| 8   | 1N4148             | 1.0      |
| 9   | M8275-ND           | 3.0      |
| 10  | QRD114             | 2.0      |
| 11  | MBR150             | 2.0      |
| 12  | Capacitor 10µF     | 2.0      |
| 13  | Capacitor 1nF      | 1.0      |
| 14  | Capacitor 10nF     | 1.0      |
| 15  | Capacitor 100nF    | 2.0      |
| 16  | Resistor 330Ω      | 2.0      |
| 17  | Resistor 1KΩ       | 7.0      |
| 18  | Resistor 4.7KΩ     | 1.0      |
| 19  | Resistor 100KΩ     | 4.0      |
| 20  | Resistor 330KΩ     | 2.0      |

{{< figure src="robot_block_diagram.jpg" alt="Robot block diagram" >}}
#### Remote controller

{{< figure src="left_view.jpg" alt="Remote" >}}

| No. | Components         | Quantity |
|----|--------------------------|----------|
| 1  | ATMega328P                | 1        |
| 2  | CEM-1203(42)                   | 1        |
| 3  | FT230XSR| 1        |
| 4  | FQU13N06LTU                   | 1        |
| 5  | JDY-40       | 1        |
| 6  | MCP1700            | 6        |
| 7  | 1N4148         | 1        |
| 8  | QYF-860            | 1        |
| 9  | Resistor 2KΩ           | 1        |
| 10 | Resistor 1KΩ                | 1        |
| 11 | Push buttons          | 2        |
| 12 | Capacitor 0.1µF            | 1        |
| 13 | Capacitor 100µF             | 1        |

The robot system was composed of multiple functional components: the robot chassis motor drive, microcontroller, metal and perimeter detectors, wireless radio communication and coin-picking mechanism. Each subsystem was designed by applying principles of embedded systems, A/D design circuit design and power management.

**Power regulation:**
- Design approach: The robot uses 4x AA batteries (6V) to power the motors and optocouplers, and a 9V battery regulated to 5V by an LM7805 and an MCP1700 for 3.3V.

- LM7805: provides 5V for the EFM8 and sensors.
- MCP1700: provides 3.3V for JDY-40 and microcontroller
- Microcontroller system:
1. Robot MCU – EFM8:
- 4 PWM digital outputs for motor control, UART + SET pins for JDY-40 communication, 1 digital input for metal detector, and 4 analog inputs for perimeter detectors
2. Remote MCU – ATMEGA328:
-	6 digital outputs for LCD, 2 analog inputs for joystick, 1 digital output for speaker, 3 UART pins for JDY-40
- Motor driver: H-bridge and optocouplers
-	2 discrete H-bridges, each consists of N-MOS and P-MOS transistors driven by optocouplers (LTV-847), control 2 DC motors by isolation motor power circuitry from the logic-level control.  
3. Metal detector:
-	A Colpitts Oscillator with discrete CMOS inverter built from discrete components.
-	Powered at 5V
-	The frequency shift when metal is in the vicinity is detected by the MCU
4. Perimeter detectors:
-	A peak detector circuit, whose signal is amplified using an Op-Amp.
-	Two were put perpendicular to each other at the front of the robot chassis for all-direction sensitivity
-	Output is fed to analog pins of the EFM8 for perimeter detection logic
5. Radio communication: JDY-40 radio pair
-	Uses RXD, TXD and SET pins for serial communication between robot and remote.
-	Powered by 3.3 V and communicates at 9600 baud
6. Joystick, speaker and LCD (remote):
-	Joystick: 2-axis analog potentiometer-type joystick connected to 2 analog inputs
-	LCD: standard 14-bit display driven by MCU digital outputs
-	Speaker: generates PWM audio cues via a single digital output
7. Coin-picking mechanism:
-	Utilizes an electromagnet, servo motors and chassis-integrated basket to pick up metal coins. 



{{< figure src="remote_block_diagram.jpg" alt="Robot block diagram" >}}
## Standard Operating Procedure
Our team began with a structured engineering approach to ensure each subsystem was reliably tested and validated before moving on to subsequent phases of the project. First, we focused on the hardware: we assembled the robot chassis (wheels, motors, coin picking assembly, electromagnet, inductor coils for metal and perimeter detector and basket), and tested the key components—such as the Colpitts oscillator and simple perimeter detector circuits, both microcontrollers (ATMEGA328 and EFM8), JDY-40 radios—to confirm they functioned correctly. By establishing a stable hardware baseline, we minimized the risk of falsely attributing errors during software development to hardware issues.

## Requirements and Constraints

We gathered requirements by discussing baseline robot operations based on the outlined requirements, carefully examining the lecture slides and reviewing relevant best practices for designing and operating a multi-pronged system such as this project. From these activities, we identified the following needs and constraints:
- Streamlined controls during manual mode: the remote (both in terms of hardware and software) must be designed to allow for intuitive and ease of control during manual operations. Steps must be made to always allow for smooth and accurate controls with little interruptions, glitches or delay.
- 	Optimized robot logic during automatic operation: the robot must be able to perform multiple tasks simultaneously at any given point. This emphasizes the need for a clear logic flow that will allow for optimal performance and ease of debugging.
- Succinct integration between automatic and manual mode: The operator must be able to switch between automatic and manual mode at any given time. Once in automatic mode, the robot must strictly adhere to the base requirements of this project (i.e. stays withing the perimeter, automatically detects and picks up coin). In addition, after the 20 coins have been picked up during the automatic process, the robot should halt and awaits further instructions from the operator.
- Relevant Information Display: The remote should (at the bare minimum) display the signal strength based on which type of coins are detected. The signal strength must also be represented by an audio cue via a speaker.
By systematically identifying and documenting these needs, we ensured our design choices directly addressed user requirements and practical constraints from the outset, helping guide all subsequent design and development efforts.

## Solution Generation
Our team generated solution systematically and took into consideration various methods to address the project’s core requirements. We started by investigating different hardware and software configurations to deal with the robot’s various operational requirements.
1. **Controls:**
-   We opted for a simple, 2-axis control via the provided joystick when it comes to the movement of the robot. 
- The robot arm can be activated by pressing down on the joystick
- 	Toggling between manual and automatic mode can be done via a pushbutton.

2. **Radio communication between robot and remote:**
- The ATMEGA328 microcontroller had several built-in ADC input pins, which, when connected to the joystick, can translate its movement into ADC signal and then to voltage. We then programmed the movement of the robot by figuring out the joystick’s “dead zone” and finetuning it to fit with the H-bridge logic, which is then used to move the robot.

3. **Software Implementation:**
-	Our team decided to drive the robot’s logic by imbedding different parameters as presets. From the frequency picked up by the perimeter and metal detector, to the text command signals sent and received from the robot to the remote, we were able to systematically work out the robot’s core operation via simple while loops and if-else statements. This greatly enhanced the efficiency of our workflow, allowed for ease of debugging and optimized the robot’s performance and accuracy.

## Solution Evaluation
After potential solutions were generated, we evaluated each of them based on accuracy, ease of implementation and how well each idea interacts with one and another in the context of this project. Our evaluation criteria included:
-	**Hardware reliability**: assuring an ergonomic, neat and efficient circuit design that minimizes errors and allows for easier modification and troubleshooting, as well as succinct integration with software.
-	**Software efficiency**: ensuring an optimal and logical code flow that once again highlights the need for ease of troubleshooting and modification.
-	Efficient and predictable robot operation.


## Key Findings:
Although a simple control scheme and clear logic-based code fast-tracked the development of our design, we encountered multiple hiccups regarding to the communication between the robot and remote, which caused unpredictable robot movements, delays and crashes. We eventually narrowed down the cause of the issue: the radio communication received by the robot from the remote were somehow being offset. To be more specific:
- For example, during manual operation, when the robot is commanded to move forward, the operator moves the joystick forward, which will send a series of signal to the robot, the continuous signal looks something like this: “!FN!FN!….” The software of the robot was supposed to only grab “FN”, which was the valid command for “forward neutral”, but sometimes, it picked up “!F”, which was a false command based on our existing logic. This happened consistently for other commands as well, causing the robot to behave unpredictably. We were able to fix this issue by hardcoding the invalid commands (i.e. “!F”, etc.) as valid instructions. This fixed the issue, while maintaining the overall code efficiency and logic flow:

{{< figure src="codefixing.jpg" alt="Expanding parameter for bug fixing" >}}

## Software
1. **Slave code:**
-	Servos control: Implemented in Timer5_ISR, creating PWM signals with a 20ms period
-	Sensor integration:
  -	Metal detector: coins are detected via frequency shift
  -	Perimeter detectors: voltage threshold logic triggers a perimeter flag
-	Movement control:
  - Motor logic implemented via move_robot() function; encoded movement commands include:
    - “FN”: Forward (2-wheels moving forward), “BN”: Backwards (2-wheels moving backward), “HL” / “HR”: Hard-left, Hard-right (1-wheel moving forward, other backward), “FL” / “FR”: Gradual-left, Gradual-right (Only one wheel moving forward), BL” / “BR”: Back-left, Back-right (Only one wheel moving backward) and “ST”: Stop
-	Coin-picking mechanism:
  -	Servos_magnet() executes a defined range of motion sequence to pick up coins upon detection
- Wireless communication:
  - Slave-to-master transmits coin data types (“!DO” - Dollar, “!TW” – 2 Dollars, “!NI” – Nickel, etc.)
  -	“TO” – toggles between manual and automatic modes
  -	“PU”  - triggers the coin pick-up sequence
  - Unknown commands are handled (see Key findings, above)
- Automatic mode logic:
	- Moves forward by default
  -	If perimeter is detected, triggers perimeter_flag, then executes a range of motion moving backward then turning right (the degree of turn is randomized)
  - If metal is detected, uses frequency difference baseline to:
-	Detect presence of coin (triggers coinflag); Classify coin types (coin_tier); Broadcast coin classification to master (remote); Activate servos_magnet() to collect coin
-	Coin collection is hardcoded to 20. After 20 pick-ups, the robot stops. Note that the robot has no means to detect a successful pick-up. It counts every activation of the coin-picking assembly as an attempt.
- Manual mode logic:
 - In manual mode, commands are received wirelessly and processed directly
 - “PU” initiates the pick-up sequence
 - Directional and stop commands are passed to move_robot()
2. **Master Code:**
  - Core features:
    - Joystick-based control: reads analog joystick input to send movement commands.
    -	Mode toggle: a pushbutton to toggle between automatic and manual mode by sending “!TO” and waits for “!TD” / “!TF confirmation
    -	Pressing down on the joystick to send “!PU” to activate the coin collection sequence
  -	JDY-40 communication:
    - Sends commands with a “!” header (e.g., “!FN”, “!ST”, “!PU”, etc.)
    -	Receives coin types identifiers from the robot (“DI”, “QU”, “NI”, “TW”, “DO”) and toggles “TF” from the robot
  -	Speaker feedback:
    - Uses Timer0 interrupts to generates tones with different frequencies based on coin type:
  -	LCD feedback:
    -	Two-line LCD display:
        -	Current mode (“Toggle On/Off”) and coin strength
        -	Display and updates joystick command (e.g. Forward, etc.)

# Solution assessment
-	The robot was tested over 20 independent trials across various coin placement within the perimeter
-	Consistency of successful number of coins pick up per run remained at 18-19 out of 20 coins (± 1)
-	List of performed tests and observations:

| Test                             | Expected Outcome                             | Observed Outcome                                                                 | Pass/Fail        |
|----------------------------------|----------------------------------------------|----------------------------------------------------------------------------------|------------------|
| Coin detection (static and moving) | Coin correctly identified and picked up      | Coin detection is 100% functional, but hardcoded movement after pickup only allowed for 80–90% success | Pass (Partial)   |
| Boundary detection               | Robot reroutes away from the perimeter       | Correct response 100% of the time                                               | Pass             |
| Remote toggle and command response | Mode toggles + joystick driving              | Works reliably with LCD feedback; minor inconsistency with auto/manual toggle   | Pass (Partial)   |
| Coin classification              | Correct sound + LCD                          | All coin types correctly identified                                              | Pass             |


# Conclusion and Reflection
This project was a great learning experience in hardware design, firmware development, and time management. Using two family of microcontrollers required a lot of planning, testing and attention to details as well as a lot of debugging. I learned the use of makefiles, code initialization and the importance of coding sparingly and efficiently. I also learned the importance of clear hardware design and wiring as it made the debugging process much easier. I also learned the importance of testing and validating each subsystem before moving on to the next phase of the project. This helped us to identify and fix issues early on, rather than waiting until the end of the project to find out that something was not working. 

I was also really proud of the team perserverance and dedication to the project. Despite having both technical difficulties when integrating the radio communication and some communication issues within the team especially at the end when we also had final exams, we were able to come together, push through till the final hours of the project and delivered an product that was worthy of pads on the back. 

# Acknowledgements
I want to thank my team members, Jackson Rockford, Matthew Yeun, Harry Nguyen and Adrian Chua for their hard work and dedication to the project. I also want to thank the ELEC 291 instructor, Jesus Calvino-Fraga for his guidance and support throughout the project.
