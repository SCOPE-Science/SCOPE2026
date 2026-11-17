# A Pareto area-deficit law for triangles sampled on expanding hyperbolic horocycles

## Finding

**Theorem.** In the curvature-\(-1\) hyperbolic plane, fix any horocycle segment of intrinsic arclength \(L>0\). Choose exactly three points independently and uniformly with respect to its hyperbolic arclength measure. Join them with minimizing hyperbolic geodesic segments, and denote the geodesic triangle's intrinsic area by \(A_L\in(0,\pi)\). There exists a coupling under which

\[
Y_L:=L(\pi-A_L)\longrightarrow Z=\frac4T\left(\frac1{P(1-P)}-1\right)\quad\text{almost surely as }L\to\infty,
\]

where \(T\sim\operatorname{Beta}(2,2)\) and \(P\sim\operatorname{Uniform}(0,1)\) are independent. In particular, the limiting cdf is exactly

\[
\Pr(Z\le z)=\begin{cases}0,&z\le12,\\
\displaystyle 6\int_{12/z}^1t(1-t)\sqrt{\frac{zt-12}{zt+4}}\,dt,&z>12.
\end{cases}
\]

The upper tail and positive-moment threshold are sharp:

\[
\lim_{z\to\infty}z\Pr(Z>z)=24,\qquad
\mathbb E[Z^p]<\infty\ \Longleftrightarrow\ 0<p<1.
\]

For every \(0<p<1\), the moments \(\mathbb E[Y_L^p]\to\mathbb E[Z^p]\), but for \(p\ge1\) one has \(\mathbb E[Y_L^p]\to\infty\). In particular, the ordinary area deficit has a precise logarithmically enhanced mean,

\[
\boxed{\mathbb E A_L=\pi-\frac{24\log(L/2)-24+o(1)}L.}
\]

**Marked rare-event geometry of the limiting law.** Write \(Q\) for the normalized leftmost sample coordinate, \(T\) for the normalized span between the outermost sampled points, and \(P\) for the proportion of that span between the first and second order statistics. Under the above coupling, \(Q\mid T=t\) is uniform on \((0,1-t)\), independently of \(P\). Let \(I=0\) if \(P<1/2\) and \(I=1\) otherwise, and set \(V_z=zT\min(P,1-P)/4\). Conditional on \(Z>z\), the joint law of \((I,T,Q,V_z)\) converges in total variation as \(z\to\infty\) to the law in which \(I\) is a fair binary variable, \(T\sim\operatorname{Beta}(1,2)\), \(Q\mid T=t\sim\operatorname{Uniform}(0,1-t)\), and \(V\sim\operatorname{Uniform}(0,1)\), with the stated conditional independences. Thus extreme rescaled deficits are caused by one exceptionally short adjacent horocyclic gap, not by a uniform collapse of all three sample positions.

## Assumptions and scope

Use the upper-half-plane model \(\mathbb H=\{x+iy:y>0\}\) with metric \(ds^2=(dx^2+dy^2)/y^2\). Every horocycle segment is isometric, via a hyperbolic isometry, to \(\{x+i:0\le x\le L\}\). Hyperbolic arclength on this segment is ordinary \(dx\), which specifies precisely the sampling measure. Sampling is with replacement and all order statistics are distinct with probability one. The triangle uses the unique minimizing geodesic between each pair of sampled interior points. All limits are at fixed curvature with \(L\to\infty\). The auxiliary variables \(T,P,Q\) are defined on one probability space and do not depend on \(L\). The marked limit concerns the variable \(Z\), after the \(L\to\infty\) limit, not a uniform joint limit in both \(L\) and the conditioning threshold \(z\).

## Proof

**1. Exact intrinsic triangle area.** Translate the sorted sampled points to \((0,1),(u,1),(u+v,1)\), with \(u,v>0\). A hyperbolic geodesic between two points on \(y=1\) is a Euclidean circle with center at the midpoint of their horizontal coordinates on the real axis, orthogonal to the boundary. By conformality, the interior angle at the middle point is \(\pi-\arctan(u/2)-\arctan(v/2)\). The angles at the left and right points are respectively \(\arctan((u+v)/2)-\arctan(u/2)\) and \(\arctan((u+v)/2)-\arctan(v/2)\). By the hyperbolic Gauss--Bonnet area formula,

