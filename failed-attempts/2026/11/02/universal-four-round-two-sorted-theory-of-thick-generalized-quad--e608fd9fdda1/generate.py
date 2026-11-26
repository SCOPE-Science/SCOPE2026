"""Construct four classical thick generalized quadrangle incidence structures.
The output format is n, number_of_points, edge_count; then point-line edges.
Only standard Python libraries are used.
"""
from itertools import product, combinations
from pathlib import Path

HERE=Path(__file__).resolve().parent

def save(name, np, nl, lines):
    edges=sorted((p,np+i) for i,line in enumerate(lines) for p in line)
    assert len(edges)==sum(map(len,lines))
    with (HERE/name).open('w', encoding='ascii') as f:
        f.write(f'{np+nl} {np} {len(edges)}\n')
        for x,y in edges:f.write(f'{x} {y}\n')
    return edges

def symplectic(q):
    def normalize(v):
        for x in v:
            if x:
                inv=pow(x,-1,q)
                return tuple((inv*y)%q for y in v)
        raise ValueError('zero vector')
    points=sorted({normalize(v) for v in product(range(q),repeat=4) if any(v)})
    idx={p:i for i,p in enumerate(points)}
    def orthogonal(u,v):
        return (u[0]*v[2]-u[2]*v[0]+u[1]*v[3]-u[3]*v[1])%q==0
    lines=set()
    for a,b in combinations(points,2):
        if not orthogonal(a,b):continue
        line=tuple(sorted({idx[normalize(tuple((x*a[i]+y*b[i])%q for i in range(4)))]
                           for x,y in product(range(q),repeat=2) if x or y}))
        assert len(line)==q+1
        lines.add(line)
    ls=sorted(lines)
    assert len(points)==len(ls)==q**3+q*q+q+1
    save(f'w{q}.txt',len(points),len(ls),ls)
    return len(points),len(ls)

def elliptic_binary():
    def Q(v):return (v[0]*v[1]+v[2]*v[3]+v[4]+v[4]*v[5]+v[5])%2
    points=[tuple(v) for v in product(range(2),repeat=6) if any(v) and Q(v)==0]
    idx={p:i for i,p in enumerate(points)}
    lines=set()
    for a,b in combinations(points,2):
        c=tuple(x^y for x,y in zip(a,b))
        if Q(c)==0:
            lines.add(tuple(sorted((idx[a],idx[b],idx[c]))))
    lines=sorted(lines)
    assert len(points)==27 and len(lines)==45
    save('qminus2.txt',27,45,lines)
    # Point-line dual: old lines are points, and old points are lines.
    dual_lines=[[] for _ in range(27)]
    for i,line in enumerate(lines):
        for p in line:dual_lines[p].append(i)
    assert all(len(z)==5 for z in dual_lines)
    save('qminus2dual.txt',45,27,dual_lines)
    return 27,45

if __name__=='__main__':
    print('SYMPLECTIC_QUADRANGLE_W2',symplectic(2))
    print('SYMPLECTIC_QUADRANGLE_W3',symplectic(3))
    print('ELLIPTIC_QUADRANGLE_QMINUS2',elliptic_binary())
    print('GEOMETRY_GENERATION_OK')
