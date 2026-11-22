#!/usr/bin/env python3
"""Reproduce simplicial face counts and the finite boundary cases for total three-cut complexes of Möbius ladders."""
from itertools import combinations
from collections import Counter, defaultdict, deque
from math import comb


def ladder(m):
    n=2*m
    rim={tuple(sorted((i,(i+1)%n))) for i in range(n)}
    chord={(i,i+m) for i in range(m)}
    return rim|chord


def independent_triples(n,E):
    return [t for t in combinations(range(n),3) if all(e not in E for e in combinations(t,2))]


def total_cut_faces(n,E):
    full=(1<<n)-1; faces=set()
    for triple in independent_triples(n,E):
        F=full ^ sum(1<<i for i in triple)
        s=F
        while True:
            faces.add(s)
            if s==0: break
            s=(s-1)&F
    return faces


def lex_matching(faces,n):
    remaining=set(faces)-{0}; pairs=[]
    for v in range(n):
        b=1<<v
        for f in sorted(remaining):
            if not (f & b) and (f|b) in remaining:
                remaining.remove(f);remaining.remove(f|b)
                pairs.append((f,f|b))
    # Explicit full directed Hasse graph, matched edges upward and other edges downward.
    verts=set(faces)-{0}; matched=set(pairs)
    indeg={f:0 for f in verts};out={f:[] for f in verts};edgecount=0
    for face in verts:
        for i in range(n):
            if face>>i&1:
                lower=face^(1<<i)
                if lower==0:continue
                start,end=(lower,face) if (lower,face) in matched else (face,lower)
                out[start].append(end);indeg[end]+=1;edgecount+=1
    todo=deque(v for v in verts if indeg[v]==0);seen=0
    while todo:
        a=todo.popleft();seen+=1
        for b in out[a]:
            indeg[b]-=1
            if indeg[b]==0:todo.append(b)
    assert seen==len(verts), 'Not an acyclic Morse matching'
    return remaining,pairs,edgecount


def relative_collapse(base,larger,n):
    remaining=set(larger)-set(base);pairs=[]
    while True:
        co=defaultdict(list)
        for f in remaining:
            for i in range(n):
                if f>>i&1:
                    lower=f^(1<<i)
                    if lower in remaining:co[lower].append(f)
        possible=[(a,bs[0]) for a,bs in co.items() if len(bs)==1]
        if not possible:break
        a,b=min(possible,key=lambda p:(-p[1].bit_count(),p))
        # Need free face in current enlarged complex, rather than only relative! Check
        # other cofaces in base cannot exist since base is subcomplex and a is new.
        assert a in remaining and b in remaining
        remaining.remove(a);remaining.remove(b);pairs.append((a,b))
    return remaining,pairs


def four_cycles(n,E):
    q=0
    for vs in combinations(range(n),4):
        if len([e for e in combinations(vs,2) if e in E])==4 and all(sum(1 for w in vs if tuple(sorted((v,w))) in E)==2 for v in vs):
            q+=1
    return q


def bounded_faces(n,E):
    # In triangle-free girth !=5, BI3 has no face of size >=5.
    f=[n,comb(n,2),0,0]
    for t in combinations(range(n),3):
        if any(e in E for e in combinations(t,2)): f[2]+=1
    for t in combinations(range(n),4):
        if any(set(a).isdisjoint(b) for a,b in combinations((e for e in combinations(t,2) if e in E),2)):
            f[3]+=1
    if 10<=n<=14:
        for t in combinations(range(n),5):
            if all(any(e in E for e in combinations(triple,2)) for triple in combinations(t,3)):
                raise AssertionError('unexpected five-vertex BI3 face')
    return f


def formula_f(n,E):
    deg=Counter(v for a,b in E for v in (a,b))
    S=sum(comb(deg[v],2) for v in range(n));q=four_cycles(n,E)
    e=len(E)
    return [n,comb(n,2),e*(n-2)-S,comb(e,2)-S-q],q


def run():
    for m in range(4,9):
        n=2*m; E=ladder(m)
        for name,edge in [('intact',None),('rim',(0,1)),('chord',(0,m))]:
            H=E if edge is None else E-{edge}
            f,q=formula_f(n,H)
            if m>=5: assert f==bounded_faces(n,H), (m,name,f)
            if m>=5:
                assert q==m-(1 if name=='rim' else 2 if name=='chord' else 0)
                beta=1-f[0]+f[1]-f[2]+f[3]
                target=1+comb(m+1,2) if name=='intact' else (1+comb(m,2) if name=='rim' else 2+comb(m,2))
                assert beta==target,(m,name,beta,target)
            print('M',n,name,'BI3 faces=',tuple(f),'squares=',q)
    n=8; E=ladder(4);X=total_cut_faces(n,E)
    for name,edge,want in [('intact',None,3),('rim',(0,1),3),('chord',(0,4),2)]:
        Y=X if edge is None else total_cut_faces(n,E-{edge})
        unmatched,pairs,H=lex_matching(Y,n)
        crit=Counter(f.bit_count()-1 for f in unmatched)
        assert crit==Counter({0:1,2:want}),(name,crit)
        print('M8',name,'faces=',len(Y)-1,'Morse pairs=',len(pairs),'Hasse edges=',H,'critical=',dict(crit))
        if name!='intact':
            if name=='rim':
                R,M=relative_collapse(X,Y,n)
                assert len(R)==0 and len(M)==6,(len(R),len(M))
            else:
                R=set(Y)-set(X);M=[]
                for a,b in [('1237','12357'),('3567','13567'),('123','1235'),('567','1567')]:
                    a=sum(1<<int(i) for i in a);b=sum(1<<int(i) for i in b)
                    assert a in R and b in R and b.bit_count()==a.bit_count()+1
                    assert all((f==b) for f in R if f!=a and (f&a)==a)
                    R.remove(a);R.remove(b);M.append((a,b))
                assert R=={sum(1<<i for i in (1,3,5,7))} and len(M)==4,(R,M)
                for i in (1,3,5,7):assert (next(iter(R))^(1<<i)) in X
            print('M8',name,'relative collapses=',len(M),'remaining relative faces=',len(R))
    print('VERIFY_OK')

if __name__=='__main__':run()
