#!/usr/bin/env python3
"""Independent shortest-path face oracle and finite homology checks for wheel general-position complexes."""
from collections import Counter
from itertools import combinations


def wheel(n):
    g=[set() for _ in range(n+1)]
    for i in range(n):
        for j in ((i+1)%n,n):
            g[i].add(j); g[j].add(i)
    return g


def distances(g):
    d=[]
    for a in range(len(g)):
        row=[-1]*len(g); row[a]=0; q=[a]
        for x in q:
            for y in g[x]:
                if row[y]<0: row[y]=row[x]+1;q.append(y)
        d.append(row)
    return d


def enumerated_gp_faces(n):
    g=wheel(n); d=distances(g)
    bad=[]
    for a,b,c in combinations(range(n+1),3):
        if any(d[x][y]+d[y][z]==d[x][z] for x,y,z in [(a,b,c),(a,c,b),(b,a,c)]):
            bad.append((1<<a)|(1<<b)|(1<<c))
    return [q for q in range(1<<(n+1)) if all(q&t!=t for t in bad)]


def predicted_faces(n):
    r=[]
    for mask in range(1<<(n+1)):
        rim=mask&((1<<n)-1); bits=[(rim>>i)&1 for i in range(n)]
        if mask&(1<<n):
            on=[i for i in range(n) if bits[i]]
            good=(len(on)<=1 or len(on)==2 and ((on[1]-on[0])%n in (1,n-1))) if n>=4 else True
        else:
            good= all(not(bits[i] and bits[(i+1)%n] and bits[(i+2)%n]) for i in range(n)) if n>=4 else True
        if good: r.append(mask)
    return r


def rank_mod2(cols):
    pivots={}
    for x in cols:
        while x:
            p=x.bit_length()-1
            if p in pivots: x^=pivots[p]
            else: pivots[p]=x;break
    return len(pivots)


def betti(faces):
    fs={}
    for x in faces:
        if x: fs.setdefault(x.bit_count()-1,[]).append(x)
    ranks={}
    for k in range(1,max(fs)+1):
        rowindex={x:i for i,x in enumerate(fs[k-1])}
        cols=[]
        for mask in fs.get(k,[]):
            cc=0; mm=mask
            while mm:
                b=mm&-mm;mm^=b
                cc^=1<<rowindex[mask^b]
            cols.append(cc)
        ranks[k]=rank_mod2(cols)
    return {k:len(v)-ranks.get(k,0)-ranks.get(k+1,0)-(1 if k==0 else 0) for k,v in fs.items() if len(v)-ranks.get(k,0)-ranks.get(k+1,0)-(1 if k==0 else 0)!=0}


def expected(n):
    if n==3:return {}
    if n==4:return {1:2}
    if n==5:return {1:1,2:1}  # mod-two RP^2
    k,r=divmod(n,4)
    if r==0: other=(2*k-1,3)
    elif r==1:other=(2*k-1,1)
    elif r==2:other=(2*k,1)
    else:other=(2*k+1,1)
    ans={2:1}; degree,count=other
    ans[degree]=ans.get(degree,0)+count
    return ans


def surface5(faces):
    n=5; fs=set(faces)
    assert len([f for f in fs if f.bit_count()==3])==10
    assert len([f for f in fs if f.bit_count()==2])==15
    assert len([f for f in fs if f.bit_count()==1])==6
    tris=[x for x in fs if x.bit_count()==3]
    for a,b in combinations(range(6),2):
        assert sum(1 for t in tris if (t&(1<<a)) and (t&(1<<b)))==2
    for v in range(6):
        links=[t^(1<<v) for t in tris if t&(1<<v)]
        assert len(links)==5
        deg=Counter()
        for link in links:
            for u in range(6):
                if (link>>u)&1:deg[u]+=1
        assert sorted(deg.values())==[2]*5
        visited={next(iter(deg))};stack=list(visited)
        while stack:
            x=stack.pop()
            for e in links:
                if e&(1<<x):
                    y=(e^(1<<x)).bit_length()-1
                    if y not in visited:visited.add(y);stack.append(y)
        assert len(visited)==5
    assert 6-15+10==1
    return 'closed connected surface, Euler characteristic 1 => RP2'


def main():
    for n in range(3,13):
        gp=enumerated_gp_faces(n)
        pp=predicted_faces(n)
        assert gp==pp,(n,'face-rule mismatch')
        b=betti(gp)
        assert b==expected(n),(n,b,expected(n))
        counts=Counter(x.bit_count()-1 for x in gp if x)
        print(f'n={n} faces={len(gp)} face_vector={[counts[i] for i in range(max(counts)+1)]} mod2_reduced_betti={b}')
        if n==5: print('n=5 surface_check='+surface5(gp))
    print('PASS: independent shortest-path faces, induced-run characterization, and mod-2 homology, 3<=n<=12')

if __name__=='__main__':main()
