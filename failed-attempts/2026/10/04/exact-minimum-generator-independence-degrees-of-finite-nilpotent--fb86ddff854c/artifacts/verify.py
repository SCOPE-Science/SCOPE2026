from itertools import product

class Group:
    def __init__(self, factors, name, info):
        self.factors=factors
        self.name=name
        self.info=info
        self.elems=tuple(product(*[f["elems"] for f in factors]))
        self.e=tuple(f["e"] for f in factors)
        self.invmap={}
        for x in self.elems:
            for y in self.elems:
                if self.mul(x,y)==self.e and self.mul(y,x)==self.e:
                    self.invmap[x]=y
                    break
            assert x in self.invmap

    def mul(self,a,b):
        return tuple(f["mul"](x,y) for f,x,y in zip(self.factors,a,b))

    def generated(self, gens):
        H={self.e}
        changed=True
        for g in gens:
            H.add(g)
            H.add(self.invmap[g])
        while changed:
            changed=False
            cur=list(H)
            for a in cur:
                for b in cur:
                    c=self.mul(a,b)
                    if c not in H:
                        H.add(c)
                        H.add(self.invmap[c])
                        changed=True
        return frozenset(H)

    def order(self,g):
        x=self.e
        for k in range(1,len(self.elems)+1):
            x=self.mul(x,g)
            if x==self.e:
                return k
        raise AssertionError("order bound")

def cyclic(n):
    return {
        "elems":tuple(range(n)),
        "e":0,
        "mul":lambda a,b:(a+b)%n,
    }

def elementary(p,r):
    return {
        "elems":tuple(product(range(p),repeat=r)),
        "e":(0,)*r,
        "mul":lambda a,b:tuple((x+y)%p for x,y in zip(a,b)),
    }

def d8():
    elems=tuple(product(range(4),range(2)))
    def mul(x,y):
        i,j=x
        k,l=y
        return ((i+(k if j==0 else -k))%4,(j+l)%2)
    return {"elems":elems,"e":(0,0),"mul":mul}

def predicted_degree(G,g):
    d=max(v["d"] for v in G.info.values())
    phi=1
    qcount=1
    for p,v in G.info.items():
        phi*=v["phi_order"]
        dp=v["d"]
        inside=v["in_phi"](v["component"](g))
        if dp==d:
            if inside:
                return 0
            qcount*=p**d-p
        elif dp==d-1:
            qcount*=p**(d-1)-(1 if inside else 0)
        else:
            qcount*=p**dp
    return phi*qcount

groups=[
    Group(
        [elementary(2,2),cyclic(3)],
        "C2^2 x C3",
        {
            2:{"d":2,"phi_order":1,"component":lambda g:g[0],"in_phi":lambda x:x==(0,0)},
            3:{"d":1,"phi_order":1,"component":lambda g:g[1],"in_phi":lambda x:x==0},
        },
    ),
    Group(
        [d8(),cyclic(3)],
        "D8 x C3",
        {
            2:{"d":2,"phi_order":2,"component":lambda g:g[0],"in_phi":lambda x:x in {(0,0),(2,0)}},
            3:{"d":1,"phi_order":1,"component":lambda g:g[1],"in_phi":lambda x:x==0},
        },
    ),
    Group(
        [d8(),elementary(3,2)],
        "D8 x C3^2",
        {
            2:{"d":2,"phi_order":2,"component":lambda g:g[0],"in_phi":lambda x:x in {(0,0),(2,0)}},
            3:{"d":2,"phi_order":1,"component":lambda g:g[1],"in_phi":lambda x:x==(0,0)},
        },
    ),
    Group(
        [cyclic(4),cyclic(2),cyclic(3)],
        "C4 x C2 x C3",
        {
            2:{"d":2,"phi_order":2,"component":lambda g:(g[0],g[1]),"in_phi":lambda x:x in {(0,0),(2,0)}},
            3:{"d":1,"phi_order":1,"component":lambda g:g[2],"in_phi":lambda x:x==0},
        },
    ),
]

for G in groups:
    whole=frozenset(G.elems)
    for g in G.elems:
        actual=sum(
            1
            for h in G.elems
            if h!=g and G.generated([g,h])==whole
        )
        expected=predicted_degree(G,g)
        assert actual==expected,(G.name,g,actual,expected)
        assert actual % G.order(g)==0,(G.name,g,G.order(g),actual)

# Independent quotient-completion check at d=3.
def rank_mod(vectors,p):
    A=[list(v) for v in vectors if any(x%p for x in v)]
    if not A:
        return 0
    m=len(A)
    n=len(A[0])
    r=0
    c=0
    while r<m and c<n:
        pivot=next((i for i in range(r,m) if A[i][c]%p),None)
        if pivot is None:
            c+=1
            continue
        A[r],A[pivot]=A[pivot],A[r]
        inv=pow(A[r][c]%p,-1,p)
        A[r]=[(inv*x)%p for x in A[r]]
        for i in range(m):
            if i!=r and A[i][c]%p:
                t=A[i][c]%p
                A[i]=[(x-t*y)%p for x,y in zip(A[i],A[r])]
        r+=1
        c+=1
    return r

V2=list(product(range(2),repeat=3))
V3=list(product(range(3),repeat=2))
Q=list(product(V2,V3))

def can_complete(g,h):
    for z in Q:
        if rank_mod([g[0],h[0],z[0]],2)==3 and rank_mod([g[1],h[1],z[1]],3)==2:
            return True
    return False

def predicted_q_degree(g):
    if g[0]==(0,0,0):
        return 0
    factor2=2**3-2
    factor3=3**2 if g[1]!=(0,0) else 3**2-1
    return factor2*factor3

for g in Q:
    actual=sum(1 for h in Q if h!=g and can_complete(g,h))
    expected=predicted_q_degree(g)
    assert actual==expected,(g,actual,expected)

print("VERIFY_OK")
