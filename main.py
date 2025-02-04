import numpy as np

class BinomialTreeEuropean:

  def __init__(self, steps, r, delta, T, sigma, S, K, call=True, european=True):
    self.S = S
    self.K = K
    self.r = r
    self.delta = delta

    self.h = float(T)/steps
    self.call = call
    self.european = european
    self.u = np.exp((r-delta)*self.h + sigma * np.sqrt(self.h))
    self.d = np.exp((r-delta)*self.h - sigma * np.sqrt(self.h))
    self.p = (np.exp((r-delta)*self.h) - self.d) / (self.u - self.d)

    self.spot_tree = [[0 for _ in range(i + 1)] for i in range(steps + 1)]
    self.payoff_tree = [[0 for _ in range(i + 1)] for i in range(steps + 1)]
    self.value_tree = [[0 for _ in range(i + 1)] for i in range(steps + 1)]

    self.propagate()
    value = self.backpropagate()
    self.value = value
    

  def propagate(self):
    self.spot_tree[0][0] = self.S
    self.payoff_tree[0][0] = self.S - self.K
    for i in range(len(self.spot_tree) - 1):
      for j in range(len(self.spot_tree[i])):
        self.spot_tree[i+1][j] = self.spot_tree[i][j] * self.u
        if self.call:
          self.payoff_tree[i+1][j] = max(self.spot_tree[i+1][j] - self.K, 0)
        else:
          self.payoff_tree[i+1][j] = max(self.K - self.spot_tree[i+1][j], 0)

        self.spot_tree[i+1][j+1] = self.spot_tree[i][j] * self.d
        if self.call:
          self.payoff_tree[i+1][j+1] = max(self.spot_tree[i+1][j+1] - self.K, 0)
        else:
          self.payoff_tree[i+1][j+1] = max(self.K - self.spot_tree[i+1][j+1], 0)
        
  def backpropagate(self):
    for j in range(len(self.value_tree[-1])):
      self.value_tree[-1][j] = self.payoff_tree[-1][j]

    discount = np.exp(-self.r*self.h)
    for i_ in range(len(self.value_tree)-1):
      i = len(self.spot_tree) - 2 - i_
      for j in range(len(self.value_tree[i])):
        weighted_up = self.p * self.value_tree[i+1][j]
        weighted_down = (1-self.p) * self.value_tree[i+1][j+1]
        self.value_tree[i][j] = discount * (weighted_up + weighted_down)

        if not self.european:
          self.value_tree[i][j] = max(self.value_tree[i][j], self.payoff_tree[i][j])
    return self.value_tree[0][0]
  

def main():
  steps = 200
  r = 0.03
  delta = 0
  T = 1/3
  sigma = 0.3
  S = 78
  K = 80
  call = True
  european = False

  tree = BinomialTreeEuropean(steps, r, delta, T, sigma, S, K, call, european)
  
  print(tree.value)

  


if __name__ == '__main__':
  main()
