# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** One-sided sqrt finite threshold E66 vs 0.001
- **Round:** 2026-09-07-first-light-01
- **Lane:** 1847
- **Disposition:** NO_RESULT
- **Domain:** approximation theory
- **Method:** endpoint-clustered poles plus dense-grid certificate or de la Vallee Poussin alternation

## Problem

Let f3(x)=0 for -1<=x<=0 and f3(x)=sqrt(x) for 0<x<=1 with f3(0)=0, continuous on [-1,1] with a one-sided square-root branch point at 0, and let E_{6,6}(f3) be the minimum of max_{x in [-1,1]}|f3(x)-r(x)| over real rational functions r=p/q with deg p<=6, deg q<=6 and q nonzero on [-1,1]. Prove or disprove that E_{6,6}(f3) <= 0.001. A complete resolution either exhibits an explicit real type-(6,6) rational with certified uniform error at most 0.001 on [-1,1] via poles clustered at 0 plus a verifiable dense-grid error certificate, or proves rigorously via a Chebyshev alternation (de la Vallee Poussin) certificate that every such rational has uniform error above 0.001.

## Attempted claim

Let f3(x)=0 for -1<=x<=0 and f3(x)=sqrt(x) for 0<x<=1 with f3(0)=0, continuous on [-1,1] with a one-sided square-root branch point at 0, and let E_{6,6}(f3) be the minimum of max_{x in [-1,1]}|f3(x)-r(x)| over real rational functions r=p/q with deg p<=6, deg q<=6 and q nonzero on [-1,1]. Prove or disprove that E_{6,6}(f3) <= 0.001. A complete resolution either exhibits an explicit real type-(6,6) rational with certified uniform error at most 0.001 on [-1,1] via poles clustered at 0 plus a verifiable dense-grid error certificate, or proves rigorously via a Chebyshev alternation (de la Vallee Poussin) certificate that every such rational has uniform error above 0.001.

## Research outcome

Target blocked: best type-(6,6) grid error 0.0151 vs 0.001 threshold with no certifiable route; clean exit with no auditable finding.

## Why this attempt failed

Failed axes: no independent audit (NO_RESULT).

No certified upper or lower bound on E_{6,6}(f3) was established: the best computed type-(6,6) approximant reaches only grid error 0.0151 (uncertified, with a near-pole min|D|=3.4e-6 defeating rigorous certification) and no 14-point alternation certificate was found, so the threshold question at 0.001 remains fully open; all error figures are grid-based and non-rigorous.

## Conditions for a legitimate retry

introduce a materially new method or a justified, still-valuable revised claim; address the recorded limitation: No certified upper or lower bound on E_{6,6}(f3) was established: the best computed type-(6,6) approximant reaches only grid error 0.0151 (uncertified, with a near-pole min|D|=3.4e-6 defeating rigorous certification) and no 14-point alternation certificate was found, so the threshold question at 0.001 remains fully open; all error figures are grid-based and non-rigorous.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
