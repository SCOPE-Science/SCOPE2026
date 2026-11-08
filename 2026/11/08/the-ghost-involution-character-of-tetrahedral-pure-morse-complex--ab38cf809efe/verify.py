#!/usr/bin/env python3
"""Standalone exact signed Lefschetz certificate for tetrahedral Morse-matching complexes.
Only Python 3 standard library is needed. No stored numerical tables are used in the calculation.
"""
from itertools import permutations
from collections import Counter, defaultdict


def faces(boundary):
    return sorted((s for s in range(1,16) if not (boundary and s==15)), key=lambda s:(s.bit_count(),s))


def hasse(faces):
    index={s:i for i,s in enumerate(faces)}
    return sorted((index[s],index[t]) for s in faces for t in faces if t.bit_count()==s.bit_count()+1 and s&t==s)


def acyclic(n,edges,matching):
    used=set(matching)
    graph=[[] for _ in range(n)]
    indeg=[0]*n
    for i,(a,b) in enumerate(edges):
        v,w=(a,b) if i in used else (b,a)
        graph[v].append(w)
        indeg[w]+=1
    zero=[i for i,d in enumerate(indeg) if d==0]
    while zero:
        i=zero.pop()
        for j in graph[i]:
            indeg[j]-=1
            if indeg[j]==0:zero.append(j)
    return all(x==0 for x in indeg)


def all_matchings(fs,es):
    result=[]
    def rec(i,used,chosen):
        if i==len(es):
            if chosen and acyclic(len(fs),es,chosen): result.append(tuple(chosen))
            return
        rec(i+1,used,chosen)
        a,b=es[i]
        if not (used & ((1<<a)|(1<<b))):
            chosen.append(i)
            rec(i+1,used|(1<<a)|(1<<b),chosen)
            chosen.pop()
    rec(0,0,[])
    return result


def pure_faces(matchings):
    maxsize=max(map(len,matchings))
    out=set()
    for f in matchings:
        if len(f)==maxsize:
            for mask in range(1,1<<maxsize):
                out.add(tuple(f[i] for i in range(maxsize) if (mask>>i)&1))
    return sorted(out)


def vertex_action(p,fs,es):
    index={s:i for i,s in enumerate(fs)}
    fmap=[index[sum(1<<p[i] for i in range(4) if (s>>i)&1)] for s in fs]
    eindex={ab:i for i,ab in enumerate(es)}
    return [eindex[(fmap[a],fmap[b])] for a,b in es]


def parity_of_images(seq):
    inv=sum(seq[i]>seq[j] for i in range(len(seq)) for j in range(i+1,len(seq)))
    return -1 if inv%2 else 1


def contributions(matchings,permutation):
    c=defaultdict(int)
    for simplex in matchings:
        images=tuple(permutation[i] for i in simplex)
        if sorted(images)==list(simplex):
            c[len(simplex)]+=(-1)**(len(simplex)-1)*parity_of_images(images)
    return c


def orbit_contributions(fs,es,permutation,pure=None):
    # independent enumeration of invariant matchings as unions of vertex orbits
    unused=set(range(len(es)));orbits=[]
    while unused:
        i=min(unused);orb=[];j=i
        while j not in orb:
            orb.append(j);unused.remove(j);j=permutation[j]
        orbits.append(tuple(sorted(orb)))
    orbitdata=[]
    for orb in orbits:
        mask=0;disjoint=True
        for i in orb:
            a,b=es[i]
            if mask&((1<<a)|(1<<b)):disjoint=False;break
            mask|=(1<<a)|(1<<b)
        if disjoint:orbitdata.append((orb,mask))
    c=defaultdict(int)
    def rec(j,used,chosen):
        if j==len(orbitdata):
            if not chosen:return
            s=tuple(sorted(chosen))
            if pure is not None and s not in pure:return
            if not acyclic(len(fs),es,s):return
            images=[permutation[i] for i in s]
            assert sorted(images)==list(s)
            c[len(s)]+=(-1)**(len(s)-1)*parity_of_images(images)
            return
        rec(j+1,used,chosen)
        orb,mask=orbitdata[j]
        if not(used&mask):rec(j+1,used|mask,chosen+list(orb))
    rec(0,0,[])
    return c


def cycletype(p):
    seen=set(); lengths=[]
    for i in range(4):
        if i in seen:continue
        j=i;n=0
        while j not in seen:
            seen.add(j);j=p[j];n+=1
        lengths.append(n)
    return tuple(sorted(lengths,reverse=True))

