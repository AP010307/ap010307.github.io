---
title: "Signal Generator"
date: "2025-03-08T16:46:16-08:00"
draft: false
tags: ["hugo", "PaperMod"]
categories: ["Projects"]
weight: 4
---
| **Schematics** | **PCB_layout** |
|------------------------------|--------------------------------|
| ![Schematics](/image/PCB_schematics.png) | ![PCB layout](/image/PCB_layout.png) |


  
  **PCB_3D**  
  ![PCB 3D](/image/PCB_3D.png)


# Overview
A signal generator PCB created using KiCad.


# Introduction
This project was my introduction to PCB design using KiCad. Provided with a schematics, I created a square-wave signal generator that its frequency and gain can be adjusted using multiple potentiometers.

# Objective
The objective of this project was to learn how to design a PCB using KiCad and to understand the basic concepts of signal generation. The project also taught me to use different circuit testing equpments such as oscilloscope and multimeter. Lastly, I was introduced to SMD components, bill of materials and how to solder these components onto the PCB.


# Design

## Hardware
The project is purely a hardware project, with the following components:
### Bill of Materials
| Part Number          | Reference Designator(s)                      | Quantity |
|----------------------|---------------------------------------------|----------|
| NE555DR             | U1                                          | 1.00     |
| AD8039ARZ          | U2                                          | 1.00     |
| LM7805MPX          | U3                                          | 1.00     |
| MAX889SESA+        | U4                                          | 1.00     |
| PJ-002A            | J1                                          | 1.00     |
| DMN10H700S-7       | Q1                                          | 1.00     |
| CMD17-21SRC        | "+5V LED1, -5V LED1, +15V LED1, Signal LED1" | 4.00     |
| PV36W104C01B00     | "Freq_Adj1, Gain_Adj1, Gain_Adj2, Offset_Adj1" | 4.00     |
| 5002 Test Point    | -                                           | 10.00    |
| T491C106K025AT     | C2, C12, C13, C17, C18                      | 5.00     |
| C0805C103K3RACTU   | C3, C4, C6, C7, C10, C11, C14, C15, C19, C20 | 11.00    |
| C0805C220K3GACTU   | C5, C9                                      | 2.00     |
| RMCF0805ZT0R00     | R14, R20                                    | 2.00     |
| ESR10EZPJ151       | R10, R17, R21                               | 3.00     |
| RC0805FR-07649RL   | R15                                         | 1.00     |
| RC0805JR-071KL     | R1, R2, R3, R9                              | 4.00     |
| RC0805FR-071RL     | R4, R5                                      | 2.00     |
| RC0805FR-0710RL    | R13                                         | 1.00     |
| RC0805FR-07100RL   | R8                                          | 1.00     |
| RC0805FR-0710KL    | R6, R7, R12                                 | 2.00     |
| RT0805BRD0724K9L   | R11                                         | 1.00     |
| RC0805FR-07100KL   | R18, R19                                    | 2.00     |
| RC0805FR-07210KL   | -                                           | 1.00     |
| QPC02SXGN-RC       | for JP1                                     | 1.00     |
| PRPC002SACN-RC     | JP1                                         | 1.00     |
| BZT52C3V3-7-F      | D1                                          | 1.00     |

### Setup and Configuration
The circuit was powered by a 15V barrel jack and being regulated by a LM7805 voltage regulator to output a 5V source for all the ICs.

![Power Supply](/image/PS.png)


The NE555 timer IC, when put in the astable configuration, had a default frequency of the output signal given by:

                      f = 1/T = 1.44/((R_A + 2*R_B)*C)

where R_B is a 100k ohm potentiometer, R_A is a 10k ohm resistor, and C is equal 10 microFarad. This allows the output signal to range from 1.2Hz to 7.2Hz. 

![NE555 Timer](/image/NE_555.png)

The output signal is then amplified by the AD8039ARZ op-amp, which is powered by a 5V and -5V source from the MAX889SESA+ voltage regulator. The gain of the op-amp can be adjusted by two \( 100k\Omega \) potentiometers, one of them is connected to the inverting input of U2A and the other one to the inverting input of U2B. These potentiometer configurations allows the output signal to range from 0V to 5V.


The last 100k\Omega potentiometer is used to adjust the offset of the output signal, which allows the output signal to range from -2.5V to 2.5V.
![AD8039ARZ Op-amp](/image/AD8039.png)

There are test points that would allow the user to test the effects of the potentiometers on the output signal. The test points are connected to the output of the NE555 timer IC, the output of the AD8039ARZ op-amp, and the output of the MAX889SESA+ voltage regulator.

# Results
The PCB was hand-soldered and tested using an oscilloscope.

![PCB_soldered](/image/PXL_20240627_014233494_Original.jpg)
The output signal was a square wave signal that can be adjusted using the potentiometers. The gain and offset of the signal can be adjusted to the user's preference. However, there was some issues with the output signal where the gain and offset potentiometers were not working as intended.

# Conclusion
The project was a success in terms of learning how to design a PCB using KiCad and understanding the basic concepts of signal generation. The project also introduced me to SMD components, bill of materials and how to solder these components onto the PCB. However, there were some issues with the output signal that needs to be addressed in the future.