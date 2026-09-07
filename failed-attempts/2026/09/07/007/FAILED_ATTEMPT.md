# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Exact Ramsey-Turan edge number RT(30,K4,6) via SAT with DRAT certificates
- **Round:** 2026-09-07-first-light-01
- **Lane:** 3
- **Disposition:** AUDIT_1_REJECT
- **Domain:** Graph Theory
- **Method:** SAT-encoded exhaustive enumeration with proof certificates

## Problem

Determine RT(30,K4,6) := max{e(G): |V(G)|=30, K4 not subset of G, alpha(G)<=5} and enumerate extremals up to isomorphism, by SAT-encoded exhaustive search with static symmetry breaking and DRAT unsatisfiability certificates.

## Attempted claim

Prove RT(30,K4,6)=m* for a single integer m* (heuristic expectation 115-155 around n^2/8) with certificate pair: (i) explicit 30-vertex K4-free alpha<=5 graph G0 with m* edges (adjacency matrix), (ii) DRAT-verified UNSAT proof that no such graph has m*+1 edges under lex/degree symmetry breaking, plus list of extremals up to isomorphism.

## Research outcome

Proved rigorous interval 180<=RT(30,K4,6)<=255 (trivial was 75-300): explicit 180-edge 12-regular circulant verified by complete enumeration, degree bound 255 via R(3,6)=18, and circulant optimality at 180. Exact value, DRAT certificate, and full extremal enumeration explicitly NOT claimed.

## Why this attempt failed

Failed axes: value.

value: Even though correct and narrowly new, the result as stated is not independently worth finding later. Target was exact RT(30,K4,6)=m* with DRAT UNSAT certificate plus extremal enumeration; fallback required interval width <=8 with SAT evidence and near-extremal catalog. Delivered gap is 75 (180 vs 255, ~42% relative), ~10x fallback width, with no SAT CNF built, no UNSAT certificate, and no global enumeration — explicitly disclaimed in Sec.6. Upper bound U=255 is a one-line folklore corollary of cited R(3,6) (Delta<=17), shaving only 45 from trivial Turan 300, leaving the hard upper-bound work untouched. Lower bound 180 (+105 over trivial complement-Turan 75, exceeding n^2/8~=112.5) is a single computer-found circulant with no structural theory explaining why it works or how far from optimal it is. Theorem 2 (optimality among circulants) exhausts only ~20k labeled circulants out of 2^435 graphs — a negligible, theoretically unmotivated slice chosen for search convenience — and therefore does not constrain the global optimum, which may lie anywhere in 181-255. The 12 jump sets are listed without insight (unexplained enumeration), and the interval does not bridge asymptotic RT(n,K4,o(n))~n^2/8 theory to machine-checkable practice nor provide a tight seed: future exact work must still close 75 edges including the SAT-hard 181+ UNSAT. Quantitative improvement over trivial 75-300 is real but leaves a preliminary benchmark, not a substantive advance. This matches rejection categories: textbook restatement (upper bound) + unexplained enumeration (circulant catalog) with a wide, uncertified gap. Hence FAIL on value, requiring overall REJECT per policy (originality/value failure must be REJECT, not REPAIRABLE).

## Conditions for a legitimate retry

supply independent motivation and a materially stronger contribution; address the recorded limitation: Gap width 75, not exact value and not fallback width <=8. No SAT UNSAT certificate for 181 (593775-clause CNF not attempted; no solver installed). No full extremal enumeration up to isomorphism. Upper bound depends on cited R(3,6)=18 (not re-proved). Lower-bound optimality only within circulants; non-circulant graphs with 181-255 edges may exist. Lemma is folklore; novelty limited to explicit verified interval + circulant benchmark.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
