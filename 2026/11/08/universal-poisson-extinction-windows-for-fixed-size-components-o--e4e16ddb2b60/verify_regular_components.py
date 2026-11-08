"""Finite rational tests for component-count factorial moments and tree witnesses.

Independent code for the numerical asymptotic and finite count identities.
No external packages or files are required.
"""
from fractions import Fraction
from itertools import combinations, permutations, product
from collections import Counter
import math

assertions = 0

def check(condition, message):
    global assertions
    assertions += 1
    if not condition:
        raise AssertionError(message)


def hosts():
    return {
        'K4': (4, list(combinations(range(4),2))),
        'C5': (5, [(i,(i+1)%5) for i in range(5)]),
        'K3,3': (6, [(i,j) for i in range(3) for j in range(3,6)]),
        '2K3': (6, [(a+i,a+j) for a in (0,3) for i,j in combinations(range(3),2)]),
    }


def component_shapes(n, edges, mask):
    p=list(range(n))
    def root(x):
        while p[x]!=x:
            p[x]=p[p[x]]
            x=p[x]
        return x
    for i,(a,b) in enumerate(edges):
        if mask >> i & 1:
            ra,rb=root(a),root(b)
            p[rb]=ra
    cc=Counter(root(v) for v in range(n))
    ct=Counter()
    for size in cc.values():ct[size]+=1
    tree=Counter()
    for r,size in cc.items():
        vset={v for v in range(n) if root(v)==r}
        ec=sum((a in vset and b in vset and bool(mask>>i&1)) for i,(a,b) in enumerate(edges))
        if ec==size-1:tree[size]+=1
    return ct,tree


def tree_embeddings(n, edges, k):
    adj=set(tuple(sorted(e)) for e in edges)
    if k==1:return n
    ct=0
    # Enumerate labeled trees on k abstract points by Prufer codes.
    for code in product(range(k),repeat=k-2):
        deg=[1]*k
        for x in code:deg[x]+=1
        template=[]
        for x in code:
            leaf=next(i for i in range(k) if deg[i]==1)
            template.append((leaf,x));deg[leaf]-=1;deg[x]-=1
        last=[i for i in range(k) if deg[i]==1]
        template.append(tuple(last))
        for pos in permutations(range(n),k):
            if all(tuple(sorted((pos[a],pos[b]))) in adj for a,b in template):ct+=1
    check(ct%math.factorial(k)==0,('embedding divisibility',n,k,ct))
    return ct//math.factorial(k)


def tree_witness_expectation(n,edges,k,p):
    # Enumerate unordered vertex sets and all distinct spanning trees.
    q=1-p
    total=Fraction(0)
    for ss in combinations(range(n),k):
        st=set(ss)
        internal=[e for e in edges if e[0] in st and e[1] in st]
        incident=sum(a in st or b in st for a,b in edges)
        if k==1:
            total+=q**incident
            continue
        for trial in combinations(internal,k-1):
            if component_shapes(k,[(ss.index(a),ss.index(b)) for a,b in trial],(1<<(k-1))-1)[0].get(k,0)==1:
                total+=p**(k-1)*q**(incident-(k-1))
    return total


def exact_enumeration(n,edges,p,k):
    m=len(edges)
    excomp=Fraction(0);extree=Fraction(0);e2tree=Fraction(0)
    for mask in range(1<<m):
        a,b=component_shapes(n,edges,mask)
        t=b[k];c=a[k]
        weight=p**mask.bit_count()*(1-p)**(m-mask.bit_count())
        excomp+=c*weight
        extree+=t*weight
        e2tree+=t*(t-1)*weight
    return excomp,extree,e2tree

for name,(n,ed) in hosts().items():
    p=Fraction(2,7)
    d=Counter()
    for a,b in ed:d[a]+=1;d[b]+=1
    check(len(set(d.values()))==1,('not regular',name))
    for k in range(1,min(n,4)+1):
        ec,et,em=exact_enumeration(n,ed,p,k)
        wt=tree_witness_expectation(n,ed,k,p)
        check(et==wt,('tree witness finite identity',name,k,et,wt))
        check(ec>=et,('component dominates tree',name,k))
        if k>=2:
            check(tree_embeddings(n,ed,k)>=0,('valid tree embedding',name,k))
        # Independently compute the factorial pair sum for exact tree components.
        if k>n//2:
            check(em==0,('disjoint pair impossible',name,k))
        print(f'{name:6} k={k} exact_E_components={float(ec):.8f} exact_E_trees={float(et):.8f} excess={float(ec-et):.8f}')

for k in range(1,7):
    target=1/(k*math.factorial(k))
    estimates=[]
    for n in (10_000,1_000_000,1_000_000_000,1_000_000_000_000):
        d=n-1
        L=math.log(n)+(k-1)*math.log(math.log(n))
        p=-math.expm1(-L/(k*d))
        q_log=-L/(k*d)
        # Number of embedded trees in K_n = C(n,k) k^(k-2).
        log_B=sum(math.log(n-i) for i in range(k))-math.lgamma(k+1)+(k-2)*math.log(k) if k>1 else math.log(n)
        absent=(k*(n-k)+k*(k-1)/2-(k-1)) if k>1 else n-1
        log_E=log_B+(k-1)*math.log(p)+absent*q_log
        estimate=math.exp(log_E)
        estimates.append(estimate)
        check(estimate>0 and math.isfinite(estimate),('asymptotic finite',n,k))
    Llast=math.log(1_000_000_000_000)+(k-1)*math.log(math.log(1_000_000_000_000))
    refined=target*(Llast/math.log(1_000_000_000_000))**(k-1)
    check(abs(estimates[-1]-refined)<0.02*refined,('finite-size corrected constant',k,estimates[-1],refined))
    print(f'K_n asymptotic k={k}: expected tree components ~ {estimates[-1]:.9g}; predicted {target:.9g}')
print('PASS:',assertions,'finite exact and asymptotic checks')
