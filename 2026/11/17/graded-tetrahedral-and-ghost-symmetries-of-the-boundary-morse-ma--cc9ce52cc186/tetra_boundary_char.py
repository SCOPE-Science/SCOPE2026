#!/usr/bin/env python3
"""Exact finite combinatorics for ordinary acyclic Hasse-matching complex of tetrahedron boundary.
External claim: all homology outside H3 and H4 vanishes, H3 rank21, H4 rank24 (Scoville, arXiv:2604.18172).
The program independently enumerates matchings and ranks the relevant differentials modulo two primes.
"""
import itertools, collections, json, sys
from functools import lru_cache
P=(1009,10007)
base=tuple(range(4))
# boundary of tetrahedron = all nonempty proper subsets of 4
vertices=tuple(range(1,15))
vi={s:i for i,s in enumerate(vertices)}
hedges=tuple((x,y) for x in vertices for y in vertices if y.bit_count()==x.bit_count()+1 and x&y==x)
eidx={xy:i for i,xy in enumerate(hedges)}
assert len(hedges)==24
# original Hasse graph orientation lower -> upper
arcs=list((vi[x],vi[y]) for x,y in hedges)
N=len(vertices)

def acyclic(matching):
    rev=set(matching)
    adj=[[] for _ in range(N)]; indeg=[0]*N
    for i,(a,b) in enumerate(arcs):
        if i in rev:a,b=b,a
        adj[a].append(b);indeg[b]+=1
    ready=[i for i,d in enumerate(indeg) if d==0];n=0
    while ready:
        a=ready.pop(); n+=1
        for b in adj[a]:
            indeg[b]-=1
            if not indeg[b]:ready.append(b)
    return n==N

def compatible(prefix, i,used):
    a,b=hedges[i]
    if (used>>vi[a])&1 or (used>>vi[b])&1: return False
    return True

faces=[ [()]]
state=[((),0, -1)]
while state:
    cur,used,last=state.pop()
    for i in range(last+1,24):
        if compatible(cur,i,used):
            nxt=cur+(i,)
            if acyclic(nxt):
                while len(faces)<len(nxt)+1:faces.append([])
                faces[len(nxt)].append(nxt)
                a,b=hedges[i]
                state.append((nxt,used|1<<vi[a]|1<<vi[b],i))
faces=[sorted(t) for t in faces]
print('F_VECTOR',tuple(len(t) for t in faces[1:]),flush=True)
assert tuple(len(t) for t in faces[1:]) == (24,216,896,1692,1248,256)
fi=[{f:i for i,f in enumerate(level)} for level in faces]

def rank_columns(cols,prime):
    piv={};rank=0
    for col0 in cols:
        c={r:(v%prime) for r,v in col0.items() if v%prime}
        while c:
            p=min(c)
            if p not in piv:
                v=c[p]; iv=pow(v,-1,prime)
                piv[p]={r:(x*iv)%prime for r,x in c.items() if x%prime}
                rank+=1
                break
            b=piv[p];coeff=c[p]
            for r,v in b.items():
                z=(c.get(r,0)-coeff*v)%prime
                if z:c[r]=z
                elif r in c:del c[r]
    return rank

def boundary_col(k,i):
    f=faces[k][i];return {fi[k-1][f[:j]+f[j+1:]]:(-1)**j for j in range(k)}

print('RANKS',flush=True)
for prime in P:
    r5=rank_columns((boundary_col(6,i) for i in range(len(faces[6]))),prime)
    r4=rank_columns((boundary_col(5,i) for i in range(len(faces[5]))),prime)
    print('PRIME',prime,'rank_d5',r5,'rank_d4',r4,'H4',len(faces[5])-r4-r5,flush=True)
    assert (r5,r4)==(256,968)

def perm_map(perm):
    def mapmask(x):return sum(1<<perm[j] for j in range(4) if (x>>j)&1)
    return tuple(eidx[(mapmask(x),mapmask(y))] for x,y in hedges)

def face_action(f,emap):
    mapped=tuple(emap[i] for i in f)
    sign=1
    for i in range(len(mapped)):
        for j in range(i+1,len(mapped)):
            if mapped[i]>mapped[j]:sign=-sign
    return tuple(sorted(mapped)),sign

