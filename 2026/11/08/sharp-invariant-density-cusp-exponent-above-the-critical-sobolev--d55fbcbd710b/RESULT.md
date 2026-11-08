# Sharp invariant-density cusp exponent above the critical Sobolev threshold

## Finding
For \(-1/2<\beta<0\) and \(1<\vartheta<2\), define \(F_{\beta,\vartheta}:[0,1]\to[0,1]\) by
\[
F_{\beta,\vartheta}(1/2\pm t)=1-\vartheta t-A t^{1+\beta},\quad A=2^{1+\beta}(1-\vartheta/2),\quad 0\le t\le1/2.
\]
Let \(h\) be its normalized absolutely continuous invariant density. Put \(\gamma=-\beta/(1+\beta)\in(0,1)\). Its bounded-variation representative is continuous at the cusp \(c=1/2\), strictly positive there, and obeys
\[
\lim_{x\uparrow1}\frac{h(x)}{(1-x)^\gamma}
=\frac{2h(1/2)}{(1+\beta)A^{1/(1+\beta)}}\in(0,\infty).
\]
In particular, \(h\notin W^{2,1}(0,1)\). The exact endpoint power supplies a sharp *actual-density* obstruction on the side \(\beta>-1/2\) of the critical exponent, complementing the established \(W^{2,1}\) result at \(\beta=-1/2\).

