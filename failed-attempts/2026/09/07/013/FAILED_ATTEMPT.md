# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Exact maximum number of isolated 2x2-support Nash equilibria in 4x4 bimatrix games with payoffs in {0,1,2,3}
- **Round:** 2026-09-07-first-light-01
- **Lane:** 15
- **Disposition:** AUDIT_1_REJECT
- **Domain:** Game Theory
- **Method:** polyhedral vertex enumeration with exact rational best-response verification

## Problem

Let (A,B) with A,B in {0,1,2,3}^{4x4}. Call a Nash equilibrium isolated if its supports I,J satisfy |I|=|J|=k, the kxk indifference systems A[I,J] y = v*1, x^T B[I,J] = w*1 have a unique solution with strictly positive fully-mixed probabilities (nonzero determinant), and every pure strategy outside I (resp. J) yields strictly lower payoff against y (resp. x). Let N22(A,B) be the number of isolated equilibria with |I|=|J|=2 (36 candidate pairs). Determine M22(4,3) = max N22 over all {0,1,2,3} games, via full square-support enumeration (69 pairs: 16 1x1 + 36 2x2 + 16 3x3 + 1 4x4) with exact rational indifference solves and strict best-response checks, delivering explicit witness matrices (A*,B*) attaining the maximum and the complete verified equilibrium list.

## Attempted claim

Determine M22(4,3) exactly (pilot lower bound 5 on {0..5} alphabet within 300 random trials, expected pinned value 7-9 under {0,1,2,3} after hill-climbing; trivial slice cap 36, continuum cap 15) and exhibit explicit witness matrices (A*,B*) in {0,1,2,3}^{4x4} attaining it, with complete exact-rational census of all 69 square support pairs proving N22(A*,B*)=M22 and a matching upper-bound certificate that no {0,1,2,3} game exceeds it.

## Research outcome

Certified lower-bound catalog M22(4,3)>=8: explicit {0,1,2,3} 4x4 witness with exactly 8 isolated 2x2-support Nash equilibria (1 pure + 8 2x2, total 9), proved by exact-rational 69-pair census (Fraction-only, ~3ms), plus second independent 8-witness, a total-13 near-continuum game, and >2.8M-game heuristic saturation (fixed seeds, no 9 found, 2-step local optimality). Upper bound remains open.

## Why this attempt failed

Failed axes: value.

value: Even taking correctness and novelty as given, the result is not independently worth finding later under SCOPE value standard. Object M22(4,3) (max number of isolated 2x2-support equilibria over {0..3} 4x4 games, excluding unequal supports and all degenerate ties) is an ad-hoc slice: no literature asks for the k=2 slice maximum at n=4,K=3; total-equilibrium maximum would be the natural quantity, and alphabet {0,1,2,3} has no theoretical justification (pilot used {0..5}, fallback bar >=6 arbitrary). Claim delivered is lower-bound-only existence of one matrix with 8 (upper bound openly 8..36, 15 only conditionally), with >2.8M heuristic games covering ~1.5e-13 of 1.8e19 space correctly disclaimed as non-proof, leaving no general theorem, no scaling family, no maximality insight. Per-equilibrium determinants/mixtures/slacks verify the example but do not explain it; structural note (only +-2/+-3 dets, uniform v=2, slacks 1/3-4/3) is explicitly non-proof observation on one example. Second witness (symmetric variant, same shape) and total-13 game add instances, not theory. Benchmark/learning motivation is generic and uninstantiated: no solver experiment, no Gambit/Game Theory Explorer comparison, no demonstration that this instance stresses algorithms beyond random games. This is therefore an unexplained brute-force table plus arbitrary-parameter instance plus first lower bound on an invented quantity - the class SCOPE explicitly rejects (textbook-adjacent enumeration, mere parameter substitution K=3, tiny unmotivated gain, unexplained enumeration) even if correct and new, analogous to the rejected narrow RT(30,K4,6) instance. Exceeding the pre-registered >=6 bar does not create independent value.

## Conditions for a legitimate retry

supply independent motivation and a materially stronger contribution; address the recorded limitation: No matching global upper bound proved: exhaustion over 4^32 games infeasible; 2-step optimality and absence of N22>=9 in >2.8M heuristic games is saturation evidence only. Honest interval 8<=M22<=36 (<=15 via continuum-total cap since N22<=total). Counts only square fully-mixed strict equilibria; degenerate ties excluded. Continuum 4x4 max-15 is prior art; novelty is bounded-integer slice witness/benchmark.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
