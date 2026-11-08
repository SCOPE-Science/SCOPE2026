# Scientific review

## Correctness — PASS
The graph decomposition is exact: every geodesic from the common hub remains in one clique petal. Exponential exploration gives independent rates \(i(k+1-i)\). The double unit-rate endpoints yield an exact tilted residue \((k-1)^2\). The tilted mean is \(2kH_{k-2}/(k-1)\), uniformly close to \(2\log(k-1)\), while the tilted variance and centered exponential moment are uniformly bounded. These estimates establish the finite tail expansion and, by independence, the Gumbel and marked-Poisson limits for every growth regime of \(k\ge2\). The exact star boundary is separate. The companion finite checker reports `VERIFY_OK 33396 assertions` and is supplemental to the proof.

## Originality — PASS (priority qualified)
Full-text comparison covered Janson (1999), Asimit--Jones (2007, Proposition 1), Leskelä--Ngo (arXiv:1806.09568), and Mountford--Saliba (arXiv:1909.04563). **Fixed-\(k\) Gumbel convergence with the same \(\log\log m\) normalization is covered by Asimit--Jones**, so that specialization is not claimed as new. Their theorem assumes a single fixed phase-type law and does not yield the new uniform-in-\(k\) quantitative tail expansion for arbitrary dimension growth or the endpoint-stage marked Poisson limit. Janson establishes the pure-birth complete-graph law and its large-clique scaling, not the unrestricted maximum-over-cliques triangular array. Random configuration-model results have incompatible assumptions and first-order precision. No precise full-strength implication was found in the inspected papers or research records, but priority cannot be independently certified.

## Value — PASS
The claim measures exact near-completion flooding reliability of a natural articulated clique network and explains the already-known fixed-phase-type \(\log\log m\) centering and establishes **uniform control across arbitrarily growing phase dimension**. The uniformity across all interior clique sizes and the entire marked extremal point process improve materially on a fixed-clique Gumbel specialization. The one-edge petal boundary provides a clear structural contrast.

## Limits and literature
All passage weights are independent exponential; roots other than the shared hub, general petals and recovering epidemics are outside scope. Computations test finite formulas, not convergence over infinitely many sizes. Exact prior-claim searches cannot certify novelty. Primary sources: https://arxiv.org/abs/1806.09568 ; https://arxiv.org/abs/1909.04563 ; https://doi.org/10.1017/S0963548399003892 .

Self-review: passed. Independent audit: not yet performed.
