# Scientific review

## Correctness — PASS

The exact joint probability-generating function follows from three exclusive single-particle statuses and the Poisson marking formula. A Palm argument selects precisely the first binding particle; differentiation gives the displayed conditional generating function and mean. The derivative identity \(\int_0^t\rho(u)\psi''(q(u))\,du=\mu-\psi'(q(t))\) proves fixed-positive-time finiteness even if the batch second moment diverges. Dominated/monotone convergence and a regularly varying Riemann sum give the size-biased limit and the complete three-regime theorem. The Brownian erfc asymptotic fixes the logarithmic and essential factors. Independent finite-state checks in `CHECK.py` passed 54 comparisons; `TAIL_CHECK.py` passed six finite power-tail comparisons. The analytical arguments, not these finite checks, establish the theorem.

## Originality — PASS, qualified

Boyer and Mercado-Vásquez, arXiv:2611.04843v1, Sections 2, 4 and 6 and Appendix A, already establish the single-particle input, unconditional particle counts, first-binding marginal survival, mean first-passage times, and burst comparisons. Those are not claimed. The new joint live-count/first-binding transform retains information missing from the no-hit marginal, and the sharp second-moment-boundary law has different quantifiers and outcomes. Mercado-Vásquez and Boyer, arXiv:2602.11095, treat earlier unit-production first-passage theory. Accessible statement-level comparisons with relevant published work on mortal recruitment, renewal sources and batch-reset gases did not identify a covering statement. Some complete manuscripts remained inaccessible; an equivalent in general marked-Poisson Palm literature cannot be excluded and is a priority risk.

## Value — PASS

The live population at the first actual reaction, rather than its unconditional mean or the average reaction waiting time, is a natural size-biased observable in burst-produced transport. The theorem determines exactly when this conditional mean remains bounded and identifies both a critical inverse-time law and an essential singularity, with leading constants and no source-intensity dependence. The results do not establish experimental observability, noisy inference, interactions or nonexponential mortality.

## References and integrity

The scientific source is D. Boyer and G. Mercado-Vásquez, *Stochastic synthesis and degradation of arbitrary diffusive processes*, arXiv:2611.04843v1 (3 November 2026). The preceding unit-production source is arXiv:2602.11095v1. The complete contents of the mathematical claim and proof are in `RESULT.md`; numerical checks are independent supporting evidence only.

Self-review: passed. Independent audit: not yet performed.
