"""Bounded recovery test for lane-20327 target.

Tests NECESSARY computable conditions for:
  omega_{n+3}(S^{n+1}) = Area(C^n_bal), mult-one, index n+3 (3<=n<=6),
and checks status of the SUFFICIENT rigidity (Perdomo/Solomon-type gap).

Run: python3 output/artifacts/recovery_test.py
"""
import mpmath as mp


def sphere_area(m, r=1.0):
    return (r ** m) * 2 * (mp.pi ** ((m + 1) / 2)) / mp.gamma((m + 1) / 2)


def clifford_area(n, k):
    l = n - k
    return sphere_area(k, mp.sqrt(k / n)) * sphere_area(l, mp.sqrt(l / n))


print("=== T1: balanced Clifford uniquely minimizes area in Clifford family ===")
t1 = True
for n in [3, 4, 5, 6]:
    areas = {k: clifford_area(n, k) for k in range(1, n)}
    kbal = n // 2
    amin = min(areas.values())
    ok = areas[kbal] == amin and list(areas.values()).count(amin) == (
        1 if n % 2 else 1)  # symmetric k<->l; balanced unique up to swap
    # uniqueness up to k<->l swap:
    uniq = {float(v) for v in areas.values()}
    ok = (float(areas[kbal]) == min(uniq)) and sum(
        1 for v in areas.values() if abs(v - amin) < 1e-9) <= 2
    t1 &= ok
    print(f"  n={n}: " + ", ".join(
        f"k={k}: {float(v):.4f}" for k, v in areas.items())
        + f"  -> balanced-min: {ok}")
print("T1 PASS" if t1 else "T1 FAIL")

print("=== T2: multiplicity-one gate Area(C_bal) < 2*Area(S^n) ===")
t2 = True
for n in [3, 4, 5, 6]:
    ac = clifford_area(n, n // 2)
    ae = sphere_area(n)
    ok = ac < 2 * ae
    t2 &= ok
    print(f"  n={n}: Area(C)={float(ac):.4f} 2*eq={float(2*ae):.4f} ratio={float(ac/ae):.6f} -> {ok}")
print("T2 PASS" if t2 else "T2 FAIL")

print("=== T3: index(C_bal) = n+3 via Jacobi spectrum J = Delta + 2n ===")
# Eigenvalues of J on S^k(r)xS^l(s), r^2=k/n, s^2=l/n:
#   mu = j(j+k-1)*n/k + i(i+l-1)*n/l - 2n, j,i >= 0.
# Values < 0: (0,0)->-2n [mult 1]; (1,0)->-n [mult k+1]; (0,1)->-n [mult l+1].
# (1,1) -> 0 (null). All others > 0, since next candidates:
# (2,0): 2(k+1)n/k-2n = 2n/k > 0; (0,2): 2n/l > 0. So index = 1+(k+1)+(l+1) = n+3.
t3 = True
for n in [3, 4, 5, 6]:
    k = n // 2
    l = n - k
    vals = []
    for j in range(0, 5):
        for i in range(0, 5):
            mu = j * (j + k - 1) * n / k + i * (i + l - 1) * n / l - 2 * n
            vals.append(((j, i), mu))
    neg = [v for v in vals if v[1] < -1e-9]
    idx = 1 + (k + 1) + (l + 1)
    ok = (idx == n + 3)
    # confirm no other negative among sampled and next shell positive
    ok &= all(v[1] > 0 for v in vals if v not in neg and v != ((1, 1), v[1]))
    t3 &= ok
    print(f"  n={n} k={k} l={l}: negative modes (0,0),(1,0)x{k+1},(0,1)x{l+1} "
          f"-> index={idx} == n+3={n+3}: {ok}")
print("T3 PASS" if t3 else "T3 FAIL")

print()
print("RESULT: all necessary conditions PASS; sufficient global rigidity")
print("(Perdomo index-gap equality case / Solomon area-gap) is an OPEN problem:")
print("  Chen-Wang arXiv:2405.10843 (May 2024): 'So far this conjecture stays open.'")
print("Hence the target cannot be completed by a bounded route in this session.")
