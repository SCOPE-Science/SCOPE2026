# A beta-shrinkage law for Haar-orthogonalized diagonal probes

## Finding

Let \(n\geq3\), \(1\leq k\leq n\), and let \(A\in\mathbb R^{n\times n}\) be fixed (symmetry is not required). Draw an \(n\)-by-\(k\) matrix of independent standard Gaussians, orthonormalize its columns to a matrix \(Q\), and put \(P=QQ^{\mathsf T}\). For every coordinate \(i\), estimate its diagonal entry by
\[
\widehat a_i^{\mathrm{orth}}=\frac{(AP)_{ii}}{P_{ii}}.
\]
The denominator is positive almost surely. Write \(h_i^2=\sum_{j\ne i}A_{ij}^2\). If \(h_i=0\), the estimate is exact. If \(h_i>0\) and \(1\leq k<n\), its error obeys the **exact distributional identity**
\[
\boxed{\widehat a_i^{\mathrm{orth}}-A_{ii}\ \overset{d}{=}\ h_i\sqrt{V}\,\frac{Z}{\sqrt{Y}}},
\]
where \(Z\sim N(0,1)\), \(Y\sim\chi_k^2\), and \(V\sim\operatorname{Beta}((n-k)/2,(k-1)/2)\) are mutually independent; at \(k=1\), interpret \(V=1\) deterministically. At \(k=n\), the error is identically zero.

For the usual self-normalized estimator built from \(k\) **independent** Gaussian probes, the error law is \(h_i Z/\sqrt{Y}\). Therefore the orthogonalized estimator has a coordinatewise coupling in which its absolute error is the independent-probe absolute error multiplied by \(\sqrt V\leq1\). For \(2\leq k<n\) and \(h_i>0\), it is strictly better at **every positive absolute-error threshold**:
\[
\Pr(|\widehat a_i^{\mathrm{orth}}-A_{ii}|>t)
<\Pr(|\widehat a_i^{\mathrm{iid}}-A_{ii}|>t),\qquad t>0.
\]
At \(k=1\) the two laws coincide. The coupling is **marginal for a specified coordinate**, not a simultaneous ordering of all coordinates of one draw.

For every real \(0<p<k<n\), all finite positive absolute moments have the exact formula
\[
\mathbb E|\widehat a_i^{\mathrm{orth}}-A_{ii}|^p
=\frac{h_i^p\,\Gamma((p+1)/2)\Gamma((k-p)/2)}{\sqrt\pi\,\Gamma(k/2)}
\frac{\Gamma((n-k+p)/2)\Gamma((n-1)/2)}{\Gamma((n-k)/2)\Gamma((n-1+p)/2)}.
\]
For \(1\leq k<n\) and \(h_i>0\), this absolute moment is infinite whenever \(p\geq k\). In particular, the mean exists and equals \(A_{ii}\) exactly when \(k\geq2\), while at \(k=1\) the error is symmetric Cauchy and has **no Lebesgue expectation**. The mean squared error is finite exactly when \(k\geq3\); for \(3\leq k<n\),
\[
\boxed{\mathbb E(\widehat a_i^{\mathrm{orth}}-A_{ii})^2
=\frac{n-k}{n-1}\,\frac{h_i^2}{k-2}}.
\]
This is exactly \((n-k)/(n-1)\) times the corresponding independent-Gaussian mean squared error. Orthogonalization does not remove the critical small-\(k\) heavy-tail moment obstruction unless \(k=n\).

The high-threshold failure probability has the additional sharp ratio
\[
\lim_{t\to\infty}\frac{\Pr(|\widehat a_i^{\mathrm{orth}}-A_{ii}|>t)}{\Pr(|\widehat a_i^{\mathrm{iid}}-A_{ii}|>t)}
=\frac{\Gamma(n/2)\Gamma((n-1)/2)}{\Gamma((n-k)/2)\Gamma((n+k-1)/2)}
\quad(1\leq k<n,\ h_i>0).
\]

## Assumptions and scope

