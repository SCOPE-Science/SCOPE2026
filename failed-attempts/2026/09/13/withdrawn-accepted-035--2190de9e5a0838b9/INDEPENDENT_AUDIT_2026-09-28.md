# Independent Audit — 2026/09/13/035

**Audit date:** 2026-09-28 (UTC)  
**Audited tree:** `91e8f5bce1de3d23f1a8b9a43cf2732425bf4e46`  
**Disposition:** **FAILED**

## Correctness

**Verdict:** PASS  
The lower-bound argument checks. For C contained in E1=[0,1/3]∪[2/3,1], Green-function domain monotonicity gives g_C≥g_E1 off E1. With R(z)=9z^2−9z+1, E1=R^{-1}([-1,1]) and the degree-2 polynomial-preimage formula gives g_E1=(1/2)g_[-1,1]∘R. On [2/5,3/5] symmetry and monotonicity put the minimum at the endpoints. R(2/5)=−29/25 and R(2/5)^2−1=216/625, yielding (1/2)log((29+6√6)/25)≈0.2792011083. The supplied rational Taylor/square-root chain correctly proves this exceeds 0.27. Thus the proposed interval [0.17,0.27] is rigorously excluded; no exact value of the true Cantor-set minimum is claimed.

## Originality

**Verdict:** FAIL  
The certified number is an unprinted parameter evaluation of standard potential-theory machinery rather than a new theorem. Once one takes the first-stage outer approximation E1, textbook domain monotonicity and the standard polynomial-preimage Green-function formula mechanically reduce the claim to evaluating R(2/5) and an elementary exponential inequality. Current Cantor-capacity literature does not print this exact threshold, but absence of the decimal in a table does not make a direct specialization of established formulas research-level original.

## Scientific value

**Verdict:** PASS  
As a certified benchmark and as a rigorous falsification of the supplied numerical enclosure, the bound has concrete diagnostic value for computations of the Cantor Green function. Its value is narrow—it is only a lower bound and is not sharp—but the exact certificate is reusable even though the package does not clear the originality axis as a standalone research finding.

## Evidence

- [Ransford–Rostand, Computation of capacity](https://doi.org/10.1090/S0025-5718-07-01941-2): Provides numerical/global capacity context for the middle-third Cantor set, not the submitted interval-specific lower bound.
- [Liesen–Sete–Nasser, Computing the logarithmic capacity of compact sets having (infinitely) many components](https://arxiv.org/abs/2201.10228): Modern Cantor-capacity computations; no pointwise [0.4,0.6] threshold, while the submitted derivation uses standard Green-function monotonicity and polynomial-preimage formulas.

## Independent checks

- Recomputed R(2/5), the square-root term, and the half-log value 0.2792011083…; the exact rational threshold chain is valid.
- Checked the complex polynomial preimage and Green-function monotonicity direction.
- Current main directory tree SHA exactly equals the assigned tree SHA; no GitHub writes were made.

## Limitations

- The bound is only a lower bound and is not claimed sharp or equal to the true minimum.
- Failure is on originality as a research contribution, not on the certified inequality itself.

## Repository action

This audit is a guarded change-set only. Source tree `91e8f5bce1de3d23f1a8b9a43cf2732425bf4e46` still matches current `main`; no GitHub write was performed by this audit.
