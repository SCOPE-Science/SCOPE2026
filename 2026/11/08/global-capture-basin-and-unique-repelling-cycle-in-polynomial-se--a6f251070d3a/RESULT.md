# Global capture basin and unique repelling cycle in polynomial sewed-focus flows

## Finding
For every integer \(k\ge2\), the specific global polynomial crossing flow described below has a **complete three-way forward-orbit classification**: finite-time capture at the origin inside one bounded Jordan oval, exactly one nonconstant periodic orbit on that oval, and escape to spatial infinity outside. The boundary orbit has least period \(4\) and transverse Poincaré multiplier \(4\). The exact area of the finite-time capture basin is
\[
\mathcal A_k=4-\frac{2}{2k+1}-\frac{2}{4k+1}.
\]
The explicit local polynomial sewed-focus family and its small-radius intersection map come from [1]; the global basin, unique boundary orbit, transverse multiplier and exact basin area are the additional findings here.

## Assumptions and scope
Let \(k\in\mathbb Z\) satisfy \(k\ge2\), and define nonnegative potentials on the whole real axis:
\[
\begin{aligned}
\psi_+(x)&=\begin{cases}(-x)^{4k},&x\le0,\\x^{2k},&x\ge0,\end{cases}\\
\psi_-(x)&=\begin{cases}(-x)^{2k},&x\le0,\\x^{4k},&x\ge0.\end{cases}
\end{aligned}
\]
In the open upper half-plane the vector field is \((\dot x,\dot y)=(1,-\psi_+'(x))\); in the open lower half-plane it is \((-1,-\psi_-'(x))\). At \((x,0)\) with \(x\ne0\), follow the unique transverse crossing of the switching axis. At the origin the absorbing forward continuation is stipulated. These crossing conventions are part of the statement, not a conclusion about all possible generalized solutions at that singularity.

Define the open oval interior \(B_k\) explicitly as
\[
\begin{aligned}
 B_k={}&\{(x,y):y>0,\ y+\psi_+(x)<1\}\\
 &\cup\{(x,y):y<0,\ -y+\psi_-(x)<1\}\\
 &\cup\{(x,0):-1<x<1\}.
\end{aligned}
\]
Its boundary \(\Gamma_k\) consists of the two graphs \(y=1-\psi_+(x)\) and \(y=\psi_-(x)-1\) for \(-1\le x\le1\), each restricted to its respective half-plane, joined at \((\pm1,0)\). Both potentials vanish at zero and increase strictly away from zero on each half-axis.

## Proof
**1. Integral arcs and global first crossings.** Along upper-half-plane solutions, \(C_+=y+\psi_+(x)>0\) is constant, and \(x\) increases at speed one. Along lower-half-plane solutions, \(C_-=-y+\psi_-(x)>0\) is constant, and \(x\) decreases at speed one. Because each potential is strictly monotone on each half-axis and tends to infinity at infinity, every orbit segment starting in either open half-plane reaches a unique next transverse crossing in finite time: from above it crosses at \((C_+^{1/(2k)},0)\), and from below it crosses at \((-C_-^{1/(2k)},0)\). At nonzero switching-axis points, both transverse components have the same nonzero sign (positive for \(x<0\), negative for \(x>0\)), so there is no sliding or ambiguity in the forward crossing.

