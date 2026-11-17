# Sharp arbitrary-order blindness and phase recovery for relative normal angles of convex ovals

## Finding

Fix coprime integers \(2\le p<q\), positive amplitudes \(a,b\) satisfying \(a+b<1\), and a phase \(\phi\) modulo \(2\pi\). Define a planar convex body by the support function
\[
h_\phi(\theta)=1-\frac{a}{p^2-1}\cos(p\theta)-\frac{b}{q^2-1}\cos(q\theta+\phi).
\]
At \(m\) independent arclength-uniform boundary points, measure the oriented outward unit-normal angles \(\Theta_1,\ldots,\Theta_m\). Discard the common absolute direction but retain the complete ordered vector
\[
D_m=(\Theta_2-\Theta_1,\ldots,\Theta_m-\Theta_1)\pmod{2\pi}.
\]
**Theorem.** For all integers \(m<p+q\), the entire joint probability law of \(D_m\) is independent of \(\phi\). For \(m=p+q\), the measurable rotation-invariant Fourier coefficient
\[
W_{p,q}:=\mathbb E\exp\!\left(i p\sum_{j=1}^{q}\Theta_j-i q\sum_{j=q+1}^{p+q}\Theta_j\right)
=\left(\frac a2\right)^q\left(\frac b2\right)^p e^{ip\phi}
\]
first detects that phase. When the family frequencies \(p,q\) are specified, the full \(D_{p+q}\)-law identifies \(a,b\) and the body up to rotation and translation.

For any prescribed finite sample-order bound \(M\), choose \(p=2\), any odd \(q>\max\{3,M-2\}\), and two phases \(\phi_0=0\), \(\phi_1=\pi/2\). These yield *noncongruent real-analytic strictly positively curved ovals*, even modulo reflections, for which the complete relative normal-angle laws agree for every \(1\le m\le M\). They also have identical perimeter, area, and directional width in the same angular reference frame:
\[
P=2\pi,\qquad
A=\pi\left(1-\frac{a^2}{6}-\frac{b^2}{2(q^2-1)}\right),\qquad
w(\theta)=2-\frac{2a}{3}\cos(2\theta).
\]
Thus no universally bounded order of exact relative-normal correlation laws identifies all smooth positively curved planar bodies, even with these geometric side observables. The first separating order is exactly \(q+2\) for this pair.

## Assumptions and scope

All angles live on \(\mathbb R/2\pi\mathbb Z\). The integers \(p,q\) are coprime and at least two; the strictly positive amplitudes satisfy \(a+b<1\). Samples are independent and uniform in **Euclidean arclength** on the same body, and each batch's *oriented* normal directions are registered only relative to its first direction. The data consist of the **whole exact joint law** of the relative normal-angle vector, not a finite empirical sample, histogram or an unoriented-angle statistic. The pair construction fixes \(p=2\) and odd \(q\ge5\). Normal directions are not measured in a shared absolute frame; that different observation model is reconstructible by the classical surface-area measure correspondence.

## Proof

**1. Every Fourier density defines a genuine convex oval.** Differentiating twice gives
\[
\rho_\phi=h_\phi+h_\phi''=1+a\cos(p\theta)+b\cos(q\theta+\phi)\ge1-a-b>0.
\]
The standard support parametrization \(x(\theta)=h_\phi(\theta)n(\theta)+h_\phi'(\theta)t(\theta)\), with \(n=(\cos\theta,\sin\theta)\), \(t=(-\sin\theta,\cos\theta)\), obeys \(x'(\theta)=\rho_\phi(\theta)t(\theta)\). Positivity yields an embedded strictly convex real-analytic closed oval whose outer normal angle is \(\theta\); translation adds only first harmonics to \(h\). Consequently \(ds=\rho_\phi\,d\theta\) and \(P=\int\rho_\phi\,d\theta=2\pi\).

**2. Relative-angle law and its exact Fourier support.** The individual normal angle has density \(\rho_\phi/(2\pi)\). Write \(c_k=\mathbb E e^{ik\Theta}\), so the only nonzero coefficients are
\[
c_0=1,\qquad c_{\pm p}=a/2,\qquad c_q=(b/2)e^{-i\phi},\qquad c_{-q}=(b/2)e^{i\phi}.
\]
For arbitrary integers \(k_1,\ldots,k_m\) with \(\sum_j k_j=0\), the corresponding rotation-invariant moment factors by independence as \(\prod_jc_{k_j}\). Moreover every Fourier coefficient of the law of \(D_m\) is such a product: the coefficient with indices \(\ell_2,\ldots,\ell_m\) equals the product with \(k_1=-\sum_{j=2}^m\ell_j\), \(k_j=\ell_j\) for \(j\ge2\). Thus the entire relative law is controlled by zero-sum tuples from \(\{0,\pm p,\pm q\}\).

Let \(r_p\) be the number of \(+p\) entries minus the number of \(-p\) entries, and likewise \(r_q\). The zero-sum equation \(p r_p+q r_q=0\) and coprimality imply \(r_p=qj\), \(r_q=-pj\) for an integer \(j\). If \(j\ne0\), the tuple contains at least \(q|j|+p|j|\ge p+q\) nonzero entries. Therefore for \(m<p+q\), necessarily \(r_q=0\); its Fourier product contains as many \(e^{i\phi}\) factors as \(e^{-i\phi}\) factors and is phase independent. Uniqueness of Fourier coefficients for probability measures on a compact torus proves equality of the **whole probability laws**, not merely finitely many moments.

