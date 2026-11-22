"""Finite arithmetic and simulation checks for the scalar variation-memory theorem.

Run: python3 verify.py  (Python 3 standard library only).
The infinite-time proof is mathematical and is not replaced by these tests.
"""
from fractions import Fraction as Q
import math
import random


def run_path(curvatures, x0, step, epsilon):
    """Exact source ordering: observe gradient, update accumulated difference, step."""
    x = float(x0)
    prev_g = 0.0
    energy = 0.0
    traj = []
    for a in curvatures:
        g = a*x
        increment = (g-prev_g)**2
        energy += increment
        w = epsilon + math.sqrt(energy)
        new_x = x - step*g/w
        assert math.isfinite(energy) and math.isfinite(new_x)
        assert energy >= 0.0 and w >= epsilon
        assert math.isclose(new_x, (1.0-step*a/w)*x, rel_tol=2e-11, abs_tol=2e-11)
        traj.append((x,g,w,energy,new_x,a))
        prev_g = g
        x = new_x
    return traj


def finite_algebra():
    n = 0
    # The descent inequality on the stabilised interval.
    for i in range(101):
        t = Q(i,100)
        assert 2*t-t*t >= t
        n += 1
    # Difference-square upper bound at arbitrary signed gradients.
    for i in range(-12,13):
        for j in range(-12,13):
            u,v=Q(i,7),Q(j,9)
            assert (u-v)**2 <= 2*u*u+2*v*v
            n+=1
    # Elementary sqrt(A) telescoping bound for A >= C^2.
    for j in range(1,101):
        for k in range(0,j+1):
            # Comparison is checked numerically; the proof uses a rational bound.
            A=float(j)
            B=float(k)
            C=math.sqrt(A)
            den=C+2*math.sqrt(A)
            left=(A-B)/den
            right=(math.sqrt(A)-math.sqrt(B))/3
            assert left+1e-12>=right
            n+=1
    return n


def sampled_paths():
    cases = 0
    # Deterministic adversarial curvature sequences plus Bernoulli cases.
    for L in (0.25,1.0,3.0):
        for eta in (0.2,1.9,12.0,80.0):
            for eps in (0.01,0.6):
                for p in (0.07,0.37,0.91):
                    rng=random.Random(1003+cases)
                    n=6000
                    seq=[L if rng.random()<p else 0.0 for _ in range(n)]
                    traj=run_path(seq,-0.7,eta,eps)
                    # Once w > eta L/2, every subsequent active step contracts.
                    stable=[idx for idx, (_,_,w,_,_,_) in enumerate(traj) if w>eta*L/2]
                    assert stable
                    idx=stable[0]
                    for x,g,w,S,nx,a in traj[idx:]:
                        assert abs(nx) <= abs(x)*(1+1e-12)
                    assert abs(traj[-1][4]) < abs(traj[0][0])*1e-6
                    # Check finite-variation behaviour on the observed trajectory:
                    mid=traj[n//2-1][3]
                    end=traj[-1][3]
                    assert end >= mid >=0
                    assert end-mid < 1e-6*(1+end)
                    cases+=1
    # All-zero gradient sequence, and an adversarial non-stochastic sequence.
    t=run_path([0.0]*1000,2.0,500.0,0.001)
    assert t[-1][4]==2.0 and t[-1][3]==0.0
    for seq in ([0.0]*100+[1.0]*500, [1.0 if j%2==0 else 0.0 for j in range(1000)]):
        t=run_path(seq,0.8,30.0,0.05)
        assert t[-1][3] < 1e10
        cases += 1
    return cases


if __name__=='__main__':
    n=finite_algebra()
    m=sampled_paths()
    print(f'PASS: {n} elementary checks and {m} sample-path cases; the infinite-time argument is in RESULT.md')
