# Quartic near-circular section tails and a sharp two-statistic ambiguity for triaxial ellipsoids

## Finding

Let \(E\subset\mathbb R^3\) be the ellipsoid
\[
E=\{x:\alpha x_1^2+\beta x_2^2+\gamma x_3^2\leq1\},\qquad 0<\alpha<\beta<\gamma.
\]
Choose the plane \(n^\perp\) through the origin with its unit normal \(n\) uniformly distributed on \(S^2\). Let \(e(n)\in[0,1)\) be the ordinary eccentricity of its elliptical section, namely \(e(n)^2=1-b(n)^2/a(n)^2\), where \(a(n)\ge b(n)>0\) are the section's semiaxes. Put \(F_E(\varepsilon)=\mathbb P\{e(n)\leq\varepsilon\}\).

**Quartic law.** For every fixed triaxial ellipsoid,
\[
\boxed{F_E(\varepsilon)=C_E\varepsilon^4+o_E(\varepsilon^4),\qquad C_E=\frac{\beta^2}{4(\beta-\alpha)(\gamma-\beta)}.}
\]
Thus the exponent and its coefficient are exact, without fitting or choosing a numerical angular cutoff.

**Sharp constraint and inverse ambiguity.** Write \(M_E=\max_n e(n)^2\). Then
\[
\boxed{M_E=1-\frac\alpha\gamma,\qquad C_E\geq\frac{1-M_E}{M_E^2}.}
\]
Equality in the second inequality holds exactly when
\[
\beta=\frac{2\alpha\gamma}{\alpha+\gamma},
\]
equivalently the squared middle semiaxis equals the arithmetic mean of the squares of the other two semiaxes. At any fixed \(M_E\in(0,1)\), the pair of statistics \((M_E,C_E)\) determines the similarity class of the triaxial ellipsoid either once (at the sharp lower bound) or **exactly twice** (for every larger finite coefficient). The two possibilities are explicitly related by
\[
\boxed{\beta' = \frac{\alpha\gamma\beta}{(\alpha+\gamma)\beta-\alpha\gamma}.}
\]
For example, the inverse-square semiaxis triples \((1,2,4)\) and \((1,4/3,4)\) are non-similar yet both have \((M_E,C_E)=(3/4,1/2)\).

**Biaxial transition.** For spheroids, by contrast, \(F_E(\varepsilon)\) is of exact second order in \(\varepsilon\), not fourth order. When \(\alpha=\beta<\gamma\),
\[
F_E(\varepsilon)\sim \frac{\alpha}{2(\gamma-\alpha)}\varepsilon^2,
\]
and when \(\alpha<\beta=\gamma\),
\[
F_E(\varepsilon)\sim\frac{\beta}{2(\beta-\alpha)}\varepsilon^2.
\]
The complete spheroid distributions are given in the proof as a comparison with established one-spike section laws; novelty is claimed only for the triaxial quartic coefficient and sharp two-statistic inverse classification.

## Assumptions and scope

The normal direction is exactly Haar-uniform on the Euclidean unit sphere. The plane always passes through the ellipsoid's center. Uniformly offset random affine planes, or planes sampled conditionally from stationary line/plane processes, need not have the same angular law. The eigenvalues \(\alpha,\beta,\gamma\) are positive reciprocals of the squared semiaxes, sorted increasingly. Similarity means congruence after a positive common dilation; coordinate permutations have no effect on the statements. The parameter \(\varepsilon\) tends to zero while the ellipsoid remains fixed. No assertion of uniform error bounds as two eigenvalues merge is made.

## Proof

**1. Restricted quadratic forms.** Restrict \(Q=\operatorname{diag}(\alpha,\beta,\gamma)\) to the Euclidean plane \(n^\perp\). If its two eigenvalues are \(0<\lambda_-(n)\leq\lambda_+(n)\), then the semiaxes of the section are \(\lambda_-^{-1/2}\) and \(\lambda_+^{-1/2}\), hence
\[
e(n)^2=1-\frac{\lambda_-(n)}{\lambda_+(n)}=\frac{\lambda_+(n)-\lambda_-(n)}{\lambda_+(n)}.
\]
For any orthonormal basis of \(n^\perp\), let \(B(n)\) be the corresponding symmetric \(2\times2\) matrix. Its eigenvalue gap is
\[
G(n)=\sqrt{\left(B_{11}-B_{22}\right)^2+4 B_{12}^2}.
\]
Thus \(e(n)^2=G(n)/\lambda_+(n)\).

**2. Exactly four circular-section normals.** Set \(d_1=\beta-\alpha\), \(d_2=\gamma-\beta\), and \(d=d_1+d_2\). If a plane has a circular section, the quadratic form \(Q-\beta I=\operatorname{diag}(-d_1,0,d_2)\) vanishes identically on that plane: any isotropic two-plane for this form necessarily has common eigenvalue \(\beta\) by eigenvalue interlacing, or directly by the dimensions of its positive and negative subspaces. The coordinate projection of such a plane to the \((x_1,x_3)\)-plane cannot be surjective (otherwise the indefinite binary form would vanish everywhere); hence it contains the \(x_2\)-axis. Its remaining direction is one of the two null lines \(d_1x_1^2=d_2x_3^2\). Consequently the four unit normals are exactly
\[
n=(\pm\sqrt{d_1/d},\,0,\,\pm\sqrt{d_2/d}),
\]
with independent signs. Their antipodal identification corresponds to two distinct unoriented planes. No other normal has \(e(n)=0\).

**3. First-order circularity jet.** Fix one circular normal \(n_0\), and choose an orthonormal tangent frame \((v_0,e_2)\) there, where \(v_0\) lies in the \((x_1,x_3)\)-plane. Its restricted quadratic form is \(\beta I\) and
\[
|v_0^TQn_0|=\sqrt{d_1d_2}=:h>0.
\]
Use local coordinates
\[
n(s,t)=\frac{n_0+sv_0+te_2}{\sqrt{1+s^2+t^2}}.
\]
Orthonormalize the two tangent vectors to this plane starting from \(v_0-sn_0\) and \(e_2-tn_0\). With \(r=\sqrt{s^2+t^2}\), the resulting restriction matrix satisfies, up to independent signs absorbed by the frame,
\[
B_{11}-B_{22}=-2hs+O(r^2),\qquad B_{12}=-ht+O(r^2),
\]
and \(\lambda_+(n)=\beta+O(r)\). Hence
\[
e(n(s,t))^2=\frac{2h}{\beta}\sqrt{s^2+t^2}+O(r^2).
\]
The displayed linearization has full rank in the two coordinates: there are no further near-circular regions beyond small neighborhoods of the four listed normals.

**4. Spherical area and quartic coefficient.** The event \(e\leq\varepsilon\) has in each circular-normal chart an asymptotically round disk of radius
\[
r_\varepsilon=\frac{\beta}{2h}\varepsilon^2(1+o(1)).
\]
The spherical area density in these coordinates tends to one. Each of the four small patches therefore has area \(\pi r_\varepsilon^2(1+o(1))\). The complement of the four neighborhoods has eccentricity bounded away from zero by compactness. Dividing their combined area by \(4\pi\), we obtain
\[
F_E(\varepsilon)=r_\varepsilon^2(1+o(1))
=\frac{\beta^2}{4d_1d_2}\varepsilon^4+o(\varepsilon^4).
\]
This is a statement about a continuum limit, proved by a local change of variables, not by finite sampling.

**5. Largest eccentricity.** The min–max principle gives \(\lambda_-(n)\geq\alpha\) and \(\lambda_+(n)\leq\gamma\), so \(e(n)^2\leq1-\alpha/\gamma\). Equality holds for the plane spanned by the first and third principal axes (normal \(e_2\)). Thus \(M_E=1-\alpha/\gamma\).

**6. Sharp coefficient inequality and full inverse classification.** A direct factorization is
\[
\frac{\beta^2}{4(\beta-\alpha)(\gamma-\beta)}-
\frac{\alpha\gamma}{(\gamma-\alpha)^2}
=\frac{\bigl(\beta(\alpha+\gamma)-2\alpha\gamma\bigr)^2}
{4(\beta-\alpha)(\gamma-\beta)(\gamma-\alpha)^2}.
\]
Since \(\alpha\gamma/(\gamma-\alpha)^2=(1-M_E)/M_E^2\), the inequality and its unique equality case follow. For the inverse problem scale \(\alpha\) to one and write \(R=\gamma/\alpha=1/(1-M_E)\) and \(t=\beta/\alpha\). Then
\[
C_E=\frac{t^2}{4(t-1)(R-t)},\qquad 1<t<R.
\]
The function diverges at both endpoints and has its unique minimum at \(t=2R/(R+1)\). Therefore each coefficient strictly exceeding the minimum has exactly two preimages. Their explicitly displayed relation
\[
t\longmapsto\frac{Rt}{(R+1)t-R}
\]
is an involution preserving \(C_E\) and exchanging the two branches. Only its fixed point \(t=2R/(R+1)\) produces a single preimage. This proves the complete sharp inverse classification. The middle physical semiaxis squared is \(1/\beta\), and the equality relation becomes \(1/\beta=(1/2)(1/\alpha+1/\gamma)\).

**7. Biaxial comparison.** If \(\alpha=\beta<\gamma\), write \(y=\varepsilon^2\), \(k=(\gamma-\alpha)/\gamma\); the range is \(0\leq y\leq k\), and a uniform normal has uniformly distributed cosine to the distinguished axis. Direct diagonalization of its section gives
\[
\mathbb P\{e^2\leq y\}=1-\sqrt{1-\frac{\alpha y}{(\gamma-\alpha)(1-y)}}.
\]
If \(\alpha<\beta=\gamma\), for \(0\leq y\leq(\beta-\alpha)/\beta\) one instead obtains
\[
\mathbb P\{e^2\leq y\}=1-\sqrt{1-\frac{\beta y}{\beta-\alpha}}.
\]
In each case the CDF is zero below its range and one above its range. Taylor expansion at zero yields the announced quadratic laws. If all three parameters coincide, every section is circular and \(F_E(\varepsilon)=1\) for every \(\varepsilon\geq0\).

## Verification

The standalone file `verify.py` computes section eigenvalue ratios by two independent methods, checks all four optical normals for two strict triaxial examples, validates the rational two-shape ambiguity exactly, evaluates one million uniformly distributed low-discrepancy directions, and checks both exact spheroid CDFs. It reports:

`VERIFY_OK alternative_plane_bases=4500 circular_normals=8 sobol_normals=1048576 exact_ambiguity=1 axisymmetric_CDF_cases=6 quartic_coeff=0.5`

Run with Python 3, NumPy and SciPy: `python verify.py`. The proof of the asymptotic law and exact inverse multiplicity is analytical; these finite tests are diagnostic only.

## Relationship to prior work

Hayes's treatment of circular sections of strain ellipsoids explicitly identifies the two special circular planes, a classical geometric fact reused here. Makarenko–Fletcher–Shukurov (2014) study random cut *filamentarity* distributions and extraction of aspect ratios from whole histograms; Landrø (2015) develops cross-sectional aspect-ratio histograms, using an approximate treatment for general triaxial ellipsoids. Those investigations motivate the statistical question but do not state the exact quartic small-eccentricity law, its coefficient, or the present sharp two-statistic multiplicity classification in the inspected material. A prior exact one-spike ellipsoid random-radius law encompasses related axisymmetric distributions, which are used here for contrast rather than asserted as independent new findings.

The distinction is between full histogram reconstruction, already studied, and the precise loss of information when retaining only a small-eccentricity coefficient and the largest possible eccentricity. No equality of *full* section-eccentricity laws is asserted for the two different triaxial examples.

## Limitations

The quartic coefficient is a fixed-shape asymptotic and diverges as either adjacent inverse-square semiaxis gap tends to zero; it cannot be used uniformly across the spheroidal limit. The experiment uses a central plane with Haar-uniform normal, not a plane sampled from a random offset process. Exact observation of a tail coefficient is an idealized population statistic; statistical sample-complexity and noise stability are not established. Prior-art searching and comparison cannot by themselves certify historical priority or replace independent mathematical review.

## References

- I. Makarenko, A. Fletcher, A. Shukurov, *3D morphology of a random field from its 2D cross-section*, arXiv:1407.4048, initial public version 2014-07-15. https://arxiv.org/abs/1407.4048
- M. Hayes, *Central Circular Sections of the Strain Ellipsoids*, Journal of Elasticity 49 (1998), 285–288. DOI: 10.1023/A:1007454919900.
- M. Landrø, *Aspect ratio histograms of 3D ellipsoids and 2D ellipses: Analytical relations and numerical examples*, Geophysics 80 (2015), D429–D440. DOI: 10.1190/geo2014-0481.1.
