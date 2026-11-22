"""Exact finite-ring verification for the cycle-sum principal-intersection theorem.
Run: python VERIFY.py.  Standard-library only.
The tested finite rings are the divisor-closed subrings of binary cycle sums.
Finite tests corroborate, but do not replace, the all-length proof.
"""
from math import gcd


def divisors(n):
    return [d for d in range(1,n+1) if n%d==0]


def make_ring(n):
    ds=divisors(n); idx={d:i for i,d in enumerate(ds)}
    base=[]
    for x in ds:
        row=[]
        for y in ds:
            row.append(0 if gcd(x,y)%2==0 else 1<<idx[x*y//gcd(x,y)])
        base.append(row)
    def mul(x,y):
        out=0; i=0
        while x:
            if x&1:
                j=0; z=y
                while z:
                    if z&1: out ^=base[i][j]
                    z >>=1; j+=1
            x >>=1; i+=1
        return out
    a=0; u=n
    while u%2==0:
        u//=2; a+=1
    od=divisors(u)
    def phi(x):
        result=[]
        for t in od:
            v=[]
            for j in range(a+1):
                v.append(sum((x >> idx[(1<<j)*d])&1 for d in divisors(t))%2)
            result.append(v)
        return result
    def inv(components):
        out=0
        for j in range(a+1):
            co={}
            for t,vs in zip(od,components):
                co[t]=(vs[j] ^ (sum(co[d] for d in od if d<t and t%d==0)%2))
                if co[t]: out |=1<<idx[(1<<j)*t]
        return out
    def gen(x,y):
        out=[]
        for X,Y in zip(phi(x),phi(y)):
            p,uvec=X[0],X[1:]; q,vvec=Y[0],Y[1:]
            if p and q: out.append([1]+[0]*a)
            elif p: out.append([0]+vvec)
            elif q: out.append([0]+uvec)
            elif uvec==vvec: out.append([0]+uvec)
            else: out.append([0]*(a+1))
        return inv(out)
    return ds,mul,phi,inv,gen


def check(n):
    ds,mul,phi,inv,gen=make_ring(n)
    sz=1<<len(ds)
    for x in range(sz):
        assert inv(phi(x))==x,(n,x,"inversion")
    ideal=[]
    for x in range(sz):
        b=0
        for z in range(sz):
            w=mul(x,z)
            b |=1<<w
        ideal.append(b)
    for x in range(sz):
        for y in range(sz):
            g=gen(x,y)
            assert ideal[g] == (ideal[x]&ideal[y]), (n,x,y,g,"bad intersection")
    # Explicitly verify the same multiplication under the independent coordinate model.
    for x in range(sz):
        px=phi(x)
        for y in range(sz):
            py=phi(y)
            prod=[]
            for X,Y in zip(px,py):
                prod.append([X[0]*Y[0]] + [(X[0]*Y[j]+X[j]*Y[0])%2 for j in range(1,len(X))])
            assert phi(mul(x,y))==prod,(n,x,y,"product mismatch")
    print("PASS N=%d basis=%d elements=%d principal-pairs=%d"%(n,len(ds),sz,sz*sz))
    return sz*sz

def check_cutoff_stability(n,m):
    assert m%n == 0
    small, _, _, _, gs = make_ring(n)
    big, _, _, _, gm = make_ring(m)
    ii={d:i for i,d in enumerate(big)}
    def embed(z):
        return sum((1<<ii[d]) for i,d in enumerate(small) if z>>i & 1)
    sz=1<<len(small)
    for x in range(sz):
        for y in range(sz):
            assert embed(gs(x,y))==gm(embed(x),embed(y)),(n,m,x,y)
    print('STABLE N=%d TO M=%d pairs=%d'%(n,m,sz*sz))

if __name__=='__main__':
    count=sum(check(n) for n in (2,6,12,18,24,30))
    for n,m in ((2,24),(6,12),(6,30),(12,24)):
        check_cutoff_stability(n,m)
    print('VERIFY_OK',count)
