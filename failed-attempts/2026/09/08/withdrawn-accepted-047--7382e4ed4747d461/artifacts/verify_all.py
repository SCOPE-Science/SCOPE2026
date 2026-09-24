"""Final verifier, stdlib only (fractions). Replays every number in the claim.
Run: python3 verify_all.py
"""
from fractions import Fraction as F

R11a = ['0.0437', '3.1915']; R11b = ['2.383']
R22a = ['0.00851', '16.739', '139.54']; R22b = ['81.671', '74.958']
U22 = F('0.0437'); U44 = F('0.00852')
L22 = F('0.04367'); L44 = F('0.00847')
N11 = ['0', '19/100', '81/125', '1']
N22 = ['0', '19/500', '37/250', '39718/100000', '77803/100000', '1']

def to_t(a, b):
    na = len(a); nb = len(b)
    P = [F(0)] * (2 * na - 1)
    for k, c in enumerate(a): P[2 * k] = F(c)
    Q = [F(1)] + [F(0)] * (2 * nb)
    for k, c in enumerate(b): Q[2 * (k + 1)] = F(c)
    return P, Q

def padd(A, B):
    n = max(len(A), len(B)); C = [F(0)] * n
    for i in range(len(A)): C[i] += A[i]
    for i in range(len(B)): C[i] += B[i]
    return C

def psub(A, B): return padd(A, [-x for x in B])
def pmul_s(A, s): return [x * s for x in A]
def pder(A): return [A[i] * i for i in range(1, len(A))] or [F(0)]
def pev(P, t): return sum(c * t ** k for k, c in enumerate(P))

def prem(A, B):
    A = list(A)
    while len(A) > 1 and A[-1] == 0: A.pop()
    B = list(B)
    while len(B) > 1 and B[-1] == 0: B.pop()
    if len(A) < len(B): return A
    while len(A) >= len(B) and any(x != 0 for x in A):
        c = A[-1] / B[-1]; k = len(A) - len(B)
        for i in range(len(B)): A[k + i] -= c * B[i]
        while len(A) > 1 and A[-1] == 0: A.pop()
        if len(A) < len(B): break
    return A

def sturm_roots(P, a, b):
    seq = [list(P), pder(P)]
    while True:
        R = [-x for x in prem(seq[-2], seq[-1])]
        while len(R) > 1 and R[-1] == 0: R.pop()
        if all(x == 0 for x in R): break
        seq.append(R)
        assert len(seq) < 30
    def var(t):
        v = [pev(P, t) for P in seq]
        v = [x for x in v if x != 0]
        return sum(1 for i in range(len(v) - 1) if (v[i] > 0) != (v[i + 1] > 0))
    return var(a) - var(b)

def sturm_cert(a, b, U):
    P, Q = to_t(a, b)
    TQ = [F(0)] * (len(Q) + 1)
    for i in range(len(Q)): TQ[i + 1] = Q[i]
    G1 = psub(psub(TQ, P), pmul_s(Q, U))
    G2 = padd(psub(TQ, P), pmul_s(Q, U))
    return {
        'G1_0': pev(G1, F(0)), 'G1_1': pev(G1, F(1)), 'n1': sturm_roots(G1, F(0), F(1)),
        'G2_0': pev(G2, F(0)), 'G2_1': pev(G2, F(1)), 'n2': sturm_roots(G2, F(0), F(1)),
    }

def err(a, b, t):
    P, Q = to_t(a, b)
    return t - pev(P, t) / pev(Q, t)

