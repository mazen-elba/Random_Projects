# Bias-Variance Tradeoffs
- Sample complexity is at odds with model complexity in Machine Learning.
  - Model complexity - a sufficiently complex model is necessary to solve a problem
  - Sample complexity - a model that does not require many samples is preferrable
- For both models to attain the same performance, bias-variance tells us that an extremely complex model will need exponentially more samples to train
  - To maintain same error rate, increasing model complexity increases sample complexity exponentially
  - Decreasing sample complexity decreases model complexity
- Bias-Variance decomposition is a breakdown of "true error" (mean squared error (MSE)) into two components: bias and variance
  - MSE is the expected difference between predicted labels and true labels

# Reinforcement Learning
## Q-Learning Policy
  - In any game, a player's goal is to maximize their score.
  - The player's score is the agent's reward.
  - To maximize the reward, the player must be able to refine its decision-making abilities.
  - A dicision is the process of looking at the game, or observing the game's state, and picking an action.
  - The deicion-making function is called a policy.
  - A policy accepts a state as input and "decides" an action (policy: state -> action).
  - To build a policy function, start with a algorithms (ie; Q-Learning algorithms).
  - Q-Learning policy provides (policy: state -> pick action with greatest reward (from Q-function)).
  - Q-function: Q(state, action) = reward
  - Given a particular state, it's easy to make a decision (look at each possible action and its reward, then take action corresponding to highest expected reward).
  - Thus gives Q-learning policy: state -> argmax_{action} Q(state, action)
  - To estimate Q(state, action) consider the following:
    - 1) Given many observations of an agent's states, actions, and rewards, obtain an estimate of the reward for every state and action (by taking a running average)
      - Q(state, action) = (1 - learning_rate) * Q(state, action) + learning_rate * Q_target
    - 2) Given delayed rewards, Q-function must assign (state, action) a positive reward
      - Q_target = reward + discount_factor * max_{action'} Q(state', action')
    - state: state at current time step
    - action: action taken at current time step
    - reward: reward for current time step
    - state': new state for next time step (given an action was taken)
    - action': all possible actions
    - learning_rate: learning rate
    - discount_factor: how much reward "degrades" as we propagate it
  
