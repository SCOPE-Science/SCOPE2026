# A sharp three-cycle frontier and multiplier spectrum for a singular logistic family

## Finding
For the singular rational map
\[
 f_\mu(x)=\frac{\mu x(1-x)}{\mu-x},\qquad -\infty<\mu<-\frac13,
\]
with forward iterates required to be finite and defined, set \(A=1-1/\mu\in(1,4)\). It has no real primitive period-three orbit when \(1<A<3\). At \(A=3\), equivalently \(\mu=-1/2\), exactly one real primitive period-three orbit exists and its return multiplier is \(+1\). For every \(3<A<4\) there are exactly two real primitive period-three orbits, with multipliers
\[
 \Lambda_{\mathrm{low}}=1+2(A-3)^2-2A\sqrt{A(A-3)},\qquad
 \Lambda_{\mathrm{high}}=1+2(A-3)^2+2A\sqrt{A(A-3)}.
\]
The high-multiplier orbit always repels. The low-multiplier orbit attracts exactly when \(3<A<3+\delta_*\), has multiplier \(-1\) at \(A=3+\delta_*\), and repels thereafter, where \(\delta_*\in(0,1)\) is the unique positive zero of
\[
 9\delta^3+25\delta^2+27\delta-1=0
\]
(\(\delta_*\approx0.03583282014255\)). At the onset \(A=3\), the two orbit-trace branches split with square-root separation. Furthermore, the map admits real primitive periodic points of **every positive integer least period** precisely for \(3\le A<4\) within the stated parameter interval.

## Assumptions and scope
All parameters satisfy \(\mu< -1/3\) and \(\mu\) is finite, so \(1<A<4\). Only finite real periodic orbits of the single-valued rational map are counted; an orbit cannot hit the pole \(x=\mu\). The point \(x=0\) is fixed, not a three-cycle. Other points with singular or eventually undefined iterates are excluded. A real period-three orbit is a set of three distinct finite points cycled by the map. The multiplier of such an orbit is the product of the three ordinary one-step derivatives.

For \(x\ne0,1\), introduce the fractional-linear coordinate \(y=1-1/x\), with inverse \(x=1/(1-y)\), wherever finite. Direct substitution yields the conjugate
\[
 F_A(y)=y-A+\frac{A}{y}.
\]
The coordinate \(y=1\) corresponds to the point at infinity rather than a finite real \(x\), and \(y=0\) to \(x=1\). Neither belongs to a primitive three-cycle. For \(y<0\), \(F_A(y)<y-A\), so no negative \(y\) can be periodic. When \(1<A<4\), every positive \(y\) has positive image, since \(F_A(y)\ge2\sqrt A-A>0\). Therefore every finite real primitive three-cycle corresponds exactly to a positive primitive three-cycle of \(F_A\).

## Proof
**1. Exact cycle polynomial and root count.** Write
\[
 Q_1=y^2-Ay+A,\qquad Q_2=Q_1^2-AyQ_1+Ay^2.
\]
Because \(F_A(y)=Q_1/y\) and \(F_A^2(y)=Q_2/(yQ_1)\), substitution and cancellation give the exact identity
\[
 F_A^3(y)-y=-\frac{A(y-1)P_A(y)}{yQ_1(y)Q_2(y)},
\]
where
\[
\begin{aligned}
P_A(y)={}&3y^6-12Ay^5+(15A^2+9A)y^4\\
&-(6A^3+20A^2)y^3+(11A^3+6A^2)y^2\\
&-6A^3y+A^3.
\end{aligned}
\]
For the relevant positive coordinates, \(Q_1,Q_2>0\), because they are positive multiples of successive images of positive iterates. In particular, no root of \(P_A\) is a spurious pole. The only positive fixed point of \(F_A\) is \(y=1\); it is not a root of \(P_A\) because
\[
 P_A(1)=A^2-3A+3>0.
\]
Consequently the real positive roots of \(P_A\) count primitive period-three points exactly.

