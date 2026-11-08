"""Reproducible integral chain and symmetry check for the 3-nonmatching
complex of K_(4,4). Python 3, standard library only.

A face is an edge subset admitting no matching of size three. Vertex
index 4*i+j denotes the edge joining row i to column j.
"""
from collections import Counter, defaultdict, deque
from itertools import combinations, permutations
from math import prod

SIZE = 4
EDGES = range(16)
PERMS = list(permutations(range(SIZE)))
FORBIDDEN = tuple(
    sum(1 << (SIZE*i+j) for i,j in zip(rows,cols))
    for rows in combinations(range(SIZE),3)
    for cols in permutations(range(SIZE),3)
)
FACES = {mask for mask in range(1<<16)
         if not any(mask & forbidden == forbidden for forbidden in FORBIDDEN)}
assert len(FORBIDDEN)==96
assert len(FACES)==3017
fvector=Counter(mask.bit_count() for mask in FACES)
assert dict(sorted(fvector.items())) == {0:1,1:16,2:120,3:464,4:932,5:912,6:448,7:112,8:12}

# Greedy element matching by 16 edge coordinates; this includes the
# empty face, hence computes reduced rather than unreduced homology.
remaining=set(FACES)
matched=[]
for bit in EDGES:
    for face in sorted(remaining):
        if face & (1<<bit):
            continue
        upper=face | (1<<bit)
        if upper in remaining:
            remaining.remove(face)
            remaining.remove(upper)
            matched.append((face,upper))
assert len(matched)==1504
assert len(remaining)==9 and all(f.bit_count()==4 for f in remaining)
critical=sorted(remaining)

# Entire directed Hasse graph: matched incidences point upwards,
# all other incidences point downwards; Kahn exhaustion certifies no cycle.
matched_set=set(matched)
links=defaultdict(list)
indeg={f:0 for f in FACES}
cover_count=0
for upper in FACES:
    for bit in EDGES:
        if not upper & (1<<bit):
            continue
        lower=upper^(1<<bit)
        assert lower in FACES
        source,target=(lower,upper) if (lower,upper) in matched_set else (upper,lower)
        links[source].append(target)
        indeg[target]+=1
        cover_count+=1
assert cover_count==13504
queue=deque(f for f in sorted(FACES) if indeg[f]==0)
visited=0
while queue:
    u=queue.popleft();visited+=1
    for v in links[u]:
        indeg[v]-=1
        if indeg[v]==0:queue.append(v)
assert visited==len(FACES)


def oriented_boundary(mask):
    verts=[v for v in EDGES if mask & (1<<v)]
    return {mask^(1<<v): -1 if pos%2 else 1
            for pos,v in enumerate(verts)}


def inversion_sign(seq):
    return -1 if sum(x>y for i,x in enumerate(seq) for y in seq[i+1:])%2 else 1


def sphere_cycle(I,J):
    """Fundamental integral S^3 cycle on alternating matchings of a C_6."""
    (i0,i1,i2),(j0,j1,j2)=I,J
    a=(4*i0+j0,4*i1+j1,4*i2+j2)
    b=(4*i0+j1,4*i1+j2,4*i2+j0)
    result={}
    for missing_a in range(3):
        for missing_b in range(3):
            edge_list=[a[k] for k in range(3) if k!=missing_a]
            edge_list +=[b[k] for k in range(3) if k!=missing_b]
            face=sum(1<<v for v in edge_list)
            coeff=(-1)**(missing_a+missing_b)*inversion_sign(edge_list)
            assert face in FACES and face not in result
            result[face]=coeff
    assert len(result)==9
    return result


def is_cycle(chain):
    boundary=defaultdict(int)
    for face,coeff in chain.items():
        for lower,sign in oriented_boundary(face).items():
            boundary[lower]+=coeff*sign
    return all(v==0 for v in boundary.values())

# Matchings of 3-faces to 4-faces are integral unit pivots in d_4.
# An acyclic elimination order on the matched lower 3-faces is generated
# from the coefficients of their paired 4-simplex boundaries.
low_up={a:b for a,b in matched if a.bit_count()==4}
assert len(low_up)==564
successors={a:[] for a in low_up}
deg={a:0 for a in low_up}
for a,b in low_up.items():
    for other in oriented_boundary(b):
        if other!=a and other in low_up:
            successors[a].append(other)
            deg[other]+=1
