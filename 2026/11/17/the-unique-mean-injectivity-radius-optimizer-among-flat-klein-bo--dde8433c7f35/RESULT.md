# The unique mean-injectivity-radius optimizer among flat Klein bottles

## Finding

For positive lengths \(L,H\), let \(K(L,H)\) be the flat Klein bottle obtained from \(\mathbb R^2\) by the fixed-point-free deck transformations
\[
a(x,y)=(x+L,y),\qquad b(x,y)=(-x,y+H).
\]
Its area is \(A=LH\) and its similarity parameter is \(q=L/H\). For each point \(p\), let \(\operatorname{inj}(p)\) be the Riemannian injectivity radius, equivalently the maximal radius of an embedded geodesic disk centered at \(p\). The scale-invariant *mean injectivity radius* is
\[
\mathcal M(q)=\frac{1}{A^{3/2}}\int_{K(L,H)}\operatorname{inj}(p)\,dA(p).
\]

**Theorem (sharp metric optimizer).** Among all flat Riemannian Klein bottles of any fixed area, \(\mathcal M\) has exactly one maximizer up to isometry. Its parameter \(q_*\in(1,2/\sqrt3)\) is the unique solution of
\[
q_*^2-q_*\sqrt{q_*^2-1}-3\operatorname{arcosh}(q_*)=0.
\]
Numerically, \(q_*=1.0352663712132635\ldots\) and the sharp normalized maximum is
\[
\mathcal M(q_*)=0.5027812352805047\ldots.
\]
In particular, the square flat Klein bottle \(q=1\), although optimal for the normalized systole, is **not** optimal for the mean pointwise injectivity radius: \(\mathcal M(1)=1/2<\mathcal M(q_*)\).

An explicit area-normalized pointwise distribution supplies the proof. Let \(P\) be area-uniform on \(K(L,H)\), put \(Y=2\operatorname{inj}(P)/\sqrt A\), and let \(U\) be uniform on \([0,q/2]\). Then
\[
Y\ \stackrel{d}=\ \frac{1}{\sqrt q}\min\{q,2,\sqrt{1+U^2}\}.
\]
This distributional expression follows from known deck-displacement geometry; it is a supporting lemma, **not** an assertion of novelty for the pointwise formula.

## Assumptions and scope

All parameters \(L,H\) are strictly positive. The quotient is smooth, closed, connected, flat, and nonorientable; the deck action is free. The metric is the intrinsic Euclidean quotient metric, not an immersion metric of a self-intersecting picture in three-space. The parameters are geometric: the translation perpendicular to glide axes has length \(L\), while a primitive glide has axial displacement \(H\). Every flat Klein bottle is isometric to one of these quotients. Area-normalized mean injectivity radius is unchanged by simultaneous rescaling of \(L,H\). All probability statements concern the area measure on the quotient, with no distribution imposed on metrics.

## Proof

**1. Exact pointwise injectivity radius.** On a complete flat quotient without conjugate points, the injectivity radius at \([p]\) equals half the smallest Euclidean displacement \(\lVert \gamma p-p\rVert\) over nonidentity deck transformations. Every even power of the glide, composed with a translation, displaces by a vector \((kL,2mH)\); its smallest nonzero norm is \(\min\{L,2H\}\). Every odd glide image of \((x,y)\) differs in the horizontal coordinate by \(kL-2x\) and in the vertical coordinate by an odd multiple of \(H\). Its smallest displacement is \(\sqrt{H^2+\delta(x)^2}\), where
\[
\delta(x)=\operatorname{dist}(2x,L\mathbb Z).
\]
Consequently
\[
2\operatorname{inj}([x,y])=\min\{L,2H,\sqrt{H^2+\delta(x)^2}\}.
\]
The quotient has a fundamental rectangle of dimensions \(L\) and \(H\). Under area-uniform sampling, \(x\) is uniform modulo \(L\), so \(\delta(x)/H\) is uniform on \([0,q/2]\). This proves the displayed distribution of \(Y\) by dividing by \(\sqrt{LH}\).

**2. Exact mean profile.** For \(q>0\), set \(c(q)=\min\{q,2\}\). Integrating the preceding uniform variable yields
\[
\mathcal M(q)=q^{-3/2}\int_0^{q/2}\min\{c(q),\sqrt{1+u^2}\}\,du.
\]
The crossover \(\sqrt{c(q)^2-1}=q/2\), when meaningful, occurs at \(q=2/\sqrt3\) for \(1<q\le2\), and at \(q=2\sqrt3\) for \(q\ge2\). Elementary integration therefore gives the complete continuous profile
\[
\mathcal M(q)=
\begin{cases}
\dfrac{\sqrt q}{2},&0<q\le1,\\[4pt]
\dfrac{q^2-q\sqrt{q^2-1}+\operatorname{arcosh}q}{2q^{3/2}},&1<q<2/\sqrt3,\\[6pt]
\dfrac{(q/2)\sqrt{1+q^2/4}+\operatorname{arsinh}(q/2)}{2q^{3/2}},&2/\sqrt3\le q\le2\sqrt3,\\[6pt]
\dfrac{q-\sqrt3+\tfrac12\operatorname{arsinh}\sqrt3}{q^{3/2}},&q>2\sqrt3.
\end{cases}
\]
Here \(\operatorname{arcosh}q=\log(q+\sqrt{q^2-1})\) and \(\operatorname{arsinh}u=\log(u+\sqrt{1+u^2})\). The piecewise formulas agree at each boundary.

