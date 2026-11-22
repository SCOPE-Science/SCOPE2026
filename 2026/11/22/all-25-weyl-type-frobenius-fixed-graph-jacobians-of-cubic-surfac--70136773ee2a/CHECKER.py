#!/usr/bin/env python3
"""Exact, self-contained verifier of the cubic line--tritangent Levi graph and its Weyl fixed Jacobians.
Python 3.10+; standard library only. This is a finite exact arithmetic certificate, not an implementation of an external proof assistant.
"""
import collections
import itertools
import math

NUM_LABELS = 6
P = range(NUM_LABELS)
LINE_LABELS = ([('E', i) for i in P] +
               [('L', i, j) for i,j in itertools.combinations(P, 2)] +
               [('Q', i) for i in P])
ID = {v:i for i,v in enumerate(LINE_LABELS)}


def divisor(v):
    m=[0]*6
    if v[0]=='E': m[v[1]]=-1; return (0,tuple(m))
    if v[0]=='L': m[v[1]]=m[v[2]]=1; return (1,tuple(m))
    m=[1]*6; m[v[1]]=0
    return (2,tuple(m))


def product(a,b):
    return a[0]*b[0]-sum(x*y for x,y in zip(a[1],b[1]))


def triangles():
    triples=[]
    for i in P:
        for j in P:
            if i!=j: triples.append((('E',i),('L',min(i,j),max(i,j)),('Q',j)))
    for a,b in itertools.combinations(P,2):
        rem=sorted(set(P)-{a,b})
        for c,d in itertools.combinations(rem,2):
            e,f=sorted(set(rem)-{c,d})
            t=tuple(sorted((('L',a,b),('L',c,d),('L',e,f))))
            if t not in triples: triples.append(t)
    assert len(triples)==len(set(tuple(sorted(t)) for t in triples))==45
    return triples

TRIPLES = triangles()
TRI_ID = {tuple(sorted(t)):j for j,t in enumerate(TRIPLES)}


def verify_geometry():
    vec=[divisor(v) for v in LINE_LABELS]
    anti=(3,(1,1,1,1,1,1))
    geometric=[]
    for a,b,c in itertools.combinations(range(27),3):
        x,y,z=vec[a],vec[b],vec[c]
        if (x[0]+y[0]+z[0],tuple(x[1][i]+y[1][i]+z[1][i] for i in P)) == anti:
            geometric.append(frozenset((LINE_LABELS[a],LINE_LABELS[b],LINE_LABELS[c])))
    assert len(geometric)==45
    assert set(geometric)==set(frozenset(t) for t in TRIPLES)
    for t in TRIPLES:
        assert all(product(divisor(a),divisor(b))==1 for a,b in itertools.combinations(t,2))
    assert all(product(x,x)==-1 for x in vec)
    return vec


def laplacian():
    L=[[0]*72 for _ in range(72)]
    for j,t in enumerate(TRIPLES):
        for v in t:
            i=ID[v];w=27+j
            L[i][i]+=1;L[w][w]+=1
            L[i][w]-=1;L[w][i]-=1
    assert all(L[i][i]==(5 if i<27 else 3) for i in range(72))
    assert all(sum(row)==0 for row in L)
    assert sum(L[i][i] for i in range(72))==270
    # A = point collinearity graph, all twenty-seven lines meet ten others.
    BB=[[sum(L[i][j]*L[k][j] for j in range(27,72)) for k in range(27)] for i in range(27)]
    assert all(BB[i][i]==5 for i in range(27))
    A=[[BB[i][j]-(5 if i==j else 0) for j in range(27)] for i in range(27)]
    assert all(sum(row)==10 for row in A)
    V=verify_geometry()
    assert all(A[i][j]==(product(V[i],V[j]) if i!=j else 0) for i in range(27) for j in range(27))
    for i in range(27):
        for j in range(27):
            dot=sum(A[i][k]*A[k][j] for k in range(27))
            assert dot == 5*(i==j)-4*A[i][j]+5
    return L


def bareiss(A):
    M=[list(row) for row in A]; n=len(M); d=1; sign=1
    for k in range(n-1):
        if M[k][k]==0:
            t=next(i for i in range(k+1,n) if M[i][k]); M[k],M[t]=M[t],M[k];sign=-sign
        p=M[k][k]
        for i in range(k+1,n):
            c=M[i][k]
            for j in range(k+1,n):
                num=p*M[i][j]-c*M[k][j]
                assert num%d==0
                M[i][j]=num//d
            M[i][k]=0
        d=p
    return sign*M[-1][-1]


