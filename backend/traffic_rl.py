import numpy as np
import random

class TrafficLightRL:
    def __init__(self):
        self.state = [0, 0]  # [Cars at red light, Cars at green light]
        self.q_table = np.zeros((10, 10, 2))  # Q-learning table

    def choose_action(self, epsilon=0.1):
        if random.uniform(0, 1) < epsilon:
            return random.choice([0, 1])  # 0 = Stay Red, 1 = Switch to Green
        return np.argmax(self.q_table[self.state[0], self.state[1]])

    def update_q_table(self, reward, action):
        alpha = 0.1  # Learning rate
        gamma = 0.9  # Discount factor
        self.q_table[self.state[0], self.state[1], action] += alpha * (reward + gamma * np.max(self.q_table[self.state[0], self.state[1]]) - self.q_table[self.state[0], self.state[1], action])

if __name__ == "__main__":
    traffic_rl = TrafficLightRL()
    action = traffic_rl.choose_action()
    print(f"Chosen Action: {action}")
