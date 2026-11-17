# A sign-changing puncture response in Sylvester's four-point problem for disks

## Finding

Let \(D=\{z\in\mathbb R^2:\|z\|<1\}\). For a measurable planar region \(E\) of positive finite area, write \(Q(E)\) for the probability that four independent area-uniform points of \(E\) are the four vertices of their convex hull. For an interior point \(x\in D\), put \(D_{x,h}=D\setminus\overline{B(x,h)}\), \(0<h<1-\|x\|\), and \(r=\|x\|\).

**Puncture theorem.** For every fixed \(x\in D\), as \(h\downarrow0\),
\[
Q(D_{x,h})=Q(D)+S(r)h^2+o_x(h^2),\qquad Q(D)=1-\frac{35}{12\pi^2}.
\]
The susceptibility \(S(r)\) is continuous on \([0,1)\) and satisfies
\[
S(0)=1-\frac{19}{3\pi^2}>0,\qquad
S(r)<0\quad(99/100\le r<1),
\]
and the explicit boundary asymptotic
\[
S(r)=-\frac{10}{\pi^2}(1-r)+O((1-r)^{3/2})\quad(r\uparrow1).
\]
Consequently, deleting a sufficiently small *central* disk **increases** the probability of convex position, while deleting a sufficiently small disk centered sufficiently near (but strictly inside) the outer circle **decreases** that probability. At least one transition radius lies in \((0,99/100)\); uniqueness is not asserted.

More precisely, if \(X,Y,Z\) are independent uniform points of \(D\), define
\[
I(r)=\Pr\{(r,0)\in\operatorname{conv}(X,Y,Z)\}.
\]
Then the entire susceptibility has the formula
\[
\boxed{S(r)=4I(r)-\frac{(1-r^2)(r^4-5r^2+19)}{3\pi^2}.}
\]
The function \(I\) has a standard exact one-dimensional angular integral, but the claimed sign reversal and boundary coefficient require no evaluation of that integral.

## Assumptions and scope

All random points are independent and have normalized two-dimensional Lebesgue-area distribution. Convex position means that all four sampled points are extreme points of their convex hull. Boundaries and collinear configurations have probability zero. Radius one is a normalization; uniform dilation gives the corresponding statement for every circular disk. The puncture center \(x\) is held fixed before \(h\downarrow0\); no uniform asymptotic is claimed while \(x\) simultaneously approaches the boundary.

## Proof

**1. The anchored triangle-area polynomial.** Fix \(x=(r,0)\), \(0\le r\le1\), and set \(A(r)=\mathbb E[\operatorname{area}(\triangle xYZ)]\), where \(Y,Z\) are independent area-uniform points of \(D\). Parameterize the line through \(Y,Z\) by an unoriented normal direction \(\theta\in[0,\pi)\), signed distance \(t\in[-1,1]\), and positions \(s_1,s_2\in[-\sqrt{1-t^2},\sqrt{1-t^2}]\) along the line. The planar pair change-of-variables has absolute Jacobian \(|s_1-s_2|\). Furthermore,
\[
2\operatorname{area}(\triangle xYZ)=|s_1-s_2|\,|t-r\cos\theta|,\qquad
\int_{-w}^w\!\int_{-w}^w(s_1-s_2)^2ds_1ds_2=\frac83w^4.
\]
Therefore
\[
A(r)=\frac4{3\pi^2}\int_0^\pi\!\int_{-1}^1(1-t^2)^2|t-r\cos\theta|\,dt\,d\theta.
\]
For \(|u|\le1\), direct integration gives
\[
\int_{-1}^1(1-t^2)^2|t-u|dt
=\frac13+u^2-\frac{u^4}{3}+\frac{u^6}{15}.
\]
Averaging the even powers of \(\cos\theta\) yields the exact polynomial
\[
\boxed{A(r)=\frac4{3\pi}\left(\frac13+\frac{r^2}{2}-\frac{r^4}{8}+\frac{r^6}{48}\right).}
\]
In particular \(A(0)=4/(9\pi)\), \(A(1)=35/(36\pi)\), and integration against the radial density \(2r\,dr\) gives \(\mathbb E[\operatorname{area}(\triangle XYZ)]=35/(48\pi)\).

**2. The fixed-vertex convex-position law.** Let \(q(r)\) be the probability of convex position of the four points \((r,0),X,Y,Z\). Exactly one vertex lies in the triangle of the remaining three whenever convex position fails (disjoint events). The fixed vertex is inside \(\triangle XYZ\) with probability \(I(r)\). Each of the other three vertices, conditional on the other two and on the fixed point, lies in the corresponding triangle with probability its area divided by \(\pi\), because the disk is convex. Consequently,
\[
q(r)=1-I(r)-\frac{3A(r)}\pi.
\]
For four fully random disk points, the same disjoint-event argument gives
\[
Q(D)=1-\frac4\pi\mathbb E[\operatorname{area}(\triangle XYZ)]
=1-\frac{35}{12\pi^2}.
\]
At \(r=0\), independent uniform angular directions contain the origin in their triangle with probability \(1/4\): the complementary event has probability \(3(1/2)^2=3/4\), by identifying the unique first vertex of a containing semicircle. Thus
\[
q(0)=\frac34-\frac4{3\pi^2},\qquad
4(Q(D)-q(0))=1-\frac{19}{3\pi^2}>0.
\]
At \(r=1\), the fixed point is on the boundary and \(I(1)=0\); hence \(q(1)=Q(D)\). More generally,
\[
q(r)-Q(D)=\frac{(1-r^2)(r^4-5r^2+19)}{12\pi^2}-I(r).
\]

