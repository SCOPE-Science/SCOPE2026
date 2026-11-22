"""Independent exhaustive checker using the even-to-odd edge representation of Q4.
The Gray-coded four-cycle coordinate system identifies Q4 with C4 x C4.
Requires only Python 3 standard library and no external input.
"""
from itertools import combinations,product
from collections import Counter
V=range(16)
ev=[x for x in V if x.bit_count()%2==0]
od=[x for x in V if x.bit_count()%2==1]
edges=[];eid={};byeven={}
for e in ev:
    byeven[e]=[]
    for a in range(4):
        o=e^(1<<a)
        eid[e,o]=len(edges);byeven[e].append(len(edges));edges.append((e,o))
byodd={o:[eid[o^(1<<a),o] for a in range(4)] for o in od}
choices=[[sum(1<<z for z in c) for c in combinations(byeven[e],2)] for e in ev]
states=set()
for parts in product(*choices):
    s=0
    for p in parts:s|=p
    if all(sum((s>>z)&1 for z in byodd[o])==2 for o in od):states.add(s)
assert len(states)==2970, len(states)
# Gray cycle 00,01,11,10 in each independent pair of coordinates.
gray=(0,1,3,2)
gv=lambda i,j:gray[i%4]|(gray[j%4]<<2)
H=lambda i,j:1<<(4*(i%4)+(j%4))
VV=lambda i,j:1<<(16+4*(i%4)+(j%4))
def arrow(s,a,b):
    e,o=(a,b) if a.bit_count()%2==0 else (b,a)
    return bool((s>>eid[e,o])&1) == (a==e)
translated=[]
for s in states:
    t=0
    for i in range(4):
        for j in range(4):
            if arrow(s,gv(i,j),gv(i,(j+1)%4)):t|=H(i,j)
            if arrow(s,gv(i,j),gv((i+1)%4,j)):t|=VV(i,j)
    translated.append(t)
assert len(set(translated))==2970
assert all(all(int(bool(t&H(i,j)))+int(bool(t&VV(i,j)))==int(bool(t&H(i,j-1)))+int(bool(t&VV(i-1,j))) for i in range(4) for j in range(4)) for t in translated)
# Every square of the cube corresponds either to one face or to a winding loop.
squares=[]
for x in V:
    for a,b in combinations(range(4),2):
        corners={x,x^(1<<a),x^(1<<b),x^(1<<a)^(1<<b)}
        if x==min(corners):
            square=sum(1<<i for i,(e,o) in enumerate(edges) if e in corners and o in corners)
            assert square.bit_count()==4
            squares.append((square,{a,b}))
assert len(squares)==24
# 16 local squares have one coordinate from {0,1} and one from {2,3}.
face=[s for s,c in squares if len(c&{0,1})==1]
extra=[s for s,c in squares if len(c&{0,1})!=1]
assert (len(face),len(extra))==(16,8)
index={s:i for i,s in enumerate(states)}
links={m:[(index[s],index[s^m]) for s in states if s^m in index] for m,c in squares}
def components(cycles):
    par=list(range(len(states)));size=[1]*len(states);n=len(states)
    def root(x):
        while x!=par[x]:par[x]=par[par[x]];x=par[x]
        return x
    for mask in cycles:
        for i,j in links[mask]:
            a,b=root(i),root(j)
            if a!=b:
                if size[a]<size[b]:a,b=b,a
                par[b]=a;size[a]+=size[b];n-=1
    return n
assert components(face)==69
assert all(components(face+[c])==19 for c in extra)
for i,j in combinations(range(8),2):
    is_x=lambda k: next(cs for mask,cs in squares if mask==extra[k])=={0,1}
    assert components(face+[extra[i],extra[j]])==(11 if is_x(i)==is_x(j) else 1)
connect=0
for bits in range(256):
    sub=face+[extra[i] for i in range(8) if bits>>i&1]
    is_x=lambda k: next(cs for mask,cs in squares if mask==extra[k])=={0,1}
    both=any((bits>>i)&1 and is_x(i) for i in range(8)) and any((bits>>j)&1 and not is_x(j) for j in range(8))
    assert (components(sub)==1)==both
    connect+=both
assert connect==225
print('PASS independent Q4 even-to-odd generator 2970, 24 squares, 16 faces and 8 loops')
print('PASS independent full 256 subsets, sharp two transverse loops, 225 connected update sets')
