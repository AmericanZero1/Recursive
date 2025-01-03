class DefenseCognitionLayer:
    def __init__(self, snn, symbol_map):
        self.snn = snn
        self.symbol_map = symbol_map

    def analyze_spiking(self, inputs):
        spikes = self.snn.simulate_step(inputs)
        return spikes

    def classify_threat(self, spikes):
        spike_sum = sum(spikes)
        return self.symbol_map.get(spike_sum % len(self.symbol_map), "Unknown")