"""Exact-rational verification of five-site local-TV perturbation amplification.
No external dependencies: Python 3 standard library only.
"""
from fractions import Fraction as Q
from itertools import product

def V(z):
    return sum((abs(b-a) for a,b in zip(z,z[1:])), Q(0))

def prox_five_with_certificate(y, penalty=Q(1)):
    """Enumerate all edge-sign patterns; verify primal-dual KKT exactly."""
    assert len(y)==5 and penalty>0
    valid=[]
    for signs in product((-1,0,1), repeat=4):
        starts=[0]+[k+1 for k,s in enumerate(signs) if s]
        ends=[k for k,s in enumerate(signs) if s]+[4]
        u=[None]*5
        blocks=[]
        for a,b in zip(starts,ends):
            left = Q(signs[a-1]) if a else Q(0)
            right = Q(signs[b]) if b<4 else Q(0)
            mean=(sum(y[a:b+1],Q(0))+penalty*(right-left))/Q(b-a+1)
            for k in range(a,b+1):u[k]=mean
            blocks.append((a,b))
        p=[]; cumulative=Q(0); okay=True
        for k in range(4):
            cumulative+=(u[k]-y[k])/penalty
            p.append(cumulative)
            if signs[k]:
                if p[k]!=signs[k] or signs[k]*(u[k+1]-u[k])<=0:
                    okay=False;break
            elif not (-1<p[k]<1):
                okay=False;break
        if okay:
            assert sum(u)==sum(y)
            valid.append((tuple(u),tuple(signs),tuple(p),tuple(blocks)))
    assert len(valid)==1, ('ambiguous KKT candidate',y,valid)
    return valid[0]

def output_with_certificates(x):
    return [prox_five_with_certificate(x[i:i+5]) for i in range(len(x)-4)]

x=[Q(v,10) for v in (18,-11,-5,18,0,-6,-18,1,3,-3)]
h=[Q(0)]*5+[Q(1)]*5
eta=Q(1,1000)
y=[a+eta*b for a,b in zip(x,h)]
c0=output_with_certificates(x)
c1=output_with_certificates(y)
assert len(c0)==len(c1)==6
z0=[c[0][2] for c in c0]
z1=[c[0][2] for c in c1]
gain=[(a-b)/eta for a,b in zip(z1,z0)]
assert gain==[Q(0),Q(1,3),Q(0),Q(1),Q(2,3),Q(1)]
assert V([b-a for a,b in zip(x,y)])==eta
assert V([b-a for a,b in zip(z0,z1)])==eta*Q(7,3)
assert [c[1] for c in c0]==[c[1] for c in c1]
print('EXACT_RATIONAL_PRIMAL_DUAL_KKT_PASS: 12 five-point windows')
print('FUSED_BLOCK_PARTITIONS')
for i,c in enumerate(c0):
 print(i, c[3],c[1], ['%s'%p for p in c[2]],'centre',str(c[0][2]))
print('OUTPUT_DIFFERENCE_OVER_EPSILON:',[str(q) for q in gain])
print('INPUT_VARIATION:',eta,'OUTPUT_VARIATION:',eta*Q(7,3))
print('FIVE_POINT_COUNTEREXAMPLE_PASS')
