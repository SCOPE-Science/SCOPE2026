# Exact stretch distribution and sharp extreme distortion on a circular-cone sidewall

## Finding

Let \(L>0\) and \(0<q<1\). Consider the lateral surface, without the base disk, of the right circular cone with slant length \(L\), rim radius \(qL\), and height \(L\sqrt{1-q^2}\). Choose two points independently from normalized surface area. Let \(D_g\) denote their intrinsic shortest-path distance along the sidewall and \(D_e\) their ambient three-dimensional Euclidean distance. The ratio \(Z=D_g/D_e\) is defined almost surely. Its **entire distribution is independent of** \(L\) and has essential support from \(1\) to
\[
K(q)=\frac{\sin(\pi q/2)}q.
\]
The maximum \(K(q)\) is attained exactly by pairs of equal nonzero slant radius with opposite azimuths, and is strictly decreasing from \(\pi/2\) toward \(1\) as \(q\) increases from zero to one. Thus the maximum distortion uniquely identifies the cone opening; the opening together with the lateral area identifies both physical cone dimensions.

For every \(1<\lambda<K(q)\), let \(\theta_\lambda\in(0,\pi)\) be the unique solution
\[
\frac{\sin(q\theta_\lambda/2)}{q\sin(\theta_\lambda/2)}=\lambda,
\]
and put
\[
Q_{q,\lambda}(\theta)=\frac{\sin^2(q\theta/2)-\lambda^2q^2\sin^2(\theta/2)}{\lambda^2-1}.
\]
Then the exact strict survival function is
\[
\boxed{\Pr(Z>\lambda)=\frac1\pi\int_{\theta_\lambda}^\pi
\left[1-\exp\left(-4\operatorname{arsinh}\sqrt{Q_{q,\lambda}(\theta)}\right)\right]d\theta.}
\]
It equals \(1\) for \(\lambda\le1\) and \(0\) for \(\lambda\ge K(q)\).

For each **fixed** \(q\in(0,1)\), the upper endpoint has the sharp tail
\[
\boxed{\Pr(Z>K(q)-\varepsilon)=C(q)\varepsilon^{3/2}+o_q(\varepsilon^{3/2}),}\quad
C(q)=\frac{16\sqrt{2q^3\sin(\pi q/2)}}{3\pi\cos(\pi q/2)\sqrt{\sin^2(\pi q/2)-q^2}}>0.
\]
A conditional limiting shape is also explicit. Write \(U=\log(s/t)\) for the sampled slant radii, \(\eta=\pi-\delta\) for the deficit in shorter azimuthal separation, and set
\[
A_q=\tfrac12\cos(\pi q/2),\qquad
B_q=\frac{\sin^2(\pi q/2)-q^2}{2q^3\sin(\pi q/2)}.
\]
Conditioned on \(Z>K(q)-\varepsilon\), the vector \((\eta/\varepsilon,U/\sqrt\varepsilon)\) converges weakly to uniform Lebesgue measure on
\[
\{(v,w):v\ge0,\quad A_qv+(B_q/4)w^2<1\}.
\]

## Assumptions and scope

The surface is embedded in \(\mathbb R^3\) and carries its induced intrinsic path-length metric, including the tip and rim in its metric completion. Neither the tip nor the rim has positive surface-area mass. The normalized area element in slant-polar coordinates \(s\in(0,L)\), \(\phi\in[0,2\pi)\) is \(s\,ds\,d\phi/(\pi L^2)\). The two points are independent. The case \(q=1\) is a planar disk, for which \(Z=1\) almost surely, and is not part of the stated endpoint asymptotic. All asymptotics hold with \(q\) fixed; no uniformity near either degenerate opening is asserted.

## Proof

**Exact metric reduction.** Parametrize the sidewall by
\[
X(s,\phi)=(qs\cos\phi,qs\sin\phi,\sqrt{1-q^2}\,s).
\]
For two samples with slant radii \(s,t\) and shorter azimuthal separation \(\delta\in[0,\pi]\), cone development uses the sector angle \(q\delta\in[0,\pi q)\). Since this is strictly less than \(\pi\), its planar straight segment is a shortest geodesic and stays within the developed radial disk. Thus
\[
D_g^2=(s-t)^2+4st\sin^2(q\delta/2),\qquad
D_e^2=(s-t)^2+4q^2st\sin^2(\delta/2).
\]
The first formula is intrinsic and the second is the actual three-dimensional Cartesian chord. Both formulas are valid at the metric boundaries by continuity.

**Two independent variables.** Each slant radius has density \(2s/L^2\); the independent shorter angle \(\delta\) is uniform on \([0,\pi]\). If \(U=\log(s/t)\), then \(\Pr(U\in du)=e^{-2|u|}\,du\): indeed, \(\log(s/L)\) and \(\log(t/L)\) are independent negatives of rate-two exponential random variables. Consequently \(U\) and \(\delta\) are independent. Dividing the squared distances by \(4st\) gives the exact law
\[
Z^2=\frac{\sinh^2(U/2)+\sin^2(q\delta/2)}{\sinh^2(U/2)+q^2\sin^2(\delta/2)}.
\]
For \(0<\delta\le\pi\), \(\sin(q\delta/2)>q\sin(\delta/2)\) by strict decrease of \(\sin x/x\) on \((0,\pi/2]\). Hence \(Z\) strictly decreases as \(|U|\) increases, and at \(U=0\) it equals \(h_q(\delta)=\sin(q\delta/2)/(q\sin(\delta/2))\). The derivative of \(\log h_q\) has the sign of \((q\delta/2)\cot(q\delta/2)-(\delta/2)\cot(\delta/2)\), which is positive because \(x\cot x\) strictly decreases on \((0,\pi/2]\). Therefore the global maximum is \(h_q(\pi)=K(q)\), attained precisely at \(U=0,\delta=\pi\). Finally \(\sin x/x\) strictly decreases with \(x\), proving the asserted strict dependence of \(K\) on \(q\).

