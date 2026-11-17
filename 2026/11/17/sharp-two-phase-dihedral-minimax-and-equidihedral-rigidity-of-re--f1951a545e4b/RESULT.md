# Sharp two-phase dihedral minimax and equidihedral rigidity of regular bipyramids

## Finding
For every integer \(n\ge3\), among all right bipyramids with an equatorial regular \(n\)-gon and two arbitrary positive coaxial apex heights, the sharp minimum of the largest interior dihedral angle is
\[
\Phi_n^*=\pi-2\arctan\!\bigl(\sin(\pi/n)\bigr).
\]
Equality holds precisely when the two apex heights equal the base circumradius times \(\cot(\pi/n)\). At this unique similarity class all \(3n\) dihedral angles are equal. No other such bipyramid reaches the bound.

There is a complete sharper constrained optimization. Write \(s=\sin(\pi/n)\), \(c=\cos(\pi/n)\). For base circumradius \(R>0\) and heights \(h_+,h_->0\), set \(\theta_\pm=\arctan(Rc/h_\pm)\) and \(D=|\theta_+-\theta_-|\), so \(0\le D<\pi/2\). Define
\[
 z_n=\frac{\sqrt{1+8s^2}-1}{4s},\qquad D_n=2\arcsin z_n.
\]
The sharp *infimum* of the maximum interior dihedral angle among bipyramids of fixed \(D\) equals
\[
 \beta_n(D)=\begin{cases}
 \pi-2\arctan\!\dfrac{s\cos(D/2)}{1+s\sin(D/2)},&0\le D<D_n,\\[5pt]
 \pi-2\arcsin(s\cos D),&D_n\le D<\pi/2.
 \end{cases}
\]
For \(D<D_n\), the infimum is attained by a unique unordered pair of normalized apex heights, characterized by \(\theta_+=m_D+D/2\), \(\theta_-=m_D-D/2\), and \(m_D=\arctan[s\cos(D/2)/(1+s\sin(D/2))]\). For \(D\ge D_n\), the infimum is **not attained at any finite positive heights**: it is approached as the larger apex height tends to infinity. In particular, the critical value is an exact transition between existence and nonexistence of a fixed-asymmetry minimizer. Near symmetry,
\[
\beta_n(D)=\Phi_n^*+\frac{s^2}{1+s^2}D+O(D^2)\quad(D\downarrow0).
\]

## Assumptions and scope
A right regular \(n\)-gonal bipyramid is the convex hull of the points \((R\cos(2\pi j/n),R\sin(2\pi j/n),0)\) for \(0\le j<n\), the upper apex \((0,0,h_+)\), and the lower apex \((0,0,-h_-)\). The angles are the ordinary interior Euclidean dihedral angles between its planar triangular facets, not the exterior normal angles. The admissible heights are finite and strictly positive. The infima include limiting values from degenerating sequences but equality claims apply only to admissible polytopes. The asymmetry \(D\) is the difference of facet-normal elevation angles, not the ratio of heights.

## Proof
Let \(\alpha=\pi/n\), \(s=\sin\alpha\), \(c=\cos\alpha\). The outward unit normal to upper facet \(j\) is
\[
 u_j^+=(\cos\theta_+\cos((2j+1)\alpha),\,\cos\theta_+\sin((2j+1)\alpha),\,\sin\theta_+),
\]
and the lower normal \(u_j^-\) is given by replacing \(\theta_+\) with \(\theta_-\) and negating the last coordinate. These follow directly by taking cross-products of two equatorial edge vectors and an apex-edge vector. The \(3n\) ridges comprise \(n\) equatorial edges between upper and lower facets at equal azimuth and \(n\) upper and \(n\) lower apex edges between neighboring facets. Since an interior dihedral angle is \(\pi\) minus the angle between outward normals, the three possible interior dihedral angles are
\[
 \phi_0=\pi-(\theta_++\theta_-),\quad
 \phi_+=\pi-2\arcsin(s\cos\theta_+),\quad
 \phi_-=\pi-2\arcsin(s\cos\theta_-).
\]
The normal-angle identity for adjacent facets is \(u_j^\pm\cdot u_{j+1}^\pm=1-2s^2\cos^2\theta_\pm\); all inverse trigonometric branches lie in their indicated principal ranges because \(n\ge3\). Write \(m=(\theta_++\theta_-)/2\), \(D=|\theta_+-\theta_-|\). We have \(D/2<m<\pi/2-D/2\), and \(\arcsin(s\cos\theta)\) is strictly decreasing in \(\theta\). Therefore
\[
 \max\{\phi_0,\phi_+,\phi_-\}=\pi-\min\{2m,\,g(m+D/2)\},\quad g(x)=2\arcsin(s\cos x).
\]
At fixed \(D\), \(2m\) increases strictly, while \(g(m+D/2)\) decreases strictly. They cross in the admissible interval if and only if \(D<g(D)\). The condition is equivalent to \(\sin(D/2)<s\cos D\). Put \(z=\sin(D/2)\): the crossing condition becomes \(2sz^2+z-s<0\), hence \(D<D_n\) with the stated positive root \(z_n\). At the crossing, \(\sin m=s\cos(m+D/2)\), so \(\tan m=s\cos(D/2)/(1+s\sin(D/2))\). Thus the unique maximum of \(\min\{2m,g(m+D/2)\}\) is \(2m_D\) when \(D<D_n\). When \(D\ge D_n\), the decreasing branch governs throughout the open interval, and its supremum is \(g(D)\) as \(m\downarrow D/2\), never attained. These observations prove the full two-piece envelope, uniqueness, and boundary nonattainment, including equality at \(D_n\).

