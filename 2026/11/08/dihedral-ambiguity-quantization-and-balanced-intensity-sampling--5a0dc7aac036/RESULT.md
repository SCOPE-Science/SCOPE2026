# Dihedral ambiguity quantization and balanced intensity sampling on two crossing circles

## Finding
Let \(C_1,C_2\subset\mathbb C\) be two distinct Euclidean circles with exactly two intersection points \(a\ne b\). Let \(\theta\in(0,\pi)\) be an angle between their tangent lines at either intersection, and let \(\mathcal P_d\) denote polynomials of degree at most \(d\) with complex coefficients, for integer \(d\ge1\). Define \(q\) to be the denominator in lowest terms of \(\theta/\pi\), setting \(q=\infty\) when it is irrational. Then full intensity data \(|p|^2\) on \(C_1\cup C_2\) determine **every** \(p\in\mathcal P_d\), up to one constant unimodular factor, if and only if \(d<q\).

More precisely, choose a unit complex number \(\eta\) so that \(w(z)=\eta(z-a)/(z-b)\) sends \(C_1\) to the extended real line. Its image of \(C_2\) is a line of angle \(\pm\theta\). For nonzero polynomials \(p,v\) with equal magnitudes on both circles, the reduced rational quotient \(R=v/p\) is constant unimodular when \(q=\infty\). For finite \(q\), every nonconstant quotient has the form
\[
R(z)=H\bigl(w(z)^q\bigr),\qquad
H(s)=\xi\prod_{j=1}^{m}\frac{s-\alpha_j}{s-\overline{\alpha_j}},
\]
where \(m\ge1\), \(|\xi|=1\), and the nonreal numbers \(\alpha_j\) are listed with multiplicity, with no cancellation. Its rational-map degree is exactly \(qm\). Conversely, every such reduced quotient is realized by two polynomials of degree at most \(qm\) having equal magnitudes on the two circles. Thus the possible positive degrees of a nonconstant ambiguity quotient are exactly the positive multiples of \(q\).

Independently of the angle, the real vector space spanned by restrictions of all profiles \(|p|^2\), \(p\in\mathcal P_d\), has dimension exactly \(4d\). Every such profile can therefore be reconstructed linearly from \(4d\) suitable point intensities, and fewer measurements cannot recover *all profiles by a real-linear map*. In fact, choose exactly \(2d\) distinct nonintersection points on each circle. Parametrize \(C_j\) by \(z=c_j+r_j e^{it}\), write their chosen angles \(t_{j,1},\ldots,t_{j,2d}\), and define
\[
 h_j(t)=\prod_{\ell=1}^{2d}\sin\!\left(\frac{t-t_{j,\ell}}2\right).
\]
When writing \(h_j(a)\) or \(h_j(b)\), evaluate at the corresponding angular coordinate on \(C_j\). This balanced \(4d\)-point design recovers the entire intensity profile **if and only if**
\[
\boxed{h_1(a)h_2(b)-h_1(b)h_2(a)\ne0.}
\]
The inequality holds for an open dense full-measure set of balanced point configurations. For \(d<q\) these same intensity measurements also recover every polynomial up to global phase; when \(d\ge q\), no amount of intensity sampling on these two circles removes all polynomial ambiguities.

## Assumptions and scope
All circles have positive radius and meet transversely at exactly two distinct points; neither tangential nor disjoint circles are included in the angle-dependent statement. Measurements are noise-free magnitudes or squared magnitudes of the same polynomial at points of the indicated circles. The degree bound \(d\) is known, and the curves and sample locations are known. The rational-map degree of a reduced quotient is the larger of the degrees of its coprime numerator and denominator. A linear intensity-profile reconstruction reconstructs the restriction of the full Hermitian quadratic lift, not necessarily its entire coefficient matrix, and is distinct from minimum-sample nonlinear phase retrieval.

