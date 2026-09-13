import numpy as np, sys
sys.path.insert(0,'output/artifacts')
from delta import eu, es, lam, mu, apply_B, r, B, Binv
# S_m(y) = sum_{k>=0} exp(2 pi i m.(B^k y)) mu^k ... derive coefficient map
# Fourier mode m in Z^2: term T_k(y) = sum over 4 corners c_j exp(2pi i m.B^k(y+d_j)) with corner offsets
# T_k(y) = exp(2pi i (B^{-T k} m).y) * C(m,k,a,b) where phase factor per corner.
# For fixed corner offsets d in {0, a eu, b es, a eu+b es}: corner phase = exp(2pi i m.B^k d).
# So F_mk = rhat_m * C(m,k) with C = e(m.B^k(aeu+bes)) - e(m.B^k aeu) - e(m.B^k bes) + 1.
# C = (e_A - 1)(e_B - 1), A=m.B^k a eu (scalar), B_=m.B^k b es.
# rhat: m=(1,0): -0.02i; m=(-1,0): +0.02i; m=(0,1): 0.015; m=(0,-1): 0.015.
# Backward sum similarly: G_mj corners with B^{-j}, sign pattern from Delta def:
# back summand: r(x^{-j}) - r(xu^{-j}) + r(xus^{-j}) - r(xs^{-j}) = -(corner pattern with +1,-1,+1,-1 on (0,aeu,aeu+bes,bes))
# = -C(m,-j) e(m.B^{-j} y). Same C formula.
# So F_m(a,b) = rhat_m * [sum_{k>=0} C(m,k) + sum_{j>=1} (-C(m,-j))].
# Key: C decays? |e_A-1| ~ 2pi|A|; A forward ~ lam^k a (m_k . eu)|...| grows; backward decays. Product stays bounded; convergence from rhat? No: each C is O(1)?? Hmm - forward: A grows (unstable stretch, phase wraps), B_ decays; (e_A-1) O(1) oscillatory, (e_B-1) ~ O(mu^k b). So C ~ O(mu^k): summable. Backward: A decays O(mu^j), B_ grows O(lam^j) oscillatory, C ~ O(mu^j): summable. Great, both summable via the contracting factor.
# Check numerically: compute F_m for a=b=0.03 etc.
def Ccoef(m, k, a, b):
    # m: array(2) int; k int (can be neg)
    if k>=0: Mk = np.linalg.matrix_power(B,k)
    else: Mk = np.linalg.matrix_power(Binv,-k)
    w = Mk.T @ m  # m.B^k as row -> (B^k)^T m
    A = float(w @ (a*eu)); Bb = float(w @ (b*es))
    return (np.exp(2j*np.pi*A)-1)*(np.exp(2j*np.pi*Bb)-1)
def Fmode(m, a, b, K=40):
    m=np.array(m,float)
    s = sum(Ccoef(m,k,a,b) for k in range(0,K+1)) - sum(Ccoef(m,-j,a,b) for j in range(1,K+1))
    return s
rhat = {(1,0):-0.02j, (-1,0):0.02j, (0,1):0.015, (0,-1):0.015}
for (a,b) in [(0.03,0.03),(0.03,-0.03),(0.015,0.015)]:
    print("a,b",a,b)
    for m in [(1,0),(-1,0),(0,1),(0,-1)]:
        print("  ",m, Fmode(m,a,b), "|F|",abs(Fmode(m,a,b)))
# tail check
for m in [(1,0),(0,1)]:
    print(m, [abs(sum(Ccoef(np.array(m,float),k,0.03,0.03) for k in range(K,K+5))) for K in [10,20,30]])
