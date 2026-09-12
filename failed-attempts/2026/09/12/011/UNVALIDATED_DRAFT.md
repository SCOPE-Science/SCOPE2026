# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# First exact census and insertion-encoding state-complexity obstruction for the 4231-anchored sibling pair Av(4231,3124) vs Av(4231,3214)

## 1. Claim

Let A = Av(4231,3124) and B = Av(4231,3214) be the classical two-pattern
classes with the shared anchor 4231. Then:

(a) **Exact census.** The avoider counts |A_n| and |B_n| for n = 0..15 (A) and
n = 0..12 (B, dual-verified) are

| n | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 |
|---|---|---|---|---|---|---|---|---|---|---|----|----|----|----|----|----|
| A | 1 | 1 | 2 | 6 | 22 | 88 | 363 | 1508 | 6255 | 25842 | 106327 | 435965 | 1782733 | 7275351 | 29648647 | 120707058 |
| B | 1 | 1 | 2 | 6 | 22 | 87 | 352 | 1428 | 5768 | 23156 | 92416 | 367007 | 1451780 | 5725959 | 22535868 | 88566290 |

Rows n = 0..12 are byte-identical across two independently written C engines
(`census.c`: max-insertion DFS with the incremental slot lemma, values
0..n-1; `verify_brute.c`: max-insertion DFS re-scanning every index
quadruple with ranking, values 1..n), and rows n = 0..8 agree with a third
independent Python brute-force enumerator (`xcheck.py`) that checks every
quadruple of every candidate permutation. In particular the admission anchors
(n=6: 363 vs 352; n=7: 1508 vs 1428; n=8: 6255 vs 5768) are confirmed, and the
new terms n = 9..15 are: A: 25842, 106327, 435965, 1782733, 7275351,
29648647, 120707058; B: 23156, 92416, 367007, 1451780, 5725959, 22535868,
88566290.

(b) **Finite-data direction.** A_n > B_n for every 5 <= n <= 15, with the
ratio A_n/B_n widening monotonically (1.011, 1.031, 1.056, 1.084, 1.116,
1.151, 1.188, 1.228, 1.271, 1.316, 1.363); successive ratios at n=15 are
4.071 (A) vs 3.930 (B) and 15th roots are 3.458 (A) vs 3.387 (B). Hence no
ratio- or root-based argument from this data can prove gr(A) < gr(B); the
finite data uniformly favors the opposite ordering.

(c) **Coarse-profile automaton impossibility (structural obstruction).**
The length-<=3 subsequence-occurrence profile cannot serve as an
insertion-encoding state for either class. Minimal hand-checkable witness
(class A, n=7): the avoiders 6.5.4.3.2.7.1 and 6.5.4.3.7.2.1 have IDENTICAL
length-<=3 occurrence profiles but different futures — 3 children and 11
grandchildren vs 4 children and 17 grandchildren — so no well-defined
deterministic quotient transition exists on profiles. Consequences:
- the first-representative profile quotient undercounts class A at n=7
  (1266 walks vs the exact 1508), missing 242 permutations;
- 29 distinct length-<=3 profiles at n=7 (class A) conflate permutations with
  provably different futures (different child-count/grandchild multisets);
  class B shows 22 such divergent profiles;
