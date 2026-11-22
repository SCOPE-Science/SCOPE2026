"""Finite-field group homomorphism and retraction checks for affine groups."""
from collections import deque
from math import comb

FIELD_POLYS = {3:(3,[0,1]), 4:(2,[1,1,1]), 5:(5,[0,1]), 7:(7,[0,1]), 8:(2,[1,1,0,1]), 9:(3,[1,0,1])}

class Field:
    def __init__(self,q):
        self.q=q
        self.p,self.pol=FIELD_POLYS[q]
        self.f=len(self.pol)-1
        assert self.p**self.f==q
        self.digits=[[i//self.p**j%self.p for j in range(self.f)] for i in range(q)]
        self.add=[[sum(((self.digits[a][j]+self.digits[b][j])%self.p)*self.p**j for j in range(self.f)) for b in range(q)] for a in range(q)]
        self.mul=[[self._multiply(a,b) for b in range(q)] for a in range(q)]
        self.neg=[next(b for b in range(q) if self.add[a][b]==0) for a in range(q)]
        self.one=1
        self.inv=[None]+[next(b for b in range(1,q) if self.mul[a][b]==1) for a in range(1,q)]
        self.g=next(a for a in range(1,q) if len({self.pow(a,j) for j in range(q-1)})==q-1)
    def _multiply(self,a,b):
        v=[0]*(2*self.f-1)
        for i,ai in enumerate(self.digits[a]):
            for j,bj in enumerate(self.digits[b]):v[i+j]=(v[i+j]+ai*bj)%self.p
        for d in range(2*self.f-2,self.f-1,-1):
            c=v[d]
            for j in range(self.f):v[d-self.f+j]=(v[d-self.f+j]-c*self.pol[j])%self.p
        return sum(v[j]*self.p**j for j in range(self.f))
    def pow(self,a,n):
        out=1
        for _ in range(n):out=self.mul[out][a]
        return out

def enumerate_homomorphisms(q):
    f=Field(q)
    G=[(v,a) for v in range(q) for a in range(1,q)]
    idx={x:i for i,x in enumerate(G)}
    e=(0,1)
    def prod(x,y):return (f.add[x[0]][f.mul[x[1]][y[0]]],f.mul[x[1]][y[1]])
    def inverse(x):return (f.neg[f.mul[f.inv[x[1]]][x[0]]],f.inv[x[1]])
    tau=(1,1); mu=(0,f.g)
    gens=[tau,mu,inverse(tau),inverse(mu)]
    homs=set()
    for itau in G:
        for imu in G:
            images=[itau,imu,inverse(itau),inverse(imu)]
            mapping={e:e}; queue=deque([e]); consistent=True
            while queue and consistent:
                g=queue.popleft(); im=mapping[g]
                for d,h in zip(gens,images):
                    nxt=prod(g,d); new=prod(im,h)
                    if nxt in mapping:
                        if mapping[nxt]!=new:consistent=False;break
                    else:mapping[nxt]=new;queue.append(nxt)
            if consistent and len(mapping)==len(G):
                homs.add(tuple(idx[mapping[x]] for x in G))
    return G, sorted(homs), idx[e]

def formula(q):
    n=q-1
    # number of distinct prime divisors of n
    p=2; k=0; m=n
    while p*p<=m:
        if m%p==0:
            k+=1
            while m%p==0:m//=p
        p+=1
    if m>1:k+=1
    num=2+q*(2**k-1)
    pairs=4+4*q*(2**k-1)+q*(4**k-3**k)+q*q*(3**k-2**(k+1)+1)
    return k,num,pairs,1+q*(q-2)+q*(q-1)*Field(q).f

def check(q):
    G,homs,e=enumerate_homomorphisms(q)
    rets=[h for h in homs if all(h[h[i]]==h[i] for i in range(len(G)))]
    pairs=sum(1 for a in rets for b in rets if all(a[b[i]]==b[a[i]] for i in range(len(G))))
    k,expected_rets,expected_pairs,expected_homs=formula(q)
    # Independently check the band identity using the enumerated endomorphism maps.
    retset=set(rets)
    for a in rets:
        for b in rets:
            ab=tuple(a[b[i]] for i in range(len(G)))
            assert ab in retset
            aba=tuple(ab[a[i]] for i in range(len(G)))
            assert aba==ab
    z=tuple(e for _ in G)
    identity=tuple(range(len(G)))
    proper=[h for h in rets if h!=z and h!=identity]
    adjacency={a:set() for a in proper}
    for a in proper:
        for b in proper:
            if a!=b and all(a[b[i]]==b[a[i]] for i in range(len(G))):adjacency[a].add(b)
    # Predict the exact degree sequence solely from the number of prime factors.
    predicted=[]
    for s in range(1,k+1):
        predicted.extend([2**k-2+(q-1)*(2**(k-s)-1)]*(q*comb(k,s)))
    assert sorted(len(x) for x in adjacency.values())==sorted(predicted)
    if k==1:
        assert all(not x for x in adjacency.values())
    elif k>=2:
        dmax=0
        for a in proper:
            dist={a:0};queue=deque([a])
            while queue:
                u=queue.popleft()
                for v in adjacency[u]:
                    if v not in dist:dist[v]=dist[u]+1;queue.append(v)
            assert len(dist)==len(proper)
            dmax=max(dmax,max(dist.values()))
        assert dmax==3

    assert (len(homs),len(rets),pairs)==(expected_homs,expected_rets,expected_pairs),(q,len(homs),len(rets),pairs,expected_homs,expected_rets,expected_pairs)
    print('q=%d, k=%d, endomorphisms=%d, retractions=%d, ordered commuting pairs=%d: VERIFIED' % (q,k,len(homs),len(rets),pairs))

if __name__=='__main__':
    for q in (3,4,5,7,8,9):check(q)
    print('AFFINE_RETRACTION_GRAPH_VERIFIED')
