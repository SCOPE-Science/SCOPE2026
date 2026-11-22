# The sharp tenth-order Fourier-intensity jet for five equal-width intervals

## Finding
Let \(\Omega=\bigcup_{j=1}^{5}[x_j,x_j+w]\subset\mathbb R\), with \(w>0\) and \(x_1<x_2<\cdots<x_5\), \(x_{j+1}>x_j+w\). Define the angular-frequency Fourier transform and intensity by
\[
\widehat{\mathbf1_\Omega}(t)=\int_\Omega e^{-itx}\,dx,
\qquad I_\Omega(t)=|\widehat{\mathbf1_\Omega}(t)|^2.
\]
Then the six even Taylor data
\[
I_\Omega(0),\ I_\Omega''(0),\ I_\Omega^{(4)}(0),\ I_\Omega^{(6)}(0),\ I_\Omega^{(8)}(0),\ I_\Omega^{(10)}(0)
\]
determine \(\Omega\) up to translation and reflection. Tenth order is *globally necessary*: two explicit noncongruent five-interval unions have identical Taylor derivatives through order nine. Furthermore, on the open class where the third centered elementary symmetric function of the interval starts is nonzero, the derivatives through order eight already suffice; the extra tenth-order measurement resolves precisely the zero-skewness stratum.

## Assumptions and scope
The number of components is known to be exactly five; all five intervals have one unknown common positive width and have strictly positive separating gaps. No integer grid, generic gap, collision-free distance, or symmetry assumption is imposed. Translation and reflection are unavoidable since they preserve Fourier intensity. All derivatives are exact mathematical data at frequency zero, not noisy approximations. Only the one-dimensional angular-frequency convention above is used.

## Proof
**Step 1: remove the interval window.** Since \(I_\Omega(0)=25w^2\), recover \(w=\sqrt{I_\Omega(0)}/5\). The analytic identity
\[
I_\Omega(t)=w^2\operatorname{sinc}^2(wt/2)J(t),\qquad
J(t)=\left|\sum_{j=1}^{5}e^{-itx_j}\right|^2,
\qquad \operatorname{sinc}(u)=\frac{\sin u}{u}
\]
holds with the removable value at the origin. Division by the known nonvanishing analytic factor near zero recovers the Taylor jet of \(J\) to exactly the same order.

**Step 2: recover pairwise-distance moments.** Put
\[
M_{2k}=\sum_{1\le i<j\le5}(x_j-x_i)^{2k}, \qquad 1\le k\le5.
\]
From \(J(t)=5+2\sum_{i<j}\cos(t(x_j-x_i))\) we obtain
\[
J^{(2k)}(0)=2(-1)^kM_{2k}, \qquad J(0)=25.
\]
Translate the five starts to mean zero and denote their elementary symmetric functions by \(e_j\), so \(e_1=0\). Their monic root polynomial is
\[
P(X)=X^5+e_2X^3-e_3X^2+e_4X-e_5.
\]
Newton's identities and the binomial identity
\[
M_{2k}=\frac12\sum_{\ell=0}^{2k}(-1)^\ell\binom{2k}{\ell}p_\ell p_{2k-\ell},\quad
p_0=5,\ p_1=0,\ p_j=\sum_{i=1}^{5}x_i^j
\]
give, by exact expansion,
\[
\begin{aligned}
M_2&=-10e_2,\\
M_4&=2(11e_2^2-10e_4),\\
M_6&=-5(14e_2^3-30e_2e_4+15e_3^2),\\
M_8&=2(131e_2^4-468e_2^2e_4+316e_2e_3^2-400e_3e_5+290e_4^2),\\
M_{10}&=-5(206e_2^5-994e_2^3e_4+723e_2^2e_3^2-1600e_2e_3e_5\\
&\hspace{20mm}+1090e_2e_4^2+10e_3^2e_4+625e_5^2).
\end{aligned}
\]
Thus successive even moments recover exactly \(e_2\), \(e_4\), \(e_3^2\), \(e_3e_5\), and \(e_5^2\), in that order, each with nonzero coefficient.

**Step 3: prove global injectivity.** For real \(e_3,e_5\), the triple \((e_3^2,e_3e_5,e_5^2)\) determines \((e_3,e_5)\) modulo simultaneous sign reversal. If \(e_3\ne0\), the first two entries already suffice. If \(e_3=0\), the fifth moment \(M_{10}\) determines \(e_5^2\). Under reflection \(x_j\mapsto-x_j\), the even coefficients \(e_2,e_4\) stay fixed while \(e_3,e_5\) change sign simultaneously. Hence the recovered root polynomial specifies precisely one centered unordered five-point configuration modulo reflection; its strictly ordered roots recover the interval starts. This proves both the global tenth-order statement and the eighth-order statement for \(e_3\ne0\).

