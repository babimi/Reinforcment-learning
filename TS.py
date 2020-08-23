import numpy as np

def main():
  print("Begin Thompson sampling demo ")
  print("Goal is to maximize payout from three machines")
  print("Machines pay out with probs 0.1,0.4,0.45,0.6,0.61")

  N = 5  # number machines
  means = np.array([0.1,0.4,0.45,0.6,0.61])
  probs = np.zeros(N)
  S = np.zeros(N, dtype=np.int)
  F = np.zeros(N, dtype=np.int)
  rnd = np.random.RandomState(7)

  for trial in range(1000):
    print("\nTrial " + str(trial))
#built-in NumPy beta(a, b) function draws a sample from the beta distribution.
    for i in range(N): 
      probs[i] = rnd.beta(S[i] + 1, F[i] + 1)

    print("sampling probs =  ", end="")
    for i in range(N):
      print("%0.4f  " % probs[i], end="")
    print("")

    machine = np.argmax(probs)
    print("Playing machine " + str(machine), end="")

    p = rnd.random_sample()  # [0.0, 1.0)
    if p < means[machine]:
      print(" -- win")
      S[machine] += 1
    else:
      print(" -- lose")
      F[machine] += 1

  print("Final Success vector: ", end="")
  print(S)
  print("Final Failure vector: ", end="")
  print(F)

if __name__ == "__main__":
  main()


