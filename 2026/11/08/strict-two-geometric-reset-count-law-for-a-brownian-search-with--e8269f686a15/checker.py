#!/usr/bin/env python3
"""Numerical diagnostics for a gated Brownian target's reset-count distribution.

Only mathematical calculations and assertions are included; the analytical
proof of the infinite reset-count law is given separately in RESULT.md.
Run: python3 checker.py
"""
import math
import random


def compute(p, r, c, d, a):
    q = 1.0 - p
    z = r / (r + c)
    A = math.sqrt((r + c) / r)
    u = math.exp(-a * math.sqrt(r / d))
    v = math.exp(-a * math.sqrt((r + c) / d))
    B = q + p * A
    h = (p * (A * u - v) / B, (p * A * u + q * v) / B)
    U = ((q + p * z, p * (1.0 - z)),
         (q * (1.0 - z), p + q * z))
    K = tuple(tuple(U[i][j] - h[i] * U[1][j] for j in range(2)) for i in range(2))
    s = 1.0 - p * A * u / B
    tr = K[0][0] + K[1][1]
    det = K[0][0] * K[1][1] - K[0][1] * K[1][0]
    disc = math.sqrt(max(0.0, tr * tr - 4.0 * det))
    lm, lp = (tr - disc) / 2.0, (tr + disc) / 2.0
    wp = (s - lm) / (lp - lm)
    wm = 1.0 - wp
    return locals()


def near(x, y, atol=1e-11, rtol=2e-10):
    return abs(x-y) <= atol + rtol * max(abs(x), abs(y))


def run():
    rng = random.Random(1729)
    tests = 0
    cases = [(0.5, 1.0, 1.0, 1.0, 1.0)]
    for _ in range(320):
        cases.append((rng.uniform(0.08, 0.92), 10**rng.uniform(-0.5, 0.5),
                      10**rng.uniform(-0.7, 1.2), 10**rng.uniform(-0.4, 0.4),
                      10**rng.uniform(-0.4, 0.35)))
    for p, r, c, d, a in cases:
        obj = compute(p, r, c, d, a)
        q,z,A,u,v,B,h,U,K,s,tr,det,lm,lp,wp,wm = (
            obj[k] for k in ('q','z','A','u','v','B','h','U','K','s','tr','det','lm','lp','wp','wm'))
        assert 0 < h[0] < h[1] < 1
        tests += 1
        assert 0 < lm < s < lp < 1 and 0 < wp < 1 and 0 < wm < 1
        tests += 1
        assert near(wp+wm, 1)
        tests += 1
        assert all(K[i][j] > 0 for i in range(2) for j in range(2))
        tests += 1
        assert all(near(K[i][0]+K[i][1], 1-h[i]) for i in range(2))
        tests += 1
        assert near(det, z*(1-h[1]))
        tests += 1
        assert near(tr, 1+z-(p*A*u + q*z*v)/B)
        tests += 1
        assert near((s-lm)*(s-lp), -p*q*u*v/(A*B**2))
        tests += 1
        assert near(q*h[0]+p*h[1], p*A*u/B)
        tests += 1
        # Verify the count law via a distinct matrix-power computation.
        row=(q,p)
        for n in range(22):
            raw = row[0]*h[0]+row[1]*h[1]
            mixed = (wm*(1-lm)*lm**n + wp*(1-lp)*lp**n)
            assert near(raw,mixed,atol=2e-12)
            tests += 1
            row = (row[0]*K[0][0]+row[1]*K[1][0],
                   row[0]*K[0][1]+row[1]*K[1][1])
        m_minus=lm/(1-lm); m_plus=lp/(1-lp)
        mean=wm*m_minus+wp*m_plus
        var=mean+mean**2+2*wm*wp*(m_plus-m_minus)**2
        assert var>mean*(1+mean)
        tests += 1
        # Source mean first-passage identity; compensator gives E[N]=r E[tau].
        theoretical_T = (1/u-1)/r + (q/p) * (1/u) * (1/(r*A)) * (1+(r/c)*v)
        assert near(mean, r*theoretical_T,atol=5e-10)
        tests += 1
        # Mixtures of two different geometrics have strictly decreasing hazard.
        hz=[]
        for n in range(8):
            survival=wm*lm**n+wp*lp**n
            survival_next=wm*lm**(n+1)+wp*lp**(n+1)
            hz.append(1-survival_next/survival)
        assert all(hz[i]>=hz[i+1]-1e-13 for i in range(7))
        tests += 1
    print('PASS:',tests,'deterministic diagnostics across',len(cases),'parameter configurations')
    print('Illustrative parameters: p=1/2, r=c=D=a=1')
    obj = compute(0.5,1,1,1,1)
    print('eigenvalues:',repr(obj['lm']),repr(obj['lp']))
    print('positive weights:',repr(obj['wm']),repr(obj['wp']))

if __name__ == '__main__': run()
