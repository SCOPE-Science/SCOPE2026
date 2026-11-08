# Exact illumination-area profile and saturation for planar disks under ball convexity

## Finding

Fix \(0<r<R\), let \(B_2^2\) be the closed Euclidean unit disk, and put \(K=rB_2^2\). The complete finite-scale area response of the radius-\(R\) ball hull of \(K\) and an illuminating point, and the resulting unweighted illumination bodies, have explicit forms.

Set \(a=R-r\) and \(s_*=2R-r\). For \(r\le s\le s_*\), define
\[
\theta(s)=\arccos\!\left(\frac{s^2+a^2-R^2}{2as}\right),\qquad
\phi(s)=\operatorname{atan2}\!\left(a\sin\theta(s),s-a\cos\theta(s)\right).
\]
At the endpoints these angles are interpreted continuously, so \(\theta(r)=\pi\), \(\theta(s_*)=0\), and \(\phi(r)=\phi(s_*)=0\). The hull area is
\[
 A(s):=|[K,se_1]_R|
 =R^2\bigl(\pi-\theta(s)-\phi(s)\bigr)
  +r^2\theta(s)-as\sin\theta(s).
\]
It is strictly increasing from \(A(r)=\pi r^2\) to \(A(s_*)=\pi R^2\).

For the unweighted illumination family
\[
 I_R^\delta(K)=\{x\in\mathbb R^2:|[K,x]_R\setminus K|\le\delta\},\qquad\delta\ge0,
\]
let \(\delta_*=\pi(R^2-r^2)\). Its exact global profile is
\[
 I_R^\delta(K)=
 \begin{cases}
 A^{-1}(\pi r^2+\delta)\,B_2^2,&0\le\delta<\delta_*,\\
 (2R-r)B_2^2,&\delta\ge\delta_*.
 \end{cases}
\]
The inverse is the ordinary inverse of the strictly increasing function \(A\) on \([r,s_*]\). For \(\delta\ge\delta_*\), the body has saturated rather than expanding further. The sharp radius-\(R\) ball-convexity threshold is
\[
 \delta_c=A(R)-\pi r^2,\qquad 0<\delta_c<\delta_*;
 \quad I_R^\delta(K)\text{ is radius-}R\text{ ball convex iff }\delta\le\delta_c.
\]
The two opposite endpoint asymptotics, for \(\epsilon\downarrow0\), are
\[
 A(r+\epsilon)-\pi r^2
 =\frac{2\sqrt2}{3}\sqrt{\frac{Rr}{R-r}}\,\epsilon^{3/2}
 +O_{R,r}(\epsilon^{5/2}),
\]
\[
 \pi R^2-A(s_*-\epsilon)
 =4R\sqrt{\frac{2R(R-r)}{2R-r}}\,\epsilon^{1/2}
 +O_{R,r}(\epsilon^{3/2}).
\]
In particular, with \(\rho(\delta)\) denoting the illumination body's radius,
\[
 s_*-\rho(\delta)\sim
 \frac{2R-r}{32R^3(R-r)}(\delta_*-\delta)^2
 \quad(\delta\uparrow\delta_*).
\]

## Assumptions and scope

Every area is planar Lebesgue measure. For any nonempty set \(S\subset\mathbb R^2\) write
\[
 [S]_R:=\bigcap\{B_2^2(c,R):S\subseteq B_2^2(c,R)\}.
\]
The intersection of an empty family is the whole plane, whose area is infinite. Thus points \(x\) for which no radius-\(R\) disk contains \(K\cup\{x\}\) never enter finite-volume illumination sublevels. The theorem assumes strictly \(0<r<R\); the singular full-radius limit \(r=R\) is excluded. The center is zero; translation and rotation invariance give the corresponding statement for arbitrary disk centers and illuminating directions.

## Proof

**1. Feasible centers and admissible points.** A radius-\(R\) disk contains \(K\) exactly when its center \(c\) satisfies \(\|c\|_2\le a\). With \(x=se_1\), the centers of disks containing \(K\cup\{x\}\) consequently form
\[
 C_s=B_2^2(0,a)\cap B_2^2(se_1,R).
\]
For \(s\ge r\), this set is nonempty precisely when \(s\le s_*\); for \(s>s_*\) the hull is the whole plane by the specified convention. At \(s=r\), the point is already in \(K\), giving hull \(K\). For \(r<s<s_*\), the two circles bounding \(C_s\) meet at centers
\[
 c_\pm=a(\cos\theta,\pm\sin\theta),
 \qquad \cos\theta=\frac{s^2+a^2-R^2}{2as}.
\]
The disks centered at \(c_\pm\) both contain \(K\) and \(x\).

