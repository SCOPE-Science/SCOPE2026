"""BFS ideal-class enumeration + Brandt matrices for disc 109. L-coords valid for odd-norm ideals (3∤[O:L]... but ideals may have even norm! Use O-coords: basis {1,i,j,v} with v=(i+k)/2.
Convert: x=(x0,x1,x2,x3)_L = c0*1+c1*i+c2*j+c3*v with x1=c1+c3/2, x3=c3/2 → c3=2x3, c1=x1-x3. So O-coords c=(x0,x1-x3,x2,2x3), x=(c0,c1+c3/2,c2,c3/2).
Right multiplication by generators in O-coords; subideal HNF in O-coords."""
from fractions import Fraction
from itertools import product
import numpy as np, json, sys
sys.path.insert(0,'output/artifacts')
from hnf import hnf_full_rank

def mulL(a,b):
    a0,a1,a2,a3=a; b0,b1,b2,b3=b
    return (a0*b0-2*a1*b1-109*a2*b2-218*a3*b3, a0*b1+a1*b0+109*a2*b3-109*a3*b2,
            a0*b2+a2*b0-2*a1*b3+2*a3*b1, a0*b3+a3*b0+a1*b2-a2*b1)
def toL(c):
    c0,c1,c2,c3=c  # O-coords, c3 even? no: c general integers; x=(c0, c1+c3/2, c2, c3/2)
    return (Fraction(c0),Fraction(c1)+Fraction(c3,2),Fraction(c2),Fraction(c3,2))
def toO(x):
    x0,x1,x2,x3=x
    c3=2*x3; c1=x1-x3
    assert c3.denominator==1 and c1.denominator==1 and x0.denominator==1 and x2.denominator==1
    return (int(x0),int(c1),int(x2),int(c3))
# right-mult-by-generator matrices in O-coords (columns? rows = images of basis)
OBAS=[(1,0,0,0),(0,1,0,0),(0,0,1,0),(0,0,0,1)]
GENS_O=[(1,0,0,0),(0,1,0,0),(0,0,1,0),(0,0,0,1),(-1,0,0,0),(0,-1,0,0),(0,0,-1,0),(0,0,0,-1)]
# add key gens: i, j, v in O-coords: i=(0,1,0,0), j=(0,0,1,0), v=(0,0,0,1); also k = 2v-i = (0,-1,0,2)
GENS_O += [(0,1,0,0),(0,0,1,0),(0,0,0,1),(0,-1,0,2)]
def rmulO(c,g):
    return toO(mulL(toL(c),toL(g)))
RM={g:np.array([rmulO(e,g) for e in OBAS],dtype=int) for g in set(GENS_O)}
print("right-mult matrices ok", flush=True)
# O itself HNF = identity. Norm of ideal with HNF basis B (O-coords): N = sqrt(det B /det O)= sqrt(det B) since O=I.
# theta fingerprint: enumerate x in lattice with N(x)<=bound, values N(x)/N(J).
QMAT=np.diag([1.0,2.0,109.0,218.0])  # in L-coords
def theta_fp(B_O, nvals=24, bound=200):
    B=np.array(B_O,dtype=float)  # rows O-coords
    # convert rows to L
    BL=np.array([[r[0],r[1]+r[3]/2,r[2],r[3]/2] for r in B])
    # enumerate coeffs: bound each |c| by sqrt(bound/min-eig)... brute force box
    inv=BL  # x = c @ BL
    # coefficient bound: ||c|| <= sqrt(bound)*||BL^{-1}||
    Bi=np.linalg.inv(BL)
    cb=int(np.ceil(np.sqrt(bound)*np.linalg.norm(Bi,ord=2)))+1
    vals=[]
    R=range(-cb,cb+1)
    for c in product(R,repeat=4):
        if all(v==0 for v in c): continue
        x=np.array(c,dtype=float)@BL
        q=float(x@QMAT@x)
        if q<=bound: vals.append(q)
    vals=np.array(sorted(vals))
    N=round(abs(np.linalg.det(BL))/np.sqrt(4*109**2))  # N(J)=sqrt([O:J]); [O:J]=det(B_O rows as O-lattice)... det in O-coords directly:
    # det rows (O-coords) = [O:J] since O=I in these coords
    idx=round(abs(np.linalg.det(np.array(B,dtype=float))))
    NJ=int(round(np.sqrt(idx)))
    assert NJ*NJ==idx, (idx,NJ)
    return tuple(round(v/NJ,6) for v in vals[:nvals]), NJ
fp, n = theta_fp(np.eye(4,dtype=int))
print("O fp:", fp, "N:", n, flush=True)
