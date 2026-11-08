# Scientific review

## Correctness — PASS

The exact domain is the five-dimensional pure degree-two subspace of complex \(L^2(S^2,d\Omega)\), with normalized Funk averages and five unweighted complex readings. A trace-free quadratic and the great-circle second-moment identity give the Funk multiplier \(-1/2\). Orthonormal degree-two spherical harmonics and five-point DFT orthogonality yield the full five-eigenvalue Gram spectrum with the stated \(25/(64\pi)\) normalization. The condition minimax is proved by a two-interval monotonicity comparison and strict bounds beyond \(r=1/4\). The separate lower-frame minimax uses all three eigenvalue branches, including the high-latitude regime. No discrete computation is used to infer an infinite assertion. The reconstruction DFT is exact and has no hidden generic-position assumption beyond \(t\not=1/3\).

The checked, package-contained script passed 1,353 numerical assertions, including direct Funk integrals and inverse reconstruction. Numerical comparisons are supplementary; the proof covers all allowed latitudes, and boundary degeneracies are stated. A priority check has no bearing on the mathematical algebra.

## Originality — PASS, with historical-priority risk

The focal 2023 Funk-transform paper provides the spectral eigenvalue relation and a much broader infinite-dimensional reconstruction framework, but not a five-normal, single-ring quadratic design with a sharp algebraic best condition number. The 2018 spin-s sampling paper considers full low-pass spin functions on multiple iso-latitude rings and numerical condition-based placement, not this scalar degree-two Funk restriction or its exact simultaneous minimax. The preceding 2014 scalar low-pass design paper samples nine modes on multiple rings at degree cutoff three, again without a five-view pure-quadrupole minimax. The statement has been compared with the relevant published index records for spherical concentration and finite Radon tomography. None identified implies the specific optimality formula. This is a best-knowledge literature judgment, not a mathematical proof of global novelty; unindexed alternative optimization formulations remain a risk. The familiar Funk multiplier, spherical harmonic expressions and DFT are openly credited.

## Mathematical value — PASS

Pure degree two is the first nonconstant spherical-harmonic space observable through great-circle Funk averaging. Its five independent parameters make five labelled scans the minimal possible exact measurement count. A single regular latitude ring is a natural fixed-tilt acquisition geometry, not an arbitrary spectral slice. The finding completely determines all singular values and singular locations and, more importantly, produces the unique exactly optimal scan tilt for both relative conditioning and absolute worst-case recovery error. The coincidence of the two optima and the three-versus-two spectral split are useful algebraic design benchmarks for finite-angle spherical tomography.

## Closest sources and limitations

Quellmalz et al., arXiv:2303.05179v1, Section 3; Elahi et al., arXiv:1809.01321v1, Section III; and Khalid et al., arXiv:1403.4661, Sections II–III, were inspected beyond abstracts. This is a statement about **restricted equal-azimuth single-ring sampling**, not global optimality across all directional designs. Independent publication-priority and mathematical audits remain open.

Self-review: passed. Independent audit: not yet performed.
