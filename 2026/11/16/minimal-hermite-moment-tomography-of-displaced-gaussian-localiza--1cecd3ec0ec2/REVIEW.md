# Scientific review

## Correctness: PASS

The Fock matrix entries are precisely the Gaussian zeroth and first moments. For two different balls, the difference of their normalized defining quadratics is affine and has the same sign as the indicator difference on the symmetric difference. Integrating against the strictly positive Gaussian proves global injectivity. The positive-part integral is a convex differentiable potential with this moment map as its gradient, so the true parameters are its unique dual minimizer. Boundary transport and a Schur complement yield a strictly positive covariance Jacobian in all even real dimensions. Invariance of domain supplies the minimal continuous-data count. Planar Bessel formulas and independent numerical examples were checked with the attached script. The checks are finite corroboration, not substitutes for the proofs.

## Originality: PASS (historical priority provisional)

A current exact-claim search found no published equivalent among the returned records or the accessible earlier ledger titles and claims. Jaming–Speckbacher (2019) establish forward planar STFT sampling estimates; Kisil (2021) analyzes Fock/Toeplitz operator calculus; Abreu–Dörfler (2012) use prescribed eigenfunctions in an inverse problem. The 2000 moment-reconstruction paper gives a broad general-domain uniqueness theorem with a larger order-one complex moment array (including the mixed moment), not this minimal Gaussian ball family and its convex inverse/positive Jacobian. The affine separation argument is elementary and could well appear in older convex-moment folklore; this is an explicit residual priority risk. The 2026 Ramos paper was accessible only by abstract and remains a named limited comparison.

## Value: PASS

The question asks for the fewest Gaussian Gabor/Hermite operator coefficients needed to identify a single geometric aperture, without access to the full operator or unordered spectrum. This natural \(2d+1\)-parameter inverse problem is settled sharply in every dimension, and the convex objective gives an algorithmically explicit characterization of the unique target while the covariance Jacobian quantifies local recoverability. The statement is not asserted for general symbols and does not claim uniform global noise stability. Its value is the complete minimal-observation theorem and mathematically defined reconstruction, rather than just an instance of ordinary Gaussian integration.

## Relationship and limits

Specific comparisons: arXiv:1906.02964, arXiv:2108.13710, arXiv:1202.5841, arXiv:2204.03068, DOI 10.1088/0266-5611/16/4/312. No equivalence was found, but a failed search cannot certify novelty, and the classical geometric sign argument has uncertain independent priority. Numerical checks cannot establish the infinite-dimensional claims. No independent validation has occurred.

Self-review: passed. Independent audit: not yet performed.
