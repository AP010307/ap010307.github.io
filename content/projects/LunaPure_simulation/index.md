---
title: "LunaPure thermal system simulation"
date: "2025-08-29T16:46:16-08:00"
draft: false
tags: ["MATLAB", "Simulink"]
categories: ["Projects"]
github:
weight: 1
---

# DISCLAIMER
This project is ongoing and is currently under the intellectually property of the Pacific Space Exploration Corp and Canadian Space Mining Corperation so the information on this site is a work in progress and has been allowed to be disclosed with supervision. Further discussion about the project can be discussed later through email or interview.

# Overview
I created a Simulink model of PARSEC's lunar water purification system to help fellow engineers to improve their thermal system and understand the mechanism of the reactor.

# Introduction
As the Canadian Space Mining Cooperation (CSMC) is currently competiting for the [AquaLunar Competition](https://www.canada.ca/en/space-agency/news/2024/01/the-aqualunar-challenge-purifying-moon-water.html) created by the Canadian Space Agency (CSA) in the attempt to return to the Moon for more ambitious space missions, CSMC needs an innovative solutions to purify our Moon's icecap for potable and usable water. LunaPure, with its capabilities of extracting water through several processes of distillation, will need several rounds of upgrades and optimization so that LunaPure can guarateed CSMC's championing the competition. To find area of improvements, the Pacific Space Exploration Corp (PARSEC), a student team contracted by CSMC, has allowed their team members to create simulation attempting to replicate a process cycle of LunaPure and using existing laboratory data to improve and imply the performance of the reactor and discovering new optimization.


# Objective

This project will need to investigate and discover areas of improvement for LunaPure so that PARSEC's engineers can implement data-driven changes and be ready for the upcoming deadline in early 2026.

- **Reactor replication**  
  - The model must be able to mimic a purification cycle of LunaPure.  
  - The model's must have the result similar from **1% to 5%** of the laboratory data.  

- **Cooling requirement**  
  - The model should be able to create parameters for the implementation of the cooling loop such as:
    - Pump parameters such as flow rate.
    - Cooling fluid properties.
    - Radiation physical parameters.

- **Being Modular and Customizable**  
  - Customizablility through adding new reactors' features  
  

# Design
## Iterations
**Version 1**
{{< figure src= "Reactor_1st_It.png" alt="First Reactor Model Iteration" >}} 
Given the similar characteristic of LunaPure's to an engine cooling system, the first iterations took heavy inspiration from an exisiting [MATLAB model]( https://www.mathworks.com/help/releases/R2025a/hydro/ug/engine-cooling-system.html) with some modification in the reactor cycle such as the removal of the fan system, change the engine cycle to have more constant instead of relying on a time-dependent look up table.
{{< figure src= "Air_model_input.png" alt="Air model input" >}} 
{{< figure src= "Air_property_calculations.png" alt="Air property calculation" >}} 

**Version 2**
{{< figure src= "Reactor_2nd_it.png" alt="Reactor_2nd_it" >}}
After discussion with the fellow engineers, the model needs to be adjusted to simulate laboratory settings. These adjustments include changing the layout of the model, increasing the complexity of the reactor itself to comply with different chemicals inside lunar ice pole, and a controller unit using PID. 

{{< figure src= "Inside.png" alt="Reactor_inner_component" >}}

Given the project are mostly tested in laboratory setting and some lunar environment conditions, the coolant loop is modeled with a radiator to simulate the functionality of LunaPure when it will be on the Moon. Detailed mechanism of the heating loop and cold loop will be disclosed when the competition is completed. 

{{< figure src= "Cold loop.png" alt="Coolant simulation" >}}

 Using Simulink components such as thermal mass to simulate the thermal capacity of the reactor, conductive  and radiative block to illustrate the model of heat transfer within LunaPure, combining different MATLAB functions, and containers that model 2-phase components well, these are the starting blocks to model the functionality of LunaPure.

 {{< figure src= "Hot_loop.png" alt="Heating_element simulation" >}}
  {{< figure src= "2_phase.png" alt="2_phase system" >}}

# To be continued

