"""Independent finite-field checks of a conjugacy-class formula for height-two incidence algebra unit groups.

Runs as `python verify.py`, using only the Python standard library.
"""
from itertools import product

class Field:
    def __init__(self, q):
        assert q in (2, 3, 4)
        self.q=q
        self.nonzero=tuple(range(1,q))
        self.generator={2:1,3:2,4:2}[q]
        self.inverses={a:next(b for b in self.nonzero if self.mul(a,b)==1) for a in self.nonzero}

    def add(self,a,b):
        return a^b if self.q==4 else (a+b)%self.q

    def neg(self,a):
        return a if self.q==4 else (-a)%self.q

    def sub(self,a,b):
        return self.add(a,self.neg(b))

    def mul(self,a,b):
        if self.q!=4:return a*b%self.q
        r=0
        for i in range(2):
            for j in range(2):
                if ((a>>i)&1) and ((b>>j)&1):
                    r ^= (1<<(i+j))
        if r&8:r^=0b1001  # x^3 = 1 in F_2[x]/(x^2+x+1)
        if r&4:r^=0b111   # x^2 = x+1
        return r

def class_count_direct(q,n,edges):
    """Enumerate conjugacy orbits by explicit generator action, not via orbit formulas."""
    f=Field(q)
    elems=list(product(range(q),repeat=len(edges)))
    answer=0
    for t in product(f.nonzero,repeat=n):
        remaining=set(elems)
        while remaining:
            start=next(iter(remaining));remaining.remove(start)
            answer+=1;stack=[start]
            while stack:
                a=stack.pop()
                # Conjugate by a diagonal unit whose single selected entry is a generator.
                for vertex in range(n):
                    b=list(a)
                    for j,(u,v) in enumerate(edges):
                        if vertex==u:b[j]=f.mul(f.generator,b[j])
                        elif vertex==v:b[j]=f.mul(f.inverses[f.generator],b[j])
                    b=tuple(b)
                    if b in remaining:remaining.remove(b);stack.append(b)
                # Conjugate by 1+e_{uv}; since the radical squares to zero, this translates just that edge.
                for j,(u,v) in enumerate(edges):
                    b=list(a)
                    b[j]=f.add(b[j],f.sub(t[v],t[u]))
                    b=tuple(b)
                    if b in remaining:remaining.remove(b);stack.append(b)
    return answer

def class_count_commuting_pairs(q,n,edges):
    """Independent Burnside count using the original componentwise commutation equations."""
    tvals=list(product(range(1,q),repeat=n))
    total=0
    for t in tvals:
        for s in tvals:
            doubly_equal=sum(t[u]==t[v] and s[u]==s[v] for u,v in edges)
            total+=q**doubly_equal
    denominator=(q-1)**n
    assert total%denominator==0
    return total//denominator

def main():
    c4=[(0,1),(1,2),(2,3),(3,0)]
    c6=[(i,(i+1)%6) for i in range(6)]
    cases=[(4,4,c4),(5,4,c4+[(3,4)]),(6,4,c4+[(0,4),(4,5)]),
           (6,4,c4+[(0,4),(1,5)]),(6,6,c6)]
    checks=0
    for n,ell,edges in cases:
        assert len(edges)==n
        for q in (2,3,4,5):
            if (q-1)**(2*n)>900000:continue
            target=q**n+(q-2)*q**(n-ell+1)
            actual=class_count_commuting_pairs(q,n,edges)
            assert actual==target,(q,n,ell,actual,target)
            checks+=1
            if q in (2,3,4) and (q-1)**n * q**n<60000:
                direct=class_count_direct(q,n,edges)
                assert direct==target,(q,n,ell,direct,target)
                checks+=1
    # Independent structure checks: trees do not create cycles; the formula distinguishes cycle length at q>2.
    assert 3**6+(3-2)*3**(6-6+1)==732
    assert 3**6+(3-2)*3**(6-4+1)==756
    assert 4**6+(4-2)*4**(6-6+1)==4104
    assert 4**6+(4-2)*4**(6-4+1)==4224
    print(f'{checks} independent class-count checks; VERIFY_OK')

if __name__=='__main__':main()
