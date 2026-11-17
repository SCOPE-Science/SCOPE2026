#!/usr/bin/env python3
"""Finite certificate for the Desargues-graph dominance complex.
Python 3, standard library only; no precomputed data or external dependencies.
"""
from collections import Counter,deque
from array import array
from itertools import combinations
import hashlib, json, time

N=20; n=10; full=(1<<N)-1
adj=[0]*N

def edge(a,b):
    assert a!=b
    adj[a]|=1<<b;adj[b]|=1<<a
for j in range(n):
    edge(j,(j+1)%n)
    edge(j,j+n)
    edge(j+n,n+(j+3)%n)
assert sum(x.bit_count() for x in adj)==60 and all(x.bit_count()==3 for x in adj)
closed=[a | (1<<i) for i,a in enumerate(adj)]

def valid_direct(mask):
    return all((mask&cl)!=cl for cl in closed)

# A separate monotonic dynamic-programming enumeration of every face
ok=bytearray(1<<N); ok[0]=1
faces=[0]
for mask in range(1,1<<N):
    p=mask^(mask&-mask)
    if ok[p] and valid_direct(mask):
        ok[mask]=1; faces.append(mask)
assert len(faces)==434221
def valid_complement(mask):
    remaining=full^mask
    dominated=remaining
    rest=remaining
    while rest:
        bit=rest&-rest;rest-=bit
        dominated |= adj[bit.bit_length()-1]
    return dominated==full
assert all(bool(ok[i])==valid_complement(i) for i in range(1<<N))
face_vector=Counter(mask.bit_count()-1 for mask in faces if mask)
assert dict(sorted(face_vector.items()))=={0:20,1:190,2:1140,3:4825,4:15184,5:36390,6:66800,7:93120,8:96400,9:71356,10:35680,11:11105,12:1880,13:130}

# Facets have genuinely different dimensions, a useful structural check.
facet_dims=Counter()
for f in faces[1:]:
    if all(f&(1<<j) or not ok[f|(1<<j)] for j in range(N)):
        facet_dims[f.bit_count()-1]+=1
assert facet_dims=={9:14,11:205,12:180,13:130}, facet_dims

# Two distinct valid vertex orders give independent Morse matching checks.

def morse(vertex_order, *, full_check=False):
    alive=ok[:]
    mate=array('i',[-1])*(1<<N)
    stage=[]
    # Includes empty face, so delete the empty--{first vertex} pair
    # afterwards to obtain a standard matching with critical vertex.
    for v in vertex_order:
        bit=1<<v;matched=0
        for x in faces:
            if alive[x] and not(x&bit) and alive[x|bit]:
                alive[x]=0;alive[x|bit]=0
                mate[x]=x|bit;mate[x|bit]=x
                matched+=1
        stage.append(matched)
    # Turn the unique empty-face pair into an unmatched critical vertex.
    vertex=mate[0]
    assert vertex!=-1 and vertex.bit_count()==1
    mate[0]=mate[vertex]=-1
    critical=[x for x in faces if mate[x]<0 and x]
    critical_dims=Counter(x.bit_count()-1 for x in critical)
    assert critical_dims=={0:1,9:13}, critical_dims
    assert vertex in critical
    pair_count=(len(faces)-1-len(critical))//2
    assert pair_count==217103, pair_count
    if full_check:
        # All faces including empty participate in the augmented Hasse graph.
        # Unmatched codimension-one arrows descend; matched arrows ascend.
        indeg=array('I',[0])*(1<<N)
        incidences=0
        for upper in faces[1:]:
            bits=upper
            while bits:
                bit=bits&-bits;bits-=bit
                lower=upper^bit
                if mate[upper]==lower:
                    indeg[upper]+=1
                else:
                    indeg[lower]+=1
                incidences+=1
        # Standard matching has no edge to empty, which is a sink.
        queue=deque(x for x in faces if indeg[x]==0)
        visited=0
        while queue:
            x=queue.popleft();visited+=1
            y=mate[x]
            if y>x:  # matched ascent
                indeg[y]-=1
                if indeg[y]==0:queue.append(y)
            bits=x
            while bits:
                bit=bits&-bits;bits-=bit
                lower=x^bit
                if lower==y:continue
                indeg[lower]-=1
                if indeg[lower]==0:queue.append(lower)
        assert visited==len(faces), (visited,len(faces))
    else:incidences=None;visited=None
    return {'critical_cells':dict(sorted(critical_dims.items())),'pair_count':pair_count,
            'stage_pairs':stage,'directed_incidence_count':incidences,'acyclic_nodes_checked':visited,
            'critical_masks_hex':[hex(x) for x in critical if x!=vertex]}