\[
A(u,v)=2\left[\arctan(u/2)+\arctan(v/2)-\arctan((u+v)/2)\right].\tag{1}
\]

Equivalently, using \(\arctan x+\arctan(1/x)=\pi/2\) for positive arguments,

\[
\pi-A(u,v)=2\left[\arctan(2/u)+\arctan(2/v)-\arctan(2/(u+v))\right].\tag{2}
\]

**2. Exact independent spacing coordinates.** If the three normalized uniform order statistics are \(0<U_{(1)}<U_{(2)}<U_{(3)}<1\), put

\[
Q=U_{(1)},\quad T=U_{(3)}-U_{(1)},\quad P=\frac{U_{(2)}-U_{(1)}}T.
\]

The ordered joint density is \(6\). The change of variables has Jacobian \(T\) and support \(0<T<1\), \(0<Q<1-T\), \(0<P<1\). Hence \(T\) has density \(6t(1-t)\), \(P\) is independent uniform, and \(Q\mid T=t\) is uniform on \((0,1-t)\), independent of \(P\). The two horocyclic gaps are \(u=LTP\), \(v=LT(1-P)\).

**3. The almost-sure limit and exact cdf.** Substitute those gaps into (2). Since \(L\arctan(a/L)\to a\) for fixed positive \(a\),

\[
Y_L\longrightarrow4\left(\frac1{TP}+\frac1{T(1-P)}-\frac1T\right)=Z
\]

for almost every sampled \((T,P)\). For \(z>12\), conditioning on \(T=t\), the event \(Z\le z\) is equivalent to

\[
P(1-P)\ge\frac4{zt+4}.
\]

It is possible only when \(t\ge12/z\), and its conditional probability is \(\sqrt{(zt-12)/(zt+4)}\). Integrating against \(6t(1-t)\) proves the displayed cdf and the strict lower support endpoint \(12\).

**4. Pareto tail and moment cutoff.** For \(t\ge12/z\), the conditional exceedance probability is

\[
1-\sqrt{\frac{zt-12}{zt+4}}=\frac{16/(zt+4)}{1+\sqrt{(zt-12)/(zt+4)}}\sim\frac8{zt}.
\]

The contribution of \(t<12/z\) is \(O(z^{-2})\). Since the displayed conditional tail is at most \(16/(zt+4)\), dominated convergence after multiplication by \(z\) yields \(\lim z\Pr(Z>z)=8\int_0^1 6(1-t)\,dt=24\). Independence gives, for any positive \(p\),

\[
\mathbb E Z^p=4^p\mathbb E(T^{-p})\int_0^1\left(\frac1{q(1-q)}-1\right)^p dq.
\]

The first factor is finite exactly when \(p<2\), and the second exactly when \(p<1\), proving the threshold. Moreover, from (2), \(0\le Y_L\le4/(TP)+4/(T(1-P))\); its \(p\)-th power has a common integrable majorant for \(0<p<1\), by the same endpoint estimates. Dominated convergence proves subcritical moment convergence; Fatou's lemma and the divergent limiting moment prove divergence for \(p\ge1\).

**5. Exact leading and constant terms of the finite-size mean.** By the marginal \(\operatorname{Beta}(1,3)\) law for either adjacent gap fraction and the \(\operatorname{Beta}(2,2)\) law for their sum, (2) gives the exact formula

\[
\mathbb E Y_L=12L\int_0^1(1-t)^2\arctan\frac2{Lt}\,dt
-12L\int_0^1t(1-t)\arctan\frac2{Lt}\,dt.\tag{3}
\]

Put \(H=L/2\). After the substitution \(t=x/H\), the first term of (3) is

\[
24\int_0^H(1-x/H)^2\arctan(1/x)\,dx.
\]

The three constituent integrals obey

\[
\int_0^H\arctan(1/x)\,dx=\log H+1+o(1),\qquad
H^{-1}\int_0^H x\arctan(1/x)\,dx\to1,\qquad
H^{-2}\int_0^H x^2\arctan(1/x)\,dx\to\tfrac12.
\]

Therefore the first term is \(24\log H-12+o(1)\). The second term of (3) converges to \(12\) by dominated convergence, giving \(\mathbb E Y_L=24\log(L/2)-24+o(1)\), as asserted.

**6. Conditional mark law in total variation.** Given \(T=t\), the event \(Z>z\) consists of two symmetric intervals for \(P\). When \(zt>12\), each has length

