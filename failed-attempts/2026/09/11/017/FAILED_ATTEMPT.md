# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Spectral-gap resurgence bound for cover ideals of an LPS Ramanujan expander family
- **Round:** 2026-09-07-first-light-01
- **Lane:** 717
- **Disposition:** NO_RESULT
- **Domain:** Commutative Algebra
- **Method:** spectral-expansion transfer with symbolic-power containment and Waldschmidt-constant estimation

## Problem

Transfer spectral expansion into symbolic-power theory for cover ideals: establish a uniform resurgence bound over a named infinite LPS Ramanujan expander family truncated to 120-520 vertices via a spectral-gap Waldschmidt lower bound plus a Harbourne-Huneke containment lemma, with one fully certified witness ideal.

## Attempted claim

Let {G_q} be the named LPS Ramanujan family (fixed prime p, varying quotient q) restricted to graphs with 120 <= |V(G_q)| <= 520, and let J(G_q) be the squarefree cover ideal in k[V(G_q)]. Then rho(J(G_q)) <= 1.35 for every graph in this window, proved via a spectral-gap lower bound hat-alpha(J(G_q)) >= f(lambda2) plus a cited Harbourne-Huneke-type containment lemma, with the 120-vertex member fully worked as extremal witness.

## Research outcome

Target rho<=1.35 blocked by inequality-direction obstruction (spectral data bounds the wrong side; numeric certifiable interval [~1.18,~1.67] cannot imply <=1.35). Revealed fallback attempted with bounded exact effort and blocked: the named 120-vertex LPS quotient X^{5,q0} does not exist (|PSL(2,q)|=120 has no integer solution; |PGL(2,q)|=120 only at degenerate excluded q==p==5 where LPS generators are singular), so its exact certificate is unsatisfiable. Replay: python3 output/artifacts/verify_fallback_block.py -> VERIFY_OK. CLEAN_EXIT; no emergent finding.

## Why this attempt failed

Failed axes: no independent audit (NO_RESULT).

['No CAS (Macaulay2/Singular/gap) available in environment; symbolic-power inclusion step unreachable, though already moot given G0 nonexistence.', 'Numeric target recovery used a configuration-model 6-regular 120v proxy, not an LPS quotient; sufficient to demonstrate the inequality-direction gap but not a certificate about any LPS graph.', 'Originality/value literature checks rely on the admission fused retrieval, not a fresh independent search.']

## Conditions for a legitimate retry

introduce a materially new method or a justified, still-valuable revised claim; address the recorded limitation: ['No CAS (Macaulay2/Singular/gap) available in environment; symbolic-power inclusion step unreachable, though already moot given G0 nonexistence.', 'Numeric target recovery used a configuration-model 6-regular 120v proxy, not an LPS quotient; sufficient to demonstrate the inequality-direction gap but not a certificate about any LPS graph.', 'Originality/value literature checks rely on the admission fused retrieval, not a fresh independent search.']

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