queue=deque(sorted(a for a in deg if deg[a]==0))
elim=[]
while queue:
    a=queue.popleft();elim.append(a)
    for other in successors[a]:
        deg[other]-=1
        if not deg[other]:queue.append(other)
assert len(elim)==len(low_up)


def project_to_critical(chain):
    chain=chain.copy()
    for lower in elim:
        coeff=chain.get(lower,0)
        if not coeff:continue
        bd=oriented_boundary(low_up[lower])
        factor=coeff*bd[lower]  # pivot is ±1
        for face,v in bd.items():
            after=chain.get(face,0)-factor*v
            if after:chain[face]=after
            else:chain.pop(face,None)
    assert not any(face in chain for face in low_up)
    return [chain.get(face,0) for face in critical]


TRIPLES=[(0,)+pair for pair in combinations((1,2,3),2)]
KEYS=[(I,J) for I in TRIPLES for J in TRIPLES]
CYCLES=[sphere_cycle(*key) for key in KEYS]
assert all(is_cycle(c) for c in CYCLES)
B=list(map(list,zip(*(project_to_critical(c) for c in CYCLES))))


def det_int(A):
    A=[row[:] for row in A]
    size=len(A)
    sign=1
    denominator=1
    for k in range(size-1):
        if A[k][k]==0:
            candidate=next((i for i in range(k+1,size) if A[i][k]),None)
            if candidate is None:return 0
            A[k],A[candidate]=A[candidate],A[k]
            sign=-sign
        pivot=A[k][k]
        for i in range(k+1,size):
            for j in range(k+1,size):
                numerator=A[i][j]*pivot-A[i][k]*A[k][j]
                assert numerator%denominator==0
                A[i][j]=numerator//denominator
            A[i][k]=0
        denominator=pivot
    return sign*A[-1][-1]
assert det_int(B)==-1

# For this ordered list of critical simplices, B is a NEGATIVE signed
# permutation matrix. Thus converting from Morse coordinates to the
# displayed nine sphere-basis coordinates uses a simple signed inverse.
assert all(sum(abs(v) for v in row)==1 for row in B)
assert all(sum(abs(B[i][j]) for i in range(9))==1 for j in range(9))

def basis_coordinates(z):
    y=project_to_critical(z)
    return [sum(B[i][j]*y[i] for i in range(9)) for j in range(9)]


