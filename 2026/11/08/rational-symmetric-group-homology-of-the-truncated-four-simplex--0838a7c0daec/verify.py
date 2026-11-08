"""Exact rational character calculation for an independence complex.

Run: python verify.py
Requires only the Python standard library. All row reductions use Fraction,
not floating point or modular arithmetic. Simplices have lexicographic orientation.
"""
from collections import Counter
from fractions import Fraction
from itertools import permutations, product

N = 5


def faces():
    out = [[] for _ in range(N)]
    for choices in product(*([[None] + [b for b in range(N) if b != a]
                             for a in range(N)])):
        simplex = tuple((a, b) for a, b in enumerate(choices) if b is not None)
        if simplex and all((b, a) not in simplex for a, b in simplex):
            out[len(simplex)-1].append(simplex)
    return out


def reduced_boundary_basis(lower, upper):
    """Return a normalized exact echelon basis of im(boundary).

    The first nonzero coefficient of every basis vector is 1. The pivot
    procedure is elementary Gaussian elimination by columns over Q.
    """
    index = {f: i for i, f in enumerate(lower)}
    basis = {}
    for face in upper:
        v = {index[face[:j] + face[j+1:]]: Fraction((-1)**j)
             for j in range(len(face))}
        while v:
            i = min(v)
            if i not in basis:
                a = v[i]
                basis[i] = {j: x/a for j, x in v.items()}
                break
            a = v[i]
            for j, b in basis[i].items():
                c = v.get(j, 0) - a*b
                if c: v[j] = c
                else: v.pop(j, None)
    return basis


def act(g, face):
    image = [(g[a], g[b]) for a, b in face]
    sign = (-1)**sum(image[i] > image[j]
                     for i in range(len(image)) for j in range(i+1,len(image)))
    return tuple(sorted(image)), sign


def chain_trace(g, chain_faces):
    return sum(act(g, face)[1] for face in chain_faces
               if act(g, face)[0] == face)


def image_trace(g, lower, basis):
    """Trace on invariant rational image, by exact basis reduction.

    Since the boundary commutes with the group action, its image is
    invariant. Reduction of each transformed basis vector gives diagonal
    coordinates in a normalized echelon basis.
    """
    index = {f: i for i,f in enumerate(lower)}
    trace = Fraction(0)
    for pivot, vec in basis.items():
        mapped = {}
        for j, coefficient in vec.items():
            f, s = act(g, lower[j])
            k = index[f]
            c = mapped.get(k, 0) + s*coefficient
            if c: mapped[k] = c
            else: mapped.pop(k, None)
        while mapped:
            k = min(mapped)
            assert k in basis, 'image is not invariant'
            a = mapped[k]
            if k == pivot:
                trace += a
            for j,b in basis[k].items():
                c = mapped.get(j, 0) - a*b
                if c: mapped[j] = c
                else: mapped.pop(j, None)
    assert trace.denominator == 1
    return int(trace)


def representative(lengths):
    g=list(range(N)); start=0
    for k in lengths:
        for j in range(k):g[start+j]=start+(j+1)%k
        start+=k
    return tuple(g)


def partition(n, smallest=1):
    if n==0:
        yield ()
    for k in range(smallest,n+1):
        for rest in partition(n-k,k):yield (k,)+rest


def cycle_sign(lengths):
    return (-1)**(N-len(lengths))


def cycle_perm_trace(lengths):
    return 24 if lengths==(1,1,1,1,1) else 4 if lengths==(5,) else 0


def check_chain_equivariance(all_faces):
    # Verify both generators on every positive-dimensional simplex, which
    # implies equivariance for the whole group they generate.
    generators=((1,0,2,3,4),(1,2,3,4,0))
    for g in generators:
        for dim in range(1,N):
            for face in all_faces[dim]:
                transformed, sign = act(g, face)
                lhs=Counter()
                for j in range(len(face)):
                    f,s=act(g, face[:j]+face[j+1:])
                    lhs[f]+=(-1)**j*s
                rhs=Counter()
                for j in range(len(transformed)):
                    f=transformed[:j]+transformed[j+1:]
                    rhs[f]+=sign*(-1)**j
                assert {k:v for k,v in lhs.items() if v} == {k:v for k,v in rhs.items() if v}, (g,face)
    return sum(len(all_faces[i]) for i in range(1,N))*len(generators)


def main():
    f=faces()
    assert [len(x) for x in f]==[20,150,520,815,444]
    bases={i:reduced_boundary_basis(f[i-1],f[i]) for i in range(1,N)}
    ranks=[1]+[len(bases[i]) for i in range(1,N)]
    assert ranks==[1,19,131,389,421]
    assert [len(f[i])-ranks[i]-(ranks[i+1] if i+1<N else 0)
            for i in range(N)]==[0,0,0,5,23]
    assert all(v.denominator==1 for b in bases.values() for col in b.values() for v in col.values())
    print('FACE_VECTOR', [len(x) for x in f])
    print('AUGMENTED_BOUNDARY_RANKS',ranks)
    print('EXACT_ECHELON_CERTIFICATE',sum(len(x) for x in f),'nonempty_faces',sum(len(b) for b in bases.values()),'nonzero_pivots')
    check_count=check_chain_equivariance(f)
    print('SIGNED_CHAIN_EQUIVARIANCE',check_count)
    print('CLASSES cycle_type H3 H4  signed_fixed_points cyclic_orbit_minus_sign')
    table={}
    for lengths in partition(N):
        g=representative(lengths)
        c=[chain_trace(g,x) for x in f]
        t={i:image_trace(g,f[i-1],bases[i]) for i in range(1,N)}
        h=[c[i]-t.get(i,0)-t.get(i+1,0) for i in range(N)]
        h[0]-=1 # reduced H_0
        assert h[:3]==[0,0,0], (lengths,h)
        prediction3=cycle_sign(lengths)*lengths.count(1)
        prediction4=cycle_perm_trace(lengths)-cycle_sign(lengths)
        assert (h[3],h[4])==(prediction3,prediction4),(lengths,h,prediction3,prediction4)
        table[lengths]=(h[3],h[4])
        print('CLASS',str(lengths).replace(' ',''),h[3],h[4],prediction3,prediction4)
    # Check the invariant multiplicity by the complete 120-element trace average.
    sums=[0,0]
    all_perms=list(permutations(range(N)))
    for g in all_perms:
        visited=set(); lengths=[]
        for v in range(N):
            if v in visited: continue
            j=v;k=0
            while j not in visited:
                visited.add(j);j=g[j];k+=1
            lengths.append(k)
        a,b=table[tuple(sorted(lengths))]
        sums[0]+=a;sums[1]+=b
    assert sums==[0,120]
    print('INVARIANTS_H3_H4',[x//120 for x in sums])
    print('TRUNCATED_FOUR_SIMPLEX_S5_MODULES_EXACT_PASS')

if __name__=='__main__':main()
