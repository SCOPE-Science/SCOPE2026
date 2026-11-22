#!/usr/bin/env python3
"""Exact finite verification for geodesic general-position caterpillar complexes.

No external packages needed. All operations are over integer bitmasks; an
explicit sequence of free-face collapses is checked face by face.
"""
from itertools import product, combinations

def data(profile):
    m=len(profile)
    parents=[]
    for i,a in enumerate(profile): parents.extend([i]*a)
    n=m+len(parents)
    def distance(a,b):
        if a==b: return 0
        ia= a if a<m else parents[a-m]
        ib= b if b<m else parents[b-m]
        return abs(ia-ib)+(a>=m)+(b>=m)
    bad=[]
    for a,b,c in combinations(range(n),3):
        if distance(a,b)+distance(b,c)==distance(a,c) or distance(a,c)+distance(c,b)==distance(a,b) or distance(b,a)+distance(a,c)==distance(b,c):
            bad.append((1<<a)|(1<<b)|(1<<c))
    faces={s for s in range(1<<n) if all(s&f!=f for f in bad)}
    return faces,m,n,parents

def collapse(profile,verbose=False):
    faces,m,n,parents=data(profile)
    initial=len(faces)
    toggles=0
    def remove(F,a):
        nonlocal toggles
        G=F|(1<<a)
        assert F in faces and G in faces and F!=G,(profile,'not pair',F,a)
        cofaces=[x for x in faces if F&x==F]  # exact, not just codim-one
        assert set(cofaces)=={F,G},(profile,'not free',F,a,[hex(x) for x in cofaces[:8]])
        faces.remove(F);faces.remove(G);toggles+=1
    # Phase I: two distinct backbone vertices with nonempty intervening leaf set.
    for i in range(m):
      for j in range(i+1,m):
        middle=[m+k for k,p in enumerate(parents) if i<p<j]
        if not middle:continue
        a=middle[0]
        candidates=[f for f in faces if (f&(1<<i)) and (f&(1<<j)) and not(f&(1<<a))]
        for f in sorted(candidates,key=lambda x:(-x.bit_count(),x)):
            remove(f,a)
    # Phase II: each one-backbone-vertex cone with leaves on one side.
    for i in range(m):
      for side in ('left','right'):
        leaves=[m+k for k,p in enumerate(parents) if (p<i if side=='left' else p>i)]
        if not leaves:continue
        a=leaves[0]
        candidates=[f for f in faces if f&(1<<i) and f.bit_count()>=2 and (f & ((1<<m)-1)) == (1<<i) and all((f&(1<<(m+k)))==0 or m+k in leaves for k in range(len(parents))) and not f&(1<<a)]
        for f in sorted(candidates,key=lambda x:(-x.bit_count(),x)):
            remove(f,a)
    # Phase III: leaf simplex to tree of leaf edges through fixed leaf.
    if parents:
        a=m
        candidates=[f for f in faces if f>>(m) and (f & ((1<<m)-1))==0 and f.bit_count()>=2 and not f&(1<<a)]
        for f in sorted(candidates,key=lambda x:(-x.bit_count(),x)):
            remove(f,a)
    assert all(f.bit_count()<=2 for f in faces),(profile,'non-graph')
    V={f for f in faces if f.bit_count()==1};E={f for f in faces if f.bit_count()==2}
    assert len(V)==n
    # Every leaf connects to the leaf-star; every backbone vertex connects via backbone path.
    adj={i:set() for i in range(n)}
    for e in E:
        u=[i for i in range(n) if e>>i&1]
        adj[u[0]].add(u[1]);adj[u[1]].add(u[0])
    seen={0};stack=[0]
    while stack:
        for w in adj[stack.pop()]:
            if w not in seen:seen.add(w);stack.append(w)
    assert len(seen)==n,(profile,'disconnected',seen)
    betti=len(E)-n+1
    L=len(parents)
    occupied=[i for i,a in enumerate(profile) if a]
    gaps=[occupied[k+1]-occupied[k]-1 for k in range(len(occupied)-1)]
    expected=L+2*m-3+sum(g*(g+1)//2 for g in gaps)
    assert betti==expected,(profile,'wrong formula',betti,expected)
    if verbose: print('PASS',profile, 'faces',initial, 'pairs',toggles,'vertices',len(V),'edges',len(E),'circle rank',betti)
    return initial,toggles,betti

def main():
    count=0;total_faces=0;total_pairs=0;max_faces=0
    for m in range(1,8):
        for t in product(range(3),repeat=m):
            if m==1:
                if t[0]<2:continue
            elif t[0]<1 or t[-1]<1:continue
            if sum(t)+m>12:continue
            F,P,r=collapse(t)
            count+=1;total_faces+=F;total_pairs+=P;max_faces=max(max_faces,F)
    for p in ((1,)*9,(2,1,2,1,2),(1,0,0,0,1),(1,1,1,1,1,1,1,1),(3,0,0,2)):
        if len(p)+sum(p)>18:continue
        F,P,r=collapse(p,True)
        count+=1;total_faces+=F;total_pairs+=P;max_faces=max(max_faces,F)
    print('RESULT:',count,'profiles;',total_faces,'initial faces;',total_pairs,'checked collapses; max complex',max_faces,'faces')
if __name__=='__main__':main()
