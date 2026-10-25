from math import exp, pi

# Tiny exact linear-symbol algebra: an expression is a dict atom -> integer coefficient.
def add(*exprs):
    out = {}
    for e in exprs:
        for k, v in e.items():
            out[k] = out.get(k, 0) + v
            if out[k] == 0:
                del out[k]
    return out

def scale(a, e):
    return {k: a*v for k, v in e.items() if a*v}

def atom(name):
    return {name: 1}

d = atom("d")
d1 = atom("d1")
c = atom("c")
gamma = atom("gamma")
X = atom("beta_D_v")
Y = atom("beta1_beta_v_T")
LT = atom("lambda_over_T")
LD = atom("lambda1_over_D")

# Published Jacobian trace.
div = scale(-1, add(d, d1, c, gamma, X, Y))
# Model equations divided by T and D.
logTdot = add(LT, scale(-1, X), scale(-1, d))
logDdot = add(LD, scale(-1, Y), scale(-1, gamma))
# Claimed cohomological right-hand side.
rhs = add(scale(-1, add(d1, c, LT, LD)), logTdot, logDdot)
assert add(div, scale(-1, rhs)) == {}

# Source example: omega=pi/5, mean(d1)=0.1, mean(c)=0.06.
omega = pi/5
baseline = exp(-omega*(0.1+0.06))
assert abs(baseline - 0.9043571086383213) < 2e-15
assert 0.0 < baseline < 1.0

# Independent numerical replay reported in the verification note obeys the theorem's strict bound.
replayed_det = 0.665268082639013
assert 0.0 < replayed_det < baseline
assert replayed_det**0.25 < baseline**0.25

print("VERIFY_OK")
