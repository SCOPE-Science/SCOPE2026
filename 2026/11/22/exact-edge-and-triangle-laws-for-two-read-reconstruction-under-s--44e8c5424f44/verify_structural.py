"""Independent interval-and-context enumeration for the two-read graph."""
from itertools import product

def legal(w): return '001' not in w

def fib(k):
    a,b=0,1
    for _ in range(k): a,b=b,a+b
    return a

def coefficients(nmax=32):
    # P(z)=1/(1-z-z^2) and S(z)=(1+z)/(1-z-z^2).
    P=[fib(i+1) for i in range(nmax+1)]
    S=[fib(i+2) for i in range(nmax+1)]
    H=[sum(P[j]*S[i-j] for j in range(i+1)) for i in range(nmax+1)]
    E=[sum(H[n-L] for L in range(2,n+1)) for n in range(nmax+1)]
    T=[sum((L-3)*H[n-L] for L in range(4,n+1)) for n in range(nmax+1)]
    for n in range(nmax+1):
        assert T[n] == sum(E[j] for j in range(2,n-1))
    return E,T

def structural_sets(n):
    edges=set();triangles=set()
    for ell in range(2,n+1):
        for prelen in range(n-ell+1):
            suflen=n-ell-prelen
            prefixes=[''.join(w) for w in product('01',repeat=prelen) if prelen==0 or (w[-1]=='1' and legal(''.join(w)))]
            suffixes=[''.join(w) for w in product('01',repeat=suflen) if legal(''.join(w)) and (suflen==0 or (w[0]=='1' or all(c=='0' for c in w)))]
            a=''.join('01'[i%2] for i in range(ell));b=''.join('10'[i%2] for i in range(ell))
            for pre in prefixes:
                for suf in suffixes:
                    x=pre+a+suf;y=pre+b+suf
                    assert legal(x) and legal(y)
                    edges.add(tuple(sorted((x,y))))
                    if ell>=4:
                        for cut in range(2,ell-1):
                            for zcore in (a[:cut]+b[cut:], b[:cut]+a[cut:]):
                                z=pre+zcore+suf
                                if legal(z):
                                    triangles.add(tuple(sorted((x,y,z))))
    return edges,triangles

def direct_sets(n):
    words=[''.join(w) for w in product('01',repeat=n) if legal(''.join(w))]
    D={w:{w[:i]+w[i+1:] for i in range(n)} for w in words}
    edges={tuple(sorted((x,y))) for i,x in enumerate(words) for y in words[i+1:] if len(D[x]&D[y])>=2}
    triangles=set()
    adjacency={x:set() for x in words}
    for x,y in edges:adjacency[x].add(y);adjacency[y].add(x)
    for x,y in edges:
        for z in adjacency[x]&adjacency[y]:
            if z>y:triangles.add(tuple(sorted((x,y,z))))
    return edges,triangles

def main():
    E,T=coefficients()
    for n in range(2,11):
        e,t=structural_sets(n)
        de,dt=direct_sets(n)
        assert e==de and t==dt, (n,len(e),len(de),len(t),len(dt))
        assert len(e)==E[n] and len(t)==T[n]
        print(n,len(e),len(t))
    print('first 16 edge coefficients:',E[:16])
    print('first 16 triangle coefficients:',T[:16])
    print('VERIFY_STRUCTURAL_OK')
if __name__=='__main__': main()
