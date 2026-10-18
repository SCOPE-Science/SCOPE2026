#!/usr/bin/env python3
from collections import deque, Counter

N=20
# Canonical labels: 0..9 = u_0..u_9, 10..19 = v_0..v_9.
adj=[set() for _ in range(N)]
def add(a,b):
    adj[a].add(b); adj[b].add(a)
for i in range(10):
    add(i,(i+1)%10)
    add(i,10+i)
    add(10+i,10+((i+3)%10))

assert sum(map(len,adj))//2 == 30
assert all(len(a)==3 for a in adj)

# All-pairs shortest-path distances.
dist=[[99]*N for _ in range(N)]
for s in range(N):
    dist[s][s]=0
    q=deque([s])
    while q:
        x=q.popleft()
        for y in adj[x]:
            if dist[s][y]==99:
                dist[s][y]=dist[s][x]+1
                q.append(y)
assert max(max(row) for row in dist)==5

def rips_adjacency(r):
    bits=[0]*N
    for i in range(N):
        for j in range(i+1,N):
            if dist[i][j] <= r:
                bits[i] |= 1<<j
                bits[j] |= 1<<i
    return bits

def all_cliques(bits):
    faces=[]
    def rec(cand, chosen):
        while cand:
            b=cand & -cand
            cand ^= b
            v=b.bit_length()-1
            new=chosen|b
            faces.append(new)
            rec(cand & bits[v], new)
    rec((1<<N)-1,0)
    return faces

def fvector(faces):
    c=Counter(m.bit_count()-1 for m in faces)
    return tuple(c[i] for i in range(max(c)+1))

ORDER=[0,1,10,13,2,11,14,3,12,15,4,16,5,17,6,18,7,19,8,9]

def staged_matching(faces):
    un=set(faces)
    pairs=[]
    for v in ORDER:
        bit=1<<v
        for m in sorted(tuple(un)):
            if m & bit:
                continue
            up=m|bit
            if up in un:
                un.remove(m); un.remove(up)
                pairs.append((m,up))
    return pairs,un

def verify_acyclic(faces,pairs):
    faceset=set(faces)
    matched=set(pairs)
    indeg={m:0 for m in faces}
    out={m:[] for m in faces}
    covers=0
    for up in faces:
        if up.bit_count()<2:
            continue
        x=up
        while x:
            b=x & -x; x^=b
            lo=up^b
            if lo and lo in faceset:
                covers+=1
                if (lo,up) in matched:
                    a,c=lo,up
                else:
                    a,c=up,lo
                out[a].append(c); indeg[c]+=1
    q=deque(m for m in faces if indeg[m]==0)
    seen=0
    while q:
        a=q.popleft(); seen+=1
        for b in out[a]:
            indeg[b]-=1
            if indeg[b]==0:q.append(b)
    assert seen==len(faces)
    return covers

# Scale 1: the graph itself, since the Desargues graph has girth 6.
triangles=0
for a in range(N):
    for b in adj[a]:
        if b>a:
            triangles += len(adj[a] & adj[b])
assert triangles==0
assert all(dist[0][v] < 99 for v in range(N))
assert 30-20+1==11

# Scale 2: exact face enumeration and complete Morse certificate.
f2=all_cliques(rips_adjacency(2))
assert len(f2)==260
assert fvector(f2)==(20,90,120,30)
assert 20-90+120-30 == 20
p2,c2=staged_matching(f2)
assert len(p2)==120
assert Counter(m.bit_count()-1 for m in c2)==Counter({2:19,0:1})
covers2=verify_acyclic(f2,p2)
assert covers2==660

# Scale 3: exact face enumeration and complete Morse certificate.
f3=all_cliques(rips_adjacency(3))
assert len(f3)==3200
assert fvector(f3)==(20,150,540,1000,960,450,80)
assert 20-150+540-1000+960-450+80 == 0
p3,c3=staged_matching(f3)
assert len(p3)==1599
assert Counter(m.bit_count()-1 for m in c3)==Counter({0:1,3:1})
covers3=verify_acyclic(f3,p3)
assert covers3==13980

# Scale 4: every vertex has a unique distance-5 antipode. Therefore the
# only forbidden pairs are ten disjoint antipodal pairs and the complex is
# the boundary of the 10-dimensional cross-polytope, hence S^9.
pairs5=[]
for i in range(N):
    for j in range(i+1,N):
        if dist[i][j]==5:
            pairs5.append((i,j))
assert len(pairs5)==10
assert all(sum(v in e for e in pairs5)==1 for v in range(N))
expected={(i,(i+5)%10) if i<(i+5)%10 else ((i+5)%10,i) for i in range(10)}
expected |= {(10+i,10+((i+5)%10)) if i<(i+5)%10 else (10+((i+5)%10),10+i) for i in range(10)}
assert set(pairs5)==expected

print('DESARGUES_RIPS_VERIFY_OK')
print('diameter=5')
print('scale1_beta1=11')
print('scale2_fvector=(20,90,120,30) pairs=120 critical=(c0=1,c2=19) covers=%d' % covers2)
print('scale3_fvector=(20,150,540,1000,960,450,80) pairs=1599 critical=(c0=1,c3=1) covers=%d' % covers3)
print('scale4_antipodal_pairs=10 sphere_dimension=9')
