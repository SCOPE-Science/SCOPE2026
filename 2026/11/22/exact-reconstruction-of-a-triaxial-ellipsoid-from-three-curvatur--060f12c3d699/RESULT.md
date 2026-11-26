# Exact reconstruction of a triaxial ellipsoid from three curvature-histogram statistics

## Finding

Let \(E\subset\mathbb R^3\) be the smooth ellipsoid with unknown, strictly ordered semiaxes \(a>b>c>0\). Choose \(X\) uniformly in **Euclidean surface area** on \(\partial E\), and observe its positive Gaussian curvature \(K=K(X)\). The probability law of \(K\) has a complete one-dimensional quadrature density, exactly two finite nonzero endpoint-density limits, and exactly one logarithmic interior singularity. The two support endpoints and the ratio of these two limiting densities uniquely recover **all three semiaxes**, without supplying the total surface area or the interior singularity's location.

Write
\[
\lambda_1=a^{-2}<\lambda_2=b^{-2}<\lambda_3=c^{-2},\qquad
C=\lambda_1\lambda_2\lambda_3,
\quad Q(u)=\sum_{j=1}^3\lambda_j u_j^2,
\quad Z=\int_{\mathbb S^2}\sqrt{Q(u)}\,d\sigma(u).
\]
Let \(\ell(\phi)=\lambda_1\cos^2\phi+\lambda_2\sin^2\phi\), where \(d\sigma\) denotes ordinary unnormalized area measure on the unit sphere. The exact curvature-density formula is
\[
\begin{split}
f_K(k)&=\frac{q(k)^{3/2}}{2kZ}\int_{\{\phi\in[0,2\pi):\ell(\phi)<q(k)\}}
\frac{d\phi}
{\sqrt{(\lambda_3-\ell(\phi))(q(k)-\ell(\phi))}},\\
q(k)&=\sqrt{C/k},\qquad k_-<k<k_+,
\end{split}
\]
with sharp support endpoints and the interior critical value
\[
k_-={C\over\lambda_3^2}={c^2\over a^2b^2},\quad
k_s={C\over\lambda_2^2}={b^2\over a^2c^2},\quad
k_+={C\over\lambda_1^2}={a^2\over b^2c^2}.
\]
The limits \(d_-=\lim_{k\downarrow k_-} f_K(k)\) and \(d_+=\lim_{k\uparrow k_+}f_K(k)\) satisfy
\[
\begin{split}
d_-&={\pi\lambda_3^{3/2}\over Zk_-\sqrt{(\lambda_3-\lambda_1)(\lambda_3-\lambda_2)}},\\
d_+&={\pi\lambda_1^{3/2}\over Zk_+\sqrt{(\lambda_2-\lambda_1)(\lambda_3-\lambda_1)}}.
\end{split}
\]
At the unique interior critical value the density diverges, on both sides, as
\[
f_K(k)=\frac{\lambda_2^{3/2}}{Zk_s\sqrt{(\lambda_2-\lambda_1)(\lambda_3-\lambda_2)}}
\log\frac{k_s}{|k-k_s|}+O_{a,b,c}(1)\qquad(k\to k_s).
\]
The density is real analytic on each of the two open intervals separated by \(k_s\).

**Explicit inverse from three histogram statistics.** Define the observables
\[
r=\sqrt{k_+/k_-}>1,\qquad m=\sqrt{k_-k_+}>0,\qquad
T={1\over r^7}\left({d_-\over d_+}\right)^2>0.
\]
Then the semiaxes are recovered *uniquely* by
\[
\boxed{\lambda_2=m,\qquad
\lambda_1=m\frac{1+T}{1+rT},\qquad
\lambda_3=rm\frac{1+T}{1+rT},\qquad
(a,b,c)=(\lambda_1^{-1/2},\lambda_2^{-1/2},\lambda_3^{-1/2}).}
\]
The support endpoints alone determine the middle semiaxis \(b=m^{-1/2}\) and the ratio \(a/c=\sqrt r\). They leave one free parameter: any \(\lambda_1\in(m/r,m)\), with \(\lambda_3=r\lambda_1\), gives the same endpoints. The density ratio resolves that freedom and determines the largest and smallest semiaxes individually.

## Assumptions and scope

