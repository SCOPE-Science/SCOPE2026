"""Standalone direct product enumerator for GL2 of small square-zero local rings."""
from collections import Counter
from itertools import product
import numpy as np

def ring(q,d,kind='split'):
    if kind=='mixed8':
        el=list(product(range(4),range(2))); lookup={v:i for i,v in enumerate(el)};m=8
        add=np.zeros((m,m),dtype='int16');mul=np.zeros((m,m),dtype='int16');red=np.zeros(m,dtype='int16')
        for i,(a,b) in enumerate(el):
            red[i]=a%2
            for j,(c,e) in enumerate(el):
                add[i,j]=lookup[((a+c)%4,(b+e)%2)]
                mul[i,j]=lookup[((a*c)%4,((a%2)*e+(c%2)*b)%2)]
        return m,add,mul,red,2,2
    if kind=='z4':
        m=4; add=np.fromfunction(lambda a,b:(a+b)%4,(m,m),dtype=int).astype('int16')
        mul=np.fromfunction(lambda a,b:(a*b)%4,(m,m),dtype=int).astype('int16')
        red=np.arange(4)%2
        return m, add,mul,red,2,1
    el=list(product(range(q),repeat=d+1));lookup={v:i for i,v in enumerate(el)}
    m=len(el);add=np.zeros((m,m),dtype='int16');mul=np.zeros((m,m),dtype='int16');red=np.zeros(m,dtype='int16')
    for i,a in enumerate(el):
        red[i]=a[0]
        for j,b in enumerate(el):
            add[i,j]=lookup[tuple((x+y)%q for x,y in zip(a,b))]
            mul[i,j]=lookup[((a[0]*b[0])%q,)+tuple((a[0]*b[t]+b[0]*a[t])%q for t in range(1,d+1))]
    return m,add,mul,red,q,d

def predicted(q,d):
    U=q*(q-1)**2*(q+1);t=q-1
    S=q*(q+1)//2; I=q*(q-1)//2; J=q+1
    cs=t*t; ci=q*q-1; cj=q*t
    nc=q**(4*d)-(q*q+q+1)*q**(2*d)+(q*q+q)*q**d
    ms=(t*(q-2)//2)*(U//cs) if q>2 else 0
    mi=(q*t//2)*(U//ci)
    mj=t*(U//cj)
    h=Counter()
    def push(n,c):
        if n>0: h[c]+=n
    push(t*q**d,U*q**(4*d))
    for N,c in [(S,cs),(I,ci),(J,cj)]:push(t*N*(q**(2*d)-q**d),c*q**(4*d))
    push(t*nc,t*q**(4*d))
    for M,c in [(ms,cs),(mi,ci),(mj,cj)]:push(M*q**(4*d),c*q**(2*d))
    expected_classes=(q*q-1)*q**(2*d)+(q**(4*d)-q**(2*d))//(q*(q+1))
    return U*q**(4*d),dict(h),expected_classes

def verify(q,d,kind='split'):
    m,add,mul,red,_,_=ring(q,d,kind)
    mats=np.array([x for x in product(range(m),repeat=4) if (red[x[0]]*red[x[3]]-red[x[1]]*red[x[2]])%q],dtype='int16')
    n=len(mats);counts=np.zeros(n,dtype='int64')
    # Coordinate-by-coordinate multiplication, independent of linearized commutator equations.
    for lo in range(0,n,64):
        a=mats[lo:lo+64];b=mats
        ok=np.ones((len(a),n),dtype=bool)
        for i,j in [(0,0),(0,1),(1,0),(1,1)]:
            k=2*i; v=j
            left=add[mul[a[:,None,k],b[None,:,v]],mul[a[:,None,k+1],b[None,:,2+v]]]
            right=add[mul[b[None,:,k],a[:,None,v]],mul[b[None,:,k+1],a[:,None,2+v]]]
            ok &= (left==right)
        counts[lo:lo+len(a)]=ok.sum(axis=1)
    actual=dict(Counter(map(int,counts)));size,h,k=predicted(q,d)
    assert size==n,(size,n)
    assert actual==h,(q,d,kind,actual,h)
    assert int(counts.sum())==n*k,(int(counts.sum()),n*k)
    print(f'PASS {kind} q={q} d={d} group={n} classes={k} commuting_pairs={int(counts.sum())} centralizer_histogram={sorted(actual.items())}')

if __name__=='__main__':
    verify(2,1)
    verify(2,2)
    verify(3,1)
    verify(2,1,'z4')
    verify(2,2,'mixed8')
