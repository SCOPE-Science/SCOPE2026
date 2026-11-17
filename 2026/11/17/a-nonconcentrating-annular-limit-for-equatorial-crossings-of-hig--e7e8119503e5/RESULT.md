# A nonconcentrating annular limit for equatorial crossings of high-dimensional spherical chords

## Finding

For each integer \(d\ge3\), let \(U_d,V_d\) be two independent surface-area-uniform points on the Euclidean unit sphere \(S^{d-1}\subset\mathbb R^d\). Write \(E_d\) for the event that their last coordinates have opposite signs. Its probability is exactly \(1/2\). Conditional on \(E_d\), let \(Z_d\) be the unique intersection of the **straight Euclidean segment** \([U_d,V_d]\) with the equatorial hyperplane \(H_d=\{x_d=0\}\), and put \(Q_d=\|Z_d\|^2\).

**Theorem.** As \(d\to\infty\) through integers, \(Q_d\) converges in distribution to a nondegenerate random variable \(Q\) whose cumulative distribution function is
\[
F(q)=\begin{cases}
0,&q\le 1/2,\\
\dfrac4\pi\arctan\sqrt{2q-1},&1/2<q<1,\\
1,&q\ge1.
\end{cases}
\]
Its density is
\[
\boxed{f_Q(q)=\frac{2}{\pi q\sqrt{2q-1}}\,\mathbf 1_{\{1/2<q<1\}}.}
\]
For every real \(s>0\), \(\mathbb E[Q_d^s\mid E_d]\to\mathbb E[Q^s]\). In particular,
\[
\boxed{\mathbb E[Q]=\frac2\pi,\qquad \mathbb E[Q^2]=\frac4{3\pi},\qquad
\operatorname{Var}(Q)=\frac4{3\pi}-\frac4{\pi^2}>0.}
\]
The limiting crossing point therefore lies outside every fixed ball of radius strictly less than \(1/\sqrt2\) with probability tending to one, yet its distance from the center **does not concentrate at any constant**. In contrast, the chord length \(\|U_d-V_d\|\) converges in probability to \(\sqrt2\).

For every fixed \(d\ge3\), conditional on \(E_d\), the direction \(Z_d/\|Z_d\|\) is surface-uniform on \(S^{d-2}\subset H_d\) and is independent of \(Q_d\). This finite-dimensional rotational statement does not assert a common limiting direction as the ambient dimension changes.

## Assumptions and scope

Sample each endpoint independently from normalized \((d-1)\)-dimensional surface measure. This is **not** a Euclidean-motion-invariant random-line ensemble in dimensions other than three, nor a pair of points sampled from a solid ball. Condition on the two endpoints lying in opposite open hemispheres. The measure-zero events of an endpoint on the equator or an undefined chord direction are ignored. \(Z_d\) denotes the intersection of the *straight segment*, not a shortest spherical geodesic or its midpoint. All assertions are for fixed unit radius, and every limit is taken as the integer ambient dimension grows.

## Proof

**1. Exact intersection parametrization.** By the reflection symmetry, and conditional on \(E_d\), represent the endpoints, up to a harmless exchange, as
\[
U_d=(\sqrt{1-A_d^2}\,u_d,A_d),\qquad V_d=(\sqrt{1-B_d^2}\,v_d,-B_d),
\]
where \(A_d,B_d>0\) are independent with the distribution of the absolute last coordinate of a uniform point on \(S^{d-1}\). The directions \(u_d,v_d\) are independent surface-uniform points on \(S^{d-2}\), independent of \((A_d,B_d)\). The segment meets \(H_d\) at linear interpolation parameter \(A_d/(A_d+B_d)\), hence
\[
Z_d=\frac{B_d\sqrt{1-A_d^2}\,u_d+A_d\sqrt{1-B_d^2}\,v_d}{A_d+B_d}.
\]
It follows, writing \(C_d=u_d\cdot v_d\), that
\[
Q_d=\frac{B_d^2(1-A_d^2)+A_d^2(1-B_d^2)
+2A_dB_d\sqrt{(1-A_d^2)(1-B_d^2)}\,C_d}{(A_d+B_d)^2}.
\]
For \(d\ge3\), the conditional distribution of \(Z_d\) is invariant under every rotation of the first \(d-1\) coordinates. The unique invariant probability on each sphere of positive radius is surface-uniform; disintegration yields its independence from the radial variable. The crossing point vanishes with probability zero, by absolute continuity.

**2. Gaussian and orthogonality limits.** A uniform point on \(S^{d-1}\) has the law of a standard Gaussian vector divided by its Euclidean norm. The law of large numbers for the denominator therefore implies
\[
\left(\sqrt d\,A_d,\sqrt d\,B_d\right)\ \Rightarrow\ (X,Y),
\]
where \(X,Y\) are independent standard *half-normal* variables, namely absolute values of independent \(N(0,1)\) variables. Independently, rotational symmetry gives \(\mathbb E[C_d]=0\) and \(\mathbb E[C_d^2]=1/(d-1)\), so \(C_d\to0\) in \(L^2\). Substituting \(X_d=\sqrt d A_d\), \(Y_d=\sqrt d B_d\) into the exact formula, and applying the continuous mapping theorem (the limit denominator \(X+Y\) is strictly positive almost surely), yields
\[
Q_d\ \Rightarrow\ Q:=\frac{X^2+Y^2}{(X+Y)^2}.
\]
The limiting value lies almost surely in \((1/2,1)\).