if __name__=='__main__':
    records={}
    reps={}
    for p in permutations(range(4)):
        reps.setdefault(cycletype(p),p)
    expected_sizes={(1,1,1,1):1,(2,1,1):6,(2,2):3,(3,1):8,(4,):6}
    assert {k:sum(cycletype(p)==k for p in permutations(range(4))) for k in reps}==expected_sizes
    for boundary in (False,True):
        fs=faces(boundary);es=hasse(fs);allf=all_matchings(fs,es);pure=pure_faces(allf)
        fvec=tuple(Counter(map(len,allf))[k] for k in range(1,max(map(len,allf))+1))
        purevec=tuple(Counter(map(len,pure))[k] for k in range(1,max(map(len,pure))+1))
        print('boundary',boundary,'full_f_vector',fvec,'pure_f_vector',purevec)
        assert fvec==((24,216,896,1692,1248,256) if boundary else (28,300,1544,3932,4632,2128,256))
        assert purevec==((24,216,896,1680,1152,256) if boundary else (28,300,1544,3680,3672,1600,256))
        result={}
        for typ,p in reps.items():
            action=vertex_action(p,fs,es)
            t1=contributions(allf,action)
            t2=contributions(pure,action)
            if typ!=(1,1,1,1):
                assert dict(t1)==dict(orbit_contributions(fs,es,action))
                assert dict(t2)==dict(orbit_contributions(fs,es,action,set(pure)))
            lf=sum(t1.values());lp=sum(t2.values())
            result[typ]=(lf,lp)
            print('cycle_type',typ,'full_trace',lf,'pure_trace',lp,'pure_contrib_by_cardinality',tuple(t2.get(k,0) for k in range(1,max(map(len,pure))+1)))
        for p in permutations(range(4)):
            typ=cycletype(p);act=vertex_action(p,fs,es)
            assert (sum(contributions(allf,act).values()),sum(contributions(pure,act).values()))==result[typ]
        records[boundary]=result
    assert [records[b][k][1] for k in [(1,1,1,1),(2,1,1),(2,2),(3,1),(4,)] for b in (False,True)]==[-80,-80,2,2,4,4,1,1,0,0]
    assert [records[False][k][0] for k in [(1,1,1,1),(2,1,1),(2,2),(3,1),(4,)]]==[100,2,0,1,0]
    # Boundary face-complement reverses inclusions. On a Hasse incidence (a,b),
    # it sends (a,b) to (complement(b),complement(a)), defining the ghost involution.
    bfs=faces(True);bes=hasse(bfs);ball=all_matchings(bfs,bes);bpure=pure_faces(ball)
    faceindex={s:i for i,s in enumerate(bfs)}
    edgeindex={ab:i for i,ab in enumerate(bes)}
    dual=[edgeindex[(faceindex[15^bfs[b]],faceindex[15^bfs[a]])] for a,b in bes]
    assert all(dual[dual[i]]==i for i in range(len(bes)))
    dual_l={}
    for typ,p in reps.items():
        sigma=vertex_action(p,bfs,bes)
        assert all(dual[sigma[i]]==sigma[dual[i]] for i in range(len(bes)))
        action=[dual[sigma[i]] for i in range(len(bes))]
        c=contributions(bpure,action)
        c_orbit=orbit_contributions(bfs,bes,action,set(bpure))
        assert dict(c)==dict(c_orbit)
        dual_l[typ]=sum(c.values())
        print('ghost_cycle_type',typ,'pure_boundary_lefschetz',dual_l[typ], 'contributions', tuple(c.get(k,0) for k in range(1,7)))
    for p in permutations(range(4)):
        sigma=vertex_action(p,bfs,bes)
        action=[dual[sigma[i]] for i in range(len(bes))]
        assert sum(contributions(bpure,action).values())==dual_l[cycletype(p)]
    assert [dual_l[k] for k in [(1,1,1,1),(2,1,1),(2,2),(3,1),(4,)]]==[-8,-2,4,1,0]
    irreps={
      '(4)':(1,1,1,1,1),
      '(3,1)':(3,1,-1,0,-1),
      '(2,2)':(2,0,2,-1,0),
      '(2,1,1)':(3,-1,-1,0,1),
      '(1,1,1,1)':(1,-1,1,1,-1),
    }
    classes=[(1,1,1,1),(2,1,1),(2,2),(3,1),(4,)]
    chi_pure=[1-records[False][k][1] for k in classes]
    chi_full=[records[False][k][0]-1 for k in classes]
    chi_ghost=[1-dual_l[k] for k in classes]
    chi_ghost_plus=[(u+v)//2 for u,v in zip(chi_pure,chi_ghost)]
    chi_ghost_minus=[(u-v)//2 for u,v in zip(chi_pure,chi_ghost)]
    assert chi_ghost==[9,3,-3,0,1]
    assert chi_ghost_plus==[45,1,-3,0,1]
    assert chi_ghost_minus==[36,-2,0,0,0]
    print('rational_top_homology_characters','pure',chi_pure,'full_simplex',chi_full,'ghost_coset',chi_ghost)

    for name,chi in [('pure',chi_pure),('full_simplex',chi_full),('ghost_plus',chi_ghost_plus),('ghost_minus',chi_ghost_minus)]:
        mult={ir:sum(chi[j]*vals[j]*expected_sizes[classes[j]] for j in range(5))//24 for ir,vals in irreps.items()}
        assert all(sum(chi[j]*vals[j]*expected_sizes[classes[j]] for j in range(5))%24==0 for vals in irreps.values())
        assert sum(mult[k]*irreps[k][0] for k in irreps)==chi[0]
        print('decomposition',name,mult)
    assert chi_pure==[81,-1,-3,0,1]
    assert chi_full==[99,1,-1,0,-1]
    print('ALL_VERIFY_OK')
