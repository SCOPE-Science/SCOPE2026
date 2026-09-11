"""Replay: HOMFLY-PT of 6_3 from braid BR[3,{-1,-1,2,-1,2,2}] + MFW bound.
Prints VERIFY_OK with the polynomial, min v-degree, and bound."""
import sys; sys.path.insert(0, 'work'); sys.path.insert(0, 'output/artifacts')
sys.setrecursionlimit(100000)
from skein import homfly_braid, fmt
checks = []
checks.append((homfly_braid([], 1) == {(0,0): 1}, 'unknot'))
checks.append((homfly_braid([1], 2) == {(0,0): 1}, 'kink+'))
checks.append((homfly_braid([-1], 2) == {(0,0): 1}, 'kink-'))
checks.append((homfly_braid([1,1,1], 2) == {(2,0):2,(2,2):1,(4,0):-1}, 'trefoil'))
checks.append((homfly_braid([1,-2,1,-2], 3) == {(-2,0):1,(0,0):-1,(0,2):-1,(2,0):1}, 'fig8'))
P = homfly_braid([-1,-1,2,-1,2,2], 3)
KATLAS = {(-2,0):-1,(-2,2):-1,(0,0):3,(0,2):3,(0,4):1,(2,0):-1,(2,2):-1}
checks.append((P == {k: __import__('fractions').Fraction(v) for k,v in KATLAS.items()}, '6_3==katlas'))
for ok, nm in checks: print(('PASS' if ok else 'FAIL'), nm)
print('6_3 HOMFLY:', fmt(P))
print('min v-degree:', min(a for (a,b) in P))
assert all(ok for ok,_ in checks)
print('VERIFY_OK')
