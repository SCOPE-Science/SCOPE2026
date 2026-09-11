"""ADM mass by volume integral (robust for spinning punctures) + convergence check at S=2.

M_ADM = 1 + (1/2pi) ∫ beta psi^-7 d^3x   (Brandt-Brügmann: M=m+1/(2π)∫βψ^-7)
Compare with falloff estimate; check grid sensitivity; print ψ on horizon, u(0), etc.
"""
import numpy as np, math, sys
sys.path.insert(0, "output/artifacts")
from puncture_mots import solve_u, make_interp, find_mots, shoot, mots_area

for tag in ["S2"]:
    Uc, psi, Mfall, res = solve_u(2.0, verbose=True)
    from puncture_mots import R, TH, dr, dth
    beta = (9.0/4.0)*4.0*(np.sin(TH)**2)/(R**6)
    integ = beta * psi**-7 * R**2 * np.sin(TH)
    I = float(np.sum(integ) * dr * dth * 2*math.pi)
    Mvol = 1.0 + I/(2*math.pi)
    print("M_falloff=", Mfall, " M_volume=", Mvol, " res=", res, flush=True)
    print("u max/min:", Uc.max(), Uc.min(), " psi max:", psi.max(), flush=True)
