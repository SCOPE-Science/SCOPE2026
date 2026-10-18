#!/usr/bin/env python3
import itertools, math

SQ2=math.sqrt(2.0)

def closure(nodes,covers):
    reach={u:{u} for u in nodes}
    for u,v in covers:
        reach[u].add(v)
    changed=True
    while changed:
        changed=False
        for u in nodes:
            z=set(reach[u])
            for v in list(reach[u]):
                z |= reach[v]
            if z != reach[u]:
                reach[u]=z
                changed=True
    return reach

def check_regular(nodes,marks,covers):
    reach=closure(nodes,covers)
    for p,q in covers:
        for a,la in marks.items():
            if q not in reach[a]:
                continue
            for b,lb in marks.items():
                if b not in reach[p]:
                    continue
                if a!=b and not (la < lb):
                    return False
    return all(not (u in marks and v in marks) for u,v in covers)

def marked_chains(nodes,marks,covers):
    out={u:[] for u in nodes}
    for u,v in covers:
        out[u].append(v)
    ans=[]
    for a in marks:
        stack=[(a,[a],0.0)]
        while stack:
            u,path,w=stack.pop()
            for v in out[u]:
                ew=1.0 if ((u in marks) ^ (v in marks)) else SQ2
                if v in marks:
                    if len(path)>=2:
                        ans.append((path+[v],w+ew))
                else:
                    stack.append((v,path+[v],w+ew))
    return ans

def formula(nodes,marks,covers):
    cs=marked_chains(nodes,marks,covers)
    assert cs
    vals=[((marks[path[-1]]-marks[path[0]])/w,path,w) for path,w in cs]
    r,path,w=min(vals,key=lambda z:z[0])
    return r,vals

def solve(A,b,eps=1e-10):
    n=len(A)
    M=[list(map(float,A[i]))+[float(b[i])] for i in range(n)]
    for c in range(n):
        p=max(range(c,n),key=lambda z:abs(M[z][c]))
        if abs(M[p][c])<eps:
            return None
        M[c],M[p]=M[p],M[c]
        q=M[c][c]
        M[c]=[x/q for x in M[c]]
        for i in range(n):
            if i==c: continue
            q=M[i][c]
            if abs(q)>eps:
                M[i]=[M[i][j]-q*M[c][j] for j in range(n+1)]
    return [M[i][-1] for i in range(n)]

def lp(nodes,marks,covers):
    U=[u for u in nodes if u not in marks]
    idx={u:i for i,u in enumerate(U)}
    m=len(U)
    rows=[]
    # rows encode lhs >= rhs, variables U then r
    for u,v in covers:
        row=[0.0]*(m+1)
        if u in marks and v not in marks:
            row[idx[v]]=1.0
            row[-1]=-1.0
            rhs=marks[u]
        elif u not in marks and v in marks:
            row[idx[u]]=-1.0
            row[-1]=-1.0
            rhs=-marks[v]
        elif u not in marks and v not in marks:
            row[idx[v]]=1.0
            row[idx[u]]=-1.0
            row[-1]=-SQ2
            rhs=0.0
        else:
            raise AssertionError("marked-marked cover")
        rows.append((row,rhs))
    row=[0.0]*(m+1); row[-1]=1.0
    rows.append((row,0.0))
    best=-1.0; bestz=None
    for act in itertools.combinations(range(len(rows)),m+1):
        z=solve([rows[i][0] for i in act],[rows[i][1] for i in act])
        if z is None: continue
        if all(sum(a*x for a,x in zip(row,z)) >= rhs-2e-8 for row,rhs in rows):
            if z[-1]>best:
                best=z[-1]; bestz=z
    assert bestz is not None
    return best,bestz,U

def envelopes(nodes,marks,covers,r):
    inc={u:[] for u in nodes}; out={u:[] for u in nodes}
    for u,v in covers:
        out[u].append(v); inc[v].append(u)
    order=[]
    rem=set(nodes)
    while rem:
        ready=[u for u in rem if all(v not in rem for v in inc[u])]
        assert ready
        for u in ready:
            order.append(u); rem.remove(u)
    L={}
    for u in order:
        if u in marks:
            L[u]=marks[u]
        else:
            vals=[]
            for v in inc[u]:
                ew=1.0 if v in marks else SQ2
                vals.append(L[v]+r*ew)
            L[u]=max(vals)
    U={}
    for u in reversed(order):
        if u in marks:
            U[u]=marks[u]
        else:
            vals=[]
            for v in out[u]:
                ew=1.0 if v in marks else SQ2
                vals.append(U[v]-r*ew)
            U[u]=min(vals)
    return L,U

cases=[
    (
        ["a","p","q","b"],
        {"a":0.0,"b":3.0},
        [("a","p"),("p","q"),("q","b")]
    ),
    (
        ["a","c","p","q","r","b"],
        {"a":0.0,"c":0.4,"b":2.0},
        [("a","p"),("c","q"),("p","r"),("q","r"),("r","b")]
    ),
    (
        ["a","c","p","q","r","s","b","d"],
        {"a":0.0,"c":0.5,"b":3.0,"d":2.4},
        [("a","p"),("c","q"),("p","r"),("q","r"),
         ("r","s"),("s","b"),("r","d")]
    ),
    (
        ["a","p","q","r","s","t","b"],
        {"a":-1.0,"b":2.5},
        [("a","p"),("a","q"),("p","r"),("q","r"),
         ("r","s"),("r","t"),("s","b"),("t","b")]
    ),
]

for j,(nodes,marks,covers) in enumerate(cases,1):
    assert check_regular(nodes,marks,covers)
    rf,vals=formula(nodes,marks,covers)
    rl,z,Uvars=lp(nodes,marks,covers)
    assert abs(rf-rl) <= 5e-8*max(1.0,abs(rf)),(j,rf,rl,vals)
    L,U=envelopes(nodes,marks,covers,rf)
    for u,v in covers:
        ew=1.0 if ((u in marks) ^ (v in marks)) else SQ2
        lv=marks[v] if v in marks else L[v]
        lu=marks[u] if u in marks else L[u]
        uv=marks[v] if v in marks else U[v]
        uu=marks[u] if u in marks else U[u]
        assert lv-lu >= rf*ew-2e-9
        assert uv-uu >= rf*ew-2e-9
    for u in Uvars:
        assert L[u] <= U[u]+2e-9

print(f"VERIFY_OK marked-order-inradius cases={len(cases)} active_set_lp=yes")
