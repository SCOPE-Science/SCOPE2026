# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# DRAFT — lane-1082 (target-only lane; TARGET negative resolution)

## Claim (TARGET, disproof)

In the all-negative window — fields K = Q(sqrt(pq)) with p < q both primes
3 mod 4 and pq < 2500 — **no field has ordinary 4-rank 1**. Hence the target
claim, "the least field with ordinary 4-rank 1 has 2-class group exactly C4
with an explicit unramified generator beta," is **false by vacuity of its
presupposition**: there is no least 4-rank-1 field to certify. Concretely:

- The window contains exactly **161** admissible pairs (least pair (3,7), D=21).
- Every field has narrow 4-rank **0** and ordinary 4-rank **0**.
- Every class number h in the window is **odd** (h in {1,3,5,7}; 143 fields
  have h=1, thirteen have h=3, four have h=5, one — D=1761=3·587 — has h=7),
  so 4 ∤ h everywhere; neither a C4 nor a V4 2-class group occurs anywhere.

## Proof

### 1. Discriminant shape (cheap falsification check 1)

If p ≡ q ≡ 3 (mod 4) then pq ≡ 1 (mod 4), so K = Q(sqrt(pq)) has fundamental
discriminant D = pq (squarefree, 1 mod 4). The genus-theory prime-discriminant
factorisation is D = (−p)(−q), both factors negative — the "all-negative"
shape. The verifier asserts D ≡ 1 (mod 4) and distinctness of all 161 values.

### 2. Opposite-sign lemma → Redei rank 1 → narrow 4-rank 0 everywhere

For D = pq with prime discriminants d1 = −p, d2 = −q, the Rédei 2×2 matrix is
built from A = (d1/q) = (−p/q) and B = (d2/p) = (−q/p), with entries 0/1
according as the symbol is +1/−1. The matrix is [[x,x],[y,y]].

Lemma (opposite sign). For p < q both ≡ 3 (mod 4),
(−p/q)·(−q/p) = −1, i.e. A = −B always.

Proof. By multiplicativity, A = (−1/q)(p/q) and B = (−1/p)(q/p).
Since q ≡ p ≡ 3 (mod 4), (−1/q) = (−1/p) = −1. By quadratic reciprocity for two
primes both 3 mod 4, (p/q) = −(q/p). Hence A = −(p/q) = (q/p) while
B = −(q/p), so A = −B. ∎

Consequence. Exactly one of x, y is 0 and the other is 1, so the matrix has
exactly one nonzero row: rank 1. By Rédei–Reichardt (t = 2 prime discriminants),
narrow 4-rank = (t−1) − rank = 1 − 1 = 0 for **every** pair. There are no
"ambiguous" cases at all — the window's tiny-instance split hypothesised at
admission does not occur. The verifier checks A = −B and rank 1 for all 161
pairs (81 with (A,B) = (1,−1), 80 with (−1,1)).

Since the ordinary class group is a quotient of the narrow class group
(forgetting the infinite places), the ordinary 2-class group is a quotient of a
group with 4-rank 0, hence itself has ordinary 4-rank 0 everywhere.

### 3. Independent exact certificate: 4 ∤ h(D) for all 161 fields

For each D, the verifier enumerates **all** reduced indefinite binary quadratic
forms (a,b,c) of discriminant D, i.e. |√D − 2|a|| < b < √D with
b² − 4ac = D. Completeness: any reduced form has |a| < √D (else
2|a| − √D ≥ √D > b, contradicting reducedness), so the finite box searched is
exhaustive. It then checks the ρ-operator is a permutation of the enumerated
set (closure + bijectivity asserted per D) and counts its cycles; the number of
cycles is the narrow class number h⁺ (standard: ρ-cycles ↔ narrow classes of
the indefinite order, and D = pq ≡ 1 mod 4 is fundamental so this is the field's
narrow class group). The continued-fraction period ℓ of √D gives the norm of
the fundamental unit: ℓ even forces N(ε) = +1 and h = h⁺/2; ℓ odd forces
N(ε) = −1 and h = h⁺.

Result: all 161 periods are even (so h = h⁺/2 throughout), all h⁺ are even
(consistent with genus theory: narrow 2-rank t−1 = 1), and every ordinary class
number is odd: 143 × h=1, 13 × h=3, 4 × h=5, 1 × h=7. Hence v2(h) = 0 and the
ordinary 4-rank is 0 for all 161 fields — confirming §2 and additionally ruling
out V4.

Calibration: the routine reproduces standard values (D = 21, 33, 57, 69, 77, 93
all h=1; D = 65, 85 h=2 for mixed-sign controls outside the window where
applicable).

### 4. Conclusion

Because no field in the window has ordinary 4-rank 1, the "least field with
4-rank 1" does not exist, and the positive C4-with-generator claim is
rigorously false. This is a complete TARGET resolution by disproof (a rigorous
proof that the target is impossible/false), returned immediately per protocol.

## Replay

`python3 output/artifacts/verify.py` → prints `VERIFY_OK` (< 1 s, stdlib only).
It asserts, per field: A·B = −1, Rédei rank 1, ρ a permutation (closure +
bijectivity), period/units consistency, h odd, and writes
`output/artifacts/table.json` (161 rows with per-field symbols, ranks, class
numbers, periods).

## Why the admission-time expectation failed (for the record)

The admission preflight expected "early pairs already split between forced-zero
and ambiguous cases." The opposite-sign lemma above shows this is impossible:
when both primes are 3 mod 4, reciprocity forces the two Rédei symbols to be
opposite in **every** case, so the rank is pinned at 1 and the 4-rank at 0
window-wide. The window is vacuous for 4-rank 1 — a structural fact, not a
computation failure.

## Limitations / uncertainty

- The class-number certificate uses the ρ-cycle count on reduced indefinite
  forms (a standard theorem: cycles ↔ narrow classes) plus the CF-period parity
  for h⁺ → h; both steps are machine-asserted per field in the replay script.
- The disproof needs no unramifiedness analysis, no norm-equation search, and
  no beta: there is no field to attach a generator to.
- Scope is strictly the stated window (pq < 2500, both 3 mod 4); nothing is
  claimed about other congruence families or larger bounds.
