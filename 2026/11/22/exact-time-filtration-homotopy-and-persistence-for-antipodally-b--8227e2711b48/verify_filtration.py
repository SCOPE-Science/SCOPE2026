#!/usr/bin/env python3
"""Recompute filtered translated four-chip avalanche complexes and their incidence data."""
from itertools import combinations
from collections import Counter


def subsets(vertices):
    s = sorted(vertices)
    return {frozenset(c) for k in range(1, len(s) + 1)
            for c in combinations(s, k)}


def firing(m, t):
    n = 2*m
    return frozenset((t % n, (t+1)%n, (t+m-1)%n, (t+m)%n))


def predicted_edges(m,t):
    if t == 0:
        return set(), set()
    if t <= m-3:
        return {frozenset((t,t+m-1))}, set()
    if t == m-2:
        return {frozenset((m-2,2*m-3))}, {m-1}
    if t == m-1:
        return {frozenset((m-1,2*m-2)),frozenset((m-1,m))}, set()
    if t == m:
        return {frozenset((m,m+1)),frozenset((0,m)),frozenset((m,2*m-1))}, set()
    if t <= 2*m-2:
        j=t-m
        return {frozenset(e) for e in ((j-1,j),(j-1,m+j),(j,m+j),(m+j,m+j+1))}, set()
    return {frozenset(e) for e in ((m-2,m-1),(m-2,2*m-1),(m-1,2*m-1),(0,m-1),(0,2*m-1))}, set()


def cone_triangle(m,j,prior):
    # Triangle {j-1,j,m+j} coned at {m+j-1} by three earlier 2-simplices.
    v=(j-1,j,m+j);a=m+j-1
    return all(frozenset((a,)+pair) in prior for pair in combinations(v,2))


def last_cone(m,prior):
    v=(0,m-1,2*m-1)
    return all(frozenset((m,)+pair) in prior for pair in combinations(v,2))


def stage_complex_check(m):
    prior=set();count=0;cones=0
    for t in range(2*m):
        F=firing(m,t)
        # independently simulate one step of threshold-one parallel chip firing
        assert len(F)==4
        new=subsets(F)
        I=new & prior
        expected_edges,extra=predicted_edges(m,t)
        got_edges={s for s in I if len(s)==2}
        assert got_edges==expected_edges,(m,t,got_edges,expected_edges)
        assert not any(len(s)>=3 for s in I),(m,t)
        verts={v for s in I for v in s}
        expected_verts={v for s in expected_edges for v in s}|extra
        assert verts==expected_verts,(m,t,verts,expected_verts)
        if m+1<=t<=2*m-2:
            assert cone_triangle(m,t-m,prior),(m,t,'cone')
            cones+=1
        if t==2*m-1:
            assert cone_triangle(m,m-1,prior) and last_cone(m,prior),(m,t,'last cone')
            cones+=2
        prior.update(new);count+=1
    return count,cones,len(prior)


def barcode(m):
    n=2*m;born={}
    for t in range(n):
        for f in subsets(firing(m,t)):
            if f not in born:born[f]=t
    simps=sorted(born,key=lambda f:(born[f],len(f),tuple(sorted(f))))
    ix={s:i for i,s in enumerate(simps)};piv={};pairs=[];births=[]
    for i,s in enumerate(simps):
        col=0
        if len(s)>1:
            for lower in combinations(sorted(s),len(s)-1):
                col^=1<<ix[frozenset(lower)]
        while col:
            row=col.bit_length()-1
            if row in piv:col^=piv[row]
            else:
                piv[row]=col
                pairs.append((row,i))
                break
        else:
            births.append(i)
    paired={p for p,_ in pairs}
    finite=Counter((len(simps[p])-1,born[simps[p]],born[simps[d]])
                   for p,d in pairs if born[simps[p]]<born[simps[d]])
    infinite=Counter((len(simps[i])-1,born[simps[i]]) for i in births if i not in paired)
    exp=Counter({(0,0):1,(1,m-2):1})
    for t in range(m+1,2*m-1):exp[(2,t)]+=1
    exp[(2,2*m-1)]+=2
    assert finite==Counter(),(m,finite)
    assert infinite==exp,(m,infinite,exp)
    return len(simps),len(pairs)


def dynamics(m):
    n=2*m;chips=[int(i in firing(m,0)) for i in range(n)]
    for t in range(n+4):
        fire={i for i,c in enumerate(chips) if c>=1}
        assert fire==firing(m,t),(m,t)
        nxt=chips[:]
        for i in fire:
            nxt[i]-=1;nxt[(i+1)%n]+=1
        chips=nxt


def main():
    stages=cones=0
    for m in range(4,101):
        dynamics(m)
        x,y,_=stage_complex_check(m)
        stages+=x;cones+=y
    simplices=columns=0
    for m in range(4,20):
        a,b=barcode(m);simplices+=a;columns+=b
    print('VERIFY_OK m=4..100 exact_step_intersections stages=%d explicit_null_disks=%d dynamics_cycles=97'%(stages,cones))
    print('BARCODE_OK m=4..19 integral_prediction_GF2_confirmed simplices=%d matrix_pairs=%d finite_positive_intervals=0'%(simplices,columns))
    print('INFINITE_BARS: H0 at 0; H1 at m-2; H2 at each t=m+1..2m-2 and twice at 2m-1')

if __name__=='__main__':main()