**3. Strict global maximization.** On \((0,1]\), the profile is strictly increasing. On \((1,2/\sqrt3)\), the derivative has the sign of
\[
\Psi(q)=q^2-q\sqrt{q^2-1}-3\operatorname{arcosh}q.
\]
Indeed \(\mathcal M'(q)=\Psi(q)/(4q^{5/2})\), and
\[
\Psi'(q)=2\left(q-\frac{q^2+1}{\sqrt{q^2-1}}\right)<0.
\]
Also \(\lim_{q\downarrow1}\Psi(q)=1\) and \(\Psi(2/\sqrt3)=2/3-3\log\sqrt3<0\). Thus exactly one zero \(q_*\) exists in this interval; the profile increases before it and decreases afterward up to \(2/\sqrt3\).

For \(2/\sqrt3\le q\le2\sqrt3\), writing \(t=q/2\) shows that the sign of \(\mathcal M'(q)\) is that of \(h(t)=t\sqrt{1+t^2}-3\operatorname{arsinh}t\), on \([1/\sqrt3,\sqrt3]\). Now
\[
h'(t)=\frac{2(t^2-1)}{\sqrt{1+t^2}},\quad h(0)=0,\quad
h(\sqrt3)=2\sqrt3-3\log(2+\sqrt3)<0.
\]
The last inequality follows from \(\log(2+\sqrt3)=2\operatorname{artanh}(1/\sqrt3)>2/\sqrt3\). Thus \(h(t)<0\) on the entire stated interval: it decreases up to \(t=1\), then increases but remains negative at \(\sqrt3\).

For \(q\ge2\sqrt3\), write \(C=\sqrt3-\tfrac12\log(2+\sqrt3)\), so that \(\mathcal M(q)=(q-C)q^{-3/2}\). Its derivative is \(\tfrac12(3C-q)q^{-5/2}<0\), since \(3C<2\sqrt3\) by the same strict logarithmic inequality. Therefore \(q_*\) is the **unique global maximizer** on all \(q>0\). Equality of the optimal bound characterizes its similarity class and, at fixed area, a unique isometry class. \(\square\)

## Verification

The proof is analytic. A standalone numerical checker is included at `scripts/klein_injectivity_checks.py`. It directly enumerates nonidentity deck images (independently from the closed pointwise expression), verifies the uniform-coordinate law across thirteen metric ratios, checks the mean against independent quadrature, compares empirical CDFs at continuity thresholds, and locates the unique critical root. Run using Python 3 with NumPy and SciPy: `python scripts/klein_injectivity_checks.py`. Successful output begins with `FLAT_KLEIN_INJECTIVITY_LAW_CHECKS_OK`.

## Relationship to prior work

The standard flat Klein-bottle quotient and its systolic geometric classes appear explicitly in El Mir and Yassine (arXiv:1209.6202v1, Section 1.1, posted 27 September 2012). Eyll (2025, Section 2) gives the same quotient framework and studies stability of *systolic* inequalities. Sabourau (arXiv:2606.06777v1, Section 6.4 and Proposition 6.18, posted 4 June 2026) already derives the *pointwise shortest-deck displacement* for flat Klein bottles and optimizes the radius of **one largest** embedded disk. The present theorem does not claim a new pointwise formula or merely its one-dimensional pushforward. Instead it optimizes the **area average** over the entire manifold, obtaining a different, uniquely nonsquare optimizer; the pointwise result by itself does not state this sharp mean theorem. Katz and Sabourau (2026, Theorem A) prove the square flat Klein bottle is uniquely *systolic* among nonpositively curved non-tori; this optimizes a different, worst-case geometric invariant.

## Limitations

Only smooth intrinsically flat Klein-bottle metrics are covered. No optimality is claimed among all smooth metrics, conformal changes, Finsler metrics, or nonpositively curved metrics. The pointwise injectivity-radius expression is known from the cited deck analysis; the independent mathematical claim here is the exact unique **area-normalized mean** optimizer and its sharp value. The root digits are numerical illustrations, not independent certificates. The checker tests finitely many parameters and does not prove the analytic inequalities. Historical priority of the exact mean optimization remains subject to independent scholarly checking.

## References

1. C. El Mir and Z. Yassine, *Conformal Geometric Inequalities on the Klein Bottle*, arXiv:1209.6202v1, posted 2012-09-27, https://arxiv.org/html/1209.6202v1, especially Section 1.1.
2. J. Eyll, *Stability of Systolic Inequalities for the Möbius Strip and Klein Bottle*, Journal of Geometric Analysis 35 (2025), article 365, https://doi.org/10.1007/s12220-025-02197-9, especially Section 2.
3. S. Sabourau, *Systole, inradius and rigidity of cusped hyperbolic 3-manifolds*, arXiv:2606.06777v1, posted 2026-06-04, https://arxiv.org/abs/2606.06777, especially Section 6.4, Proposition 6.18.
4. M. G. Katz and S. Sabourau, *Klein bottle and optimal systolic inequality for nonpositively curved surfaces*, Annals of Global Analysis and Geometry 70 (2026), article 11, https://doi.org/10.1007/s10455-026-10057-0, especially Theorem A.
