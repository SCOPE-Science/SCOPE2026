"""Independent finite verification for induced-path partial automorphism estimates."""
from itertools import combinations, permutations
from collections import Counter, defaultdict
from math import factorial


def run_profile(mask, n):
    runs=[]
    j=0
    while j<n:
        if (mask>>j)&1:
            k=j
            while j<n and (mask>>j)&1:
                j+=1
            runs.append(j-k)
        else:
            j+=1
    return tuple(sorted(Counter(runs).items()))


def finite_distribution(n):
    types=defaultdict(lambda: [0,0,0])
    for mask in range(1<<n):
        p=run_profile(mask,n)
        row=types[p]
        row[0]+=1
        row[1]=mask.bit_count()
        row[2]=sum(y for x,y in p)
    byrank=Counter(); bycomponent=Counter(); byedge=Counter()
    for p,(m,k,c) in types.items():
        aut=1
        for length,a in p:
            aut*=factorial(a)*(2 if length>1 else 1)**a
        cnt=m*m*aut
        byrank[k]+=cnt;bycomponent[c]+=cnt;byedge[k-c]+=cnt
    return byrank,bycomponent,byedge


def brute_distribution(n):
    subsets={k:[] for k in range(n+1)}
    for k in range(n+1):
        subsets[k]=list(combinations(range(n), k))
    br=Counter();bc=Counter();be=Counter()
    for k in range(n+1):
        for A in subsets[k]:
            ed={(i,j) for i in range(k) for j in range(i+1,k) if abs(A[i]-A[j])==1}
            c=k-len(ed)
            for B in subsets[k]:
                for im in permutations(B):
                    if all((abs(im[i]-im[j])==1)==((i,j) in ed) for i in range(k) for j in range(i+1,k)):
                        br[k]+=1;bc[c]+=1;be[k-c]+=1
    return br,bc,be


for n in range(1,7):
    a=finite_distribution(n)
    b=brute_distribution(n)
    assert a==b,(n,a,b)
    print('EXHAUSTIVE',n,'TOTAL',sum(a[0].values()),'RANK',sorted(a[0].items()))

for n in [8,12,16,20]:
    ranks,components,edges=finite_distribution(n)
    total=sum(ranks.values());h=(n+1)//2
    assert total==sum(components.values())==sum(edges.values())
    assert factorial(h) <=total<=8**n*factorial(h)
    for k in range(h+1):
        count=sum(v for c,v in components.items() if c<=k)
        assert count*factorial(h)<=total*(8**n)*factorial(k)
        ranklower=sum(v for r,v in ranks.items() if r<=k)
        assert ranklower<=count
        assert ranklower*factorial(h)<=total*(8**n)*factorial(k)
        assert count>=factorial(k) and ranklower>=factorial(k)
    print('BOUNDARY',n,'TOTAL',total,'MEAN_RANK',round(sum(r*v for r,v in ranks.items())/total,5),'MEAN_COMPONENTS',round(sum(c*v for c,v in components.items())/total,5))
print('CHECKS PASS')
