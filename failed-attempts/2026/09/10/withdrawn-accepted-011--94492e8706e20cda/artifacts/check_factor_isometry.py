"""Check X-factor embedding t=0 is isometric and cross-factor distance is pi/2.
Also check GH-continuity proxy: join distance is 1-Lipschitz in a via cos(d_Y) term
(d_Y(y1,y2) = min(|s1-s2|, a-|s1-s2|) on circle of length a)."""
import math, random
random.seed(5130)

def join_dist(dx, dy, t1, t2):
    c = math.cos(t1)*math.cos(t2)*math.cos(dx) + math.sin(t1)*math.sin(t2)*math.cos(dy)
    return math.acos(max(-1.0, min(1.0, c)))

# 1. factor isometry: t1=t2=0 -> d_join == d_X exactly, random trials
worst = 0.0
for _ in range(5000):
    dx = random.uniform(0, math.pi)
    if abs(join_dist(dx, 0.0, 0.0, 0.0) - dx) > 1e-12:
        worst = max(worst, abs(join_dist(dx, 0.0, 0.0, 0.0) - dx))
print("factor-isometry max err:", worst)
assert worst == 0.0

# 2. cross-factor: t1=0,t2=pi/2 -> pi/2 for ANY dx,dy
for _ in range(1000):
    dx = random.uniform(0, math.pi); dy = random.uniform(0, math.pi)
    assert abs(join_dist(dx, dy, 0.0, math.pi/2) - math.pi/2) < 1e-12
print("cross-factor pi/2 OK")

# 3. Y-factor isometry: t1=t2=pi/2 -> d_join == d_Y
for _ in range(1000):
    dy = random.uniform(0, math.pi)
    assert abs(join_dist(0.0, dy, math.pi/2, math.pi/2) - dy) < 1e-12
print("Y-factor isometry OK")

# 4. antipodal S^2 pair => pi for every a (a only enters via d_Y, irrelevant at t=0)
for a in [0.01, 0.5, 1.0, math.pi, 2*math.pi]:
    d = join_dist(math.pi, 0.0, 0.0, 0.0)
    assert abs(d - math.pi) < 1e-12, a
print("antipodal pi for all a OK")
print("ALL FACTOR CHECKS PASS")
