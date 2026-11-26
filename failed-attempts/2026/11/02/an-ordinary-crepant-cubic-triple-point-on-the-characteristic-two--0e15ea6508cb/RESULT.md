# An ordinary crepant cubic triple point on the characteristic-two Barth–Nieto quintic

## Finding
Let \(k=\overline{\mathbb F}_2\). Write \(\sigma_i\) for the elementary symmetric form of degree \(i\) in six variables. Consider the coefficientwise integral-model reduction
\[
N=\{\sigma_1(X_0,\ldots,X_5)=\sigma_5(X_0,\ldots,X_5)=0\}\subset \mathbb P_k^5.
\]
Then \(N\) is a geometrically integral, normal projective threefold with trivial dualizing sheaf. Its **reduced geometric singular support** is exactly the union of the \(20\) coordinate lines
\[
L_I=\{X_i=0\ (i\in I),\ \sigma_1=0\},\qquad I\subset\{0,\ldots,5\},\ |I|=3,
\]
and the isolated point \(P=[1:1:1:1:1:1]\), which lies on none of these lines.

The isolated point is an **ordinary triple point**. With \(u=(u_0,u_1,u_2,u_3)\) as local affine coordinates at \(P\), its exact defining equation is
\[
Q_3(u)+Q_5(u)=0,\quad
Q_3(u)=\sum_{0\le i<j\le3}u_i u_j(u_i+u_j),\quad
Q_5(u)=u_0u_1u_2u_3(u_0+u_1+u_2+u_3).
\]
Its projectivized tangent cone \(E=V(Q_3)\subset\mathbb P^3_{\mathbb F_2}\) is a smooth cubic surface. Blowing up \(P\) resolves the threefold near its exceptional divisor \(E\), and the blowup has **discrepancy zero** along \(E\). The ambient singular lines elsewhere are not resolved by this assertion.

There is a natural, permutation-equivariant identification of \(E\) with the base of the characteristic-two Segre cubic cone
\[
S=\{\sum_{i=0}^5 X_i=0,\ \sum_{i=0}^5X_i^3=0\}\subset\mathbb P^5.
\]
This identification is a geometric relationship between two coefficientwise reductions, **not** an identification of their entire threefolds or a characteristic-two Hessian construction. In characteristic two the actual Hessian matrix of the Segre cubic vanishes.

