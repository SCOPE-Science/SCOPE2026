"""Direct element-level fixed-ring census for a characteristic-two monomial algebra.

The check forms images of x, y and xy in A=F_q[x,y]/(x*x,y*y), then
substitutes into every algebra element without using a rank formula.
"""
from itertools import product


def mul(a,b,q):
    if q==2:return a&b
    irr=0b111 if q==4 else 0b1011
    c=0
    while b:
        if b&1:c^=a
        b>>=1;a<<=1
        if a&q:a^=irr
    return c


def algebra_mul(a,b,q):
    return (mul(a[0],b[0],q),mul(a[0],b[1],q)^mul(a[1],b[0],q),
            mul(a[0],b[2],q)^mul(a[2],b[0],q),
            mul(a[0],b[3],q)^mul(a[3],b[0],q)^mul(a[1],b[2],q)^mul(a[2],b[1],q))


def check(q):
    elements=list(product(range(q),repeat=4))
    aut={i:0 for i in range(1,5)};end={i:0 for i in range(1,5)}
    for a,b,c,d,u,v in product(range(q),repeat=6):
        X=(0,a,c,u);Y=(0,b,d,v)
        assert algebra_mul(X,X,q)==(0,0,0,0)
        assert algebra_mul(Y,Y,q)==(0,0,0,0)
        Z=algebra_mul(X,Y,q)
        nfix=0
        for t0,t1,t2,t3 in elements:
            image=(t0,
                   mul(t1,X[1],q)^mul(t2,Y[1],q),
                   mul(t1,X[2],q)^mul(t2,Y[2],q),
                   mul(t1,X[3],q)^mul(t2,Y[3],q)^mul(t3,Z[3],q))
            if image==(t0,t1,t2,t3):nfix+=1
        dim=next(i for i in range(1,5) if q**i==nfix)
        end[dim]+=1
        if Z[3]:aut[dim]+=1
    E1=q**3*(q**3-2*q*q+2)
    E3=(q*q-1)*(q+1)
    A1=q**3*(q+1)*(q-2)**2
    A3=E3
    Atotal=q**3*(q-1)**2*(q+1)
    assert end=={1:E1,2:q**6-E1-E3-1,3:E3,4:1},end
    assert aut=={1:A1,2:Atotal-A1-A3-1,3:A3,4:1},aut
    assert sum(aut[d]*q**d for d in aut)==Atotal*3*q
    print('q',q,'endo',end,'auto',aut,'orbits',3*q)

if __name__=='__main__':
    for q in (2,4):check(q)
    print('VERIFY_OK_DIRECT')
