from collections import Counter
from math import log2

def rank(vs):
    b={}
    for v in vs:
        while v:
            t=v.bit_length()-1
            if t in b: v ^= b[t]
            else:
                b[t]=v;break
    return len(b)

def check(m):
    n=1<<m
    words=[]
    for a in range(n):
        for c in (0,1):
            w=sum((((((a & t).bit_count())&1)^c)<<t) for t in range(n))
            pw=sum(bool((w>>t)&1 or (w>>((t+1)%n))&1) for t in range(n))
            words.append((a,c,w,pw))
    hist=Counter(pw for a,c,w,pw in words)
    expected={0:1,n:3,**{n//2+r:4 for r in range(1,n//2)}}
    assert hist==expected,(m,hist,expected)
    vals=sorted(set(pw for a,c,w,pw in words))
    for alpha in range(n+1):
        got=rank([w for a,c,w,pw in words if pw>0 and pw<=alpha])
        if alpha<n//2+1: pred=0
        else:pred=min(m+1,3+(alpha-n//2).bit_length()-1)
        assert got==pred,(m,alpha,got,pred)
    print('PASS',m,'n',n,'words',len(words),'pair weights',list(hist.items())[:5], 'full at',3*n//4)

for m in range(2,9):check(m)
print('CERTIFICATE_OK')
