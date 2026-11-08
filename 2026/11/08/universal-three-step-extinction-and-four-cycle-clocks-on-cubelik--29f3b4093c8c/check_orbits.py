"""Independent labelled-state dynamical enumeration on connected cubelike line graphs."""
from collections import Counter


def edges_of_cayley(dim,generators):
    vertices=range(1<<dim)
    return sorted({tuple(sorted((x,x^step))) for x in vertices for step in generators})


def make_map(edges):
    near=[0]*len(edges)
    for i,e in enumerate(edges):
        for j,f in enumerate(edges):
            if i!=j and (e[0] in f or e[1] in f):
                near[i]|=1<<j
    def update(state):
        result=0
        for i,mask in enumerate(near):
            if (state & mask).bit_count() & 1:
                result|=1<<i
        return result
    return update


def case(dim,gens):
    edges=edges_of_cayley(dim,gens)
    u=make_map(edges)
    m=len(edges)
    n=1<<dim
    assert m<=16
    assert __import__('functools').reduce(int.__xor__,gens)!=0
    expected=[1,(1<<(m-n+2))-1,(1<<(m-n//2+2))-(1<<(m-n+2)),(1<<m)-(1<<(m-n//2+2))]
    extinct=Counter()
    periodic=Counter()
    for z in range(1<<m):
        a=z
        if a==0:depth=0
        else:
            depth=0
            while a!=0 and depth<4:
                depth+=1
                a=u(a)
            assert a==0
        extinct[depth]+=1
        b=z
        if b^(u(b))==b:per=1
        else:
            v=b^u(b)
            w=v^u(v)
            if w==b:per=2
            else:
                v=w^u(w)
                w=v^u(v)
                assert w==b
                per=4
        periodic[per]+=1
    assert [extinct[j] for j in range(4)]==expected,(dim,gens,extinct,expected)
    assert [periodic.get(j,0) for j in (1,2,4)]==[sum(expected[:2]),expected[2],expected[3]]
    return (dim, len(gens), m, expected,[periodic.get(j,0) for j in (1,2,4)])

if __name__=='__main__':
    for d,s in [(2,[1,2]),(3,[1,2,4]),(3,[1,2,4,3]),(3,[1,2,4,5])]:
        print('CASE',case(d,s))
    # An excluded generating-set instance witnesses the sharpness of the nonzero-sum rank formula.
    edges=edges_of_cayley(3,[1,2,4,7])
    u=make_map(edges)
    assert len(edges)==16
    assert all(u(u(k))==0 for k in range(1<<16))
    print('BOUNDARY_OK: folded four-cube K4,4 has second-step extinction; violates asserted three-step Jordan rank')
    print('ORBITS_OK')
