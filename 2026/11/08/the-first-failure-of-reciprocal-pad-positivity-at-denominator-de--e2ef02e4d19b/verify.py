"""Exact rational certificate for the [k/5] exponential-Pade reciprocal frontier.

Run: python3 verify.py in the directory containing root_centers.json.
Requires only Python's standard library; no floating point operations.
"""
import json
import math
from fractions import Fraction as Q
from pathlib import Path

SCALE=10**9
RADIUS=Q(1,10**6)
TAIL_START=300

def plus(a,b):return(a[0]+b[0],a[1]+b[1])
def multiply(a,b):return(a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0])
def absolute_interval(v):
    x,y=v
    square=x*x+y*y
    lower_integer=math.isqrt((square.numerator*SCALE*SCALE)//square.denominator)
    return Q(lower_integer,SCALE),Q(lower_integer+1,SCALE)
def evaluate(coeff,z):
    val=(Q(0),Q(0))
    for c in reversed(coeff):val=plus(multiply(val,z),(Q(c),Q(0)))
    return val

def polynomial(k):
    # Q_{k,5}(z)=D_k*q_{k,5}(z), D_k=(k+1)...(k+5).
    return [(-1)**j*math.comb(5,j)*math.prod(k+s for s in range(1,6-j)) for j in range(6)]

def check_one(k,root_centers):
    p=polynomial(k)
    D=p[0]
    assert len(root_centers)==5
    z=[(Q(a,SCALE),Q(b,SCALE)) for a,b in root_centers]
    assert z[0][1]==0 and z[0][0]>0
    for i in range(5):
        for j in range(i):
            displacement=(z[i][0]-z[j][0],z[i][1]-z[j][1])
            assert absolute_interval(displacement)[0]>2*RADIUS
    radius_lower=[];radius_upper=[];residue_lower=[];residue_upper=[]
    for i,c in enumerate(z):
        # Taylor coefficients of Q_{k,5} about the exact rational center c.
        t=[evaluate([math.comb(j,h)*p[j] for j in range(h,6)],c) for h in range(6)]
        v0_upper=absolute_interval(t[0])[1]
        v1_lower,v1_upper=absolute_interval(t[1])
        high=sum(absolute_interval(t[h])[1]*RADIUS**h for h in range(2,6))
        # Rouché: linear term dominates the constant and higher terms.
        assert v0_upper+high < v1_lower*RADIUS
        derivative_error=sum(h*absolute_interval(t[h])[1]*RADIUS**(h-1) for h in range(2,6))
        assert derivative_error<v1_lower
        center_lower,center_upper=absolute_interval(c)
        assert center_lower>RADIUS
        radius_lower.append(center_lower-RADIUS)
        radius_upper.append(center_upper+RADIUS)
        residue_lower.append(Q(D,1)/((center_upper+RADIUS)*(v1_upper+derivative_error)))
        residue_upper.append(Q(D,1)/((center_lower-RADIUS)*(v1_lower-derivative_error)))
        if i==0:
            assert t[1][1]==0 and t[1][0]<-derivative_error
    # Exactly one root in each disjoint disk, hence every root is localized.
    assert radius_upper[0] < min(radius_lower[1:])
    # For the real root A_0=-D/(rho*Q'(rho))>0.
    # All remaining residues are bounded in modulus by residue_upper.
    error_bound=sum(residue_upper[i]*(radius_upper[0]/radius_lower[i])**TAIL_START for i in range(1,5))
    assert error_bound < residue_lower[0]
    # Thus c_n>0 for every n >= 300 by partial fractions.
    coefficients=[Q(1)]
    for n in range(1,TAIL_START):
        coefficients.append(-sum(Q(p[j],D)*coefficients[n-j] for j in range(1,min(5,n)+1)))
        assert coefficients[n]>0,(k,n)
    return error_bound/residue_lower[0]

def main():
    centers=json.loads((Path(__file__).resolve().parent/'root_centers.json').read_text(encoding='utf-8'))
    assert len(centers)==66
    worst=Q(0)
    for k in range(66):
        ratio=check_one(k,centers[k])
        if ratio>worst:worst=ratio
    # Source counterexample; computed independently with the same recurrence.
    p=polynomial(66);D=p[0];c=[Q(1)]
    for n in range(1,39):
        c.append(-sum(Q(p[j],D)*c[n-j] for j in range(1,min(5,n)+1)))
    assert c[38]<0
    assert worst < Q(34,100) # uniform explicit exact rational tail margin
    print('VERIFY_OK; k=0..65; c_n>0 for every n>=0; '
          '330 root disks, 19734 positive finite checks (n=1..299); '
          '66 exact tail estimates at n=300; k=66, n=38 negative; '
          'largest tail/leading-residue bound < 17/50')

if __name__=='__main__':main()
