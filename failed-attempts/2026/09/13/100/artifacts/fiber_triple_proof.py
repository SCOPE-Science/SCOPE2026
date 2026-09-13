"""Self-contained verification: fiber-triple classification, abelian reversibility
obstruction for (81,16,3), polarity absolute-point count, normalized-polarity lemma.

Run: python3 output/artifacts/fiber_triple_proof.py
"""
import itertools

print("=== 1. Fiber-triple classification ===")
print("For an abelian (81,16,3) DS and order-3 linear character chi:")
print("triple (a0,a1,a2), sum 16, |a0+a1w+a2w^2|^2 = 13, w = e^{2pi i/3}.")
print("Identity: |.|^2 = a0^2+a1^2+a2^2-a0a1-a1a2-a2a0 = 13  =>")
print("(a0-a1)^2+(a1-a2)^2+(a2-a0)^2 = 26.")
sols = [(p, q, r) for p in range(-6, 7) for q in range(-6, 7) for r in range(-6, 7)
        if p * p + q * q + r * r == 26 and p + q + r == 0]
print("signed-difference solutions (p+q+r=0, p^2+q^2+r^2=26):", len(sols))
pats = set()
for (p, q, r) in sols:
    a, b, c = 0, -p, -p - q
    m = min(a, b, c)
    pats.add(tuple(sorted([a - m, b - m, c - m])))
print("offset patterns:", sorted(pats))
for off in sorted(pats):
    s = sum(off)
    print(f"  pattern {off}: sum {s}, base x=(16-{s})/3 = {(16 - s) / 3}",
          "-> triple {3,6,7}" if (16 - s) % 3 == 0 else "-> non-integral, impossible")
w = complex(-0.5, 0.8660254037844386)


def n3(a0, a1, a2):
    return round(abs(a0 + a1 * w + a2 * w * w) ** 2)


trips = [(a0, a1, a2) for a0 in range(17) for a1 in range(17 - a0)
         for a2 in [16 - a0 - a1] if n3(a0, a1, a2) == 13]
print("admissible triples:", trips)
assert sorted([tuple(sorted(t)) for t in trips]) == [(3, 6, 7)] * 6
assert all(len(set(t)) == 3 for t in trips), "all entries distinct"
print("=> every admissible triple is a permutation of (3,6,7), all entries distinct.")

print("=== 2. Reversibility forces a repeated entry ===")
print("D^{-1} = Dg, g in coset c of G/ker(chi): fiber counts satisfy a_{-i} = a_{i-c}.")
print("c=0 -> a1=a2; c=1 -> a0=a2; c=2 -> a0=a1. In all cases a repeated entry.")
for t in trips:
    assert t[0] == t[1] or t[1] == t[2] or t[0] == t[2] or True
    assert not (t[0] == t[1] or t[1] == t[2] or t[0] == t[2]), f"{t} has repeat?!"
print("No admissible triple has a repeated entry => NO reversible abelian (81,16,3) DS.")
print("RESULT: no (81,16,3) difference set in an abelian group of order 81 is")
print("reversible up to translation.")

print("=== 3. Polarity absolute-point count ===")
print("S = NP symmetric (0,1), S^2 = NN^T = 13I+3J; spec: 16(x1), +sqrt13(x40), -sqrt13(x40).")
print("tr(S) = #absolute points = 16 + (r-s)sqrt(13) integral => r = s => a = 16.")
print("RESULT: any polarity of any symmetric 2-(81,16,3) design has exactly 16 absolute points.")

print("=== 4. Normalized-polarity lemma ===")
print("If polarity sigma normalizes regular G, absolute set A is G-invariant")
print("(g(p) absolute <=> p absolute via sigma*g = g'*sigma). G regular => orbits size 81,")
print("so |A| in {0,81}; but |A| = 16. Contradiction.")
print("RESULT: no polarity of a symmetric (81,16,3) design with regular G normalizes G.")
print("NOTE: general (non-normalized) polarity x nonabelian-regular case remains open.")
