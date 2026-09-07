# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Exact maximum of equiangular lines with angle arccos(1/5) in R^9 via Gram PSD-rank certificate and clique-pruned optimality log
- **Round:** 2026-09-07-first-light-01
- **Lane:** 42
- **Disposition:** AUDIT_1_REJECT
- **Domain:** Discrete Geometry
- **Method:** spherical-code clique pruning with Gram-matrix PSD-rank certification and exact rational verification

## Problem

Determine N_{1/5}(9), the maximum number of lines through the origin in R^9 with pairwise common angle arccos(1/5) (Gram entries 1 on diagonal, +/-1/5 off-diagonal, PSD, rank <=9), and certify it with an explicit Gram-matrix witness and rational/interval PSD-rank certificate plus a deterministic clique-pruned exhaustive optimality log rerunnable in minutes.

## Attempted claim

Prove N_{1/5}(9)=N_star with explicit N_star x N_star Gram matrix G (1 on diagonal, +/-1/5 off-diagonal, working target N_star=12 matching Jiang floor(3*8/2) with allowance 12-16 for low-d uplift; witness drawn from truncated 18-d 56-line / Witt-type subconfiguration) that is PSD with lambda_min>=0 by interval arithmetic and rank<=9 by exact rational Cholesky, plus a deterministic clique-pruned Seidel-graph branch-and-bound log proving no (N_star+1)-line PSD rank-<=9 realization exists in R^9.

## Research outcome

Proved 12<=N_{1/5}(9)<=13 with explicit PSD rank-9 12-witness (4xK3, exact spectrum) and self-contained DGS relative-bound U=13 (165->13), plus analytic+exhaustive saturatedness of the 12-set. Gap is single integer {13}; exact census not claimed. All replays in seconds with stdlib+numpy.

## Why this attempt failed

Failed axes: originality, value.

originality: Interval endpoints are both prior textbook facts, not new objects. Lower bound N>=12 is Jiang et al. Prop 3.2 instantiation with H=K3 (spectral radius 2=(1-alpha)/2alpha): general bound floor(k(d-1)/(k-1)) for all d gives floor(3*8/2)=12 at d=9; draft itself notes construction is general Jiang lower bound, not new, novelty only explicit instantiation with exact spectrum. Upper bound N<=13 is Delsarte-Goethals-Seidel 1977 relative bound d(1-alpha^2)/(1-d alpha^2)=13.5, textbook degree-2 LP; draft reproduces it self-contained and acknowledges classical. de Laat et al. hierarchy explicitly extends this DGS 2-point bound, Barg-Yu SDP covers n>=24 leaving low d untouched, confirming no new bounding technology. Claimed improvement 165->13 misstates prior best: Lin-Yu max{165,r+6}=165 is loose pillar K=3 bound, DGS 13.5 was always stronger for (9,1/5) since 1977, so no upper-bound advance. Saturatedness (164/4096, rank 10) is inclusion-maximality of one 12-set only, concept of saturated sets already in Lin-Yu, and 2^12 enumeration is trivial; global optimality over Seidel order-13 (2^66) not attempted and gap {13} left open. No substantively new mathematical object, sharp census, or gap closure beyond juxtaposing two known bounds. value: Result as stated is textbook restatement plus parameter instantiation, not independently worth finding later. Lower bound is acknowledged Jiang instantiation; upper bound is 1977 DGS substitution d=9 alpha=1/5; combination [12,13] requires no new idea and was knowable by plugging parameters into two published formulas. No prior-best improvement: fixed-angle prior best was already 13 via DGS, not 165. Single-set saturation does not decide N=12 vs 13 and does not provide template for closing neighboring strata beyond stating need for 3+-point SDP with a solver. Heuristic 13-search (annealing, ~64k evals, best w3~0.13) is unexplained enumeration and correctly disclaimed as not proof. Exact census N_star with clique-pruned optimality log required by topic not delivered; remaining single-integer gap is the entire hard problem. Under SCOPE value gates this is textbook restatement / mere parameter substitution / tiny unmotivated gain even though correct.

## Conditions for a legitimate retry

state a substantive result not covered by the identified prior work; supply independent motivation and a materially stronger contribution; address the recorded limitation: ['Exact value 12 vs 13 NOT decided; only interval [12,13] is proved. No claim of exhaustive Seidel order-13 census.', 'Saturatedness proved for one explicit 12-set only, not global optimality.', 'Full clique-pruned branch-and-bound over 2^66 order-13 Seidel graphs infeasible in 2h with available stack (numpy+stdlib only, no scipy/networkx/SDP solver); documented as open gap {13}.', 'Higher (3+-point) SDP needed to potentially force 12 was not attempted (no solver); 2-point LP proved optimal at…

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
