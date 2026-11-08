"""Exact checks of the four-point Segre determinant singular-locus theorem.

Run with python 3; optional SymPy provides characteristic-zero Hessian witnesses.
The finite-field check is exhaustive over (P1(F2) x P1(F2))^4.
"""
from itertools import product, combinations

P1 = ((1, 0), (0, 1), (1, 1))
Q = tuple(product(P1, P1))

def tensor(u, v):
    return tuple(a*b % 2 for a in u for b in v)

def rowbit(row):
    return sum(int(b) << i for i, b in enumerate(row))

def rank2(rows):
    basis = [0]*4
    for x in rows:
        for i in range(3, -1, -1):
            if (x>>i)&1:
                if basis[i]: x ^= basis[i]
                else:
                    basis[i] = x
                    break
    return sum(b!=0 for b in basis)

def det(rows):
    return rank2(rows) == 4

def dirs(pt):
    u,v=pt
    du=(0,1) if u==(1,0) else (1,0)
    dv=(0,1) if v==(1,0) else (1,0)
    return (rowbit(tensor(du,v)), rowbit(tensor(u,dv)))

def geometric_rank3_stratum(points):
    for i,j in combinations(range(4),2):
        if points[i]!=points[j]: continue
        k,l=(z for z in range(4) if z not in (i,j))
        a,b=points[i]
        if ((points[k][0]==a and points[l][1]==b)
          or (points[k][1]==b and points[l][0]==a)):
            return True
    return False

def component_union(points):
    # ruling components
    if len({p[0] for p in points})==1 or len({p[1] for p in points})==1:
        return True
    # seven two-value components, including all diagonal strata
    if len(set(points))<=2:
        return True
    return geometric_rank3_stratum(points)

def verify_F2():
    singular=rank2_count=rank3_count=F_zero=0
    for points in product(Q, repeat=4):
        rows=[rowbit(tensor(*p)) for p in points]
        rank=rank2(rows)
        f_zero=(rank<=3)
        if f_zero: F_zero+=1
        gradient_zero=f_zero and all(
            not det(rows[:i]+[direction]+rows[i+1:])
            for i,p in enumerate(points) for direction in dirs(p)
        )
        predicted=(rank<=2) or (rank==3 and geometric_rank3_stratum(points))
        assert gradient_zero == predicted, (points, rank, gradient_zero, predicted)
        assert predicted == component_union(points), (points,rank)
        if gradient_zero: singular+=1
        if rank<=2: rank2_count+=1
        if rank==3 and gradient_zero:rank3_count+=1
    print('GF2_EXHAUSTIVE_OK', 'all_configs',len(Q)**4,'F_zero',F_zero,
          'singular',singular,'rank_le2',rank2_count,'rank3',rank3_count)

def verify_hessians():
    try:
        import sympy as s
    except ImportError:
        print('SYMPY_OPTIONAL_CHECK_SKIPPED')
        return
    z=s.symbols('x1 y1 x2 y2 x3 y3 x4 y4')
    mat=s.Matrix([[1,z[2*i],z[2*i+1],z[2*i]*z[2*i+1]] for i in range(4)])
    f=s.expand(mat.det(method='domain-ge'))
    h=s.hessian(f,z)
    tests=(
        ('ruling',(0,0,0,1,0,2,0,3),3,(0,2,4),24),
        ('two_value_1_3',(0,0,0,0,0,0,1,1),4,(0,1,2,3),1),
        ('two_value_2_2',(0,0,0,0,1,1,1,1),4,(0,1,4,5),1),
        ('rank3_tangent',(0,0,0,0,0,2,3,0),4,(0,1,2,3),1296),
    )
    for name,p,rank,indices,expected in tests:
        subs=dict(zip(z,p))
        assert f.subs(subs)==0
        assert all(s.diff(f,zi).subs(subs)==0 for zi in z)
        H=h.subs(subs)
        assert H.rank()==rank,(name,H.rank())
        assert H.extract(indices,indices).det()==expected
        print('CHAR0_HESSIAN_OK',name,'rank',rank,'nonzero_minor',expected)

if __name__=='__main__':
    verify_F2()
    verify_hessians()
