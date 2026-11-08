# Scientific review

## Correctness — PASS

The Laurent exponential and absolute weighted coefficient majorant are well-defined for every positive real radius. The essential singularity plus \(q(r)\to-\infty\) gives infinitely many coefficients of each sign at every strictly positive time. Finite cyclic Fourier eigenvalues give eventual positivity; coefficient periodization and weighted Laurent moments give the linear lower bound, with short-time and compact-time cases handled separately. Exact rational evaluation of the five-point stencil, the negative moment at radius 16, and the \(\alpha<105\) inequality make the \(1/500\) constant valid. A direct heat-symbol bound gives the stated quadratic upper bound. A standalone standard-library verifier ran 3977 assertions. Numerical tests are supporting checks, not infinite proofs.

## Originality — PASS, qualified

The closest prior mathematical result is the general spectral eventual-positivity theory of signed Laplacians in Chen et al. (2020), which already implies finite-dimensional eventual positivity. That known component is explicitly excluded from the new contribution. Cross and Zhang (2020) treat elliptic inverse positivity and a related five-point stencil, while Hu and Zhang (2021) design different positivity-preserving finite-difference schemes. Published results on filtered Crank–Nicolson lattice positivity concern nearest-neighbor spatial generators and rational time maps, and a published example of a nowhere-positive semigroup concerns a nontranslation-invariant infinite operator. Their precise claims do not entail the combined all-time infinite sign oscillation and quantitative periodic-grid delay. Earlier high-order-difference and convolution-semigroup literature may contain equivalent results; no independent priority determination has been performed.

## Mathematical value — PASS

The theorem supplies a structural warning about high-order heat semi-discretizations: spectral stability and even qualitative eventual positivity of each finite grid cannot guarantee positivity at any fixed dimensionless time across larger grids. The infinite signed kernel creates a provable, dimension-dependent recovery-time obstruction. The result separates elliptic inverse positivity from semigroup positivity and provides a reproducible analytical test case for positivity-preserving spatial discretizations.

## Scientific limitations

The theorem is restricted to symmetric finite-range translation-invariant stencils, strict nonzero-frequency damping and negative outermost coefficient. It gives a conservative linear obstruction and a nonsharp quadratic upper bound. Only exact arithmetic is analyzed. Specialized older overlap remains a priority risk; no independent scientific audit has been performed.

Self-review: passed. Independent audit: not yet performed.