**2. Determine the entire hull boundary.** Set
\[
 T_\pm=r(-\cos\theta,\pm\sin\theta).
\]
The disk centered at \(c_-\) passes through \(x\) and \(T_+\), and is externally tangent there to the boundary of \(K\); the disk centered at \(c_+\) has the analogous lower tangency. The short arcs of these two radius-\(R\) circles from \(x\) to the respective \(T_\pm\) belong to the radius-\(R\) spindles of their endpoints. Here is a direct proof of the two-point spindle fact used. Translate and rotate two arbitrary endpoints to \((\pm d/2,0)\) with \(0<d\le2R\), and put \(h=\sqrt{R^2-d^2/4}\). Every feasible center \((\xi,\eta)\) satisfies \(\xi^2+\eta^2+d|\xi|\le h^2\). Every point \((u,v)\) in the lens of disks centered at \((0,\pm h)\) satisfies \(|u|\le d/2\) and \(u^2+v^2+2h|v|\le d^2/4\). Consequently, for every such center and point,
\[
 \|(u,v)-(\xi,\eta)\|_2^2
 \le u^2+v^2+h^2-d|\xi|-2u\xi-2v\eta
 \le u^2+v^2+h^2+2h|v|\le R^2.
\]
The two disks centered at \((0,\pm h)\) are themselves feasible, so their intersection is exactly the two-point radius-\(R\) spindle. Thus every disk containing the endpoint pair contains each of the two spindle arcs. Every feasible disk for \(K\cup\{x\}\) contains both pairs and the disk \(K\). The two outer arcs join the inner circle tangentially at \(T_\pm\); at \(x\) the outward normals span the positive corner angle \(2\phi\). Along the three arcs the outward normal turns monotonically, so this boundary encloses a convex region \(Q_s\). It is the convex hull of the three boundary arcs, two of which belong to the spindles and one to \(K\). Thus \(Q_s\subseteq[K,x]_R\).

Conversely, on either outer arc the corresponding feasible radius-\(R\) disk supplies a supporting circle and hence its supporting halfplane. At every point \(ru\) on the opposite arc of \(\partial K\), the radius-\(R\) disk centered at \(-au\) contains both \(K\) and \(x\), since \(\langle u,e_1\rangle\le-\cos\theta\). It supplies the tangent supporting halfplane at \(ru\). At the corner \(x\), supporting normals between the two limiting arc normals are their nonnegative linear combinations, so the two corresponding feasible-disk tangent halfplanes suffice there. Hence the supporting halfplanes of the three arcs and corner contain the hull; intersecting these halfplanes gives \([K,x]_R\subseteq Q_s\). Thus the three-arc description is exact, including the two limiting cases by continuity.

**3. Exact area.** Orient \(\partial Q_s\) counterclockwise, first along the upper radius-\(R\) arc, then the opposing radius-\(r\) arc, then the lower radius-\(R\) arc. Both outer arcs turn by \(\psi=\pi-\theta-\phi\), with \(\phi=\operatorname{atan2}(a\sin\theta,s-a\cos\theta)\), whereas the inner arc turns by \(2\theta\). For a counterclockwise circle arc from \(p\) to \(q\) with center \(c\), radius \(t\), and angle change \(\gamma\), Green's theorem gives the signed-area contribution \(\frac12(t^2\gamma+\det(c,q-p))\). Applying this to the three arcs yields
\[
 |Q_s|=R^2\psi+r^2\theta-as\sin\theta=A(s).
\]
The endpoint areas are \(\pi r^2\) and \(\pi R^2\).

**4. Strict monotonicity and illumination threshold.** If \(r\le s_1<s_2\le s_*\), the convex hull \([K,s_2e_1]_R\) contains the segment from the origin to \(s_2e_1\), hence contains \(s_1e_1\). Monotonicity of the hull operator gives \([K,s_1e_1]_R\subseteq[K,s_2e_1]_R\). The feasible radius-\(R\) disk centered at \((s_1-R)e_1\) has rightmost coordinate \(s_1\), so the smaller hull is contained in the halfplane with first coordinate at most \(s_1\), whereas the larger hull contains \(s_2e_1\) and has nonempty interior. Its area is therefore strictly larger. Rotation invariance makes the illumination body a centered disk with the stated inverse profile. A Euclidean centered disk of radius \(t>0\) is radius-\(R\) ball convex exactly when \(t\le R\): when \(t\le R\), it is the intersection of all radius-\(R\) disks containing it; when \(t>R\), no such disk contains it. Since \(r<R<s_*\), its phase change is at \(\delta_c=A(R)-\pi r^2\).

