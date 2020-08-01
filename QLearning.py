

import Environment


env = Environment.Environment()

s0 = env.reset()

for i in range(1000):
    at = 0
    st1, rt, done, debug = env.step(at)

    if done:
        break