**2. Exact return dynamics.** For any \(r>0\), the upper arc from \((-r,0)\) has level \(C_+=r^{4k}\) and next meets the axis at \((r^2,0)\). The following lower arc has level \(C_-=r^{8k}\) and meets at \((-r^4,0)\). Thus the full first-return map on the negative switching ray, in its positive radius coordinate, is
\[
\mathcal R(r)=r^4,\qquad r>0.
\]
It has precisely one positive periodic radius: \(r=1\). Indeed every positive periodic point of \(r\mapsto r^4\) satisfies \(r^{4^n}=r\) for some positive integer \(n\), hence \(r=1\). There are no nonconstant orbits avoiding the switching line, since upper arcs have strictly increasing \(x\), and lower arcs strictly decreasing \(x\). Therefore the only nonconstant periodic orbit is \(\Gamma_k\), which traverses from \((-1,0)\) to \((1,0)\) in time \(2\) above, then returns in time \(2\) below. Its least period is \(4\). The transverse multiplier is \(\mathcal R'(1)=4\), so it is repelling.

**3. Complete finite-time capture and escape.** When \(0<r<1\), successive switching radii are \(r,r^2,r^4,r^8,\ldots\), tending to zero; from the first negative-ray crossing their total remaining travel time is exactly
\[
T(r)=r+2\sum_{j=1}^{\infty}r^{2^j}<\infty.
\]
The series converges because its terms are bounded by ordinary geometric powers of \(r\). Its vanishing endpoint is the origin, so the stipulated absorbing continuation applies. Any point of \(B_k\) reaches a switching-axis point of radius smaller than one after at most one finite half-plane arc, hence reaches the origin in finite time. Conversely, if \(r>1\) then \(r^{4^n}\to+\infty\). Along each ensuing half-plane excursion its conserved positive level tends to infinity, so whenever \(|x|\) remains bounded, \(|y|\) tends to infinity; whenever \(|x|\) is unbounded the Euclidean norm is already large. This proves the orbit norm tends to infinity, not merely that a subsequence of switching crossings escapes. There is no finite-time blowup: \(|\dot x|=1\) away from the absorbing origin, hence \(|x(t)|\le |x(0)|+t\); the polynomial expression for \(\dot y\) then remains bounded on every finite time interval. A starting point outside \(\overline{B_k}\) gives a first-crossing radius greater than one, proving complete exterior escape. Boundary data give the unique periodic oval.

**4. Exact basin area.** The upper boundary is \(y=1-\psi_+(x)\) and lower boundary is \(y=\psi_-(x)-1\) for \(-1\le x\le1\). The upper area is \(\int_0^1(1-t^{2k})\,dt+\int_0^1(1-t^{4k})\,dt\), and reflection shows that the lower area is identical. Hence
\[
\operatorname{Leb}_2(B_k)=2\left(\frac{2k}{2k+1}+\frac{4k}{4k+1}\right)=4-\frac2{2k+1}-\frac2{4k+1}.
\]
For the original example \(k=2\), the area is exactly \(152/45\). It increases strictly with integer \(k\) and tends to \(4\), quantifying the basin geometry across increasing smoothness orders.

## Verification
The companion `CHECKER.py` reproduces exact algebraic arc integrals, both switching maps, the monotonic return regimes, and the rational area formula for integers \(2\le k\le15\) using `fractions.Fraction`; executing it yields `PIECEWISE_FOCUS_EXACT_IDENTITIES_OK 742`. Supplemental numerical event integration for \(k=2,3,5\) and initial negative radii \(0.5,0.85,1,1.2\) reproduced the positive crossing radius \(r^2\) to solver tolerance. The all-parameter and infinite-trajectory conclusions are proved above; the finite checks are supplementary.

## Relationship to prior work
Glendinning, Hogan, Homer, Jeffrey and Szalai [1, Sect. 3, Eq. (13)–(15)] introduce the \(k=2\) polynomial sewed focus and show **local** finite-time approach through the crossings \(r\mapsto r^2\), and explicitly describe higher-power substitutions. They do not state a complete global forward partition of the plane, a unique global periodic boundary, its transverse multiplier, or a Lebesgue-area formula for the basin. Their later classification [2, Appendix B] reproduces the local polynomial calculation and classifies local Filippov type-3 singularities, again without the global basin geometry. These first-return identities are taken as known ingredients, not asserted as novel. A search for equivalent global oval and basin-area laws found no covering published account in the inspected sources.

## Limitations
This is a global result for the **specific** polynomial crossing family and the specified absorbing convention at the origin. It neither classifies arbitrary Filippov systems nor implies stability or invariance under all regularizations of the switch. The negative result of finding no covering literature is not a proof of publication priority; unindexed equivalent work remains a possibility. The exact proof is analytical; the checker cannot certify every real trajectory by finite computation. Independent mathematical validation has not been performed.

## References
[1] P. Glendinning, S. J. Hogan, M. Homer, M. R. Jeffrey and R. Szalai, *Uncountably Many Cases of Filippov’s Sewed Focus*, Journal of Nonlinear Science 33, article 52 (first published 2023-05-05). DOI: `10.1007/s00332-023-09910-4`; arXiv: `2306.09743`.

[2] P. Glendinning, S. J. Hogan, M. E. Homer, M. R. Jeffrey and R. Szalai, *Classification of Filippov Type 3 Singular Points in Planar Bimodal Piecewise Smooth Systems*, SIAM Journal on Applied Dynamical Systems 23 (2024), 2242–2261. DOI: `10.1137/23M1622842`, especially Appendix B (open accepted manuscript available via the University of Manchester).
