# Scientific review: signed spectra of symmetric ratio-type copula chains

## Correctness — PASS

For the stated class the centered Markov operator is compact and self-adjoint because the symmetric density is continuous on the compact square. The covariance formula (2) follows by integrating the joint density twice by parts; all boundary terms vanish. For positive parameters, the uniformly differentiable geometric expansion (3) produces a trace-class sum of nonnegative rank-one operators, and the Vandermonde independence of sampled features gives infinite positive rank. The spectral theorem then yields complete monotonicity at all nonnegative lags. For negative parameters, the exact Cauchy double-alternant (6) gives every principal-minor sign and hence the \(LDL^\mathsf{T}\) pivot sequence \(-,+,-,+,\ldots\). Smooth derivative-bump approximation transfers arbitrary finite positive and negative subspace dimensions to the Markov operator; compactness gives infinitely many eigenvalues of both signs. These arguments establish all index and parameter quantifiers, not just finite experiments. The included exact-rational checker reproduced determinant and pivot identities through dimension six.

The only assumption about the distribution is that the ratio formula is a genuine copula with positive denominator; no arbitrary parameter is presumed valid. The published exponential example meets this condition in the stated interval, excluding the positive singular endpoint. No infinite-dimensional theorem is inferred solely from the finite computations.

## Originality — PASS, with residual historical-priority risk

The 2024 source defining the symmetric separable ratio construction and its exponential example addresses admissible parameters, quadrant ordering and rank dependence rather than the covariance-kernel inertia or Markov spectral signature. Longla's 2024 spectral representation covers the existence of eigenfunction decompositions for generic symmetric square-integrable copula densities, but does not determine the positive/negative inertia of this particular ratio construction. The 2022 Ali–Mikhail–Haq Markov analysis concerns mixing bounds; the 2023 ratio-type copulas paper concerns constructions and dependence measures. These results do not, as written, imply the exact all-dimensional alternation of (6) or the positive-parameter all-observable complete monotonicity. The old Cauchy determinant and spectral theorems are explicitly acknowledged as ingredients rather than claimed new results. Indexed searches found no prior identical formulation; absence of search results is not a proof of historical uniqueness, and older kernel literature could contain equivalent results.

## Value — PASS

Quadrant dependence governs monotone statistics, but gives no immediate sign classification for arbitrary centered time-series observables. The result makes a sharp, reusable distinction for an established family: positive parameters forbid negative spectral modes and force complete monotonicity of *every* lag covariance; every negative parameter, including the extended admissible range of the exponential example, has infinitely many modes of each sign and admits indefinitely alternating covariances. The exact finite-matrix inertia is a structural signature applicable to arbitrary sample grids and is not a small numerical enhancement or arbitrary parameter slice. The result helps assess spectral assumptions in stationary copula-chain modeling without claiming to compute mixing rates.

## Closest literature and limits

- El Ktaibi, Bentoumi and Mesfioui (2024), https://doi.org/10.3390/math12111743 — prior ratio family and exponential model, not spectral classification.
- Longla (2024), https://doi.org/10.1007/s00362-024-01559-9 — generic spectral framework and other copula constructions, not the Cauchy-inertia calculation.
- Longla, Mous-Abou and Ngongo (2022), https://doi.org/10.1007/s44199-022-00045-1 — mixing of Ali–Mikhail–Haq, not the present sign laws.
- Chesneau (2023), https://doi.org/10.3390/sym15050977 — earlier ratio constructions, not the stationary spectral result.

The strictly positive denominator assumption excludes certain singular endpoints; no exact eigenvalue locations or mixing rates are claimed. General historical priority requires further independent literature scrutiny.

Self-review: passed. Independent audit: not yet performed.
