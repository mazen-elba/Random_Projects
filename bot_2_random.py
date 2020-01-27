"""
Bot 2 -- Make a random, baseline agent for the SpaceInvaders game.
"""

import gym
import random

random.seed(0) # make results reproducible

num_episodes = 10

def main():
	env = gym.make('SpaceInvaders-v0') # create game environment
	env.seed(0) # make results reproducible
	rewards = []

	for _ in range(num_episodes):
		env.reset() # initialize the game
		episode_reward = 0
		while True:
			action = env.action_space.sample()
			_, reward, done, _ = env.step(action) # random action
			episode_reward += reward
			if done:
				print('Reward: %d' % episode_reward)
				rewards.append(episode_reward)
				break
	print('Average reward: %.2f' % (sum(rewards) / len(rewards)))

if __name__ == '__main__':
	main()
