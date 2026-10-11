from itertools import product, combinations

def mm(A,B,p):
    return tuple(tuple(sum(A[i][k]*B[k][j] for k in range(2))%p for j in range(2)) for i in range(2))

def mv(A,v,p):
    return tuple(sum(A[i][j]*v[j] for j in range(2))%p for i in range(2))

def mpow(A,n,p):
    R=((1,0),(0,1))
    while n:
        if n&1: R=mm(R,A,p)
        A=mm(A,A,p); n//=2
    return R

def make_group(p,M):
    powers=[mpow(M,j,p) for j in range(3)]
    assert mpow(M,3,p)==((1,0),(0,1)) and M!=((1,0),(0,1))
    V=list(product(range(p),repeat=2))
    G=[(v,j) for v in V for j in range(3)]
    e=((0,0),0)
    def add(a,b): return ((a[0]+b[0])%p,(a[1]+b[1])%p)
    def neg(a): return ((-a[0])%p,(-a[1])%p)
    def mul(x,y):
        v,i=x; w,j=y
        return (add(v,mv(powers[i],w,p)),(i+j)%3)
    def inv(x):
        v,i=x; j=(-i)%3
        return (mv(powers[j],neg(v),p),j)
    return G,e,mul,inv

def conjugacy_classes(G,mul,inv):
    unseen=set(G); out=[]
    while unseen:
        x=next(iter(unseen))
        C=frozenset(mul(mul(g,x),inv(g)) for g in G)
        out.append(C); unseen-=C
    return out

def order(x,e,mul):
    y=e
    for n in range(1,10000):
        y=mul(y,x)
        if y==e: return n
    raise AssertionError

def canonical_line(v,p):
    if v[0]:
        a=pow(v[0],-1,p)
        return (1,v[1]*a%p)
    return (0,1)

def check_prime(p):
    omega=next(a for a in range(2,p) if pow(a,3,p)==1 and a!=1)
    mats=[((omega,0),(0,omega)),((omega,0),(0,pow(omega,-1,p)))]
    signatures=[]
    invariant_counts=[]
    for M in mats:
        G,e,mul,inv=make_group(p,M)
        Cs=conjugacy_classes(G,mul,inv)
        trivial=next(C for C in Cs if e in C)
        verts=[C for C in Cs if C!=trivial]
        A=(p*p-1)//3
        assert len(verts)==A+2

        adj=set()
        for i,j in combinations(range(len(verts)),2):
            if any(mul(x,y)==mul(y,x) for x in verts[i] for y in verts[j]):
                adj.add((i,j))
        nb={i:set() for i in range(len(verts))}
        for i,j in adj: nb[i].add(j); nb[j].add(i)
        comps=[]; seen=set()
        for s in nb:
            if s in seen: continue
            stack=[s]; seen.add(s); C=set()
            while stack:
                u=stack.pop(); C.add(u)
                for v in nb[u]:
                    if v not in seen: seen.add(v); stack.append(v)
            comps.append(C)
        assert sorted(map(len,comps))==sorted([A,2])
        assert all(all((min(i,j),max(i,j)) in adj for i,j in combinations(C,2)) for C in comps)

        kernel=[]; outside=[]
        for i,C in enumerate(verts):
            js={x[1] for x in C}
            (kernel if js=={0} else outside).append(i)
        assert len(kernel)==A and len(outside)==2

        # Every mixed representative pair has coprime orders and fails to commute.
        # Such a pair cannot lie in a finite nilpotent subgroup.
        for i in kernel:
            for j in outside:
                for x in verts[i]:
                    assert order(x,e,mul)==p
                    for y in verts[j]:
                        assert order(y,e,mul)==3
                        assert mul(x,y)!=mul(y,x)

        # Every commutator lies in the abelian kernel, so the group is metabelian.
        for x in G:
            for y in G:
                comm=mul(mul(inv(x),inv(y)),mul(x,y))
                assert comm[1]==0

        signatures.append(tuple(sorted(map(len,comps))))

        lines={canonical_line(v,p) for v in product(range(p),repeat=2) if v!=(0,0)}
        c=0
        for v in lines:
            w=mv(M,v,p)
            if (v[0]*w[1]-v[1]*w[0])%p==0: c+=1
        invariant_counts.append(c)

    assert signatures[0]==signatures[1]==tuple(sorted([(p*p-1)//3,2]))
    assert invariant_counts==[p+1,2]
    print({'p':p,'component_sizes':signatures[0],'invariant_lines':invariant_counts})

for p in (7,13): check_prime(p)
print('VERIFY_OK')
