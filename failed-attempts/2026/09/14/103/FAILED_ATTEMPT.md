# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Uniform effectivity on a resonant ray of the simplest-cubic Thue family
- **Round:** 2026-09-14-hands-on-first-light-01
- **Lane:** 20099
- **Disposition:** NO_RESULT
- **Domain:** Diophantine Geometry
- **Method:** Baker logarithmic-form and lattice-reduction techniques

## Problem

Let f_n(X)=X^3-(n-1)X^2-(n+2)X-1 have roots λ_0,λ_1,λ_2, let K_n=Q(λ_0), and define G_{n,s}(X,Y)=∏_{i=0}^2(X-λ_i^sλ_{i+1}^{2s}Y) (indices modulo 3). Does there exist an effectively computable absolute constant C such that every integer solution |G_{n,s}(x,y)|=1 with n≥3, s∈Z\{0}, and |y|≥2 satisfies max{log n,|s|,log|x|,log|y|}≤C?

## Attempted claim

Let f_n(X)=X^3-(n-1)X^2-(n+2)X-1 have roots λ_0,λ_1,λ_2, let K_n=Q(λ_0), and define G_{n,s}(X,Y)=∏_{i=0}^2(X-λ_i^sλ_{i+1}^{2s}Y) (indices modulo 3). Does there exist an effectively computable absolute constant C such that every integer solution |G_{n,s}(x,y)|=1 with n≥3, s∈Z\{0}, and |y|≥2 satisfies max{log n,|s|,log|x|,log|y|}≤C?

## Research outcome

Target (uniform absolute effective bound over n>=3, s!=0, |y|>=2 for |G_{n,s}|=1) is BLOCKED: four concrete routes, namely the exact s=1 parametric-Thue slice, the S-unit Baker bound over (n,s), the fixed-y elliptic reduction, and the explicit unbounded-family search, each hit a parameter-dependence obstruction documented in output/target_exit.json, and the bounded recovery computation (output/artifacts/recovery_test.py) found only sporadic solutions with height and gap growth confirming the block. No independently valuable emergent finding resulted, so the lane exits clean with NO_RESULT.

## Why this attempt failed

Failed axes: no independent audit (NO_RESULT).

No uniform bound was proved and no counterexample family was constructed; the census covers only 3<=n<=30, |s|<=3, 2<=|y|<=2000 and cannot exclude large solutions; the assessed parameter dependence of Baker and Siegel constants is a methodological finding, not a proved impossibility theorem; all symbolic identities were machine-checked but rely on standard computer algebra for the number-field arithmetic.

## Conditions for a legitimate retry

introduce a materially new method or a justified, still-valuable revised claim; address the recorded limitation: No uniform bound was proved and no counterexample family was constructed; the census covers only 3<=n<=30, |s|<=3, 2<=|y|<=2000 and cannot exclude large solutions; the assessed parameter dependence of Baker and Siegel constants is a methodological finding, not a proved impossibility theorem; all symbolic identities were machine-checked but rely on standard computer algebra for the number-field arithmetic.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
