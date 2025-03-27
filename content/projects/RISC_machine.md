---
title: "RISC Machine"
date: "2025-02-14T16:46:16-08:00"
draft: false
tags: ["hugo", "PaperMod"]
categories: ["Projects"]
weight: 3
---
[🔗 View on GitHub](https://github.com/AP010307/CPEN_211_RSIC.git)

A SystemVerilog and ARM assembly project that creates a simple computer with basic arithmetics and memories.

# Overview
This project is 3 labs combined into one project for CPEN 211, where we designed a  reduced set instruction computer (RISC) machine using SystemVerilog and ARM assembly on a De1-SoC board. The RISC machine is capable of performing basic arithmetic operations and memory operations.

# Introduction
The project was divided into two parts: the SystemVerilog part and the ARM assembly part. The SystemVerilog part was to design the RISC machine using a finite state machine (FSM) and the ARM assembly part was to write a program that runs on the RISC machine. The RISC machine was designed to have a 16-bit data bus, 16-bit address bus, 16-bit registers, and 16-bit memory. The machine was capable of performing basic arithmetic operations such as addition, subtraction, multiplication, and division. It was also capable of performing memory operations such as load and store.

# Objective
The objective conveyed the following requirements:
- **Datapath**
  - A register file containing 8 locations with 16-bit registers.
  - A 16-bit ALU (Arithmetic logic unit) capable of performing addition, subtraction, multiplication, and division.
- **Finite state machine controller**
  - A finite state machine that controls the datapath.
  - The FSM should be able to perform the following operations:
    - Load a value from memory to a register.
    - Store a value from a register to memory.
    - Perform arithmetic operations.
- **Memory input and output**
    - A 16-bit memory that can store 256 16-bit values.
    - The memory should be able to read and write values.

# Design
## Hardware
The hardware only required the De1-SoC board.
## SystemVerilog
The SystemVerilog design was divided into two parts: the datapath and the finite state machine controller.
### Datapath
![Datapath](/image/Datapath_diagram.png)
The datapath consisted of the following components:
- **A 16-bit ALU**.
- **8 16-bit registers**.
- **A 16-bit shifter**.
#### ALU
| ***ALU's lab 5*** | ***ALU lab 6*** |
|------------------------------|--------------------------------|
![ALU](/image/ALU_image.png)|![ALU_lab6](/image/ALU_image_upgrade.png)

First, I declared ALU macros that represented 2-bit binary value. Then, I created a 16-bit ALU that could perform addition, subtraction, multiplication, and division.
| Value on ALUop input | Operation |
|----------|---------------------------|
| 00      | Ain + Bin                 |
| 01      | Ain - Bin                     |
| 10      | Ain & Bin              |
| 11      | ~Bin                     |
#### Register File
| ***Register's diagram*** | ***Register's declaration*** |
|------------------------------|--------------------------------|
| ![Diagram](/image/Regfile_diagram.png) | ![Declare](/image/Regfile_declare.png) |
For the register file, it took input data through a multiplexer which selected whether data was coming from the output or the external switches. It contained two 3-8 decoder that one selected the register to write to while the other chose which register's output to continue. 

#### Shifter
![Shifter](/image/Shifter_declare.png)
The shifter was used to shift the data to the left or right by 1 bit. It was used in the multiplication and division operations.
| shift | Operation |
|----------|---------------------------|
| 00      |B|
| 01      |B shifted left 1-bit, least significant bit is zero                     |
| 10      |B shifted right 1-bit, most significant bit, MSB is zero             |
| 11      |B shifted right 1-bit, MSB is copy of B[15]                    |

#### Datapath
 ***Datapath's code*** |
|![Datapath_code](/image/Datapath_code_1st.png)|![Datapath_code](/image/Datapath_code_2nd.png)|
|-----------------------------------------------|-----------------------------------------------|
![Datapath_code](/image/Datapath_code_3rd.png)

The datapath file called all the components and connected them together. It took the input data from the ALU, the register file, and the shifter. It also took the input data from the memory and the output data from the memory. The datapath was controlled by the FSM controller.

## Finite State Machine Controller
| ![FSM](/image/FSM_1st.png) | ![FSM](/image/FSM_2nd.png) |
|------------------------------|--------------------------------|
| ![FSM](/image/FSM_3rd.png) | ![FSM](/image/FSM_4th.png) |

Instead of manually controlling the datapath, the FSM controller was used to control the datapath. The FSM controller was designed to have 6 states:
- **WAIT**: The initial state of the machine.
- **DECODE**: Load a value from memory to a register.
- **MOV_IMM**: Move an immediate value to a register.
- **MOV_RM**: Move a value from a register to memory.
- **ADD**: Perform addition.
- **CMP**: Perform comparison.
- **AND**: Perform bitwise AND.
- **MVN**: Perform bitwise OR. 
- **Writeback**: Write the result back to the register.

They also contain new components such as instructional register and decoder.
### Instructional register
A simple instructional file that stored the current instruction according to the rising edge of the clock.
### Instructional Decoder 
| ***Decoder's declaration*** | ***Cont*** |
|------------------------------|--------------------------------|
| ![Diagram](/image/Instructional_decoder.png) | ![Declare](/image/Instructional_decoder.png) |

| ***Decoder's declaration*** |
|------------------------------|
| ![Diagram](/image/Instruction_decoder_diagram.png) |

One of the most important components of the FSM controller was the decoder. The decoder took the 16-bit current instruction and and a 2 bit select for the multiplexer to output MOVE instructions and ALU operations. The 16-bit instruction was divided into 4 parts: the opcode, the destination register, the source register, and the immediate value. The opcode was used to determine the operation to be performed. The destination register was used to determine the register to write to. The source register was used to determine the register to read from. The immediate value was used to store the immediate value to be used in the operation.

## Memory input
Despite the team are willing to work to create a final product, the memory was not implemented due to team member's unforseen circumstances. The memory was supposed to be a 16-bit memory that could store 256 16-bit values. The memory was supposed to be able to read and write values.

# Conclusion
Overall, the project taught me how to design a simple computer using SystemVerilog and ARM assembly. I learned how to design a finite state machine that controlled the datapath. I also learned how to design a datapath that contained an ALU, a register file, and a shifter. I also learned how to design a decoder that decoded the current instruction. I also learned how to design a memory that could read and write values. The project was a great learning experience and I would recommend it to anyone who is interested in computer architecture.

Even though the RSIC did not have a memory, the team was able to implement the ALU, the register file, the shifter, the FSM controller, and the decoder. The team was also able to implement the ALU operations, the MOVE operations, and the ALU operations. The team was also able to implement the FSM controller that controlled the datapath. The team was also able to implement the decoder that decoded the current instruction. The team was also able to implement the memory that could read and write values.

# Acknowledgement
I want to thank my teammate Rio DaCosta for his unwavering dedication and hard work on this project. 
