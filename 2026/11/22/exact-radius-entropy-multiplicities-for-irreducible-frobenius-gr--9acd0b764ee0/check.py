"""Finite independent checks of endomorphism and commuting-image counts.

The enumerator tests a map on every ordered pair in its finite group.
It is evidence for small cases, not a proof of statements for all primes.
"""
from itertools import product

class Frobenius:
    def __init__(self, p, d, q, matrix):
        self.p, self.d, self.q, self.matrix = p,d,q,matrix
        self.vectors=list(product(range(p),repeat=d))
        self.zero=(0,)*d
        self.e=(self.zero,0)
        self.elts=list(product(self.vectors,range(q)))
        self.identity=self.e
        self.generators=[(tuple(1 if k==i else 0 for k in range(d)),0) for i in range(d)]+[(self.zero,1)]
        self.powers=[[(g if j else self.e) for j in range(1)] for g in []]
        self.card=len(self.elts)
        self.idx={g:i for i,g in enumerate(self.elts)}
        self.mult=[[self.idx[self.mul(a,b)] for b in self.elts] for a in self.elts]
        self.gen_indices=[self.idx[g] for g in self.generators]
    def act(self,v):
        p=self.p
        return tuple(sum(self.matrix[i][j]*v[j] for j in range(self.d))%p for i in range(self.d))
    def actk(self,v,k):
        for _ in range(k):v=self.act(v)
        return v
    def mul(self,a,b):
        v,k=a;w,l=b
        w=self.actk(w,k)
        return (tuple((v[i]+w[i])%self.p for i in range(self.d)),(k+l)%self.q)
    def maps(self):
        found=[]
        for images in product(range(self.card),repeat=self.d+1):
            # For normal form (v,k) = prod_i e_i^(v_i) b^k
            lookup={self.e:self.idx[self.e]}
            for v,k in self.elts:
                target=self.idx[self.e]
                for i,v_i in enumerate(v):
                    for _ in range(v_i):target=self.mult[target][images[i]]
                for _ in range(k):target=self.mult[target][images[-1]]
                lookup[(v,k)]=target
            values=tuple(lookup[g] for g in self.elts)
            if all(values[self.mult[i][j]]==self.mult[values[i]][values[j]] for i in range(self.card) for j in range(self.card)):
                found.append(values)
        assert len(set(found))==len(found)
        return found
    def commute(self,a,b):
        return all(self.mult[u][v]==self.mult[v][u] for u in set(a) for v in set(b))

def check(p,d,q,A):
    G=Frobenius(p,d,q,A)
    M=G.maps()
    aut=[m for m in M if len(set(m))==G.card]
    target_aut=p**d*d*(p**d-1)
    expected_endo=1+p**d*(q-1)+target_aut
    assert len(aut)==target_aut,(p,d,q,len(aut),target_aut)
    assert len(M)==expected_endo,(p,d,q,len(M),expected_endo)
    nonfull=[m for m in M if len(set(m))<G.card]
    comm=lambda a,b:G.commute(a,b)
    N2=sum(comm(a,b) for a in M for b in M)
    expect2=1+p**d*(q**2-1)+2*target_aut
    assert N2==expect2,(p,d,q,N2,expect2)
    N3=sum(comm(a,b) and comm(a,c) and comm(b,c) for a in M for b in M for c in M)
    expect3=1+p**d*(q**3-1)+3*target_aut
    assert N3==expect3,(p,d,q,N3,expect3)
    print('p,d,q,|G|,End,Aut,N2,N3',p,d,q,G.card,len(M),len(aut),N2,N3)

def check_laurent_counts(q, radius):
    from collections import Counter
    sites=list(range(-radius,radius+1))
    found=Counter()
    for coeff in product(range(q),repeat=len(sites)):
        supp=[sites[i] for i,c in enumerate(coeff) if c]
        width=(max([0]+supp)-min([0]+supp))
        found[width]+=1
    assert found[0]==q
    for k in range(1,2*radius+1):
        a_min=max(1,k-radius)
        a_max=min(radius,k-1)
        pair_count=max(0,a_max-a_min+1)
        expected=(2*(q-1)*q**k if k<=radius else 0)+pair_count*(q-1)**2*q**(k-1)
        assert found[k]==expected,(q,radius,k,found[k],expected)
    assert sum(found.values())==q**len(sites)
    print('q,radius,entropy width multiplicities',q,radius,dict(sorted(found.items())))

if __name__=='__main__':
    check(3,1,2,[[2]])  # S3, a special case of the uniform theorem
    check(2,2,3,[[0,1],[1,1]])  # A4 (tetrahedral group)
    check(7,1,3,[[2]])  # nonabelian group of order 21

    for q in (2,3,5):
        for radius in (1,2,3):
            check_laurent_counts(q,radius)
