#!/usr/bin/env python3
"""Independent numerical checks for a two-mode sampled-oscillator phase-density theorem.

All loops use exact intersections of analytic sampling-interval windows;
none of these finite checks substitutes for the averaging proof.
"""
import math
import cmath

PI = math.pi
A = PI / 2

def exact_stable_measure(epsilon, horizon):
    """Exact Lebesgue measure, up to floating-point rounding, via window intersections."""
    assert epsilon > -1 and horizon >= 0
    w = 1.0 + epsilon
    b = 2.0 * math.atan(w)
    total = 0.0
    for k in range(int(horizon/(2*PI))+1):
        lo = 2*PI*k
        hi = min(lo + A, horizon)
        if hi <= lo: continue
        jl = max(0, int(w*lo/(2*PI))-1)
        jr = int(w*hi/(2*PI))+2
        for j in range(jl, jr+1):
            left = 2*PI*j/w
            right = (2*PI*j+b)/w
            total += max(0.0, min(hi,right)-max(lo,left))
    return total

def primitive(L):
    if L <= A:
        return A*L-L**2/2
    if L <= 2*PI-A:
        return A**2/2
    return A**2/2 + (L-(2*PI-A))**2/2

def crossover(L):
    assert L > 0
    q = int(L/(2*PI))
    r = L - q*2*PI
    return (q*A*A+primitive(r))/(2*PI*L)

def step_factor(omega,h):
    return (1+1j/omega)*cmath.exp(1j*omega*h)-1j/omega

checks = 0
for omega in [0.7,1.0,1.05,1.7,3.0]:
    for h in [0.001,0.4,1.0,3.2,6.3,9.4,14.9]:
        phase = omega*h % (2*PI)
        analytic = 1+2/(omega*omega)*(1-math.cos(omega*h))-2/omega*math.sin(omega*h)
        assert abs(abs(step_factor(omega,h))**2-analytic)<1e-12
        criterion = 0<phase<2*math.atan(omega)
        assert (abs(step_factor(omega,h))<1-1e-12)==criterion or abs(abs(step_factor(omega,h))-1)<1e-12
        checks += 2
for L in [0.13,0.5,A-1e-6,A,A+1e-6,PI,3*PI/2-1e-6,3*PI/2,3*PI/2+1e-6,2*PI,2*PI+1e-6,5*PI,20*PI]:
    val=crossover(L)
    assert 0<val<=.25
    checks += 1
for L in [1.0,PI,4.0, PI*math.sqrt(10)/2,2*PI,3*PI,7*PI]:
    for e in [0.01,0.002]:
        estimate=exact_stable_measure(e,L/e)/(L/e)
        # A rigorous error constant is established in the paper, not from these tests.
        assert abs(estimate-crossover(L))<8*e
        checks += 1
star = PI*math.sqrt(10)/2
starval=(math.sqrt(10)-3)/4
assert abs(crossover(star)-starval)<1e-14
assert crossover(star-.2)>starval and crossover(star+.2)>starval
checks += 3
for t in [0.002,0.1,1,2,4,6,9,12,30,60,150]:
    assert crossover(t)+1e-12>=starval
    checks+=1
for e in [math.sqrt(2)-1, math.sqrt(3)-1]:
    observed=exact_stable_measure(e,60000)/60000
    expected=math.atan(1+e)/(4*PI)
    assert abs(observed-expected)<0.0003, (e,observed,expected)
    checks+=1
assert abs(exact_stable_measure(0.0,200*PI)/(200*PI)-0.25)<1e-12
checks+=1
print(f'VERIFY_PASS: {checks} analytic and independent window-overlap checks')
print(f'L_star = {star:.15f}, F_min = {starval:.15f}')
for e in [0.02,0.005,0.001]:
    print(f'epsilon={e}: P_epsilon(L_star/epsilon)={exact_stable_measure(e,star/e)/(star/e):.12f}')
