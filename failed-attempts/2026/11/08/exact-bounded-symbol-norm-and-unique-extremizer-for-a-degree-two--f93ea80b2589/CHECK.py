"""Numerical diagnostics for a rank-one truncated Toeplitz symbol extremizer.

The analytic proof of optimality is separate; these finite quadratures do not certify it.
Run with Python 3 (standard library only).
"""
from cmath import exp
from math import pi


def compute(r, n=32768):
    v = 2*r/(1+r*r)
    theta_sum = 0.0
    moment_0 = 0j
    moment_pos = 0j
    moment_neg = 0j
    samples=[]
    for j in range(n):
        x = (j+0.5)*2*pi/n
        z = exp(1j*x)
        w=(1-r*r)/abs(1-r*z*z)**2
        g=z-v/z
        mod=abs(g)
        theta_sum+=w*mod
        samples.append((z,w,g,mod))
    F=theta_sum/n
    for z,w,g,mod in samples:
        phi=-g.conjugate()/(F*mod)
        moment_0+=phi*w
        moment_pos+=phi*z*w
        moment_neg+=phi/z*w
        assert abs(abs(phi)-1/F)<1.e-10
    return F,moment_0/n,moment_pos/n,moment_neg/n


def run():
    checks=0
    for r in (0,0.1,0.2,0.5,0.75,0.90,0.95):
        f,m0,mp,mn=compute(r)
        assert abs(m0)<1e-8
        assert abs(mp+1)<2e-7
        assert abs(mn)<2e-7
        assert f>0
        checks+=4
        print(f"r={r:.2f}: v={2*r/(1+r*r):.9f} F={f:.9f} optimal_symbol_norm={1/f:.9f}, moments=(zero {m0:.2g}, pos {mp:.9g}, neg {mn:.2g})")
    print(f"passed: {checks} diagnostics")


if __name__ == '__main__':
    run()
