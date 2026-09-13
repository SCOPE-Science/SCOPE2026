# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Pants Hitchin vs same-boundary Fuchsian figure-eight domination
- **Round:** 2026-09-07-first-light-01
- **Lane:** 1554
- **Disposition:** AUDIT_1_REJECT
- **Domain:** higher Teichmuller theory
- **Method:** Fock-Goncharov weight-matrix monodromy and cross-ratio bounds

## Problem

Let P be the pair of pants (three-holed sphere) with fixed boundary loops g1,g2,g3. Consider the set R of positive representations rho: pi1(P)->PSL(3,R) with loxodromic boundary holonomy, in Fock-Goncharov coordinates on the standard two-triangle triangulation (positive shear/cross-ratio coordinates on the three internal edges and two positive triangle invariants), with Labourie cross-ratios from the boundary framing. Fix the cuff pair (g1,g2) and the fixed interior seam word w=g1*g2 (figure-eight curve). For each rho let J(rho) be the Fuchsian (hyperbolic) pants representation into PSL(2,R)<PSL(3,R) with the same three boundary Hilbert lengths H_rho(gi)=log|lambda1/lambda3|, which exists and is unique up to conjugacy. Decide the domination inequality: for every rho in R, is H_rho(w) >= H_{J(rho)}(w), with both sides computed as log of eigenvalue-modulus ratio, decidable from explicit Fock-Goncharov weight-matrix monodromy formulas and positivity/cross-ratio bounds? Scope is all positive coordinates with all boundary holonomies loxodromic (no cusp restriction). A complete answer is either a general proof of the inequality for all such rho, or an explicit positive coordinate tuple with rigorously computed H_rho(w) and H_{J(rho)}(w) giving strict reverse inequality.

## Attempted claim

Let P be the pair of pants (three-holed sphere) with fixed boundary loops g1,g2,g3. Consider the set R of positive representations rho: pi1(P)->PSL(3,R) with loxodromic boundary holonomy, in Fock-Goncharov coordinates on the standard two-triangle triangulation (positive shear/cross-ratio coordinates on the three internal edges and two positive triangle invariants), with Labourie cross-ratios from the boundary framing. Fix the cuff pair (g1,g2) and the fixed interior seam word w=g1*g2 (figure-eight curve). For each rho let J(rho) be the Fuchsian (hyperbolic) pants representation into PSL(2,R)<PSL(3,R) with the same three boundary Hilbert lengths H_rho(gi)=log|lambda1/lambda3|, which exists and is unique up to conjugacy. Decide the domination inequality: for every rho in R, is H_rho(w) >= H_{J(rho)}(w), with both sides computed as log of eigenvalue-modulus ratio, decidable from explicit Fock-Goncharov weight-matrix monodromy formulas and positivity/cross-ratio bounds? Scope is all positive coordinates with all boundary holonomies loxodromic (no cusp restriction). A complete answer is either a general proof of the inequality for all such rho, or an explicit positive coordinate tuple with rigorously computed H_rho(w) and H_{J(rho)}(w) giving strict reverse inequality.

## Research outcome

Decided the pants Hitchin-vs-Fuchsian domination target: the inequality holds for all positive loxodromic-boundary representations, in fact as an exact equality, because w=g1*g2 is conjugate to g3^{-1}.

## Why this attempt failed

Failed axes: value.

value: ADMISSION_DEFECT: target framed w=g1*g2 as interior figure-eight domination, but w is boundary-parallel by pants relation, so H_rho(w)>=H_J(w) collapses to definitional equality H_rho(g3)=H_J(g3) from J's construction. This is a type/normalization error and vacuity under STANDARD: textbook restatement mechanically implied by elementary group presentation plus eigenvalue invariance, with no FG estimates needed, no new boundary, no downstream use, and no independently retrievable invariant. Fixing it requires replacing w or surface, i.e. a new research direction, so intrinsic low value mandates REJECT.

## Conditions for a legitimate retry

supply independent motivation and a materially stronger contribution; address the recorded limitation: Result is for the literal word w=g1*g2 as stated; the label 'figure-eight' is a misnomer since this word is boundary-parallel on the pants. A genuinely interior self-intersecting word (e.g. a commutator) or a larger surface would pose a different domination problem not decided here. The argument needs loxodromic boundary so Hilbert lengths are finite and the Fuchsian match exists.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
