# Independent mathematical audit

## correctness

PASS

Reconstructed the Cayley rotation matrix as angle α=2 arctan(sqrt(h)Z/2), the exact diffusion Fourier multiplier exp(-m²h/2), and for r=h/4, t=2/h the Gaussian Laplace–Chebyshev representation λ_m(h)=sqrt(t/π)∫_{0}^{∞}e^{-ty}y^{-1/2}T_m((1-y)/(1+y))dy. K_m has precisely m alternating simple positive zeros y_j=tan²((2j-1)π/(4m)). If its Laplace transform had m+1 distinct positive zeros, a nonzero linear combination of the m+1 exponential kernels vanishing at the m prescribed sign changes, by the Rolle/Chebyshev bound, has exactly those m simple zeros and no others, making the integral g(y)q(y) strictly one-signed and contradicting the assumed vanishing. This establishes the infinite-domain <=m zero count, not via finite samples. Gaussian integration and IBP yield A(r)=sqrt(π/(2r)) exp(1/(2r)) erfc(1/sqrt(2r)), λ1=2A-1, λ2=1+4/r-4(1+1/r)A. At r=1 the alternating-erf series and rational comparisons sqrt(e)>8/5, sqrt(π/2)>5/4 show A(1)>47/75>5/8, hence λ2(4)<-1/75. Endpoint λ_m(0+)=1 and λ_m(∞)=(-1)^m force exactly one λ1 root and exactly two λ2 roots, with no extras by the zero-count theorem. Smooth nondegenerate increment density on (-π,π) and strict |λ_m|<1 for m≠0 imply unique Haar invariant law at any finite h>0. Checked large-step asymptotics and the factor 1/2 in the Cayley map. Independent 60-digit Gaussian quadratures matched erfc-mode formulas at 14 (mode,h) combinations to <1e-48, roots 10.6795421075101613, 1.4898325714354649, 36.8209600939775341, λ2(4)=-0.24543633935038777; these are corroborative numerical tests, not root certificates or infinite-time proof.

## originality

PASS

Full relevant primary texts on Cayley matrix distributions, stochastic SO(n) schemes and manifold/jet numerical integration were compared with the actual SO(2) Gaussian circle convolution theorem. Established classical Cayley and total-positivity ingredients are credited. Published numerical-SDE correlation sign and planar random-rotation findings concern different recurrences and random matrices and do not imply this all-h second-mode reentrance plus at-most-m zero bound. The exactly matching Resultary hit is the assigned same record, not separate prior art. This is a best-of-knowledge conclusion subject to explicitly identified older specialist-literature priority risks.

## value

PASS

For a basic geometry- and invariant-measure-preserving Brownian time step, the transition eigenvalues determine finite-lag and long-run modewise correlation behavior. The previously unstated exact crossing of the m=2 multiplier positive→negative→positive despite positive heat-semigroup multipliers, together with a sharp global zero-count across all integer harmonics and a rigorous nonnumerical witness, is a natural structural benchmark for invariant-preserving stochastic integration. This is neither a trivial coordinate renaming nor an isolated arbitrary negative numerical sample; it identifies the exact qualitative frontier in a canonical test model.

The dated certificate retains the supplied scientific assessment, sources and limitations.
