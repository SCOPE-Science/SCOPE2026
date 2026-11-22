# Self-review of the sharp robust Poisson-aliasing claim

## Correctness (PASS)

The domain is the full compact location-scale rectangle and arbitrary positive probability mixtures, with a shared uniformly random phase on an \(N\)-node cyclic grid. The Cauchy quantile change sends each component to a circular Poisson kernel with alias ratio squared \(r^2=((c-m)^2+(a-s)^2)/((c-m)^2+(a+s)^2)\). Orthogonality gives exact variance \(2r^{2N}/(1-r^{2N})\). Minkowski plus Dirac extremizers reduces arbitrary positive mixtures exactly to one component. Monotonicity in distance forces the reference center to zero; unimodality in target scale forces extreme-scale controls; a comparison of their crossing with the narrow-scale individual maximizer yields the unique two-branch optimal width and sharp cusp. The proof is infinite and analytic; 15,968 independently rerun numerical assertions support, but cannot certify, it. Edge cases \(C=0\), \(C^2=A(B-A)/2\), and \(C^2\ge AB\) were included in the reasoning.

## Originality (PASS relative to inspected evidence)

The 2024 randomized Möbius rule, the 2026 polynomial-weight extension and the 2026 inverse-CDF Fourier approximation provide the changes of variables and general aliasing framework. A published single-Poisson randomized-grid result already provides exact variance and near-boundary asymptotics. A published centered Cauchy-mixture result already treats deterministic parity-dependent scale optimization. Both were read as mathematical statements, and neither contains or dominates the all-reference, all-positive-mixture location-scale minimax optimizer with the transition \(2C^2=A(B-A)\). The inspected sources cannot establish universal priority: a hyperbolic Chebyshev-center reinterpretation in less-indexed literature remains possible.

## Value (PASS)

The target is an arbitrary positive mixture with a potentially unknown normalizing mass in a natural compact location-scale uncertainty family, rather than a manufactured finite list. The result solves its continuous sharp minimax Poisson Fourier-tail problem over *every reference Cauchy center and width*, shows that mixtures cannot worsen the extremal risk, provides an \(N\)-independent optimal design and exact exponential risk, and proves a counterintuitive narrowing-then-widening cusp with a rigorous exchange of active extremal scales. This is a substantive exact extremal classification and a robust calibration principle for nonuniform Fourier sampling; it is not a claim of general quadrature optimality.

## Limitations and closest literature

The result does not cover arbitrary reference probability measures, general integrands, noise, deterministic phases or arbitrary uncertainty shapes. Classical Fourier aliasing and Cauchy–Poisson conjugacy are not new. The main residual originality risk is an older equivalent pseudohyperbolic-center optimization. Formal independent validation has not been performed.

Self-review: passed. Independent audit: not yet performed.
