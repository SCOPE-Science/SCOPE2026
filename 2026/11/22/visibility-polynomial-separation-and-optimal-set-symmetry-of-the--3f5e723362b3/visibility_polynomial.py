"""Exact independent-set enumeration of ordinary mutual-visibility sets.

Uses a finite obstruction hypergraph and explicit graph automorphisms.
Requires Python 3 standard library only.
"""
from itertools import combinations, permutations, product
from collections import Counter
from hashlib import sha256

N=16
V=range(N)
xy=lambda v: divmod(v,4)

def edge(g,u,v):
    if u==v:return False
    a,b=xy(u);c,d=xy(v)
    if g=='R':return a==c or b==d
    dx=(c-a)%4;dy=(d-b)%4
    return (dx,dy) in ((1,0),(3,0),(0,1),(0,3),(1,1),(3,3))

def quartets(g):
    adj=[{v for v in V if edge(g,u,v)} for u in V]
    assert all(len(x)==6 for x in adj)
    out=set(); n_pairs=0
    for u,v in combinations(V,2):
        cs=adj[u]&adj[v]
        assert len(cs)==2
        if not edge(g,u,v):
            n_pairs+=1
            out.add(sum(1<<j for j in {u,v}|cs))
    assert n_pairs==72
    return sorted(out)

def membership(g):
    bad=quartets(g)
    n=Counter();tops=[];flags=[]
    for mask in range(1<<N):
        ok=all(mask&q!=q for q in bad)
        flags.append('1' if ok else '0')
        if ok:
            k=mask.bit_count();n[k]+=1
            if not tops or k>tops[0].bit_count():tops=[mask]
            elif k==tops[0].bit_count():tops.append(mask)
    assert sum(n.values())==flags.count('1')
    return n,tops,bad,sha256(''.join(flags).encode()).hexdigest()

def rook_automorphism_maps():
    ps=list(permutations(range(4)))
    for p in ps:
        for q in ps:
            for t in (0,1):
                yield tuple(4*(p[a] if not t else p[b]) + (q[b] if not t else q[a]) for a,b in map(xy,V))

def shrikhande_automorphism_maps():
    # All invertible linear maps of Z4^2 preserving the six Cayley generators,
    # followed by all sixteen translations.
    st={(1,0),(3,0),(0,1),(0,3),(1,1),(3,3)}
    for A,B,C,D in product(range(4),repeat=4):
        imgs={((A*x+B*y)%4,(C*x+D*y)%4) for x,y in st}
        if imgs!=st:continue
        for s,t in product(range(4),repeat=2):
            yield tuple(4*((A*x+B*y+s)%4)+((C*x+D*y+t)%4) for x,y in map(xy,V))

def orbit(g,seed):
    ims=list(rook_automorphism_maps() if g=='R' else shrikhande_automorphism_maps())
    assert len(ims)==(1152 if g=='R' else 192)
    assert len(set(ims))==len(ims)
    for p in ims:
        assert all(edge(g,u,v)==edge(g,p[u],p[v]) for u,v in combinations(V,2))
    return {sum(1<<p[u] for u in V if seed>>u&1) for p in ims}

def main():
    wanted={
      'R':([1,16,120,560,1784,3936,5728,4768,1512,96],36,96,
           '9e7519d29046d4130f286ed4b88f6362278acb553f9095e8e0859df356a8d7b0'),
      'S':([1,16,120,560,1760,3744,5216,4432,2004,384,32],60,32,
           '6fa4ad1ff4f4f2ec7e58ec30d93a5dd47919630e7da3974fb65669af9474e9a0')
    }
    for g in ('R','S'):
        hist,tops,bad,digest=membership(g)
        expect,kbad,ntop,wsha=wanted[g]
        assert [hist[k] for k in range(len(expect))]==expect
        assert sum(hist.values())==sum(expect)
        assert len(bad)==kbad and len(tops)==ntop and digest==wsha
        assert orbit(g,tops[0])==set(tops)
        assert all(not any(((m ^ (1<<a) ^ (1<<b)) in set(tops)) for a in V if m>>a&1 for b in V if not m>>b&1) for m in tops)
        print(g,'polynomial',expect,'forbidden',len(bad),'max',len(tops),'orbit',len(orbit(g,tops[0])),'membership_sha256',digest)
    print('VISIBILITY_EXACT_PY_OK')

if __name__=='__main__':main()
