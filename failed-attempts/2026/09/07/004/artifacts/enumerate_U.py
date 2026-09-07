"""Enumerate digit-restricted universes U(p,10,D) in exact integer arithmetic."""
import math

def U_set(p, digits):
    digits = set(digits)
    U = []
    for x in range(p):
        if all(int(ch) in digits for ch in str(x)):
            U.append(x)
    return U

def triangular_lb(p):
    return math.ceil((math.sqrt(8*p+1)-1)/2)

if __name__ == "__main__":
    for p in [173,179,181,191,193,197]:
        for D in [[0,1,2],[0,1,2,3],[0,1,2,3,4]]:
            U = U_set(p, set(D))
            print(f"p={p} D={D} |U|={len(U)}")
    # main case
    U = U_set(197, {0,1,2,3,4})
    assert len(U) == 50, len(U)
    n_lo, n_hi = [x for x in U if x < 100], [x for x in U if x >= 100]
    assert len(n_lo) == 25 and len(n_hi) == 25, (len(n_lo), len(n_hi))
    assert U == sorted(U)
    print("MAIN: |U(197,D4)|=50 verified (25 in [0,99] + 25 in [100,144])")
    print("U =", U)
    for p in [173,179,181,191,193,197]:
        k = triangular_lb(p)
        print(f"p={p} triangular_lb={k} check {k*(k+1)//2}>=p>{(k-1)*k//2}: {k*(k+1)//2>=p>(k-1)*k//2}")
    # full-universe sumset sizes
    for p in [173,179,181,191,193,197]:
        for D in [{0,1,2},{0,1,2,3},{0,1,2,3,4}]:
            U2 = U_set(p, D)
            S = set((a+b) % p for a in U2 for b in U2)
            print(f"p={p} Dmax={max(D)} |U|={len(U2)} |S(U)|={len(S)} full={len(S)==p} frac={len(S)/p:.4f}")
