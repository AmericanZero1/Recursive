class DefenseActionLayer:
    def __init__(self, decision_threshold):
        self.decision_threshold = decision_threshold

    def evaluate_action(self, classification, risk_level):
        return classification != "Low Threat" and risk_level < self.decision_threshold

    def execute_action(self, classification):
        print(f"Executing Response for: {classification}")