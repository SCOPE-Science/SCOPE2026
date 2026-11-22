# Sharp orthogonal-support variance stability of ellipsoids in every dimension

## Finding

Let \(d\ge3\), and let \(K\subset\mathbb R^d\) be any centrally symmetric convex body with the origin in its interior. Denote its Euclidean support function by \(h_K(u)=\max_{x\in K}\langle x,u\rangle\), for \(u\in\mathbb S^{d-1}\). Choose a Haar-uniform orthonormal basis \(U=(u_1,\ldots,u_d)\) and intersect the \(d\) supporting hyperplanes \(\langle x,u_j\rangle=h_K(u_j)\). Their unique common intersection is \(X_U=\sum_j h_K(u_j)u_j\), and its squared distance from the origin is \(S_U=\sum_j h_K(u_j)^2\).

Write \(d\sigma\) for normalized spherical surface measure. Define the least-squares quadratic support defect
\[
\Delta_K^2=\min_{Q=Q^{\mathsf T}\in\mathbb R^{d\times d}}\int_{\mathbb S^{d-1}}\left(h_K(u)^2-u^{\mathsf T}Qu\right)^2\,d\sigma(u).
\]
Then the **two optimal dimension-dependent constants** satisfy
\[
\boxed{\quad
\frac{d(d+6)(d-2)}{(d+1)(d+3)}\,\Delta_K^2
\ \le\ \operatorname{Var}(S_U)\ \le\ 
\frac{d(d+4)}{d+1}\,\Delta_K^2.\quad}
\]
Both constants are attained by smooth strictly convex origin-symmetric nonellipsoids arbitrarily close to the unit ball. The lower equality class consists precisely of squared support functions with spherical-harmonic degrees \(0,2,6\); the upper equality class consists precisely of squared support functions with degrees \(0,2,4\). (As usual, the zero-defect ellipsoids attain both equalities.) In particular, \(\operatorname{Var}(S_U)=0\) holds **if and only if** \(K\) is a centered ellipsoid. In dimension \(3\) the sharp coefficients are \(9/8\) and \(21/4\).

## Assumptions and scope

The result is for all integers \(d\ge3\) and all compact centrally symmetric full-dimensional convex bodies centered at the origin, without smoothness assumptions. The random ordered basis has Haar law on the orthogonal group. Variance is with respect to this law; all spherical norms use probability-normalized area measure. \(\Delta_K\) measures distance of the *squared* support function to the finite-dimensional vector space of arbitrary real quadratic forms, not automatically to the cone of positive definite forms. When \(\Delta_K=0\), positivity of \(h_K\) makes the resulting quadratic form positive definite. For bodies sufficiently close to a ball in the squared-support \(L^2\) topology, the least-squares quadratic form is positive definite, and the bounds directly quantify least-squares distance to ellipsoid squared-support functions.

## Proof

**Step 1 (frame reduction and projection).** Put \(f=h_K^2\). By central symmetry \(f(-u)=f(u)\), and \(f\in L^2(\mathbb S^{d-1})\). Every real quadratic function restricted to the sphere belongs exactly to \(\mathcal H_0\oplus\mathcal H_2\), where \(\mathcal H_{\ell}\) denotes the degree-\(\ell\) real spherical harmonics. The unique orthogonal projection of \(f\) onto this subspace is \(u^{\mathsf T}Q_*u\), with
\[
Q_*={d(d+2)\over2}\int f(u)uu^{\mathsf T}\,d\sigma(u)-{d\over2}\left(\int f\,d\sigma\right)I.
\]
Indeed, \(\int u_iu_ju_ku_l\,d\sigma=(\delta_{ij}\delta_{kl}+\delta_{ik}\delta_{jl}+\delta_{il}\delta_{jk})/[d(d+2)]\); the normal equations therefore give \(Q_*\) and the orthogonal projection. Consequently \(\Delta_K^2=\sum_{m\ge2}\|f_{2m}\|_2^2\), where \(f_{2m}\) is the degree-\(2m\) projection.

**Step 2 (orthogonal-frame spectral identity).** For independent first and second columns \(u,v\) of a Haar orthogonal frame, conditioning on \(u\) makes \(v\) uniform on the great subsphere orthogonal to \(u\). The orthogonal-equatorial averaging operator \(Tg(u)=\mathbb E[g(v)\mid u]\) is self-adjoint and rotation-equivariant. The spherical-harmonic addition theorem (equivalently, the normalized zonal Gegenbauer formula) gives \(T|_{\mathcal H_{\ell}}=p_{d,\ell}(0)\,I\). In even degree \(\ell=2m\),
\[
p_{d,2m}(0)=(-1)^m\prod_{j=1}^{m}{2j-1\over d+2j-3}.
\]
Writing \(S_U=\sum_{j=1}^d f(u_j)\), invariance and the preceding conditional identity give the exact nonnegative Parseval sum
\[
\operatorname{Var}(S_U)=\sum_{m\ge1}d\bigl[1+(d-1)p_{d,2m}(0)\bigr]\|f_{2m}\|_2^2.
\]
The mean is \(d\int f\,d\sigma\); all mixed harmonic degrees vanish by orthogonality. Degree \(2\) has \(p_{d,2}(0)=-1/(d-1)\), hence its coefficient vanishes exactly.

