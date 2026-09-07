# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Digit-restricted order-2 bases for Z_197 inside decimal digits {0-4}: annealed size-22 construction with exact covering verification
- **Round:** 2026-09-07-first-light-01
- **Lane:** 2
- **Disposition:** AUDIT_1_REJECT
- **Domain:** Number Theory
- **Method:** heuristic constructive search with deterministic covering verification

## Problem

Let p=197 (prime below 200) and U = {x in [0,196] : decimal expansion of x uses only digits 0,1,2,3,4}. Then |U|=50 (25 in [0,99] plus 25 in [100,144]). A set A subset of U is an order-2 digit-restricted additive basis if S(A) = {(a+b) mod 197 : a,b in A} equals all of Z_197, i.e. the translates {a+A} cover Z_197. Triangular counting gives |A|(|A|+1)/2 >= 197 so |A| >= 20 (19*20/2=190<197<=210=20*21/2). Find by simulated annealing over subsets of U plus greedy completion/reduction an explicit A with |A| <= 22 and S(A)=Z_197, certified by deterministic exact-integer covering check. Survey companions p in {173,179,181,191,193} with D_3/D_4 for threshold table.

## Attempted claim

Exhibit an explicit subset A of U(197,10,{0,1,2,3,4}) with |A| <= 22 (stretch goal 21) such that the 253 unordered sums (a+b) mod 197 cover all 197 residues, i.e. A+A=Z_197. Deliver the sorted list of A, the sorted 197-element sumset, and a <60s exact-integer verification script plus annealing seeds and greedy baseline (expected greedy 25-27) showing a 3+ element improvement and only 2 above the triangular optimum 20. This is an improved explicit upper-bound construction: 22 << 50 (trivial) and < greedy.

## Research outcome

Refuted the assigned size-22 digit-restricted basis for Z_197: proved no order-2 basis inside decimal digits {0-4} exists for any p in {173,179,181,191,193,197} x D2/D3/D4 (interval-gap proof for p>=191, exact full-universe + counting certificates otherwise), and delivered a certified threshold/maximal-coverage table with annealed best sets (22-set best 163/197) and 50-run greedy baselines, all exactly verified.

## Why this attempt failed

Failed axes: value.

value: Correct and narrowly new, but not independently worth finding later. (i) What was assigned as improved explicit upper bound (size<=22 basis, 2 above triangular optimum 20, redundancy 253/197=1.28 suggesting feasibility) is FALSE; replacement is 18-cell non-existence table. Theorem A is a 5-line envelope observation: once [0,44] U [100,144] is noted, gaps follow by r/r+p casework with no further theory. It is not developed into a general lemma (arbitrary alphabets, bases, p), gives only 16/8/4 residues for 3 primes, and would be derived in minutes before any annealing — it reveals poor parameter choice rather than a phenomenon. (ii) Theorem B is brute-force enumeration of <=2500 modular sums per cell (<2s total) for an ad-hoc slice: same 50/32/18-element universes across all p (since max 144<173, only modulus varies), decimal alphabet {0-4} and 6 primes <200 have no demonstrated coding/coin/covering application (coding uses binary/ternary, Maynard link is asymptotic vs finite, tenuous). Values like |S(U)|=165 vs 171 vs 173 are reported without conceptual explanation beyond 'computer says', i.e. a parameter sweep. (iii) Heuristic SA/greedy numbers are explicitly non-optimal by DRAFT's own admission (true k=22 max in [163,173]; companions best-found at 20x200k / 8x80k budgets), so they are unstable algorithm-performance snapshots at arbitrary budgets, not citable maxima; future budgets can improve them up to the known ceiling but never to p, so no later work would search for or cite '163/197 at seeds 1000-1019'. Even ceiling-achieving cases (p197/D3 k20=119=ceiling, p191/D3 k20=111=ceiling) achieve only incomplete ceilings (60%/58%), not bases. (iv) This combines the reject categories: mere parameter substitution (same U, varied modulus; single decimal-alphabet slice) plus small exact enumeration that is explained by scripts but not by theory, with no generalizable insight, no application, and no stable positive record. A future researcher on constrained-alphabet bases would re-derive the interval obstruction in seconds and would not need to retrieve this 6-prime table. Hence fails 'independently worth finding later' even though correct and new.

## Conditions for a legitimate retry

supply independent motivation and a materially stronger contribution; address the recorded limitation: Result is specific to decimal alphabets D2/D3/D4 and p in {173,179,181,191,193,197}; no claim for other alphabets or p. Exact certificates assume script correctness (short auditable code with boolean-array cross-check). Annealed coverages are verified lower bounds on maxima (existence), not proven optima; larger budgets might improve them up to the |S(U)| ceiling but can never reach p. No live-web priority check was possible; no priority/originality claim beyond triage separation stated in DRAF…

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
