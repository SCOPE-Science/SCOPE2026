#!/usr/bin/env python3
"""Independent finite-state exact-arithmetic checks of the stated kinetic-spin identity.
Runs with Python's standard library only; no external data or package files.
"""
from fractions import Fraction as F
from itertools import product
from math import atanh, isclose

checks = 0
for n in range(3, 10):
    for delta in (F(-3, 4), F(-1, 2), F(0), F(1, 4), F(3, 4)):
        states = tuple(product((-1, 1), repeat=n))
        assert len(states) == 2**n
        v_sum = F(0)
        j_sum = F(0)
        for state in states:
            q = sum(state[i] * state[(i+2)%n] for i in range(n))
            row = F(0)
            lq = F(0)
            j = F(0)
            local_variance = F(0)
            for i in range(n):
                t = state[i] * (state[(i-1)%n] - state[(i+1)%n])
                rate = (1 - delta*F(t,2))/2
                assert rate > 0
                nxt = list(state)
                nxt[i] *= -1
                qn = sum(nxt[k] * nxt[(k+2)%n] for k in range(n))
                lq += rate*(qn-q)
                a_by_eta = -t
                j += rate*a_by_eta
                # h=-eta*delta*Q/4 solves L h = -(j-Ej).
                dh_by_eta = -delta*F(qn-q,4)
                local_variance += rate*(a_by_eta+dh_by_eta)**2
                reverse_t = nxt[i]*(nxt[(i-1)%n]-nxt[(i+1)%n])
                reverse_rate=(1-delta*F(reverse_t,2))/2
                assert reverse_t == -t
                assert reverse_rate == (1+delta*F(t,2))/2
                checks += 3
            assert lq == -2*q
            assert j == delta*F(n-q,2)
            checks += 2
            v_sum += local_variance
            j_sum += j
        v_by_eta2 = v_sum/F(2**n)
        mean_by_eta = j_sum/F(2**n)
        v_expected = F(n)*(1+delta**2*(F(1,2) if n == 4 else F(1,4)))
        mean_expected= F(n)*delta/2
        assert v_by_eta2 == v_expected, (n, delta, v_by_eta2, v_expected)
        assert mean_by_eta == mean_expected
        checks += 2
print('PASS: %d exact-rational assertions for N=3..9 and five nonreciprocity values' % checks)
# The N=3 case is an independent consistency check; the new claim covers N>=4.
# Check independent spectral derivative on finite state Markov generators.
try:
    import numpy as np
    for n in (4, 5, 6):
        d=0.43
        eta=atanh(d)
        states=tuple(product((-1,1), repeat=n))
        index={s:i for i,s in enumerate(states)}
        def tilted(s):
            mat=np.zeros((2**n,2**n),dtype=float)
            for src,st in enumerate(states):
                for i in range(n):
                    t=st[i]*(st[(i-1)%n]-st[(i+1)%n])
                    w=0.5*(1-0.5*d*t)
                    dest=list(st);dest[i]*=-1
                    mat[index[tuple(dest)],src]+=w*np.exp(s*eta*t)
                    mat[src,src]-=w
            return mat
        h=2e-3
        def lam(s):return max(np.linalg.eigvals(tilted(s)).real)
        v=(lam(h)-2*lam(0)+lam(-h))/h**2
        expected=n*eta**2*(1+d*d*(0.5 if n==4 else 0.25))
        assert isclose(v,expected,rel_tol=3e-5,abs_tol=1e-5),(n,v,expected)
        checks += 1
    print('PASS: independent tilted-generator eigenvalue curvature, N=4,5,6')
except ImportError:
    print('OPTIONAL: NumPy not present, spectral cross-check skipped; exact proof and rational checks unaffected')
print('TOTAL checks:',checks)