def valuations(M,p,level):
    modulus=p**level
    a=[[z%modulus for z in row] for row in M]
    r=len(a);s=len(a[0]);out=[]
    def val(z):
        if not z: return level
        k=0
        while z%p==0: k+=1;z//=p
        return k
    for k in range(min(r,s)):
        loc=None;v=level
        for i in range(k,r):
            for j in range(k,s):
                if a[i][j]!=0:
                    w=val(a[i][j])
                    if w<v:loc=(i,j);v=w
                    if w==0:break
            if v==0:break
        if loc is None:
            out.extend([level]*(min(r,s)-k));break
        i,j=loc
        a[k],a[i]=a[i],a[k]
        if j!=k:
            for row in a:row[j],row[k]=row[k],row[j]
        pv=p**v
        inv=pow(a[k][k]//pv,-1,modulus)
        a[k]=[(x*inv)%modulus for x in a[k]]
        assert a[k][k]==pv
        for i in range(k+1,r):
            c=a[i][k]//pv
            if c: a[i]=[(a[i][j]-c*a[k][j])%modulus for j in range(s)]
        for j in range(k+1,s):
            c=a[k][j]//pv
            if c:
                for i in range(r):a[i][j]=(a[i][j]-c*a[i][k])%modulus
        assert all(a[i][k]==0 for i in range(k+1,r))
        assert all(a[k][j]==0 for j in range(k+1,s))
        out.append(v)
    return out


def cycle_type(p):
    seen=set();lengths=[]
    for i in range(len(p)):
        if i in seen: continue
        j=i;length=0
        while j not in seen:
            seen.add(j);j=p[j];length+=1
        lengths.append(length)
    return tuple(sorted(lengths,reverse=True))


def compose(a,b):return tuple(a[b[i]] for i in range(len(a)))


def line_action_from_point_permutation(perm):
    def image(v):
        if v[0] in ('E','Q'):return (v[0],perm[v[1]])
        a,b=sorted([perm[v[1]],perm[v[2]]]);return ('L',a,b)
    return tuple(ID[image(v)] for v in LINE_LABELS)


def reflection():
    vecs={divisor(v):i for i,v in enumerate(LINE_LABELS)}
    out=[]
    for v in LINE_LABELS:
        degree,m=divisor(v);k=degree-sum(m[:3])
        new=(degree+k,tuple(m[i]+(k if i<3 else 0) for i in P))
        out.append(vecs[new])
    return tuple(out)


def generators():
    gen=[]
    for i in range(5):
        p=list(range(6));p[i],p[i+1]=p[i+1],p[i]
        gen.append(line_action_from_point_permutation(p))
    gen.append(reflection())
    ident=tuple(range(27))
    assert all(compose(g,g)==ident for g in gen)
    return gen


def conjugacy_classes():
    gen=generators(); identity=tuple(range(27))
    universe={identity}
    queue=[identity]
    for elt in queue:
        for g in gen:
            nxt=compose(g,elt)
            if nxt not in universe:
                universe.add(nxt);queue.append(nxt)
    assert len(queue)==len(universe)==51840
    remaining=universe.copy();cls=[]
    while remaining:
        rep=min(remaining);orbit={rep};todo=[rep]
        for x in todo:
            for g in gen:
                y=compose(g,compose(x,g))
                if y not in orbit:orbit.add(y);todo.append(y)
        assert orbit<=remaining
        remaining-=orbit
        cls.append((rep,len(orbit)))
    assert len(cls)==25 and sum(size for _,size in cls)==51840
    return cls


def extend_action(g):
    out=list(g)
    for t in TRIPLES:
        t2=tuple(sorted(LINE_LABELS[g[ID[v]]] for v in t))
        out.append(27+TRI_ID[t2])
    assert sorted(out)==list(range(72))
    return out


def group_coinvariants(L,g,root):
    f=extend_action(g)
    vv=[i for i in range(72) if i!=root];pos={v:i for i,v in enumerate(vv)}
    E=[[0]*71 for _ in vv]
    for j,v in enumerate(vv):
        if f[v]!=root:E[pos[f[v]]][j]+=1
        if f[root]!=root:E[pos[f[root]]][j]-=1
        E[j][j]-=1
    presentation=[[L[v][w] for w in vv]+E[i] for i,v in enumerate(vv)]
    x=valuations(presentation,3,4)
    y=valuations(presentation,5,2)
    assert max(x)<4 and max(y)<2
    return dict(sorted((k,v) for k,v in collections.Counter(3**x[i]*5**y[i] for i in range(71)).items() if k!=1))


def fmt_cycle(c):
    return tuple(sorted(collections.Counter(c).items()))


def run():
    L=laplacian()
    root=[row[:71] for row in L[:71]]
    # B B^t eigenvalues 15 (once), 6 (20 times), 0 (six times).
    # The matrix-tree theorem gives exactly 3^62*5^6.
    exact=3**62*5**6
    assert bareiss(root)==exact
    base=group_coinvariants(L,tuple(range(27)),71)
    assert base=={3:10,9:5,27:8,135:6}
    assert group_coinvariants(L,tuple(range(27)),0)==base
    rows=[]
    for rep,size in conjugacy_classes():
        v=group_coinvariants(L,rep,71)
        assert group_coinvariants(L,rep,0)==v
        cyc=cycle_type(rep)
        order=math.lcm(*cyc)
        cyc45=cycle_type(tuple(x-27 for x in extend_action(rep)[27:]))
        rows.append((order,size,fmt_cycle(cyc),fmt_cycle(cyc45),v))
    rows.sort(key=lambda x:(x[0],x[1],x[2]))
    assert len(set((x[0],x[1],x[2]) for x in rows))==25
    assert len(set(tuple(x[4].items()) for x in rows))==23
    assert sum(x[1] for x in rows)==51840
    for row in rows:
        assert all(b in (3,9,27,135) for b in row[4])
        print('class',rows.index(row)+1,'order',row[0],'size',row[1],
              'lines',row[2],'planes',row[3],'group',row[4])
    # Main distinction: two classes with nine cycles of length three on lines
    same=[x for x in rows if x[2]==((3,9),)]
    assert len(same)==2
    assert {x[1] for x in same}=={80,480}
    assert {x[1]:sum(v for k,v in x[4].items() if k%5==0) for x in same}=={80:0,480:2}
    print('CUBIC_TRITANGENT_WEYL_25_FROBENIUS_CRITICAL_GROUPS_OK')

if __name__=='__main__':run()
