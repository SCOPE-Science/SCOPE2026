# A sharp four-atom dual Minkowski inverse and symmetry-breaking threshold

## Finding
Fix a real exponent \(q>0\). For \(a,b>0\), let \(K_{a,b}=[-a,a]\times[-b,b]\subset\mathbb R^2\), with the origin in its interior, and denote its standard \(q\)-th dual curvature measure by \(\widetilde C_q(K_{a,b},\cdot)\). Let \(A\) be its mass at each of \(e_1,-e_1\), and \(B\) its mass at each of \(e_2,-e_2\). For prescribed \(A,B>0\), define \(\rho=A/B\).

**Exact realization criterion for an even four-atom measure.** In fact these conditions characterize realizability among **all planar convex bodies containing the origin** whose \(q\)-th dual curvature measure has precisely the four indicated atoms. The number of centered rectangular realizers, with actual side lengths rather than only their shapes, is as follows:

* For \(0<q\leq1\), every \(\rho>0\) is realized by exactly one centered rectangle.
* For \(1<q<2\) or \(q>2\), a rectangle exists exactly when
  \[
  \min\{q-1,(q-1)^{-1}\}<\rho<\max\{q-1,(q-1)^{-1}\}.
  \]
  Within this strict interval the realizing rectangle is unique, and no rectangle exists at either endpoint.
* For \(q=2\), a rectangle exists exactly when \(A=B\); then the complete fiber is the one-parameter family \(ab=A\). Otherwise the fiber is empty.

**Rigidity and symmetry breaking.** When \(q\geq1\), **every** planar convex body realizing such an even four-atom measure (without any a priori symmetry assumption) must be a centered axis-parallel rectangle. Thus the classification above is also the complete global solution-fiber classification in this range. By contrast, for every \(0<q<1\) there are positive even four-atom targets admitting both a centered rectangle and a distinct **off-center** rectangle with the origin in its interior; uniqueness is asserted only among centered rectangles for those exponents.

The inverse has an explicit one-dimensional construction. Put \(r=a/b\), \(p=(q-2)/2\), and
\[
 I_x(r)=\int_0^1(r^2+t^2)^p\,dt,\qquad
 I_y(r)=\int_0^1(1+r^2t^2)^p\,dt,\qquad
 R_q(r)=\frac{I_x(r)}{I_y(r)}.
\]
For \(q\ne2\), there is exactly one \(r>0\) solving \(R_q(r)=\rho\) whenever the above existence condition holds. Its unique realization is
\[
 b=\left(\frac{B}{r I_y(r)}\right)^{1/q},\qquad a=rb.
\]
The ratio map is strictly decreasing when \(0<q<2\), strictly increasing when \(q>2\), and obeys \(R_q(1/r)=R_q(r)^{-1}\). Its sharp endpoint behavior is
\[
 \lim_{r\to\infty}R_q(r)=
 \begin{cases}0,&0<q\leq1,\\q-1,&q>1.\end{cases}
\]
For \(0<q<1\), setting \(c_q=\int_0^\infty(1+t^2)^{(q-2)/2}\,dt\), one has \(R_q(r)\sim r^{q-1}/c_q\) as \(r\to\infty\); for \(q=1\), \(R_1(r)\sim1/\log(2r)\). These supply precise boundary degeneration rates. At \(q=4\), \(R_4(r)=(3r^2+1)/(r^2+3)\): a mass ratio of two determines \(r=\sqrt5\) and the admissible ratio interval is \((1/3,3)\).

## Assumptions and scope
The statement concerns the exact image of even four-atom targets under the \(q\)-th dual curvature measure on all planar convex bodies containing the origin, plus a complete solution-fiber classification when \(q\geq1\) and a complete **centered-rectangle** fiber classification for every \(q>0\). The four normal directions are precisely \(\{\pm e_1,\pm e_2\}\), with a positive equal mass on each antipodal pair. For \(0<q<1\), it does not classify every off-center realizing rectangle (only proves some exist in addition to the uniquely determined centered rectangle). Any other normal set is excluded by the exact support of the prescribed measure. It assumes \(q>0\), positive side lengths, and positive prescribed masses. The endpoints in the displayed solvability interval correspond only to degenerate limits of aspect ratio and are not attained by a positive-width rectangle.