The ellipsoid is three-dimensional, centered, nondegenerate, strictly triaxial and sampled from normalized induced Euclidean surface area. Curvature uses the ordinary positive Gaussian curvature (the product of the two principal curvatures). Densities refer to ordinary Lebesgue measure in the curvature variable \(k\); the support endpoint density limits are taken **from within the support**. The inverse is stated only for strictly ordered semiaxes and exact probability data. No curvature-noise model is assumed.

## Proof

**Step 1 — curvature and area density.** Let \(A=\operatorname{diag}(a,b,c)\) and parameterize \(X=Au\), \(u\in\mathbb S^2\). The surface Jacobian of this linear map is \(\det A\,\lVert A^{-T}u\rVert=abc\sqrt{Q(u)}\). Thus the sampling law of \(u\) has density \(\sqrt{Q(u)}/Z\) relative to \(d\sigma\), and the actual surface area of the ellipsoid is \(abcZ\). For \(F(x)=x^T\operatorname{diag}(\lambda_1,\lambda_2,\lambda_3)x-1\), the restriction of the second fundamental form to the tangent plane and the adjugate determinant identity give
\[
K(Au)={\det\operatorname{diag}(\lambda_1,\lambda_2,\lambda_3)
\;(Au)^T\operatorname{diag}(\lambda_1,\lambda_2,\lambda_3)(Au)
\over\bigl|\operatorname{diag}(\lambda_1,\lambda_2,\lambda_3)Au\bigr|^4}
={C\over Q(u)^2}.
\]
This also follows from the classical ellipsoid curvature formula in [1].

**Step 2 — exact density.** Use coordinates \(u=(\sqrt{1-z^2}\cos\phi,\sqrt{1-z^2}\sin\phi,z)\), with \(-1<z<1\), \(0<\phi<2\pi\), and spherical area element \(d\sigma=dzd\phi\). Then \(Q=\ell(\phi)+(\lambda_3-\ell(\phi))z^2\). For a fixed \(\phi\), transforming the two roots \(z=\pm\sqrt{(q-\ell)/(\lambda_3-\ell)}\) gives the unnormalized density \(1/\sqrt{(\lambda_3-\ell)(q-\ell)}\) for \(Q\) on \(\ell<q<\lambda_3\). Multiplication by the surface-area weight \(\sqrt q/Z\), and the monotone change \(k=C/q^2\) whose derivative has magnitude \(q/(2k)\), proves the stated formula. Strict inequalities \(\lambda_1<\lambda_2<\lambda_3\) imply the support and exclude point atoms.

**Step 3 — endpoint limits.** Near each of the two sphere poles \(u=\pm e_1\), the exact quadratic expression in tangent coordinates is \(Q=\lambda_1+(\lambda_2-\lambda_1)s^2+(\lambda_3-\lambda_1)t^2\), with smooth positive area density \(\sqrt{\lambda_1}/Z+O(s^2+t^2)\). The planar quadratic-sublevel-area derivative at zero equals \(\pi/\sqrt{(\lambda_2-\lambda_1)(\lambda_3-\lambda_1)}\) **per pole**. Taking both poles, then applying \(|dq/dk|=q/(2k)\), yields \(d_+\). The two poles \(\pm e_3\) give \(d_-\) analogously. In both cases higher local Taylor terms vanish in the density limit.

**Step 4 — interior saddle and analyticity.** The only critical points of \(Q\) on the sphere are \(\pm e_i\). At \(\pm e_2\), tangent coordinates \((s,t)\) satisfy the exact relation
\[
Q-\lambda_2=-(\lambda_2-\lambda_1)s^2+(\lambda_3-\lambda_2)t^2.
\]
For \(A_0,B_0>0\), the local pushforward of area under \(-A_0s^2+B_0t^2\), with unit density at the origin, has density \((A_0B_0)^{-1/2}\log(1/|q-\lambda_2|)+O(1)\) **per saddle**. Indeed the scaled coordinates \(\xi=\sqrt{B_0}t+\sqrt{A_0}s\) and \(\eta=\sqrt{B_0}t-\sqrt{A_0}s\) give \(Q-\lambda_2=\xi\eta\) and Jacobian \(ds\,dt=d\xi\,d\eta/(2\sqrt{A_0B_0})\). Integrating over \(|\xi|,|\eta|<\delta\) gives \(2\log(\delta^2/|q-\lambda_2|)\) before this Jacobian factor. Smooth weight errors are bounded after integration, since after substitution \(\eta=(q-\lambda_2)/\xi\) the error is \(O(|\xi|+|q-\lambda_2|/|\xi|)\) times the coarea factor \(1/|\xi|\). Multiplying by the weight \(\sqrt{\lambda_2}/Z\), by the two poles, and by \(\lambda_2/(2k_s)\) gives the displayed logarithmic coefficient. Away from critical values the quadrature is analytic: for \(q>\lambda_2\) the angular range is fixed and both denominator factors are bounded from zero locally in \(q\); for \(q<\lambda_2\), use symmetry to restrict to one quadrant and put \(\sin\phi=\sqrt{(q-\lambda_1)/(\lambda_2-\lambda_1)}\sin\theta\). This fixes the range at \([0,\pi/2]\), cancels the square root that vanishes at the moving endpoint, and leaves only denominators bounded away from zero locally in \(q\). There are no other interior singularities.