**5. The two endpoint expansions.** For the inner endpoint write \(h=\pi-\theta\). The cosine rule can be solved exactly as
\[
 s=-a\cos h+\sqrt{R^2-a^2\sin^2h},\qquad
 \phi=\arcsin\left(\frac aR\sin h\right).
\]
Therefore, as \(h\downarrow0\),
\[
 s-r=\frac{ar}{2R}h^2+O_{R,r}(h^4),\quad
 \phi=\frac aR h+\frac{(a/R)^3-a/R}{6}h^3+O_{R,r}(h^5).
\]
Substituting into the area expression and cancelling the linear terms yields the sharper intermediate identity
\[
 A(s)-\pi r^2=\frac{ar^2}{3R}h^3+O_{R,r}(h^5).
\]
Replacing \(h\) by \(\sqrt{2R/(ar)}\sqrt{s-r}+O_{R,r}((s-r)^{3/2})\) proves the displayed inner coefficient with error \(O_{R,r}((s-r)^{5/2})\).

At the other endpoint write \(t=\theta\downarrow0\). The same cosine rule instead gives
\[
 s=a\cos t+\sqrt{R^2-a^2\sin^2t}
 =s_*-\frac{as_*}{2R}t^2+O_{R,r}(t^4),
 \qquad \phi=\frac aR t+O_{R,r}(t^3).
\]
The area gap is consequently
\[
 \pi R^2-A(s)=4Ra\,t+O_{R,r}(t^3)
 =4R\sqrt{\frac{2Ra}{s_*}}\,\sqrt{s_*-s}+O_{R,r}((s_*-s)^{3/2}).
\]
Squaring the inverse relation yields the asserted quadratic saturation coefficient. All asymptotics hold for each fixed pair \(0<r<R\); no uniformity near \(r=0\) or \(r=R\) is asserted.

## Verification

The supplementary standalone Python 3 standard-library program `verify.py` checks monotonicity, endpoint normalization, both asymptotic leading coefficients and 25 interior hull areas against independently sampled feasible-center radial integrations. It also checks random admissible parameters. It reports `PASS 2050 numeric supplementary checks; direct sampled-center radial integration in 25 nontrivial cases`. Finite numerical samples are only consistency checks: the proof above establishes the continuously quantified statements.

## Relationship to prior work

Oliva, Werner and Yalikun (2026, arXiv:2607.13714) define ball-convex illumination bodies and prove general convexity and small-scale relative-affine-surface-area asymptotics. Their planar isoperimetric theorem uses disks as comparison objects, but their stated results do not supply this disk's complete finite-scale point-hull area, the exact global inverse profile, finite-level saturation, or the sharp ball-convexity threshold. The leading inner exponent is consistent with their general asymptotic theory, and is not claimed as a new exponent. Lángi, Naszódi and Talata (2011, arXiv:1110.4823) establish the two-point spindle and ball-convexity framework used in the boundary argument. Artstein-Avidan and Florentin (2025, arXiv:2505.09200) provide general ball-body background. The novelty claimed is the explicit global coupled profile and its sharp transitions, not the definitions, the elementary spindle construction, or general illumination convexity.

## Limitations

This theorem is restricted to the plane, concentric Euclidean disk input, and unweighted radius-\(R\) hulls with \(0<r<R\). It does not classify all initial ball-convex bodies or weights. Saturation uses the explicit convention that an empty intersection of containing disks is the full plane and has infinite area; other conventions for infeasible configurations may lead to differently defined objects. At the singular endpoint \(r=R\), the analysis is not asserted. Historical novelty is best-knowledge provisional: an equivalent older finite-scale disk computation could exist under different terminology. No independent mathematical audit has been performed.

## References

- B. Oliva, E. M. Werner, D. Yalikun, *Illumination bodies for ball-convex bodies*, arXiv:2607.13714 (first posted 2026-07-15), https://arxiv.org/abs/2607.13714.
- Z. Lángi, M. Naszódi, I. Talata, *Ball and Spindle Convexity with respect to a Convex Body*, arXiv:1110.4823 (2011), https://arxiv.org/abs/1110.4823.
- S. Artstein-Avidan and D. Florentin, *An in-depth study of ball-bodies*, arXiv:2505.09200 (2025), https://arxiv.org/abs/2505.09200.
