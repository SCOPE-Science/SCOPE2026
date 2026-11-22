# Exact two-shell Fourier energy and a three-valued elliptic-trace cancellation

## Finding

Let \(q\) be any odd prime power, let \(d=2m\ge 2\), and let \(Q\) be any nondegenerate quadratic form on \(\mathbb F_q^d\). Choose distinct \(a,b\in\mathbb F_q^\times\), and put \(S=S_a\cup S_b\), where \(S_c=\{x:Q(x)=c\}\). Write \(\chi\) for the quadratic character, with \(\chi(0)=0\). The following formulas give the complete two-sum convolution, its exact fourth Fourier moment, and an exact mean over the second radius.

Define
\[
\begin{gathered}
\varepsilon=\chi((-1)^m\det Q),\quad L=q^{d-2},\quad B=\varepsilon q^{m-1},\\
U=q^{d-1}-B,\qquad Z=q^{d-1}+(q-1)B,\\
\Delta_{a,b}(t)=(t-a-b)^2-4ab,\\
H_{a,b}(t)=\chi(t(t-4a))+\chi(t(t-4b))+2\chi(\Delta_{a,b}(t)),\\
T_a=\sum_{t\in\mathbb F_q}\chi\bigl(t(t-4a)\Delta_{a,b}(t)\bigr),\qquad
T_b=\sum_{t\in\mathbb F_q}\chi\bigl(t(t-4b)\Delta_{a,b}(t)\bigr).
\end{gathered}
\]
Here \(\det Q\) is the determinant of any symmetric matrix representing \(Q\); its quadratic-character class is basis independent. If \(r(z)=\sum_{x\in\mathbb F_q^d}\mathbf 1_S(x)\mathbf 1_S(z-x)\), then
\[
\boxed{
 r(z)=\begin{cases}
 2U,&z=0,\\
 4L-2B,&z\ne0\text{ and }Q(z)=0,\\
 4L+B H_{a,b}(Q(z)),&Q(z)\ne0.
 \end{cases}}
\]
The (ordered) additive energy, equal to the unnormalized Fourier fourth moment by Plancherel, is
\[
\boxed{\begin{aligned}
\mathcal E(S)&=\sum_{z\in\mathbb F_q^d}r(z)^2
=q^{-d}\sum_{\xi\in\mathbb F_q^d}|\widehat{\mathbf1_S}(\xi)|^4\\
&=4U^2+(Z-1)(4L-2B)^2\\
&\quad+U\left[16(q-1)L^2-48LB+B^2\left(6q-14-6\chi(ab)+4(T_a+T_b)\right)\right].
\end{aligned}}
\]
Here the Fourier transform uses any nontrivial additive character and an arbitrary fixed nondegenerate pairing to identify the dual with \(\mathbb F_q^d\).

For **every** fixed \(a\in\mathbb F_q^\times\), with the sum ranging over all \(b\in\mathbb F_q^\times\setminus\{a\}\), the following cancellation has no growing dependence on the field size and depends on field arithmetic only through \(\chi(-3)\):
\[
\boxed{\sum_{b\ne0,a}T_a(a,b)=\sum_{b\ne0,a}T_b(a,b)=4-q+\chi(-3).}
\]
For every nonsingular quartic in these sums, define the corresponding elliptic Frobenius trace by \(\tau_a=-1-T_a\) and \(\tau_b=-1-T_b\). At the singular ratios, use the same numerical quantities (without assigning them to a smooth elliptic curve). Then
\[
\boxed{\sum_{b\ne0,a}(\tau_a+\tau_b)=-4-2\chi(-3).}
\]
Consequently the **exact average energy** over the \(q-2\) choices of the second nonzero radius is
\[
\boxed{\begin{aligned}
\frac{1}{q-2}\sum_{b\ne0,a}\mathcal E(S_a\cup S_b)
&=4U^2+(Z-1)(4L-2B)^2\\
&\quad+U\left[16(q-1)L^2-48LB+B^2\left(6q-14+\frac{38-8q+8\chi(-3)}{q-2}\right)\right].
\end{aligned}}
\]
This remains valid at \(q=3\), where there is exactly one permissible second radius. The normalized four-step return probability for the uniform walk with increments in \(S\) is \(\mathcal E(S)/(2U)^4\), because \(S=-S\).

## Assumptions and scope

