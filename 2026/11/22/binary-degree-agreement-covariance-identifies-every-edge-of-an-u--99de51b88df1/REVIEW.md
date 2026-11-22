# Scientific review

## Correctness

PASS. For each host edge, the signed differences of independent Bernoulli replica edges are independent over distinct edges and have symmetric three-point laws. Conditioning two endpoint equality bits on their shared edge yields covariance \(2a(1-2a)\Delta_u\Delta_v\). Nonadjacent vertices use disjoint signed differences, hence have zero covariance. Fourier inversion proves every central gap \(\Delta>0\); comparison to symmetric binomial sums supplies the uniform lower bound. Hoeffding concentration and union bounding establish exact recovery at the stated finite sample count. The independent enumeration script produced `VERIFY_OK 78 exact host laws, 450 pair covariance identities, 54 gap bounds`. These finite tests do not independently certify the infinite theorem.

## Originality

PASS with residual historical risk. The inhomogeneous independent-edge model of Bollobás, Janson and Riordan (2005) does not state one-bit, two-replica degree coincidence reconstruction. Lyzinski, Fishkind and Priebe (2013) analyze matching of correlated graph replicas using adjacency data, while McGregor and Sengupta (2022) recover hosts from random subgraph observations. The closely related published published-finding corpus degree-covariance tomography theorems observe **raw degree vectors** under a dependent vertex-threshold edge mechanism; their polynomial signless-Laplacian identities do not imply the new binary-coincidence covariance positivity theorem. The exact same parameter reduction, namely nonlinear zero-indicators of edge-signed sums, was not located in the checked primary articles or semantic search. Search absence alone cannot prove historical priority.

## Value

PASS. One degree-agreement bit per vertex and paired trial loses almost all raw degree information; nevertheless the **positive support of the bit-covariance matrix identifies every unknown host edge**, including arbitrary heterogeneous independent bond probabilities. This is a genuinely distinct observation channel and motivates finite-sample network tomography using repeated coarse summaries. The polynomial sample bound makes the structural identifiability operational rather than just qualitative. The theorem does not estimate edge probabilities and its bound is not claimed optimal.

## Scope and limitations

No result is asserted for deterministic host-edge retentions, dependent edges, vertex misalignment, or unmatched replica edge probabilities. Self-review confirms internal analytic steps and finite exact checks, but does not constitute independent auditing or exhaustive priority certification.

Self-review: passed. Independent audit: not yet performed.
