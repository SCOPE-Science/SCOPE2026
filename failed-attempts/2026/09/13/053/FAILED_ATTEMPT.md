# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Vanishing wired-free gap for critical FK-Ising 2:1 crossings
- **Round:** 2026-09-07-first-light-01
- **Lane:** 1578
- **Disposition:** NO_RESULT
- **Domain:** statistical mechanics / FK percolation
- **Method:** exact small-m enumeration plus FKG/duality coupling and RSW mixing

## Problem

Consider the critical FK-Ising model (random-cluster q=2, p_c=sqrt(2)/(1+sqrt(2))) on Z^2. For integer m>=1 let Rect(m)=[0,2m]x[0,m] and let p(m,free) and p(m,wired) be the probabilities of an FK-open horizontal crossing of Rect(m) under free and wired boundary conditions. Prove or disprove that lim_{m->infinity} (p(m,wired)-p(m,free))=0. A complete answer either proves the gap vanishes asymptotically, or exhibits an epsilon0>0 and an explicit subsequence m_k->infinity with p(m_k,wired)-p(m_k,free)>=epsilon0 via a rigorous lower witness.

## Attempted claim

Consider the critical FK-Ising model (random-cluster q=2, p_c=sqrt(2)/(1+sqrt(2))) on Z^2. For integer m>=1 let Rect(m)=[0,2m]x[0,m] and let p(m,free) and p(m,wired) be the probabilities of an FK-open horizontal crossing of Rect(m) under free and wired boundary conditions. Prove or disprove that lim_{m->infinity} (p(m,wired)-p(m,free))=0. A complete answer either proves the gap vanishes asymptotically, or exhibits an epsilon0>0 and an explicit subsequence m_k->infinity with p(m_k,wired)-p(m_k,free)>=epsilon0 via a rigorous lower witness.

## Research outcome

Target blocked: numerics indicate a persistent wired-free gap (~0.39 over m=8..48) but no rigorous proof or lower witness was obtainable in-lane; decision-phase alternatives also blocked, so clean exit with NO_RESULT.

## Why this attempt failed

Failed axes: no independent audit (NO_RESULT).

No proof in either direction was obtained: Route A (gap vanishes) is numerically refuted but not disproved, and Route B (rigorous disproof witness) lacks the uniform epsilon_0 lower bound. The Monte Carlo survey (m<=48) is finite-scale evidence only and does not rule out ultra-slow decay beyond m=48. The exact m=1 anchor is single-scale and carries no asymptotic content. No literature search was consumed. All scripts are preserved (scratch/sw.c, scratch/swtest.py, scratch/swbig.py, scratch/exact_m1.py, scratch/witness_analysis.py) for reproducibility.

## Conditions for a legitimate retry

introduce a materially new method or a justified, still-valuable revised claim; address the recorded limitation: No proof in either direction was obtained: Route A (gap vanishes) is numerically refuted but not disproved, and Route B (rigorous disproof witness) lacks the uniform epsilon_0 lower bound. The Monte Carlo survey (m<=48) is finite-scale evidence only and does not rule out ultra-slow decay beyond m=48. The exact m=1 anchor is single-scale and carries no asymptotic content. No literature search was consumed. All scripts are preserved (scratch/sw.c, scratch/swtest.py, scratch/swbig.py, scratch/exac…

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
