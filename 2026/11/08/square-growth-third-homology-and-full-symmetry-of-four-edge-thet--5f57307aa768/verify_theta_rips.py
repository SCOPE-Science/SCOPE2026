#!/usr/bin/env python3
"""Finite cross-checks for the four-edge multi-theta Rips theorem.

Run with Python 3 standard library: python3 verify_theta_rips.py
This validates finite cases; the all-m theorem uses the symbolic join proof.
"""


def graph(m):
    assert m >= 2
    n = 3*m+2
    adj = [set() for _ in range(n)]
    for i in range(m):
        p, a, b, c, q = 0, 2+3*i, 3+3*i, 4+3*i, 1
        for u,v in ((p,a),(a,b),(b,c),(c,q)):
            adj[u].add(v); adj[v].add(u)
    return adj


def distances(adj):
    n=len(adj)
    d=[]
    for s in range(n):
        ds=[n+1]*n; ds[s]=0
        queue=[s]
        for u in queue:
            for v in adj[u]:
                if ds[v]==n+1:
                    ds[v]=ds[u]+1; queue.append(v)
        assert len(queue)==n
        d.append(ds)
    return d


def faces_at_distance(d,r):
    n=len(d)
    neighbors=[{j for j in range(i+1,n) if d[i][j]<=r} for i in range(n)]
    faces={}
    def extend(prefix,candidates):
        for v in sorted(candidates):
            t=prefix+(v,)
            faces.setdefault(len(t)-1,[]).append(t)
            extend(t,{w for w in candidates if w>v and w in neighbors[v]})
    extend((),set(range(n)))
    return [faces.get(k,[]) for k in range(max(faces)+1)]


def mod2_betti(fs):
    ranks=[]
    for k in range(1,len(fs)):
        idx={f:j for j,f in enumerate(fs[k-1])}; piv={}; rank=0
        for f in fs[k]:
            vector=0
            for j in range(len(f)):
                b=f[:j]+f[j+1:]
                vector ^= 1<<idx[b]
            while vector:
                lead=vector.bit_length()
                if lead in piv: vector ^= piv[lead]
                else:
                    piv[lead]=vector; rank+=1; break
        ranks.append(rank)
    return [len(f)-(ranks[k-1] if k else 0)-(ranks[k] if k<len(ranks) else 0)-(k==0) for k,f in enumerate(fs)]


def permutation(m,sigma,flip=False):
    v=[0]*(3*m+2)
    v[0]=1 if flip else 0
    v[1]=0 if flip else 1
    for i in range(m):
        j=sigma[i]
        for typ in range(3):
            v[2+3*i+typ]=2+3*j+(2-typ if flip else typ)
    assert sorted(v)==list(range(len(v)))
    return v


def sign_of_permutation(x):
    inv=sum(x[i]>x[j] for i in range(len(x)) for j in range(i+1,len(x)))
    return -1 if inv%2 else 1


def signed_reduced_lefschetz(fs,v):
    # The empty face contributes -1 to the ordinary alternating simplex trace.
    tr=-1
    for k,faces in enumerate(fs):
        for f in faces:
            mapped=[v[x] for x in f]
            if sorted(mapped)==list(f):
                tr+=(-1)**k*sign_of_permutation(mapped)
    return tr


def test():
    checked=0
    for m in range(2,8):
        a=graph(m);d=distances(a);n=len(a)
        assert max(map(max,d))==4
        assert all(d[0][1]==4 for _ in [0])
        # Independent determination of all forbidden distance-three pairs.
        forbidden={tuple(sorted((0,1)))}
        forbidden.update((3+3*i,3+3*j) for i in range(m) for j in range(i+1,m))
        forbidden.update(tuple(sorted((2+3*i,4+3*j))) for i in range(m) for j in range(m) if i!=j)
        actual={(i,j) for i in range(n) for j in range(i+1,n) if d[i][j]>3}
        assert actual==forbidden,(m,actual.symmetric_difference(forbidden))
        for radius,expected in ((1,[0,m-1]),(2,[0,m-1]),(3,[0,0,0,(m-1)**2])):
            fs=faces_at_distance(d,radius)
            betti=mod2_betti(fs)
            assert betti[:len(expected)]==expected,(m,radius,betti)
            assert not any(betti[len(expected):]),(m,radius,betti)
            if radius==3:
                ftotal=3*(m+1)*(2**(m+1)+m-1)-1
                assert sum(map(len,fs))==ftotal,(m,list(map(len,fs)),ftotal)
                if m<=5:
                    maps=[(tuple(range(m)),False),
                          (tuple(range(m)),True),
                          (tuple([1,0]+list(range(2,m))),False),
                          (tuple(list(range(1,m))+[0]),True)]
                    for sigma,flip in maps:
                        v=permutation(m,sigma,flip)
                        assert all(v[j] in a[v[i]] for i in range(n) for j in a[i])
                        assert all(d[v[i]][v[j]]==d[i][j] for i in range(n) for j in range(n))
                        fixed=sum(i==sigma[i] for i in range(m))
                        assert signed_reduced_lefschetz(fs,v)==-(fixed-1)**2,(m,sigma,flip)
            checked+=1
        print('m=',m,'n=',n,'r=3 f=',ftotal,'beta3=',(m-1)**2,'PASS')
    print('ALL_CHECKS_PASS',checked,'complexes; exact forbidden pairs; rational character samples; mod-two chain ranks')

if __name__=='__main__':test()
