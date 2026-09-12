# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Factor-ten gain from doubling denominator degree
- **Round:** 2026-09-07-first-light-01
- **Lane:** 1157
- **Disposition:** NO_RESULT
- **Domain:** approximation theory
- **Method:** best-error comparison via explicit approximants and lower bounds

## Problem

Prove or disprove that doubling only the denominator degree gives at least a factor-ten improvement for f(x)=|x| on [-1,1] from degree 5 onward: with E(m,n) as the best uniform error over real R(m,n) on [-1,1], decide whether E(n,2n)<=0.1*E(n,n) for every integer n>=5. Scope is all n>=5, comparing diagonal type (n,n) against unbalanced type (n,2n) for the same f and interval. A complete answer either constructs, for each n>=5, an explicit s_n in R(n,2n) with rigorous sup error <=0.1 times a rigorous lower bound for E(n,n), or disproves the factor-ten claim by exhibiting one n>=5 with a rigorous lower bound E(n,2n)>0.1 times a rigorous upper bound for E(n,n).

## Attempted claim

Prove or disprove that doubling only the denominator degree gives at least a factor-ten improvement for f(x)=|x| on [-1,1] from degree 5 onward: with E(m,n) as the best uniform error over real R(m,n) on [-1,1], decide whether E(n,2n)<=0.1*E(n,n) for every integer n>=5. Scope is all n>=5, comparing diagonal type (n,n) against unbalanced type (n,2n) for the same f and interval. A complete answer either constructs, for each n>=5, an explicit s_n in R(n,2n) with rigorous sup error <=0.1 times a rigorous lower bound for E(n,n), or disproves the factor-ten claim by exhibiting one n>=5 with a rigorous lower bound E(n,2n)>0.1 times a rigorous upper bound for E(n,n).

## Research outcome

Target blocked: no rigorous proof or disproof of the factor-ten claim was established; the only viable disproof route (rational lower bound) proved methodologically unavailable, so CLEAN_EXIT with NO_RESULT.

## Why this attempt failed

Failed axes: no independent audit (NO_RESULT).

Heuristic SK/Lawson upper bounds (~8.55e-3 and ~2.83e-3) are non-rigorous floats without verified certificates; no lower bound on E(n,2n) was established; asymptotic comparisons are intuition only. The target claim for all n>=5 remains fully open.

## Conditions for a legitimate retry

introduce a materially new method or a justified, still-valuable revised claim; address the recorded limitation: Heuristic SK/Lawson upper bounds (~8.55e-3 and ~2.83e-3) are non-rigorous floats without verified certificates; no lower bound on E(n,2n) was established; asymptotic comparisons are intuition only. The target claim for all n>=5 remains fully open.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
