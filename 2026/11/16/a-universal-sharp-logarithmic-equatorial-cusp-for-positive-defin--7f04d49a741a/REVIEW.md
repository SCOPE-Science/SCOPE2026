# Scientific review

## Correctness — PASS

The exact formula for \(P'_{4j+1}(0)\) follows from Rodrigues' formula, and Stirling gives \(\sqrt{8j/\pi}+O(j^{-1/2})\). The Laplace integral for \(P_n\) gives uniform interior angular derivative estimates through order three. Splitting at \(J=\lfloor |h|^{-1}\rfloor\) then controls both the cubic Taylor errors and the high-frequency tail by \(O(|h|)\). The resulting coefficient is exactly \(A\sqrt{8/\pi}\). The packaged checker passed 90 finite tests. This review does not treat those finite tests as proof of the infinite statement.

## Originality — PASS relative to the inspected material, with priority risk

The motivating 2026 paper establishes failure of equatorial differentiability for a particular sparse Legendre series. The newly assessed statement gives an exact two-sided logarithmic coefficient, a controlled \(O(|h|)\) remainder, and universality over a nontrivial asymptotic class of positive coefficient sequences. Classical Legendre asymptotics and Schoenberg theory alone are known but do not literally state this sum asymptotic. The motivating 2026 preprint was inspected in full using its public arXiv HTML rendition (especially §4.1–4.3): it gives the same seed, exact Legendre slopes, and Poisson-regularized nondifferentiability proof, but no two-sided logarithmic asymptotic for the original boundary series. Its analytic strict-positive-definiteness admixture is known, not new. Searches did not identify a directly covering theorem; absence of a match does not establish global novelty.

## Value — PASS

The exact leading modulus is a precise local regularity invariant for a natural spherical covariance witness, sharpening a bare failure-of-differentiability obstruction. Stability under faster coefficient perturbations and strictly positive-definite analytic admixtures makes the quantitative boundary robust and useful for local regularity and interpolation error estimates. The claim is not offered as a general sharp regularity theorem for arbitrary spherical kernels.

## Principal limitations

The motivating manuscript was inspected via its full public HTML version; its qualitative nondifferentiability is distinct from the quantitative theorem here. The proof concerns the particular arithmetic Legendre support and the specified coefficient asymptotics. Independent verification has not been performed.

Self-review: passed. Independent audit: not yet performed.
