from itertools import combinations
from math import comb

def enum(n):
    out = {(-1,)*n}
    for s in range(-n+1,n):
        base = [i+s if 0<=i+s<n else -1 for i in range(n)]
        allowed = [i for i,v in enumerate(base) if v!=-1]
        for mask in range(1<<len(allowed)):
            arr = [-1]*n
            for j,i in enumerate(allowed):
                if mask>>j &1:arr[i]=base[i]
            out.add(tuple(arr))
    for c in range(0, 2*n-1):
        base = [c-i if 0<=c-i<n else -1 for i in range(n)]
        allowed = [i for i,v in enumerate(base) if v!=-1]
        for mask in range(1<<len(allowed)):
            arr=[-1]*n
            for j,i in enumerate(allowed):
                if mask>>j&1:arr[i]=base[i]
            out.add(tuple(arr))
    return list(out)

def compose(f,g):
    return tuple(-1 if x<0 else f[x] for x in g)

for n in range(2,8):
    fs=enum(n)
    nID=sum(compose(f,f)==f for f in fs)
    cnt=0
    for i,f in enumerate(fs):
        for j in range(i,len(fs)):
            g=fs[j]
            if compose(f,g)==compose(g,f):cnt+=1 if i==j else 2
    expected=6*2**n-n*n-4*n-5
    print(n,len(fs),expected,nID,cnt,round(cnt/len(fs)**2,7))
for n in range(2,8):
    fs=enum(n)
    computed=sum(sum(compose(e,f)==compose(f,e) for e in fs if compose(e,e)==e) for f in fs)
    H=lambda ell:2**(n-ell)*10**(ell//2)*4**(ell%2)
    forecast=4**n+4*3**n+H(n)+2*sum(H(l) for l in range(1,n))-(5*n+3)*2**n-n*(n-1)*2**(n-1)
    print('weighted',n,computed,forecast, 'match',computed==forecast)
