from collections import Counter
from itertools import combinations

def parity(x):return x.bit_count() & 1

def enumerate_law(n):
    edges=list(combinations(range(n),2)); out=Counter()
    for mask in range(1<<len(edges)):
        rows=[0]*n
        for j,(a,b) in enumerate(edges):
            if mask>>j&1: rows[a]^=1<<b;rows[b]^=1<<a
        d=sum(parity(rows[i])<<i for i in range(n))
        t=sum(parity(rows[i]&d)<<i for i in range(n))
        out[(d,t)]+=1
    return out

def analytic_pair_count(n,d,t):
    m=n*(n-1)//2
    allones=(1<<n)-1
    if parity(d) or parity(t):return 0
    if d==0:return (1<<(m-n+1)) if t==0 else 0
    if n%2==0 and d==allones:return (1<<(m-n+1)) if t==d else 0
    if parity(d&t):return 0
    return 1<<(m-2*n+3)

for n in range(2,7):
    actual=enumerate_law(n)
    for d in range(1<<n):
        for t in range(1<<n):
            pred=analytic_pair_count(n,d,t)
            assert actual[d,t]==pred,(n,d,t,actual[d,t],pred)
    marginal=Counter()
    for (d,t),v in actual.items():marginal[t]+=v
    print(n,len(actual),len(marginal),sorted(marginal.items())[:4])
print('ALL_TWO_LAYER_EXHAUSTIVE_CHECKS_PASS')
