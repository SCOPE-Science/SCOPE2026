"""Self-contained exact finite certificate for Pappus independence homology symmetry.
Requires only Python 3 standard library. Usage: python verify_integral.py.
"""
import itertools
import collections
import math

N=18
lcf=(5,7,-7,7,-7,-5)*3
edges=set()
for v,s in enumerate(lcf):
    edges.add(tuple(sorted((v,(v+1)%N))))
    edges.add(tuple(sorted((v,(v+s)%N))))
assert len(edges)==27
nb=[0]*N
for a,b in edges:
    nb[a]|=1<<b;nb[b]|=1<<a
assert all(x.bit_count()==3 for x in nb)
faces=[]
def enum_faces(mask,eligible):
    if mask:faces.append(mask)
    while eligible:
        bit=eligible&-eligible;eligible-=bit
        v=bit.bit_length()-1
        enum_faces(mask|bit,eligible&~nb[v])
enum_faces(0,(1<<N)-1)
F=set(faces)
assert len(faces)==len(F)==2597
counts=collections.Counter(x.bit_count() for x in F)
assert [counts[k] for k in range(1,10)]==[18,126,438,801,756,348,90,18,2]
# Pivot toggles produce an acyclic face matching. Check directed Hasse acyclicity in full.
unpaired=set(F);match=[]
for v in range(N):
    bit=1<<v
    for f in sorted(unpaired,key=lambda f:(f.bit_count(),f)):
        if f not in unpaired or f&bit:continue
        up=f|bit
        if up in unpaired:
            unpaired.remove(f);unpaired.remove(up)
            match.append((f,up))
crit=collections.Counter(f.bit_count()-1 for f in unpaired)
assert crit=={0:1,4:11,5:1},crit
matched=set(match)
indeg={x:0 for x in F};adj={x:[] for x in F}
for upper in F:
    for k in range(N):
        bit=1<<k
        if not upper&bit:continue
        low=upper^bit
        if low not in F:continue
        u,v=(low,upper) if (low,upper) in matched else (upper,low)
        adj[u].append(v);indeg[v]+=1
queue=collections.deque(f for f in F if indeg[f]==0);seen=0
while queue:
    s=queue.popleft();seen+=1
    for t in adj[s]:
        indeg[t]-=1
        if indeg[t]==0:queue.append(t)
assert seen==len(F),('directed Morse cycle',seen)

def vertices(f):
    return [v for v in range(N) if f>>v&1]
def boundary(f):
    return [(f^(1<<v),-1 if j%2 else 1) for j,v in enumerate(vertices(f))]

# Exact integral cellular Morse d5, via algebraic cancellation of matched 4/5 pairs.
matched4to5={lo:up for lo,up in match if lo.bit_count()==5}
critical5=[f for f in unpaired if f.bit_count()==6]
critical4=[f for f in unpaired if f.bit_count()==5]
assert len(critical5)==1 and len(critical4)==11
coef=collections.Counter()
for low,sign in boundary(critical5[0]):coef[low]+=sign
iterations=0
while any(c and k in matched4to5 for k,c in coef.items()):
    low=min(k for k,c in coef.items() if c and k in matched4to5)
    up=matched4to5[low]
    bdy=dict(boundary(up)); sgn=bdy[low];assert abs(sgn)==1
    scale=coef[low]*sgn
    for x,coeff in bdy.items():coef[x]-=scale*coeff
    assert coef[low]==0
    iterations+=1
    assert iterations<5000
assert all(k in critical4 or k in {hi for lo,hi in match if hi.bit_count()==5} for k,c in coef.items() if c)
morsevec=tuple(coef[x] for x in sorted(critical4))
assert math.gcd(*morsevec)==1,(morsevec, 'not primitive')
# A primitive nonzero boundary gives reduced integral homology Z^10 in degree 4.

# Enumerate all graph automorphisms using adjacency-preserving partial injections.
perms=[]
def automorphisms(assignment,unused):
    if len(assignment)==N:
        perms.append(tuple(assignment[i] for i in range(N)))
        return
    # Pick the next vertex with the tightest adjacency-constrained image domain.
    options=[]
    for v in range(N):
        if v in assignment:continue
        dom=[w for w in unused if all(bool(nb[v]>>u&1)==bool(nb[w]>>assignment[u]&1) for u in assignment)]
        if not dom:return
        options.append((len(dom),-sum(bool(nb[v]>>u&1) for u in assignment),v,dom))
    _,_,v,dom=min(options)
    for w in dom:
        assignment[v]=w
        automorphisms(assignment,unused-{w})
        del assignment[v]
automorphisms({},set(range(N)))
assert len(perms)==216
assert len(set(perms))==216

def chain_trace(p):
    total=-1 # augmented empty-face term
    for face in F:
        verts=vertices(face)
        images=[p[v] for v in verts]
        if sorted(images)!=verts:continue
        inversions=sum(images[i]>images[j] for i in range(len(images)) for j in range(i+1,len(images)))
        total+=(-1)**(len(verts)-1+inversions)
    return total
traces={p:chain_trace(p) for p in perms}
assert traces[tuple(range(N))]==10
assert sum(traces.values())==0
assert sum(t*t for t in traces.values())==432 # 216*2 => exactly two irreducibles, multiplicity one

def compose(p,q):return tuple(p[q[i]] for i in range(N))
def inverse(p):
    inv=[0]*N
    for i,v in enumerate(p):inv[v]=i
    return tuple(inv)
def cycles(p):
    out=[]; seen=set()
    for v in range(N):
        if v in seen:continue
        orb=[];x=v
        while x not in seen:
            orb.append(x);seen.add(x);x=p[x]
        if len(orb)>1:out.append(tuple(orb))
    return out
classes=[];todo=set(perms)
while todo:
    rep=min(todo)
    cls={compose(compose(h,rep),inverse(h)) for h in perms}
    assert cls<=todo
    assert len({traces[p] for p in cls})==1
    todo-=cls;classes.append((rep,cls))
classes.sort(key=lambda item:(-len(item[1]),item[0]))
assert len(classes)==13

print('PAPPUS_FULL_HOMOLOGY_CHARACTER_PASS')
print('graph: vertices=18 edges=27; graph automorphisms=216; independence faces=2597')
print('face distribution by cardinality',*[counts[k] for k in range(1,10)])
print('acyclic face matching:',len(match),'pairs; critical dimension counts',dict(sorted(crit.items())))
print('integral Morse d5:',morsevec,'gcd',math.gcd(*morsevec),'steps',iterations)
print('reduced integral homology: Z^10 in degree 4, zero otherwise')
print('character: class count=13; invariant rank=0; character norm=2; two distinct constituents')
print('class table: size | representative disjoint nontrivial cycles | trace')
for rep,cls in classes:
    print(len(cls),'|',cycles(rep),'|',traces[rep])
print('sum of character values:',sum(traces.values()),'sum of squared values:',sum(x*x for x in traces.values()))
