# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Bounded-systole polylog multiplicity bound via Selberg trace and representation counting
- **Round:** 2026-09-14-hands-on-first-light-01
- **Lane:** 20389
- **Disposition:** NO_RESULT
- **Domain:** Spectral Geometry
- **Method:** Selberg trace formula and representation-counting analysis

## Problem

Fix s_0>0. Do there exist an absolute constant c>0 and a constant C=C(s_0)>0 such that every closed oriented hyperbolic surface X of genus g>=2 with systole sys(X)>=s_0 satisfies m_1(X) <= C(s_0) g/(log(2+g))^c, where m_1(X) is the multiplicity of the first non-zero Laplacian eigenvalue lambda_1(X), decidable by the Selberg trace formula with test-function support of order A log g combined with a uniform length-spectrum (conjugacy-class) counting estimate under sys>=s_0 and, when Isom(X) is non-trivial, twisted-trace irreducible-representation exclusion?

## Attempted claim

Fix s_0>0. Do there exist an absolute constant c>0 and a constant C=C(s_0)>0 such that every closed oriented hyperbolic surface X of genus g>=2 with systole sys(X)>=s_0 satisfies m_1(X) <= C(s_0) g/(log(2+g))^c, where m_1(X) is the multiplicity of the first non-zero Laplacian eigenvalue lambda_1(X), decidable by the Selberg trace formula with test-function support of order A log g combined with a uniform length-spectrum (conjugacy-class) counting estimate under sys>=s_0 and, when Isom(X) is non-trivial, twisted-trace irreducible-representation exclusion?

## Research outcome

Target blocked: bounded-systole polylog multiplicity bound m_1(X)<=C(s_0)g/(log g)^c cannot be completed because the required additive length-spectrum counting bound is unavailable and multiplicative counting provably dominates the trace identity term. Clean exit with matching target_exit.json.

## Why this attempt failed

Failed axes: no independent audit (NO_RESULT).

The Selberg trace route with R=A log g support, the small-versus-tempered regime split, and the twisted-trace quotient argument all block on the same missing additive counting lemma N(X,L)<=C(s_0)(g+e^L) under only sys>=s_0. Only multiplicative Buser-type counting is locally available, which provably cannot yield the claimed saving. No emergent finding of independent audit value was produced; the scaling comparison in output/artifacts/trace_scaling.py is routine arithmetic on known bounds.

## Conditions for a legitimate retry

introduce a materially new method or a justified, still-valuable revised claim; address the recorded limitation: The Selberg trace route with R=A log g support, the small-versus-tempered regime split, and the twisted-trace quotient argument all block on the same missing additive counting lemma N(X,L)<=C(s_0)(g+e^L) under only sys>=s_0. Only multiplicative Buser-type counting is locally available, which provably cannot yield the claimed saving. No emergent finding of independent audit value was produced; the scaling comparison in output/artifacts/trace_scaling.py is routine arithmetic on known bounds.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
