"""Independent incidence and sharp-witness checks for critical excitation."""
from itertools import product

def field_mult(a, b, q):
    if q == 2:
        return a & b
    # Elements 0,1,z,1+z in GF(4), with z*z=z+1.
    x0, x1 = a & 1, (a >> 1) & 1
    y0, y1 = b & 1, (b >> 1) & 1
    return (x0*y0 ^ x1*y1) | ((x0*y1 ^ x1*y0 ^ x1*y1) << 1)

def projective_points(q):
    norm = set()
    for xyz in product(range(q), repeat=3):
        if xyz == (0,0,0):
            continue
        a = next(c for c in xyz if c)
        inv = next(u for u in range(1,q) if field_mult(a,u,q)==1)
        norm.add(tuple(field_mult(u,inv,q) for u in xyz))
    return sorted(norm)

def matrix(q):
    pts = projective_points(q)
    n = q*q + q + 1
    assert len(pts)==n
    out = []
    for p in pts:
        row=[]
        for line in pts:
            dot=0
            for a,b in zip(p,line): dot ^= field_mult(a,b,q)
            row.append(int(dot != 0))
        assert sum(row)==q*q
        out.append(row)
    for i in range(n):
        for j in range(n):
            common=sum(out[i][k]*out[j][k] for k in range(n))
            assert common==(q*q if i==j else q*(q-1)), (i,j,common)
    return pts,out

for q in (2,4):
    pts,nonincidence=matrix(q)
    print('projective_order',q,'points_lines',len(pts),'degree',q*q,
          'shared_nonincidences',q*(q-1),'nontrivial_gram_eigenvalue',q)

# Independent direct trajectory for the first sharp witness, using ternary digits.
start=82105
N=14
lines=[{(k+d)%7 for d in (0,1,3)} for k in range(7)]
neighbors=[[] for _ in range(N)]
for p in range(7):
    for k in range(7):
        if p not in lines[k]:
            neighbors[p].append(7+k)
            neighbors[7+k].append(p)
assert all(len(s)==4 for s in neighbors)
x=[];tmp=start
for i in range(N):
    x.append(tmp%3)
    tmp//=3
assert tmp==0
for t in range(8):
    print('witness_time',t,'digits',''.join(map(str,x)))
    if t<7:
        x=[(c+1)%3 if c else int(sum(x[u]==1 for u in neighbors[v])>=2)
           for v,c in enumerate(x)]
    if t<7: assert any(x) or t==6
assert x==[0]*N
