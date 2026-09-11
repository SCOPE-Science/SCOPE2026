"""Symmetric-ray probe for fallback: ell_p^4 balls are S4-invariant unconditional.
Exact rigorous facts (pi>3 only):
  P(B_2^4) = pi^4/4 >= 81/4 = 20.25 > 32/3  =>  deficit >= 28.75/3 > 9.58.
  d_BM(B_2^4, cube) = sqrt(4) = 2  =>  capped modulus min{1,d-1}^2 = 1.
So this ray is consistent with (not proof of) stability; any valid c4sym <= actual
deficit here. Indicative gamma values for other p are non-rigorous illustration.
Conclusion printed: RAY_CONSISTENT (universality NOT established by this probe).
"""
import math

def probe():
    # Rigorous lower bound via pi > 3
    deficit_lb = Q_ = (81*3 - 32*4) / 12  # 81/4 - 32/3 = (243-128)/12 = 115/12
    print(f"P(B_2^4)=pi^4/4 >= 81/4; deficit >= 81/4-32/3 = {deficit_lb:.4f}")
    assert deficit_lb > 9.5
    print("d_BM(B_2^4, B_inf^4) = sqrt(4) = 2 (standard); capped modulus = min{1,2-1}^2 = 1")
    # Indicative (non-rigorous) scan over p in (1,inf) using floating gamma
    print("indicative P(B_p^4) scan (floating point, NOT part of certificate):")
    for p in [1.0, 1.5, 2.0, 4.0, 10.0, float('inf')]:
        if p == 1.0:
            P = 32/3
        elif p == float('inf'):
            P = 32/3
        else:
            q = p/(p-1)
            V = lambda r, n=4: (2*math.gamma(1+1/r))**n / math.gamma(1+n/r)
            P = V(p)*V(q)
        print(f"  p={p}: P~{P:.4f} (min 32/3={32/3:.4f})")
    print("RAY_CONSISTENT")
probe()
