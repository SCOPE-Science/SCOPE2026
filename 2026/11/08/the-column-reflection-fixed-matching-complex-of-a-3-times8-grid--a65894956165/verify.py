"""Reproducible exact topology checks for a finite reflection-fixed matching complex."""
import itertools
from collections import Counter,deque

ORDER=(4,11,1,18,15,5,8,12,13,10,14,2,17,6,9,0,3,7,16,19)

def norm_edge(u,v):return tuple(sorted((u,v)))

def grid(R,C):
    E=[]
    for c in range(C):
      for r in range(R):
        if r+1<R:E.append(norm_edge((r,c),(r+1,c)))
        if c+1<C:E.append(norm_edge((r,c),(r,c+1)))
    return E

def whisker(m):
    E=[]
    for c in range(m):
      for r in range(3):
        if r<2:E.append(norm_edge((r,c),(r+1,c)))
        if c<m-1:E.append(norm_edge((r,c),(r,c+1)))
    for r in range(3):E.append(norm_edge((r,m-1),(r,m)))
    return E

def matching(E,ids):
    V=[u for i in ids for u in E[i]]
    return len(V)==len(set(V))

def faces(E):
    # Independent recursion with selected vertex list rather than combinations of graph edges
    ans=[()]
    for i,e in enumerate(E):
        add=[]
        for s in ans:
            if matching(E, s+(i,)):add.append(s+(i,))
        ans+=add
    return sorted(ans)

def fixed_orbits():
    E=grid(3,8);D={e:i for i,e in enumerate(E)}
    def refl(e):return norm_edge(*[(r,7-c) for r,c in e])
    orbit_set={tuple(sorted({i,D[refl(e)]})) for i,e in enumerate(E)}
    O=sorted(orbit_set)
    assert len(E)==37 and len(O)==20
    assert sum(len(x)==1 for x in O)==3
    assert all(matching(E,orb) for orb in O)
    A=whisker(4)
    assert len(A)==20
    # map an orbit to its left-half graph edge, or the corresponding seam pendant edge
    def key(orb):
        if len(orb)==1:
            e=E[orb[0]]
            r=e[0][0]
            return norm_edge((r,3),(r,4))
        left=[E[i] for i in orb if all(c<=3 for r,c in E[i])]
        assert len(left)==1
        return left[0]
    orbit_to_whisker={i:A.index(key(orb)) for i,orb in enumerate(O)}
    assert len(set(orbit_to_whisker.values()))==20
    for p in range(20):
      for q in range(p+1,20):
        eligible_orig=matching(E,O[p]+O[q])
        eligible_wh=matching(A,(orbit_to_whisker[p],orbit_to_whisker[q]))
        assert eligible_orig==eligible_wh,(p,q)
    # For graph matching complexes all higher simplices follow from pairwise tests.
    print('FIXED_ORBIT_MODEL_OK 37 original edges 20 orbit vertices 190 pairwise compatibility checks')

def morses():
    E=whisker(4);F=faces(E); FS=set(F)
    assert len(E)==20 and len(F)==2636
    hist=Counter(len(s)-1 for s in F if s)
    assert [hist[i] for i in range(7)]==[20,149,524,911,750,255,26]
    pairs=[]
    for v in ORDER:
      for s in sorted(FS,key=lambda x:(-len(x),x)):
        if s not in FS or v in s:continue
        t=tuple(sorted(s+(v,)))
        if t in FS:
          pairs.append((s,t))
          FS.remove(s);FS.remove(t)
    assert len(pairs)==1316 and len(FS)==4
    assert all(len(s)==5 for s in FS)
    # Independently create the full Hasse directed graph and establish acyclicity
    idx={f:i for i,f in enumerate(F)}
    matched={(idx[a],idx[b]) for a,b in pairs}
    dig=[[] for f in F];deg=[0]*len(F)
    for s in F:
      big=idx[s]
      for k in range(len(s)):
        small=idx[s[:k]+s[k+1:]]
        start,end=(small,big) if (small,big) in matched else (big,small)
        dig[start].append(end);deg[end]+=1
    queue=deque(i for i,d in enumerate(deg) if d==0)
    visited=0
    while queue:
      v=queue.popleft();visited+=1
      for w in dig[v]:
        deg[w]-=1
        if deg[w]==0:queue.append(w)
    assert visited==len(F),f'cycle in Morse matching: {visited}/{len(F)}'
    assert sum(len(a)==0 for a,b in pairs)==1
    # Remove augmented empty face and its pair: ordinary critical 0 and four 4-cells.
    crit=sorted(FS)
    print('MORSE_CERTIFICATE_OK 2636 augmented faces 1316 matched pairs 4 critical 4-faces full Hasse DAG acyclic')
    print('CRITICAL_FACES',crit)
    print('HOMOTOPY_TYPE_OK wedge of four S^4')

def direct_betti2():
    # independent mod-2 reduced boundary rank test with bit-vector elimination
    E=whisker(4);F=faces(E)
    bydim={d:[f for f in F if len(f)==d+1] for d in range(-1,7)}
    ranks={}
    for d in range(0,7):
      loc={s:i for i,s in enumerate(bydim[d-1])}
      B={}
      for s in bydim[d]:
        x=0
        for j in range(len(s)):
          x^=1<<loc[s[:j]+s[j+1:]]
        while x:
          p=x.bit_length()-1
          if p in B:x^=B[p]
          else:B[p]=x;break
      ranks[d]=len(B)
    reduced={d:len(bydim[d])-ranks.get(d,0)-ranks.get(d+1,0) for d in range(0,7)}
    assert reduced=={0:0,1:0,2:0,3:0,4:4,5:0,6:0},reduced
    print('INDEPENDENT_MOD2_RANKS_OK',reduced)

if __name__=='__main__':
 fixed_orbits();morses();direct_betti2();print('VERIFY_OK')
