# Scientific review: the first nonisomorphic cubic epidemic pair

## Correctness — PASS
The six-vertex cubic graphs are exhaustively classified by taking complements of the two possible two-regular graphs. The probability tails follow from finite edge-state sums. Independently constructed induced-vertex connectivity recurrences reproduce the same distribution polynomials for both graphs. The resulting factorized tail differences are strictly positive at thresholds four through six for every interior transmissibility. Exact moment formulas give the polynomial \(Q(p)\) governing the variance difference. Under \(u=p/(1-p)\), Descartes' rule and endpoint signs prove a unique simple crossing, not merely a sampled sign change.

## Originality — PASS, with residual priority risk
Newman's epidemic/percolation equivalence supplies the model; Miller and Ritchie et al. give network-clustering context. Allard et al.'s general small-graph exact procedure is the closest broader computational coverage. The inspected source material does not state the explicit pairwise stochastic-dominance factorization together with an all-probability one-crossing variance classification. General algorithms for deriving distributions are acknowledged and not represented as new. Historical unindexed tables and supplements remain a material novelty risk.

## Value — PASS
Equal degree and equal edge count isolate the structural effect of triangles in the first graph size where a nonisomorphic cubic comparison exists. A stochastically larger outbreak at every probability but a smaller variance above a sharp transition demonstrates a distinct, motivated dispersion-risk effect. The cutoff is complete for this natural smallest comparison and gives a reproducible benchmark for epidemic-network risk.

## Limitations and verification
This theorem concerns uniform initial infection and independent identically distributed edge transmission; common random infectious periods can create correlated transmissions and are not included. No result is claimed for larger cubic graphs or other stochastic epidemic dynamics. Exact checks and the independent-recurrence implementation are in `verify.py`; they do not replace the analytic continuum sign argument. The review has no independent scientific audit.

Self-review: passed. Independent audit: not yet performed.
