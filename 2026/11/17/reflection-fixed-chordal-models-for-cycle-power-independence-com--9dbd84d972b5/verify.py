"""Finite tests for dihedral geometric fixed loci of cycle-power independence complexes.

Run: python verify.py
Uses only the Python standard library.
"""
from collections import defaultdict, Counter, deque
from itertools import combinations


def neighbor(a,b,n,k):
    d=abs(a-b)
    return min(d,n-d)<=k and a!=b


def gen_orbits(n,t,a=None):
    assert n%t==0
    gens=[lambda x:(x+t)%n]
    if a is not None:
        gens.append(lambda x:(a-x)%n)
    unseen=set(range(n)); out=[]
    while unseen:
        start=min(unseen); stack=[start]; orbit={start}
        while stack:
            z=stack.pop()
            for f in gens:
                y=f(z)
                if y not in orbit: orbit.add(y);stack.append(y)
        out.append(frozenset(orbit));unseen-=orbit
    return out


def actual_orbit_graph(n,k,t,a):
    orbits=gen_orbits(n,t,a)
    valid=[o for o in orbits if all(not neighbor(x,y,n,k) for x,y in combinations(sorted(o),2))]
    E={frozenset((i,j)) for i,j in combinations(range(len(valid)),2)
       if any(neighbor(x,y,n,k) for x in valid[i] for y in valid[j])}
    return valid,E


def canonical_model(t,k,a):
    if a is None:
        if t<=k:return [],set(),None
        return list(range(t)),{frozenset((i,j)) for i,j in combinations(range(t),2)
                 if neighbor(i,j,t,k)},None
    if t<=k:return [],set(),None
    a%=t
    if t%2:
        b=(a*pow(2,-1,t))%t; type_=0
    else:
        b=(a-(a%2))//2;type_=a%2
    if type_==0:
        m=t//2
        valid=sorted(set(([0,m] if t%2==0 else [0])+
                  [j for j in range(1,m+1) if (2*j>k and t-2*j>k)]))
        classes={j:frozenset((j,(-j)%t)) for j in valid}
    else:
        valid=[j for j in range(1,t//2+1) if 2*j-1>k and t-2*j+1>k]
        classes={j:frozenset((j,(1-j)%t)) for j in valid}
    edge={frozenset((i,j)) for i,j in combinations(valid,2) if j-i<=k}
    return valid,edge,(b,classes)


def direct_face_comparisons(n,k,orbits,E):
    edges={(min(e),max(e)) for e in (tuple(x) for x in E)}
    count=0
    for mask in range(1<<len(orbits)):
        selected=[i for i in range(len(orbits)) if mask>>i&1]
        union=sorted(v for i in selected for v in orbits[i])
        source_independent=all(not neighbor(x,y,n,k) for x,y in combinations(union,2))
        model_independent=all(not(i in selected and j in selected) for i,j in edges)
        assert source_independent==model_independent,(n,k,orbits,selected)
        count+=1
    return count


def test():
    checked=0;count_faces=0;rotations=0;reflections=0; nonzero=0; maxn=0
    for n in range(4,33):
        maxn=max(maxn,n)
        for k in range(1,min(7,(n-2)//2)+1):
            for t in range(1,n+1):
                if n%t:continue
                cases=[None,0,1,2,3]
                for a in cases:
                    if a is not None and a>=n:continue
                    obs,edges=actual_orbit_graph(n,k,t,a)
                    names,expected,sym=canonical_model(t,k,a)
                    if a is None:
                        labels={i:frozenset((i,)) for i in names}
                        shift=0
                    else:
                        shift,labels=sym if sym is not None else (0,{})
                    actual_labels=[frozenset({(x-shift)%t for x in orb}) for orb in obs]
                    assert len(obs)==len(names),(n,k,t,a,obs,names)
                    ren={label:idx for idx,label in enumerate(actual_labels)}
                    assert len(ren)==len(actual_labels),(n,k,t,a,actual_labels)
                    assert all(label in ren for label in labels.values()),(n,k,t,a,actual_labels,labels)
                    pred_edges={frozenset((ren[labels[i]],ren[labels[j]])) for i,j in
                       (tuple(e) for e in expected)}
                    assert edges==pred_edges,(n,k,t,a,obs,edges,labels,expected,pred_edges)
                    # Exhaustively compare all invariant vertex-orbit subsets for tractable cases.
                    if len(obs)<=12:
                        count_faces+=direct_face_comparisons(n,k,obs,pred_edges)
                    checked+=1
                    rotations+=(a is None)
                    reflections+=(a is not None)
                    nonzero+=(len(obs)>0)
    # The explicit mixed-wedge test: reflection i -> 1-i of C_22^3.
    obs,edges=actual_orbit_graph(22,3,22,1)
    ns,exp,_=canonical_model(22,3,1)
    assert ns==list(range(3,10))
    # Independence complex of P_7^3 has 7 vertices and exactly six edges;
    # its graph realization has two components, hence reduced H_0=Z and H_1=Z.
    ind_edges=[(i,j) for i,j in combinations(ns,2) if frozenset((i,j)) not in exp]
    assert len(ind_edges)==6,(ns,ind_edges)
    adj={i:set() for i in ns}
    for i,j in ind_edges:adj[i].add(j);adj[j].add(i)
    seen=set();ncomp=0
    for i in ns:
        if i in seen:continue
        ncomp+=1;st=[i];seen.add(i)
        while st:
            for j in adj[st.pop()]:
                if j not in seen:seen.add(j);st.append(j)
    assert ncomp==2 and 6-7+ncomp==1
    assert all(not(all(frozenset((i,j)) not in exp for i,j in combinations(t,2)))
               for t in combinations(ns,3))
    print('CYCLE_POWER_FIXED_ORBIT_MODELS_PASS')
    print(f'cases={checked} rotations={rotations} reflections={reflections} nonempty_models={nonzero}')
    print(f'exhaustive_invariant_face_subsets_count={count_faces} maximum_original_cycle_size={maxn}')
    print('mixed_example=n22_k3_edge_reflection: Ind(P7^3)=S0 wedge S1')

if __name__=='__main__':test()
