# Self-review

## Correctness — PASS

Using the stated \(e^{-2\pi i x\xi}\) convention, the inverse Fourier transform of \(|\widehat{\mathbf1_\Omega}|^2\) is the autocorrelation \(\mathbf1_\Omega*\mathbf1_{-\Omega}\). With \(d>3L\), the perturbed peaks near \(\pm d\) and \(\pm2d\) stay disjoint. Plancherel gives \(E^2=2\|A\|_2^2+2\|B\|_2^2\). The three disjoint cusp tents give \(\|D_sK_L\|_2^2=4|s|^3\) exactly, and the top-distance peak measures \(|v|\) linearly. These facts prove the uniform two-sided estimate; the pure splitting direction proves the exact constant and optimal inverse exponent. Direct exact rational integrals of the original autocorrelation difference passed the standalone checker. The finite checks are supplemental, and the theorem is restricted to the declared neighborhood.

## Originality — PASS relative to inspected sources

Xia–Xu's 2026 interval-phase-retrieval analysis establishes uniqueness and stability for at most two intervals and counterexamples to global uniqueness for at least three, not a sharp anchored modulus at a three-interval distance collision. Ranieri et al.'s collision-free sparse uniqueness theory does not cover repeated distances or prove this \(2/3\) exponent. Novikov–White's multidimensional sparse-support results are distinct. Relevant published-finding corpus searches on collision stability, equal intervals, three-point turnpike phase retrieval, Hölder exponents and aliases found no claim with an implication covering this exact continuous-three-interval result. Related finite cyclic three-frequency results concern different objects and implications. There remains a literature risk from older covariogram/B-spline local-stability theory; the searches are not a novelty certificate.

## Mathematical value — PASS

The smallest equal-width interval system with a repeated pairwise distance is a natural boundary of the turnpike collision-free regime. The sharp \(2/3\) inverse exponent, exact leading energy \(8|\varepsilon|^3\), and uniform two-direction estimate identify the precise severity of that instability and distinguish it from global nonidentifiability of unrestricted three-component unions. The quantity is intrinsically motivated by recoverability at the first collision, rather than an arbitrary parameter slice.

## Limits and closest literature

The result is anchored, not all-pairs local stability; lengths and count of intervals are known, and the measurement is full continuous squared Fourier magnitude. Xia–Xu (arXiv:2606.19855), Ranieri et al. (arXiv:1308.3058), and Novikov–White (arXiv:2011.00619) provide related foundations but not the present sharp modulus in the inspected material. Priority against all historical literature is not established.

Self-review: passed. Independent audit: not yet performed.
