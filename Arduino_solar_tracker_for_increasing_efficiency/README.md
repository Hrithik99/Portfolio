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

#include <Servo.h>

// Define Servo objects
Servo servohori;  // Horizontal servo
Servo servoverti; // Vertical servo

// Servo position variables
int servoh = 0;
int servov = 0;

// Servo angle limits
int servohLimitHigh = 160;
int servohLimitLow = 20;
int servovLimitHigh = 160;
int servovLimitLow = 20;

// LDR pin assignments
int ldrtopl = 2; // Top left LDR (green wire)
int ldrtopr = 1; // Top right LDR (yellow wire)
int ldrbotl = 3; // Bottom left LDR (blue wire)
int ldrbotr = 0; // Bottom right LDR (orange wire)

void setup() {
  // Attach and initialize servos
  servohori.attach(10);
  servohori.write(0);
  servoverti.attach(9);
  servoverti.write(0);
  delay(500);
}

void loop() {
  // Read current servo positions
  servoh = servohori.read();
  servov = servoverti.read();

  // Read LDR values
  int topl = analogRead(ldrtopl);
  int topr = analogRead(ldrtopr);
  int botl = analogRead(ldrbotl);
  int botr = analogRead(ldrbotr);

  // Calculate averages
  int avgtop = (topl + topr) / 2;   // Average of top LDRs
  int avgbot = (botl + botr) / 2;   // Average of bottom LDRs
  int avgleft = (topl + botl) / 2;  // Average of left LDRs
  int avgright = (topr + botr) / 2; // Average of right LDRs

  // Adjust vertical position
  if (avgtop < avgbot) {
    servoverti.write(constrain(servov + 1, servovLimitLow, servovLimitHigh));
  } else if (avgbot < avgtop) {
    servoverti.write(constrain(servov - 1, servovLimitLow, servovLimitHigh));
  } else {
    servoverti.write(servov);
  }

  // Adjust horizontal position
  if (avgleft > avgright) {
    servohori.write(constrain(servoh + 1, servohLimitLow, servohLimitHigh));
  } else if (avgright > avgleft) {
    servohori.write(constrain(servoh - 1, servohLimitLow, servohLimitHigh));
  } else {
    servohori.write(servoh);
  }

  delay(50); // Small delay to prevent rapid movements
}



## Conclusion

The Arduino Solar Tracker project showcases an effective way to maximize solar energy capture using readily available components and Arduino technology. By automatically aligning solar panels with the sun's position, this system can significantly improve the efficiency of solar power installations.


