"""Verification: BDS Thm 1.1 rank-2 counts, scalar/moment block triangularity.
Run: python3 output/artifacts/verify_counts.py
"""
import sympy as sp

def D_target(l):
    # 1<=l<m (or l=m with same formula 3m+2floor(m/2)): D = 3l+2(l//2)+1
    return 3*l + 2*(l//2) + 1

def check_bds_table():
    # d=2f, f=1, 1<=l<m: 3lf^2+2floor(l/2)-2f^2+2f+1 = 3l+2floor(l/2)+1
    for l in range(1, 12):
        f = 1
        v = 3*l*f*f + 2*(l//2) - 2*f*f + 2*f + 1
        assert v == D_target(l), (l, v, D_target(l))
    # l=m: 3mf^2+2floor(m/2)-3f^2+2f+1 with f=1 -> 3m+2floor(m/2)
    for m in range(2, 8):
        f = 1
        v = 3*m*f*f + 2*(m//2) - 3*f*f + 2*f + 1
        assert v == 3*m + 2*(m//2), (m, v)
    print("BDS d=2 counts match D(l)=3l+2floor(l/2)+1 (l<m), 3m+2floor(m/2) (l=m)")

def check_split():
    # Hom([0])=1+floor(l/2) (Q.mu block); Hom([2])=3l+floor(l/2) (tracefree block)
    # Hom([2]) = mult{0;2}+mult{1;1}+mult{2;0} = l + (l+floor(l/2)) + l
    for l in range(1, 12):
        assert l + (l + l//2) + l == 3*l + l//2
    print("tracefree split l+(l+floor(l/2))+l = 3l+floor(l/2) OK")

def check_triangular():
    for l in range(1, 9):
        qs = list(range(l//2 + 1))
        n = len(qs)
        M = sp.zeros(n)
        for a, q in enumerate(qs):
            for b, i in enumerate(qs):
                M[a, b] = ((-1)**(i+q))*sp.binomial(i, q) if i >= q else 0
        assert M.det() == 1, (l, M.det())
    for l in range(1, 9):
        M = sp.zeros(l)
        for t in range(l):
            for j in range(l):
                M[t, j] = sp.binomial(t, j)
        assert M.det() == 1, (l, M.det())
    print("scalar Klain block det=1; level (section) block det=1 for all tested l")

def check_basis_count():
    # N_k + 3l + floor(l/2) with N_k=1+floor(l/2) equals D(l)
    for l in range(1, 12):
        assert (1 + l//2) + 3*l + l//2 == D_target(l)
    print("basis index count N_k+3l+floor(l/2) attains BDS dimension exactly")

if __name__ == "__main__":
    check_bds_table()
    check_split()
    check_triangular()
    check_basis_count()
    print("ALL CHECKS PASSED")
