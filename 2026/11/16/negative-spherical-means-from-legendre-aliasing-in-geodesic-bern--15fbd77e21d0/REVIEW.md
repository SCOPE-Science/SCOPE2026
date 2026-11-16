# Scientific review

## Correctness — PASS

The exact input \(P_{2n-2}(\cos\theta)\) is a zonal positive-definite kernel on \(S^2\) by spherical-harmonic addition. Darboux's interior Legendre expansion at \(\theta_j=\pi j/n\) yields an aliased phase \(2\pi j-3\theta_j/2-\pi/4\), giving the asserted locally uniform profile after binomial concentration. The beta-binomial identity supplies an exact expression for the spherical mean, and the beta mean/variance bounds produce an \(O(n^{-1})\) correction; uniform Legendre Bernstein bounds control endpoints. The resulting beta cosine integral evaluates to \(-\sqrt\pi/(4\sqrt2)\). Negative constant Legendre coefficient proves non-positive-definiteness on \(S^2\). The standalone numerical checker passed 28 assertions. This is a proof of eventual failure, not of the least failing degree.

## Originality — PASS relative to inspected evidence

Otten–Nguyen–Watts (arXiv:2608.04836v1, 2026-08-05) prove positivity preservation on the circle for all degrees and discuss an **affine dot-product** higher-sphere obstruction; their available full text does not state the present angular two-sphere monopole limit. Published affine Bernstein findings (full RESULT.md inspected) concern a distinct operator. The nearest angular dimension-lifting result establishes failure to lift to positivity on *all* sphere dimensions simultaneously, which does not imply failure on \(S^2\). The present negative zeroth Legendre coefficient and exact aliasing constant provide the non-covered fixed-sphere implication. Searches included equivalent wording, the constant, spherical means, Legendre aliases, the source and the operator. Priority risk remains from classical spherical approximation literature not fully indexed.

## Value — PASS

A real question prompted by a recent circle-positive-preservation theorem is whether the **same geodesic sampling** preserves spherical covariance positive definiteness. The theorem provides an infinite-family fixed-sphere obstruction and a sharp diagnostic amplitude/phase law; its failure is detected by the most natural spherical invariant, the constant harmonic coefficient. The distinction between failure of Hilbert-sphere lifting and failure on the original two-sphere is mathematically substantive. The limit is a structural phenomenon rather than arbitrary small-degree arithmetic, and the input sequence is explicitly admissible.

## Closest literature and limitations

The mathematical comparison uses full accessible text for Otten, Nguyen and Watts, *Preservation of Positive-Definiteness by Bernstein Operators on the Circle*, https://arxiv.org/abs/2608.04836; published affine results at https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-sharp-dimension-degree-frontier-and-infinite-sphere-lift-for-aff--3785c4062726 and https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-a-sharp-degree-frontier-for-affine-bernstein-approximation-of-sp--a8520e405e97; and standard Legendre asymptotics from Szegő/DLMF. There is no independently verified publication priority; an older aliasing equivalent remains possible. No sharp finite cutoff, no uniform endpoint asymptotic, and no higher-dimensional universal frontier is claimed.

Self-review: passed. Independent audit: not yet performed.
