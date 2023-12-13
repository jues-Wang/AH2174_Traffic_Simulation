import traci
import traci.constants as tc
import time

# Start the SUMO simulation
sumo_binary = "sumo-gui"  # or "sumo" for headless mode
sumo_cmd = [sumo_binary, "-c", "sumo_test.sumo.cfg"]
traci.start(sumo_cmd)

# Run the simulation for a few steps
for _ in range(100):
    traci.simulationStep()

    # Get the current simulation time
    sim_time = traci.simulation.getTime()

    # Control the vehicle after 10 seconds
    if sim_time >= 0:
        vehicle_id = "veh0"

        # Accelerate for 20 seconds with an acceleration rate of 0.9 m/s^2
        if sim_time <= 20.0:
            #traci.vehicle.setSpeedMode(vehicle_id, tc.Vehicle.CMD_ACC)
            traci.vehicle.setSpeed(vehicle_id, traci.vehicle.getSpeed(vehicle_id) + 0.9 * traci.simulation.getDeltaT())

        # Run with constant speed for the next 20 seconds
        elif 20.0 < sim_time <= 40.0:
            #traci.vehicle.setSpeedMode(vehicle_id, tc.Vehicle.CMD_SPEED)
            traci.vehicle.setSpeed(vehicle_id, traci.vehicle.getSpeed(vehicle_id) + 0 * traci.simulation.getDeltaT())  # Set the desired constant speed

        # Decelerate with a deceleration rate of 1.5 m/s^2 until the vehicle stops
        elif sim_time > 40.0:
            #traci.vehicle.setSpeedMode(vehicle_id, tc.Vehicle.CMD_DECEL)
            traci.vehicle.setSpeed(vehicle_id, max(0.0, traci.vehicle.getSpeed(vehicle_id) - 1.5 * traci.simulation.getDeltaT()))

# Close the TraCI connection
traci.close()