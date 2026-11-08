# Self-review

## Correctness — PASS

For the exact estimator definitions in RESULT.md, Walsh orthogonality proves the unbiasedness and the Parseval variance decomposition; without-replacement covariance gives the finite-population factor. The partition of off-diagonal edges into XOR matchings and equality in Cauchy--Schwarz prove both a sharp bound and the complete equality classification. The permutation matrix \(P_s\) gives explicit strictly positive-definite sharp examples. Orthogonality of distinct degree-two sign monomials proves the shared-sign identity. The standalone exact checker verifies 3151 finite assertions, but the unbounded-dimension theorem is justified analytically. Normalization includes the factor of two between ordered and unordered off-diagonal entries; the \(k=n\), \(n=2\), and diagonal-only boundary cases are handled separately.

## Originality — PASS, qualified

The 2023 primary stochastic-probing analysis studies graph-color partition probe variances, rather than the exact unmodified Hadamard-row finite-budget worst-case ratio. The 2013 hierarchical-probing work already develops a shared-sign Hadamard correction; the correction itself is **not** claimed to be new. The relevant 2020 extended hierarchical-probing analysis likewise does not state the proved XOR-matching worst-case classification in the inspected passages. The specialist Hadamard-trace paper of Fika and Koukouvinos could not be inspected in full, and overlapping prior analysis remains possible. Semantic mathematical overlap searches yielded no direct match; no claim is made that absence of a search result establishes uniqueness.

## Value — PASS

The result identifies a concrete estimator-selection failure mode: at fixed low query budget, an ostensibly highly structured orthogonal probe family may have variance greater by a factor growing linearly in dimension. The sharp extremizers can be strictly positive-definite and arbitrarily well-conditioned, so the effect is not limited to indefinite or ill-conditioned cases. The precise query-budget crossover, equality characterization, and variance restoration by the established random-sign fix make this a useful benchmark for stochastic trace computation.

## Closest literature and limits

Frommer--Rinelli--Schweitzer (2023), arXiv:2308.07722; Stathopoulos--Laeuchli--Orginos (2013), arXiv:1302.4018; Laeuchli--Stathopoulos (2020), DOI:10.1137/18M1176427; Fika--Koukouvinos (2015), DOI:10.1080/03610918.2015.1096373 (full text unavailable). Specially structured hierarchical row ordering and adaptive methods are not covered.

Self-review: passed. Independent audit: not yet performed.