To optimize without fixing \(D\), note that increasing \(D\) while keeping \(m\) fixed weakly decreases \(g(m+D/2)\); moreover \(D=0\) allows the entire interval \(0<m<\pi/2\). The unique global maximizing pair therefore has \(D=0\) and \(2m=g(m)\), namely \(m=\arctan s\). The elevation-to-height conversion \(h=Rc/\tan m\) gives \(h_+=h_-=Rc/s=R\cot\alpha\). Both spoke and equatorial dihedral angles then coincide. Strict monotonicity rules out any second equality case. Finally, Taylor differentiation of \(m_D\) at zero gives \(2m_D=2\arctan s-s^2D/(1+s^2)+O(D^2)\), proving the linear asymmetry penalty. Since \(s\sim\pi/n\), the optimal largest dihedral angle approaches \(\pi\) as \(n\to\infty\), quantitatively \(\Phi_n^*=\pi-2\pi/n+O(n^{-3})\).

## Verification
The accompanying self-contained `verify.py` evaluates actual three-dimensional outward unit facet normals and all three ridge classes for orders \(3\le n\le24\), checks the proposed symmetric optimum against random admissible height pairs, and independently samples the fixed-asymmetry envelopes. The direct Python run passes 172,040 numerical assertions with explicit tolerance. This is a finite numerical cross-check; the arbitrary real parameters and all integer orders follow from the analytic proof above, not the tests.

## Relationship to prior work
Li, Wang and Yu (arXiv:2611.09021, first public 2026-11-06) construct infinitely many convex polytopes with dihedral angles bounded above by a prescribed amount over a right angle. That result motivates a concrete sharp comparison with the rigid right regular bipyramid family, but does not state the present bipyramid minimax, equidihedral rigidity, or the existence/nonexistence transition at fixed normal-elevation asymmetry. Standard dihedral-angle formulas for right regular pyramids, such as those described by Rajpoot, determine local angles but do not by themselves assert this minimax and phase classification. Existing geometric studies of bipyramids optimizing shadow statistics, solid angles, and other quantities address distinct objectives. The algebraic reductions here are explicit to permit checking whether an earlier equivalent result is present under alternative terminology.

## Limitations
The theorem concerns only coaxial bipyramids over regular polygonal bases and positive finite heights. It does not optimize over skew apices, irregular equators, or arbitrary combinatorial types; it does not bound the minimal dihedral angle or vertex solid angles. The asymmetry measure is an angle difference, not the absolute apex-height difference. Priority comparisons are limited to retrieved and inspected accessible sources; undocumented or differently named previous results remain possible. No independent mathematical validation was performed.

## References
1. Z. Li, J. Wang, J. Yu, *Infinitely many convex polytopes with dihedral angles bounded above by \(\pi/2+\delta\)*, arXiv:2611.09021 (first public 2026-11-06), https://arxiv.org/abs/2611.09021.
2. H. C. Rajpoot, *HCR's theorem for dihedral angles in a regular n-gonal right pyramid* (2015), DOI:10.13140/RG.2.2.16488.74242 (earlier local-angle formula; an equivalent global optimization was not established by the accessible excerpt).
3. E. W. Weisstein, *Dipyramid*, MathWorld, https://mathworld.wolfram.com/Dipyramid.html (standard geometry of regular bipyramids).
