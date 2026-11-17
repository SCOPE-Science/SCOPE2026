# Review of exact planar shear distortion

## Correctness

**PASS.** The determinant-one chain rule gives upper bounds by nonnegative column sums at every homogeneous derivative level. Those sums strictly increase with derivative order when the shear is nontrivial. Ornstein's same-order non-inequality supplies compactly supported smooth functions that asymptotically isolate any chosen top-order derivative monomial, and uniform dilation eliminates lower orders. Reverse triangle inequalities then prove matching lower bounds, with no false assumption that jets can be assigned arbitrarily. Every nonzero input has a positive zeroth-order mass, giving strict nonattainment. Polynomial comparisons prove both order-three cusps. The standalone checker verifies finite coefficient algebra, not the functional-analytic theorem.

## Originality

**PASS, subject to publication-priority uncertainty.** Hamad's 2026 full text uses the same norm but classifies surjective isometries rather than sharp norms of nonisometric shears. Ornstein's theorem already supplies the critical top-order derivative concentration and is explicitly credited; it does not itself state any affine Sobolev composition norm. Related general composition estimates and Sobolev isometry classifications concern other questions and do not supply the current all-order constant or the order-three cusp diagram in inspected material. The connection between the classical non-inequality and this coordinate-dependent quantitative distortion is the claimed contribution. The formula may nevertheless be known under different terminology; database searches do not certify priority.

## Mathematical value

**PASS.** The full derivative-sum norm is a current natural object of Sobolev isometry theory. Determining its exact distortion under a basic volume-preserving affine deformation is a natural quantitative problem, not an arbitrary numerical parameter. A strict rank-one high-frequency gap of at least \(2q(1-q)/3\) for \(0<q<1\) demonstrates that ordinary single-direction tests do not reach the sharp order-two norm, which requires an endpoint \(L^1\) phenomenon. At orders two and three the calculation completely classifies the shear allocation regimes and the exact cusp locations, providing test cases for quantitative stability of Sobolev symmetry groups. No higher-order crossover classification or nonlinear mapping generalization is claimed.

## Closest literature and limits

References: Hamad, arXiv:2611.09577v1 (full HTML inspected); Kazaniecki–Stolyarov–Wojciechowski, DOI:10.2140/apde.2017.10.351 (Theorem 2, proof, and adjacent text inspected); Ornstein (1962), DOI:10.1007/BF00253928; Biegert–Nittka (2012), arXiv:0807.0360 (cited in Hamad; direct preprint not accessible); Oliva–Prats (2017), DOI:10.1016/j.jmaa.2017.02.016 (abstract and opening inspected). The main unresolved risk is an older direct evaluation of these shear composition norms or an equivalent general jet-norm result. The script does not construct the Ornstein extremizers or independently verify the classical theorem.

Self-review: passed. Independent audit: not yet performed.
