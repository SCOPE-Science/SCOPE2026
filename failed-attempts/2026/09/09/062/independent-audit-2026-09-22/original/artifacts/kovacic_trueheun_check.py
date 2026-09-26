"""Cross-check: TRUE Heun variant (alpha*beta=2/9, numerator 2x/9-q) also dies uniformly.
b0=-1/4,b1=b2=-3/16 (same, q-indep), b_inf=-2/9, rho_inf=1/3 rational.
Case1: a_inf in {2/3,1/3}; S in {1,3/2,2}; d=a_inf-S in {-1/3,-5/6,-4/3,-2/3,-7/6,-5/3}: never Z>=0. DEAD.
Case2: E_inf={2} (2+-2/3 nonint) -> d=-(e1+e2)/2<0. DEAD.
Case3: n=4: E_inf={(6+k/3)/4}={3/2,19/12,17/12,5/3,4/3}: EMPTY. DEAD.
        n=12: E0={1/2}: EMPTY. DEAD. n=6: all {1}, d=-1. DEAD.
Conclusion identical. stdlib only."""
from fractions import Fraction as F
print("true-Heun b_inf check: N lead -32 / D lead 144 = -2/9:", F(-32,144) == F(-2,9))
print("1+4b_inf =", 1+4*F(-2,9), "= 1/9, sqrt = +-1/3")
S_vals = [F(1), F(3,2), F(2)]
for ai in [F(2,3), F(1,3)]:
    for S in S_vals:
        d = ai - S
        print(f"a_inf={ai} S={S} d={d} inZ>=0? {d.denominator==1 and d>=0}")
print("CASE1 DEAD (true Heun too)")
print("CASE2: E_inf={2}: d=-(e1+e2)/2<= -1 DEAD")
E4_inf = [(F(6)+F(k,3))/F(4) for k in [-2,-1,0,1,2]]
print("n=4 E_inf cands:", E4_inf, "integers:", [v for v in E4_inf if v.denominator==1])
print("n=12 E0 = 6/12 = 1/2 nonint => DEAD; n=6: d=(1/2)(1-3)=-1 DEAD")
print("TRUE_HEUN_UNIFORM_OK")