**Exact distribution.** For \(1<\lambda<K(q)\), the event \(Z>\lambda\) requires \(\delta>\theta_\lambda\), and is equivalent to
\[
|U|<2\operatorname{arsinh}\sqrt{Q_{q,\lambda}(\delta)}.
\]
Since \(\Pr(|U|<w)=1-e^{-2w}\), integrating this conditional event against \(d\delta/\pi\) yields the survival integral. There are no atoms at the endpoints, since the maximizing set and the equal-angle set have zero sampling measure.

**Sharp endpoint and conditional law.** Let \(S=\sin(\pi q/2)\) and \(C_0=\cos(\pi q/2)\). Near the unique maximizing pair of variables \((\eta,U)=(0,0)\), direct Taylor expansion of the displayed rational formula for \(Z^2\) gives
\[
K(q)-Z=\frac{C_0}{2}\eta+\frac{S^2-q^2}{8Sq^3}U^2
+O_q(\eta^2+\eta U^2+U^4).
\]
Both leading coefficients are strictly positive, so compactness away from the maximizing point localizes the tail to \(\eta=O_q(\varepsilon)\), \(U=O_q(\sqrt\varepsilon)\). Under \(\eta=\varepsilon v\), \(U=\sqrt\varepsilon w\), the joint sampling density is \(\pi^{-1}e^{-2\sqrt\varepsilon|w|}\varepsilon^{3/2}\,dv\,dw\). The rescaled domain converges, with a bounded dominating region, to \(A_qv+(B_q/4)w^2<1\), \(v\ge0\). Its planar Lebesgue area is \(8/(3A_q\sqrt{B_q})\). Dominated convergence gives
\[
\lim_{\varepsilon\downarrow0}\varepsilon^{-3/2}\Pr(Z>K(q)-\varepsilon)
=\frac8{3\pi A_q\sqrt{B_q}}=C(q).
\]
The same normalized integral for bounded continuous test functions proves the conditional uniform weak limit. This proves all asserted statements.

## Verification

The accompanying standalone Python 3 file `check_ratio.py` evaluates the derived one-dimensional integral by composite Simpson quadrature and independently samples Cartesian three-dimensional cone coordinates. For each of three cone openings, two interior stretch thresholds are compared with the Monte Carlo proportions from 180,000 independent pairs per comparison, and the squared Cartesian chord is checked independently against the algebraic formula. For each opening, two shrinking upper-tail thresholds check the convergence rate to the explicit \(C(q)\). All nine checks passed with marker `CONE_RATIO_DISTRIBUTION_AND_TAIL_OK 9`. These finite comparisons supplement but do not replace the analytic proof for every fixed opening.

## Relationship to prior work

Isometric development of conical surfaces into planar sectors is classical. O'Rourke and Vîlcu (2011) systematically treat cone development of curves on polyhedra; their examined definitions and arguments concern development and visibility, not area-uniform pairwise intrinsic-to-ambient stretch. A 2016 public calculation gives the cone's opposite-rim geodesic length, equivalent to the numerator of the deterministic endpoint \(K(q)\) when divided by the straight opposite-rim chord. That partial geometric observation is **not** claimed new here. Published studies of the mean-square *intrinsic distance* and its extreme-distance tails on truncated cones provide the same unfolding law but do not give the **ratio of intrinsic to extrinsic distances**, its exact survival distribution, the \(3/2\)-power distortion tail, or the conditional scaled shape. A general positive-reach bound for metric distortion likewise does not give the opening-specific distribution; the conical apex has zero reach. The new assertion is the joint ratio law and its sharp endpoint asymptotics, not the elementary unfolding or the endpoint geodesic identity.

## Limitations

Historical priority has been checked against the specifically named sources and accessible related published findings but is not certified exhaustively. The scope excludes noncircular cones, frusta, conical disks with angle exceeding \(2\pi\), different sampling measures, weighted paths and any uniform double limit in opening and endpoint deficit. The proof determines a one-dimensional exact integral for the CDF, not an elementary closed form for arbitrary thresholds. Independent mathematical audit has not been performed.

## References

- J. O'Rourke and C. Vîlcu, *Conical Existence of Closed Curves on Convex Polyhedra*, arXiv:1102.0823, first posted 2011-02-04. https://arxiv.org/abs/1102.0823
- J. O'Rourke and C. Vîlcu, *Development of Curves on Polyhedra via Conical Existence*, publicly dated 2011-10-07 manuscript, https://www.science.smith.edu/~jorourke/Papers/ConicalDevelopment.pdf
- B. Berentsen and J. D'Aurizio, *Geodesic on a right circular cone problem*, public discussion and opposite-rim geodesic formula dated August 2016. https://math.stackexchange.com/questions/1897144/geodesic-on-a-right-circular-cone-problem/2061892
- *Sharp mean-square geodesic separation and a third-order transition in Euclidean cone disks*, public mathematical result (2026). Public research identifier cc597f8daf41; https://github.com/published-finding corpus/2026
- *Sharp upper-distance tails at the tip-rim transition of a finite flat cone*, public mathematical result (2026). Public research identifier b319e1ca315a; https://github.com/published-finding corpus/2026
- J.-D. Boissonnat, A. Lieutier, M. Wintraecken, *The reach, metric distortion, geodesic convexity and the variation of tangent spaces*, J. Appl. Comput. Topol. 3 (2019), 29–58. https://doi.org/10.1007/s41468-019-00029-8
