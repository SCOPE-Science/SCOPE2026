# Scientific review

**Correctness: PASS.** The one-step cross approximation can only have normalized spectral error \(1\) or \(\kappa\), depending on selected column. The first row-pivot of \((SA_\kappa)^\mathsf T\) uses two entries from only the first Gaussian row. Their ratio gives the exact Cauchy tail; CPQR uses two independent chi-square lengths and hence a beta CDF. Endpoint asymptotics of beta density establish the sharp moment transitions. `verify.py` checks independent even-sketch CDF polynomial identities and representative values.

**Originality: PASS, with priority risks.** Current full-text algorithms in *IterativeCUR* and *Adaptive LSQR Preconditioning from One Small Sketch* identify the sketch-transpose LUPP rule and norm-based alternatives but do not establish the exact normalized CUR moment cutoffs. Related published search results on multistage ARP and complete-pivot ACA describe different pivoting operations. A classical Cauchy/Beta comparison is not new on its own; the mathematical contribution is the exact induced approximation-loss phase diagram for this explicit rule. Priorities in unindexed literature are not resolved by unsuccessful searches.

**Value: PASS.** The finding locates a real gap between selection consistency in probability and bounded moment-optimality for a natural rank-one numerical approximation, with an exact dependence on sketch height and a concrete alternative pivot. It is not a result about the full multi-step adaptive least-squares solver or the source papers' default sparse-sign sketches.

Closest literature: Pritchard et al., arXiv:2509.21963 (first released 2025-09-26), and Huh et al., arXiv:2604.05065 (first released 2026-04-06), especially their appendix algorithm for transpose-of-sketch LUPP. Related but different schemes include multistage adaptive randomized pivoting and complete-pivot ACA. The exact two-dimensional Gaussian comparison might have been derived elsewhere without indexing; no independent scholarly audit has been performed.

Self-review: passed. Independent audit: not yet performed.
