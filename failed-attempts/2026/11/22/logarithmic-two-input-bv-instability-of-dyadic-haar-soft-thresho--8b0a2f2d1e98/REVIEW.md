# Independent mathematical audit

## correctness

PASS

Quotient by constants: the open first-difference map is an isometry to ℓ¹, and the unit coordinate directions lift to the single cuts. A scalar soft-threshold secant has slope in [0,1], so the effective detail multiplier lies in the convex hull of all 0/1 masks. Every vertex is realized exactly on sufficiently short segments in the corresponding strict chamber for every λ>0, including the maximizing cut. All nonstraddling details vanish, and dotting the remaining normalized detail with the cut yields −m/√s, so the response is ∓m/s as stated, including m=0 at boundaries. At most two end jumps and one interior jump give total variation at most 4m/s≤2. For even d the selected cuts at j=(2^d−1)/3 on scales k=2 mod 4, k≤d−2, have m=(2^k−1)/3, true interior block boundaries, and distinct jump positions: each finer selected block lies strictly between the left endpoint and midpoint of its next larger selected ancestor and away from both. This also separates it from all other larger ancestors. Each contributes at least one. Duplicating coordinates embeds depth d−1 without changing the coarser masked variation, and floor(d/4) is unchanged at odd d. Independent exact reproduction from dyadic conditional averages (python3 /workspace/reviews/evidence_4_5.py) obtained all eight stated numbers; it did not run the uploaded verifier. The chamber/cut arguments, not those eight values, prove the all-depth claims.

## originality

FAIL

A distinct earlier Resultary record, 8271a7c110ab, treats the identical two-input real soft-threshold open-path modulus on the identical dyadic domain, reduces it to masks and one straddling detail per scale, gives a stronger exact all-depth computation via a nine-state recurrence, reproduces the same first eight exact values, and proves logarithmic growth with a stronger lower bound. It covers the material claims. The current q-vector form is a direct rewriting of the retained Haar responses, not a separate new invariant.

## value

FAIL

The sharp modulus would be useful for distinguishing ℓ² nonexpansiveness from open-path variation instability, but that scientific gain is supplied already by an earlier stronger exact result. The elementary rewriting into q-vectors, weaker bound, and repeated finite table do not provide a distinct useful consequence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
