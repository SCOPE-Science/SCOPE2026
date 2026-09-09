"""Effective threshold schema from Bisain-type error to the 1-1/40 cap.
Replay: python3 threshold.py
Error model (Bisain Thm 1.1, eq 6): |<mu_j,Theta0> - m| <= C(Theta0) * lam^{-d} * log(lam),
lam = 1/4+t^2. With m<=0.5535, gap g>=0.4215, need error < g/2 ~ 0.21.
Illustrates T* for hypothetical (C,d); real C,d come from cited H hypothesis.
"""
import mpmath as mp
mp.mp.dps = 30
m = mp.mpf('0.55349832')
g = mp.mpf('0.975') - m
print(f"m<={m}, gap g={g}, need err<{g/2}")
def Tstar(C, d):
    # solve C*lam^{-d}*log(lam) = g/2, lam=1/4+t^2
    f = lambda L: C*L**(-d)*mp.log(L) - g/2
    lo, hi = mp.mpf('2'), mp.mpf('10')
    while f(hi) > 0: hi *= 10
    for _ in range(200):
        mid = (lo+hi)/2
        if f(mid) > 0: lo = mid
        else: hi = mid
    L = (lo+hi)/2
    return mp.sqrt(L-mp.mpf('0.25')), L
for C, d in [(10,0.01),(100,0.02),(1000,0.05),(10,0.1)]:
    t, L = Tstar(mp.mpf(C), mp.mpf(d))
    print(f"C={C} d={d}: lam*={float(L):.6g} t*={float(t):.6g}")
print("THRESHOLD_OK")
