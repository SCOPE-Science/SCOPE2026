"""Resonant geometry for the inhomogeneous target.

Game: standard Schmidt (alpha,beta) on [0,1]^2. Bad set:
  Bad^gamma = { x : liminf_q q^{1/2} max_i ||q x_i - gamma_i|| > 0 }.
At scale with Bob ball radius rho, resonant q ~ rho^{-2} (Dirichlet exponent 1/2
in simultaneous form: |x - (p+gamma)/q| ~ q^{-3/2} matches ball radius when
q^{-3/2} ~ rho i.e. q ~ rho^{-2/3}... careful: simultaneous in R^2 has
approximation function q^{-3/2}? No: ||q x - gamma|| < c q^{-1/2} means
|x-(p+gamma)/q| < c q^{-3/2}. So resonant centers (p+gamma)/q with spacing
1/q and danger radius ~ c q^{-3/2}.

Lower (Alice at alpha_low): need that in any ball, at most ~2 resonant
neighborhoods at the active scale matter (An separation), so Alice's deletion
of proportion alpha_low avoids them. Threat count per ball ~ (rho/(1/q))^2
centers times... compute directly.

Upper (Bob at alpha_high=1/12, beta0=1/2): need a scale where MANY resonant
neighborhoods cluster so Alice (deleting only 1/12-radius sub-ball... in
Schmidt game Alice chooses ball of radius alpha*rho inside Bob's ball, Bob
then chooses sub-ball of radius beta*that) cannot cover all threats; Bob
steers into a threat. Actually "not (alpha,beta)-winning" needs explicit Bob
strategy forcing limit outside Bad for those parameters. We test cluster
density: count of resonant centers per Bob-ball at active scale.
"""
import math
g1 = math.e - 2
g2 = math.sqrt(3) - 1
alpha_low = 1/(34*math.sqrt(2))
alpha_high = 1/12.0
beta0 = 0.5

def resonant_centers(q):
    # all (p1+g1)/q, (p2+g2)/q in [0,1]^2: p1 in 0..q-1 shifted; count ~ q^2
    # centers: ((p1+g1)/q mod 1...) but gamma in (0,1) so p_i=0..q-1 gives values in (0,1)
    pts = []
    for p1 in range(q):
        x = (p1 + g1)/q
        if x < 0 or x > 1: continue
        for p2 in range(q):
            y = (p2 + g2)/q
            if y < 0 or y > 1: continue
            pts.append((x,y))
    return pts

def count_in_ball(pts, cx, cy, rho):
    n = 0
    for (x,y) in pts:
        if abs(x-cx) <= rho and abs(y-cy) <= rho:
            n += 1
    return n

# Active scale analysis: Bob ball radius rho_n = (alpha*beta)^n rho0.
# Resonant q at scale rho: danger radius c*q^-1.5 ~ rho * something.
# Take c = 0.05 (Bad constant proxy). q_active ~ (c/rho)^{2/3}.
import json
out = {"gamma":[g1,g2], "alpha_low":alpha_low, "scales":[]}
c = 0.05
for k, rho in enumerate([0.1*(0.25)**n for n in range(6)]):
    q = int(round((c/rho)**(2/3)))
    q = max(q, 2)
    pts = resonant_centers(q)
    dr = c*q**-1.5
    # grid of test ball centers
    import random
    random.seed(0)
    counts = []
    for t in range(40):
        cx = random.random(); cy = random.random()
        counts.append(count_in_ball(pts, cx, cy, rho))
    # expected count ~ (2rho/(1/q))^2 = (2 rho q)^2
    out["scales"].append({"rho":rho, "q_active":q, "danger_r":dr,
        "n_centers":len(pts), "expected_per_ball": (2*rho*q)**2,
        "max_count":max(counts), "mean_count":sum(counts)/len(counts)})
print(json.dumps(out, indent=1))
