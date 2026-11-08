"""Exact rational independent checks of a two-leader multipartite graph theorem.
No external dependencies. Run: python3 verify.py
"""
from fractions import Fraction as F
from itertools import combinations, combinations_with_replacement


def objective_from_counts(parts, leaders):
    N = sum(parts)
    C = F(0)
    U = F(0)
    V = F(0)
    for n, s in zip(parts, leaders):
        f = n - s
        if f:
            C += F(f - 1, N - n) + F(1, N - s)
            U += F(f, N - s)
            V += F(f, (N - s)**2)
    return C + V/(1-U)


def base_C(parts):
    N = sum(parts)
    return sum((F(n-1, N-n)+F(1,N) for n in parts), F(0))


def same_formula(parts, i):
    N = sum(parts)
    u = parts[i]
    return base_C(parts) + F(N*N - 8*N + 4*u, 2*N*(N-u))


def mixed_formula(parts, i, k):
    N = sum(parts)
    u,v=parts[i],parts[k]
    return (base_C(parts) - F(1,N-u)-F(1,N-v)+F(2,N*(N-1))
            + F(N*(N-1), 2*N-u-v) * (F(N-u-v,N*N)+F(u+v-2,(N-1)**2)))


def numerator(h, d, R):
    p0 = 2*(R+h+2)**2*(R*R+R*(4*h+9)+4*h*h+16*h+16)
    p1 = (R+h+2)*(R**3+R*R*(6*h+13)+R*(12*h*h+48*h+54)
                    +8*h**3+44*h*h+88*h+64)
    p2 = 3*R**3+R*R*(15*h+24)+R*(24*h*h+74*h+58)+12*h**3+54*h*h+80*h+40
    p3 = 3*R*R+R*(9*h+11)+6*h*h+13*h+4
    p4 = R+h
    return p0+d*p1+d*d*p2+d**3*p3+d**4*p4


def denominator(h,d,R):
    u=h+2
    return 2*(R+u)*(R+d+u)*(R+d+2*u)*(2*R+d+2*u)*(R+d+2*u-1)


def matrix_inverse_trace(A):
    n=len(A)
    Q=[[F(x) for x in row]+[F(int(i==j)) for j in range(n)] for i,row in enumerate(A)]
    for col in range(n):
        pivot=next(i for i in range(col,n) if Q[i][col])
        Q[col],Q[pivot]=Q[pivot],Q[col]
        z=Q[col][col]
        Q[col]=[x/z for x in Q[col]]
        for i in range(n):
            if i!=col:
                z=Q[i][col]
                if z:
                    Q[i]=[a-z*b for a,b in zip(Q[i],Q[col])]
    return sum((Q[i][n+i] for i in range(n)),F(0))


def matrix_objective(parts, pair):
    N=sum(parts)
    part_of=[i for i,n in enumerate(parts) for _ in range(n)]
    Fset=[v for v in range(N) if v not in pair]
    A=[]
    for u in Fset:
        row=[]
        for v in Fset:
            row.append(N-parts[part_of[u]] if u==v else -int(part_of[u]!=part_of[v]))
        A.append(row)
    return matrix_inverse_trace(A)


def main():
    identities=0
    # Finite polynomial identity certificate: after multiplying by denominator,
    # both sides are polynomials of separate degree <=8 in h,d,R.
    # Values at 9 distinct points per variable therefore prove identity.
    for h in range(9):
        for d in range(9):
            for R in range(9):
                u,v=h+2,h+2+d
                N=u+v+R
                # The formulas depend on other groups only through the total R.
                # R=0 is permitted in the algebraic identity although the target
                # theorem has at least three groups and thus R>=2.
                C=F(0)
                same=C+F(N*N-8*N+4*u,2*N*(N-u))
                mixed=(C-F(1,N-u)-F(1,N-v)+F(2,N*(N-1))
                       +F(N*(N-1),2*N-u-v)*(F(N-u-v,N*N)+F(u+v-2,(N-1)**2)))
                assert mixed-same==F(numerator(h,d,R),denominator(h,d,R))
                assert numerator(h,d,R)>0
                identities+=1
    direct=0
    classified=0
    for r in (3,4):
        for parts in combinations_with_replacement(range(2,7 if r==3 else 5),r):
            N=sum(parts)
            if N>17:continue
            seen={}
            for a,b in combinations(range(N),2):
                value=matrix_objective(parts,(a,b))
                seen[(a,b)]=value
                direct+=1
            expected=min(seen.values())
            first=[0]
            for n in parts: first.append(first[-1]+n)
            optparts=[i for i,n in enumerate(parts) if n==min(parts)]
            selected={pair for pair in seen if any(first[i]<=pair[0]<pair[1]<first[i+1] for i in optparts)}
            actual={pair for pair,v in seen.items() if v==expected}
            assert actual==selected, (parts,actual,selected)
            for i in range(r):
                s=[0]*r;s[i]=2
                assert objective_from_counts(parts,s)==same_formula(parts,i)
            for i,k in combinations(range(r),2):
                s=[0]*r;s[i]=s[k]=1
                assert objective_from_counts(parts,s)==mixed_formula(parts,i,k)
            classified+=1
    print('VERIFY_OK identity_grid=%d graph_instances=%d exact_matrix_pair_comparisons=%d' % (identities,classified,direct))

if __name__ == '__main__': main()