**Step 3 (optimal universal constants).** For all \(d>2\), the magnitudes \(a_m=|p_{d,2m}(0)|\) strictly decrease with \(m\), because \(a_{m+1}/a_m=(2m+1)/(d+2m-1)<1\). Among \(m\ge2\), the largest positive coefficient occurs at \(m=2\), where \(p_{d,4}(0)=3/[(d-1)(d+1)]\); the smallest negative coefficient occurs at \(m=3\), where \(p_{d,6}(0)=-15/[(d-1)(d+1)(d+3)]\). Thus the largest multiplier is \(d(d+4)/(d+1)\), and the least positive multiplier is \(d(d+6)(d-2)/[(d+1)(d+3)]\). Substituting these extrema into the Parseval sum proves both inequalities and the exact equality harmonic subspaces.

**Step 4 (strict convexity and geometric rigidity).** Fix a real nonzero degree-\(4\) or degree-\(6\) spherical harmonic \(Y\). For sufficiently small nonzero real \(\varepsilon\), the even positive function \(h_\varepsilon(u)=\sqrt{1+\varepsilon Y(u)}\) obeys \(\nabla_{\mathbb S}^2h_\varepsilon+h_\varepsilon I>0\) pointwise: at \(\varepsilon=0\) it is exactly \(I\), and the sphere is compact. It is therefore the support function of a smooth strictly convex centrally symmetric body. Its squared support function has only degrees \(0,4\) or \(0,6\), attaining the respective sharp constant exactly, and is not quadratic. Finally, \(\operatorname{Var}(S_U)=0\) forces all harmonic degrees above two to vanish; then \(f(u)=u^{\mathsf T}Qu\). Since \(h_K(u)>0\) for all unit \(u\), \(Q\) is positive definite. The support function is exactly that of the centered ellipsoid \(\{x:x^{\mathsf T}Q^{-1}x\le1\}\). Conversely such an ellipsoid has \(S_U=\operatorname{tr}Q\) identically.

## Verification

The included `verify.py` checks the rational three-dimensional spherical moment identities for degrees \(2,4,6,8,10,12\), the exact degree-\(4\)/degree-\(6\) orthogonality, and seeded uniform-sphere numerical diagnostics. It independently obtains \(\operatorname{Var}(\sum_{i=1}^3P_4(Z_i))=7/12\) and \(\operatorname{Var}(\sum_{i=1}^3P_6(Z_i))=9/104\). The dimension-uniform inequalities follow analytically from the displayed Gegenbauer product and its strictly decreasing absolute ratios; finite tests are not substituted for this proof.

## Relationship to prior work

The director-circle/orthogonal-tangent construction for ellipses and classical support-function geometry motivate the observable. Gleason's theorem and its later real-frame formulations establish the zero-variance rigidity in dimension at least three, by characterizing exactly constant orthonormal-basis sums as quadratic forms. The quantitative claim here is the **sharp, all-dimensional two-sided Haar variance inequality**, including its exact degree-\(6\)/degree-\(4\) equality spectra and convex-body sharpness. These conclusions are not claimed as implications of the classical director-circle formula alone. The proof makes the known harmonic diagonalization explicit; priority for quantitative refinements remains subject to further literature review.

## Limitations

The comparison is for squared support functions, not direct Hausdorff distance, and does not supply a global Hausdorff stability estimate. It requires exact Haar sampling of complete orthogonal frames and central symmetry; non-even support functions can have additional harmonic modes. The projection quadratic form need not be positive definite for arbitrary far-from-spherical bodies. Classical zero-variance rigidity is not asserted to be new. No independent mathematical audit has been performed.

## References

1. R. Cooke, M. Keane, W. Moran, *An elementary proof of Gleason's theorem*, Proceedings of the Cambridge Philosophical Society 98 (1985), 117–128. Open text: https://rogermcooke.net/rogermcooke_files/Elementary%20Proof%20of%20Gleasons%20Theorem.pdf
2. V. Moretti, D. Pastorello, *Generalized Complex Spherical Harmonics, Frame Functions, and Gleason Theorem*, arXiv:1205.4504 (first posted 2012-05-21), https://arxiv.org/html/1205.4504v2 . The complex-setting paper is used as background for the harmonic frame-function method, not as an asserted result about real convex bodies.
3. Classical spherical-harmonic addition theorem, equatorial (Funk) transform, and Gegenbauer evaluation; the exact identities needed are derived and normalized in the proof above.