Direct elimination gives the fully factored discriminant
\[
 \operatorname{Disc}_y P_A=5184A^{15}(A-3)^3(A^2-3A+3)^2.
\]
At \(A=1\), every positive orbit of \(F_1(y)=y-1+1/y\) enters \([1,\infty)\) in at most one step, then decreases strictly toward \(1\) unless already fixed. No positive primitive three-cycle exists, and none of the rational iteration denominators vanishes. Thus \(P_1\) has no real roots. Its leading coefficient is the fixed constant \(3\), its constant term \(A^3\) is nonzero for \(A>0\), and its discriminant is nonzero throughout \(1\le A<3\). Continuity of the polynomial roots implies it has no real roots throughout \(1<A<3\).

At \(A=3\),
\[
 P_3(y)=3\bigl(y^3-6y^2+9y-3\bigr)^2.
\]
The cubic has three distinct positive real roots: one each in \((0,1/2)\), \((1,2)\), and \((3,4)\), using sign changes at these rational endpoints. They are not the fixed point \(1\), hence constitute one primitive three-cycle. Because they are double roots of \(F_3^3(y)-y\), the primitive return multiplier is \(+1\).

At \(A=4\) the sextic specializes to
\[
 P_4(y)=\bigl(y^3-10y^2+24y-8\bigr)
\bigl(3y^3-18y^2+24y-8\bigr).
\]
The first cubic has roots respectively in \((0,1)\), \((3,4)\), and \((6,7)\); the second in \((0,1)\), \((1,2)\), and \((4,5)\). The discriminant stays nonzero for all \(3<A\le4\), and \(P_A(0)>0\), so the six positive simple real roots persist throughout \(3<A<4\). They partition into exactly two primitive three-cycles.

**2. Explicit orbit cubics and multipliers.** For \(3<A<4\), put \(t=\sqrt{A(A-3)}\) and define
\[
 C_\pm(y)=y^3-(2A\pm t)y^2+A(A\pm t)y-\frac{A(A\pm t)}3.
\]
Expansion using \(t^2=A(A-3)\) gives \(P_A=3C_+C_-\). Indeed each cubic separately carries one orbit: with \(Q_1=y^2-Ay+A\), the exact polynomial identities are
\[
 y^3 C_\pm(Q_1/y)=C_\pm(y)
 \bigl(y^3-3Ay^2+(A^2\mp At+3A)y-A^2\pm At\bigr).
\]
The three roots of each cubic are therefore permuted by \(F_A\). Since no root is fixed, each triple is one primitive period-three orbit.