- (Myhill–Nerode lower bound) the number of distinct depth-2 future
  signatures (#children, #grandchildren) grows strictly with n while the
  number of coarse profiles saturates at 45:

| n | 5 | 6 | 7 | 8 |
|---|---|---|---|---|
| A signatures | 20 | 33 | 50 | 71 |
| B signatures | 25 | 44 | 73 | 112 |
| coarse profiles (both) | 42/41 | 45 | 45 | 45 |

Since two permutations with different (#children, #grandchildren) cannot
share an insertion-encoding DFA state, class B needs at least 112
Myhill–Nerode states already at depth 8 — more than twice the 45 available
coarse profiles. A bounded-future signature-state BFS (depth-2 signatures as
states) exceeded time/memory limits (>10 min, no stabilization), documenting
that the "small regular DFA + disjoint Perron enclosure" route is concretely
obstructed for this pair within feasible computation.

## 2. Methods (replay)

- `artifacts/census.c` — build `gcc -O2 -fopenmp census.c -o census_par`,
  run `./census_par 15 9 > census_n15.csv`. Lemma used: when inserting the new
  maximum n (value 4 in every forbidden pattern), a 4231-occurrence must place
  the new element first, so only triples after the slot are tested for 231;
  a 3124/3214-occurrence must place it last, so only triples before the slot
  are tested for 312/321. Parallel over frontier at depth 9. Timings: n=15 in
  ~7 s wall (32 threads).
- `artifacts/verify_brute.c` — build `gcc -O2 -fopenmp verify_brute.c -o
  verify_brute`, run `./verify_brute 12 8 > verify_n12.csv`. Independent:
  values 1..n, every index quadruple ranked and compared against all three
  forbidden patterns at every node. Rows 0..12 byte-identical to census.c.
- `artifacts/xcheck.py` — `python3 xcheck.py 8`; third independent check to
  n=8 (iterative max-insertion with `itertools.combinations` pattern test).
- `artifacts/sig_complexity.py` — `python3 sig_complexity.py`; recomputes the
  signature/profile table above (`sig_table.txt`).
- `artifacts/ie_overcount.py` — `python3 ie_overcount.py` (`ie_overcount.log`);
  certifies profile-quotient inexactness (representative quotient: 1266 vs
  exact 1508), prints the hand-checkable witness pair and all divergent
  profiles, and replays the signature table.

## 3. Proofs and lemmas

**Lemma 1 (incremental insertion check, used by census.c).** Inserting a new
maximum element m into an avoider can create a forbidden length-4 pattern
only with m playing value-role 4. For 4231 the 4 is in position 1, so only
index triples strictly after the insertion slot can complete a new
occurrence (checked for pattern 231); for 3124/3214 the 4 is in position 4,
so only triples strictly before the slot can (checked for 312/321).
*Proof.* Direct from the definition of pattern involvement: the new maximum
is the largest value, hence must assume the largest value-role. ∎

**Lemma 2 (signature lower bound).** If two avoiders p, q have different
pairs (e1, e2) = (#live children, #live grandchildren), their future
insertion languages differ, so no deterministic insertion-encoding automaton
accepting exactly the class can assign them the same state.
*Proof.* A DFA state determines the counting generating function of all
accepted continuations; e1 is the number of length-1 continuations and e2 the
number of length-2 continuations, both read off the state. ∎

**Corollary.** The table in (c) gives certified lower bounds: at depth 8,
class A needs ≥71 IE-states and class B ≥112 IE-states; the 45-state
length-≤3-profile quotient is therefore not an exact automaton for either
class (it is additionally inexact: the representative quotient gives 1266).

## 4. What is NOT claimed

- No Stanley–Wilf limit or growth-rate inequality in either direction is
  proved. The census direction (A ahead of B through n=15) is finite evidence
  only and does not imply gr(A) ≥ gr(B).
- No (non-)regularity theorem for either insertion language is proved; the
  obstruction is a certified lower-bound/overcount pair against the natural
  coarse-profile DFA route, plus documented non-stabilization of the
  depth-2 signature quotient within the compute budget.
- Growth constants, transfer matrices, and Perron enclosures are explicitly
  absent: they were the blocked target route.

## 5. Originality and value

No located source (exact-pair, spectral/singularity-equivalent, broader
4231-family, or tabular/OEIS searches per the admission record) publishes
enumeration of Av(4231,3124) or Av(4231,3214) beyond the n≤8 anchors, let
alone side-by-side census to n=12–15, and no source records the
coarse-profile DFA impossibility for this pair. The census gives the first
benchmark rows for the 4231-anchored Wilf-growth atlas; the obstruction lemma
steers future automaton attacks away from the coarse-profile route and toward
exact Myhill–Nerode state analysis, and it explains *why* the admitted target
(DFA + disjoint Perron enclosures proving gr(A) < gr(B)) is blocked: the
required automata are large (≥112 states already forced at depth 8 for B)
while all finite data favors the reverse inequality.

## 6. Limitations

- Census extends only to n=15 (A) / n=15 single-engine with dual verification
  to n=12; no asymptotic claim follows.
- The obstruction rules out only the length-≤3-profile quotient route and
  lower-bounds exact IE-state counts; it does not decide regularity.
- Pure-Python signature BFS beyond n=8 was compute-limited; tighter bounds
  need a compiled implementation.
