# Arduino Solar Tracker

## Introduction

The Arduino Solar Tracker is an innovative project that utilizes light-dependent resistors (LDRs) and servo motors to automatically orient a solar panel towards the sun for maximum energy capture. This system enhances the efficiency of solar panels by ensuring they receive optimal sunlight throughout the day.

## Features

- 🌞 Dual-axis tracking for precise solar panel orientation
- 🔧 Uses four LDRs for accurate light detection
- 🤖 Arduino-controlled for automated operation
- ⚡ Improves solar panel efficiency

## Components Required

- 2 Servo motors
- Solar panel
- Cardboard
- 4 LDRs (Light Dependent Resistors)
- Straight perforated metal strip
- 10K Ω resistor
- Arduino board
- Connecting wires
- Breadboard

## Installation

1. Create a cardboard mount with holes for the LDRs and solar panel.
2. Attach the solar panel to the cardboard and connect its wires.
3. Insert and secure the LDRs into the designated holes.
4. Solder the LDR connections and add 10k Ω resistors.
5. Mount the servo motors using perforated metal strips.
6. Connect the components according to the circuit diagram provided in the documentation.

## Usage

After assembling the hardware and connections:

1. Upload the provided Arduino code to your Arduino board.
2. Place the solar tracker in an open area with direct sunlight.
3. The system will automatically adjust the solar panel's position to track the sun.

## Working Principle

The solar tracker operates by comparing light intensity detected by the four LDRs:

- For east-west tracking, it compares top and bottom LDR pairs.
- For angular adjustment, it compares left and right LDR pairs.

The Arduino processes these readings and controls the servo motors to orient the solar panel towards the brightest light source, effectively tracking the sun's position.

## Code

Here's a snippet of the Arduino code that controls the solar tracker:

