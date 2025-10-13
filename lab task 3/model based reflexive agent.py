class ModelBasedReflexAgent:
    def __init__(self, desired_temperature):
        self.desired_temperature = desired_temperature
        self.last_action = {}
    def act(self, room, current_temperature):
        if current_temperature < self.desired_temperature:
            action = "Turn on heater"
        else:
            action = "Turn off heater"
        prev = self.last_action.get(room)
        if prev == action:
            return "No action"
        self.last_action[room] = action
        return action

rooms = {"Living Room": 18, "Bedroom": 22, "Kitchen": 20, "Bathroom": 24}
desired_temperature = 22
agent = ModelBasedReflexAgent(desired_temperature)
for room, temperature in rooms.items():
    print(f"{room}: {agent.act(room, temperature)} (temp={temperature}°C)")

next_readings = {"Living Room": 19, "Bedroom": 22, "Kitchen": 23, "Bathroom": 21}
for room, temperature in next_readings.items():
    print(f"{room}: {agent.act(room, temperature)} (temp={temperature}°C)")