The theorem covers both Witt classes of every nondegenerate form in every even dimension \(d\ge2\), over all odd finite fields including characteristic three and extension fields. The radii are nonzero and distinct; zero-radius or coincident-radius unions are excluded. The two-sum convolution counts ordered pairs. No upper bound on \(q\) or \(d\) is assumed. A smooth genus-one interpretation applies separately to each quartic except at the explicitly listed singular ratios; the exact energy and trace cancellation do **not** require smoothness.

## Proof

**1. Standard quadratic counts.** For an even-dimensional nondegenerate form of dimension \(2m\), the number of vectors on every nonzero level is \(U=q^{2m-1}-\varepsilon q^{m-1}\), while the zero level has \(Z=q^{2m-1}+(q-1)\varepsilon q^{m-1}\) vectors. These follow by additive-character orthogonality and the quadratic Gauss sum. In odd dimension \(2m-1\), the analogous level count is \(q^{2m-2}+\chi((-1)^{m-1}\det R)\chi(s)q^{m-1}\) for a nondegenerate form \(R\) and level \(s\).

**2. Two spheres at a nonisotropic sum.** Fix \(Q(z)=t\ne0\). For \(Q(x)=i\), \(Q(z-x)=j\), the polar identity gives \(2B_Q(z,x)=t+i-j\), where \(B_Q(x,y)=[Q(x+y)-Q(x)-Q(y)]/2\). Thus
\[
x=\frac{t+i-j}{2t}z+y,\quad y\in z^\perp,\qquad Q(y)=-\frac{\Delta_{i,j}(t)}{4t}.
\]
The \((2m-1)\)-dimensional form \(Q|_{z^\perp}\) has determinant class \(\det Q/t\). Substitution into the odd-dimensional level count yields, for all nonzero \(i,j\),
\[
(\mathbf1_{S_i}*\mathbf1_{S_j})(z)=L+B\chi(\Delta_{i,j}(t)).
\]
For \(i=j\) its discriminant is \(t(t-4i)\), proving the nonisotropic case of the convolution formula after summing \((i,j)\in\{a,b\}^2\).

**3. Nonzero isotropic sums and the origin.** When \(z\ne0\) and \(Q(z)=0\), choose a hyperbolic partner and split off its plane. The constraint \(Q(x)=i, Q(z-x)=j\) fixes the coefficient of the partner to \(i-j\). For \(i\ne j\) the remaining \(d-2\) coordinates are free, giving \(L\) solutions. For \(i=j\), the even-dimensional quadratic quotient gives \(L-B\) solutions. These conclusions also hold when \(d=2\): the quotient is zero-dimensional and the isotropic case occurs only in the split plane. Summing gives \(4L-2B\). At \(z=0\), the disjoint symmetric spheres each contribute \(U\) pairs, hence \(r(0)=2U\).

**4. Fourth moment.** Every nonzero quadratic level occurs \(U\) times and the nonzero isotropic level occurs \(Z-1\) times. The three relevant character sums are
\[
\sum_{t\ne0}H_{a,b}(t)=-6,
\qquad \sum_{t\ne0}H_{a,b}(t)^2
=6q-14-6\chi(ab)+4(T_a+T_b).
\]
For the first identity, each polynomial \(t(t-4a)\), \(t(t-4b)\), and \(\Delta_{a,b}(t)\) has discriminant a nonzero square or nonsquare but in all cases a nonzero *polynomial discriminant*, so the standard quadratic-character sum equals \(-1\) over the whole field, and \(H_{a,b}(0)=2\). For the second, expand the square. The three square terms sum to \(6q-12-4\chi(ab)\), the cross term between the first two is \(-2-2\chi(ab)\), and the remaining two cross terms are \(4T_a+4T_b\). Inserting both identities into the squared convolution proves the displayed energy formula. The Fourier identity follows from Parseval on the finite additive group.

**5. Cancellation across the second radius.** Fix \(a\ne0\). The polynomial \(\Delta_{a,b}(t)\), treated as a quadratic in \(b\), has discriminant \(16at\). Therefore, for \(t\ne0\), \(\sum_{b\in\mathbb F_q}\chi(\Delta_{a,b}(t))=-1\), and because the factors \(t(t-4a)\) vanish at \(t=0,4a\),
\[
\sum_{b\in\mathbb F_q}T_a(a,b)
=-\sum_{t\in\mathbb F_q}\chi(t(t-4a))=1.
\]
At \(b=0\) the quartic becomes \(t(t-4a)(t-a)^2\), whence \(T_a(a,0)=-1-\chi(-3)\). At \(b=a\), it becomes \(t^2(t-4a)^2\), whence \(T_a(a,a)=q-2\). Subtracting those excluded values gives \(4-q+\chi(-3)\). Also, a fourth-power change of variables gives the exact involution \(T_b(a,b)=T_a(a,a^2/b)\); as \(b\mapsto a^2/b\) permutes the allowed second radii, its sum is identical. The asserted \(\tau\)-sum follows from \(\tau_i=-1-T_i\).