**3. Rigorous opposite sign near the boundary.** Put \(\delta=1-r\). If \((r,0)\) belongs to a triangle whose three vertices lie in \(D\), at least one of those vertices has first coordinate at least \(r\). The area of that circular cap equals \(\arccos r-r\sqrt{1-r^2}\), and integration of its derivative gives
\[
0\le I(r)\le \frac3\pi\bigl(\arccos r-r\sqrt{1-r^2}\bigr)
\le \frac{4\sqrt2}{\pi}\delta^{3/2}.
\]
Since \(r^4-5r^2+19\ge15\) for \(0\le r\le1\),
\[
q(r)-Q(D)\ge
\delta\left(\frac{5(1+r)}{4\pi^2}-\frac{4\sqrt2}{\pi}\sqrt\delta\right)>0
\quad(99/100\le r<1).
\]
The last strict inequality follows, for instance, from \(3<\pi<22/7\), \(\sqrt2<3/2\), \(1+r\ge199/100\) and \(\sqrt\delta\le1/10\). Also the polynomial contribution is \(5\delta/(2\pi^2)+O(\delta^2)\), while \(I(r)=O(\delta^{3/2})\). Thus
\[
q(r)-Q(D)=\frac{5}{2\pi^2}(1-r)+O((1-r)^{3/2}).
\]
Continuity of \(q\) follows by dominated convergence away from the null set of collinear triples; the intermediate value theorem gives a zero of \(q(r)-Q(D)\) between \(0\) and \(99/100\).

**4. First variation under a removed disk.** Write \(\mu\) for normalized area measure on \(D\), \(\tau_h\) for normalized area measure on \(B(x,h)\), and \(\nu_h\) for normalized area measure on \(D_{x,h}\). Their exact mixture relation is \(\mu=(1-h^2)\nu_h+h^2\tau_h\). Apply the fourfold product to the bounded convex-position indicator. Expanding the mixture and using \(\|\mu-\nu_h\|_{\mathrm{TV}}=O(h^2)\) yields
\[
Q(D_{x,h})=Q(D)+4h^2\bigl(Q(D)-Q(\tau_h,\mu,\mu,\mu)\bigr)+O(h^4).
\]
The mixed probability tends to \(q(r)\) as \(h\downarrow0\), because the indicator is a.s. continuous at the fixed non-collinear configuration. Hence \(S(r)=4(Q(D)-q(r))\), proving the stated formula, signs and boundary expansion.

## Verification

The accompanying `check.py` evaluates \(I(r)\) by an independently parameterized angular integral and checks the anchored area polynomial, the disk constant, the explicit cap lower bounds at three near-boundary radii, the boundary coefficient, and direct Monte Carlo convex-position tests with one fixed vertex. It prints `DISK_PUNCTURE_SYLVESTER_SIGN_REVERSAL_OK` on completion. The analytic proof above does not rely on Monte Carlo or numerical quadrature.

## Relationship to prior work

Sylvester's classical four-point problem and Blaschke's disk extremality theorem concern **convex sampling regions**. Marckert's 2014 arXiv preprint provides exact disk convex-position probabilities; its formula for four points supplies the classical constant used here, independently rederived above. Marckert and Rahmani investigate extrema over convex regions. Eisenberg and Sullivan study a different normalized expected-area statistic over arbitrary probability measures rather than the four-point convex-position probability. Ionascu's work supplies general formulas for the chance that a fixed point is inside a random triangle and, in particular, studies an off-center point in a disk; that component \(I(r)\) is therefore **not claimed as new**. The present theorem instead combines an exact anchored area polynomial with the four-point mixture derivative and proves the unexpected **sign reversal** for infinitesimal holes. Related thin-shell asymptotics and hole-placement effects for *other* observables do not imply this small-hole four-point result.

## Limitations

Historical priority is provisional. The sign reversal and coefficient are a claimed new combination, not the classical disk probability, Wendel semicircle count, or a new general formula for \(I(r)\). The sign may change more than once; no uniqueness or full classification of the zero set is proved. The asymptotic is pointwise in the fixed puncture center and says nothing uniform about centers whose distance to the outer circle is of the same order as the puncture radius. Independent mathematical and historical validation has not been performed.

## References

- J.-F. Marckert, *Probability that n random points in a disk are in convex position*, arXiv:1402.3512, first posted 2014-02-14, https://arxiv.org/abs/1402.3512.
- J.-F. Marckert, *Around Sylvester's question in the plane*, arXiv:1511.03658, first posted 2015-11-11, https://arxiv.org/abs/1511.03658; later joint work with S. Rahmani.
- E. J. Ionaşcu, *Random triangles in planar regions containing a fixed point*, arXiv:1612.08619, first posted 2016-12-15, https://arxiv.org/abs/1612.08619.
- B. Eisenberg and R. Sullivan, *A Modification of Sylvester's Four Point Problem*, Mathematics Magazine 84 (2011), 173–184, doi:10.4169/math.mag.84.3.173.
- J. J. Sylvester, *Problem 1491*, Educational Times (1864); W. Blaschke, *Über affine Geometrie XI*, 1917.