def orbit_columns(k, emap):
    level=faces[k]
    unused=set(level)
    cols=[]
    npos=0;fixed_signed=0
    while unused:
        first=min(unused); x=first;sgn=1
        steps=[]
        while True:
            unused.remove(x)
            steps.append((x,sgn))
            y,sg=face_action(x,emap)
            sgn*=sg
            if y==first:break
            assert y in unused
            x=y
        if len(steps)==1: fixed_signed+=sgn
        if sgn==1:
            npos+=1
            if k>1:
                acc=collections.defaultdict(int)
                for f,s in steps:
                    for j in range(len(f)):
                        ff=f[:j]+f[j+1:]
                        acc[fi[k-1][ff]]+=s*((-1)**j)
                cols.append(dict(acc))
    return npos, fixed_signed, cols

results={}
for lab,per in [('id',(0,1,2,3)),('transposition',(1,0,2,3)),('double_transposition',(1,0,3,2)),('three_cycle',(1,2,0,3)),('four_cycle',(1,2,3,0))]:
    emap=perm_map(per)
    cs=[orbit_columns(k,emap) for k in range(1,7)]
    chi_tilde=-1+sum(((-1)**(k-1))*cs[k-1][1] for k in range(1,7))
    b4plus=cs[4][0];b5plus=cs[5][0]
    ranks=[rank_columns(cs[4][2],p) for p in P]
    d3_ranks=[rank_columns(cs[3][2],p) for p in P]
    assert len(set(d3_ranks))==1
    h3plus=cs[3][0]-d3_ranks[0]-ranks[0]
    assert len(set(ranks))==1
    h4plus=b4plus-ranks[0]-b5plus
    # By Scoville: homology only in H3,H4, H4 rank24, H3 rank21
    if lab=='id':h4char=24
    elif lab in ('transposition','double_transposition'):h4char=2*h4plus-24
    elif lab=='three_cycle':h4char=(3*h4plus-24)//2;assert (3*h4plus-24)%2==0
    else:
        # four-cycle: need the -1 eigenspace, may recover using g^2 and +1 for g and 4th eig dimensions
        # g^2 double-transposition: m1+mMinus=(24+chi(g^2))/2
        # chi(g)=2 m1-(24+chi(g^2))/2
        double_chi=results['double_transposition']['H4_trace']
        h4char=2*h4plus-(24+double_chi)//2
    h3char=h4char-chi_tilde
    results[lab]={'permutation':list(per),'face_fixed_signed_traces':[c[1] for c in cs],
        'invariant_C4':b4plus,'rank_d4_invariant':ranks[0],'invariant_C5':b5plus,
        'invariant_H4':h4plus,'invariant_C3':cs[3][0],'rank_d3_invariant':d3_ranks[0],'invariant_H3':h3plus,'reduced_lefschetz':chi_tilde,'H4_trace':h4char,'H3_trace':h3char}
    print('CLASS',lab,results[lab],flush=True)
    assert h3plus == {'id':21,'transposition':9,'double_transposition':11,'three_cycle':7,'four_cycle':5}[lab]
print('RESULT_JSON',json.dumps(results,sort_keys=True),flush=True)

# The boundary tetrahedron also has its canonical order-reversing complement
# automorphism of Hasse incidences. It commutes with all four-label permutations.
# Compute the entire S4 x C2 graded character, which is not determined by
# the restriction to S4 or by the pure Morse-complex ghost character.
ghost_map=tuple(eidx[(15^b,15^a)] for a,b in hedges)
assert all(ghost_map[ghost_map[i]]==i for i in range(24))

def compose_maps(a,b):
    return tuple(a[b[i]] for i in range(24))

idmap=tuple(range(24))

def invariant_dims(emap):
    cs=[orbit_columns(k,emap) for k in (4,5,6)]
    # k=4 is C3, k=5 is C4, k=6 is C5
    r3=[rank_columns(cs[0][2],p) for p in P]
    r4=[rank_columns(cs[1][2],p) for p in P]
    assert r3[0]==r3[1] and r4[0]==r4[1]
    h3=cs[0][0]-r3[0]-r4[0]
    h4=cs[1][0]-r4[0]-cs[2][0]  # d5 globally injective
    assert 0<=h3<=21 and 0<=h4<=24
    return {'H3':h3,'H4':h4,'C3':cs[0][0],'C4':cs[1][0],'C5':cs[2][0],
            'rank_d3':r3[0],'rank_d4':r4[0]}

@lru_cache(None)
def inv_cached(emap):return invariant_dims(emap)

