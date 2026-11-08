# Sharp mean-square geodesic separation and a third-order transition in Euclidean cone disks

## Finding

Let \(C_{\alpha,R}\) be the closed radial disk of slant radius \(R>0\) in the two-dimensional Euclidean metric cone of total angle \(\alpha>0\). Sample \(X,Y\) independently from normalized intrinsic area, write \(D=d_{C_{\alpha,R}}(X,Y)\), and let \(A=\alpha R^2/2\) be the disk area. Put \(x=\alpha/2\). Then the complete area-normalized mean-squared distance law is

\[
\frac{\mathbb E[D^2]}{A}=F(x):=
\begin{cases}
\dfrac{9x-8\sin x}{9x^2},&0<x\le\pi,\\[2mm]
\dfrac{17x-8\pi}{9x^2},&x\ge\pi.
\end{cases}
\]

For \(0<x\le\pi\), corresponding exactly to the lateral surfaces of ordinary right circular cones (including the planar disk as the endpoint), there are precisely two stationary points \(x_-\in(0,\pi/2)\) and \(x_+\in(\pi/2,\pi)\). They are the unique zeros in those ranges of
\[
16\sin x=x(9+8\cos x).
\]
The first is the **unique global minimizer** over all such fixed-area conical disks; the second is a strict local maximum. Numerically,
\[
x_-=0.925373136253\ldots,\qquad
x_+=2.922167960398\ldots,\qquad
F(x_-)=0.251412549578\ldots,
\]
so that the uniquely optimal total cone angle is \(\alpha_*=2x_-=1.850746272506\ldots\). In particular,
\[
\mathbb E[D^2]\ge F(x_-)\,A
\]
for every \(0<\alpha\le2\pi\), with equality exactly when \(\alpha=\alpha_*\).

The levels satisfy \(F(x_-)<F(\pi)=1/\pi<F(x_+)\). Consequently **every** level \(y\in(1/\pi,F(x_+))\) is realized by exactly three distinct ordinary right circular cone shapes at any prescribed positive area. This is an exact threefold inverse ambiguity of one natural intrinsic pair-distance statistic.

For abstract Euclidean cones with \(\alpha>2\pi\), a shortest geodesic between uniform points passes through the apex with probability exactly \(1-2\pi/\alpha\); this event has probability zero for \(\alpha\le2\pi\). The function \(F\) is \(C^2\), but not \(C^3\), at \(x=\pi\):
\[
F'''(\pi^-)-F'''(\pi^+)=-\frac8{9\pi^2}.
\]
For \(x\ge\pi\), \(F\) decreases strictly to zero. Thus there is no positive global minimum over *all* abstract cone angles \(\alpha>0\).

## Assumptions and scope

A Euclidean metric cone of angle \(\alpha\) is obtained from the warped polar metric \(ds^2=dr^2+r^2d\theta^2\), with \(r\ge0\) and \(\theta\) interpreted modulo \(\alpha\). The radial disk has \(0\le r\le R\). Angular circles have length \(\alpha r\), and area element is \(r\,dr\,d\theta\). For \(\alpha\in(0,2\pi]\), the disk is intrinsically isometric to a right circular cone lateral surface of finite slant radius; the case \(\alpha=2\pi\) is the flat planar disk. Angles greater than \(2\pi\) are considered only as intrinsic cone metrics, not as embedded right circular cones in ordinary three-dimensional Euclidean space.

The samples have normalized **intrinsic area** measure, not uniform radial distance, not boundary sampling, and not ambient Euclidean chord distance. The distance is the intrinsic shortest-path metric of the radial disk. Every intrinsic minimizing geodesic between points in the disk stays in the disk.

## Proof

For independent area-uniform points, their radial coordinates \(r,s\) are independent with density \(2r/R^2\) on \([0,R]\), and their angular coordinates are independent uniform on a circle of length \(\alpha\). Their shorter angular separation \(\delta\) is uniform on \([0,\alpha/2]\). The metric-cone distance law is
\[
D^2=r^2+s^2-2rs\cos(\min\{\delta,\pi\}).
\]
To see this, unfold the sector along the shorter angular arc. If \(\delta<\pi\), the straight chord is minimizing; if \(\delta\ge\pi\), the radial path through the apex has length \(r+s\) and is minimizing. The latter case can occur with positive probability only when \(\alpha>2\pi\). The cone-law formula also holds when one point is the apex, by continuity.

Radial integration gives \(\mathbb E[r^2]=R^2/2\) and \(\mathbb E[rs]=4R^2/9\). Angular integration then gives
\[
\mathbb E\!\left[\cos(\min\{\delta,\pi\})\right]
=\begin{cases}
\dfrac{\sin x}{x},&0<x\le\pi,\\[2mm]
\dfrac{\pi-x}{x},&x\ge\pi.
\end{cases}
\]
Substitution into the cone-distance law, followed by \(A=xR^2\), proves the displayed formula for \(F\). For \(x>\pi\), the event \(\delta\ge\pi\) has probability \((x-\pi)/x=1-2\pi/\alpha\), proving the apex statement.

