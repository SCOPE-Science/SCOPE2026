# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Vanishing q-derivative for Beffara's mixed-percolation interpolation from centered-square site to square-lattice bond percolation
- **Round:** 2026-09-14-hands-on-first-light-01
- **Lane:** 20448
- **Disposition:** NO_RESULT
- **Domain:** Probability Theory
- **Method:** stochastic coupling and conformal martingale analysis

## Problem

Let G_s be the centered square lattice with type-I vertices Z^2 open with p=1/2, type-II face-centres open with probability q, type-III face-centres open with probability 1-q, independently; write P_{1/2,q} for mixed percolation. Fix a continuum conformal rectangle (Omega,A,B,C,D) and its delta-mesh discretization Omega_delta, and let U_delta be the open-chain crossing from arc AB to arc CD. For an interior type-II vertex v and its one-step translate v'=v+(delta,0) of type III, prove Delta_delta(v)=P_{1/2,q}[v in Piv(U_delta)]-P_{1/2,q}[v' in Piv(U_delta)]=o(delta^2), uniformly in q in [0,1] and uniformly for v bounded away from the boundary and corners, so that d/dq P_{1/2,q}[U_delta] -> 0 in Beffara Eq. (5.2) and the delta->0 crossing limits at q=0 (critical bond percolation on Z^2) and q=1/2 (critical site percolation on G_s) coincide whenever one exists.

## Attempted claim

Let G_s be the centered square lattice with type-I vertices Z^2 open with p=1/2, type-II face-centres open with probability q, type-III face-centres open with probability 1-q, independently; write P_{1/2,q} for mixed percolation. Fix a continuum conformal rectangle (Omega,A,B,C,D) and its delta-mesh discretization Omega_delta, and let U_delta be the open-chain crossing from arc AB to arc CD. For an interior type-II vertex v and its one-step translate v'=v+(delta,0) of type III, prove Delta_delta(v)=P_{1/2,q}[v in Piv(U_delta)]-P_{1/2,q}[v' in Piv(U_delta)]=o(delta^2), uniformly in q in [0,1] and uniformly for v bounded away from the boundary and corners, so that d/dq P_{1/2,q}[U_delta] -> 0 in Beffara Eq. (5.2) and the delta->0 crossing limits at q=0 (critical bond percolation on Z^2) and q=1/2 (critical site percolation on G_s) coincide whenever one exists.

## Research outcome

Target blocked: uniform per-pair pivotal cancellation needs relative precision beyond available symmetry and RSW/quasi-multiplicativity technology; corrected full-adjacency numerics show plausibility but no proof route remains, and no independently valuable emergent result was produced.

## Why this attempt failed

Failed axes: no independent audit (NO_RESULT).

The uniform per-pair little-o bound Delta_delta(v) = o(delta^2) remains unproved: no fixed-q local symmetry exists, four-arm methods fall three-quarters of an exponent short, and the corrected simulations plus exact tiny-domain enumerations corroborate plausibility without constituting proof. An early falsification signal was traced to a truncated-graph artifact and retracted.

## Conditions for a legitimate retry

introduce a materially new method or a justified, still-valuable revised claim; address the recorded limitation: The uniform per-pair little-o bound Delta_delta(v) = o(delta^2) remains unproved: no fixed-q local symmetry exists, four-arm methods fall three-quarters of an exponent short, and the corrected simulations plus exact tiny-domain enumerations corroborate plausibility without constituting proof. An early falsification signal was traced to a truncated-graph artifact and retracted.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
