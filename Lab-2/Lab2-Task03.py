class ClassroomAgent:
    def __init__(self):
        self.prev_mode = None  
    def act(self, temp, occupied):

        if not occupied:
            target = "ECO"
        elif temp > 26:
            target = "COOL"
        elif temp < 20:
            target = "WARM"
        else:
            target = "IDLE"
        if target == self.prev_mode:
            should_send = False
        else:
            should_send = True
            self.prev_mode = target  
        return target, should_send
agent = ClassroomAgent()
percepts = [
    (29, True),(29, True),(20, True),(26, True),(19, True),(19, True),(29, False),(29, False)   
]
print("Step | Prev Mode | Percept      | Target | Outcome")
print("-" * 55)
for step, percept in enumerate(percepts, 1):
    prev_before = agent.prev_mode
    target, send = agent.act(*percept)
    outcome = "SEND" if send else "NO-COMMAND"
    print(f"{step}    | {str(prev_before):<9} | {percept} | {target:<6} | {outcome}")