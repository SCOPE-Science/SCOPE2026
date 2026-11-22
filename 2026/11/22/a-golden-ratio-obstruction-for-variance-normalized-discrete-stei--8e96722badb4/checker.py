"""Exact arithmetic checks of finite geometric-edge Stein envelopes.
The proof is analytic; these checks test its finite identities independently.
"""
from fractions import Fraction as Q
from math import sqrt

def exact(q, N, eps):
    assert 0 < q < 1 and 0 < eps < 1 and eps <= 1/q
    a = [q ** (N-j) for j in range(N+1)]
    tail = eps/(1-eps)
    Z = sum(a, Q(0)) + tail
    p = [v/Z for v in a]
    ex1 = (sum((j*a[j] for j in range(N+1)),Q(0)) + N*tail + eps/(1-eps)**2)/Z
    ex2 = (sum((j*j*a[j] for j in range(N+1)),Q(0)) + N*N*tail + 2*N*eps/(1-eps)**2 + eps*(1+eps)/(1-eps)**3)/Z
    var = ex2 - ex1*ex1
    F = Q(0)
    mx = tail # exact supremum in far tail
    checks = 0
    for j in range(N+1):
        F += p[j]
        G = 1-F
        h = F*G/p[j]
        # Closed expression from exact geometric sums and normalization.
        eF_over_p = (1-q**(j+1))/(1-q)
        eG = ((1-q**(N-j))/(1-q)+tail)/Z
        assert h == eF_over_p * eG
        checks += 1
        mx = max(mx,h)
    assert var>0 and mx>0
    return float(mx),float(var),checks

def main():
    total=0
    for q in [Q(1,4), Q(1,3), Q(3,8), Q(2,5), Q(1,2), Q(3,5), Q(4,5)]:
        for N in [4,8,12,20,32,48,64]:
            gamma,var,c=exact(q,N,Q(1,2)**N)
            total+=c+2
            if N>=64:
                target=1/float(1-q)
                target_var=float(q/(1-q)**2)
                assert abs(gamma-target)<0.025
                assert abs(var-target_var)<0.025
                total+=2
    phi=(1+sqrt(5))/2
    qstar=(3-sqrt(5))/2
    assert abs(1/(1-qstar)-phi)<1e-13
    assert abs(1/sqrt(qstar)-phi)<1e-13
    total+=2
    print('PASS',total,'exact identities and finite-limit checks; optimal limiting normalized factor =',phi)
if __name__=='__main__':main()
