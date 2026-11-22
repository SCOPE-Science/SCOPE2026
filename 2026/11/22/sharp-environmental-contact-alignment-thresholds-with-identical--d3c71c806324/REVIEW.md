# Scientific review

## Correctness — PASS

The matrix is primitive for the stated positive rates, and the positive-eigenvector reduction proves the unique Perron root of the cubic equation. The derivative with respect to the aligned-contact dot product is strictly positive, and adjacent swaps yield global sorting optimality for every positive population size. The \(R=1\) comparison and rational two-group witness are exact. Independent direct-matrix checks and permutation enumeration (`check.py`, 5,090 checks) agree with the formula; the theorem does not depend on finite verification.

## Originality — PASS (literature-bounded)

The closest source, Caiza–Qin–Paré (arXiv:2610.09066), bounds the spectral epidemic factor by local reproduction scores and reduces it to two layers under uniform interlayer row sums. Its reduction does not imply the heterogeneous exposure–shedding assignment extremizers. Qu–Wang (arXiv:1608.07327) address degree-correlated rates and a special wheel epidemic. Li–Wang–Van Mieghem (arXiv:1303.0783) supply the general directed spectral threshold viewpoint. Tuschhoff–Kennedy (DOI:10.1016/j.jtbi.2025.112186) study infection-risk correlations in a stochastic SIR model; their full text was not accessible in this review. The positive-correlation intuition is known; the claimed contribution is narrowly the exact all-permutation reservoir factor, its necessary-and-sufficient classification, and the smallest reversal under invariant individual local scores.

## Value — PASS

The structural question is motivated by the limitations of local reproduction metrics in a two-channel epidemic. The theorem solves the entire assignment problem for any fixed positive intensity lists, identifies the exact direct-versus-mediated environmental feedback budget, and produces an exact two-group case where identical per-node local scores yield opposite global invasion decisions. This is a natural complete comparison, not a numerical parameter sweep. It is only an invasion-scale result, not a validated intervention or empirical epidemic prediction.

## Residual risks

Full historical priority for correlation effects cannot be established from incomplete access to the stochastic-SIR comparison; broader general Perron–rearrangement results may encode the algebraic argument. The intended contribution is only the application-specific exact characterization. No independent mathematical audit has been performed.

Self-review: passed. Independent audit: not yet performed.
