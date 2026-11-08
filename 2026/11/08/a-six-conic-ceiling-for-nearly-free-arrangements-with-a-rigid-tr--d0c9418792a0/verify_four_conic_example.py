#!/usr/bin/env python3
"""Exact syzygy and incidence checks for an explicit four-conic arrangement.
Requires SymPy. The conics are given directly; no external data are needed.
"""
import sympy as s
x,y,z=s.symbols('x y z')
qs=[x*x+y*y-z*z,2*x*x+y*y+2*x*z,x*x+y*y+2*x*z,4*x*x+6*y*y+4*x*z-8*z*z]
f=s.prod(qs).expand()

def syzygy_dim(deg):
    mons=[x**a*y**b*z**(deg-a-b) for a in range(deg+1) for b in range(deg-a+1)]
    coeffs=s.symbols('c:'+str(3*len(mons)))
    combo=sum(coeffs[i*len(mons)+j]*mons[j]*s.diff(f,v) for i,v in enumerate([x,y,z]) for j in range(len(mons)))
    P=s.Poly(combo,x,y,z)
    A,_=s.linear_eq_to_matrix(P.coeffs(),coeffs)
    return len(coeffs)-A.rank()

def incidence_check():
    # Every asserted order-four contact is certified by an exact square identity.
    contacts=[
        (0,1,(x+z)**2,qs[1]-qs[0],(-1,0,1)),
        (1,2,x**2,qs[1]-qs[2],(0,0,1)),
        (2,3,2*(x+2*z)**2,6*qs[2]-qs[3],(-2,0,1)),
        (0,3,2*(x-z)**2,6*qs[0]-qs[3],(1,0,1))]
    for i,j,square,difference,pt in contacts:
        assert s.expand(square-difference)==0
        assert qs[i].subs(dict(zip((x,y,z),pt)))==0
        assert qs[j].subs(dict(zip((x,y,z),pt)))==0
    # Q0-Q2=-z(z+2x): two intersections on each line.
    assert s.expand(qs[0]-qs[2]+z*(z+2*x))==0
    assert s.factor(qs[0].subs(z,0))==x*x+y*y
    assert s.factor(qs[0].subs(z,-2*x))==y*y-3*x*x
    # Q3-2 Q1=4(y^2-2z^2), so two intersections on each
    # of y=+/-sqrt(2) z, with quadratic x^2+xz+z^2.
    assert s.expand(qs[3]-2*qs[1]-4*(y*y-2*z*z))==0
    assert s.expand(qs[1].subs(y,s.sqrt(2)*z)-2*(x*x+x*z+z*z))==0
    assert s.discriminant(x*x+x*z+z*z,x)==-3*z*z
    # The four contacts have y=0. Each residual intersection has
    # y != 0: the first pair has y^2=-x^2 or 3x^2 and x!=0;
    # the second has y^2=2z^2 and z!=0.
    # Any common zero Q1=Q2 forces x=y=0, where Q0,Q3 do not
    # vanish (z != 0). Any common zero Q0=Q1 forces x=-z,y=0,
    # where Q3 does not vanish. Q0=Q2=Q3 implies z(z+2x)=0
    # and x+2z=0, hence x=z=0 and Q0=y^2 !=0 projectively.
    # These exclusions cover all potential triple intersections.
    assert s.expand(qs[1]-qs[2]-x*x)==0
    assert s.expand(qs[0]-qs[2]+z*(z+2*x))==0
    # On each tangency pair the displayed square is a nonzero
    # multiple of the squared tangent line to each smooth conic;
    # since the total intersection number is four, the contact
    # point has exact local intersection multiplicity four.
    print('FOUR_CONIC_INCIDENCE_PASS 4_A7 8_nodes')

def main():
    incidence_check()
    for q in qs:
        M=s.hessian(q,(x,y,z))
        assert M.det()!=0
    out=[syzygy_dim(j) for j in range(4)]
    assert out[:3]==[0,0,0] and out[3]>=1,out
    print('FOUR_CONIC_MDR_3_PASS',out)

if __name__=='__main__':main()
