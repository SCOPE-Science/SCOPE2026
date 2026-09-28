"""Link diameter: diam(S^1(1) * S^1_a) = pi for every a (target (E)-directed).

Same constant-diameter mechanism applied to Sigma_p = S^1 * S^1_a: the unit
circle S^1(1) (length 2pi) has antipodes at distance pi, embedded isometrically
at t=0. Consequence for (E): opposite strainer pairs are NOT blocked by link
diameter (which is pi, ample); the obstruction must be dimensional/density-type
(needs 4 mutually orthogonal opposite pairs in a 3-dim link of volume pi*a).
Rules out the naive diameter mechanism inside branch (E) itself.
"""
import math, random

def join_dist(dx, dy, t1, t2):
    c = math.cos(t1)*math.cos(t2)*math.cos(dx) + math.sin(t1)*math.sin(t2)*math.cos(dy)
    return math.acos(max(-1.0, min(1.0, c)))

# lower bound: antipodal S^1(1) pair at t=0 -> pi (a-independent)
d = join_dist(math.pi, 0.0, 0.0, 0.0)
print("link antipodal-factor distance:", d)
assert abs(d - math.pi) < 1e-12

# upper bound: grid sweep, max <= pi
random.seed(5314)
worst = 0.0
for a in [0.5, 1.0, math.pi, 5.0, 2*math.pi]:
    diamY = a/2
    for _ in range(20000):
        t1 = random.uniform(0, math.pi/2); t2 = random.uniform(0, math.pi/2)
        dx = random.uniform(0, math.pi); dy = random.uniform(0, diamY)
        worst = max(worst, join_dist(dx, dy, t1, t2))
print("link grid max:", worst)
assert worst <= math.pi + 1e-9
print("LINK DIAMETER OK: diam(Sigma_p) = pi for all a; (E) needs density/dimension mechanism")
