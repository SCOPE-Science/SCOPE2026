"""Independent finite checks of a multipartite induced-forest fault classification.
Python standard library only. The structural all-order proof is separate.
"""
import itertools, collections

def graph(parts, fault):
    labels=[]; index=0
    for n in parts:
        labels.append(list(range(index,index+n))); index+=n
    adj=[0]*index
    for i in range(len(parts)):
        for j in range(i+1,len(parts)):
            for u in labels[i]:
                for v in labels[j]:
                    if fault and (u,v)==(labels[0][0],labels[1][0]): continue
                    adj[u]|=1<<v; adj[v]|=1<<u
    return adj

def faces(adj):
    n=len(adj); F=collections.defaultdict(list)
    for s in range(1,1<<n):
        V=[i for i in range(n) if s>>i&1]
        parent=list(range(n))
        def root(x):
            while parent[x]!=x: x=parent[x]
            return x
        ok=True
        for j,v in enumerate(V):
            for u in V[:j]:
                if adj[u]>>v&1:
                    ru,rv=root(u),root(v)
                    if ru==rv:ok=False;break
                    parent[ru]=rv
            if not ok: break
        if ok:F[len(V)].append(s)
    return F

def rank(cols):
    piv={}
    for col in cols:
        while col:
            k=col.bit_length()-1
            if k in piv: col^=piv[k]
            else: piv[k]=col;break
    return len(piv)

def betti(F):
    idx={k:{v:i for i,v in enumerate(f)} for k,f in F.items()}
    d={}
    for k,V in F.items():
        if k==1:continue
        cols=[]
        for s in V:
            col=0
            for v in range(s.bit_length()):
                if s>>v&1: col ^= 1<<idx[k-1][s^(1<<v)]
            cols.append(col)
        d[k]=rank(cols)
    return {k-1:len(F[k])-d.get(k,0)-d.get(k+1,0)-(k==1) for k in F if len(F[k])-d.get(k,0)-d.get(k+1,0)-(k==1)}

def test(parts):
    N=sum(parts); r=len(parts)
    A,B=faces(graph(parts,False)),faces(graph(parts,True))
    u=sum((parts[i]-1)*(parts[j]-1) for i in range(r) for j in range(i+1,r))
    a=(parts[0]-1)*(parts[1]-1)
    s=sum(x-1 for x in parts[2:])
    expected_old={1:(r-1)*(r-2)//2,2:u}
    expected_new={1:(r-2)*(r-3)//2,2:u-a+s}
    fo=betti(A); fn=betti(B)
    assert fo=={k:v for k,v in expected_old.items() if v},(parts,fo,expected_old)
    assert fn=={k:v for k,v in expected_new.items() if v},(parts,fn,expected_new)
    allnew={k:set(B.get(k,()))-set(A.get(k,())) for k in B}
    sizes={k:len(v) for k,v in allnew.items() if v}
    assert sizes=={k:v for k,v in {3:sum(parts[2:]),4:a}.items() if v},(parts,sizes)
    oldnew={k:set(A[k])-set(B.get(k,())) for k in A}
    assert not any(oldnew.values())
    print('PASS',parts, 'new_faces',sizes, 'old_hom',fo, 'new_hom',fn, flush=True)

cases=[(1,1,1),(1,2,2),(2,2,2),(2,3,2),(3,3,2),(2,3,3),(3,3,3),(2,4,4),
       (1,1,1,1),(1,2,2,2),(2,2,2,2),(1,2,3,2),(2,2,2,3),
       (1,1,1,1,1),(2,1,1,1,1)]
for case in cases:test(case)
print('ALL_CHECKS_PASS',len(cases))
