import numpy as np

class QuantumKeyDistribution:
    def __init__(self):
        self.sender_key = []
        self.receiver_key = []
        self.basis = []

    def generate_key(self, key_length):
        self.sender_key = np.random.randint(0, 2, key_length)
        self.basis = np.random.choice(['+', 'x'], key_length)
        return self.sender_key, self.basis

    def simulate_measurement(self, received_basis):
        self.receiver_key = []
        for sender_bit, sender_basis, receiver_basis in zip(self.sender_key, self.basis, received_basis):
            if sender_basis == receiver_basis:
                self.receiver_key.append(sender_bit)
            else:
                self.receiver_key.append(np.random.randint(0, 2))
        return self.receiver_key

    def compare_bases(self, received_basis):
        matching_bits = [i for i in range(len(self.basis)) if self.basis[i] == received_basis[i]]
        return matching_bits