The real matrix \(A\) is deterministic and square, and \(n\geq3\). The probe matrix \(G\in\mathbb R^{n\times k}\) has iid standard normal entries, \(1\leq k\leq n\), and its reduced QR factor \(Q\) is a Haar-distributed orthonormal \(k\)-frame. Exactly \(k\) matrix-vector evaluations are required to obtain \(AQ\). One can equivalently compute \(AG\) first and obtain \(AQ\) by the invertible triangular change of basis; QR itself has an additional arithmetic cost. For the comparator, use the same query count \(k\) with iid Gaussian \(g_1,\ldots,g_k\) and form
\[
\widehat a_i^{\mathrm{iid}}=
\frac{\sum_{j=1}^{k}(g_j)_i(Ag_j)_i}{\sum_{j=1}^{k}(g_j)_i^2}.
\]
The two estimators are compared **in distribution**, not necessarily when calculated from the same underlying Gaussian matrix. The exact result applies to individual diagonal coordinates and requires neither positivity nor symmetry of \(A\).

## Proof

**1. Haar projection geometry.** Fix a coordinate \(i\) and abbreviate \(B=P_{ii}\). Since \(P\) is an orthogonal projection, \(P^2=P\), and therefore
\[
\sum_{j\ne i}P_{ij}^2=B-B^2.
\]
The Gaussian orthonormalization makes \(P\) a uniform rank-\(k\) projection. Consequently \(B\sim\operatorname{Beta}(k/2,(n-k)/2)\) for \(k<n\). Invariance under all orthogonal transformations that fix the \(i\)-th basis vector implies, conditional on \(B\), that the normalized off-diagonal row is uniform on the sphere in \(\mathbb R^{n-1}\), with a direction independent of \(B\). Rotate this off-diagonal direction so that its first coordinate aligns with the fixed vector \((A_{ij})_{j\ne i}/h_i\). If \(U\) denotes that first spherical coordinate, independent of \(B\), then
\[
\frac{\widehat a_i^{\mathrm{orth}}-A_{ii}}{h_i}
\overset d=\sqrt{\frac{1-B}{B}}\,U.
\]

