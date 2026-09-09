# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Minimal word-growth rate with certified gap for committed infinite rank-3/4 Coxeter groups via Steinberg series
- **Round:** 2026-09-07-first-light-01
- **Lane:** 278
- **Disposition:** AUDIT_1_REJECT
- **Domain:** Geometric Group Theory
- **Method:** Steinberg rational growth-series computation with smallest-pole enclosure and BFS word-count cross-check

## Problem

Fix 6-8 explicit connected infinite (non-spherical, non-affine) Coxeter matrices of rank 3 (hyperbolic triangle types with large labels and at least one infinity label) and rank 4 (compact-hyperbolic simplex-like and infinity-label types outside the minimal-hyperbolic dataset). For each committed matrix compute the exact Steinberg rational word-growth series, certify its exponential growth rate omega (reciprocal of the smallest-modulus pole) inside a rigorous enclosure, cross-check series coefficients against BFS Cayley word counts to length >=12, and determine the minimal-growth system with an explicit certified gap to the next-smallest rate.

## Attempted claim

Over the committed infinite rank-3/4 window, exact Steinberg rational growth series yield certified growth-rate intervals whose minimum is attained at a single explicit system (minimal-growth witness) separated by a positive certified gap delta>0 from every other system in the window, with all series coefficients agreeing with BFS word counts to length >=12.

## Research outcome

Certified minimal-growth witness (triangle [3,3,4], omega in [1.40126836,1.40127916]) with gap 0.064292 over a committed 7-system infinite rank-3/4 Coxeter window via exact Steinberg rationals, Sturm pole brackets, argument-principle radius certificates, and BFS agreement to length 12; independent verifier prints VERIFY_OK.

## Why this attempt failed

Failed axes: correctness, originality, value.

correctness: Steinberg denominators/numerators for all 7 systems re-derived independently and match: triangle A-E match both direct Steinberg enumeration with longest-element shifts and Terragni infinite-family closed forms (A: [1,3,5,6,5,3,1]/[1,0,-1,-1,-1,0,1]; B: [1,2,3,3,3,2,1]/[1,-1,0,-1,0,-1,1]; C: [1,3,5,6,5,3,1]/[1,0,-1,-2,-1,0,1]; D: [1,2,2,1]/[1,-1,-1]; E: [1,2,2,2,1]/[1,-1,0,-1]). verify.py rebuild prints VERIFY_OK; bfs_check.py re-run matches all series coefficients to length 12 for all 7 systems. Sturm smallest-positive-root lower bounds (omega_lo=1/b) are exact rational and rechecked. Numpy root check confirms smallest-modulus root is real, well separated from second root (modulus gaps 0.28-1.0), so omega_lo side is sound. HOWEVER the headline ordering/gap requires upper bounds omega_hi=1/rho from the argument-principle winding count, which is not a proof: certify_radii.py/verify.py evaluate Q(rho e^{it}) at float midpoints with second-order remainder r=M2*(dth/2)^2/2 plus heuristic float padding 1e-9*sum+1e-12 and float atan/asin/hypot with 1e-9 padding, not rigorous interval arithmetic or certified rounding-error bounds. A sound first-order Lipschitz bound L*(dth/2) is 361x-1204x larger than the claimed radius (e.g. A at Narcs=4096: claimed 4.18e-06 vs sound 3.02e-03; E: claimed 1.04e-06 vs sound 1.25e-03; G: claimed 1.88e-06 vs sound 1.59e-03), and dense sampling shows min|Q| on the circle (~1.81e-05 for A, ~1.73e-06 for E, ~3.12e-06 for G) is below the sound radius, so the tight width<=1.1e-05 and the certified A_hi/E_lo separation depend on the unsound remainder. Thus omega_hi, interval widths, and the 0.064292 gap are experimental evidence with heuristic error accounting, not machine-checked proof as claimed ('certified', 'rigorous', 'disjoint enclosures'). Essential headline inference (A_hi < E_lo and all other gaps) is therefore not proved. originality: Substantive overlap defeats novelty. System A (triangle [3,3,4]) is verbatim in Terragni arXiv:1503.08764 sec 2.1.3 as a <=-minimal hyperbolic system with identical numerator 1+3t+5t^2+6t^3+5t^4+3t^5+t^6, denominator 1-t^2-t^3-t^4+t^6, initial coefficients (1,3,6,10,15,22,31), and growth rate 1.40126836793985... within the claimed [1.40126836,1.40127916]. The per-system table is therefore not wholly new. Further, the same paper p.2 displays closed parametric formulas p_<a,b,c>, p_<a,b,inf>, p_<a,inf,inf>, p_<inf,inf,inf>; B=[3,3,5], C=[3,4,4], D=[3,3,inf], E=[2,4,inf] series were verified to equal direct substitution into those formulas exactly, i.e. mechanically implied parameter instances, not new Steinberg computations. D's rate is the golden ratio phi=(1+sqrt5)/2 from Q=1-t-t^2, classical. Only rank-4 F/G (non-minimal-hyperbolic / non-hyperbolic with inf) lie outside the minimal-hyperbolic dataset scope by definition, but the headline minimum (A<E<B<C<D<G<F) does not depend on them beyond being larger, and the comparative window-minimum over this ad hoc 7-set is not a re…

## Conditions for a legitimate retry

repair the decisive proof or computational defect and recheck the full claim; state a substantive result not covered by the identified prior work; supply independent motivation and a materially stronger contribution; address the recorded limitation: Window-relative minimum (7 committed systems), not global; novelty vs Terragni dataset / Bredon-Kellerhals minima per admission triage, no fresh literature search; winding bounds use float midpoints with rigorous remainder radii and slack accounting, replayable via verify.py; BFS to length 12, series exact to a14.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
