# First positive-curvature core in Euclidean-distance weighted disk Bergman metrics

## Finding
Let \(A_t^2(\mathbb D)\) be the analytic Bergman Hilbert space with Euclidean boundary-distance weight \((1-|z|)^t\), \(t>-1\). With the curvature normalization below, the curvature at the center is
\[
\kappa_t(0)=\frac{4(t^2+t-15)}{5(t+3)(t+4)}.
\]
Consequently, the exact onset of **positive central curvature** is \(t_\star=(\sqrt{61}-1)/2\). For every \(t>t_\star\) the metric has a positive-curvature neighborhood of the center and negative curvature sufficiently close to the boundary, hence at least one zero-curvature circle. Near the onset, a unique **small** zero-curvature circle emerges, with squared radius
\[
s_\star(t)=\frac{56\sqrt{61}-427}{270}(t-t_\star)+O((t-t_\star)^2),\qquad t\downarrow t_\star.
\]
For the natural integer exponents \(t=0,1,2,3\), curvature is strictly negative throughout the disk. At the **first integer exponent permitting positive curvature, \(t=4\)**, there is **exactly one** zero-curvature circle in the entire disk, at radius \(r_4=\sqrt{s_4}\) where \(s_4=0.0175975033598718\ldots\). Curvature is positive inside that circle and negative outside. The algebraic equation determining \(s_4\) is given below.

## Assumptions and scope
The norm is \(\|f\|_t^2=\int_{|z|<1}|f(z)|^2(1-|z|)^t\,dx\,dy\). Its diagonal reproducing kernel is \(K_t(z,z)\). Put \(s=|z|^2\), \(L_t(s)=\log K_t(z,z)\), and define the positive radial metric coefficient and normalized complex curvature by
\[
g_t(s)=L_t'(s)+sL_t''(s)=\partial_z\partial_{\bar z}\log K_t(z,z),\qquad
\kappa_t(s)=-g_t(s)^{-1}\partial_z\partial_{\bar z}\log g_t(s).
\]
This normalization gives \(\kappa_0\equiv-1\) for the ordinary unweighted disk Bergman metric. The Gaussian curvature of the real conformal metric \(g_t(z)|dz|^2\) is \(2\kappa_t\); all curvature signs and zero sets are independent of this factor. All claimed zero circles are centered at \(0\). A “unique small circle” is a local statement; global uniqueness is asserted only at \(t=4\), not for arbitrary real \(t\).

## Proof
**1. Exact kernel and center jets.** The monomials form an orthogonal complete basis by angular Parseval and Tonelli. Their moments are
\[
\|z^n\|_t^2=2\pi\mathrm B(2n+2,t+1)=\frac{2\pi\Gamma(2n+2)\Gamma(t+1)}{\Gamma(2n+t+3)}.
\]
Writing \(F_t(s)=K_t(z,z)/K_t(0,0)\) gives, for \(|s|<1\),
\[
F_t(s)={}_2F_1\!\left(\frac{t+3}{2},\frac{t+4}{2};\frac32;s\right)=1+a_1s+a_2s^2+a_3s^3+\cdots,
\]
where
\[
a_1=\frac{(t+3)(t+4)}6,\quad
a_2=\frac{(t+3)(t+4)(t+5)(t+6)}{120},\quad
a_3=\frac{\prod_{j=3}^{8}(t+j)}{5040}.
\]
If \(\log F_t(s)=c_1s+c_2s^2+c_3s^3+O(s^4)\), the cumulant identities give
\[
 c_1=a_1,\quad
 c_2=a_2-\tfrac12a_1^2=-\frac{(t+3)(t+4)(t^2+t-15)}{180},
\]
\[
 c_3=a_3-a_1a_2+\tfrac13a_1^3
 =\frac{(t+3)(t+4)(2t^4+10t^3-16t^2-24t+315)}{5670}.
\]
Thus \(g_t(s)=c_1+4c_2s+9c_3s^2+O(s^3)\) and \(\kappa_t(0)=-4c_2/c_1^2\), proving the displayed central formula. Since \(t>-1\), its denominator is positive and the only admissible root is \(t_\star\).

