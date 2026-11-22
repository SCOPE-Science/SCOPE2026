# Certified endpoint-noise amplification in a 21-node Fourier-extension correction

## Finding
For the **21-point, 21-frequency, sixfold Fourier-extension configuration** used in Liu–Zhao–Gong (2026), the smallest-left-singular-vector endpoint recovery map amplifies worst-case Euclidean perturbations of the other 20 observations by a factor \(\mathcal A\) satisfying the rigorously certified bounds
\[
  280000<\mathcal A<290000.
\]
The same sharp operator gain applies to **either endpoint**. Independent zero-mean observation errors of common variance \(\sigma^2\) therefore create an exact endpoint prediction variance \(\mathcal A^2\sigma^2\), more than \(7.84\times10^{10}\sigma^2\), about the noise-free predicted endpoint. The numerical estimate \(\mathcal A\approx283164.108758673\) is illustrative, not the certified interval's basis.

## Assumptions and scope
Let \(L=120\), \(m=21\), and \(p\in\{0,20\}\). Form the complex square Fourier-extension sampling matrix \(F\in\mathbb C^{21\times21}\), with row indices \(j=0,\ldots,20\), frequency indices \(k=-10,\ldots,10\), and entries
\[
F_{jk}=L^{-1/2}\exp\!\left(\frac{2\pi i jk}{L}\right).
\]
Let \(u\) be any unit left singular vector corresponding to the *smallest* singular value of \(F\). Given observed values \(y_j\) for \(j\ne p\), define the singular-mode endpoint predictor
\[
\widehat y_p=-\frac{1}{\overline{u_p}}\sum_{j\ne p}\overline{u_j}\,y_j.
\]
This statement concerns this specified linear endpoint prediction subprocedure; the error of the subsequently integrated full quadrature rule is not asserted. The exact operator gain \(\mathcal A\) is from input \(\ell^2\) to scalar absolute value. Any independent errors assumed in the variance conclusion are independent of the noiseless data and have the stated common variance.

## Proof
The Gram matrix \(H=FF^*\) is real symmetric Toeplitz, since the frequencies are symmetric, with
\[
H_{ij}=\frac{1+2\sum_{k=1}^{10}\cos(k(i-j)\pi/60)}{120},\qquad0\le i,j\le20.
\]
The smallest eigenvector of \(H\) is exactly the required smallest left singular vector. Reflection \(j\mapsto20-j\) commutes with \(H\), and the verified unique smallest eigenspace has equal endpoint magnitudes. The predictor's coefficient row is \((-\overline{u_j}/\overline{u_p})_{j\ne p}\). By equality in Cauchy–Schwarz, its exact operator norm is
\[
\mathcal A=\frac{\sqrt{\sum_{j\ne p}|u_j|^2}}{|u_p|}=\sqrt{\frac{1}{|u_p|^2}-1}.
\]
For independent centered equal-variance errors, the cross-covariances vanish, so the prediction variance is exactly the squared norm times \(\sigma^2\).

To certify the strict numerical interval rather than infer it from a floating-point eigensolver, the accompanying \(\texttt{verify\_endpoint.py}\) constructs an exact rational approximation \(H_0\) to \(H\) by the Machin arctangent identity and alternating cosine Taylor sums, then rounding entries to 75 decimal places. Explicit truncation estimates give the spectral enclosure \(\|H-H_0\|_2<10^{-70}\). An embedded 21-coordinate rational approximate eigenvector \(w\) has the certified properties
\[
0<\frac{w^TH_0w}{w^Tw}<10^{-38},\qquad
\|H_0w-\mu w\|_2<10^{-52},
\]
where \(\mu=(w^TH_0w)/(w^Tw)\). The verifier checks the exact rational positivity of
\[
 H_0-(10^{-35}+10^{-70})I+10^{-25}ww^T.
\]
Its 21 leading principal minors are strictly positive, certified using integer fraction-free elimination. Hence, by the min–max principle on the subspace perpendicular to \(w\), the *second* eigenvalue of the true \(H\) exceeds \(10^{-35}\). The smallest eigenvalue is below \(2\times10^{-38}\) by its Rayleigh quotient; so it is simple. The spectral residual and gap bound the angle of \(w/\|w\|_2\) from its unit smallest eigenvector by \(10^{-15}\). The rational endpoint entries additionally satisfy the conservative strict comparisons implemented in the verifier, yielding
\[
\frac1{290000}<|u_0|=|u_{20}|<\frac1{280001}.
\]
Applying the exact operator-norm formula proves \(280000<\mathcal A<290000\), with ample slack at the interval endpoints.

## Verification
Run \(\texttt{python3 verify\_endpoint.py}\) using only the Python standard library. The program checks the rational Taylor and angle enclosures, integer Bareiss positivity pivots, rational Rayleigh and residual bounds, and both endpoint inequalities. Successful execution prints three `PASS` statements. The script is a finite, reproducible *exact-rational certificate* for the fixed 21-dimensional assertion, not an experiment extrapolated to arbitrary mesh sizes. The approximate spectral values are not needed to validate the claim.

## Relationship to prior work
Liu, Zhao and Gong (2026), Section 3 and its endpoint reconstruction formula, propose the singular-mode endpoint prediction and demonstrate accuracy for selected smooth data; their paper does not provide this specified observation-noise gain. Barnett (2022) proves exponential conditioning bounds for contiguous discrete Fourier submatrices, but singular-value conditioning by itself does not imply a particular singular-vector *endpoint coordinate* or the amplification of the stated 20-to-one predictor. Dirckx, Huybrechs and Ongenae (2022) analyze periodic-discrete-prolate eigenvectors and stable computation for Fourier submatrices; their general eigenvector machinery provides background, but no exact interval for the endpoint predictor in this 21-point configuration was found in the inspected paper. The present bound uses the method's published configuration, not an arbitrary numerical slice.

## Limitations
This is a sharp-scale, rigorously bracketed *fixed-configuration* result, not an exact closed form for the amplification and not a parameter-uniform theorem. The bound concerns added input errors to the singular-mode endpoint predictor, not the bias for noiseless smooth functions, the full corrected quadrature's eventual integration error, or implementation roundoff effects. SVD truncation used for the integration fit and the untruncated smallest-mode endpoint prediction are distinct operations. Singular-vector phase does not affect the gain. Independent external audit has not been performed.

## References
1. X. Liu, Z. Zhao, B. Gong, *High-precision quadrature via local Fourier extension: analytic integration, uniform sampling, and correction for piecewise smooth integrands* (first posted 2026-03-15), https://arxiv.org/abs/2603.14421.
2. A. H. Barnett, *How exponentially ill-conditioned are contiguous submatrices of the Fourier matrix?* (2022), https://arxiv.org/abs/2004.09643.
3. S. Dirckx, D. Huybrechs, R. Ongenae, *On the computation of the SVD of Fourier submatrices* (2022), https://arxiv.org/abs/2208.12583.
