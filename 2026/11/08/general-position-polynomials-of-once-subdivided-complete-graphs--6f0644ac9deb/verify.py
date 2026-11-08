"""Finite checks for the general-position polynomial of subdivided cliques.
Run: python3 verify.py (standard-library only)."""
from collections import Counter, deque
from itertools import combinations
from math import comb, factorial
from random import Random

def graph(n):
    E=list(combinations(range(n),2)); adj=[set() for _ in range(n+len(E))]
    for j,(a,b) in enumerate(E):
        for x in (a,b):
            adj[x].add(n+j); adj[n+j].add(x)
    return E,adj

def distance_and_forbidden(adj):
    N=len(adj); D=[]
    for x in range(N):
        d=[N+10]*N; d[x]=0; queue=deque([x])
        while queue:
            u=queue.popleft()
            for v in adj[u]:
                if d[v]>d[u]+1: d[v]=d[u]+1; queue.append(v)
        D.append(d)
    bad=[]
    for a,b,c in combinations(range(N),3):
        if (D[a][b]+D[b][c]==D[a][c] or
            D[a][c]+D[c][b]==D[a][b] or
            D[b][a]+D[a][c]==D[b][c]):
            bad.append((1<<a)|(1<<b)|(1<<c))
    return bad

def structural_valid(n,E,mask):
    edge_mask=mask>>n
    chosen=[i for i in range(len(E)) if edge_mask & (1<<i)]
    # Induced line graph of the selected edges must have no induced P3.
    for i,j,k in combinations(chosen,3):
        d=(bool(set(E[i])&set(E[j])),bool(set(E[i])&set(E[k])),bool(set(E[j])&set(E[k])))
        if sum(d)==2:return False
    original={i for i in range(n) if mask&(1<<i)}
    if not chosen:return True
    support=set().union(*(set(E[i]) for i in chosen))
    if len(chosen)==1:
        return not bool(original&support) or (len(original)==1 and original<=support)
    return not bool(original&support)

def add(p,q):
    r=Counter(p)
    for k,v in q.items():r[k]+=v
    return r

def prod(p,q):
    r=Counter()
    for a,x in p.items():
        for b,y in q.items():r[a+b]+=x*y
    return r

def formula(n):
    P=[Counter({0:1})]
    for m in range(1,n+1):
        total=Counter()
        for k in range(1,m+1):
            if k==1:block={0:1,1:1}
            elif k==2:block={1:1}
            elif k==3:block={2:3,3:1}
            else:block={k-1:k}
            for d,coef in prod(P[m-k],block).items():total[d]+=comb(m-1,k-1)*coef
        P.append(total)
    R=Counter(P[-1]);R[2]+=n*(n-1)
    return R

def structural_polynomial(n,E):
    result=Counter()
    for e_mask in range(1<<len(E)):
        Eidx=[i for i in range(len(E)) if (e_mask>>i)&1]
        good=True
        for i,j,k in combinations(Eidx,3):
            adj=sum((bool(set(E[x])&set(E[y])) for x,y in ((i,j),(i,k),(j,k))))
            if adj==2:good=False;break
        if not good:continue
        support=set().union(*(set(E[i]) for i in Eidx)) if Eidx else set()
        for k in range(n-len(support)+1):
            result[len(Eidx)+k]+=comb(n-len(support),k)
        if len(Eidx)==1:result[2]+=2
    return result

def main():
    direct_total=0; badtriples=0
    for n in (3,4,5):
        E,adj=graph(n);bad=distance_and_forbidden(adj)
        got=Counter()
        for mask in range(1<<len(adj)):
            g=not any(mask&b==b for b in bad)
            assert g==structural_valid(n,E,mask),(n,mask,g)
            if g:got[mask.bit_count()]+=1
        assert got==formula(n),(n,got,formula(n))
        assert got==structural_polynomial(n,E)
        direct_total+=(1<<len(adj));badtriples+=len(bad)
        print('DIRECT_OK',n,'subsets',1<<len(adj),'coefficients',sorted(got.items()))
    n=6;E,adj=graph(n);bad=distance_and_forbidden(adj);rng=Random(21073)
    trials=40000
    for _ in range(trials):
        mask=rng.randrange(1<<len(adj))
        assert (not any(mask&b==b for b in bad))==structural_valid(n,E,mask)
    assert formula(n)==structural_polynomial(n,E)
    print('SAMPLE_OK',n,'subsets',trials,'coefficients',sorted(formula(n).items()))
    for n in range(3,21):
        top=sum(factorial(n)//(6**j*factorial(j)*factorial(n-3*j)) for j in range(n//3+1))
        assert formula(n)[n]==top and max(formula(n))==n
    print('VERIFY_OK direct_subsets',direct_total,'sampled_subsets',trials,'orders_checked','3..20','forbidden_triples',badtriples+len(bad),'full_polynomials=PASS','maximum_multiplicity=PASS')
if __name__=='__main__':main()