**2. Emergence and boundary negativity.** At \(t=t_\star\), exact substitution into the preceding coefficients gives
\[
\partial_s\kappa_{t_\star}(0)=-\frac{24}{7}<0,\qquad
\left.\partial_t\kappa_t(0)\right|_{t=t_\star}=\frac{32\sqrt{61}-244}{45}>0.
\]
The moment series and all its spatial/parameter derivatives converge locally uniformly near \((t_\star,0)\), and \(g_t>0\) because the associated evaluation family is nondegenerate. The real-analytic implicit-function theorem therefore gives a single small root \(s(t)\) and its first-order expansion
\[
s(t)=-\frac{\partial_t\kappa}{\partial_s\kappa}(t-t_\star)+O((t-t_\star)^2)
=\frac{56\sqrt{61}-427}{270}(t-t_\star)+O((t-t_\star)^2).
\]
Its coefficient is strictly positive. For \(t\) just above the threshold, curvature is positive before this circle and negative immediately after it. For each fixed \(t>-1\), set \(x=\sqrt s\), \(T=t+2\), and use the binomial series to write
\[
K_t(z,z)=\frac{t+1}{4\pi x}\left[(1-x)^{-T}-(1+x)^{-T}\right].
\]
As \(s\uparrow1\), this implies \(g_t(s)\sim T(1-s)^{-2}\), with corresponding differentiated asymptotics and
\[
\lim_{s\uparrow1}\kappa_t(s)=-\frac2T=-\frac{2}{t+2}<0.
\]
For \(t>t_\star\), continuity now guarantees at least one zero circle between the positive center and the negative boundary.

**3. Exact first-integer classification.** For each integer \(m\ge0\), the same binomial expression reduces to \(K_m(z,z)\propto(1-s)^{-(m+2)}P_m(s)\), where
\[
P_m(s)=\sum_{0\le j<(m+2)/2}\binom{m+2}{2j+1}s^j.
\]
Direct exact differentiation gives \(\kappa_0=-1\); for \(m=1\), its numerator is \(s^6-18s^5-69s^4-140s^3-153s^2-450s-195\) with denominator \(3(s^2+2s+5)^3>0\). It is negative for \(0\le s<1\), since \(s^6\le1<195\). For \(m=2\), the curvature is
\[
-\frac{2(15s^6+150s^5+225s^4+244s^3+225s^2+150s+15)}{(5s^2+6s+5)^3}<0.
\]
For \(m=3\), its numerator is \(2[51s^{12}-324s^{11}-10170s^{10}-79220s^9-245763s^8-972936s^7-2826924s^6-4609800s^5-3802275s^4-2582580s^3-1294650s^2-346500s-6125]\), divided by \(5(3s^4+20s^3+114s^2+84s+35)^3>0\). It too is negative throughout \([0,1)\), since \(51s^{12}\le51<6125\) and the remaining terms are nonpositive.

For \(m=4\), \(P_4(s)=2(3+10s+3s^2)\). Exact differentiation and reduction give
\[
 g_4(s)=\frac{12(7s^4+28s^3+58s^2+28s+7)}{(1-s)^2(s+3)^2(3s+1)^2},
\]
\[
\kappa_4(s)=\frac{N(s)}{6(7s^4+28s^3+58s^2+28s+7)^3},
\]
with the reciprocal polynomial
\[
\begin{split}
N(s)={}&147(s^{12}+1)-7308(s^{11}+s)-55818(s^{10}+s^2)\\
&-195804(s^9+s^3)-455427(s^8+s^4)\\
&-850584(s^7+s^5)-1064716s^6.
\end{split}
\]
Its coefficient signs, from high to low degree, are \(+,-,-,\ldots,-,+\), so Descartes' rule gives **at most two** positive roots counting multiplicity. Since \(N(0)>0>N(1)\), one root is in \((0,1)\). Reciprocity \(s^{12}N(1/s)=N(s)\) yields a second root \(>1\). They exhaust the positive roots and are both simple. Therefore there is precisely one zero in \(0<s<1\), and its sign on the two sides is as stated. Numerical root isolation gives \(s_4\in(0.01759750,0.01759751)\); the exact algebraic specification is the unique root of \(N\) in \((0,1)\).

