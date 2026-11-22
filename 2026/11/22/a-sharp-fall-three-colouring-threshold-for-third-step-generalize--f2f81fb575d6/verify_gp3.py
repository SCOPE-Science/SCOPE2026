"""Independent finite checks of fall 3-colourings of GP(n,3).
Run with Python 3 (standard library only)."""
from itertools import product, permutations
from collections import Counter
BASE={
9:("010120212","122211000"),
10:("0102101201","2211020112"),
11:("01021021021","22110202110"),
12:("010210210212","221102021100"),
13:("0102101201212","2211020112000"),
14:("01021012010212","22110201122000"),
15:("010210120121021","221102011200112"),
16:("0102101201012012","2211020112221100"),
17:("01021021020210212","22110202111022100"),
18:("010210120101201021","221102011220012100"),
19:("0101201201202012012","1220012120011120201"),
}

def explicit_graph_valid(a,b):
    n=len(a)
    if len(b)!=n or n<7:return False
    c=[int(x) for x in a+b]
    e=[]
    for i in range(n):
        e.extend([(i,(i+1)%n),(i,n+i),(n+i,n+(i+3)%n)])
    adj=[set() for _ in range(2*n)]
    for x,y in e:
        adj[x].add(y);adj[y].add(x)
        if c[x]==c[y]:return False
    return all(len({c[v] for v in adj[i]})==2 for i in range(2*n))

def local_valid(a,b):
    n=len(a)
    return (n>=7 and len(b)==n and all(a[i]!=b[i] and a[i]!=a[(i+1)%n] and b[i]!=b[(i+3)%n] and len({a[(i-1)%n],a[(i+1)%n],b[i]})==2 and len({b[(i-3)%n],b[(i+3)%n],a[i]})==2 for i in range(n)))

def orbit(w):
    return {''.join(p[int(x)] for x in (w[k:]+w[:k] if not rev else (w[::-1][k:]+w[::-1][:k]))) for p in permutations('012') for rev in (0,1) for k in range(len(w))}

def profile(n):
    proper=[''.join(v) for v in product('012',repeat=n) if all(v[i]!=v[(i+1)%n] for i in range(n))]
    pool=set(proper); out=[]
    while pool:
        rep=min(pool);o=orbit(rep);assert o<=pool
        pool-=o
        choices=[]
        for i in range(n):
            choices.append([v for v in '012' if v!=rep[i] and len({rep[(i-1)%n],rep[(i+1)%n],v})==2])
        ext=[''.join(t) for t in product(*choices)]
        edge=[b for b in ext if all(b[i]!=b[(i+3)%n] for i in range(n))]
        valid=[b for b in edge if explicit_graph_valid(rep,b)]
        out.append((rep,len(o),len(ext),len(edge),len(valid)))
    return sorted(out)

EXPECTED={7:[('0101012',42,8,0,0),('0101202',42,8,4,0),('0102012',42,32,2,0)],
8:[('01010101',6,1,0,0),('01010102',48,4,0,0),('01010202',24,4,0,0),('01010212',48,16,1,0),('01012012',48,64,0,0),('01012102',48,16,3,0),('01020102',12,16,0,0),('01021012',24,64,0,0)]}

def construct(n):
    if n in BASE:return BASE[n]
    assert n>=20
    if n<=28: parts=[10,n-10]
    elif n==29:parts=[11,18]
    else:
        a,b=construct(n-10)
        x,y=BASE[10]
        return a+x,b+y
    return tuple(''.join(BASE[j][k] for j in parts) for k in range(2))

def main():
    for n in (7,8):
        actual=profile(n)
        assert actual==EXPECTED[n],(n,actual)
        print('EXHAUSTIVE n',n,'outer_words',sum(z[1] for z in actual),'orbits',len(actual),'valid',sum(z[4] for z in actual),'PASS')
    prefix=None
    for n,(a,b) in BASE.items():
        assert len(a)==len(b)==n
        assert explicit_graph_valid(a,b) and local_valid(a,b),(n,a,b)
        if 10<=n<=18:
            pref=list(zip(a[:6],b[:6]))
            if prefix is None:prefix=pref
            assert pref==prefix,(n,pref)
        print('BASE',n,'PASS')
    for n in range(20,201):
        a,b=construct(n)
        assert explicit_graph_valid(a,b) and local_valid(a,b),n
    print('SPLICED_20_TO_200_PASS')
    print('VERIFY_OK')
if __name__=='__main__': main()
