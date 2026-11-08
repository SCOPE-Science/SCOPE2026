# Finite-field checks for curves of the form det(a,X,X^(q)), q=2 or 3.
# All operations are exact; no source material is used beyond elementary field arithmetic.
from collections import Counter

def field(p, mod):
    M=p**3
    def dec(x): return [x//(p**i)%p for i in range(3)]
    def enc(v): return sum((v[i]%p)*p**i for i in range(3))
    def add(x,y): return enc([(dec(x)[i]+dec(y)[i])%p for i in range(3)])
    def neg(x): return enc([-z for z in dec(x)])
    def mul(x,y):
        a,b=dec(x),dec(y);c=[0]*5
        for i in range(3):
            for j in range(3): c[i+j]=(c[i+j]+a[i]*b[j])%p
        for i in range(4,2,-1):
            w=c[i]
            for j in range(3):c[i-3+j]=(c[i-3+j]-w*mod[j])%p
        return enc(c[:3])
    def powr(x,n):
        z=1
        while n:
            if n&1:z=mul(z,x)
            x=mul(x,x);n//=2
        return z
    inv=lambda x: powr(x,M-2)
    return M,add,neg,mul,powr,inv

def perform(p,mod):
    q=p; M,add,neg,mul,powr,inv=field(p,mod)
    def sub(a,b):return add(a,neg(b))
    def norm(x):
        for v in reversed(x):
            if v!=0:
                k=inv(v);return tuple(mul(t,k) for t in x)
        raise ValueError('zero vector')
    vectors=[(x,y,z) for x in range(M) for y in range(M) for z in range(M) if any((x,y,z))]
    P=sorted(set(map(norm,vectors)))
    assert len(P)==M*M+M+1
    def det(a,b,c):
        return add(add(sub(mul(a[0],mul(b[1],c[2])),mul(a[0],mul(b[2],c[1]))),sub(mul(a[1],mul(b[2],c[0])),mul(a[1],mul(b[0],c[2])))),sub(mul(a[2],mul(b[0],c[1])),mul(a[2],mul(b[1],c[0]))))
    def dotted(a,b):return add(add(mul(a[0],b[0]),mul(a[1],b[1])),mul(a[2],b[2]))
    def oncurve(a,x):return det(a,x,tuple(powr(t,q) for t in x))==0
    def singular(a,x):
        xq=tuple(powr(t,q) for t in x)
        return (sub(mul(a[1],xq[2]),mul(a[2],xq[1]))==0 and sub(mul(a[2],xq[0]),mul(a[0],xq[2]))==0 and sub(mul(a[0],xq[1]),mul(a[1],xq[0]))==0)
    def rank(a):
        rational=[x for x in P if tuple(powr(t,q) for t in x)==x]
        if a in rational: return 1
        if any(dotted(l,a)==0 for l in rational):return 2
        return 3
    # The rational projective points are the coefficient vectors of F_q lines.
    rational=[x for x in P if tuple(powr(t,q) for t in x)==x]
    assert len(rational)==q*q+q+1
    strata=Counter(map(rank,P)); sizes={}
    for r in (1,2,3):
        a=next(x for x in P if rank(x)==r)
        on=sum(oncurve(a,x) for x in P)
        bad=[x for x in P if singular(a,x)]
        expected=({1:(q+1)*M+1,2:2*M+1,3:M+1})[r]
        lines=[l for l in P if all(dotted(l,x)!=0 or oncurve(a,x) for x in P)]
        fqlines=[l for l in rational if dotted(l,a)==0]
        assert on==expected,(p,r,on,expected)
        assert len(bad)==1 and bad[0]==norm(tuple(powr(t,M//q) for t in a)),(p,r,bad)
        assert set(lines)==set(fqlines),(p,r,len(lines),len(fqlines))
        sizes[r]=(on,len(lines))
    expected_strata={1:q*q+q+1,2:(q*q+q+1)*(M-q),3:(M*M+M+1)-(q*q+q+1)*(M-q+1)}
    assert strata==expected_strata,(p,strata,expected_strata)
    return {'q':q,'field_size':M,'parameter_strata':dict(strata),'point_count_and_line_factors_by_rank':sizes,'status':'PASS'}

if __name__=='__main__':
    for p,mod in [(2,[1,1,0,1]),(3,[1,2,0,1])]:print(perform(p,mod))
    print('ALL_CHECKS_PASSED')
