from itertools import combinations

def add(u,v,p):
    return tuple((a+b)%p for a,b in zip(u,v))

def neg(u,p):
    return tuple((-a)%p for a in u)

def sub(u,v,p):
    return tuple((a-b)%p for a,b in zip(u,v))

def scal(a,u,p):
    return tuple((a*x)%p for x in u)

def rank(vectors,p):
    if not vectors:
        return 0
    A=[list(v) for v in vectors if any(v)]
    if not A:
        return 0
    m=len(A); n=len(A[0]); r=0
    for c in range(n):
        piv=next((i for i in range(r,m) if A[i][c]%p),None)
        if piv is None:
            continue
        A[r],A[piv]=A[piv],A[r]
        z=pow(A[r][c],-1,p)
        A[r]=[(z*x)%p for x in A[r]]
        for i in range(m):
            if i!=r and A[i][c]%p:
                z=A[i][c]%p
                A[i]=[(A[i][j]-z*A[r][j])%p for j in range(n)]
        r+=1
        if r==m:
            break
    return r

def vectors(p,t):
    out=[]
    def rec(a):
        if len(a)==t:
            out.append(tuple(a)); return
        for x in range(p):
            rec(a+[x])
    rec([])
    return out

def group(p,t):
    V=vectors(p,t)
    elems=[(v,e) for v in V for e in (0,1)]
    z=(0,)*t
    one=(z,0)
    def mul(x,y):
        v,e=x; w,f=y
        ww=w if e==0 else neg(w,p)
        return (add(v,ww,p),(e+f)%2)
    def inv(x):
        v,e=x
        if e==0:
            return (neg(v,p),0)
        return x
    return V,elems,one,mul,inv

def closure(gens,one,mul,inv):
    seen={one}
    frontier=[one]
    steps=list(gens)+[inv(g) for g in gens]
    while frontier:
        x=frontier.pop()
        for g in steps:
            y=mul(x,g)
            if y not in seen:
                seen.add(y)
                frontier.append(y)
    return seen

def pred_adj(x,y,p,t):
    if x==y:
        return False
    vx,ex=x; vy,ey=y
    z=(0,)*t
    if ex==0 and ey==0:
        return rank([vx,vy],p)==2
    if ex!=ey:
        u=vx if ex==0 else vy
        return u!=z
    return vx!=vy

def pred_degree(x,p,t):
    v,e=x
    z=(0,)*t
    if e==0 and v==z:
        return 0
    if e==0:
        return 2*(p**t)-p
    return 2*(p**t)-2

def exhaustive_rank_two(p):
    t=2
    V,E,one,mul,inv=group(p,t)
    edge=set()
    gen_count=0
    for S in combinations(E,t+1):
        if len(closure(S,one,mul,inv))==len(E):
            gen_count+=1
            for a,b in combinations(S,2):
                edge.add(frozenset((a,b)))
    for a,b in combinations(E,2):
        got=frozenset((a,b)) in edge
        want=pred_adj(a,b,p,t)
        assert got==want,(p,a,b,got,want)
    deg={x:0 for x in E}
    for ab in edge:
        a,b=tuple(ab)
        deg[a]+=1; deg[b]+=1
    for x in E:
        assert deg[x]==pred_degree(x,p,t),(p,x,deg[x],pred_degree(x,p,t))
        order=1 if x==one else (p if x[1]==0 else 2)
        assert deg[x]%order==0
    return gen_count, sorted(deg.values())

def extend_basis(seed,p,t):
    basis=[v for v in seed if any(v)]
    assert rank(basis,p)==len(basis)
    for e in [tuple(1 if i==j else 0 for i in range(t)) for j in range(t)]:
        if rank(basis+[e],p)>len(basis):
            basis.append(e)
        if len(basis)==t:
            break
    assert len(basis)==t
    return basis

def witness_pair(a,b,p,t):
    va,ea=a; vb,eb=b
    assert pred_adj(a,b,p,t)
    z=(0,)*t
    if ea==0 and eb==0:
        B=extend_basis([va,vb],p,t)
        extra=[(v,0) for v in B[2:]]+[(z,1)]
    elif ea!=eb:
        u=va if ea==0 else vb
        B=extend_basis([u],p,t)
        extra=[(v,0) for v in B[1:]]
    else:
        d=sub(va,vb,p)
        B=extend_basis([d],p,t)
        extra=[(v,0) for v in B[1:]]
    S=[a,b]+extra
    assert len(S)==t+1
    return S

def witness_check(p,t):
    V,E,one,mul,inv=group(p,t)
    predicted=set()
    for a,b in combinations(E,2):
        if pred_adj(a,b,p,t):
            predicted.add(frozenset((a,b)))
            S=witness_pair(a,b,p,t)
            assert len(closure(S,one,mul,inv))==len(E),(a,b,S)
    deg={x:0 for x in E}
    for ab in predicted:
        a,b=tuple(ab)
        deg[a]+=1; deg[b]+=1
    for x in E:
        assert deg[x]==pred_degree(x,p,t),(x,deg[x],pred_degree(x,p,t))
        order=1 if x==one else (p if x[1]==0 else 2)
        assert deg[x]%order==0
    return len(predicted), sorted(deg.values())

n3,d3=exhaustive_rank_two(3)
n5,d5=exhaustive_rank_two(5)
assert n3==504
assert n5==14000
assert d3==[0]+[15]*8+[16]*9
assert d5==[0]+[45]*24+[48]*25

e33,d33=witness_check(3,3)
assert e33==1365
assert d33==[0]+[51]*26+[52]*27

print("VERIFY_OK")
print("p=3,t=2 generating_sets",n3)
print("p=5,t=2 generating_sets",n5)
print("p=3,t=3 predicted_edges",e33)
