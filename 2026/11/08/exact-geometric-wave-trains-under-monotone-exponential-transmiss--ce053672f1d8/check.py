#!/usr/bin/env python3
"""Finite reproducibility checks for an exact SIR--Lotka--Volterra wave theorem.

Standard-library numerical experiments support the stated example; they are not the proof.
"""
import math

a = b = 0.5
gamma = a + b
v0, h0 = 2.0, 0.5

def energy(v, h):
    return v - b - b * math.log(v / b) + h - a - a * math.log(h / a)

def rhs(v, h):
    return v * (a - h), h * (v - b)

def step(v, h, dt):
    x1, y1 = rhs(v, h)
    x2, y2 = rhs(v + dt * x1 / 2, h + dt * y1 / 2)
    x3, y3 = rhs(v + dt * x2 / 2, h + dt * y2 / 2)
    x4, y4 = rhs(v + dt * x3, h + dt * y3)
    return (v + dt * (x1 + 2*x2 + 2*x3 + x4)/6,
            h + dt * (y1 + 2*y2 + 2*y3 + y4)/6)

hcrit = (a - b + math.sqrt((a - b)**2 + 8*a*b)) / 4
E0 = energy(v0, h0)
E_I = energy(gamma, a)
E_c = energy(b + hcrit, hcrit)
assert E0 > E_I > E_c > 0
assert abs(E0 - (1.5 - 0.5*math.log(4))) < 1e-14

v, h = v0, h0
step_size = 0.002
nsteps = 40000
extrema_I = []
extrema_c = []
last_I = None
last_c = None
max_energy_error = 0.0
for k in range(nsteps+1):
    t = k * step_size
    infective = h * math.exp(-a*t) / 2.5
    incidence = v*h*math.exp(-a*t) / 2.5
    dlog_I = v - gamma
    dlog_c = v - h - b
    if last_I is not None and last_I > 0 >= dlog_I:
        extrema_I.append((t, infective))
    if last_c is not None and last_c > 0 >= dlog_c:
        extrema_c.append((t, incidence))
    last_I = dlog_I
    last_c = dlog_c
    max_energy_error = max(max_energy_error, abs(energy(v,h)-E0))
    if k < nsteps:
        v, h = step(v, h, step_size)
assert len(extrema_I) >= 4, extrema_I
assert len(extrema_c) >= 4, extrema_c
assert max_energy_error < 5e-7, max_energy_error

for sequence in (extrema_I, extrema_c):
    periods = [sequence[i+1][0]-sequence[i][0] for i in range(3)]
    P = sum(periods)/len(periods)
    assert 10 < P < 30
    assert max(periods)-min(periods) < 0.006
    for i in range(3):
        observed_ratio = sequence[i+1][1]/sequence[i][1]
        predicted_ratio = math.exp(-a*periods[i])
        assert abs(observed_ratio/predicted_ratio - 1) < 0.02

# A separate derivative/energy identity check at various interior points.
for vtest, htest in ((0.2,0.1),(0.7,1.5),(2.0,0.5),(10.0,0.4)):
    dv, dh = rhs(vtest, htest)
    dF = (1-b/vtest)*dv + (1-a/htest)*dh
    assert abs(dF) < 1e-12

print('PASS: F conserved; both sharp thresholds crossed; >=4 repeating')
print('      maxima in prevalence and incidence; geometric ratios verified.')
print('example: E=',E0,'prevalence threshold=',E_I,'incidence threshold=',E_c)
print('energy drift:',max_energy_error)
print('first prevalence peaks:',extrema_I[:4])
print('first incidence peaks:',extrema_c[:4])