**Step 5 — inverse uniqueness.** From the endpoint locations,
\[
\sqrt{k_-k_+}=\lambda_2,\qquad \sqrt{k_+/k_-}=\lambda_3/\lambda_1=r.
\]
Dividing the two endpoint-density formulas cancels \(Z\) and yields
\[
{d_-\over d_+}=\left({\lambda_3\over\lambda_1}\right)^{7/2}
\sqrt{{\lambda_2-\lambda_1\over\lambda_3-\lambda_2}}.
\]
Hence \(T=(\lambda_2-\lambda_1)/(\lambda_3-\lambda_2)\); solve the linear equation \(m-\lambda_1=T(r\lambda_1-m)\). This gives precisely the inverse in the finding. Positivity of \(m,T\) and \(r>1\) ensures strict ordering \(\lambda_1<m<\lambda_3\); each recovered spectrum determines exactly one ordered positive semiaxis triple.

## Verification

The standalone file `check_curvature.py` implements the one-dimensional exact density, numerical checks using tangent-vector cross products, Sobol spherical integration, normalization/CDF comparisons, the Gauss–Bonnet identity for the mean of the Gaussian curvature, endpoint-density limits, saddle diagnostics and algebraic inversion. The accompanying verification record reports 124 deterministic assertions over four strictly triaxial test cases. These computations test the constants and normalization only; the infinite-domain statements are established by Steps 1–5 rather than by sampling. Reproduce by running `python check_curvature.py` with NumPy and SciPy installed.

As a concrete case, for \((a,b,c)=(3,2,1)\), the support endpoints are \(1/36\) and \(9/4\), the interior singularity is at \(4/9\), and the inversion returns exactly \((3,2,1)\) from the endpoint and density data.

## Relationship to prior work

Poelaert, Schniewind and Janssens [1] derive the ellipsoid's Gaussian curvature and its surface-area element. Hillier [2] studies the density of a **uniform-sphere quadratic form** and its nonanalyticity at matrix eigenvalues (building on earlier work). Combining those ingredients explains why the present area-uniform curvature density is a reweighted quadratic-form pushforward; **the unweighted quadratic-form density and curvature formula themselves are not asserted to be new**. The finding is the explicit three-statistic inverse from the curvature histogram's two support endpoints and ratio of endpoint densities, together with its exact surface-area-weighted density and geometric saddle coefficient. Ellipsoid reconstruction results using section half-diameters or projected aspect ratios use different forward observables and do not supply this specific inverse. See REVIEW.md for comparative limitations.

## Limitations

The proof excludes repeated semiaxes; their coalescing-eigenvalue limits require separate analysis. Exact recovery from three statistics does not imply statistical stability under finite noisy sampling. The one-dimensional density follows from standard quadratic-form transformations, and the literature may contain equivalent endpoint identities. The numerical tests do not substitute for the proof.

## References

[1] D. Poelaert, J. Schniewind, F. Janssens, *Surface Area and Curvature of the general Ellipsoid*, arXiv:1104.5145, first posted 2011-04-27. https://arxiv.org/abs/1104.5145

[2] G. Hillier, *The Density of a Quadratic Form in a Vector Uniformly Distributed on the n-Sphere*, Southampton Discussion Paper 9902 (revised July 1999); *Econometric Theory* 17 (2001), doi:10.1017/S026646660117101X. https://eprints.soton.ac.uk/33137/1/9902.pdf
