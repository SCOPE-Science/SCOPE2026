# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Explicit linear distance and single-shot soundness from logged coboundary expansion for a practical-length dihedral quantum Tanner subfamily
- **Round:** 2026-09-07-first-light-01
- **Lane:** 719
- **Disposition:** NO_RESULT
- **Domain:** Quantum Coding Theory
- **Method:** quantum Tanner chain-complex homology with coboundary-expansion estimation

## Problem

Connect high-dimensional expansion to quantum LDPC performance for one named practical-length family: via a logged coboundary-expansion estimate on the underlying classical Tanner complexes, prove an explicit linear-distance and single-shot soundness bound for a rate>=1/8 dihedral lifted-product quantum Tanner subfamily with n~400-1200.

## Attempted claim

For the named dihedral-group lifted-product quantum Tanner subfamily F (rate>=1/8, block lengths n with 400<=n<=1200, generators A,B, group G, and local codes CA,CB all logged), prove via a logged coboundary-expansion lower bound epsilon>0 on the classical factor Tanner complexes that every member satisfies quantum distance d>=c*n with explicit c>=0.02 and single-shot soundness: any syndrome error of weight w is explained by a data error of weight O(w) up to stabilizer, with explicit linear function logged.

## Research outcome

Target d>=0.02n blocked by arithmetic ceiling of stated reductions plus missing base instances; preset fallback (exact d0>=8 for logged n0 in [400,600]) directly attempted on three constructed dihedral Tanner Q0 instances (n=450, 400, 500) — each falsified by complete weight-4 logical scans, and the weight-<8 certificate wall was measured infeasible. CLEAN_EXIT with no claim.

## Why this attempt failed

Failed axes: no independent audit (NO_RESULT).

['Target blocked arithmetically: published PK/LZ reductions cap provable c at <=0.00284 (Delta=3, ideal expansion), >7x below c>=0.02; no n>=400 dihedral base instance exists in Radebold (max n=250, upper bounds only).', 'Fallback attempted and blocked: three constructed Q0 candidates (n=450/400/500) each have complete-certificate weight-4 logicals (d<=4); measured certification cost (21 h for weight 5 alone at n=500) blocks the no-logical-weight-<8 proof in-session.', 'No ILP/SAT/QDistRnd-certified solver available in environment; symmetry reduction (~40x) insufficient against 1e14-1e15-scale walls.', 'No original increment: ceilings are routine substitution; weight-4 logicals are byproducts of self-built codes.']

## Conditions for a legitimate retry

introduce a materially new method or a justified, still-valuable revised claim; address the recorded limitation: ['Target blocked arithmetically: published PK/LZ reductions cap provable c at <=0.00284 (Delta=3, ideal expansion), >7x below c>=0.02; no n>=400 dihedral base instance exists in Radebold (max n=250, upper bounds only).', 'Fallback attempted and blocked: three constructed Q0 candidates (n=450/400/500) each have complete-certificate weight-4 logicals (d<=4); measured certification cost (21 h for weight 5 alone at n=500) blocks the no-logical-weight-<8 proof in-session.', 'No ILP/SAT/QDistRnd-cert…

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