match_a=morse(tuple(range(N)),full_check=True)
match_b=morse(tuple(range(N-1,-1,-1)),full_check=True)
# graph is bipartite and matching pairs vertex i with n+i, so min vertex cover n
parity=[i%2 for i in range(n)] + [1-(i%2) for i in range(n)]
assert all(parity[i]!=parity[j] for i in range(N) for j in range(N) if adj[i]>>j&1)
assert all(adj[i]>> (n+i)&1 for i in range(n))

# Rotation character of H_9 via exact reduced Lefschetz counting.
def character_rotate(t):
    perm=list(range(N))
    for i in range(n):
        perm[i]=(i+t)%n
        perm[n+i]=n+(i+t)%n
    assert all(sum(1<<perm[j] for j in range(N) if adj[i]>>j&1)==adj[perm[i]] for i in range(N))
    unseen=set(range(N));cycles=[]
    while unseen:
        i=min(unseen);cycle=[];j=i
        while j in unseen:
            cycle.append(j); unseen.remove(j);j=perm[j]
        cycles.append(sum(1<<a for a in cycle))
    trace=0
    for cm in range(1<<len(cycles)):
        m=0
        for j,bitset in enumerate(cycles):
            if cm>>j&1:m|=bitset
        if ok[m]:trace+=(-1)**cm.bit_count()
    return trace
character=[character_rotate(i) for i in range(n)]
assert character[0]==13
# Character dimension of cyclic invariants always integer.
assert character==[13,-1,3,-1,3,-11,3,-1,3,-1]
assert sum(character)%10==0

# Independent signed fixed-simplex formula on the original simplicial chains.
# In degree 9, reduced Lefschetz gives Tr(H9) = sum (-1)^|F| sign(rotation|F).
# This is intentionally different from the cycle-union enumeration above.
def rotate_mask(m,t):
    a=m&1023;b=m>>10
    if t:
        a=((a<<t)|(a>>(10-t)))&1023
        b=((b<<t)|(b>>(10-t)))&1023
    return a|(b<<10)

def signed_simplex_trace(t):
    s=0;fixed=0
    for m in faces:
        if rotate_mask(m,t)!=m:continue
        fixed+=1
        seq=[(j//10)*10+(j%10+t)%10 for j in range(N) if m>>j&1]
        inversions=sum(seq[i]>seq[j] for i in range(len(seq)) for j in range(i+1,len(seq)))
        s+=(-1)**(m.bit_count()+inversions)
    return s,fixed
signed_checks=[signed_simplex_trace(t) for t in range(10)]
assert [a for a,b in signed_checks]==character
# Four rational irreducibles of C10: trivial, sign, Q(zeta_5), Q(zeta_10).
# The computed character equals 1*trivial+4*sign+2*Q(zeta_10).
assert character==[1+4*(-1)**t+2*({0:4,5:-4}.get(t, (-1 if t%2==0 else 1))) for t in range(10)]
out={'graph':'generalized Petersen G(10,3) / Desargues','vertices':N,'edges':30,'closed_neighbor_sizes':sorted(set(x.bit_count() for x in closed)),
     'total_subsets_checked':1<<N,'faces_including_empty':len(faces),
     'face_vector_dimension':dict(sorted(face_vector.items())),
     'facets_by_dimension':dict(sorted(facet_dims.items())),
     'first_morse_matching':match_a,'second_morse_matching':match_b,
     'vertex_cover_number':10,'rotation_h9_character':character,
     'rotation_fixed_h9_dimension':sum(character)//10,
     'independent_signed_chain_checks':signed_checks,
     'rational_rotation_representation':'1 trivial + 4 sign + 2 Q(zeta_10)',
     'inferred_homotopy':'wedge of 13 9-spheres (Forman acyclic matching theorem)'}
print(json.dumps(out,indent=2))
