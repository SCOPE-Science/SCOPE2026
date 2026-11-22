"""Exact exhaustive certificate: minimally ergodic cycle updates in 4x4 square ice.
Standard Python 3 only; no external data or network access.
"""
from itertools import product, combinations
from collections import Counter

L=4
H=lambda i,j:1<<(4*(i%4)+(j%4))
V=lambda i,j:1<<(16+4*(i%4)+(j%4))
faces=[H(i,j)|V(i,j+1)|H(i+1,j)|V(i,j) for i in range(4) for j in range(4)]
hrows=[sum(H(i,j) for j in range(4)) for i in range(4)]
vcols=[sum(V(i,j) for i in range(4)) for j in range(4)]

# Generate each of the 16 horizontal edges freely and solve the four independent
# vertical-column recurrences from the exact 2-in/2-out equations.
states=set()
for hs in range(1<<16):
    columns=[]
    for j in range(4):
        opts=[]
        for start in (0,1):
            z=start;bits=0
            for i in range(4):
                z+=bool(hs&H(i,j-1))-bool(hs&H(i,j))
                if z not in (0,1):break
                if z:bits|=V(i,j)
            else:
                if z==start:opts.append(bits)
        columns.append(opts)
    if all(columns):
        for cs in product(*columns):states.add(hs|cs[0]|cs[1]|cs[2]|cs[3])
assert len(states)==2970,len(states)

# The checker independently asserts every local vertex constraint.
def is_ice(s):
    return all(int(bool(s&H(i,j)))+int(bool(s&V(i,j))) ==
               int(bool(s&H(i,j-1)))+int(bool(s&V(i-1,j)))
               for i in range(4) for j in range(4))
assert all(is_ice(s) for s in states)

st=sorted(states); pos={s:i for i,s in enumerate(st)}
moves=faces+hrows+vcols
links=[]
for move in moves:
    ed=[]
    for s in st:
        t=s^move
        if t in pos and s<t:ed.append((pos[s],pos[t]))
    links.append(ed)
assert len(links)==24
assert sum(len(e) for e in links[:16])==8768

def ncomponents(sel):
    parent=list(range(len(st)));size=[1]*len(st);count=len(st)
    def find(a):
        while parent[a]!=a:
            parent[a]=parent[parent[a]];a=parent[a]
        return a
    for k in sel:
        for a,b in links[k]:
            x=find(a);y=find(b)
            if x!=y:
                if size[x]<size[y]:x,y=y,x
                parent[y]=x;size[x]+=size[y];count-=1
    return count

base=list(range(16))
assert ncomponents(base)==69
assert all(ncomponents(base+[k])==19 for k in range(16,24))
assert all(ncomponents(base+[i,j])==11 for i,j in combinations(range(16,20),2))
assert all(ncomponents(base+[i,j])==11 for i,j in combinations(range(20,24),2))
assert all(ncomponents(base+[i,j])==1 for i in range(16,20) for j in range(20,24))
# No more than two selected loops are needed: supersets of an ergodic update
# set remain ergodic, whereas lack of either winding direction preserves flux.
counts=Counter()
for mask in range(256):
    sel=base+[16+i for i in range(8) if (mask>>i)&1]
    result=ncomponents(sel)
    horizontal=(mask&15).bit_count()
    vertical=((mask>>4)&15).bit_count()
    counts[result]+=1
    assert (result==1)==(horizontal>0 and vertical>0)
assert counts[1]==225 and sum(counts.values())==256,counts
assert ncomponents(list(range(24)))==1
print('PASS: 2970 ice states; 16 facial cycles, 4 horizontal and 4 vertical winding cycles')
print('PASS: 8768 original face-flip edges; 69 components under facial flips alone')
print('PASS: 19 with exactly one winding cycle; 11 with two parallel cycles; 1 with transverse pair')
print('PASS: all 256 subsets checked; 225 ergodic and 31 nonergodic')
print('PASS: minimum two extra cycles, one of each winding direction, with 16 minimizers')
