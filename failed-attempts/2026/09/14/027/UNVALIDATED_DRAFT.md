# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Non-existence of the genus-0 degree-12 Belyi passport (2^6, 3^4, 5-4-2-1)

## Claim
The passport P1 = ([2,2,2,2,2,2], [3,3,3,3], [5,4,2,1]) is **not realizable**:
there is no connected (indeed, no possibly disconnected) holomorphic cover
f: P^1_C → P^1_C of degree 12 branched only over {0, 1, ∞} whose local
monodromy has exactly these ramification partitions. Equivalently, there is
no triple (s0, s1, sinf) in S12 with the stated cycle types satisfying
s0·s1·sinf = 1, transitively or otherwise. The obstruction is the vanishing
of the class-algebra structure constant: zero product hits. Consequently
there is no transitive subgroup G, no braid orbit, and no field of definition
or explicit model to report; these are vacuous.

## Proof
Riemann–Hurwitz is satisfied (6 + 8 + 8 = 22 = 2·12 − 2), so genus is no
obstruction, and all three classes are even, so parity is no obstruction.
The obstruction is established by exhaustive enumeration in S12.

**Normalization A.** Conjugate any hypothetical triple so that
s0 = (0 1)(2 3)(4 5)(6 7)(8 9)(10 11). Every element of the class 3^4 arises
as an oriented partition of {0,…,11} into four 3-cycles; there are exactly
12!/(3^4·4!) = 246400 of them, and the program generates each exactly once
(duplicate-checked by a seen-set of cardinality 246400). For each, it computes
ctype(s0·s1). Zero of the 246400 products has type (5,4,2,1). The full
product-type distribution over the 16 occurring types is:

(2^6): 640; (3^4): 3840; (4,2^3,1^2): 3840; (4^2,1^4): 5760;
(4^2,2^2): 11520; (5^2,1^2): 23040; (6,2^3): 1280; (6,3,2,1): 46080;
(6,4,1^2): 3840; (6^2): 12160; (8,2,1^2): 23040; (8,4): 11520;
(9,1^3): 15360; (9,3): 15360; (10,2): 23040; (11,1): 46080 (sum 246400).

**Normalization B (independent cross-check).** Conjugate instead so that
s1 = (0 1 2)(3 4 5)(6 7 8)(9 10 11) and enumerate all 11·9·7·5·3·1 = 10395
fixed-point-free involutions s0 (duplicate-checked, exact cardinality).
Zero of the 10395 products s0·s1 has type (5,4,2,1); the same 16 product
types occur with proportional counts summing to 10395.

**Convention independence.** The code asserts ctype(ab) = ctype(ba) in every
case, so the conclusion does not depend on whether the product is read as
s0·s1 or s1·s0, nor on left/right action conventions: sinf = (s0·s1)^{−1}
always has the same cycle type as the computed product.

Since every hypothetical triple is conjugate to one counted in each
normalization, and no counted pair produces the required third partition,
no triple with passport P1 exists. A fortiori no *transitive* triple exists,
so there is no connected cover, no monodromy group G, and no braid orbit.
Q.E.D.

## Verification / reproducibility
- Script: `output/artifacts/enumerate_passport_P1.py` (Python standard library
  only; deterministic; no randomness, no external packages).
- Captured run: `output/artifacts/enumeration_output.txt` (exit code 0).
- Reproduce: `python3 output/artifacts/enumerate_passport_P1.py` (≈1 s).
- In-code self-checks: exact enumeration cardinalities (246400, 10395),
  duplicate detection, per-case ab/ba type agreement, distribution sums.

## Limitations / scope
- The census is specific to degree 12 and the exact partitions stated; it
  says nothing about neighbouring passports (e.g. the occurring product
  types listed above, such as (6,3,2,1), are realized).
- The computation proves non-existence of any triple; transitivity filtering
  is unnecessary since the set of triples is already empty.
- No analytic (character-theoretic) proof is given; the obstruction is
  certified computationally but exactly (integer permutation arithmetic).
