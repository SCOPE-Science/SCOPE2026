# Scientific review: quarter-power three-site adsorption

## Correctness — PASS

The exact clock-to-embedded-chain reduction is independently reconstructed using \(a\binom b2\) and \(b\binom a2\) available paths. The normalized imbalance is a genuine stopped martingale with deterministic multiplicative factor \(h\sim(s/m)^{1/3}\). For critical initial imbalance, its conditional quadratic variation to the \(m^{1/2}\) cutoff converges to \(m\) and its increments obey Lindeberg; the remaining quadratic variation is \(o(m)\). Crossing of the physical boundary \(|d|=s\) yields the \(m^{1/4}\) Gaussian-power terminal law. For fixed nonzero relative imbalance, the normalized martingale remains within \(o_{\mathbb P}(m)\) of its initial value until the unique deterministic boundary crossing. The proof removes the possible terminal states with at most three survivors by a vanishing-probability argument. A separate labeled-state exact dynamic program and count-state exact dynamic program agree for all 16 pairs \(1\le a,b\le4\); 9,798 drift/variance identities are checked. The finite checks are diagnostics, not substitutes for the proof.

## Originality — PASS (qualified to inspected evidence)

The closest general prior work is Bennett–Bohman, arXiv:1210.3581, which analyzes random greedy hypergraph matchings. Applied to the balanced path hypergraph, its upper bound is only \(R=O_{\mathbb P}(m^{3/4+o(1)})\), not the sharp \(m^{1/4}\) scaling nor the limiting distribution. The 2011 Lebovka–Karmazina–Tarasevich–Laptev study uses finite-dimensional square lattice linear objects and numerical anisotropic adsorption, not all three-site paths of a dense bipartite graph. The 2005 Penrose–Sudbury work treats graph monomers and dimers. Targeted source, graph-alias, random-matching, normal-power and parameter searches found no identical theorem. A 2002 paper by Cortés–Valencia on bent trimers was accessible by abstract only; its disordered substrates and Monte Carlo scope do not establish direct coverage, but are a remaining priority risk. Non-indexed work or hidden specializations are not excluded by search failure.

## Value — PASS

The all-path, three-site greedy deposition model is a natural dense-network counterpart to finite-dimensional trimer adsorption. The result gives a sharp law of the number of vacant sites, not just a leading coverage fraction. The critical regime has a non-Gaussian \(3/2\)-power transform of a normal, a new \(m^{1/4}\) vacancy scale, a \(\sqrt m\)-size initial-imbalance crossover and an explicit macroscopic \(3/2\)-power depletion law. This sharpens the general hypergraph-matching estimate on a regular, physical graph-based family and supplies a concrete benchmark for adsorption fluctuations. The network is mean-field rather than planar; no planar-lattice exponent is claimed.

## Literature and limitations

Primary full-text comparisons: Lebovka et al., arXiv:1109.3271v1, introduction, model section, finite-size and jamming discussion; Bennett and Bohman, arXiv:1210.3581, introduction, theorems and proof framework. Supporting abstracts: Penrose and Sudbury, arXiv:math/0503519; Cortés and Valencia, DOI 10.1006/jcis.2002.8443. A direct priority certificate cannot be claimed. The mathematical result is model-specific and the independent audit remains outstanding.

Self-review: passed. Independent audit: not yet performed.