**3. Sharpness and identification at the threshold.** At \(m=p+q\), use exactly \(q\) frequencies \(+p\) and \(p\) frequencies \(-q\). Their sum is zero, and their product is the stated \(W_{p,q}\); this is a Fourier coefficient of the observed difference law because the common-rotation exponent sum vanishes. For \(m=2\), the coefficients at \(p\) and \(q\) of the one relative-angle distribution are respectively \(a^2/4\), \(b^2/4\), so positive \(a,b\) are known. The nonzero threshold coefficient then yields \(e^{ip\phi}\).

To check this is the exact congruence class in the fixed family, rotate the oval by \(\delta\). Preserving the positive real \(p\)-mode coefficient requires \(p\delta\equiv0\pmod{2\pi}\). Such rotations shift the \(q\)-mode phase by multiples of \(2\pi q/p\), and since \(\gcd(p,q)=1\), precisely the shifts \(2\pi j/p\) occur. Hence \(e^{ip\phi}\) identifies the member modulo rigid rotations and translations. Reflections conjugate this invariant, so \(\phi=0\) and \(\phi=\pi/p\) are inequivalent even under reflection (their invariants are \(+1\) and \(-1\)).

**4. Geometric side data and arbitrary-order obstruction.** By orthogonality and \(A=\frac12\int h_\phi\rho_\phi\,d\theta\),
\[
A=\pi\left(1-\frac{a^2}{2(p^2-1)}-\frac{b^2}{2(q^2-1)}\right),
\]
independent of \(\phi\). With \(p=2\), \(q\) odd, the two antipodal support values cancel the odd \(q\)-harmonic, giving \(w_\phi(\theta)=h_\phi(\theta)+h_\phi(\theta+\pi)=2-(2a/3)\cos2\theta\), independent of phase even as a function of the same absolute direction. For every fixed \(M\), choose an odd \(q>\max\{3,M-2\}\). Since \(p+q=M\) is excluded, all orders up to \(M\) agree for the two noncongruent ovals, while the threshold moment at \(q+2\) separates them. This proves the claimed arbitrary blindness order.

## Verification

The standalone Python file `normal_angle_tomography_checks.py` uses exact integer dynamic programming over Fourier modes to check zero-sum phase cancellation below the threshold and the first nonzero phase exponents at the threshold, for several coprime frequency pairs. Independently, Fourier quadrature on a dense deterministic angular grid checks \(h+h''>0\), perimeter, area, width, and the first separating moment. Execute `python normal_angle_tomography_checks.py` with Python 3 and NumPy. The expected output is `CONVEX_NORMAL_PHASE_THRESHOLD_CHECKS_OK`. These finite tests corroborate but are not used as a substitute for the unrestricted integer argument above.

## Relationship to prior work

The Gauss–Minkowski surface-area measure correspondence in Marckert and Renault (2012) provides the geometric correspondence between normal-angle laws and convex plane bodies, with a Fourier area identity and a convolution construction. Their two-point Fourier convolution does not give the new exact arbitrary-order indistinguishability and first separating order. The work of Abdallah and Mérigot (2014) reconstructs bodies from *absolutely directed* random normal vectors; the common-rotation-quotiented batch data here are weaker and are not covered by that theorem. Kakarala (2009) proves bispectral completeness when all Fourier coefficients are nonsingular, or when their nonzero support is representation-product closed. The sparse support \(\{0,\pm p,\pm q\}\) in this finding meets neither hypothesis: the Fourier coefficients outside that set vanish, while the set is not addition closed. The 2D covariogram inverse theorem concerns physical-point difference laws or Fourier intensity of an indicator, not difference laws of independent outer-normal directions.

The Fourier phase obstruction is an application of classical sparse frequency resonance, but the conversion to an explicit family of noncongruent **strictly convex** shapes with the complete sharp observation-order cutoff and equal width, perimeter and area is the claimed contribution. No theorem of priority or independence from all possible earlier publications is claimed.

## Limitations

The theorem is exact for its two-harmonic real-analytic family and specifically the described relative-orientation observation model. It does not limit reconstruction from a single global absolute normal frame, from sampled boundary coordinates or distances, or from unboundedly many measurements in one batch. It gives no noisy or finite-sample identification rate and no smallest possible order uniformly over a restricted smoothness/curvature-frequency class. The observational density is arclength-induced, not uniform in the angular parameter unless the curve is circular. Published results beyond the inspected sources may contain equivalent resonance statements; this historical risk remains.

## References

1. R. Kakarala, *The bispectrum as a source of phase-sensitive invariants for Fourier descriptors: a group-theoretic approach* (first publicly posted 2009-02-02), arXiv:0902.0196, https://arxiv.org/abs/0902.0196, §§1, 3, Theorems 4–5.
2. J.-F. Marckert and D. Renault, *Compact convex sets of the plane and probability theory* (first publicly posted 2012-08-27), arXiv:1208.5408, https://arxiv.org/abs/1208.5408, §§2.2, 2.4, 3.2–3.3.
3. H. Abdallah and Q. Mérigot, *On the reconstruction of convex sets from random normal measurements* (first publicly posted 2014-02-20), arXiv:1402.5010, https://arxiv.org/abs/1402.5010, §§1, 3–4.
4. G. Bianchi, R. J. Gardner and M. Kiderlen, *Phase retrieval for characteristic functions of convex bodies and reconstruction from covariograms* (first publicly posted 2010-03-23), arXiv:1003.4486, https://arxiv.org/abs/1003.4486.
