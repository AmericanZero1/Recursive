class MultiAgentCommunication:
    def __init__(self, quantum_key):
        self.quantum_key = quantum_key

    def send_message(self, agent_id, message):
        encrypted_message = f"{message}-{self.quantum_key}"
        print(f"Message sent to Agent-{agent_id}: {encrypted_message}")