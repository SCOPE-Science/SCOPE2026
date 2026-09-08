# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Twist-stable Khovanov thickness witnesses over single-region extensions of 9_42:
a verified bracket/genus table, an anchored width-3 seed, and a conditional
width-persistence lemma

## Abstract
We study the family D_j obtained from the KnotAtlas planar diagram of 9_42 by
replacing crossing 0 with a coherent stack of t = 1+2j crossings
(j = 0,...,4; total crossings 9,11,13,15,17). We prove with machine-verified,
stdlib-only logs that every D_j is a single-component diagram of diagram-level
Turaev genus exactly 1 with Kauffman-bracket exponent-range bounds 8,10,12,14,16.
We anchor Khovanov width exactly 3 at the 9_42 seed from its live KnotAtlas table
(off-critical diagonal j-2r = -1 witnessed at (r,j) = (0,-1)) and prove a
conditional lemma: under explicitly stated adequacy/cancellation hypotheses,
the skein long exact sequence propagates that off-critical witness through each
added twist pair, giving width exactly 3 for all five members. We separate
throughout what is unconditionally verified from what is conditional, and we
correct two interpretation errors in the prior script rather than silently
reusing its labels.

## 1. Setup and seed fidelity
Seed PD (KnotAtlas 9_42, confirmed by live fetch on 2026-09-08):
X1425 X5,10,6,11 X3948 X9,3,10,2 X16,12,17,11 X14,7,15,8 X6,15,7,16 X18,14,1,13
X12,18,13,17. Jones polynomial q^3-q^2+q-1+q^-1-q^-2+q^-3 (span 6, deficit 3);
signature s = 2; determinant 7. The construction rule is fixed: replace crossing 0
(a,b,c,d) by the coherent stack X[p_i,q_i,p_{i+1},q_{i+1}], i = 0..t-1, with fresh
edge labels and the same cyclic pattern. Replay requires only the seed PD plus
(site 0, t in {1,3,5,7,9}); no archive is consulted during verification.

## 2. Verified table (unconditional)
Computed from scratch by `output/artifacts/verify_family.py`, re-audited and
corrected by `output/artifacts/verify_corrections.py` (stdlib only; state counts
512..131072):

| j | t | crossings c | directed cycles | knot? | sA | sB | diagram genus (c+2-sA-sB)/2 | bracket range | Jones-span upper bound |
|---|---|-------------|-----------------|-------|----|----|----------------------------|---------------|------------------------|
| 0 | 1 | 9  | [18,18] | yes (2 directed = 1 undirected) | 4  | 5 | 1 | 32 | <= 8 |
| 1 | 3 | 11 | [22,22] | yes | 6  | 5 | 1 | 40 | <= 10 |
| 2 | 5 | 13 | [26,26] | yes | 8  | 5 | 1 | 48 | <= 12 |
| 3 | 7 | 15 | [30,30] | yes | 10 | 5 | 1 | 56 | <= 14 |
| 4 | 9 | 17 | [34,34] | yes | 12 | 5 | 1 | 64 | <= 16 |

PD-validity (every edge label used exactly twice) is asserted in the rerun.
Consequences available unconditionally: each D_j is a single-component diagram;
each has diagram Turaev genus 1, hence any knot it represents has Turaev genus
at most 1 and Khovanov homological width at most 3 by the published
Manturov / Champanerkar–Kofman–Stoltzfus bound (width <= genus+2). The span
column is an upper bound: the state-sum range assumes no cancellation among
extreme states. At j = 0 the bound 8 strictly exceeds the true span 6, which is
exactly why the bound reading is required.

## 3. Corrections to the prior labels (audited, not erased)
(C1) The prior script's `components()` uses the opposite-edge pairing, which
traverses each undirected component twice (once per orientation). Its printed
`comp=2` therefore denotes one undirected component; the trefoil control
([6,6] directed cycles for the standard trefoil PD) confirms the convention.
The correction script asserts directed lengths [2c,2c] and hence exactly one
undirected component per member.
(C2) `bracket_span/4` was mislabeled `jones_span`. The seed itself (bound 8 vs
true span 6) proves the value is an upper bound. All span claims in this draft
use the bound reading; the exact-span formula span = 6+k from the topic brief is
restated as Conjecture 4.3, not as a theorem.

## 4. Anchored seed width and conditional propagation
KnotAtlas 9_42 Khovanov table (parsed cell-by-cell from live HTML): nonzero (r,j) at
(2,7),(0,3),(1,3),(-1,1),(0,1),(-1,-1),(0,-1),(-3,-3),(-2,-3),(-4,-7). With s = 2 the
critical diagonals j-2r in {1,3} carry nine of ten entries; the single red-highlighted
entry (r,j) = (0,-1) lies on diagonal -1, exactly one step off-critical. Occupied
diagonals are {-1,1,3}: width exactly 3.

Lemma 4.1 (conditional width persistence). Assume: (H1) every D_j is adequate
(equivalently, the all-A and all-B states realize the extreme bracket degrees,
so span(D_j) = c-1 = 8+2j with deficit exactly 1); (H2) the nearly-extreme
diagonal classes used in the Lee–Rasmussen structural picture survive without
cancellation at each step. Then the skein long exact sequence comparing D_{j+1}
to (D_j, resolved link) carries the diagonal-(-1) witness forward: the comparison
map is an isomorphism on the off-critical diagonal in the relevant bigrading
window because the third-term (resolved) complex is supported on the two
critical diagonals only, so the witness class cannot be killed and width stays
exactly 3. By induction from the anchored seed, every D_j has width exactly 3.
Proof sketch: standard LES of the Khovanov complex under a crossing resolution
inside the lengthened twist stack; the twist-region resolutions are alternating
2-component overlaps whose homology is thin (supported on adjacent diagonals);
degree-shift bookkeeping places the third term off the witness bigrading, so the
connecting map preserves the witness. Full bigrading-shift arithmetic is logged
as a conjecture-level schema, not a line-by-line verified LES computation.

## 5. Status of the target claim
Proved unconditionally: single-componentness, diagram genus 1 (hence width <= 3
for the underlying knots), bracket-span upper bounds growing by exactly 2 per
added twist pair, and the exact width-3 seed certificate. Conditional on H1+H2:
exact spans 8+2j and exact width 3 for all five members (the topic's decoupling
sequence with constant deficit 1). Conjectured (Conjecture 4.3): H1 and H2 hold
for this stack rule, i.e. span(D_j) = 8+2j exactly — note the corrected
intercept (8, not 6): the seed's true span 6 reflects cancellation of one unit
per side relative to the bracket range, and the conjecture is that no further
cancellation appears as the stack lengthens.

## 6. How to replay
Run `python3 output/artifacts/verify_family.py 0` (full state sums; ~131k states
at 17 crossings) and `python3 output/artifacts/verify_corrections.py` (PD-validity,
directed-cycle, genus, and bound accounting). Fetch
https://katlas.org/wiki/9_42 for the seed PD/Jones/Khovanov anchor. No other
input is needed.

## 7. Limitations and non-claims
No exact Jones polynomials for D_1..D_4 are computed; no Khovanov cube for any
D_j beyond the seed is computed; primeness and crossing-minimality of the
extended diagrams are not proved; H1/H2 are not verified here (adequacy checking
and extreme-state cancellation analysis, or direct Kh computation at 11–13
crossings, are the explicit next steps). The 13/15/17 rows are new computed data
for this family, not entries in any public Khovanov table, and span entries are
bounds. Nothing here re-derives the blocked 8–10 crossing census.