**3. Exact limit law.** The ratio \(T=X/Y\) of independent half-normals is standard half-Cauchy, with density \(2/[\pi(1+t^2)]\) on \(t>0\). Define \(W=|T-1|/(T+1)\). The two inverse images \(T=(1+w)/(1-w)\) and \(T=(1-w)/(1+w)\) give, by an elementary Jacobian computation,
\[
f_W(w)=\frac4{\pi(1+w^2)},\qquad 0<w<1.
\]
Since \(Q=(1+W^2)/2\), its CDF is \(\Pr(W\le\sqrt{2q-1})\), giving the displayed CDF and, by differentiation, the density. Both normalize to one since \(\int_0^1\!4/[\pi(1+w^2)]\,dw=1\). Moreover,
\[
\mathbb E[Q]=\frac4\pi\int_0^1\frac{(1+w^2)/2}{1+w^2}\,dw=\frac2\pi,
\]
\[
\mathbb E[Q^2]=\frac4\pi\int_0^1\frac{(1+w^2)^2/4}{1+w^2}\,dw=\frac4{3\pi}.
\]
The variance is positive, since the limiting law has a positive density on an interval.

**4. Radial and chord-length consequences.** The intersection belongs to the unit ball, so \(0\le Q_d\le1\). Weak convergence on this compact interval implies convergence of \(\mathbb E[Q_d^s]\) for every fixed \(s>0\). The CDF is zero below \(1/2\), implying the announced annular void. Because the variance of \(Q\) is strictly positive, \(Q_d\) cannot converge in probability to a deterministic limit. Finally, \(\mathbb E[(U_d\cdot V_d)^2]=1/d\) by independence and rotational symmetry. Therefore \(U_d\cdot V_d\to0\) in probability, and \(\|U_d-V_d\|^2=2-2U_d\cdot V_d\to2\) in probability.

## Verification

The standalone `check.py` computes the exact density's normalization and first two moments by a numerical integral in the nonsingular \(w\)-coordinate, verifies the half-Cauchy transformation directly, and samples independent Gaussian-normalized sphere endpoints in dimensions three and 500. It compares their directly computed hyperplane-crossing radius distribution against the analytic high-dimensional formula. Run `python check.py` with the package dependencies installed; random checks use fixed seeds and declared tolerances. These finite diagnostics corroborate, but cannot prove, weak convergence.

## Relationship to prior work

Panagiotis Sidiropoulos, *N-sphere chord length distribution*, publicly submitted 20 November 2014 (arXiv:1411.5639), gives the all-dimensional chord-length law for independent uniform spherical endpoints and discusses its dimension dependence. That known chord-length analysis is an input and is not claimed as new; the present claim concerns the **location where such a chord crosses an equatorial hyperplane conditional on crossing**, a different random variable. The full mathematical sections of this paper were inspected for such an intersection law, and it was not stated there.

Dmitriy Bilyk, Alan Chang, Otte Heinävaara, Ryan W. Matzke and Stefan Steinerberger, *A random line intersects \(S^2\) in two probabilistically independent locations* (arXiv:2307.04314, 2023), prove that in \(\mathbb R^3\) the independent-uniform-sphere-endpoint line construction agrees with the kinematic line measure, and that the analogous equality for smooth convex bodies is unique to this three-dimensional sphere setting. This confirms why the present independent-endpoint sampling law must not be confused with invariant random lines as the dimension grows; their theorem does not give the stated high-dimensional conditional crossing law. Its principal statements and relevant proof sections were read.

The related 1989 article by R. Coleman, *Random sections of a sphere*, studies distributions involving random line/plane sections; only its abstract could be accessed. It is a residual historical priority risk, not evidence of non-coverage.

## Limitations

The limit is weak convergence of **squared crossing radii**, with bounded-moment convergence, not a quantitative convergence rate nor convergence of crossing directions in a common ambient space. The disk phenomenon in dimension three is background, not a new result. Equivalent descriptions of the law may be implicit in older stereology or spherical integral-geometry work; available literature and database checks do not establish historical uniqueness. Coleman's plausible related full text was inaccessible. No independent audit has been performed.

## References

1. P. Sidiropoulos, *N-sphere chord length distribution*, arXiv:1411.5639v1, 20 November 2014, https://arxiv.org/abs/1411.5639 and https://arxiv.org/pdf/1411.5639 .
2. D. Bilyk, A. Chang, O. Heinävaara, R. W. Matzke and S. Steinerberger, *A random line intersects \(S^2\) in two probabilistically independent locations*, arXiv:2307.04314, 10 July 2023, https://arxiv.org/abs/2307.04314 .
3. R. Coleman, *Random sections of a sphere*, *Canadian Journal of Statistics* **17** (1989), 27–39, DOI 10.2307/3314760, https://doi.org/10.2307/3314760 .
4. Standard Gaussian normalization of uniform spherical measure and the independent-normal ratio (half-Cauchy) identity are classical probabilistic facts; their short derivations are given above.
