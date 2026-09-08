"""Singular series S(H), HL vs naive predictions, integral forms."""
import json, math
import numpy as np

H = [0, 2, 6, 8, 30, 32, 36, 38, 42]
K = 9
LIM = 100000
sieve = bytearray(b'\x01') * (LIM + 1)
sieve[0] = sieve[1] = 0
for i in range(2, int(LIM**0.5) + 1):
    if sieve[i]:
        sieve[i*i:LIM+1:i] = b'\x00' * (((LIM - i*i)//i) + 1)
primes = [i for i in range(2, LIM + 1) if sieve[i]]

def nu(p):
    return len({h % p for h in H})

logP2000, logP100k = 0.0, 0.0
nu_small = {}
for p in primes:
    v = nu(p)
    if p <= 43:
        nu_small[p] = v
    assert v < p, (p, v)
    t = math.log(1 - v/p) - K*math.log(1 - 1/p)
    if p <= 2000:
        logP2000 += t
    logP100k += t
P2000 = math.exp(logP2000)
P100k = math.exp(logP100k)
# Rigorous tail. For p > 9, with f(p) = (1-9/p)(1-1/p)^{-9}:
#   ln f(p) = -sum_{k>=1} (9/p)^k/k + 9 sum_{k>=1} (1/p)^k/k
#           = sum_{k>=1} (9-9^k)/(k p^k).
# k=1 term is 0; every k>=2 term is strictly negative. Hence ln f(p) < 0 and
#   ln f(p) >= -36/p^2 - (1/3)(9/p)^3/(1-9/p)   [k=2 exact; k>=3 via 1/k<=1/3]
# For p >= 1e5 the correction is <= 2.44e-13 * (1e5/p)^3 * ... bounded below by
# per-p cubic sum C/p^3, C=243.1; sum_{p>1e5} 1/p^3 <= sum_{n>1e5} 1/n^3 <= 5e-11.
S1 = 1e-5       # sum_{p>1e5} 1/p^2 <= sum_{n>1e5} 1/n^2 <= int_{1e5}^oo dx/x^2
S2 = 5.1e-11    # sum_{p>1e5} 1/p^3 <= 1/(2 (1e5)^2) + tiny
C3 = 243.1
lo_tail = math.exp(-36*S1 - C3*S2)
hi_tail = 1.0
S_mid, S_lo, S_hi = P100k, P100k*lo_tail, P100k*hi_tail

X = 1e9
L = math.log(X)
lead = X/(L**K)
HL_lead = S_mid*lead

def simpson(a, b, N):
    u = np.linspace(a, b, 2*N + 1)
    f = np.exp(u - K*np.log(u))
    h = (b - a)/(2*N)
    return h/3*(f[0] + f[-1] + 4*f[1:-1:2].sum() + 2*f[2:-1:2].sum())

I_full = float(simpson(math.log(2), L, 100000))
I_trunc = float(simpson(math.log(50), L, 100000))

out = {
    "H": H, "k": K,
    "nu_small": {str(p): v for p, v in nu_small.items()},
    "partial_product_to_2000": P2000,
    "partial_product_to_100k": P100k,
    "tail_interval": [lo_tail, hi_tail],
    "S_mid": S_mid, "S_interval": [S_lo, S_hi],
    "X": X, "logX": L,
    "naive_leading_term": lead,
    "HL_leading_term": HL_lead,
    "enhancement_ratio_S": S_mid,
    "integral_full_2_to_X": I_full,
    "integral_trunc_50_to_X": I_trunc,
    "HL_integral_full": S_mid*I_full,
    "HL_integral_trunc50": S_mid*I_trunc,
}
with open("output/artifacts/singular.json", "w") as f:
    json.dump(out, f, indent=1)
print(json.dumps(out, indent=1))
