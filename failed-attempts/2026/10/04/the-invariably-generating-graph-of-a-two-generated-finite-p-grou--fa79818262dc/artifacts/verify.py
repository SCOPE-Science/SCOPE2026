from itertools import product
from collections import deque

class Group:
    def __init__(self, elems, mul, e, name, p):
        self.elems = tuple(elems)
        self.mul = mul
        self.e = e
        self.name = name
        self.p = p
        self.inv = {}
        for x in self.elems:
            for y in self.elems:
                if mul(x,y)==e and mul(y,x)==e:
                    self.inv[x]=y
                    break
            assert x in self.inv

    def gen(self, gens):
        H={self.e}
        q=deque(gens)
        while q:
            x=q.popleft()
            if x in H: continue
            old=list(H)
            H.add(x)
            H.add(self.inv[x])
            cur=list(H)
            for a in cur:
                for b in cur:
                    z=self.mul(a,b)
                    if z not in H:
                        q.append(z)
            for a in old:
                for b in (x,self.inv[x]):
                    q.append(self.mul(a,b)); q.append(self.mul(b,a))
        changed=True
        while changed:
            changed=False
            cur=list(H)
            for a in cur:
                for b in cur:
                    z=self.mul(a,b)
                    if z not in H:
                        H.add(z); H.add(self.inv[z]); changed=True
        return frozenset(H)

    def subgroups(self):
        seen={frozenset({self.e})}
        q=deque(seen)
        while q:
            H=q.popleft()
            for x in self.elems:
                if x not in H:
                    K=self.gen(list(H)+[x])
                    if K not in seen:
                        seen.add(K); q.append(K)
        return list(seen)

    def conjugacy_classes(self):
        rem=set(self.elems); out=[]
        while rem:
            x=next(iter(rem))
            C=frozenset(self.mul(self.mul(self.inv[g],x),g) for g in self.elems)
            out.append(C); rem-=C
        return out

def cyclic_product(m,n,p,name):
    E=[(a,b) for a in range(m) for b in range(n)]
    return Group(E, lambda x,y:((x[0]+y[0])%m,(x[1]+y[1])%n),(0,0),name,p)

def dihedral8():
    E=[(i,j) for i in range(4) for j in range(2)]
    def mul(x,y):
        i,j=x; k,l=y
        return ((i + (k if j==0 else -k))%4,(j+l)%2)
    return Group(E,mul,(0,0),"D8",2)

def heisenberg3():
    E=[(a,b,c) for a in range(3) for b in range(3) for c in range(3)]
    def mul(x,y):
        a,b,c=x; u,v,w=y
        return ((a+u)%3,(b+v)%3,(c+w+a*v)%3)
    return Group(E,mul,(0,0,0),"H3",3)

def check(G):
    subs=G.subgroups()
    whole=frozenset(G.elems)
    proper=[H for H in subs if H!=whole]
    maximals=[]
    for H in proper:
        if not any(H < K < whole for K in subs):
            maximals.append(H)
    assert len(maximals)==G.p+1,(G.name,len(maximals))

    Phi=set(G.elems)
    for M in maximals:
        Phi &= set(M)
    Phi=frozenset(Phi)
    assert len(G.elems)//len(Phi)==G.p**2,(G.name,len(Phi))

    classes=[C for C in G.conjugacy_classes() if C != frozenset({G.e})]

    def invariably(C,D):
        for x in C:
            for y in D:
                if G.gen([x,y]) != whole:
                    return False
        return True

    adj={}
    for i,C in enumerate(classes):
        for j,D in enumerate(classes):
            adj[(i,j)] = (i!=j and invariably(C,D))

    iso={i for i,C in enumerate(classes) if not any(adj[(i,j)] for j in range(len(classes)))}
    expected_iso={i for i,C in enumerate(classes) if C.issubset(Phi)}
    assert iso==expected_iso,(G.name,iso,expected_iso)

    noniso=[i for i in range(len(classes)) if i not in iso]
    label={}
    for i in noniso:
        C=classes[i]
        x=next(iter(C))
        containing=[k for k,M in enumerate(maximals) if x in M]
        assert len(containing)==1,(G.name,C,containing)
        label[i]=containing[0]
        # maximal subgroups are normal, hence whole class stays in the same part
        assert C.issubset(maximals[containing[0]])

    parts={k:[i for i in noniso if label[i]==k] for k in range(len(maximals))}
    assert all(parts[k] for k in parts)
    assert all(len(parts[k])>=G.p-1 for k in parts)

    for i in noniso:
        for j in noniso:
            want=(i!=j and label[i]!=label[j])
            assert adj[(i,j)]==want,(G.name,i,j,adj[(i,j)],want)

    return {
        "name":G.name,
        "order":len(G.elems),
        "phi_order":len(Phi),
        "class_count":len(classes)+1,
        "isolated_nonidentity_classes":len(iso),
        "part_sizes":sorted(len(v) for v in parts.values()),
    }

groups=[
    dihedral8(),
    cyclic_product(4,4,2,"C4xC4"),
    cyclic_product(9,3,3,"C9xC3"),
    heisenberg3(),
]
rows=[check(G) for G in groups]
assert rows[0]["part_sizes"]==[1,1,1]
assert rows[1]["part_sizes"]==[4,4,4]
assert rows[2]["part_sizes"]==[6,6,6,6]
assert rows[3]["part_sizes"]==[2,2,2,2]
print("VERIFY_OK")
for row in rows:
    print(row)
