#!/usr/bin/env python3
"""Self-contained exact finite certificate for the Herschel matching complex.

Run: python3 herschel_matching_verify.py
Only the Python standard library is required.
"""
from collections import Counter, deque
from itertools import permutations, combinations

# Three degree-four vertices (0,1,2); two degree-three poles (3,4);
# two intermediate vertices for each of the pairs (0,1),(0,2),(1,2).
PAIRS = ((0,1),(0,2),(1,2))
edge_list=[]
for k,(a,b) in enumerate(PAIRS):
    for t in (0,1):
        w=5+2*k+t
        edge_list.extend([(a,w),(b,w),(3+t,w)])
E=tuple(sorted(tuple(sorted(e)) for e in edge_list))
assert len(E)==18 and len(set(E))==18
N=18
# Confirm the combinatorial identification of the Herschel graph.
deg=Counter(v for e in E for v in e)
assert tuple(sorted(deg.values(),reverse=True))==(4,4,4)+(3,)*8
assert all((a<5)!=(b<5) for a,b in E)
adj={v:set() for v in range(11)}
for a,b in E: adj[a].add(b);adj[b].add(a)
for removed_size in (0,1,2):
    for removed in combinations(range(11),removed_size):
        rem=set(removed)
        active=set(range(11))-rem
        reach={min(active)}
        frontier=list(reach)
        while frontier:
            x=frontier.pop()
            for y in adj[x]-rem-reach:
                reach.add(y);frontier.append(y)
        assert reach==active,(removed,reach)
ENDS = tuple((1<<a)|(1<<b) for a,b in E)
# Two genuinely different face enumerators.
faces=[0]
for e in range(N):
    inc=ENDS[e]
    new=[x | (1<<e) for x in faces
         if all(not (inc&ENDS[j]) for j in range(e) if x&(1<<j))]
    faces += new
F=set(faces)
B=set()
for mask in range(1<<N):
    used=0
    for i in range(N):
        if mask & (1<<i):
            if used & ENDS[i]: break
            used |= ENDS[i]
    else:B.add(mask)
assert F==B
F.remove(0)
VECTOR=Counter(x.bit_count()-1 for x in F)
assert VECTOR=={0:18,1:111,2:280,3:270,4:72},VECTOR
assert len(F)==751
assert sum((-1)**d*num for d,num in VECTOR.items())==-11

# Deterministic staged coordinate toggling of valid simplices.
# The partition is certified acyclic below; no generic claim that
# arbitrary staged toggling must be acyclic is needed.
ORDER=(6,17,8,0,9,16,10,11,14,12,1,4,15,5,13,7,3,2)
remaining=set(F)
matched={}
for i in ORDER:
    bit=1<<i
    chosen=[lo for lo in remaining if not(lo&bit) and (lo|bit) in remaining]
    for lo in chosen:
        hi=lo|bit
        assert lo in remaining and hi in remaining
        remaining.remove(lo);remaining.remove(hi)
        matched[lo]=hi
assert len(matched)==369
critical=Counter(x.bit_count()-1 for x in remaining)
assert critical=={0:1,3:12}, critical

# Orient every nonempty face-poset cover downward, reversing matched covers.
# This checks the precise acyclicity hypothesis of Forman's theorem.
pairset=set(matched.items())
indeg={x:0 for x in F}
out={x:[] for x in F}
incidences=0
for upper in F:
    for i in range(N):
        if upper&(1<<i):
            lower=upper^(1<<i)
            if not lower: continue
            incidences+=1
            if (lower,upper) in pairset: src,dst=lower,upper
            else: src,dst=upper,lower
            out[src].append(dst)
            indeg[dst]+=1
q=deque(x for x in F if indeg[x]==0)
visited=0
while q:
    v=q.popleft();visited+=1
    for w in out[v]:
        indeg[w]-=1
        if indeg[w]==0:q.append(w)
assert visited==751,(visited,len(F))
assert incidences==2502,incidences

# Independently compute simplicial boundaries over several finite fields.
by_dim={d:sorted(x for x in F if x.bit_count()-1==d)
        for d in range(5)}
def finite_field_rank(d,p):
    idx={x:j for j,x in enumerate(by_dim[d-1])}
    basis={}
    for top in by_dim[d]:
        v={}
        for k,i in enumerate(i for i in range(N) if top&(1<<i)):
            row=idx[top^(1<<i)]
            v[row] = (1 if k%2==0 else -1)%p
        while v:
            pivot=max(v)
            if pivot not in basis:
                c=pow(v[pivot],-1,p)
                basis[pivot]={j:(a*c)%p for j,a in v.items()}
                break
            u=basis[pivot]
            c=v[pivot]
            for j,a in u.items():
                b=(v.get(j,0)-c*a)%p
                if b:v[j]=b
                else:v.pop(j,None)
    return len(basis)
