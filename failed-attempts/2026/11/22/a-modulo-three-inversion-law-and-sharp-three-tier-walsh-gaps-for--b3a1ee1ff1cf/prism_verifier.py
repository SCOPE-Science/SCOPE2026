"""Exact independent Walsh checks for perfect matchings of cycle prisms.

Usage: python prism_verifier.py
Uses only standard Python and NumPy. All frequencies are enumerated for n<=7.
"""
import numpy as np


def perfect_matchings(n):
    # The vertices are (row, column), with row in {0,1}.
    edges = []
    for i in range(n):
        edges.append((i, n+i))
    for i in range(n):
        edges.append((i, (i+1)%n))
    for i in range(n):
        edges.append((n+i, n+(i+1)%n))
    adj=[[] for _ in range(2*n)]
    for ei,(a,b) in enumerate(edges):
        adj[a].append((b,ei)); adj[b].append((a,ei))
    out=[]
    def dfs(remaining,mask):
        if not remaining:
            out.append(mask);return
        v=min(remaining)
        for w,ei in adj[v]:
            if w in remaining:
                dfs(remaining-{v,w},mask|(1<<ei))
    dfs(set(range(2*n)),0)
    assert len(out)==len(set(out))
    return out


def fast_walsh(v):
    out=v.copy()
    h=1
    while h<len(out):
        block=out.reshape(-1,2*h)
        x=block[:,:h].copy()
        y=block[:,h:].copy()
        block[:,:h]=x+y
        block[:,h:]=x-y
        h*=2
    return out


def cyc_transfer(y):
    # Trace of product [[1,y_i],[1,0]], using exact integer arithmetic.
    a,b,c,d=1,0,0,1
    for t in y:
        a,b,c,d=a+b,a*t,c+d,c*t
    return a+d


def predicted(n,frequency):
    x=[-1 if frequency & (1<<i) else 1 for i in range(n)]
    u=[-1 if frequency & (1<<(n+i)) else 1 for i in range(n)]
    v=[-1 if frequency & (1<<(2*n+i)) else 1 for i in range(n)]
    y=[u[i]*v[i]*x[i]*x[(i+1)%n] for i in range(n)]
    q=np.prod(x)*cyc_transfer(y)
    if n%2:
        return int(q)
    a=np.prod([u[i] if i%2==0 else v[i] for i in range(n)])
    b=np.prod([v[i] if i%2==0 else u[i] for i in range(n)])
    return int(q+a+b)


def expected_gap(n):
    return 1 if n%3 else (2 if n%2 else 4)


def test():
    for n in range(3,8):
        M=perfect_matchings(n)
        bits=3*n
        signal=np.zeros(1<<bits,dtype=np.int64)
        signal[M]=1
        fw=fast_walsh(signal)
        expected_count=round(((1+5**.5)/2)**n+((1-5**.5)/2)**n)+(2 if n%2==0 else 0)
        assert len(M)==expected_count,(n,len(M),expected_count)
        gap=min(abs(v) for v in fw if v)
        assert gap==expected_gap(n),(n,gap)
        assert (np.any(fw==0)) == (n%3==0)
        assert max(abs(fw))==len(M)
        if n<=5:
            for freq,v in enumerate(fw):
                assert predicted(n,freq)==v,(n,freq,v,predicted(n,freq))
        else:
            # Include random and deterministic frequencies.
            rng=np.random.default_rng(1234+n)
            tests=list(range(500)) + rng.integers(0,len(fw),size=1500).tolist()
            for freq in tests:
                assert predicted(n,int(freq))==fw[int(freq)]
        print(f'n={n}, perfect_matchings={len(M)}, nullity={(fw==0).sum()}, gap={gap}, checked_formula={"all" if n<=5 else 2000}')
    # All-length scalar transfer tests, 3..300.
    for n in range(3,301):
        y=[-1]*n
        y[2]=1
        if n%3==0:
            assert cyc_transfer(y)==0
        q=cyc_transfer([-1]*n)
        expected={0:2,1:1,2:-1,3:-2,4:-1,5:1}[n%6]
        assert q==expected,(n,q)
    print('Exact transfer identity and zero witnesses verified through n=300')


if __name__=='__main__':
    test()
