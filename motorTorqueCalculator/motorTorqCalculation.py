##################################################
# mass of everything excluding the servos
##################################################
massesInKG = {
    "battery": 0.531,
    "printedChassisLegsBracketsCovers": 0.400,
    "pi5CoolerStorageMounts": 0.100,
    "esp32Boards": 0.020,
    "cameraMicrophoneSpeakerSensors": 0.050,
    "regulatorsPowerDistributionWiringConnectors": 0.130,
    "bearingsBoltsNutsSpacersHorns": 0.120,
    "optionalAIAcceleratorAndMount": 0.040,
}

totalMassInKG = sum(massesInKG.values())
print(f"Total mass: {totalMassInKG:.2f} kg")

##################################################
# mass of servos
##################################################
servoMassInKG = 0.014
numberOFServos = 3 * 6 

totalServoMassInKG = servoMassInKG * numberOFServos
print(f"Total mass of servos: {totalServoMassInKG:.2f} kg")

##################################################
# total mass including servos
##################################################

totalRoboMass = totalMassInKG + totalServoMassInKG
print(f"Total mass including servos: {totalRoboMass:.2f} kg")

##################################################
# mass per leg
##################################################

massPerLegInKG = totalRoboMass / 6
print(f"Mass per leg: {massPerLegInKG:.2f} kg")