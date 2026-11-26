# Independent mathematical audit

## correctness

PASS

After m+1 updates all coordinates are in [−1,1]; the window maximum M obeys M_(n+m+1)≤sin M_n and hence tends to zero. For positive histories the window minimum a satisfies a_(n+1)≥sin a_n. The scalar sine iterates have inverse-square increments tending to 1/3, giving upper and lower bounds of order n^(−1/2) by the two comparisons. Dividing the companion characteristic equation by λ^(m+1) rules out |λ|>1; equality on the circle and w0>0 force λ=1, simple since P′(1)=W. Independently of the stable-fiber assertion, one can track the polynomial return f(t)=t+At³+Bt⁵ directly: for the lag map T let Φ(t)=(t,f⁻¹(t),…,f⁻ᵐ(t)). The displayed inverse-iterate jets give TΦ(t)−Φ(f(t))=O(t⁷) when W A=−1/6 and W B=3(μ+ν)A²/2+μA/2+1/120. For the actual state X_n subtract Φ(z_n), obtaining a transverse error E_n with newest coordinate zero. The derivative of the error map in E at zero is the companion map followed by projection along the unit eigenvector onto this hyperplane; it represents the stable quotient. In an adapted norm it is contracting, and remains so locally. Therefore ||E_(n+1)||≤ρ||E_n||+O(n^(−7/2)), with ρ<1, and geometric convolution gives E_n=O(n^(−7/2)). Thus z_(n+1)=f(z_n)+O(n^(−7/2)), inducing only O(n^(−2)) error in the reciprocal-square increment. First summation gives z_n^(−2)=n/(3W)+O(log n); the error after subtracting 1/(3W)+K/n from its increment is O(log n/n²). This proves a finite constant, not merely a bounded remainder. Algebra gives K=3W(3A²−2B). The bound ν≤mμ gives a strictly positive numerator through m=3 (discriminant already negative at m=3); at m=4 the lower bound is (3μ−2)² and equality requires endpoint support and μ=2/3. The two μ=1 examples give −1/20 and 11/80 as stated. The checker was inspected, not run. The fine expansion is not for general sign-changing histories. In the motivating map the active m=2 case of the theorem additionally requires −γ>0 and β1>0, as already required by its endpoint hypotheses.

## originality

PASS

The inverse-square parabolic clock and summation to a finite constant are not new in general. The supported advance is the dependence on both lag moments throughout the nonnegative finite-memory family, and the resulting sharp sign and cancellation thresholds. The closest inspected sinusoidal flip record yields the very same algebraic coefficient after sign alternation in a signed two-lag specialization outside this domain; it does not give the arbitrary nonnegative kernels or the horizon threshold. The same-day comparisons do not establish precedence.

## value

PASS

The leading rate alone cannot distinguish kernels with the same mean lag, while the exact second asymptotic coefficient does and can even have opposite signs for the same mean. The lag-four cancellation and first attainable negative sign at lag five are sharp structural facts across the kernel family, not just observations of a selected trajectory. No claim about mixed-sign clocks, noisy delays, or uniformity across approaching stability boundaries is needed for this value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
