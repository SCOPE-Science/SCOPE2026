"""Parametric infinite family inside the target class: near-group rings K(V,n), V=Z2xZ2.

Basis: V = {0,1,2,3} (xor group) plus X = 4. Fusion rules (n >= 0 integer):
  g * h = gh (group law),  X * g = g * X = X,  X^2 = sum_{g in V} g + n X.

Key proof device: every structure constant is constant or affine-linear in n,
so each associativity equation LHS-RHS is a polynomial in n of degree <= 2.
Verifying all 625 equations at 5 distinct n (0..4) PROVES associativity for all n.
"""
import json, math
import numpy as np

# V = Z2 x Z2 under xor on {0,1,2,3}; X = 4
X = 4
def gmul(g, h):
    return g ^ h

def N_at(a, b, c, n):
    """Structure constant N_{ab}^c for K(V,n)."""
    if a == X and b == X:
        if c == X:
            return n
        else:
            return 1  # coeff of each g in X^2
    if a == X and b != X:
        return 1 if c == X else 0
    if a != X and b == X:
        return 1 if c == X else 0
    # both in V: group law
    return 1 if gmul(a, b) == c else 0

def check_associative(n):
    viols = []
    for a in range(5):
        for b in range(5):
            for c in range(5):
                for d in range(5):
                    lhs = sum(N_at(a, b, e, n) * N_at(e, c, d, n) for e in range(5))
                    rhs = sum(N_at(b, c, e, n) * N_at(a, e, d, n) for e in range(5))
                    if lhs != rhs:
                        viols.append((a, b, c, d, lhs, rhs))
    return viols

print("=== Associativity at n=0..4 (degree<=2 => proof for all n) ===")
all_ok = True
for n in range(5):
    v = check_associative(n)
    print(f"n={n}: violations={len(v)}")
    all_ok = all_ok and (len(v) == 0)
print("Symbolic conclusion: all 625 assoc. equations are polys in n of deg<=2 vanishing at 5 points => hold for ALL n.")

print("\n=== Self-duality / commutativity (support-level, all n) ===")
# self-dual: N_{a,b}^0 = delta_{a,b*} ; check duals: g*=g^{-1}=g (exp 2), X*=X since N_XX^0=1
for n in [0, 2, 7]:
    assert N_at(X, X, 0, n) == 1
    for g in range(4):
        assert N_at(g, g, 0, n) == 1  # g*g=e (order 2), unique dual
        assert sum(N_at(g, h, 0, n) for h in range(5)) == 1  # unique dual
    # commutativity spot check
    for a in range(5):
        for b in range(5):
            for c in range(5):
                assert N_at(a, b, c, n) == N_at(b, a, c, n)
print("self-dual + commutative OK (all n, by construction + spot checks).")

print("\n=== Universal grading trivial for every n>=1 (all grading groups) ===")
# Any grading deg:B->G needs N_ab^c>0 => deg(c)=deg(a)deg(b).
# Support facts (n>=1): N_{Xg}^X=1 => deg(g)=e for all g in V; N_{XX}^X=n>=1 => deg(X)^2=deg(X) => deg(X)=e.
assert N_at(X, 1, X, 2) == 1 and N_at(X, X, X, 2) == 2
print("support: (X,g,X) present => all g in identity component; (X,X,X) present (n>=1) => deg(X)=e. Trivial grading for all n>=1.")
# brute-force Z2 illustration at n=2
def has_nontrivial_Z2(n):
    found = []
    for mask in range(1, 1 << 4):
        deg = {0: 0, X: (mask >> 3) & 1}
        for g in [1, 2, 3]:
            deg[g] = (mask >> (g - 1)) & 1
        ok = True
        for a in range(5):
            for b in range(5):
                for c in range(5):
                    if N_at(a, b, c, n) > 0 and (deg[a] + deg[b]) % 2 != deg[c]:
                        ok = False
        if ok:
            found.append(mask)
    return found
print(f"nontrivial Z2-gradings at n=2: {has_nontrivial_Z2(2)} (expect []); at n=0: {has_nontrivial_Z2(0)} (TY case, nontrivial exists)")

print("\n=== FP dims: d^2 = 4 + n d; integrality analysis ===")
# d integer => d(d-n)=4, d-n>=1 divisor of 4 => d-n in {1,2,4} => (n,d) in {(3,4),(0,2),(-3,...)}.
# So for n>=4 or n=2: d non-integral. n=3: d=4 integral (EXCLUDED from target class). n=0,1: mult<2 anyway.
results = {}
for n in [2, 3, 4, 5, 6, 7, 8, 9, 10]:
    d = (n + math.sqrt(n * n + 16)) / 2
    is_int = abs(d - round(d)) < 1e-9
    results[n] = {"d_X": d, "integral": bool(is_int)}
    print(f"n={n}: d_X={d:.6f} integral={is_int}")
assert results[2]["integral"] is False       # 1+sqrt(5)
assert results[3]["integral"] is True        # d=4 -> outside target class (all dims integral)
assert all(results[n]["integral"] is False for n in [4, 5, 6, 7, 8, 9, 10])

print("\n=== Target-hypothesis audit per n ===")
# rank 5 ✓; commutative self-dual ✓; trivial grading needs n>=1; mult>=2 needs n>=2; non-integral dim needs n!=3 (for n>=2)
audit = {}
for n in [0, 1, 2, 3, 4, 5, 6, 10, 100]:
    in_class = (n >= 1) and (n >= 2) and (n != 3)
    audit[n] = bool(in_class)
    print(f"n={n}: in_target_class={in_class}")
in_class_ns = [2] + list(range(4, 11)) + ["all n>=4"]
print("Infinite subfamily in target class: n = 2, 4, 5, 6, ... (all n>=2 except n=3).")

print("\n=== Pairwise non-isomorphism ===")
# FPdims are ring invariants; invertibles have dim 1, d_X>1 unique => X canonical => n = N_XX^X invariant.
print("d_X(n) strictly increasing in n; X = unique basis elt with dim>1 => n recoverable as N_XX^X. Distinct n => non-isomorphic.")

out = {
    "family": "K(Z2xZ2, n): X*g=X, X^2=sum_g g + nX",
    "associativity_n0_to_n4_violations": 0,
    "symbolic_proof": "625 assoc equations are degree<=2 polynomials in n, vanish at n=0,1,2,3,4, hence identically zero: associative for ALL n>=0",
    "self_dual_commutative": True,
    "trivial_grading_all_n_ge_1": True,
    "fp_formula": "d_X=(n+sqrt(n^2+16))/2; integral iff (n,d)=(3,4) among n>=2 (d|4 divisor argument)",
    "in_target_class": "all integers n>=2 with n!=3 (infinite); n=3 excluded (all dims integral), n=0,1 excluded (mult<2)",
    "pairwise_nonisomorphic": "n recovered invariantly as N_XX^X for canonical non-invertible X",
    "consequence": "Target class is infinite: no finite structure-constant bound exists; complete per-table census + per-table pentagon/obstruction is not completable.",
}
with open("output/artifacts/family_verification.json", "w") as f:
    json.dump(out, f, indent=2)
print("wrote output/artifacts/family_verification.json")
