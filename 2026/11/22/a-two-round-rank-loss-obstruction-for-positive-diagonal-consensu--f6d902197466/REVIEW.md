# Scientific review

## Correctness — PASS
Every positive-diagonal star factor has independent leaf rows and corank at most one. Left and right null vectors of distinct singular star factors have nonzero pairing, since the corresponding normalized pairing equals \(1+\sum b_i e_i/(a_i d_i)>0\). Hence two adjacent singular rounds cannot cause consecutive accumulated rank drops. There must be at least \(m\) separated rank drops to reach rank one, proving \(T\ge2m-1\). Exact Fraction arithmetic verifies the three-factor witness. The mathematical argument is independent of any finite tests.

## Originality — PASS on inspected evidence, with residual risk
The earliest inspected motivating paper (Hendrickx–Shi–Johansson, arXiv:1302.6668) establishes existence on every connected undirected graph and discusses minimizing steps, not a universal positive-diagonal rank-loss obstruction on stars. Ko's 2010 thesis derives factorization and scheduling results in different, notably symmetric, averaging classes; the inspected sections do not state this unrestricted result. The 2013 Ghosh–Lee paper concerns finite-horizon dynamic decentralized-controller synthesis rather than products of nonnegative stochastic factors; only its abstract was accessible, and it remains a material unresolved source-inspection risk. Searches of related repository findings yielded spectral contraction, peer-epoch and stochastic matching claims, not the stated two-round rank obstruction. These searches do not prove uniqueness.

## Value — PASS
The elementary individual corank bound would only give \(m=n-1\) rounds. This structural noncancellation lemma nearly doubles that necessary horizon for every star, without restricting factor weights, temporal heterogeneity, or the target consensus distribution. It is a mathematically motivated partial answer to the minimum-round question in the foundational finite-time positive-diagonal consensus setting. Its limitation at larger star sizes is explicit.

## Limitations
The construction proves sharpness only for three vertices; for larger stars, matching upper bounds are not provided. Potential equivalent rank-product results in unindexed or incompletely inspected literature may affect priority. No independent mathematical audit has been performed.

Self-review: passed. Independent audit: not yet performed.
