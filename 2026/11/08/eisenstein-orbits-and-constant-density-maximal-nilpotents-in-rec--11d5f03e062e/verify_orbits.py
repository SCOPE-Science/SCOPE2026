"""Exact conjugation-orbit verification in small truncated polynomial rings.

Run: python verify_orbits.py
Check the complete regular-nilpotent set against independently generated
conjugacy orbits of companion matrices over the indicated finite rings.
"""
from itertools import product
from collections import defaultdict


def setup(q,n):
    E=list(product(range(q),repeat=n))
    Z=(0,)*n
    O=(1,)+(0,)*(n-1)
    def add(a,b):return tuple((u+v)%q for u,v in zip(a,b))
    def neg(a):return tuple((-u)%q for u in a)
    def mult(a,b):
        z=[0]*n
        for i,u in enumerate(a):
            for j,v in enumerate(b[:n-i]): z[i+j]+=u*v
        return tuple(u%q for u in z)
    def inv(a):
        assert a[0]!=0
        c=[0]*n;c[0]=pow(a[0],-1,q)
        for k in range(1,n):
            c[k]=(-c[0]*sum(a[i]*c[k-i] for i in range(1,k+1)))%q
        out=tuple(c)
        assert mult(a,out)==O
        return out
    def mm(A,B):
        a,b,c,d=A;e,f,g,h=B
        return (add(mult(a,e),mult(b,g)),add(mult(a,f),mult(b,h)),
                add(mult(c,e),mult(d,g)),add(mult(c,f),mult(d,h)))
    def det(A):
        a,b,c,d=A;return add(mult(a,d),neg(mult(b,c)))
    def tr(A):return add(A[0],A[3])
    def invmat(A):
        a,b,c,d=A
        dinv=inv(det(A))
        return (mult(d,dinv),mult(neg(b),dinv),mult(neg(c),dinv),mult(a,dinv))
    return E,Z,O,add,neg,mult,mm,det,tr,invmat


def run(q,n):
    E,Z,O,add,neg,mult,mm,det,tr,invmat=setup(q,n)
    I=(O,Z,Z,O)
    allm=list(product(E,repeat=4))
    group=[x for x in allm if det(x)[0]!=0]
    expected_gl=(q*q-1)*(q*q-q)*q**(4*(n-1))
    assert len(group)==expected_gl
    regular={}
    for x in allm:
        reduction=(x[0][0],x[1][0],x[2][0],x[3][0])
        # Regular nilpotence of residue: trace=det=0 and matrix nonzero
        if not (sum(reduction[::3])%q==0 and
                (reduction[0]*reduction[3]-reduction[1]*reduction[2])%q==0 and
                reduction !=(0,0,0,0)):
            continue
        if det(x)[1]==0: continue
        regular[x]=(tr(x),det(x))
    target=(q-1)*(q*q-1)*q**(4*n-5)
    assert len(regular)==target,(len(regular),target)
    fibers=defaultdict(set)
    for A,chi in regular.items():fibers[chi].add(A)
    assert len(fibers)==(q-1)*q**(2*(n-1)-1)
    size=(q*q-1)*q**(2*n-2)
    assert all(len(v)==size for v in fibers.values())
    for (tr,determinant),fiber in fibers.items():
        # Companion form with trace tr, determinant determinant
        A=(Z,neg(determinant),O,tr)
        assert A in fiber
        orbit=set()
        for g in group:
            orb=mm(mm(g,A),invmat(g))
            orbit.add(orb)
        assert orbit==fiber,(q,n,tr,determinant,len(orbit),len(fiber))
    print(f'CHECK q={q} n={n}: |GL_2(R)|={len(group)} regular={len(regular)} '
          f'conjugacy_classes={len(fibers)} size={size} OK',flush=True)

if __name__=='__main__':
    for q,n in [(2,2),(2,3),(3,2)]:run(q,n)
    print('VERIFY_OK')
