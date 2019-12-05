# valueIterationAgents.py
# -----------------------
# Nhom 1:
# Ho va ten                 | MSSV       | Ngay sinh
# Hoang Thi Linh            | 17020852   | 08/03/1999
# Nguyen Thi Le             | 17020847   | 26/02/1999
# Le Thi Thuy Linh          | 17020854   | 24/10/1998
# Bui Thi Ngat              | 17020922   | 28/03/1999


import mdp, util

from learningAgents import ValueEstimationAgent

class ValueIterationAgent(ValueEstimationAgent):
    """
        * Please read learningAgents.py before reading this.*

        A ValueIterationAgent takes a Markov decision process
        (see mdp.py) on initialization and runs value iteration
        for a given number of iterations using the supplied
        discount factor.
    """
    def __init__(self, mdp, discount = 0.9, iterations = 100):
        """
          Your value iteration agent should take an mdp on
          construction, run the indicated number of iterations
          and then act according to the resulting policy.

          Some useful mdp methods you will use:
              mdp.getStates()
              mdp.getPossibleActions(state)
              mdp.getTransitionStatesAndProbs(state, action)
              mdp.getReward(state, action, nextState)
              mdp.isTerminal(state)
        """
        self.mdp = mdp
        self.discount = discount
        self.iterations = iterations
        self.values = util.Counter() # A Counter is a dict with default 0

        # Write value iteration code here
        "*** YOUR CODE HERE ***"
        states = self.mdp.getStates()
        for i in range(self.iterations):
            tmp_values = util.Counter()
            for state in states:
                if self.mdp.isTerminal(state):
                    continue
                actions = self.mdp.getPossibleActions(state)
                action_values_dict = util.Counter()
                for action in actions:
                    total_value = []
                    nextState_prob_list = self.mdp.getTransitionStatesAndProbs(state, action)
                    for (nextState, prob) in nextState_prob_list:
                        reward = self.mdp.getReward(state, action, nextState)
                        total_value.append(prob * (reward + self.discount * self.values[nextState]))
                    action_values_dict[action] = sum(total_value)
                tmp_values[state] = max(list(action_values_dict.values()))
            self.values = tmp_values


    def getValue(self, state):
        """
          Return the value of the state (computed in __init__).
        """
        return self.values[state]


    def computeQValueFromValues(self, state, action):
        """
          Compute the Q-value of action in state from the
          value function stored in self.values.
        """
        "*** YOUR CODE HERE ***"
        #util.raiseNotDefined()
        total_value = []
        nextState_prob_list = self.mdp.getTransitionStatesAndProbs(state, action)
        for (nextState, prob) in nextState_prob_list:
            reward = self.mdp.getReward(state, action, nextState)
            total_value.append(prob * (reward + self.discount * self.values[nextState]))
        return sum(total_value)

    def computeActionFromValues(self, state):
        """
          The policy is the best action in the given state
          according to the values currently stored in self.values.

          You may break ties any way you see fit.  Note that if
          there are no legal actions, which is the case at the
          terminal state, you should return None.
        """
        "*** YOUR CODE HERE ***"
        #util.raiseNotDefined()
        actions = self.mdp.getPossibleActions(state)
        action_values_dict = util.Counter()
        for action in actions:
            total_value = []
            nextState_prob_list = self.mdp.getTransitionStatesAndProbs(state, action)
            for (nextState, prob) in nextState_prob_list:
                reward = self.mdp.getReward(state, action, nextState)
                total_value.append(prob * (reward + self.discount * self.values[nextState]))
            action_values_dict[action] = sum(total_value)
        res = action_values_dict.argMax()
        return res

    def getPolicy(self, state):
        return self.computeActionFromValues(state)

    def getAction(self, state):
        "Returns the policy at the state (no exploration)."
        return self.computeActionFromValues(state)

    def getQValue(self, state, action):
        return self.computeQValueFromValues(state, action)
