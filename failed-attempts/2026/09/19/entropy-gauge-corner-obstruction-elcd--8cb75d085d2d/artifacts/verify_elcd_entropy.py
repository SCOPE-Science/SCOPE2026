#!/usr/bin/env python3
import math

GAMMA = 1.4

def eta(rho, p, c=0.0):
    return -rho/(GAMMA-1.0)*math.log(p/(rho**GAMMA)) + c*rho

def rho_star(pmax, c=0.0):
    return math.exp(-1.0-(GAMMA-1.0)*c/GAMMA)*pmax**(1.0/GAMMA)

def clip(x, lo, hi):
    return max(lo, min(hi, x))

print('gamma =', GAMMA)
for rho,p in [(0.2,0.5),(0.37,1.0),(1.1,2.0)]:
    hrr=GAMMA/((GAMMA-1.0)*rho)
    hrp=-1.0/((GAMMA-1.0)*p)
    hpp=rho/((GAMMA-1.0)*p*p)
    det=hrr*hpp-hrp*hrp
    expected=1.0/((GAMMA-1.0)*p*p)
    print(f'Hessian rho={rho:.2f} p={p:.2f}: det={det:.12f}, formula={expected:.12f}')
    assert abs(det-expected) < 1e-11 and hrr > 0 and det > 0

rlo,rhi,plo,phi=0.2,0.6,0.5,1.0
rs=clip(rho_star(phi),rlo,rhi)
true=eta(rs,phi)
corners=[(r,p,eta(r,p)) for r in (rlo,rhi) for p in (plo,phi)]
corner=min(corners,key=lambda t:t[2])
print(f'continuous rectangle minimizer: rho={rs:.12f}, p={phi:.1f}, eta={true:.12f}')
print(f'best corner: rho={corner[0]:.1f}, p={corner[1]:.1f}, eta={corner[2]:.12f}')
print(f'corner excess = {corner[2]-true:.12f}')
assert rlo < rs < rhi and corner[2] > true

rhoL,rhoR,p=0.25,1.0,1.0
for c in (0.0,-2.0):
    vals=(eta(rhoL,p,c),eta(rhoR,p,c))
    pick='left' if vals[0] <= vals[1] else 'right'
    print(f'gauge c={c:+.1f}: etaL={vals[0]:.12f}, etaR={vals[1]:.12f}, selected={pick}')
assert eta(rhoL,p,0.0) < eta(rhoR,p,0.0)
assert eta(rhoL,p,-2.0) > eta(rhoR,p,-2.0)

# With equal pressure, Algorithm 1 uses the velocity from whichever cell wins.
def eigs_x(rho,u,p):
    a=math.sqrt(GAMMA*p/rho)
    return (u-a,u,u,u+a)
print('x-Jacobian eigenvalues if left cell is selected:', tuple(round(x,12) for x in eigs_x(rhoL,-2.0,p)))
print('x-Jacobian eigenvalues if right cell is selected:', tuple(round(x,12) for x in eigs_x(rhoR,2.0,p)))

cstar=-(eta(rhoR,p)-eta(rhoL,p))/(rhoR-rhoL)
Astar=math.exp(-(GAMMA-1.0)*cstar)
print(f'switch threshold c* = {cstar:.12f}')
print(f'equivalent log-reference factor A* = {Astar:.12f}')

# eta/rho is invariant in ranking under eta -> eta + c rho.
for c in (0.0,-2.0,3.0):
    sL=eta(rhoL,p,c)/rhoL
    sR=eta(rhoR,p,c)/rhoR
    print(f'specific score c={c:+.1f}: left-right difference = {sL-sR:.12f}')
assert abs((eta(rhoL,p,0)/rhoL-eta(rhoR,p,0)/rhoR) -
           (eta(rhoL,p,-2)/rhoL-eta(rhoR,p,-2)/rhoR)) < 1e-12

# Any desired interior density can be made the continuous minimizer by an equivalent gauge.
r_target=0.45
c_target=(math.log(phi)-GAMMA*(math.log(r_target)+1.0))/(GAMMA-1.0)
rs2=rho_star(phi,c_target)
print(f'target rho={r_target:.12f}: gauge c={c_target:.12f}, recovered rho*={rs2:.12f}')
assert abs(rs2-r_target) < 1e-12
