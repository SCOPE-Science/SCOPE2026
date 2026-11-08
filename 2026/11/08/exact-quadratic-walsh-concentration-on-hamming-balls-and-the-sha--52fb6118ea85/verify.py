"""Exact arithmetic checks for quadratic Walsh concentration on Hamming balls.

Python 3 standard library only. The identities for all dimensions follow from the
proof; the finite tests independently reconstruct selected matrices.
"""
from itertools import combinations
from math import comb


def a(n, r, j):
    return sum((-1)**h * comb(j, h) * comb(n - j, k - h)
               for k in range(r + 1) for h in range(j + 1)
               if 0 <= k - h <= n - j)


def bareiss(a):
    b = [list(map(int, row)) for row in a]
    n = len(b)
    sign, prev = 1, 1
    for k in range(n - 1):
        if b[k][k] == 0:
            z = next((j for j in range(k + 1, n) if b[j][k] != 0), None)
            if z is None:
                return 0
            b[k], b[z] = b[z], b[k]
            sign *= -1
        piv = b[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                num = b[i][j] * piv - b[i][k] * b[k][j]
                assert num % prev == 0
                b[i][j] = num // prev
        for i in range(k + 1, n):
            b[i][k] = 0
        prev = piv
    return sign * b[-1][-1]


def mat_vec(m, v):
    return [sum(x*y for x,y in zip(row,v)) for row in m]


def poly_det3(m):
    return (m[0][0]*(m[1][1]*m[2][2]-m[1][2]*m[2][1])
            -m[0][1]*(m[1][0]*m[2][2]-m[1][2]*m[2][0])
            +m[0][2]*(m[1][0]*m[2][1]-m[1][1]*m[2][0]))


def main():
    checks = 0
    for n in range(5,11):
        labels = [()] + [(i,) for i in range(n)] + list(combinations(range(n),2))
        D = len(labels)
        for r in range(n + 1):
            aa = [a(n,r,j) for j in range(5)]
            points = [sum(1 << i for i in tup) for k in range(r+1)
                      for tup in combinations(range(n), k)]
            assert aa == [sum((-1)**((x & ((1 << j)-1)).bit_count()) for x in points)
                          for j in range(5)]
            checks += 5
            # Directly compute the full (unnormalized) restricted Walsh Gram matrix.
            masks = [sum(1 << j for j in tup) for tup in labels]
            m = [[sum((-1)**(((u ^ v) & x).bit_count()) for x in points)
                  for v in masks] for u in masks]
            for i in range(D):
                for j in range(D):
                    assert m[i][j] == aa[(masks[i]^masks[j]).bit_count()]
                    checks += 1
            # Invariant sectors (no floating point): radial, standard, and quadratic.
            C = comb(n,2)
            B0 = [int(len(tup)==0) for tup in labels]
            B1 = [int(len(tup)==1) for tup in labels]
            B2 = [int(len(tup)==2) for tup in labels]
            Rad = [B0,B1,B2]
            rad = [
                [aa[0],n*aa[1],C*aa[2]],
                [aa[1],aa[0]+(n-1)*aa[2],(n-1)*(2*aa[1]+(n-2)*aa[3])//2],
                [aa[2],2*aa[1]+(n-2)*aa[3],aa[0]+2*(n-2)*aa[2]+comb(n-2,2)*aa[4]]
            ]
            for j in range(3):
                assert mat_vec(m,Rad[j]) == [sum(rad[i][j]*Rad[i][k] for i in range(3)) for k in range(D)]
                checks += 1
            u=[int(i==0)-int(i==1) for i in range(n)]
            St1 = [u[tup[0]] if len(tup)==1 else 0 for tup in labels]
            St2 = [(u[tup[0]]+u[tup[1]]) if len(tup)==2 else 0 for tup in labels]
            std = [[aa[0]-aa[2],(n-2)*(aa[1]-aa[3])],
                   [aa[1]-aa[3],aa[0]+(n-4)*aa[2]-(n-3)*aa[4]]]
            for j,vec in enumerate((St1,St2)):
                assert mat_vec(m,vec)==[std[0][j]*St1[k]+std[1][j]*St2[k] for k in range(D)]
                checks += 1
            q = {(0,1):1,(2,3):1,(0,2):-1,(1,3):-1}
            Q = [q.get(tup,0) for tup in labels]
            lam=aa[0]-2*aa[2]+aa[4]
            assert mat_vec(m,Q)==[lam*v for v in Q]
            checks += 1
            if r==2:
                trace=sum(rad[i][i] for i in range(3))
                minors=(rad[0][0]*rad[1][1]-rad[0][1]*rad[1][0]
                      +rad[0][0]*rad[2][2]-rad[0][2]*rad[2][0]
                      +rad[1][1]*rad[2][2]-rad[1][2]*rad[2][1])
                assert 4*trace==n**4-14*n**3+85*n**2-204*n+212
                assert minors==n**4-2*n**3+13*n**2-60*n+116
                assert poly_det3(rad)==64
                assert std[0][0]+std[1][1]==4*((n-3)**2+4)
                assert std[0][0]*std[1][1]-std[0][1]*std[1][0]==64
                assert lam==16
                checks+=6
                if n<=6:
                    # Strong independent determinant check at the exact interpolation threshold.
                    det=bareiss(m)
                    assert abs(det)==2**(2*n+4*C)
                    checks+=1
    print(f'WALSH_QUADRATIC_BALL_EXACT_CHECKS_PASS {checks}')

if __name__=='__main__':
    main()