To average the energy, observe that \(\sum_{b\ne0,a}\chi(ab)=-1\). Summing the fourth-moment formula over \(b\), inserting the two character-sum identities just proved, and dividing by \(q-2\) gives the exact mean-energy expression.

**6. Smoothness and trace normalization.** The quartic \(t(t-4a)\Delta_{a,b}(t)\) has four distinct roots over an algebraic closure except when \(b=9a\); the analogous quartic with \(a\) replaced by \(b\) is singular only when \(a=9b\). Here \(\Delta_{a,b}(4a)=(a-b)(9a-b)\) detects the collision. At a smooth ratio, its smooth projective model \(y^2=t(t-4a)\Delta_{a,b}(t)\) has two rational points at infinity, hence exactly \(q+2+T_a\) rational points and Frobenius trace \(-1-T_a\). At \(b=9a\), the sum simplifies to \(T_a=-1-\chi(-3)\); similarly for the second quartic when \(a=9b\). Hasse's bound applies to the smooth traces, not to a fictitious smooth curve at these resonances.

## Verification

The included standalone `check_even_shells.py` uses only the Python 3 standard library. Run it in an ordinary Python 3 environment. It implements prime and quadratic-extension fields and directly enumerates **every ordered pair** of the union of the two quadratic levels for the listed cases. All 21 direct convolution-energy checks passed, covering both quadratic form determinant classes, dimensions two/four/six, and field orders three, five, seven, nine and twenty-five. In total, 5,722,928 ordered pairs were enumerated. Across field orders \(3,5,7,9,11,13,17,25\), it also checked 74 allowed radius ratios, the trace-cancellation identity, the mean-energy formula and the singular-ratio specializations. These computations corroborate but are not substitutes for the all-field proof above.

## Relationship to prior work

Pham and Xue, *Sharp spherical extension theorem in \(\mathbb F_q^{2m}\) and applications* (first public September 30, 2026), establish sharp single-sphere extension estimates and supply the motivating even-dimensional Fourier setting. Their article studies a different fourth-moment question and does not state this exact two-radius energy average or the elliptic-trace cancellation. Brittenham and Pakianathan, *Random walks and the “Euclidean” association scheme in finite vector spaces*, give general quadratic-distance association-scheme intersection numbers and random-walk methods, including machinery sufficient to recover the individual two-shell convolution. The result claimed here is **not** novelty of these intersection numbers or of general Gauss-sum techniques; it is the explicit two-radius fourth-moment formula together with the all-field, field-size-independent cancellation as the radius varies. Existing general association schemes are genuine relevant prior coverage and may encode portions of the formula implicitly.

## Limitations

The input spheres must have two distinct nonzero radii and the field must have odd characteristic. This is an exact fourth moment of the indicator with uniform coefficients, not the sharp fourth-moment extension norm optimized over arbitrary coefficients. No individual energy minimizer over radii is asserted. The elliptic-curve description excludes singular ratios, although all the displayed character-sum and energy identities continue to hold there. A search of relevant literature and published mathematical records is not an exhaustive proof of priority; a stronger prior multi-shell or elliptic-pencil trace theorem could subsume the present result. Independent validation has not been carried out.

## References

1. Thang Pham and Boqing Xue, *Sharp spherical extension theorem in \(\mathbb F_q^{2m}\) and applications*, arXiv:2609.39876v1 (public September 30, 2026). https://arxiv.org/pdf/2609.39876v1
2. Charles Brittenham and Jonathan Pakianathan, *Random walks and the “Euclidean” association scheme in finite vector spaces*, Canadian Journal of Mathematics, published online May 24, 2024; DOI 10.4153/S0008414X24000518. https://doi.org/10.4153/S0008414X24000518
3. The standard quadratic Gauss-sum level formulas and the Hasse bound for elliptic-curve traces are used in the proof; neither is claimed as new.
