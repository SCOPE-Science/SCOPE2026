"""Exact integral cell calculation for small diagonal cyclic cube-graph quotients.

Only Python 3 and SymPy are needed.  Every quotient cell is obtained by
explicitly enumerating rotations; no homological rank is assumed.
"""
from collections import Counter
from math import gcd
from sympy import Matrix, ZZ
from sympy.matrices.normalforms import smith_normal_form


def rotate(x, n, k):
    k %= n
    return ((x << k) | (x >> (n-k))) & ((1 << n)-1) if k else x


def vertex_orbit(x, y, n):
    return min((rotate(x,n,k),rotate(y,n,k)) for k in range(n))


def edge_orbit(edge, n):
    typ, i, x, y = edge
    return min((typ,(i+k)%n,rotate(x,n,k),rotate(y,n,k)) for k in range(n))


def square_orbit(sq, n):
    i,x,j,y = sq
    return min(((i+k)%n,rotate(x,n,k),(j+k)%n,rotate(y,n,k)) for k in range(n))


def cube_edges(n):
    for i in range(n):
        for x in range(1 << n):
            if x & (1 << i) == 0:
                yield (i,x)


def necklace(n,q):
    return sum(q**gcd(n,k) for k in range(n))//n


def check(n, integral):
    all_edges=list(cube_edges(n))
    verts=sorted({vertex_orbit(x,y,n) for x in range(1<<n) for y in range(1<<n)})
    horiz=sorted({edge_orbit(('H',i,x,y),n) for i,x in all_edges for y in range(1<<n)})
    vert=sorted({edge_orbit(('V',j,x,y),n) for j,y in all_edges for x in range(1<<n)})
    squares=sorted({square_orbit((i,x,j,y),n) for i,x in all_edges for j,y in all_edges})
    V,E,F=len(verts),len(horiz)+len(vert),len(squares)
    N2,N4=necklace(n,2),necklace(n,4)
    r=(1<<(n-1))-N2+1
    b2=(n-4)*4**(n-1)+N4-1+2*r
    assert (V,E,F)==(N4,4**n,n*4**(n-1))
    assert V-E+F==1-2*r+b2
    print(f'n={n}: (V,E,F)=({V},{E},{F}); expected H1 rank={2*r}, H2 rank={b2}')
    if not integral:
        return
    vi={v:i for i,v in enumerate(verts)}
    cells=horiz+vert
    ei={e:i for i,e in enumerate(cells)}
    def ends(e):
        typ,i,x,y=e
        return (vi[vertex_orbit(x,y,n)],
                vi[vertex_orbit(x+(1<<i),y,n)] if typ=='H' else
                vi[vertex_orbit(x,y+(1<<i),n)])
    endpoints=[ends(e) for e in cells]
    par=list(range(V))
    def root(x):
        while x!=par[x]:x=par[x]
        return x
    tree=set()
    for e,(a,b) in enumerate(endpoints):
        a,b=root(a),root(b)
        if a!=b:
            par[a]=b
            tree.add(e)
    assert len(tree)==V-1
    non_tree={edge:i for i,edge in enumerate(e for e in range(E) if e not in tree)}
    mat=[[0]*F for _ in range(E-V+1)]
    for c,(i,x,j,y) in enumerate(squares):
        boundary=((1,('V',j,x+(1<<i),y)),
                  (-1,('V',j,x,y)),
                  (-1,('H',i,x,y+(1<<j))),
                  (1,('H',i,x,y)))
        dd={}
        for s,e in boundary:
            eidx=ei[edge_orbit(e,n)]
            a,b=endpoints[eidx]
            dd[a]=dd.get(a,0)-s
            dd[b]=dd.get(b,0)+s
            if eidx in non_tree:mat[non_tree[eidx]][c]+=s
        assert all(v==0 for v in dd.values()),('boundary^2',n,c,dd)
    smith=smith_normal_form(Matrix(mat),domain=ZZ)
    diag=[abs(int(smith[k,k])) for k in range(min(smith.shape)) if smith[k,k]]
    tors=Counter(d for d in diag if d>1)
    assert E-V+1-len(diag)==2*r
    assert F-len(diag)==b2
    assert not tors
    print(f'  integral Smith factors: {len(diag)} unit factors; no torsion; d1*d2=0')


if __name__=='__main__':
    for n in (3,4,5,6):check(n,integral=n<=4)
    print('DIAGONAL_MOMENT_ANGLE_QUOTIENT_EXACT_PASS')
