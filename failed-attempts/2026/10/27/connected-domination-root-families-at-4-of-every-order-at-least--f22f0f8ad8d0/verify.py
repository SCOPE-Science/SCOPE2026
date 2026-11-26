from collections import defaultdict
E='''0-1 0-3 0-4 0-12 1-2 1-12 1-18 2-3 2-6 2-8 2-10 2-18 2-21 3-21 3-24 4-5 6-7 8-9 10-11 12-13 12-14 12-15 12-16 12-17 18-19 18-20 21-22 21-23 24-25 24-26 26-27 27-28 28-29 28-31 29-30 31-32'''
edges=[tuple(map(int,e.split('-'))) for e in E.split()]
N=[set() for i in range(33)]
for a,b in edges:N[a].add(b);N[b].add(a)

def order_elim(scopes):
    scopes=set(map(frozenset,scopes)); order=[]; mx=0
    while scopes:
        vs=set().union(*scopes)
        v=min(vs,key=lambda z: (len(set().union(*(f for f in scopes if z in f))),sum(len(f) for f in scopes if z in f)))
        related={f for f in scopes if v in f}; new=set().union(*related)-{v}
        mx=max(mx,len(new)+1)
        scopes.difference_update(related)
        if new:scopes.add(frozenset(new))
        order.append(v)
    return order,mx

scopes=[{i} for i in range(33)]+[{i}|N[i] for i in range(33)]


class F:
    def __init__(self,s,v):self.s=tuple(sorted(s));self.v=v

def expr_sum(x,root=None):
    fs=[]
    for i in range(33):
        fs.append(F((i,),[1,x]))
        s=tuple(sorted({i}|N[i]));n=len(s)
        if i==root:
            fs.append(F(s,[1 if j==0 else 0 for j in range(1<<n)]))
        else:
            fs.append(F(s,[1 if j else 0 for j in range(1<<n)]))
    order,_=order_elim([set(f.s) for f in fs])
    for v in order:
        rel=[f for f in fs if v in f.s];fs=[f for f in fs if v not in f.s]
        u=tuple(sorted(set().union(*(f.s for f in rel))))
        without=tuple(z for z in u if z!=v)
        pos={z:i for i,z in enumerate(u)}
        u2mask=[]
        for f in rel:
            posf=[pos[z] for z in f.s]
            u2mask.append([sum((a>>i&1)<<j for j,i in enumerate(posf)) for a in range(1<<len(u))])
        prod=[]
        for a in range(1<<len(u)):
            p=1
            for f,ms in zip(rel,u2mask):p*=f.v[ms[a]]
            prod.append(p)
        pv=pos[v]
        vals=[]
        for a in range(1<<len(without)):
            l=sum((a>>i&1)<<pos[z] for i,z in enumerate(without))
            vals.append(prod[l]+prod[l|(1<<pv)])
        fs.append(F(without,vals))
    ans=1
    for f in fs:
        assert not f.s
        ans*=f.v[0]
    return ans


COEFF = {11:288,12:5664,13:52522,14:305133,15:1244812,16:3790459,
17:8945790,18:16782136,19:25467963,20:31644123,21:32441211,
22:27555245,23:19412673,24:11324236,25:5445556,26:2142406,
27:681729,28:172534,29:33879,30:4970,31:512,32:33,33:1}

def polynomial(x):
    return sum(c*x**k for k,c in COEFF.items())

def dominates(edges, n, mask):
    adj=[1<<i for i in range(n)]
    for u,v in edges:
        adj[u] |= 1<<v
        adj[v] |= 1<<u
    return all((mask&adj[i]) for i in range(n))

def direct_polynomial(edges,n,x):
    return sum(x**mask.bit_count() for mask in range(1<<n) if dominates(edges,n,mask))

def check():
    assert len(edges)==36 and len(N)==33 and 5 in N[4] and N[5]=={4}
    # 34 evaluations establish equality of two polynomials of degree at most 33.
    for x in [-4]+list(range(33)):
        actual=expr_sum(x)
        expected=polynomial(x)
        assert actual==expected, (x,actual,expected)
    assert polynomial(-4)==0
    derivative=sum(k*c*(-4)**(k-1) for k,c in COEFF.items())
    assert derivative != 0
    # Cross-bridge test: P3 (support center 1) bridged to K2 (support 3, leaf 4)
    e=[(0,1),(1,2),(3,4),(1,3)]
    for x in [-4,-1,0,1,2]:
        assert direct_polynomial(e,5,x)==(x*(x*x+3*x+1))*(x*(x+2))
    print('verified: full 33-vertex polynomial, simple root at -4, and bridge identity')
    print('derivative at -4:',derivative)

if __name__=='__main__':
    check()
