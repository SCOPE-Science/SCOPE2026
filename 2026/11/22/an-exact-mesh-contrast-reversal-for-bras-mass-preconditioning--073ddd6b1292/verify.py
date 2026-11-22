"""Exact-rational finite checks for the alternating-mesh mass-preconditioner theorem.
The theorem for all mesh sizes and all contrasts is proved analytically in RESULT.md;
finite instances below exercise the assembly, transformations and extremal modes.
Requires only the Python standard library.
"""
from fractions import Fraction as F


def add(A, B):
    return [[x+y for x,y in zip(a,b)] for a,b in zip(A,B)]


def mult(A,B):
    return [[sum(x*y for x,y in zip(row,col)) for col in zip(*B)] for row in A]


def mv(A,v):
    return [sum(x*y for x,y in zip(row,v)) for row in A]


def mat(n, lengths, weighted=False):
    M=[[F(0) for _ in range(n)] for _ in range(n)]
    BI=[[F(0) for _ in range(n)] for _ in range(n)]
    BW=[[F(0) for _ in range(n)] for _ in range(n)]
    a,b=lengths[:2]
    for i,h in enumerate(lengths):
        j=(i+1)%n
        for p,q,k in [(i,i,F(1,3)),(j,j,F(1,3)),(i,j,F(1,6)),(j,i,F(1,6))]:
            M[p][q]+=h*k
        for p,q,k in [(i,i,F(1)),(j,j,F(1)),(i,j,-F(1,2)),(j,i,-F(1,2))]:
            BI[p][q]+=k/h
        for p,q,k in [(i,i,F(4)),(j,j,F(4)),(i,j,-F(2)),(j,i,-F(2))]:
            BW[p][q]+=h*k/(a+b)**2
    return M,BI,BW


def check(n,r):
    a,b=r,F(1)
    M,BI,BW=mat(n, [a if i%2==0 else b for i in range(n)])
    # Identity for diagonal-local-mass weighting.
    RHS=[[ (F(8)/(a+b) if i==j else F(0))-F(12)*M[i][j]/(a+b)**2
           for j in range(n)] for i in range(n)]
    assert BW==RHS
    const=[F(1)]*n
    alternate=[(-1)**i for i in range(n)]
    assert mv(M,const)==[(a+b)/2]*n
    assert mv(M,alternate)==[(a+b)*F(1,6)*v for v in alternate]
    # Bloch phase -1 for the two-node unit cell, reached when n is a multiple of 4.
    modes=[[(-1)**(i//2) for i in range(n)],
           [(-1)**(i//2)*(1 if i%2==0 else -1) for i in range(n)]]
    lower=(r+3)**2/(12*r)
    upper=(3*r+1)**2/(12*r)
    for mode,lam in zip(modes, (upper,lower)):
        assert mv(mult(BI,M),mode)==[lam*v for v in mode]
    wmax=F(4,3)-(r-1)**2/(3*(r+1)**2)
    for mode in modes:
        assert mv(mult(BW,M),mode)==[wmax*v for v in mode]
    assert mv(mult(BW,M),const)==const
    assert mv(mult(BW,M),alternate)==alternate
    return upper,lower,wmax


def main():
    tests=0
    for n in [4,8,12,16,20]:
        for r in [F(1),F(4,3),F(2),F(5,2),F(3),F(4),F(10),F(100)]:
            check(n,r)
            tests+=1
    upper,lower,w=check(8,F(4))
    assert upper==F(169,48) and lower==F(49,48)
    assert upper/lower==F(169,49) and w==F(91,75)
    assert F(169,49)>F(3)>F(91,75)
    # Polynomial for the sharp threshold: 3r^2-6r-13=0.
    assert (3*F(3)**2-6*F(3)-13)<0
    assert (3*F(4)**2-6*F(4)-13)>0
    print('PASS: %d exact-rational assembly/eigenmode configurations; r=4 gives'
          ' kappa(B_I M)=169/49, kappa(B_W M)=91/75, kappa(JM)=3.' % tests)

if __name__=='__main__':
    main()
