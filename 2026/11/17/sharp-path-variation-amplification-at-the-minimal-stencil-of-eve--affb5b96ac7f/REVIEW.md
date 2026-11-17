# Mathematical review

## Correctness — PASS
Exact rational first-difference reduction gives an induced l1 column norm; all diagonal signs are controlled since alpha u_j v_j<1. The sharp step input saturates each column, the M=0 threshold follows at p=2, and Stirling yields M_p/binom(2p,p)->sqrt2. An independent Fraction-based direct matrix inversion checked p=1..12 for three positive rational lambda values. Limits in p are analytic, not inferred from finite numerics.

## Originality — PASS (qualified)
Comparisons included general HP/Whittaker finite-sample representations, the published all-order range-preservation result and accessible previous first-/second-order total-variation findings. No inspected work states the exact all-order minimal-stencil BV norm, its sharp binary-step extremizers and fixed-lambda high-order limit. Underlying rank-one smoothing matrices are not novel and may create a priority risk; originality here refers only to the derived induced-variation invariant and asymptotic classification.

## Mathematical value — PASS
The exact sharp variation amplification quantifies worst-case creation of adjacent variation by a standard penalized smoothing method. It identifies three distinct low-order regimes, proves that monotone one-step data can be worst cases, and shows a universal high-order amplification of 1+sqrt2 despite arbitrarily small fixed positive penalty. A natural complete classification of the minimal admissible observation length with a nontrivial binomial asymptotic is useful in stability and trend-filter interpretation.

## Scientific limitations
- Published matrix formulas for the minimal stencil allow derivation of the matrix norm, so an unindexed source may already perform the same BV calculation.
- The complete full text of Eilers (2003) was not accessible; its accessible abstract and citation metadata do not establish absence of this norm classification.
- The theorem covers exactly n=p+1 and makes no all-n high-order contraction claim.

Self-review: passed. Independent audit: not yet performed.
