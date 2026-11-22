"""Exact normalized signed-continuant verification of all-width claims."""
from collections import defaultdict

def histogram(n):
    d={(1,1):1}
    for j in range(2,n+1):
        nd=defaultdict(int)
        for (a,b),m in d.items():
            nd[(b,b+a)]+=m
            nd[(b,b-a)]+=m
        d=nd
    counts=defaultdict(int)
    for (a,b),m in d.items():counts[b]+=m
    return counts

fib=[0,1]
for _ in range(2,18):fib.append(fib[-1]+fib[-2])
expected={2:1,5:5,8:27,11:152,14:879}
for n in range(1,16):
    c=histogram(n)
    assert sum(c.values())==2**max(0,n-1)
    assert max(abs(x) for x in c)==fib[n+1]
    assert min(abs(x) for x in c if x)==(2 if n%3==2 else 1)
    assert (c.get(0,0)>0)==(n%3==2)
    if n in expected:assert c[0]==expected[n],(n,c[0])
    if n%3==2:
        k=(n+1)//3
        assert c[0]>=4**(k-1)
        print('resonant n=',n,'zero-normalized-signs=',c[0], 'null fraction=',f'{c[0]}/{2**(n-1)}')
print('RECURRENCE_OK')
