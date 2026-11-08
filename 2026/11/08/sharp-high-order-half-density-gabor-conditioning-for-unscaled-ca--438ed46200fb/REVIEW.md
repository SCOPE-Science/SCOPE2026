# Review of sharp high-order half-density Gabor conditioning

## Correctness
PASS. The statement fixes both the integral-one spline normalization and the physical Gabor lattice. The exact Zak/Walnut identity gives the actual optimal frame multipliers, with the order-two spline furnishing a direct factor check. On the central frequency interval the Fourier alias remainder is uniformly geometrically small relative to each dominant term. Convexity of the two leading sinc-power profiles gives the global minimum, and an outer-frequency gap excludes any escaping minimizer. Partition of unity and a uniform distant-alias bound control the upper frame constant. The checker separately compares direct spline Zak sums with Poisson aliases and tests representative minima; finite computation is not invoked as the proof of the infinite limit.

## Originality
PASS relative to inspected literature and available records. Hasannasab–Lemvig (2026, arXiv:2609.13116) prove existence and classify Zak zeros but do not derive a large-order sharp Gabor bound. Stangl–Frederick (2026, arXiv:2609.00481) study the second-order spline. Christensen–Kim–Kim (2017, arXiv:1708.04803) approximate Gaussian windows by **rescaling** large-order splines; their regime does not cover the fixed unscaled window and the displayed sharp constant. Kloos–Stöckler (2013, arXiv:1311.7359) consider exponential B-splines and density-to-one behavior, not spline-order growth. The closest related frame calculations for the hat spline concern changes of lattice parameters at fixed order. None of these statements dominates the joint asymptotic \(A_n\sim2(8/\pi^2)^n\), \(B_n^{\mathrm{up}}\to1\) in this normalization. Residual risk: an equivalent sinc-alias calculation could be present in older numerical spline or Weyl–Heisenberg literature under different indexing.

## Mathematical value
PASS. Increasing spline order is an intrinsic smoothness parameter for a standard compactly supported generator family, whereas frame existence at this lattice is known for every order. The sharp exponential decay constant, exact leading factor, and frequency localization quantify the reconstruction penalty of smoothing a window without changing the lattice. These are natural stability invariants, not a chosen finite example or a rescaled restatement of known frame existence. The quantitative result is distinct from studying approaching critical lattice density.

## Limitations
Asymptotics are for the fixed lattice with steps one and one-half and integral-one, unscaled cardinal splines. No general lattice optimization, exact finite-order extrema, or other window class is asserted. Literature priority is not independently certified.

Self-review: passed. Independent audit: not yet performed.
