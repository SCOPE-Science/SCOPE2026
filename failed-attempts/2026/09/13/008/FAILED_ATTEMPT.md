# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** PPV group of cubic oscillator Y''=(x^3+t)Y
- **Round:** 2026-09-07-first-light-01
- **Lane:** 1474
- **Disposition:** AUDIT_2_REPAIR_EXHAUSTED
- **Domain:** parameterized differential Galois theory
- **Method:** Arreche-Dreyfus reductive quotient plus creative telescoping

## Problem

Fix the explicitly parameterized second-order equation d^2Y/dx^2 = (x^3 + t)Y with parameter t in C, equivalently the traceless rank-2 system dY/dx = [[0,1],[x^3+t,0]]Y over the (d/dx, d/dt)-field C(t,x), with a single irregular singularity at infinity; no zero-curvature or isomonodromy is assumed. What is its parameterized Picard-Vessiot (PPV) Galois group: is it the full constant group SL(2) with no nontrivial d/dt-differential-algebraic relations among a fundamental solution matrix and its t-derivatives (so generic solutions are hypertranscendent in t in the Hardouin-Minchenko-Ovchinnikov sense), versus a proper Kolchin-closed differential algebraic subgroup defined by an explicit nontrivial d/dt-polynomial equation on the unipotent radical (so solutions satisfy a concrete t-differential relation)? A complete answer runs the bounded Arreche-Dreyfus computation for this q = x^3 + t (reductive quotient plus creative-telescoping step) and proves one alternative with the defining differential equations exhibited. Either outcome is independently valuable: the first certifies hypertranscendence of this Airy-type family in its parameter, the second exhibits a new exact parameter-differential relation.

## Attempted claim

Fix the explicitly parameterized second-order equation d^2Y/dx^2 = (x^3 + t)Y with parameter t in C, equivalently the traceless rank-2 system dY/dx = [[0,1],[x^3+t,0]]Y over the (d/dx, d/dt)-field C(t,x), with a single irregular singularity at infinity; no zero-curvature or isomonodromy is assumed. What is its parameterized Picard-Vessiot (PPV) Galois group: is it the full constant group SL(2) with no nontrivial d/dt-differential-algebraic relations among a fundamental solution matrix and its t-derivatives (so generic solutions are hypertranscendent in t in the Hardouin-Minchenko-Ovchinnikov sense), versus a proper Kolchin-closed differential algebraic subgroup defined by an explicit nontrivial d/dt-polynomial equation on the unipotent radical (so solutions satisfy a concrete t-differential relation)? A complete answer runs the bounded Arreche-Dreyfus computation for this q = x^3 + t (reductive quotient plus creative-telescoping step) and proves one alternative with the defining differential equations exhibited. Either outcome is independently valuable: the first certifies hypertranscendence of this Airy-type family in its parameter, the second exhibits a new exact parameter-differential relation.

## Research outcome

PPV group of Y''=(x^3+t)Y proved to be the full constant SL(2) with no t-differential relations; hypertranscendence certified via the bounded Arreche-Dreyfus computation.

## Why this attempt failed

Failed axes: correctness.

correctness: TARGET route audited normally: draft claims classical PV=SL2 and PPV=full constant SL2 for Y''=(x^3+t)Y via Kovacic cases 1-3 plus Dreyfus-Arreche L[b]=-2 unsolvability, with hypertranscendence corollary. Re-ran inputs/artifacts/verify_operators.py: ALL CHECKS PASSED (infinity pole order 7, Riccati residue (a^2-a)/(x-c)^2, 2d!=3, log-derivative sign +P/2, residue-2 valuation >=-1, deg Q=3+2N with Q'/Q!=0, L monomial degree nu+2 lc -(4nu+6)f and pole m->m+3). Case1 holds via infinity degree argument (2d even/bounded vs cubic degree 3) which rescues an imprecise cross-term sentence. Case3 irregular-infinity and Step2 telescoping pole-amplification/degree arguments verified and hold over any char-0 K0 including r(c)=0 zeros. Case2 conclusion true but proof as written has an essential gap: it asserts every finite pole of u/v in a quadratic F is simple of residue 1 by applying the (x-c)-uniformizer residue lemma in F, without ramified-place analysis. For e=2, valuations are v(u')=-m-2 vs v(u^2)=-2m forcing m=2 and s residue 2 in x, not covered. Since residue-2 is later excluded, the final residue-1 and Q'/Q contradiction still follow after a bounded patch, but the intermediate lemma is false as stated. Hence correctness FAILs as written though repairably. Artifact checks identities only, not the full place analysis; proof vs computation distinguished.

## Conditions for a legitimate retry

repair the decisive proof or computational defect and recheck the full claim; introduce a materially new method or a justified, still-valuable revised claim; address the recorded limitation: Base d/dx-constant field taken d/dt-differentially closed per standard PPV hypothesis, though computations use only C(tbar)(x). Result is generic in t; no claim about individual specializations t=t0 beyond the same Kovacic computation applied with constant t0. Kovacic four-case theorem, Dreyfus/Arreche reduction, Sit-Cassidy SL2 classification, and the PPV Galois correspondence are used as cited oracles. Analytic incarnations (Stokes data, actual fundamental matrices) are not addressed.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