## Assumptions and scope
Throughout, \(-1/2<\beta<0\), \(1<\vartheta<2\), and \(A=2^{1+\beta}(1-\vartheta/2)>0\). All endpoint limits are one-sided. The transfer operator acts by \((P\phi)(x)=\sum_{F(y)=x}\phi(y)/|F'(y)|\), for almost every \(x\in(0,1)\). A BV density is understood through its one-sided limits at discontinuities, and its continuous representative wherever the proof establishes continuity. No claim is made for general random compositions, for invariant densities at other cusp values, or for exponents \(\beta\ge0\).

## Proof
**1. Two full expanding branches.** The endpoint values are \(F(0)=F(1)=0\) and \(F(c)=1\), so each half-interval maps monotonically onto \([0,1]\). On both branches the derivative magnitude at distance \(t>0\) from the cusp is
\[
p(t)=\vartheta+A(1+\beta)t^\beta.
\]
Because \(\beta<0\), it decreases with \(t\), and its minimum is
\[
\Lambda=\vartheta+(2-\vartheta)(1+\beta)>1.
\]
The inverse branches are therefore Lipschitz with constant at most \(\Lambda^{-1}<1\), and their positive inverse-Jacobian weights extend continuously to zero at cusp image \(1\). On each branch, the variation of \(1/p\) is bounded by its endpoint value \(1/\Lambda\). Thus the standard bounded-variation expanding-map theorem (Rychlik's setting) supplies an invariant BV density. Shrinking full-branch cylinders imply topological exactness. The BV ergodic decomposition then has one component, giving a unique normalized invariant probability density \(h\ge0\) (the same standard argument is written out for the critical family in reference [1], Proposition 4.2). No regularity stronger than BV is assumed here.

**2. Interior continuity and positivity.** Fix \(z\in(0,1)\). Since all branches of \(F^n\) have full image \([0,1]\), no interior endpoint of a branch image creates a jump at \(z\). Any jump in \(P^n h\) at \(z\) comes from jumps of \(h\) at preimages of \(z\). If \(J_\phi(y)\) denotes the jump of a BV function at \(y\), the change-of-variables formula gives
\[
|J_{P^nh}(z)|\le\sum_{F^ny=z}\frac{|J_h(y)|}{|(F^n)'(y)|}\le\Lambda^{-n}\operatorname{Var}(h).
\]
All these preimages are on smooth branch interiors because \(z\in(0,1)\), and the sum of absolute jumps over any set is bounded by the total variation. Since \(P^n h=h\) almost everywhere, their canonical BV representatives have the same jumps. Letting \(n\to\infty\) proves that \(h\) has no jumps anywhere inside \((0,1)\), hence is continuous there (a BV function has left and right limits at each point, and no jump means they agree).

Because \(h\ge0\) has integral one, there are \(d>0\) and an open interval \(U\Subset(0,1)\) on which \(h\ge d\) almost everywhere (choose a point of continuity with positive value). A sufficiently deep full-branch cylinder \(J\) has closure contained in \(U\), by contraction and topological exactness. Its inverse branch \(g_J:(0,1)\to\operatorname{int}J\) satisfies \(g_J'>0\) in absolute value. Thus
\[
h(x)=P^nh(x)\ge d\,|g_J'(x)|>0
\]
for almost all \(x\in(0,1)\) and the cylinder rank \(n\). Continuity now gives \(h(c)>0\).

**3. The endpoint transfer asymptotic.** Let \(\delta=1-x\downarrow0\) and let \(t=t(\delta)\) be the unique distance solving
\[
\delta=\vartheta t+A t^{1+\beta}.
\]
Since \(0<1+\beta<1\), one has \(\vartheta t=o(t^{1+\beta})\), hence
\[
t(\delta)\sim(\delta/A)^{1/(1+\beta)}.
\]
Both preimages of \(x\) are \(c\pm t(\delta)\); their Jacobian magnitudes equal \(p(t)\). Invariance gives the exact equation
\[
h(1-\delta)=\frac{h(c-t(\delta))+h(c+t(\delta))}{\vartheta+A(1+\beta)t(\delta)^\beta}.
\]
By continuity at \(c\) and \(h(c)>0\), the numerator tends to \(2h(c)>0\). As \(\beta<0\), the denominator is asymptotic to \(A(1+\beta)t^\beta\). Substitution yields
\[
h(1-\delta)\sim\frac{2h(c)}{(1+\beta)A^{1/(1+\beta)}}\,\delta^{-\beta/(1+\beta)}.
\]
This proves the claimed nonzero limit and shows \(h(1-)=0\), with exact exponent \(0<\gamma<1\).

**4. Sharp loss of second Sobolev regularity.** Every \(W^{2,1}(0,1)\) function has a representative with continuously differentiable first derivative up to the endpoints. Such a representative vanishing at \(x=1\) must obey \(|h(1-\delta)|\le C\delta\) for sufficiently small \(\delta\). The positive limit above instead implies \(h(1-\delta)/\delta\asymp\delta^{\gamma-1}\to\infty\). Contradiction. Consequently \(h\notin W^{2,1}(0,1)\). Reference [1], Proposition 4.2, proves \(W^{2,1}\) at \(\beta=-1/2\) for its critical specialization, so the boundary is sharp from the upper side.

## Verification
The included script `verify.py` reproduces the inverse-branch algebra at representative exact exponents and checks the positive normalized endpoint transfer coefficient using high-precision root finding. It tests only finite instances of the local formula for \(P1\). The universal assertions, continuity and positive density value are established analytically above, not by numerical sampling.

## Relationship to prior work
Reference [1] supplies the critical \(\beta=-1/2\) family, transfer-operator formulation, and the positive \(W^{2,1}\) endpoint theorem; it does not treat \(-1/2<\beta<0\). Reference [2] develops the full parameterized family and \(W^{2,1}\) regularity for \(-1<\beta<-1/2\), not the present upper interval. Reference [3] studies deterministic cusp response for a stronger-singularity range excluding the present interval. The new result is the exact positive density-power law on the opposite side and the resulting necessity of the critical threshold, not the established existence of the invariant measure or the critical regularity theorem. Earlier general existence results for cusp maps are compatible with, but do not supply, the displayed exponent and coefficient.

## Limitations
This concerns a specific two-full-branch one-dimensional family with cusp image at the boundary, not general interior-cusp-value maps. It proves a one-sided exact boundary asymptotic and failure of \(W^{2,1}\), not a global optimal fractional-Sobolev scale, a mixing rate, or a response formula. Historical novelty remains provisional, especially because the entire text of reference [2] could not be inspected; its verified stated theorem range is disjoint. No independent audit has been performed.

## References
[1] D. Oltiboev and F. Vafoyev, *Critical cusp cancellation and analytic response for a Bernoulli random interval map*, arXiv:2610.23180v1 (public October 16, 2026), Sections 2–5. https://arxiv.org/abs/2610.23180

[2] D. Oltiboev, K. Rakhimov, and M. Ruziboev, *Linear response for random systems with a cusp*, arXiv:2608.26969v1 (public August 27, 2026), theorem scope \(-1<\beta<-1/2\). https://arxiv.org/abs/2608.26969

[3] D. Oltiboev, *Linear response for systems with a cusp*, arXiv:2505.17462v1 (public May 23, 2025), theorem scope \(\beta<(1-2p)/(2p)\) for \(p>1\). https://arxiv.org/abs/2505.17462

[4] M. Rychlik, *Bounded variation and invariant measures*, Studia Mathematica 76 (1983), 69–80.
