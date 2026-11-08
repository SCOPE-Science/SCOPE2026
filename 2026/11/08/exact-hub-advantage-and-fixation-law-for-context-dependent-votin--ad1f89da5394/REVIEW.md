# Review of the exact star fixation law

## Correctness — PASS

For asynchronous uniform-neighbor adoption with two strictly positive acceptance probabilities, generator harmonicity yields two exact relations for the hub-zero and hub-one state families. Their difference has a constant geometric ratio \(q_m=(mr+1)/(r(m+r))\); the absorbing boundary conditions uniquely normalize it. The explicit placement advantage is strictly positive for every \(m>1\) and zero for the two-vertex star. The large-star limit follows by uniform exponential convergence and Riemann sums. The finite chain has no nonconsensus closed class. A separate exact-rational full-chain solver independently checks every state up to six leaves for four rate pairs, totaling 1092 assertions. The analytic argument, not the enumeration, proves the arbitrary-size statement.

## Originality — PASS, subject to residual publication-priority risk

Becchetti–Bonifaci–Cruciani–Pasquale (2023), https://arxiv.org/html/2305.07377v2 , proves an all-configuration fixation formula for regular graphs (Theorem 3 and Appendix F), and explicitly identifies biased evolution on general topologies as challenging (Section 5). This does not entail the new two-family formula on nonregular stars. Czaplicka et al. (2022), https://arxiv.org/html/2203.05376v1 , studies biased copying on complete/random networks, not exact finite-star fixation. Durocher et al. (2022), https://arxiv.org/html/2201.08207v2 , uses a different neighbor-selection transition kernel. Petsinis et al. (2022), https://arxiv.org/abs/2211.14676 , uses positional weighted-neighbor bias, not the present uniform-neighbor acceptance kernel. Zhang et al. (2012), https://doi.org/10.1155/2012/940465 , proves exact star formulas for fitness-weighted birth-death reproduction. de Souza–Neves (2020), https://arxiv.org/abs/2003.05462 , studies birth/death Moran selection on stars, not uniform-neighbor pulling with independent opinion-dependent acceptance. Public mathematical-record comparisons and mathematical title/alias searches identified no equivalent theorem. An unindexed or differently parameterized exact star result may exist; universal priority is not claimed.

## Value — PASS

Exact fixation probabilities are a core invariant of network opinion dynamics. The motivating 2023 model's biased results focus on regular graphs while the effect of degree heterogeneity is topology-dependent. A star is the canonical maximally degree-heterogeneous tree: the complete answer, explicit strict hub-versus-leaf leverage for every seed budget, and the asymptotic positive hub influence versus vanishing single-leaf influence supply motivated structural information beyond a numerical small-graph example. The result does not extrapolate to all heterogeneous graphs.

## Limits

Parameters must be fixed and positive; the dynamics uses asynchronous uniform-neighbor pulling, not fitness-weighted selection. The large-star limit fixes the ratio of acceptance probabilities. Exact timing and nonlinear extensions remain unproved; independent external review is outstanding.

Self-review: passed. Independent audit: not yet performed.