For reproducibility, the tangent cubic has \(15\) points over \(\mathbb F_2\), \(45\) points over \(\mathbb F_4\), and \(27\) geometric lines: \(15\) defined over \(\mathbb F_2\) and six Frobenius-conjugate pairs over \(\mathbb F_4\). These familiar cubic-surface arithmetic facts support the identification and are **not claimed independently new**. Likewise, \(\#N(\mathbb F_2)=31\), with \(16\) singular and \(15\) nonsingular rational points.

## Assumptions and scope
The object is specifically the scheme cut out by the two displayed **integer-coefficient symmetric equations reduced modulo two**; it is not asserted to equal a characteristic-two Hessian scheme. All singular-support, normality, and tangent-cone statements are geometric over the algebraic closure of \(\mathbb F_2\). The local crepant blowup concerns only a neighborhood of the isolated point \(P\), not a global resolution of \(N\). The listed rational counts concern the indicated model over \(\mathbb F_2\).

## Proof
**1. Singularity support.** Let \(F=\sigma_5\) on the hyperplane \(\sigma_1=0\). On the dense torus where every coordinate is nonzero, one has
\[
F=(\prod_{i=0}^5X_i)\sum_{i=0}^5X_i^{-1}.
\]
At a point of \(N\) on this torus, the six partial derivatives of \(F\) equal \(-\prod_jX_j/X_i^2\). Singularity in the smooth hyperplane \(\sigma_1=0\) means these six derivatives are equal. Since the square map on a characteristic-two field is injective, all coordinates are equal. Thus there is precisely one torus singular point, \(P\), and it satisfies both equations because \(6=0\) in the field.

If exactly one coordinate is zero, \(\sigma_5\ne0\), so the point is not in \(N\). If exactly two are zero, the two derivatives with respect to the zero coordinates are each the nonzero product of the remaining four coordinates, whereas all other derivatives vanish. Therefore this point of \(N\) is smooth, because the gradient vector is not constant. If at least three coordinates vanish, \(F\) and all its partial derivatives vanish. The projective hyperplane condition then gives precisely the union of the \(20\) distinct coordinate lines \(L_I\), including their intersections. This describes **all geometric points** of the reduced singular support, not merely the rational points.

**2. Geometric irreducibility and normality.** The hypersurface \(N\subset\mathbb P^4\) has a smooth point (take, for example, \([0:0:1:1:1:1]\)); hence its defining quintic is not a pure repeated factor. If its quintic split into two positive-degree factors over \(k\), their projective hypersurfaces in \(\mathbb P^4\) would meet in dimension at least two, and the entire intersection would be singular. A nontrivial repeated factor would likewise create a singular component of dimension three. Both contradict the singular support dimension one. Consequently \(N\) is geometrically integral. A projective hypersurface is Cohen–Macaulay, and the singular locus of \(N\) has codimension two, so \(N\) satisfies Serre's \(R_1\) and \(S_2\) and is normal. Adjunction gives \(\omega_N\simeq\mathcal O_N\), since \(N\) has degree five in \(\mathbb P^4\).

**3. Exact local cubic and its smoothness.** On \(X_5=1\) near \(P\), write \(X_i=1+v_i\) for \(0\le i\le4\), with \(v_5=0\) and \(v_4=v_0+v_1+v_2+v_3\) by \(\sigma_1=0\). Set \(u_i=v_i\) for \(0\le i\le3\). Direct expansion of elementary symmetric forms in characteristic two gives
\[
\sigma_5(1+v_0,\ldots,1+v_5)=\sigma_3(v_0,\ldots,v_5)+\sigma_5(v_0,\ldots,v_5)=Q_3(u)+Q_5(u).
\]
The cubic identity follows by expanding \(\sigma_3(u_0,u_1,u_2,u_3,\sum u_i,0)\). The exact symbolic certificate in the package checks both polynomial equalities modulo two.

For each \(i\), the cubic partial derivative is
\[
\frac{\partial Q_3}{\partial u_i}=\Bigl(\sum_{j\ne i}u_j\Bigr)^2.
\]
All four partial derivatives vanish only when every \(u_i\) equals \(U=\sum_ju_j\). Then \(U=4U=0\), so \(u=0\). There is therefore no nonzero common zero of the gradient over \(k\), proving that the projective cubic surface \(E=V(Q_3)\subset\mathbb P^3_k\) is smooth. The multiplicity of \(P\) is exactly three and its tangent cone is smooth: \(P\) is an ordinary triple point.

**4. One crepant local blowup.** Blowing up the origin in the local affine four-space, on each chart write \(u=t(1,w_1,w_2,w_3)\) after renumbering. The strict transform has equation
\[
Q_3(1,w)+t^2Q_5(1,w)=0.
\]
Along \(t=0\), smoothness of \(E\) makes at least one derivative in the chart coordinates \(w_j\) nonzero. Thus the strict transform is smooth near the entire exceptional divisor. The blowup is an isomorphism away from \(P\), so this gives a resolution of this isolated germ. Blowing up the origin in smooth four-space has canonical coefficient three on the exceptional divisor; the strict transform of a hypersurface of multiplicity three subtracts three under adjunction. Its discrepancy for the threefold is therefore \(3-3=0\). The exceptional divisor is the smooth cubic \(E\), not a union of exceptional curves.

**5. The Segre-cone identification.** Let \(V=\{(X_i)\in k^6:\sum X_i=0\}\), and let \(e=(1,1,1,1,1,1)\in V\). Diagonal translation along \(e\) preserves \(\sum X_i^3\) because the binomial expansion in characteristic two, together with \(\sum X_i=\sum X_i^2=0\), eliminates all translation-dependent terms. Writing \(X_i=1+v_i\) near \([e]\), Newton's identity yields \(\sum_i v_i^3=\sigma_3(v)=Q_3(u)\). Hence the Segre cubic is the projective cone with vertex \([e]\) over \(V(Q_3)\subset\mathbb P(V/ke)\), which is the same \(E\) arising as the quintic's exceptional divisor. These constructions are functorial under permutations of the six original coordinates, so the identification respects that action.

**6. Finite-field checks.** The package implements field arithmetic \(\mathbb F_4=\mathbb F_2[\alpha]/(\alpha^2+\alpha+1)\). It enumerates all \(85\) projective \(\mathbb F_4\)-points of \(\mathbb P^3\), finding \(45\) on \(E\). It enumerates every one of the \(357\) projective \(\mathbb F_4\)-lines in \(\mathbb P^3\) and finds \(27\) entirely contained in \(E\), of which \(15\) are Frobenius-stable and \(12\) form six pairs. These are exhaustive finite statements; the global geometric singular classification and smoothness were established algebraically above. A separate exhaustive enumeration confirms \(31\) points of \(N(\mathbb F_2)\), with \(16\) singular.

## Verification
Run `python nieto_char2_verify.py` using Python 3 and SymPy. The script executes symbolic identities with coefficients reduced modulo two, the gradient criterion, exhaustive line and point enumeration over \(\mathbb F_4\), and a complete \(\mathbb F_2\)-census for the quintic. The recorded successful output in `nieto_char2_verifier_output.txt` terminates in `VERIFY_OK`. The algebraic proof, not the finite enumeration, establishes the assertions over \(k\). The script has no external network dependencies.

## Relationship to prior work
Barth and Nieto's original quintic and its classical twenty coordinate lines and ten Segre nodes are established. Hulek–Spandaw–van Geemen–van Straten (2001) explicitly use the symmetric equation \(\sigma_1=\sigma_5=0\), discuss these classical singularities and restrict their good-reduction analysis to primes at least five. The characteristic-two exceptional isolated triple point and its crepant cubic blowup are not implied by their characteristic-zero statements. Hulek–Nieto–Sankaran's 1997 preprint concerns the original quintic; its available abstract does not address this characteristic-two local degeneration.

The geometry of the characteristic-two Segre cubic cone and the line arithmetic of its smooth Clebsch cubic base are already known, as are arithmetic line results for smooth cubics over fields of characteristic two (including Karaoğlu 2021). No novelty is asserted for those independent results. The new, model-specific claim is the identification of that cubic with the **exceptional divisor of the characteristic-two Barth–Nieto quintic's isolated ordinary crepant triple point**, together with the complete global singular-support statement and explicit local resolution. Dolgachev's treatment of characteristic-two Kummer-type geometry explains why the classical Hessian relation does not survive literally in characteristic two: the actual cubic Hessian vanishes.

## Limitations
This result gives the **reduced support** of the singular locus, not the scheme-theoretic embedded structure of the full Jacobian ideal along the twenty lines. The one-point blowup resolves only the isolated germ near \(P\); no projective crepant resolution of the entire threefold is constructed. The \(\mathbb F_2\) point census is not a complete zeta function for the quintic. The cubic surface point/line invariants are not new. Some historical sources, including the original 1994 Barth–Nieto article and the complete 1997 preprint, were not available for full-text comparison, leaving a specific priority uncertainty.

## References
1. K. Hulek, I. Nieto, G. K. Sankaran, *Heisenberg-invariant Kummer surfaces*, arXiv:alg-geom/9712025 (first public 1997-12-19), https://arxiv.org/abs/alg-geom/9712025.
2. K. Hulek, J. Spandaw, B. van Geemen, D. van Straten, *The modularity of the Barth–Nieto quintic and its relatives*, Adv. Geom. 1 (2001), 263–289, arXiv:math/0010049, https://arxiv.org/abs/math/0010049; DOI 10.1515/advg.2001.017.
3. F. Karaoğlu, *Non-Singular Cubic Surfaces over* \(\mathbb F_{2^k}\), Turkish J. Math. 45 (2021), 2492–2510, DOI 10.3906/mat-2102-10, https://journals.tubitak.gov.tr/math/vol45/iss6/11/.
4. I. Dolgachev, *K3 surfaces of Kummer type in characteristic two*, 2024, https://arxiv.org/abs/2302.13101.
5. S. McKean, *Rational lines on smooth cubic surfaces*, arXiv:2101.08217 (2021), https://arxiv.org/abs/2101.08217.
