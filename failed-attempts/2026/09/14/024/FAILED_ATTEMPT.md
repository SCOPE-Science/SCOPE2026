# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Ageometric index decomposition and IW components of a->bc,b->c,c->da,d->a in Out(F4)
- **Round:** 2026-09-07-first-light-01
- **Lane:** 1859
- **Disposition:** NO_RESULT
- **Domain:** geometric group theory, Out(F_n) train-track dynamics
- **Method:** relative train track with Perron-Frobenius data, full Nielsen-path survey, fixed-point/branch-point index computation

## Problem

Let F4 be the free group on basis {a,b,c,d} and let Phi4 be the automorphism a->bc, b->c, c->da, d->a (composition of transvections a->ab and c->cd with the 4-cycle a->b->c->d->a, inducing phi4 in Out(F4)). Determine the full ageometric-index decomposition of phi4: prove whether phi4 is fully irreducible, atoroidal, and ageometric, and compute exactly the rotationless index list (one rational number per attracting lamination component, e.g. principal value 3/2-4 versus a nonprincipal multi-component list) together with the component structure of the ideal Whitehead graph IW(phi4) (number of components, vertex count totaling at most 7 for a connected case, and adjacency within each component). A complete answer certifies the train-track representative, its transition matrix and Perron-Frobenius data, the complete periodic-Nielsen-path survey, the fixed-point/branch-point index computation, and the exact componentwise graph identification, or refutes a component of the claim with an explicit witness (reduction, periodic class, or Nielsen path). Rank is fixed at 4.

## Attempted claim

Let F4 be the free group on basis {a,b,c,d} and let Phi4 be the automorphism a->bc, b->c, c->da, d->a (composition of transvections a->ab and c->cd with the 4-cycle a->b->c->d->a, inducing phi4 in Out(F4)). Determine the full ageometric-index decomposition of phi4: prove whether phi4 is fully irreducible, atoroidal, and ageometric, and compute exactly the rotationless index list (one rational number per attracting lamination component, e.g. principal value 3/2-4 versus a nonprincipal multi-component list) together with the component structure of the ideal Whitehead graph IW(phi4) (number of components, vertex count totaling at most 7 for a connected case, and adjacency within each component). A complete answer certifies the train-track representative, its transition matrix and Perron-Frobenius data, the complete periodic-Nielsen-path survey, the fixed-point/branch-point index computation, and the exact componentwise graph identification, or refutes a component of the claim with an explicit witness (reduction, periodic class, or Nielsen path). Rank is fixed at 4.

## Research outcome

Target blocked: primitivity and rotationless gate data were certified and bounded Nielsen/periodic-class searches were negative, but the unbounded no-PNP proof and complete atoroidal/index/IW certification could not be completed, so the lane exits cleanly with partial artifacts preserved.

## Why this attempt failed

Failed axes: no independent audit (NO_RESULT).

Only bounded certificates were completed: primitivity/stretch-factor certification, direction-map and gate computation for the rotationless power g = f^4, a periodic-class search to cyclic length 6 and period 3, and an INP-candidate search at leg length <= 3. Completeness requires the full Bestvina-Handel INP algorithm with a bounded-cancellation leg bound, a complete atoroidal certification, and the derived index and Whitehead-graph identification, none of which was established; the negative bounded-search results are plausibility evidence only.

## Conditions for a legitimate retry

introduce a materially new method or a justified, still-valuable revised claim; address the recorded limitation: Only bounded certificates were completed: primitivity/stretch-factor certification, direction-map and gate computation for the rotationless power g = f^4, a periodic-class search to cyclic length 6 and period 3, and an INP-candidate search at leg length <= 3. Completeness requires the full Bestvina-Handel INP algorithm with a bounded-cancellation leg bound, a complete atoroidal certification, and the derived index and Whitehead-graph identification, none of which was established; the negative b…

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