## Verification
The accompanying standalone `CHECK.py` uses exact symbolic arithmetic to reconstruct the moment coefficients, the central curvature formula and its transverse derivatives, all four integer-weight curvature identities, the rational expression for \(g_4\), and the degree-12 reciprocal numerator. It applies exact polynomial root counting and rational endpoint checks. These finite symbolic identities support the proof but do not substitute for the all-real-parameter analytic continuation and boundary asymptotics, which are proved above.

## Relationship to prior work
Marinescu and Xing (arXiv:2609.24258, first public September 21, 2026) establish real-analytic parameter dependence of weighted Bergman kernels for genuine boundary-distance powers. Their theorem provides the regularity context but does not classify metric curvature signs. The previously published exact Euclidean-distance disk kernel identity and Lu Qi-Keng zero classification in *Sharp Lu Qi-Keng transitions for Euclidean boundary-distance weighted disk kernels* (2026) give the off-diagonal kernel as an explicit powered difference; **that kernel identity is an input here, not claimed as new**. Differentiating it determines curvature formally, but the present curvature-sign transition, all-radius sign proof for integer exponents through four, and global unique circle require additional sign and root-count analysis not stated in that result. A distinct study, *Sharp curvature-sign transition and cubic-root bubbles in meromorphic Bergman metrics* (2026), concerns Laurent-holomorphic functions on a **punctured** disk with an **origin-power** weight; its zero-circle theorem does not cover the ordinary analytic space with Euclidean boundary-distance weight studied here. Classical Bergman-kernel-zero work by Perälä (2018) and Zeytuncu (2011) concerns different radial weights and does not supply this metric classification in the accessible material.

## Limitations
No global uniqueness statement for noninteger \(t\) is claimed; for each \(t>t_\star\) only existence of a zero-curvature circle is guaranteed. A local simple circle and its asymptotic are established near onset. The complete sign classification is proved for the five integer powers \(0\le m\le4\), not all powers. This is a theorem about **weighted Bergman metrics**, not off-diagonal Bergman-kernel zeros. Its kernel input is published; the claimed novelty is the curvature geometry and sharp finite integer cutoff, and historical priority remains subject to comparison with older curvature literature. The complete contemporary parameter-regularity manuscript was not retrievable; its available abstract and secondary technical synopsis were examined, so a residual full-text comparison risk remains.

## References
1. G. Marinescu and X. Xing, *Parameter Dependence of Weighted Bergman Kernels Beyond Smoothness*, arXiv:2609.24258v1 (first public 2026-09-21), https://arxiv.org/abs/2609.24258.
2. *Sharp Lu Qi-Keng transitions for Euclidean boundary-distance weighted disk kernels* (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-sharp-lu-qi-keng-transitions-for-euclidean-boundary-distance-wei--b68d363f03d0.
3. *Sharp curvature-sign transition and cubic-root bubbles in meromorphic Bergman metrics* (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-sharp-curvature-sign-transition-and-cubic-root-bubbles-in-meromo--3801ebdfe4c3.
4. A. Perälä, *Vanishing Bergman Kernels on the Disk*, J. Geom. Anal. 28 (2018), 1716–1727, arXiv:1703.05976.
5. Y. E. Zeytuncu, *Weighted Bergman Projections and Kernels: Lp Regularity and Zeros*, Proc. Amer. Math. Soc. 139 (2011), 2105–2112, arXiv:1009.2806.
