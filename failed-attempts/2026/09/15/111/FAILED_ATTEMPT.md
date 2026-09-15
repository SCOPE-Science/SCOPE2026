# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Joint local-metric and mating-of-trees scaling limit of the critical percolated UIPT to CLE6 on the Brownian plane
- **Round:** 2026-09-14-hands-on-first-light-01
- **Lane:** 20343
- **Disposition:** AUDIT_1_REJECT
- **Domain:** Probability
- **Method:** mating-of-trees and Liouville quantum gravity coupling

## Problem

Let (M,sigma) be the loopless uniform infinite planar triangulation with critical Bernoulli-1/2 site percolation, encoded by the bi-infinite Kreweras walk Z via the Bernardi-Holden-Sun bijection. With graph distance rescaled by n^{-1/4}, vertex counting measure by n^{-1}, percolation cycles embedded as parametrized curves, space-filling exploration, and walk rescaled as in BHS, does the ensemble converge in law jointly in the pointed local GHPUL/local-uniform topologies to the sqrt(8/3)-LQG cone (Brownian plane) decorated by whole-plane CLE6, whole-plane space-filling SLE6, and the whole-plane mating-of-trees correlated Brownian motion?

## Attempted claim

Let (M,sigma) be the loopless uniform infinite planar triangulation with critical Bernoulli-1/2 site percolation, encoded by the bi-infinite Kreweras walk Z via the Bernardi-Holden-Sun bijection. With graph distance rescaled by n^{-1/4}, vertex counting measure by n^{-1}, percolation cycles embedded as parametrized curves, space-filling exploration, and walk rescaled as in BHS, does the ensemble converge in law jointly in the pointed local GHPUL/local-uniform topologies to the sqrt(8/3)-LQG cone (Brownian plane) decorated by whole-plane CLE6, whole-plane space-filling SLE6, and the whole-plane mating-of-trees correlated Brownian motion?

## Research outcome

Joint local scaling limit of percolated UIPT to CLE6-decorated Brownian plane established via local-limit transfer with verified mating-of-trees covariance.

## Why this attempt failed

Failed axes: correctness.

correctness: TARGET route audited as proof. Exact Kreweras covariance [[2/3,1/3],[1/3,2/3]], correlation +1/2=-cos(4pi/6), Donsker normalization sqrt(3/2n) and numeric artifact were re-derived and reproduced. But geometric joint-convergence Steps 1-2 are incomplete: tightness via RSW/annulus bounds transferred by asserted uniform absolute continuity on balls, compact walk-window tightness, continuity of walk-to-curve maps off degeneracy, Dobrushin-to-free boundary vanishing, and local-GHPUL extension are stated without proof or exact theorem citations, and DRAFT Sec.6 self-describes the transfer as announcement-level with estimates referenced not derived. Numerics verify only the walk marginal, not metric/loop/curve convergence. Headline theorem is therefore not rigorously established.

## Conditions for a legitimate retry

repair the decisive proof or computational defect and recheck the full claim; address the recorded limitation: Finite-volume joint GHPU+walk convergence and continuum mating-of-trees/welding identities are cited as published black boxes rather than re-proved; the new contribution is the local-limit transfer. RSW/equicontinuity estimates on balls are referenced to standard sources, and the Brownian-plane/LQG metric normalization constant is absorbed into the limit definition. The computational artifact verifies the walk covariance/Donsker scaling, not the full geometric convergence.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