**2. Independent chi-square representation.** Let independent \(Y\sim\chi_k^2\) and \(D\sim\chi_{n-k}^2\). The beta-gamma construction gives \(B\overset d=Y/(Y+D)\), independent of \(U\). Hence the last error has law \(\sqrt{D/Y}\,U\). To factor the spherical term, independently draw \(Z\sim N(0,1)\) and \(W\sim\chi_{n-2}^2\), put \(R=Z^2+W\), and take \(U=Z/\sqrt R\). Standard Gaussian polar decomposition proves \(R\sim\chi_{n-1}^2\) and \(R\) is independent of \(U\). Independently take \(V\sim\operatorname{Beta}((n-k)/2,(k-1)/2)\), or \(V=1\) if \(k=1\). By beta-gamma multiplication, \(D'=VR\sim\chi_{n-k}^2\). As \(R\) and \(V\) are independent of \(U\), so is \(D'\). Therefore the joint law of \((D',U)\) equals that of \((D,U)\), and
\[
\sqrt{D'/Y}\,U=\sqrt V\,\frac{Z}{\sqrt Y}.
\]
The variables on the right are mutually independent except for the displayed deterministic multiplication, proving the claimed identity. For \(k=n\), \(P=I\) almost surely, proving exactness at the endpoint.

**3. Independent-probe comparison and boundaries.** Conditional on its \(i\)-th Gaussian row, the independent-probe numerator \(\sum_{j\ne i}A_{ij}\sum_{s=1}^{k}(g_s)_i(g_s)_j\) is centered Gaussian of variance \(h_i^2\sum_s(g_s)_i^2\). The row norm squared is \(Y\sim\chi_k^2\), yielding \(\widehat a_i^{\mathrm{iid}}-A_{ii}\overset d=h_i Z/\sqrt Y\). Since \(0\leq V\leq1\), the coupling proves the absolute-tail ordering. For \(1<k<n\), \(0<V<1\) almost surely, while \(|Z|/\sqrt Y\) has a positive continuous density on positive arguments; thus strictness holds for every \(t>0\). For \(k=1\), \(V=1\) gives equality.

**4. Positive moments, exact variance and tails.** For \(0<p<k\), independence and the gamma integral give
\[
\mathbb E|Z|^p=\frac{2^{p/2}\Gamma((p+1)/2)}{\sqrt\pi},\qquad
\mathbb E Y^{-p/2}=\frac{2^{-p/2}\Gamma((k-p)/2)}{\Gamma(k/2)},
\]
\[
\mathbb E V^{p/2}=
\frac{\Gamma((n-k+p)/2)\Gamma((n-1)/2)}{\Gamma((n-k)/2)\Gamma((n-1+p)/2)}.
\]
These establish the full moment formula. Because \(Y\) has density proportional to \(y^{k/2-1}\) near zero and \(V\) has positive probability of being bounded away from zero, the moment diverges when \(p\geq k\). Setting \(p=2\) and using \(\mathbb E V=(n-k)/(n-1)\) and \(\mathbb E Y^{-1}=1/(k-2)\) proves the variance formula when \(k>2\). For \(k=1\), the ratio \(Z/\sqrt Y\) is a standard Cauchy variable: symmetry alone does not create a finite mean. For \(k\geq2\), finite absolute first moment and symmetry give unbiasedness. Finally, \(|Z|/\sqrt Y\) has regularly varying two-sided tail exponent \(k\); conditioning on \(V\) and applying dominated convergence to the bounded tail ratio gives the stated sharp tail constant \(\mathbb E V^{k/2}\).

## Verification

Run `python verify_orth_diag.py` with `numpy` available. The package includes its dependency declaration. It checks the idempotent projection geometry, the exact estimator identity for independently generated matrices, the equality at one probe, the zero-error full-basis endpoint, gamma-moment identities, and observed quantiles against independent beta/chi-square simulations. These finite checks do not substitute for the preceding proof. In particular, they neither establish convergence of tail moments nor certify novelty.

## Relationship to prior work

Baston and Nakatsukasa (2022), Section 5, analyze the self-normalized Gaussian diagonal estimator with independent probes; Hallman, Ipsen and Saibaba (2022), Lemma 21, explicitly identify its Student distribution. Those independent-probe formulas are **prior work**, not claimed here as new. The additional result is the exact **multiplicative beta factor for orthogonalized probes**, with its strict all-threshold comparison and sharp finite-moment and tail constants.

Dharangutte and Musco (2022) obtain concentration for a different iid Hutchinson diagonal estimator. Epperly, Tropp and Webber (2023) develop XDiag through leave-one-out low-rank residual estimates; it is not the direct normalized \((AP)_{ii}/P_{ii}\) estimator. Published studies of Haar Stiefel moments for stochastic subspace descent concern other loss functionals. The standard beta-gamma and uniform-sphere distributional identities used in the proof are classical; no claim of inventing these identities is made.

## Limitations

This is an **exact marginal statement for any fixed coordinate**. It does not imply joint stochastic ordering, simultaneous maximum-coordinate error improvement, improved wall-clock cost, or a better full-matrix error in every realization. QR and triangular solves may add work and can be numerically unstable without appropriate implementation. The comparison uses exact arithmetic, real Gaussian probes, a common query count, and self-normalized estimators; it need not apply to Rademacher or unnormalized probes, other sketch laws, adaptive sampling, or noisy matrix-vector products. Classical Haar-projector ratio formulas could provide an equivalent interpretation, so mathematical priority beyond the inspected sources is not independently certified.

## References

1. R. A. Baston and Y. Nakatsukasa, *Stochastic diagonal estimation: probabilistic bounds and an improved algorithm*, arXiv:2201.10684, first posted 2022-01-26. https://arxiv.org/abs/2201.10684
2. E. Hallman, I. C. F. Ipsen and A. K. Saibaba, *Monte Carlo Methods for Estimating the Diagonal of a Real Symmetric Matrix*, arXiv:2202.02887, first posted 2022-02-06. https://arxiv.org/abs/2202.02887
3. P. Dharangutte and C. Musco, *A Tight Analysis of Hutchinson's Diagonal Estimator*, arXiv:2208.03268, first posted 2022-08-05. https://arxiv.org/abs/2208.03268
4. E. N. Epperly, J. A. Tropp and R. J. Webber, *XTrace: Making the Most of Every Sample in Stochastic Trace Estimation*, arXiv:2301.07825, first posted 2023-01-19. https://arxiv.org/abs/2301.07825
