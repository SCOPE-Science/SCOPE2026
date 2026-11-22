"""Exact independent finite-field checks of the fourfold-contact conic theorem.

No third-party dependencies. Multiplication is performed directly in prime or
quadratic extension fields; tangent chords are tested by the dual conic form.
"""
from collections import Counter


class Field:
    def __init__(self, prime, nonsquare=None):
        self.p = prime
        self.nonsquare = nonsquare
        self.q = prime if nonsquare is None else prime * prime
        if nonsquare is not None:
            assert nonsquare % prime not in {(x*x)%prime for x in range(prime)}

    def add(self, a, b):
        p = self.p
        if self.nonsquare is None:
            return (a+b) % p
        return ((a%p+b%p) % p) + p*((a//p+b//p) % p)

    def neg(self, a):
        p = self.p
        if self.nonsquare is None:
            return (-a) % p
        return ((-a)%p) + p*((-(a//p))%p)

    def sub(self, a, b):
        return self.add(a, self.neg(b))

    def mul(self, a, b):
        p = self.p
        if self.nonsquare is None:
            return a*b % p
        x, y = a%p, a//p
        u, v = b%p, b//p
        return ((x*u+self.nonsquare*y*v)%p)+p*((x*v+y*u)%p)

    def prod(self, *args):
        ans = 1
        for a in args:
            ans = self.mul(ans, a)
        return ans

    def sum(self, *args):
        ans = 0
        for a in args:
            ans = self.add(ans, a)
        return ans

    def sq(self, a):
        return self.mul(a, a)


def cross(f, P, Q):
    return (f.sub(f.mul(P[1],Q[2]), f.mul(P[2],Q[1])),
            f.sub(f.mul(P[2],Q[0]), f.mul(P[0],Q[2])),
            f.sub(f.mul(P[0],Q[1]), f.mul(P[1],Q[0])))


def is_tangent(f, L, lam):
    # 4*adj(M) of D=XZ-Y^2+lam*X^2, evaluated on the line L.
    x,y,z=L
    return f.sub(f.sub(f.prod(4%f.p,x,z),f.sq(y)),
                 f.prod(4%f.p,lam,f.sq(z))) == 0


def components(graph):
    seen=set()
    result=[]
    for v in graph:
        if v in seen: continue
        block=[]; stack=[v]; seen.add(v)
        while stack:
            x=stack.pop(); block.append(x)
            for y in graph[x]:
                if y not in seen:
                    seen.add(y);stack.append(y)
        edges=sum(len(graph[x]) for x in block)//2
        result.append((len(block),edges))
    return Counter(result)


def verify_field(p, nonsquare=None, all_parameters=True):
    f=Field(p,nonsquare)
    q=f.q
    root_set={f.sq(x) for x in range(q)}
    vertices=list(range(q))+['contact']
    P={x:(1,x,f.sq(x)) for x in range(q)}
    P['contact']=(0,0,1)
    count_split=0
    values=range(1,q) if all_parameters else [1,2%p]
    for lam in values:
        assert lam
        graph={x:set() for x in vertices}
        for i,u in enumerate(vertices):
            for v in vertices[i+1:]:
                L=cross(f,P[u],P[v])
                assert L!=(0,0,0)
                if is_tangent(f,L,lam):
                    graph[u].add(v);graph[v].add(u)
        split=f.neg(lam) in root_set
        count_split+=int(split)
        expected=(Counter({(1,0):1,(p,p):q//p}) if split
                  else Counter({(1,0):q+1}))
        actual=components(graph)
        assert actual==expected,(p,nonsquare,lam,actual,expected)
        assert graph['contact']==set()
        if split:
            assert Counter(map(len,graph.values()))==Counter({2:q,0:1})
        else:
            assert all(not neighbors for neighbors in graph.values())
    if all_parameters:
        assert count_split==(q-1)//2
    return f"F_{q}: {len(list(values))} coefficients; {count_split} splitting cases; incidence graphs verified"


def det3(a,b,c,d,e,f):
    # determinant of twice the symmetric matrix of
    # a X²+b Y²+c Z²+d XY+e XZ+f YZ.
    return (8*a*b*c+2*d*e*f-2*a*f*f-2*b*e*e-2*c*d*d)


def count_smooth_conics(p):
    seen=set(); total=0
    from itertools import product
    for coeff in product(range(p),repeat=6):
        if not any(coeff):continue
        first=next(v for v in coeff if v)
        inv=pow(first,-1,p)
        norm=tuple((v*inv)%p for v in coeff)
        if norm in seen:continue
        seen.add(norm)
        if det3(*norm)%p:total+=1
    assert total==p*p*(p**3-1),(p,total)
    return f"F_{p}: {total} smooth conics"

if __name__=='__main__':
    for p in (3,5,7,11):
        print(verify_field(p))
    for p,d in ((3,2),(5,2),(7,3)):
        print(verify_field(p,d))
    for p in (3,5):
        print(count_smooth_conics(p))
    print('ALL EXACT CHECKS PASSED')
