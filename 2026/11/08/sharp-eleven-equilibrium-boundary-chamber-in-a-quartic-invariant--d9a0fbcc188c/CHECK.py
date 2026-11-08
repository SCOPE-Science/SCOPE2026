#!/usr/bin/env python3
"""Pure-standard-library rational checks for a quartic invariant-square flow."""
from fractions import Fraction as F
from random import Random

def sg(v):return (v>0)-(v<0)
def vcount(signs):
    a=[x for x in signs if x]
    return sum(a[i]!=a[i-1] for i in range(1,len(a)))
def rootcount(A,B,C):
    A,B,C=map(F,(A,B,C))
    if A==B==C==0:return None
    if not A:
        return int(bool(B) and -1 < -C/B < 1)
    D=B*B-4*A*C
    if D<0:return 0
    if D==0:return int(-1 < -B/(2*A) < 1)
    def inward(z, direction):
        p=A*z*z+B*z+C
        dp=2*A*z+B
        s0=sg(p) if p else sg(dp*direction) if dp else sg(A)
        s1=sg(dp) if dp else sg(2*A*direction)
        return vcount((s0,s1,sg(D/(4*A))))
    result=inward(F(-1),1)-inward(F(1),-1)
    assert 0<=result<=2
    return result

def sidepolys(par):
    l,a,b,c,d,e=map(F,par)
    return [(a,l+b,-1-a), (a,l-b,1-a), (e,l+d,c+1), (e,l-d,c-1)]
def counts(par):return tuple(rootcount(*p) for p in sidepolys(par))

def two(A,B,C):
    A,B,C=map(F,(A,B,C))
    return bool(A and B*B-4*A*C>0 and B*B<4*A*A and A*(A+B+C)>0 and A*(A-B+C)>0)
def eleven_chamber(par):
    l,a,b,c,d,e=map(F,par)
    vertical=two(e,l+d,c+1) and two(e,l-d,c-1)
    horizontal=((two(a,l+b,-1-a) and abs(l-b)>1) or (two(a,l-b,1-a) and abs(l+b)>1))
    return vertical and horizontal

if __name__=='__main__':
    examples={
      4:(0,0,0,0,0,0),
      5:(2,0,2,5,0,0),
      6:(0,2,0,0,0,0),
      7:(F(3,2),2,F(3,2),-2,0,-1),
      8:(F(3,2),2,F(3,2),-2,0,0),
      9:(F(3,2),2,F(3,2),-2,0,2),
      10:(F(3,2),2,F(3,2),-2,0,3),
      11:(F(3,2),2,F(3,2),-2,0,5)
    }
    for n,p in examples.items():
      ct=counts(p)
      assert None not in ct and 4+sum(ct)==n,(n,p,ct)
      assert eleven_chamber(p)==(n==11)
      print(n,p,ct)
    R=Random(1834)
    n=0
    for z in range(18000):
      p=tuple(F(R.randrange(-12,13),R.choice((1,2,3,4))) for _ in range(6))
      ct=counts(p)
      if None in ct:continue
      assert 4 <=4+sum(ct)<=11,(p,ct)
      assert eleven_chamber(p)==(sum(ct)==7),(p,ct)
      n+=1
    print('random rational cases:',n)
    for A in range(-5,6):
      for B in range(-5,6):
        for C in range(-5,6):
          if A==B==C==0:continue
          assert two(A,B,C)==(rootcount(A,B,C)==2),(A,B,C,rootcount(A,B,C))
    print('quadratic-criterion tests:',11**3-1)
    print('PASS')

# Extra independent exact-arithmetic hyperbolicity certificate for sharp witness.
def det4(m):
    m=[[F(x) for x in row] for row in m]
    out=F(1)
    for j in range(4):
        i=next((i for i in range(j,4) if m[i][j]),None)
        if i is None:return F(0)
        if i!=j:m[j],m[i]=m[i],m[j];out=-out
        v=m[j][j];out*=v
        for k in range(j+1,4):
            q=m[k][j]/v
            for c in range(j,4):m[k][c]-=q*m[j][c]
    return out

def resultant(A,B,C,D,E,G):
    return det4([[A,B,C,0],[0,A,B,C],[D,E,G,0],[0,D,E,G]])

def sharp_witness_certificate():
    l,a,b,c,d,e=F(3,2),F(2),F(3,2),F(-2),F(0),F(5)
    # At y=t, transverse Qinner(u,t)=c*u*u+(1+d*t)*u+l*t+e.
    # At x=s, transverse Pinner(s,u)=-a*u*u+(b*s-1)*u+l*s+a.
    coefficients=[
        (a,l+b,-a-1,c,1+d,l+e),
        (a,l-b,1-a,c,1-d,-l+e),
        (e,l+d,c+1,-a,b-1,l+a),
        (e,l-d,c-1,-a,-b-1,-l+a)
    ]
    rs=tuple(resultant(*v) for v in coefficients)
    assert rs==(F(-131),F(23),F(1669,8),F(-415,8)),rs
    assert counts((l,a,b,c,d,e))==(1,2,2,2)
    # Corners: Jacobian is diagonal at all four corners.
    eig={}
    for s in (-1,1):
      for t in (-1,1):
        px=l*s-t+a*s*s+b*s*t-a*t*t
        qy=s+l*t+c*s*s+d*s*t+e*t*t
        eig[(s,t)]=(-2*s*px,-2*t*qy)
        assert all(eig[(s,t)])
    assert eig=={(-1,-1):(F(2),F(1)),(-1,1):(F(-8),F(-7)),(1,-1):(F(-2),F(5)),(1,1):(F(-4),F(-11))},eig
    print('hyperbolicity resultants:',rs,'corner eigenvalues:',eig)

if __name__=='__main__':
    sharp_witness_certificate()
    print('SHARP HYPERBOLICITY PASS')