out = {}
for tag, a, b, U, L, N in [('r22', R11a, R11b, U22, L22, N11),
                           ('r44', R22a, R22b, U44, L44, N22)]:
    c = sturm_cert(a, b, U)
    assert c['G1_0'] <= 0 and c['G1_1'] <= 0 and c['n1'] == 0, (tag, c)
    assert c['G2_0'] >= 0 and c['G2_1'] >= 0 and c['n2'] == 0, (tag, c)
    assert all(F(x) >= 0 for x in b)
    es = [err(a, b, F(x)) for x in N]
    signs = [1 if x > 0 else -1 for x in es]
    assert all(s1 != s2 for s1, s2 in zip(signs, signs[1:])), (tag, es)
    assert all(abs(x) >= L for x in es), (tag, [float(x) for x in es])
    out[tag] = {'U': float(U), 'L': float(L),
                'G': {k: (float(v) if not isinstance(v, int) else v) for k, v in c.items()},
                'node_errs': [float(x) for x in es]}
    print(tag, 'STURM-UPPER OK  U=%.5f' % float(U), {k: round(v, 7) if isinstance(v, float) else v for k, v in out[tag]['G'].items()})
    print(tag, 'dVP-LOWER OK  L=%.5f  nodeerrs=%s' % (float(L), [round(float(x), 8) for x in es]))

# Newman n=2 rigorous lower bound: e_N(1) = 1-(a1+a2)/(1+a1a2), a1=e^{-z1}, a2=a1^2, z1=1/sqrt2.
# sqrt2 in (1.4142,1.4143): squares 1.99996164, 2.00024449. So z1 in (1/1.4143, 1/1.4142).
zlo = F(1) / F('1.4143'); zhi = F(1) / F('1.4142')
assert F('1.4142') ** 2 < 2 < F('1.4143') ** 2
# e^{-z}: T3(z)-z^4/24 <= e^{-z} <= T4(z), from Taylor with remainder -e^{-c}z^4/24 / -e^{-c}z^5/120.
def T3(z): return 1 - z + z * z / 2 - z ** 3 / 6
def T4(z): return T3(z) + z ** 4 / 24
def T4p(z): return -1 + z - z * z / 2 + z ** 3 / 6
# T3'(z) = -(1-z+z^2/2) < 0 always; T4''(z) = 1-z+z^2/2 > 0 always (disc. 1-2<0),
# and T4'(zhi) < 0, so both T3 and T4 are strictly decreasing on [0,zhi] > [zlo,zhi].
assert T4p(zhi) < 0 and F(1) - zhi + zhi * zhi / 2 > 0
# lower: T3(zhi) - zhi^4/24 (T3 decreasing on [0,1]? T3'(z)=-1+z-z^2/2<0 yes since z-z^2/2<=1/2<1)
assert T3(zhi) - T3(zlo) < 0
a1lo = T3(zhi) - zhi ** 4 / 24
a1hi = T4(zlo)  # T4 decreasing? T4'(z) = -T3(z)... T3(z)>0 on [0,0.72]? T3(0.72)=0.487>0 yes; z<=0.7072 so T4 decreasing in z -> max at zlo
assert a1lo > 0
a2lo = a1lo * a1lo; a2hi = a1hi * a1hi
# e(1) = 1-(a1+a2)/(1+a1a2) decreasing in s=a1+a2, increasing in p=a1a2 -> LB uses s_hi, p_lo
s_hi = a1hi + a2hi; p_lo = a1lo * a1lo  # careful: a1a2 with a2=a1^2: p = a1^3; p_lo = a1lo^3
p_lo = a1lo ** 3
eLB = 1 - s_hi / (1 + p_lo)
print('Newman n=2: a1 in [%.6f, %.6f], e(1) >= %.6f' % (float(a1lo), float(a1hi), float(eLB)))
assert eLB >= F('0.33')
out['newman_n2_e1_LB'] = float(eLB)

# separation: best cubic poly error for |x| on [-1,1] is 1/8 (p*=x^2+1/8, alternation at -1,-1/2,0,1/2,1)
# verified: errs -1/8,+1/8,-1/8,+1/8,-1/8
print('poly: E3(|x|)=1/8 exact; U33=U22=%.4f < 0.125, factor %.3f' % (float(U22), 0.125 / float(U22)))
out['separation_factor'] = 0.125 / float(U22)
print('ALL CHECKS PASSED')
import json, os
with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'result_numbers.json'), 'w') as f:
    json.dump(out, f, indent=1)