def char_from_invariant_powers(emap):
    powers=[idmap]; cur=idmap
    for k in range(1,13):
        cur=compose_maps(emap,cur)
        powers.append(cur)
        if cur==idmap:break
    order=len(powers)-1
    assert order in (1,2,3,4,6)
    inv={d:inv_cached(powers[d]) for d in range(1,order+1) if order%d==0}
    chis={}
    for hom,dimension in [('H3',21),('H4',24)]:
        A=inv[1][hom]
        if order==1:c=dimension
        elif order==2:c=2*A-dimension
        elif order==3:
            assert (3*A-dimension)%2==0
            c=(3*A-dimension)//2
        elif order==4:c=2*A-inv[2][hom]
        else:
            B=inv[2][hom];C=inv[3][hom]
            assert (C-A)%2==0
            a1=A;a2=B-A;a3=(C-A)//2
            assert (dimension-a1-a2-2*a3)%2==0
            a6=(dimension-a1-a2-2*a3)//2
            assert min(a1,a2,a3,a6)>=0
            c=a1-a2-a3+a6
        chis[hom]=c
    return {'order':order,'invariants':{str(k):v for k,v in inv.items()},'traces':chis}

full={}
for label,per in [('id',(0,1,2,3)),('transposition',(1,0,2,3)),('double_transposition',(1,0,3,2)),('three_cycle',(1,2,0,3)),('four_cycle',(1,2,3,0))]:
    pmap=perm_map(per)
    for ghost in (0,1):
        emap=pmap if not ghost else compose_maps(ghost_map,pmap)
        computed=char_from_invariant_powers(emap)
        if ghost==0:
            assert computed['traces']['H3']==results[label]['H3_trace']
            assert computed['traces']['H4']==results[label]['H4_trace']
        full[label+('_ghost' if ghost else '_natural')]=computed
        print('FULL',label,ghost,computed,flush=True)

# A full direct signed face trace, independent of invariant-boundary ranks,
# must agree with the alternating character in all ten conjugacy classes.
def direct_reduced_L(emap):
    return -1+sum(((-1)**(k-1))*sum(face_action(f,emap)[1] for f in faces[k] if face_action(f,emap)[0]==f)
                for k in range(1,7))
for label,per in [('id',(0,1,2,3)),('transposition',(1,0,2,3)),('double_transposition',(1,0,3,2)),('three_cycle',(1,2,0,3)),('four_cycle',(1,2,3,0))]:
    for ghost in (0,1):
        emap=perm_map(per) if not ghost else compose_maps(ghost_map,perm_map(per))
        a=full[label+('_ghost' if ghost else '_natural')]['traces']
        lf=direct_reduced_L(emap)
        assert a['H4']-a['H3']==lf,(label,ghost,a,lf)

print('FULL_CHARACTER_JSON',json.dumps(full,sort_keys=True),flush=True)
# Check all twenty irreducible multiplicities by exact group-character arithmetic.
class_order=('id','transposition','double_transposition','three_cycle','four_cycle')
class_sizes=(1,6,3,8,6)
specht={'(4)':(1,1,1,1,1), '(3,1)':(3,1,-1,0,-1),
        '(2,2)':(2,0,2,-1,0), '(2,1,1)':(3,-1,-1,0,1),
        '(1,1,1,1)':(1,-1,1,1,-1)}
expected={
  'H3':{'(4)':(0,0),'(3,1)':(2,0),'(2,2)':(1,1),'(2,1,1)':(2,1),'(1,1,1,1)':(1,1)},
  'H4':{'(4)':(0,0),'(3,1)':(1,2),'(2,2)':(1,1),'(2,1,1)':(2,1),'(1,1,1,1)':(1,1)} }
for hom in ('H3','H4'):
    natur=[full[c+'_natural']['traces'][hom] for c in class_order]
    ghost=[full[c+'_ghost']['traces'][hom] for c in class_order]
    for partition,irrep in specht.items():
        positive=sum(s*(a+b)*v for s,a,b,v in zip(class_sizes,natur,ghost,irrep))
        negative=sum(s*(a-b)*v for s,a,b,v in zip(class_sizes,natur,ghost,irrep))
        assert positive%48==0 and negative%48==0
        multiplicities=(positive//48,negative//48)
        assert multiplicities==expected[hom][partition]
        print('SPECHT',hom,partition,multiplicities,flush=True)
# Independently established full-tetrahedron H4 character is (99,1,-1,0,-1).
# The long exact sequence of the pair predicts a relative fourfold regular S4 character.
known_full=(99,1,-1,0,-1)
virtual_boundary=tuple(full[c+'_natural']['traces']['H4']-full[c+'_natural']['traces']['H3'] for c in class_order)
relative=tuple(a-b for a,b in zip(known_full,virtual_boundary))
assert relative==(96,0,0,0,0)
print('INDEPENDENT_RELATIVE_CHARACTER_CHECK',relative,flush=True)
print('BOUNDARY_TETRAHEDRON_S4xC2_GRADED_CHARACTER_PASS',flush=True)