We use the standard normalization
\[
 \widetilde C_q(K,\eta)=\frac12\int_{\alpha_K^*(\eta)}\rho_K(u)^q\,du
 =\frac q2\int_{C(K,\nu_K^{-1}(\eta))}|x|^{q-2}\,dx
\]
for planar bodies containing the origin. Here \(\alpha_K^*\) is the reverse radial Gauss image, \(\rho_K\) the radial function, and the second integral runs over the radial cone from the origin to the corresponding exposed boundary part. Edges and vertices at which the normal is not unique contribute no planar Lebesgue measure.

## Proof
**1. Exact four-atom mass formulas.** On the positive horizontal-normal edge, radial rays fill the triangle with vertices \((0,0),(a,b),(a,-b)\). Parametrize its interior as \((x,y)=(as,bst)\), with \(0<s<1\), \(-1<t<1\). The Jacobian is \(abs\). Consequently, putting \(p=(q-2)/2\) and integrating \(s^{q-1}\),
\[
\begin{aligned}
 A&=\frac q2 ab\int_{-1}^1(a^2+b^2t^2)^pdt\int_0^1s^{q-1}ds
 =ab\int_0^1(a^2+b^2t^2)^pdt,\\
 B&=ab\int_0^1(b^2+a^2t^2)^pdt.
\end{aligned}
\]
Central symmetry supplies the same masses on opposite edges. After \(r=a/b\), these identities become \(A=rb^q I_x(r)\), \(B=rb^q I_y(r)\). The integrals are positive and finite for every \(r>0,q>0\).

**2. Strict aspect-ratio monotonicity.** Let \(\langle f\rangle_x\) denote average with normalized density proportional to \((r^2+t^2)^p\) on \([0,1]\), and similarly \(\langle f\rangle_y\) with density proportional to \((1+r^2t^2)^p\). Differentiate under the integral sign for positive \(r\):
\[
 \frac{d\log R_q(r)}{d\log r}=(q-2)
 \left[\left\langle\frac{r^2}{r^2+t^2}\right\rangle_x
 -\left\langle\frac{r^2t^2}{1+r^2t^2}\right\rangle_y\right].
\]
For every \(0\leq t<1\), the first integrand is strictly greater than \(r^2/(1+r^2)\), while the second is strictly smaller than the same quantity. Both averaging densities are strictly positive on \((0,1)\). The square bracket is therefore strictly positive for every \(r>0\), independently of \(q\). Hence \(R_q\) decreases strictly for \(q<2\), increases strictly for \(q>2\), and is identically one when \(q=2\). Exchanging the axes proves the reciprocal identity \(R_q(1/r)=1/R_q(r)\).

