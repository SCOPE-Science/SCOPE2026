# Singular near-minimum width crossover for two separated orthogonal disks

## Finding
Let \(D_-(\delta)\subset\mathbb R^3\) be the filled unit disk \(z=0,\ x^2+(y+\delta/2)^2\le1\), let \(D_+(\delta)\) be the filled unit disk \(x=0,\ (y-\delta/2)^2+z^2\le1\), and set \(K_\delta=\operatorname{conv}(D_-(\delta)\cup D_+(\delta))\), \(\delta\ge0\). Choose a uniform unit direction \(U\in S^2\) and let \(W_\delta\) be the Euclidean width of \(K_\delta\) in direction \(U\). For every \(\delta\ge0\), the minimum width is \(\sqrt2\), attained precisely in the four directions \((\pm1/\sqrt2,0,\pm1/\sqrt2)\). The maximum width is \(2+\delta\); for \(\delta>0\) the only maximizing directions are \((0,\pm1,0)\).

For every fixed \(\delta>0\), as \(\varepsilon\downarrow0\),
\[
\Pr\{W_\delta<\sqrt2+\varepsilon\}
=\frac{2\sqrt2}{\pi\delta}\varepsilon^2+o_\delta(\varepsilon^2).
\]
At coincident centers, the exponent changes:
\[
\Pr\{W_0<\sqrt2+\varepsilon\}
=\frac{4\,2^{3/4}}{3\pi}\varepsilon^{3/2}+o(\varepsilon^{3/2}).
\]
The singularity has the following *uniform critical-window law*. If \(\delta=\lambda\sqrt\varepsilon\), then, locally uniformly for \(0\le\lambda<\infty\),
\[
\frac{\Pr\{W_{\lambda\sqrt\varepsilon}<\sqrt2+\varepsilon\}}{\varepsilon^{3/2}}
\longrightarrow F(\lambda)
:=\frac2\pi\left(\sqrt2\,u_\lambda-\frac{u_\lambda^3}{3}\right),\qquad
u_\lambda=\frac{\sqrt{\lambda^2+2\sqrt2}-\lambda}{\sqrt2}.
\]
The profile satisfies \(F(0)=4\,2^{3/4}/(3\pi)\), decreases strictly for \(\lambda>0\), and \(F(\lambda)\sim2\sqrt2/(\pi\lambda)\) as \(\lambda\to\infty\). Thus its two ends match the coincident-center and the positive-separation exponents.

There is also a conditional angular scaling law. Write \(U=(X,Y,Z)\), set \(y=|Y|\), and \(q=|X^2-Z^2|\). Under the conditioning \(W_{\lambda\sqrt\varepsilon}<\sqrt2+\varepsilon\), the pair \((y/\sqrt\varepsilon,q/\varepsilon)\) converges to normalized uniform planar Lebesgue measure on
\[
\Omega_\lambda=\left\{(v,s)\in\mathbb R_{\ge0}^2:
\frac{v^2}{\sqrt2}+\max\left(\frac{s}{\sqrt2},\lambda v\right)<1\right\}.
\]
For fixed \(\delta>0\), the conditional pair \((y/\varepsilon,q/\varepsilon)\) instead converges to normalized uniform measure on \([0,1/\delta]\times[0,\sqrt2]\).

## Assumptions and scope
All widths are Euclidean distances between support planes. Both disks have equal unit radius, lie in exactly perpendicular planes, and have centers separated by \(\delta\) along the shared coordinate axis. The probability law is for an isotropically uniform *unoriented* or oriented direction, which give the same widths. The critical-window assertion is uniform for \(\lambda\) in each fixed bounded interval; it does not claim an error estimate uniform over all \(\lambda\ge0\). For common disk radius \(r>0\) and physical center separation \(h\), use \(\delta=h/r\) and replace \(\varepsilon\) everywhere by the physical width deficit divided by \(r\).