## Proof
**1. Two reflections and quantized quotient degree.** The Möbius function \(w(z)=\eta(z-a)/(z-b)\) sends both circles through \(a,b\) to straight lines through zero in the Riemann sphere; take their angles to be \(0\) and \(\theta\). Set \(\mathcal R(w)=R(z(w))\). Equality of moduli implies \(|\mathcal R(w)|=1\) on both lines wherever defined. The rational identity theorem and Schwarz reflection yield
\[
\mathcal R(w)\,\overline{\mathcal R(\overline w)}=1,
\qquad
\mathcal R(w)\,\overline{\mathcal R(e^{2i\theta}\overline w)}=1.
\]
Therefore \(\mathcal R(e^{2i\theta}w)=\mathcal R(w)\) identically. If \(\theta/\pi\) is irrational, a nonconstant rational map cannot be invariant under this infinite rotation group (its nonzero Laurent coefficients at zero would all have to vanish), so \(R\) is constant of modulus one. If \(\theta/\pi=u/q\) in lowest terms, \(e^{2i\theta}\) is a primitive \(q\)-th root of unity. The invariant rational subfield of \(\mathbb C(w)\) is \(\mathbb C(w^q)\), hence \(\mathcal R(w)=H(w^q)\). Since \(w^q\) is real on both lines, \(H\) has unit modulus on a real interval and hence on its entire real locus away from poles. Comparing \(H(s)\) with \(1/\overline{H(\overline s)}\), factoring rational zeros and poles, and taking the limit along real infinity gives exactly the all-pass product displayed above. In particular \(\deg(R)=\deg(H\circ w^q)=q\deg(H)=qm\). Cancellation of a common polynomial factor from \(v,p\) shows \(qm\le\max\{\deg(v),\deg(p)\}\le d\).

Conversely, write \(H=U/V\) using the two degree-\(m\) numerator and denominator products in the displayed formula. Clearing \((z-b)^{qm}\) in \(U(w(z)^q)\) and \(V(w(z)^q)\) yields polynomial representatives of degree at most \(qm\). Their ratio is \(H(w^q)\), unimodular on both circles, so their intensities agree. The case \(m=1\), e.g. \(H(s)=(s-i)/(s+i)\), proves sharp failure starting at degree \(q\); every \(m\ge1\) proves the attainable degree spectrum. When the quotient is constant, equality of magnitude forces its constant to be unimodular.

**2. Exact real dimension of the intensity-profile space.** Let \(\mathcal H_d\) be the real vector space of Hermitian bivariate polynomials
\[
F(z,\overline z)=\sum_{j,k=0}^d H_{jk}z^j\overline z^{\,k},\qquad H_{jk}=\overline{H_{kj}},
\]
with real dimension \((d+1)^2\). Rank-one Hermitian matrices linearly span all Hermitian matrices, so the real span of \(|p|^2\) is the restriction image of \(\mathcal H_d\). A circle with center \(c_j\) and radius \(r_j>0\) has irreducible complexified equation
\[
 L_j(z,w)=(z-c_j)(w-\overline{c_j})-r_j^2=0.
\]
If a polynomial \(F(z,w)\) vanishes at every \((z,\overline z)\) on that circle, the rational substitution \(w=\overline{c_j}+r_j^2/(z-c_j)\) makes it identically zero; the irreducibility of \(L_j\) implies \(L_j\mid F\). For two different circles \(L_1,L_2\) are coprime, hence their product divides every \(F\) vanishing on both. The product has bidegree \((2,2)\); because its leading bidegree coefficient is nonzero, the quotient has bidegree at most \((d-2,d-2)\). The quotient is Hermitian because \(F,L_1,L_2\) are. The kernel thus has real dimension \((d-1)^2\) when \(d\ge2\), and zero when \(d=1\). Hence the image dimension is \((d+1)^2-(d-1)^2=4d\), including \(d=1\).

**3. The matching-traces model.** On a circle, restrictions of \(\mathcal H_d\) are exactly all real trigonometric polynomials of degree at most \(d\), a real \((2d+1)\)-dimensional space \(\mathcal T_d(C_j)\): the restriction cannot have higher harmonics, and the Hermitian polynomials \(2\operatorname{Re}((z-c_j)^k)\), \(2\operatorname{Im}((z-c_j)^k)\) and \(1\) provide a basis. A pair of traces arising from one global profile must agree at the two crossings \(a,b\). These impose two independent real conditions on \(\mathcal T_d(C_1)\oplus\mathcal T_d(C_2)\), giving a space of dimension \(2(2d+1)-2=4d\). The actual restriction image has that dimension by Step 2, so **every** pair of trigonometric traces agreeing at \(a,b\) arises from an element of \(\mathcal H_d\).