On \((0,\pi)\), differentiation gives
\[
F'(x)=\frac{G(x)}{9x^3},\quad
G(x)=16\sin x-x(9+8\cos x),\quad
G'(x)=8\cos x-9+8x\sin x,\quad G''(x)=8x\cos x.
\]
Thus \(G'\) is strictly increasing on \((0,\pi/2)\) and strictly decreasing on \((\pi/2,\pi)\). Since \(G'(0)=-1\), \(G'(\pi/2)=4\pi-9>0\), and \(G'(\pi)=-17\), \(G'\) has exactly two zeros. Moreover \(G(0)=0\), \(G(\pi/2)=16-9\pi/2>0\), and \(G(\pi)=-\pi<0\). Therefore \(G\) has exactly two positive zeros \(x_-\in(0,\pi/2)\) and \(x_+\in(\pi/2,\pi)\), with signs negative, positive, negative on the three complementary intervals. Consequently \(F\) decreases, increases, then decreases. Since \(F(x)\to+\infty\) as \(x\downarrow0\), only the first local minimum can be global; and it is below the planar-disk endpoint because \(F(\pi/2)<F(\pi)\), equivalent to \(9\pi<32\). This proves uniqueness and the sharp lower bound.

The strict inequality \(F(x_+)>F(\pi)\) follows by evaluating at \(x=7\pi/8\):
\[
F(7\pi/8)>F(\pi)
\quad\Longleftrightarrow\quad
\frac{63\pi}{64}>8\sin(\pi/8),
\]
which follows from \(\pi>157/50\), \(\sqrt2>141/100\) and \(\sin(\pi/8)=\sqrt{2-\sqrt2}/2\). The three monotonic intervals now prove the stated exactly three-to-one inverse phenomenon for all levels strictly between \(F(\pi)\) and \(F(x_+)\).

For \(x>\pi\),
\[
F'(x)=\frac{16\pi-17x}{9x^3}<0,
\]
so \(F\) decreases to zero at infinity. At \(x=\pi\) both branches agree through their second derivatives. Indeed, if the first branch is analytically continued across \(\pi\), its difference from the second branch is
\[
\frac{8(\pi-x-\sin x)}{9x^2}
=-\frac{4(x-\pi)^3}{27\pi^2}+O((x-\pi)^4).
\]
The coefficient proves the third-derivative jump and shows that no stronger smoothness is asserted.

## Verification

A standalone Python checker `check_conical_distance.py` uses independently coded root bisection, the exact stationary equation, direct Monte Carlo sampling of both radial coordinates and the angular circle, and the apex-inclusive metric-cone distance law. It tests cone angles on both sides of \(2\pi\), the strict ordering of the two stationary levels and the planar level, and the cubic mismatch near the flat-angle transition. Seven runs with \(220{,}000\) independent point pairs each passed the stated six-standard-error-plus-tolerance criterion; the output marker is `CONE_AREA_DISTANCE_PHASE_AND_MC_OK`. This numerical check is supplemental: the proof for all real \(\alpha>0\) is the analytic argument above, not a finite computation.

## Relationship to prior work

Euclidean cone metrics and the distinction between positive and negative cone-point curvature are classical. Izmestiev (2014) concerns isoperimetric inequalities for cone-surface disks, while Charitos–Papadoperakis–Tsapogas (2014) study closed-surface geodesic structure for arbitrary cone angles. Neither materially inspected paper formulates the area-normalized two-point squared-distance optimization, its three-to-one inverse levels, or the third-order transition derived here. General formulae for metric-cone distances are used as background, not claimed as new. Related treatments of uniformly random distances in balls and of other compact flat surfaces use different spaces and metrics; their formulas do not directly settle this fixed-area conical optimization. Scientific priority is subject to later historical and independent review.

## Limitations

The sharp optimizer is only for the rotational one-apex family of radial cone disks of fixed intrinsic area with \(0<\alpha\le2\pi\); it is not a claim of optimality among all cone surfaces, all smooth surfaces, or all intrinsic metrics on disks. The extension \(\alpha>2\pi\) is an abstract metric-cone result, not a smooth embedded cone result. The analysis concerns the second moment, not the whole random-distance law or optimization of other moments. Numerical tests cannot establish historical priority or independent validation.

## References

- I. Izmestiev, *A simple proof of an isoperimetric inequality for euclidean and hyperbolic cone-surfaces*, arXiv:1409.7681v1, publicly submitted 26 September 2014. https://arxiv.org/abs/1409.7681
- C. Charitos, I. Papadoperakis, G. Tsapogas, *On surfaces with conical singularities of arbitrary angle*, arXiv:1412.3404v1, publicly submitted 10 December 2014. https://arxiv.org/abs/1412.3404
- S.-J. Tu and E. Fischbach, *Random distance distribution for spherical objects: general theory and applications to physics*, J. Phys. A 35 (2002), 6557–6570, DOI:10.1088/0305-4470/35/31/303. (Background on random distances in a different geometry.)
