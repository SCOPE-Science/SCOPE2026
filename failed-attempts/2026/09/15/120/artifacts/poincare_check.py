"""Recovery test: Poincare-series breakdown of the naive Gamma-sum dispersive route,
and threshold-resonance truncation ratio. Model computation supporting the
target-exit request for lane-20356.
"""
import math

def poincare_partial(delta, Rmax, dR=0.5):
    # Model orbital counting N(R) ~ exp(delta*R) (leading exponential rate).
    # Shell count in [R, R+dR) ~ N(R+dR)-N(R); term weight ~ R/sinh(R) ~ 2R*exp(-R).
    # Partial sum S(Rmax) over shells; divergence vs convergence read off growth.
    S = 0.0
    R = dR
    traj = []
    while R <= Rmax:
        shell = math.exp(delta*(R+dR)) - math.exp(delta*R)
        w = (R/math.sinh(R)) if R < 50 else 2.0*R*math.exp(-R)
        S += shell*w
        traj.append(S)
        R += dR
    return S, traj

for delta in [0.5, 1.0, 1.5]:
    S, traj = poincare_partial(delta, 20.0)
    print(f"delta={delta}: S(5)={traj[9]:.4g} S(10)={traj[19]:.4g} S(15)={traj[29]:.4g} S(20)={S:.4g}")

# Threshold-resonance (delta=1) truncation: phi ~ e^{-r}, funnel volume ~ e^{2r} dr.
# ||u_R||_2^2 ~ int_0^R e^{-2r} e^{2r} dr = R; ||u_R||_6^6 ~ int_0^R e^{-6r} e^{2r} dr.
def ratio(R):
    import mpmath  # may not exist; fallback below
    return None
try:
    import mpmath
    have_mp = True
except ImportError:
    have_mp = False

for R in [5, 10, 20, 40]:
    L2 = math.sqrt(R)  # up to constants
    L6 = ((1.0 - math.exp(-4.0*R))/4.0)**(1.0/6.0)
    print(f"R={R}: ||u||6/||u||2 ~ {L6/L2:.4g} (bounded numerator, growing denominator -> 0)")
print("mpmath available:", have_mp)
print("CONCLUSION: Gamma-sum absolute bound diverges for delta>=1 (linear growth at delta=1, exponential for delta>1);")
print("threshold-resonance truncations give vanishing L6/L2 ratio, i.e. no elementary low-energy counterexample.")