for prime in (2,3,5,101):
    ranks=tuple(finite_field_rank(d,prime) for d in range(1,5))
    assert ranks==(17,94,186,72),(prime,ranks)

# Graph automorphisms: the three degree-four vertices are freely permuted;
# independently swap the two degree-three poles, which also swaps the
# two common-neighbor vertices within each pair. These give 6*2 automorphisms.
def sign(seq):
    return (-1)**sum(seq[i]>seq[j] for i in range(len(seq))
                     for j in range(i+1,len(seq)))

def kind_s3(p):
    if p==(0,1,2):return 0       # identity
    if sign(p)==-1:return 1      # transposition
    return 2                    # 3-cycle

class_character={}
for p in permutations((0,1,2)):
    for swap in (0,1):
        vm={i:p[i] for i in range(3)}
        vm.update({3:3+swap,4:4-swap})
        for k,(a,b) in enumerate(PAIRS):
            k2=PAIRS.index(tuple(sorted((p[a],p[b]))))
            for t in (0,1):
                vm[5+2*k+t]=5+2*k2+(t^swap)
        assert len(set(vm.values()))==11
        edge_perm=[E.index(tuple(sorted((vm[a],vm[b])))) for a,b in E]
        assert len(set(edge_perm))==18
        # The reduced Lefschetz number includes the augmented empty face (-1).
        alt=-1
        for face in F:
            chosen=[i for i in range(N) if face&(1<<i)]
            mapped=[edge_perm[i] for i in chosen]
            if set(chosen)==set(mapped):
                alt += (-1)**(len(chosen)-1)*sign(mapped)
        # The only reduced homology is in degree 3, so trace = -Lefschetz.
        ch=-alt
        # Independent orbit-subset Lefschetz identity: each invariant
        # matching is a union of admissible edge orbits. Its signed
        # contribution depends only on the number of selected orbits.
        cycles=[]
        unseen=set(range(N))
        while unseen:
            start=min(unseen)
            orb=[];v=start
            while v in unseen:
                unseen.remove(v);orb.append(v);v=edge_perm[v]
            assert v==start
            cycles.append(orb)
        admissible=[]
        for orbit in cycles:
            used=0
            for i in orbit:
                if used&ENDS[i]:break
                used|=ENDS[i]
            else:admissible.append(used)
        alt_orbit=0
        for subset in range(1<<len(admissible)):
            union=0
            for j,endpoints in enumerate(admissible):
                if subset&(1<<j):
                    if union&endpoints:break
                    union|=endpoints
            else:alt_orbit+=(-1)**subset.bit_count()
        assert ch==alt_orbit,(p,swap,ch,alt_orbit)
        k=kind_s3(p)
        assert (k,swap) not in class_character or class_character[k,swap]==ch
        class_character[k,swap]=ch
assert class_character=={(0,0):12,(0,1):-2,(1,0):0,(1,1):2,(2,0):-3,(2,1):1},class_character

s3_sizes=(1,3,2)
s3_irr={'trivial':(1,1,1),'sign':(1,-1,1),'standard':(2,0,-1)}
multiplicities={}
for name,ch in s3_irr.items():
    for central in (1,-1):
        numerator=sum(s3_sizes[k]*class_character[k,swap]*ch[k]
                      *(central if swap else 1)
                      for k in range(3) for swap in (0,1))
        assert numerator%12==0,numerator
        multiplicities[name,central]=numerator//12
assert multiplicities=={
    ('trivial',1):1, ('trivial',-1):0,
    ('sign',1):0, ('sign',-1):1,
    ('standard',1):2, ('standard',-1):3,
},multiplicities
print('GRAPH vertices=11 edges=18 degree_sequence=(4,4,4,3,3,3,3,3,3,3,3)')
print('F_VECTOR 18 111 280 270 72')
print('NONEMPTY_FACES 751 EULER -11')
print('MORSE_PAIRS',len(matched),'CRITICAL',dict(sorted(critical.items())))
print('ACYCLIC_POSET_NODES',visited,'COVER_RELATIONS',incidences)
print('BOUNDARY_RANKS_OVER_2_3_5_101 17 94 186 72')
print('S3xC2_CLASS_TRACES',dict(sorted(class_character.items())))
print('S3xC2_MULTIPLICITIES',dict(sorted(multiplicities.items())))
print('HERSCHEL_MATCHING_INTEGRAL_WEDGE_AND_CHARACTER_PASS')
