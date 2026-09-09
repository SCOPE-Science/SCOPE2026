# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Interval-certified minima of L(1,chi) and central nonvanishing for primitive characters of conductor q<=32
- **Round:** 2026-09-07-first-light-01
- **Lane:** 299
- **Disposition:** AUDIT_2_REPAIR_EXHAUSTED
- **Domain:** Analytic Number Theory
- **Method:** approximate functional equation / truncated character-sum evaluation with interval enclosure and orthogonality cross-check

## Problem

Produce an interval-certified census of L(1,chi) for every primitive Dirichlet character chi of conductor q<=32 and certify the extremal minimum: each L(1,chi) enclosed in a rigorous interval of width <=1e-6 excluding 0, the minimum-modulus pair identified with disjointness proof, plus certified nonzero enclosures of L(1/2,chi) for the even characters in the same window, all recomputed from character sums with explicit tail bounds and replayable interval arithmetic.

## Attempted claim

For all primitive Dirichlet characters chi of conductor q<=32: rigorous intervals I_chi of width <=1e-6 containing L(1,chi) with 0 not in any I_chi; min_chi |L(1,chi)| is attained at an explicitly named character pair (chi*, conjugate) with I_chi* disjoint from all others below its upper endpoint; and for every even primitive chi in the window, a rigorous interval for L(1/2,chi) excluding 0.

## Research outcome

Full q<=32 target achieved: 204 rigorous L(1) enclosures (width<=1e-6, nonzero), named q=19 extremal conjugate pair with disjointness gap ~0.0145, and 99 certified nonzero even central values; verifier replays VERIFY_OK.

## Why this attempt failed

Failed axes: correctness.

correctness: Replayed inputs/artifacts/verify.py at --half-nblocks=300: VERIFY_OK. Independently verified: 204 total primitive chi (99 even, 105 odd); completeness sum_{d|q}Nprim+1=phi(q) for all q<=32; conductor==q for all 204 (proper divisor test, 0 fails); L(1) box max width ~8e-79 (<=1e-6); min |L|^2 ordering q19 i=4/12 (0.17072881600020...) < runner-up q5 i=1 (0.18525185646175...) with gap ~0.0145; L(1) formulas spot-checked against direct Dirichlet series (even matches to 1e-10, odd to truncation O(q/N)); |L|^2 lower-bound corner logic correct conditional on box not containing origin. Central even nonvanishing passes numerically (min lo/t~5.44, margin/t~4.44 at B=1500; doubled-U check passes). BUT essential inference fails: DRAFT/verify.py claim Emax=max_b|C_b| <= floor(phi(q)/2) with justification 'at most phi(q)/2 nonzero summands of modulus 1'. That justification is false: e.g. q=5, b=3 has 3 coprime residues 1,2,3 (3 nonzero summands > phi/2=2). The verifier assumes Emax=phi//2 without any rigorous per-character certificate of max|C_b|. Hence the as-presented tail majorant U=Emax/sqrt(N+1) lacks a valid proof. The conclusion is salvageable: the trivial bound Emax=phi(q) (|C_b| <= count of coprime a<=b <= phi) is rigorously valid and still yields lo-U_phi>0 for all 99 even chi at B=1500 with min margin 0.162 (checked). Telescoping sum_r(f(N+rq+1)-f(N+rq+q))<=f(N+1) via disjoint integral spans is correct; M=0 for primitive conductor>=3 is classical and numerically re-asserted. L(1) census and minimum disjointness are sound conditional on mpmath iv outward rounding (stated limitation, margins enormous). Because one load-bearing constant has a false proof, correctness FAILs pending a bounded fix.

## Conditions for a legitimate retry

repair the decisive proof or computational defect and recheck the full claim; introduce a materially new method or a justified, still-valuable revised claim; address the recorded limitation: Containment inherits mpmath iv outward-rounding correctness (margins enormous: gaps 1e-2 vs widths 1e-79). Real-char iv imag micro-boxes straddle 0 at 1e-30 (symmetry noise; documented, bounds unaffected). Min pair = conjugate pair with identical |.|^2; disjointness vs all outside pair. Odd central values not claimed (old tail majorant withdrawn after q=3 odd counterexample: true tail ~1.09e-2 > old T ~1.11e-4 at B=300; central proof restricted to even chi with M=0 lemma). Formulas classical; n…

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
