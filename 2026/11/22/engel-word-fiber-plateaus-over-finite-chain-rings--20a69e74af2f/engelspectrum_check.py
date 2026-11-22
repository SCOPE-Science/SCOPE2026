"""Independent arithmetic enumeration for finite chain-ring Engel fibers.
This scientific checker treats finite coefficient rings and directly iterates brackets.
"""
from collections import Counter

def make_ring(q, ell, mode):
    n=q**ell
    if mode=='integer':
        return n, lambda x,y:(x+y)%n, lambda x,y:(x*y)%n, lambda x:(-x)%n
    assert q in (2,3)
    def vec(v):
        out=[]
        for _ in range(ell):out.append(v%q);v//=q
        return out
    def val(v):return sum(x*q**j for j,x in enumerate(v))
    vs=[vec(i) for i in range(n)]
    def add(x,y):return val([(a+b)%q for a,b in zip(vs[x],vs[y])])
    def neg(x):return val([(-a)%q for a in vs[x]])
    def mul(x,y):
        z=[0]*ell
        for i,a in enumerate(vs[x]):
            for j,b in enumerate(vs[y][:ell-i]):z[i+j]=(z[i+j]+a*b)%q
        return val(z)
    return n,add,mul,neg

def nu(x,q,ell,mode):
    if x==0:return ell
    if mode=='integer':
        out=0
        while x%q==0:out+=1;x//=q
        return out
    out=0
    while x%q==0:out+=1;x//=q
    return out

def predicted(q,ell,depth):
    C=lambda j:(q-1)*q**(ell-j-1) if j<ell else 1
    M=Counter({0:C(0)*q**ell, ell:q**ell})
    for i in range(1,ell):
        for j in range(i):M[min(ell,(depth-1)*i+j)]+=C(i)*C(j)
        M[min(ell,depth*i)]+=C(i)*q**(ell-i)
    N={k:sum(M[h]*q**(ell+h) for h in M if h<=k) for k in range(ell+1)}
    assert sum(M.values())==q**(2*ell)
    assert sum((q-1)*q**(ell-k-1)*N[k] for k in range(ell))+N[ell]==q**(4*ell)
    return M,N

def verify(q,ell,mode,depth):
    n,add,mul,neg=make_ring(q,ell,mode)
    M,N=predicted(q,ell,depth)
    observed=Counter()
    # Bracket [(a,b),(c,d)]=(0, ad-bc), hence iterate left ad depth.
    for a in range(n):
      for b in range(n):
        for c in range(n):
          for d in range(n):
            r=add(mul(a,d),neg(mul(b,c)))
            for _ in range(1,depth):r=mul(a,r)
            observed[r]+=1
    assert len(observed)==n
    assert all(observed[t]==N[nu(t,q,ell,mode)] for t in range(n)), (q,ell,mode,depth,observed,N)
    print('PASS',q,ell,mode,depth,'pairs',n**4,'rank_strata',sorted(M.items()),'Nvals',list(N.items()))

if __name__=='__main__':
    for q,ell,mode,depths in [(2,2,'integer',(2,3)),(2,3,'integer',(2,3,4)),(2,3,'polynomial',(2,3,4)),(2,4,'polynomial',(2,3,4,5)),(3,2,'integer',(2,3)),(3,3,'polynomial',(2,3))]:
        for d in depths:verify(q,ell,mode,d)
