# Review of Two-scale jamming and rare maximality failure in the rank-two Kneser graph

## Correctness — PASS

The three admissible-set counts are exactly \(\binom n2\), \(2(n-2)\) and \(n-2\), independently of previous labels. Only one third-success candidate closes a triangle; the other candidates create a full-star branch, with \(n-4\) independent remaining exponential clocks. This establishes the joint time/size mixture, moments, and conditional limits analytically. `check.py` independently replays exact small-state distributions and geometric and Laplace identities for \(n=5,6,7,8\); its finite tests are not treated as a proof for all \(n\).

## Originality — PASS (qualified)

Closest source literature: Pippenger (1989, https://doi.org/10.1137/0402034) defines graph RSA (abstract only accessed); Dhara et al. (2016, https://arxiv.org/abs/1604.03918) handle sparse random hosts; Krivelevich et al. (https://doi.org/10.1002/rsa.21200) address local-limit and concentration questions; Balogh et al. (https://doi.org/10.1002/rsa.21090) study the randomly thinned Kneser graph's optimum. The closest related indexed rare-catastrophe finding concerns complements of bipartite graphs, not the triangular-graph complement defining \(KG(n,2)\). The result's exact marked time law is not implied by the inspected statements. Existing generic exponential race facts and intersecting-edge classifications are acknowledged. Partial full-text access to the older RSA source and related finding leaves specific historical-priority risk.

## Value — PASS

Rank-two Kneser graphs are natural benchmark instances for the random greedy maximum-independent-set problem. The rare catastrophic outcome occurs with a vanishing yet exactly quantifiable probability; it inflates variance at order \(n\) while normalized fluctuations vanish weakly. The simultaneous two-scale jamming times demonstrate a qualitatively different failure trajectory and give an exact simulation benchmark rather than merely an isolated cardinality table.

## Limitations

Only rank-two Kneser graphs and the specified clock model are proved; the time law is not automatically valid for arbitrary i.i.d. continuous clocks, although the final-size law is. Historical uniqueness is not certified; inaccessible plausible older literature remains a risk. The supplied independent audit channel has not been exercised.

Self-review: passed. Independent audit: not yet performed.