**3. Exhaustive endpoint limits.** If \(q>1\), then \(p>-1/2\). Dividing both defining integrals by \(r^{q-2}\) and using dominated convergence (the denominator's rescaled integrand is bounded by a suitable integrable multiple of \(t^{q-2}\) near zero),
\[
 \frac{I_x(r)}{r^{q-2}}\longrightarrow1,
 \qquad \frac{I_y(r)}{r^{q-2}}\longrightarrow \int_0^1t^{q-2}dt=\frac1{q-1}.
\]
Thus \(R_q(r)\to q-1\). For \(0<q<1\), \(p<-1/2\), and the substitution \(u=rt\) yields
\[
 I_y(r)=\frac1r\int_0^r(1+u^2)^pdu\sim\frac{c_q}{r},
 \qquad I_x(r)\sim r^{q-2},
\]
so \(R_q(r)\sim r^{q-1}/c_q\to0\). At \(q=1\), exact integration gives
\[
 I_x(r)=\operatorname{arsinh}(1/r),\quad I_y(r)=\frac{\operatorname{arsinh}(r)}r,
 \quad R_1(r)=\frac{r\operatorname{arsinh}(1/r)}{\operatorname{arsinh}(r)}\sim\frac1{\log(2r)}.
\]
The limit as \(r\to0\) follows in all cases by reciprocal symmetry. Combining these limits with strict monotonicity determines precisely the open ranges above; no other values can occur, including either finite endpoint at \(q>1\).

**4. Centered inverse fiber and critical homogeneity.** When \(q\ne2\), continuous strict monotonicity gives one and only one \(r>0\) for each admissible \(\rho\). The equation \(B=rb^q I_y(r)\) fixes \(b>0\) uniquely and hence fixes \(a\). When \(q=2\), the mass equations simplify to \(A=B=ab\) and impose no restriction on the aspect ratio; exactly the family \(ab=A\) realizes the data. Finally, for \(q=4\), integrating the two quadratic kernels gives \(I_x=r^2+1/3\), \(I_y=1+r^2/3\), and hence the explicit illustration.

**5. Exhaustion of all planar convex-body realizers and the sharp symmetry threshold.** Let \(K\subset\mathbb R^2\) be any convex body with \(0\in\operatorname{int}K\) whose dual curvature measure equals the prescribed four-atom measure. On a radial cone of an exposed boundary arc, integrating the radial scale gives the Gauss-map pushforward of \(\frac12 h_K(\nu(x))|x|^{q-2}d\mathcal H^1(x)\). Since the origin lies in the interior, the support function and radial distance along the boundary are bounded above and below by positive constants. Therefore this positive bounded density does not change the support in the space of outer normals relative to ordinary surface-area measure. If that support consists of four directions \(\{\pm e_1,\pm e_2\}\), the planar convex boundary has only four straight sides and hence \(K\) is an axis-parallel rectangle. All four masses being positive forces all four sides to be present.

Write the rectangle as \(K=[-a_-,a_+]\times[-b_-,b_+]\) with positive parameters. For a given vertical interval \([-b_-,b_+]\), the opposite horizontal-normal masses equal
\[
 A_+=\frac{a_+}{2}\int_{-b_-}^{b_+}(a_+^2+y^2)^p\,dy,\qquad
 A_-=\frac{a_-}{2}\int_{-b_-}^{b_+}(a_-^2+y^2)^p\,dy.
\]
For fixed \(-b_-<0<b_+\), define \(H(s)=s\int_{-b_-}^{b_+}(s^2+y^2)^pdy\). Direct differentiation gives
\[
 H'(s)=\int_{-b_-}^{b_+}(s^2+y^2)^{p-1}\big((q-1)s^2+y^2\big)\,dy>0\quad (q\geq1,\ s>0).
\]
The strict inequality holds even at \(q=1\), since the interval contains nonzero \(y\). Equality of prescribed masses \(A_+=A_-\) forces \(a_+=a_-\). Applying the identical argument to the horizontal interval forces \(b_+=b_-\) from the two vertical-normal masses. Therefore every realizer with \(q\geq1\) is centered, proving the global characterization and the complete global fibers in that range.

For \(0<q<1\), fix the symmetric vertical span \([-1,1]\) and write
\[
 h_q(s)=s\int_0^1(s^2+y^2)^{(q-2)/2}\,dy,\qquad s>0.
\]
This is positive and continuous but satisfies \(h_q(s)\to0\) as \(s\downarrow0\) (indeed \(h_q(s)\sim c_q s^q\)) and as \(s\to\infty\) (indeed \(h_q(s)\sim s^{q-1}\)). Its supremum is therefore attained at a positive interior argument. Select any strictly smaller positive value and obtain two distinct positive numbers \(s_1<s_2\) with \(h_q(s_1)=h_q(s_2)\), by the intermediate value theorem on either side of a maximizer. Then \(K=[-s_1,s_2]\times[-1,1]\) has equal masses at \(\pm e_1\), while its top and bottom masses are automatically equal by horizontal reflection. All four atoms are positive. The centered inverse theorem already proved supplies another, centrally symmetric rectangle with exactly the same four masses, and it is distinct because \(s_1\ne s_2\). This proves a genuine loss of global origin-symmetry rigidity for every \(0<q<1\), without asserting the full off-center solution fiber classification.

## Verification
The standalone standard-library program `verify.py` tests independent radial-cone and angular formulas for face masses, exact rational-polynomial identities at \(q=4\), strict monotonicity samples for eight positive exponents, reciprocity, numerical inverse recovery, and the open solvability boundaries. It prints a count of successful deterministic cases and exits nonzero on a failed assertion. The proof above, not these finite tests, establishes the all-exponent and all-aspect-ratio assertions. Integrals for inverse reconstruction may be evaluated by deterministic one-variable quadrature and solved by bisection because strict monotonicity and the exact range are proved.

## Relationship to prior work
Cory Monahan (2026) proves existence in discrete dual Minkowski problems under geometric hypotheses on the normals, including general position and a separate planar class with at least five normals; the four coordinate normals used here contain antipodal linearly dependent pairs and therefore do not meet those hypotheses. This result instead gives a complete explicit four-normal inverse among centered rectangles, proves that these are all convex-body solutions for \(q\ge1\), and constructs off-center solutions for every exponent \(0<q<1\). No statement about other normal supports is inferred.

Ge Xiong and Kai-Wen Yang (2026) prove uniqueness **among origin-symmetric** planar convex bodies when \(0<q<2\). Together with known symmetric existence criteria based on subspace concentration (Böröczky–Lutwak–Yang–Zhang–Zhao, and Shan), this already covers the abstract symmetric realizability characterization for \(0<q<2\); the explicit inverse is not claimed to supersede those results. The new **global rigidity of all realizers about the origin for \(1\leq q<2\)**, its sharp breakdown at \(q<1\), and the complete \(q>2\) inverse fibers are distinct statements. They also establish global nonuniqueness phenomena for \(q>2\), which do not imply the restricted rectangular fiber classification or ratio boundaries. Their rectangle calculations concern total dual quermassintegrals and a Brunn–Minkowski inequality, rather than the four separate prescribed facet masses.

Tao's recent planar dual-quermassintegral inequalities and the earlier dual Brunn–Minkowski rectangle endpoint computations do not determine these inverse four-atom fibers. Nearby exact planar \(L_p\) surface-area two-atom inverse problems in cones use another measure and an unbounded domain and do not imply the dual-curvature rectangle calculation. The presently inspected sources supplied no equivalent exact range theorem; historical novelty is a qualified comparison, not a universal absence claim.

## Limitations
For \(q\geq1\) no other planar realizers are possible; for \(0<q<1\) the off-center solution set is not exhaustively classified. In the range \(0<q<2\), general symmetric uniqueness was established in prior work, and is not claimed as original here. Prior publications not indexed or accessible in the present literature comparison may contain equivalent special-case computations. The verification program supplies finite numerical consistency tests only; all exact claims rest on the elementary integral and strict inequality arguments above. The result has not undergone independent mathematical review.

## References
1. C. Monahan, *A Topological Approach to the Discrete Dual Minkowski Problem*, arXiv:2611.13375v1, first posted 9 November 2026, https://arxiv.org/html/2611.13375v1.
2. G. Xiong and K.-W. Yang, *The uniqueness and non-uniqueness of solutions to the even dual Minkowski problem*, arXiv:2608.01912v1, 3 August 2026, https://arxiv.org/abs/2608.01912.
3. J. Tao, *On the \(L_p\) Brunn–Minkowski inequality for planar dual quermassintegrals*, arXiv:2610.09636v1, October 2026, https://arxiv.org/abs/2610.09636.
4. Y. Huang, E. Lutwak, D. Yang and G. Zhang, *Geometric measures in the dual Brunn–Minkowski theory and their associated Minkowski problems*, Acta Mathematica 216 (2016), 325–388.
5. K. Böröczky, E. Lutwak, D. Yang, G. Zhang and Y. Zhao, *The dual Minkowski problem for symmetric convex bodies*, Advances in Mathematics 356 (2019), arXiv:1703.06259.
6. M. Henk and H. Pollehn, *Necessary subspace concentration conditions for the even dual Minkowski problem*, Advances in Mathematics 323 (2018), 114–141, arXiv:1703.10528v1.
7. J. Shan, *The Dual Minkowski Problem under Group Actions*, arXiv:2605.15891v1, 15 May 2026.