For a cubic root triple let \(S=\sum_jy_j\), \(U=\sum_{i<j}y_iy_j\), \(V=\prod_jy_j\). Here \(S=2A\pm t\), \(U=A(A\pm t)\), and \(V=U/3\). Since \(F'_A(y)=1-A/y^2\), its product over the orbit is
\[
\begin{split}
 \Lambda&=\frac{V^2-A(U^2-2SV)+A^2(S^2-2U)-A^3}{V^2}\\
 &=1+2(A-3)^2\mp2At.
\end{split}
\]
This gives the advertised multipliers, with \(C_+\) carrying \(\Lambda_{\mathrm{low}}\). Let \(\delta=A-3>0\). The inequality \(\delta^2<A\sqrt{A\delta}\) proves \(\Lambda_{\mathrm{low}}<1\), while \(\Lambda_{\mathrm{high}}>1\). The sign of \(\Lambda_{\mathrm{low}}+1\) is that of \(1+\delta^2-A\sqrt{A\delta}\), whose sign equals that of
\[
(1+\delta^2)^2-A^3\delta=1-27\delta-25\delta^2-9\delta^3.
\]
That polynomial decreases strictly from \(1\) to a negative value on \((0,1)\), and has the unique zero \(\delta_*\), proving the full stability classification.

At \(A=3\), the orbit cubic is \(C_0(y)=y^3-6y^2+9y-3\). Its discriminant is \(81\). Its perturbation coefficient in the \(t\)-direction is \(-y^2+3y-1\), whose resultant with \(C_0\) is \(-1\), so each of the three points splits nontrivially into two branches. As the orbit sums differ by \(2t\sim2\sqrt{3(A-3)}\), the onset is an exact three-point parabolic/saddle-node collision with square-root splitting.

**3. The all-period frontier.** For \(3\le A<4\), set \(r=\sqrt A\), \(m=2r-A\), and \(M=F_A(m)\). Then \(0<m<r\), and straightforward algebra gives
\[
 M/r-1=\frac{(2r-3)(r-1)}{2-r}>0.
\]
The unique turning point of \(F_A\) is \(r\), where its minimum equals \(m\). On the compact interval \(I=[m,M]\), its maximum occurs at an endpoint: \(F_A(m)=M\) and \(F_A(M)\le M\), the latter following from \(M>r>1\) and \(F_A(y)-y=A(1/y-1)\). Hence \(F_A(I)\subseteq I\). All period-three points lie in this interval: every point of a positive periodic orbit is at least \(m\), while a maximum greater than \(M\) could not be generated from any smaller point, since \(F_A\le M\) on \([m,r]\) and \(F_A(y)<y\) for \(y>1\). The continuous interval map \(F_A|_I\) thus has a primitive period-three orbit for every \(3\le A<4\). Sharkovskii's theorem supplies a primitive orbit for every positive least period on \(I\), with no singular points and preserved by the conjugacy to \(f_\mu\). Conversely for \(1<A<3\) a primitive period-three orbit does not exist, so the property of having every period fails. This establishes sharpness.

## Verification
The standalone `verify.py` uses exact symbolic arithmetic to check the iterate identity, degree-six discriminant, factorization into orbit cubics, their invariance, multiplier reduction, the onset factorization and cubic discriminant, the flip polynomial, the exact rational sign intervals at \(A=4\), and the trapping interval inequality. Tests at noncritical rational parameters compare the exact multiplier formulas to derivatives computed directly on numerical three-cycles. The polynomial identities prove finite algebraic certificates; root-count continuity and Sharkovskii's theorem supply the infinite-parameter and all-period deductions. Numerical tests alone would not establish those deductions.

## Relationship to prior work
Alexanian's 2022 study introduces this special \(\alpha=\mu\) branch in equation (13), and its Figure 11 explicitly exhibits a period-three orbit for \(\mu=-1/2\), while giving numerical examples of other periods. Its statements therefore already imply the **existence** of period three at this single parameter, and Sharkovskii's theorem is classical. The distinguishing claims here are the exact exclusion for \(\mu<-1/2\), the complete one-to-two orbit census across the threshold, explicit multiplier and flip spectra, and exact identification of the onset parameter as parabolic; they are not claimed as consequences of generic period-three forcing alone. The 1992 antecedent studies this singular family qualitatively, but its full text was not available for a decisive comparison. A superficially related published three-cycle classification concerns a second-order rational recurrence, not this one-dimensional rational map, so it does not imply the formulas above.

## Limitations
The theorem is deliberately limited to the real finite-orbit branch \(\mu<-1/3\), corresponding to \(1<A<4\). It does not classify complex cycles, global attractors or periodic dynamics outside this parameter interval. Linear stability is not a claim of global attraction. The parabolic orbit at the threshold has derivative \(+1\) and is not classified as hyperbolic. Algebraic checking is reproducibility support, not independent certification. Older literature including the 1992 source may contain an equivalent exact three-cycle classification; that residual publication-priority risk is unresolved without access to its complete text. Independent external mathematical validation has not occurred.

## References
1. M. Alexanian, *One-dimensional Dynamics for a Discontinuous Singular Map and the Routes to Chaos*, Armenian Journal of Physics **15** (2022), 151–161, https://arxiv.org/abs/2212.12033, https://doi.org/10.54503/18291171-2022.15.4-151 (first public arXiv record: 2022-12-22).
2. M. Alexanian, *One-dimensional dynamics for a discontinuous map*, Physica A **181** (1992), 53–68, https://doi.org/10.1016/0378-4371(92)90196-W (bibliographic and abstract-level comparison only).
3. O. M. Sharkovskii, *Co-existence of cycles of a continuous mapping of the line into itself*, Ukrainian Mathematical Journal **16** (1964), 61–71 (period-forcing theorem).