## Proof
**1. Exact support reduction and extrema.** For a unit vector \(u=(x,y,z)\), put \(A=\sqrt{x^2+y^2}\) and \(B=\sqrt{y^2+z^2}\). The disk support functions are \(A-\delta y/2\) and \(B+\delta y/2\). Taking both antipodal support maxima gives the exact width identity
\[
W_\delta(u)=A+B+\max\bigl(|A-B|,\delta|y|\bigr).
\]
It follows that \(W_\delta\ge2\max(A,B)\ge\sqrt{2(A^2+B^2)}=\sqrt{2(1+y^2)}\ge\sqrt2\). Equality requires \(y=0\) and \(A=B\), giving precisely the four stated directions. Also \(W_\delta=\max(2\max(A,B),A+B+\delta|y|)\le2+\delta\), with equality at the axial poles. For \(\delta>0\), equality forces \(|y|=1\), giving exactly those two poles. At \(\delta=0\), the maximum equals \(2\) along either great circle \(x=0\) or \(z=0\).

**2. Exact sampling coordinates.** Let \(y=|U_y|\in[0,1]\) and \(q=|U_x^2-U_z^2|\in[0,1-y^2]\). Spherical uniformity makes \(y\) uniform on \([0,1]\); conditional on \(y\), the transverse angle is uniform, so \(q=(1-y^2)|\cos(2\phi)|\). Thus the joint density is exactly
\[
f(y,q)=\frac2{\pi\sqrt{(1-y^2)^2-q^2}},
\qquad0<y<1,\quad0<q<1-y^2.
\]
Without loss \(A\ge B\), since the width is symmetric under interchanging them, and hence
\[
A=\sqrt{(1+y^2+q)/2},\quad
B=\sqrt{(1+y^2-q)/2},\quad
W_\delta=A+B+\max(A-B,\delta y).
\]
These formulas completely fix the probability normalization; in particular \(f(y,q)\to2/\pi\) at the unique folded minimum \((0,0)\).

**3. Uniform localization.** The lower bound from step 1 and \(2A\le W_\delta\) give, on the event \(W_\delta<\sqrt2+\varepsilon\),
\[
y^2<\sqrt2\varepsilon+\varepsilon^2/2,\qquad
q<\sqrt2\varepsilon+\varepsilon^2/2.
\]
Consequently only \(y=O(\sqrt\varepsilon)\), \(q=O(\varepsilon)\) can contribute, uniformly in \(\delta\ge0\). Taylor expansion on that region, with uniform remainders, gives
\[
A+B=\sqrt2+\frac{y^2}{\sqrt2}+O(y^4+q^2),
\qquad A-B=\frac q{\sqrt2}+O(qy^2+q^3).
\]
In the critical scaling \(y=\sqrt\varepsilon v,\ q=\varepsilon s,\ \delta=\lambda\sqrt\varepsilon\), the normalized width deficit therefore tends uniformly on bounded \((v,s,\lambda)\)-sets to
\[
\frac{W_\delta-\sqrt2}{\varepsilon}
\longrightarrow \frac{v^2}{\sqrt2}+\max(s/\sqrt2,\lambda v).
\]
The Jacobian contributes \(dy\,dq=\varepsilon^{3/2}dv\,ds\). The rescaled integration domain is uniformly bounded and each limiting boundary has planar Lebesgue measure zero. On any bounded interval of \(\lambda\), those boundaries are uniformly bounded-length arcs, so the measure of their small tubular neighborhoods tends uniformly to zero. Uniform Taylor remainders and this boundary control upgrade dominated convergence to local uniformity in \(\lambda\). The density \(f\) also gives the conditional uniform-area limit on \(\Omega_\lambda\).