**4. Balanced sample criterion and genericity.** A nonzero real trigonometric polynomial of degree \(d\) has at most \(2d\) distinct zeros modulo \(2\pi\). For \(2d\) distinct prescribed angles its one-dimensional vanishing space is spanned by the explicit \(h_j\) above, which is real, \(2\pi\)-periodic and has degree \(d\). Consequently a pair of traces vanishing at all balanced sampling sites is exactly \((A h_1,B h_2)\) for real \(A,B\). It arises from a global profile if and only if
\[
A h_1(a)=B h_2(a),\qquad A h_1(b)=B h_2(b).
\]
There is a nonzero such pair if and only if the boxed determinant vanishes. This proves the exact criterion and linear recovery statement. Each of its four displayed factor values is nonzero because the crossings are omitted from the \(2d\) chosen zeros. As any one sampling angle varies, \(h_1(a)/h_1(b)\) changes nontrivially (the sine-ratio for two distinct crossing angles is nonconstant). Thus the determinant is a nonzero real-analytic function on the configuration space, with a measure-zero zero set and open dense nonvanishing set. Finally, dimension \(4d\) rules out fewer real-linear intensity evaluations for reconstructing every trace.

## Verification
The accompanying `verify.py` checks the exact polynomial identity \(|z^2-1|^2-4|z|^2=0\) on both circles \(|z-1|=\sqrt2\) and \(|z+1|=\sqrt2\), giving an explicit degree-two ambiguity at angle \(\pi/2\). It also verifies symbolically an eight-sample full-rank and an eight-sample rank-deficient design for \(d=2\), and tests balanced designs at additional degrees and crossing angles. Exact rank checks are certificates only for those finite examples; Steps 1–4 provide the all-degree proof. Reproduce with `python verify.py` using Python, SymPy and NumPy.

## Relationship to prior work
Chalendar and Partington (first arXiv version March 24, 2024, arXiv:2403.16255, Theorem 2.16) classify when two full circles yield uniqueness for general holomorphic functions and exhibit counterexamples for rational intersection angle. They do **not** state the bounded-degree denominator threshold, the all-pass parametrization of *all rational ambiguity quotients*, the divisibility quantization of their degrees, or the balanced finite-sample determinant. Their irrational-angle uniqueness is retained as prior work, not claimed new. Bodmann and Hammen (arXiv:1302.5487, Section 2, especially Theorem 2.3) construct a \(4d\)-intensity polynomial-recovery design using two crossing circles of irrational angle with \(2d+1\) sites on one and \(2d-1\) new sites on the other; the number \(4d\) and the existence of some two-circle designs are therefore not new. The present statement instead characterizes arbitrary balanced \(2d+2d\) configurations exactly and separates polynomial uniqueness from the lifting rank at rational crossings. Pérez (arXiv:2009.02061, Theorem 2.1) gives irrational-angle holomorphic uniqueness. Przybyłek and Siedlecki (arXiv:1907.09371, Section 4) treat phaseless polynomial interpolation from unrestricted complex point evaluations rather than two prescribed crossing circles. All statements here are mathematical conclusions, not claims of absolute historical priority.

## Limitations
The determinant criterion concerns injectivity of the linear *intensity-profile* evaluation map, not the minimal number of nonlinear phase-retrieval measurements. At rational crossings with \(d\ge q\), complete intensity data do not yield polynomial uniqueness even if every profile value is known. The result does not give uniform conditioning/noise robustness, classify tangential or disjoint circles, or extend the quotient-degree statement to arbitrary nonrational analytic curves. Historical priority beyond the identified sources has not been independently certified.

## References
1. I. Chalendar and J. R. Partington, *Phase retrieval on circles and lines*, arXiv:2403.16255 (first posted 2024-03-24), especially Theorem 2.16. https://arxiv.org/abs/2403.16255
2. B. G. Bodmann and N. Hammen, *Stable phase retrieval with low-redundancy frames*, arXiv:1302.5487 (first posted 2013-02-22), especially Theorem 2.3. https://arxiv.org/abs/1302.5487
3. R. Pérez III, *A Note on the Phase Retrieval of Holomorphic Functions*, arXiv:2009.02061 (first posted 2020-09-04), Theorem 2.1. https://arxiv.org/abs/2009.02061
4. M. R. Przybyłek and P. Siedlecki, *A note on the complexity of a phaseless polynomial interpolation*, arXiv:1907.09371 (first posted 2019-07-22), Section 4. https://arxiv.org/abs/1907.09371