def act_on_cycle(z,rowperm,colperm,transpose=False):
    result={}
    for mask,coeff in z.items():
        original=[v for v in EDGES if mask & (1<<v)]
        if transpose:
            moved=[4*colperm[v%4]+rowperm[v//4] for v in original]
        else:
            moved=[4*rowperm[v//4]+colperm[v%4] for v in original]
        face=sum(1<<v for v in moved)
        assert face in FACES
        result[face]=result.get(face,0)+coeff*inversion_sign(moved)
    return result


def triangle_representation(p):
    matrix=[[0]*3 for _ in range(3)]
    for column,I in enumerate(TRIPLES):
        image=[p[i] for i in I]
        sign=inversion_sign(image)
        order=tuple(sorted(image))
        if order==(1,2,3):
            coordinates=(1,-1,1) # boundary of tetrahedron relation
        else:
            coordinates=tuple(1 if TRIPLES[i]==order else 0 for i in range(3))
        for row,c in enumerate(coordinates):matrix[row][column]=sign*c
    return matrix


def tensor_representation(a,b):
    A=triangle_representation(a)
    B=triangle_representation(b)
    return [[A[i//3][j//3]*B[i%3][j%3] for j in range(9)]
            for i in range(9)]

# Check each of all 576 pairs of graph-part permutations on EACH of
# the nine integral sphere cycles, i.e., 5,184 chain actions.
checks=0
for p in PERMS:
    for q in PERMS:
        expected=tensor_representation(p,q)
        for col,z in enumerate(CYCLES):
            observed=basis_coordinates(act_on_cycle(z,p,q))
            assert all(observed[i]==expected[i][col] for i in range(9))
            checks+=1
assert checks==5184

# Transposition of the two graph parts is +tensor flip, not -flip.
for col,z in enumerate(CYCLES):
    row,col2=divmod(col,3)
    expected=[1 if i==col2*3+row else 0 for i in range(9)]
    got=basis_coordinates(act_on_cycle(z,tuple(range(4)),tuple(range(4)),transpose=True))
    assert got==expected

# Verify all 16 row/column triples agree with the oriented boundary
# model of wedge^2 of the augmentation lattice, including 4-term relations.
def triangle_vector(T):
    if 0 in T:return [1 if I==T else 0 for I in TRIPLES]
    assert T==(1,2,3)
    return [1,-1,1]
for I in combinations(range(4),3):
    for J in combinations(range(4),3):
        u,v=triangle_vector(I),triangle_vector(J)
        expected=[u[i//3]*v[i%3] for i in range(9)]
        assert basis_coordinates(sphere_cycle(I,J))==expected

# Independent signed simplicial Lefschetz check. For a permutation of
# edge-vertices, a fixed face is a union of complete orbits. Its signed
# contribution to the H_3 trace (homology concentrated in odd degree)
# is (-1)^(number of chosen edge-vertex orbits). Including the empty
# augmented face is essential. This is independent of the Morse matrices.
def lefschetz_h3(p,q,transpose):
    edgeperm=[4*q[v%4]+p[v//4] if transpose else
              4*p[v//4]+q[v%4] for v in EDGES]
    visited=set()
    orbits=[]
    for v in EDGES:
        if v in visited:continue
        x=v;orb=0
        while x not in visited:
            visited.add(x);orb|=1<<x;x=edgeperm[x]
        orbits.append(orb)
    total=0
    for selector in range(1<<len(orbits)):
        face=0
        for i,orb in enumerate(orbits):
            if selector>>i&1:face |= orb
        if face in FACES:total += (-1)**selector.bit_count()
    return total

lefschetz_checks=0
for p in PERMS:
    A=triangle_representation(p)
    for q in PERMS:
        Q=triangle_representation(q)
        actual=lefschetz_h3(p,q,False)
        expected=sum(A[i][i] for i in range(3))*sum(Q[i][i] for i in range(3))
        assert actual==expected
        actual=lefschetz_h3(p,q,True)
        expected=sum(A[i][j]*Q[j][i] for i in range(3) for j in range(3))
        assert actual==expected
        lefschetz_checks+=2
assert lefschetz_checks==1152

# Character on S4 conjugacy types of wedge^2 L4; the tensor and swap
# formulas follow from the concrete action matrices verified above.
trace_by_cycle_type={}
for p in PERMS:
    seen=set();partition=[]
    for i in range(4):
        if i in seen:continue
        j=i;order=0
        while j not in seen:
            seen.add(j);order+=1;j=p[j]
        partition.append(order)
    key=tuple(sorted(partition,reverse=True))
    rep=triangle_representation(p)
    tr=sum(rep[i][i] for i in range(3))
    trace_by_cycle_type.setdefault(key,tr)
    assert trace_by_cycle_type[key]==tr
assert trace_by_cycle_type=={(1,1,1,1):3,(2,1,1):-1,(2,2):-1,(3,1):0,(4,):1}

print('BNM3_K44_INTEGRAL_SYMMETRY_PASS')
print('faces',len(FACES),'Hasse_covers',cover_count,'Morse_pairs',len(matched))
print('critical_face_count',len(critical),'critical_dimension',3,'acyclic_vertices',visited)
print('3_by_3_sphere_cycles',len(CYCLES),'unimodular_basis_determinant',det_int(B))
print('S4xS4_actions',len(PERMS)**2,'integral_cycle_action_checks',checks)
print('independent_signed_Lefschetz_checks',lefschetz_checks)
print('factor_interchange_trace',3,'factor_interchange_positive_tensor_flip',True)
print('exterior_square_character',sorted((str(k),v) for k,v in trace_by_cycle_type.items()))