**4. Evaluate the crossover area.** In the positive quadrant, at height \(v\) the allowed \(s\)-interval is \(0\le s<\sqrt2-v^2\), provided \(v^2/\sqrt2+\lambda v<1\). The endpoint is the unique positive root \(u_\lambda\) displayed above. Hence
\[
\operatorname{area}(\Omega_\lambda)=\int_0^{u_\lambda}(\sqrt2-v^2)\,dv
=\sqrt2\,u_\lambda-u_\lambda^3/3.
\]
Multiplication by the limiting sampling density \(2/\pi\) gives \(F\). Implicit differentiation of \(u_\lambda^2/\sqrt2+\lambda u_\lambda=1\) shows \(u_\lambda\) strictly decreases, while \(\sqrt2-u_\lambda^2>0\) for \(\lambda>0\); thus \(F\) strictly decreases there. Direct evaluation at zero and the expansion \(u_\lambda\sim1/\lambda\) at infinity give the endpoints.

**5. Fixed separation.** For fixed \(\delta>0\), the lower bound of step 3 improves to \(y=O_\delta(\varepsilon)\) because the width is at least \(A+B+\delta y\) and \(A+B\ge\sqrt2-O(\varepsilon^2)\) on the localized region. Put \(y=\varepsilon v\), \(q=\varepsilon s\). The normalized width deficit converges to \(\max(s/\sqrt2,\delta v)\), whose unit sublevel set is the rectangle \([0,1/\delta]\times[0,\sqrt2]\). Multiplying its area by \(2/\pi\) yields the stated positive-separation coefficient and conditional uniform rectangle. The zero-separation formula is the \(\lambda=0\) case of step 4. No finite numerical sample is used in these asymptotic proofs.

## Verification
The complete analytic identities can be checked by direct substitution. The independent diagnostic program `checks/width_tail_checker.py` computes widths both from support maxima and the folded formula, checks extrema, verifies the spherical density normalization and tests convergence of exact folded-coordinate quadratures to all displayed limiting coefficients. Its finite numerical tests are diagnostics, not a substitute for the preceding limiting argument.

## Relationship to prior work
Finch (2012) studied three hulls of perpendicular disks, their volume, surface area, and mean width, including centered and separated examples. Bäsel (first public 2016; published 2018) computed mean width and related integral geometry for the oloid, the separation-one member of this family. A published 2026 treatment of the entire separation family derives the exact pointwise directional-width identity above and strictly convex mean-width dependence on separation. **That width identity is known and not claimed as a new result here.** The new result is instead the sharp rare-direction probability, its change in exponent at coincident centers, a uniform scale-dependent crossover profile and the associated conditional angular measures. These quantitative boundary-layer statements require a localized measure analysis and are not the mean-width conclusions in those works. The 2016–17 study of convex hulls of two circles by Nash, Pir, Sottile and Ying concerns algebraic boundaries and faces, not isotropic rare-width probabilities.

## Limitations
All statements concern unit filled disks at right angles, not arbitrary planes, unequal radii or other sampling laws. No closed form for the full width distribution at every separation is claimed. Local uniformity in the crossover parameter does not imply a global uniform error bound. The published exact directional support identity means that the present result is a nontrivial new consequence of a known pointwise formula, rather than a new support-function identity. An unindexed older treatment of rare oloid widths remains a historical-priority risk.

## References
- S. R. Finch, *Convex Hull of Two Orthogonal Disks*, arXiv:1211.4514, first publicly posted 2012-11-19, https://arxiv.org/abs/1211.4514.
- U. Bäsel, *The mean width of the oloid and integral geometric applications of it*, arXiv:1604.07245, first publicly posted 2016-04-25; published as *The Mean Width and Integral Geometric Properties of the Oloid*, J. Geometry Graphics 22 (2018), 149–161, https://arxiv.org/abs/1604.07245.
- E. D. Nash, A. F. Pir, F. Sottile and L. Ying, *Convex Hull of Two Circles in R3*, arXiv:1612.09382, first publicly posted 2016-12-30, https://arxiv.org/abs/1612.09382.
- *A one-dimensional derivative law for orthogonal-disk mean width*, publicly accessible result (2026), https://github.com/published-finding corpus/2026/blob/main/2026/10/4/SCOPE-a-one-dimensional-derivative-law-for-orthogonal-disk-mean-width--6e52fbc79bdf/RESULT.md.
