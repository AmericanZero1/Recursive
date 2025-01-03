import numpy as np

class DefensePerceptionLayer:
    def __init__(self, attention_weights):
        self.attention_weights = attention_weights

    def process_inputs(self, drone_data, radar_data, thermal_data):
        drone_features = np.mean(drone_data)
        radar_features = np.max(radar_data)
        thermal_features = np.std(thermal_data)
        weighted_inputs = np.array([drone_features, radar_features, thermal_features]) * self.attention_weights
        return weighted_inputs