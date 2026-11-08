# Scientific review

## Correctness — PASS

The critical first-cycle hitting probabilities follow from the unique decaying solution of the killed two-component Brownian backward boundary-value problem with reflecting and absorbing conditions. The surviving-cycle kernel subtracts a gate resolvent started at the absorbing open state; this uses gate persistence, the strong Markov property, and exponential memorylessness, not an assumed ordinary renewal between successive gate states. The explicit characteristic identity \(\det(sI-K)=-pquv/(AB^2)<0\) forces a strict interlacing with the two positive eigenvalues, and hence two strictly positive mixture weights. Matrix-power probabilities, strict discrete log-convexity, and the law of total variance finish the result for every admissible parameter and count. The separate symbolic factorization and 10,914 numerical diagnostics support the algebra; neither numerical check is substituted for proof.

## Originality — PASS, qualified

Mercado-Vásquez and Boyer (arXiv:2107.02148, Sections 2–5 and Appendices A–B) analyze this same physical gate-persistent search system but calculate time-to-absorption laws, means, and coefficients of variation, not the reset-count distribution or the positive two-geometric decomposition. Their Appendix B expressly distinguishes Bressloff's 2020 gate-reinitializing model, which does have ordinary renewal. Bressloff (arXiv:2310.20502, Section V) treats reset-count truncation for ungated diffusion and cannot supply the gate-dependent two-component law. Biswas et al. (arXiv:2304.10605, primary equations and analysis) treat mean drift-diffusion completion time. General matrix-geometric theory explains a rational generating function, but a generic two-phase law need not be a positive mixture of geometrics; the strict characteristic sign is the nontrivial comparison. Relevant semantic mathematical-record and primary-literature searches yielded no exact covering result. The remaining risk is an unindexed treatment of the same gate-persistent count observable or a more general theorem covering the sign identity.

## Mathematical value — PASS

The number of resets measures search intervention cost. This model's persistent gate breaks ordinary renewal at reset times; a single-geometric count law and its constant hazard are physically plausible but false here. Exact positive mixture weights, strictly decreasing absorption hazard, exponential tail scales, and a strictly quantified variance penalty give experimentally meaningful predictions about rare search costs, beyond the known mean completion time. The full all-parameter strict classification is structurally motivated, not a parameter-specific calculation.

## Boundaries and limitations

The gate is stationary initially, independent of position and clock, and is not reinitialized on reset. All five model parameters are positive; excluded singular limits can collapse one component. No inference is made about a larger family of switching gates or nonexponential reset clocks. Existing time-law results are explicitly acknowledged. Literature review does not certify global publication priority; formal independent scientific validation remains outstanding.

Self-review: passed. Independent audit: not yet performed.
