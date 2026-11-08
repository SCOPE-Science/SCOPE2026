"""Exact finite checks of a triangular-ring commuting-graph independence polynomial.

Run with Python >=3.9: python verify.py
All rings and the graph are constructed directly from multiplication tables.
"""
from math import gcd, comb

class FiniteRing:
    def __init__(self, name, size, add, mul, one):
        self.name, self.size, self.add, self.mul, self.one = name, size, add, mul, one
        self.elements = tuple(range(size))
        self.zero = 0


def zn(n):
    return FiniteRing(f"Z/{n}", n, lambda a,b:(a+b)%n,
                      lambda a,b:(a*b)%n, 1)


def dual(p):
    # Encodes a+b*t by a+p*b, with t^2=0; p prime.
    def add(a,b): return ((a%p+b%p)%p)+p*((a//p+b//p)%p)
    def mul(a,b): return ((a%p)*(b%p))%p + p*(((a%p)*(b//p)+(a//p)*(b%p))%p)
    return FiniteRing(f"F_{p}[t]/t^2",p*p,add,mul,1)


def neg(r,a):
    return next(b for b in r.elements if r.add(a,b)==0)


def det(r,v,w):
    return r.add(r.mul(v[0],w[1]),neg(r,r.mul(v[1],w[0])))


def ring_data(r):
    vec=[(a,b) for a in r.elements for b in r.elements if (a,b)!=(0,0)]
    units={a for a in r.elements if any(r.mul(a,b)==r.one for b in r.elements)}
    primitive=lambda v:any(r.add(r.mul(a,v[0]),r.mul(b,v[1]))==r.one
                           for a in r.elements for b in r.elements)
    lines={frozenset((r.mul(a,u),r.mul(a,v)) for a in r.elements)
           for u,v in vec if primitive((u,v))}
    lines=list(lines)
    for v in vec:
        appearances=sum(v in line for line in lines)
        assert appearances>=1, (r.name,v,appearances)
        assert (appearances==1)==primitive(v),(r.name,v,appearances)
    for i,line in enumerate(lines):
        points=[v for v in line if v!=(0,0)]
        assert all(det(r,u,v)==0 for u in points for v in points)
        for other in lines[i+1:]:
            pu=next(u for u in line if primitive(u))
            pv=next(v for v in other if primitive(v))
            assert det(r,pu,pv)!=0
    unit_count=len(units)
    assert all(sum(primitive(v) for v in line)==unit_count for line in lines)
    assert len(lines)*unit_count==sum(primitive(v) for v in vec)
    return vec, lines, primitive, unit_count


def coeff_closed(r,q):
    Q=q*q; U=Q-q; P=q*(q+1)
    out=[0]*(P+1)
    for k in range(P+1): out[k]+=comb(P,k)*(Q*U)**k
    for k in range(P-q+1): out[k+1]+=(Q-1)*Q*comb(P-q,k)*(Q*U)**k
    return out


def enumerate_independent_sets(r,vec):
    # Each matrix fiber has |R| scalar lifts; weight |R|^k per compatible vector set.
    sizes=[0]*(len(vec)+1)
    selected=[]
    def rec(i):
        if i==len(vec):
            sizes[len(selected)]+=r.size**len(selected)
            return
        rec(i+1)
        if all(det(r,vec[i],vec[j])!=0 for j in selected):
            selected.append(i); rec(i+1);selected.pop()
    rec(0)
    while sizes[-1]==0:sizes.pop()
    return sizes


def check_length_two(r,q,exhaustive):
    vec,lines,prim,U=ring_data(r)
    Q=q*q;P=q*(q+1)
    assert r.size==Q
    assert U==Q-q
    assert len(lines)==P
    nonprim=[v for v in vec if not prim(v)]
    assert len(nonprim)==Q-1
    assert all(det(r,u,v)==0 for u in nonprim for v in nonprim)
    # Every nonprimitive vector excludes exactly q projective lines.
    for v in nonprim:
        bad=[line for line in lines if any(det(r,v,u)==0 for u in line if prim(u))]
        assert len(bad)==q,(r.name,v,len(bad))
    expected=coeff_closed(r,q)
    assert expected[1]==Q**3-Q
    assert len(expected)==P+1
    assert expected[-1]==(Q*U)**P
    if exhaustive:
        actual=enumerate_independent_sets(r,vec)
        assert actual==expected, (r.name,actual,expected)
        print('EXHAUSTIVE',r.name,'vertices',Q**3-Q,'sets',sum(actual),'alpha',P,
              'maximal_count',actual[-1])
    else:
        print('STRUCTURAL',r.name,'vertices',Q**3-Q,'alpha',P,
              'maximal_count',expected[-1])


def main():
    for r,q in [(zn(4),2),(dual(2),2),(zn(9),3),(dual(3),3)]:
        check_length_two(r,q,r.size<=4)
    for r in (zn(2),zn(3)):
        v,L,pr,U=ring_data(r)
        expected=[comb(len(L),k)*(r.size*U)**k for k in range(len(L)+1)]
        assert enumerate_independent_sets(r,v)==expected
        print('FIELD',r.name,'alpha',len(L),'maximal_count',expected[-1])
    print('VERIFY_OK')

if __name__=='__main__':main()