**Step 4: show tenth order is indispensable globally.** For \(c=1,2\), let \(x_1^{(c)}<\cdots<x_5^{(c)}\) be the real roots of
\[
P_c(X)=X^5-10X^3+9X-c.
\]
For both values of \(c\), polynomial signs at the two endpoints of each of the following five disjoint rational intervals are opposite:
\[
(-31/10,-29/10),\quad(-6/5,-9/10),\quad(0,3/10),\quad(3/4,1),\quad(29/10,31/10).
\]
Therefore each quintic has exactly one distinct real root in each displayed bracket, and adjacent roots have distance more than \(1/10\). Set \(w=1/10\) and \(\Omega_c=\bigcup_{j=1}^5[x_j^{(c)},x_j^{(c)}+w]\); both are admissible.

For both configurations, \((e_2,e_3,e_4)=(-10,0,9)\), whereas \(e_5=c\). Consequently
\[
(M_2,M_4,M_6,M_8)=(100,2020,56500,1824580)
\]
for both, while \(M_{10}=62684500-3125c^2\). Their Fourier intensities agree to derivative order nine, but
\[
I_{\Omega_1}^{(10)}(0)-I_{\Omega_2}^{(10)}(0)=-\frac{375}{2}\ne0.
\]
They are not translation-reflection congruent: once centered, a reflection changes \(e_5\) to \(-e_5\), whereas the two configurations have \(e_5=1\) and \(e_5=2\). This proves sharpness. In addition, on the \(e_3\ne0\) class, varying the constant term of a real-rooted quintic with fixed \(e_2,e_3,e_4\) preserves its first three distance moments, but changes \(e_3e_5\); for instance \(X^5-23X^3-18X^2+40X-\varepsilon\) has five distinct real roots for all sufficiently small real \(\varepsilon\), starting from simple roots \((-4,-2,0,1,5)\) at \(\varepsilon=0\). Thus the eighth-order threshold there is also necessary.

## Verification
Run \(\texttt{python checks/five_interval_jet_check.py}\) with SymPy installed. The self-contained checker exactly verifies all five Newton-moment identities, the rational endpoint sign changes for both quintics, their four coincident moments, their different tenth moments, and the common-width separation bound. It is diagnostic support, not a replacement for the universal argument above. No numerical root approximations are used as evidence. For the generic sixth-order counterexample, simple-root continuity suffices.

## Relationship to prior work
Xia and Xu (2026) motivate Fourier phase retrieval of finite interval unions, with general nonuniqueness beyond two intervals and conditions for recovery from the complete Fourier magnitude. The present restricted equal-width theorem instead determines the *sharp finite derivative order* for five components, including an exceptional algebraic stratum invisible through order eight. The accessible research literature includes a reduction of complete equal-width interval diffraction to point homometry and sixth-order jet results for three and four equal-width intervals; neither gives the five-point invariant decomposition or the tenth-order lower-bound witness. Boutin and Kemper analyze unlabeled complete distance distributions and reconstructibility tests, not sharp truncated distance-moment jets. The proof here does not infer finite-jet uniqueness from full-intensity uniqueness.

## Limitations
The theorem requires exactly five intervals of one common width and noiseless Taylor derivatives. It does not establish global stability near \(e_3=0\), solve reconstruction for arbitrary unequal widths, or classify more than five components. The cited Xia--Xu preprint could not be inspected in full in the available source access; its abstract and public description were examined, leaving residual bibliographic risk of an undisclosed overlapping finite-jet theorem. An older algebraic-invariant treatment could also imply the five-point identities without matching terminology. Independent mathematical validation has not been performed.

## References
- Yu Xia and Zhiqiang Xu, *Fourier Phase Retrieval for Finite Unions of Intervals*, arXiv:2606.19855v1, first submitted June 18, 2026, https://arxiv.org/abs/2606.19855.
- Mireille Boutin and Gregor Kemper, *Which Point Configurations are Determined by the Distribution of their Pairwise Distances?*, 2003 preprint, https://www.math.cit.tum.de/fileadmin/w00ccg/algebra/people/kemper/Boutin.Kemper_03.pdf.
- *Equal-width interval diffraction reduces exactly to finite point-set homometry*, publicly indexed research record, https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-equal-width-interval-diffraction-reduces-exactly-to-finite-point--417f34275d33.
- *Sixth-order Fourier-intensity recovery for three equal-width intervals*, publicly indexed research record, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-sixth-order-fourier-intensity-recovery-for-three-equal-width-int--df0589a6cbc2.