\[
p_z(t)=\frac12\left(1-\sqrt{\frac{zt-12}{zt+4}}\right),\qquad\frac{zt}{4}p_z(t)\longrightarrow1\quad(t>0).
\]

The remaining slice \(t\le12/z\) has probability \(O(z^{-2})\), negligible relative to \(\Pr(Z>z)\sim24/z\). In either of the two intervals change coordinates from \(P\) to \(v=(zt/4)\min(P,1-P)\). For each binary label \(I\), the unconditioned joint density of \((T,Q,v)\) is exactly \(24/z\), on

\[
0<t<1,\quad0<Q<1-t,\quad0<v<(zt/4)p_z(t).
\]

After conditioning on \(Z>z\), the density converges pointwise to \(1\) for each label on \(0<t<1\), \(0<Q<1-t\), \(0<v<1\). The limiting total mass over both labels is \(2\int_0^1(1-t)dt=1\). Scheffé's lemma proves joint total-variation convergence. Integrating this limit gives the fair label, the \(\operatorname{Beta}(1,2)\) span, the conditional uniform left location, and the independent uniform short-gap mark.

## Verification

The standalone `verify_horocycle.py` computes exact areas using (1) and, independently, angles from the hyperbolic cosine rule at five choices of positive gaps. It evaluates the finite-size expectation formula numerically for three segment lengths and compares with the stated logarithmic expansion. Finally it evaluates the limiting cdf at six thresholds and its large-threshold tail, and performs a fixed-seed independent sampling check of the rare-event beta/uniform marks. Its output ends with `HOROCYCLE_TRIANGLE_AREA_LIMIT_CHECKS_OK`. These finite numerical checks are consistency tests only; the almost-sure, total-variation, and moment statements are established by the analytic proof above.

## Relationship to prior work

Bao and Chen (2014) provide deterministic Poincaré half-plane triangle-area formulas, including a coordinate decomposition for general triangles; they do not sample three arclength-uniform vertices on an expanding horocycle or derive the limiting beta-inverse area law. Classical horocyclic chord-length identities describe metric geometry but do not imply the random conditional mark distribution without the sampling and scaling analysis. Beardon (2022) gives the classical criterion distinguishing hyperbolic circles, horocycles, and hypercycles through triangle vertices, not this limit theorem.

A separate published result, *Pareto limit law and sharp moment threshold for areas of large random hyperbolic triangles* (published-finding corpus, 2026), samples three points uniformly in an expanding **hyperbolic-volume ball**. Its independent random radial deficits and directions yield a different limiting mixture; it has no fixed horocycle, the independent \(\operatorname{Beta}(2,2)\)-uniform factorization here, or this constant \(24\) and logarithmic finite-size mean. Related prior results on triangles sampled on geodesic circles concern a distinct sampling measure and different asymptotic scalings. Neither is asserted to be false or subsumed. The theorem's contribution is the exact fixed-horocycle limit, marked short-gap mechanism, and expectation correction, not the classical triangle-area formula or the general fact that inverse spacings can have heavy tails.

## Limitations

The result assumes exactly three independent arclength-uniform points on one finite horocycle segment in a curvature-\(-1\) hyperbolic plane. The joint conditional law is for the limiting variable after the large-\(L\) limit, not for simultaneous large-\(L\), large-\(z\) scaling. No higher-dimensional analogue, nonuniform-density universality, convergence rate, or independent historical certification is claimed. Prior-work comparisons do not prove global uniqueness of the result, and some older specialized references could remain unidentified.

## References

1. H. Bao and X. Chen, *A New Hyperbolic Area Formula of a Hyperbolic Triangle and Its Applications*, Journal of Mathematics, first published 2014-08-13, https://doi.org/10.1155/2014/838497.
2. A. F. Beardon, *Circumscribed hyperbolic triangles*, Archiv der Mathematik 119 (2022), 439--448, published 2022-08-08, https://doi.org/10.1007/s00013-022-01761-x.
3. *Horocyclic polygons*, University of Glasgow geometry notes, https://www.maths.gla.ac.uk/wws/cabripages/hyperbolic/horocycles.html (undated online geometry note; no source date inferred).
4. *Pareto limit law and sharp moment threshold for areas of large random hyperbolic triangles*, publicly accessible comparative result, 2026, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-pareto-limit-law-and-sharp-moment-threshold-for-areas-of-large-r--4c826ecef45b.
