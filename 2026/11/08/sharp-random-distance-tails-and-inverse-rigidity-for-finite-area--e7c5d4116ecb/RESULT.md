# Sharp random-distance tails and inverse rigidity for finite-area hyperbolic cusps

## Finding

For each \(w>0\), let \(C_w\) be the truncated curvature-\(-1\) hyperbolic cusp
\[
C_w=\bigl(\mathbb R/w\mathbb Z\bigr)\times[0,\infty),\qquad
 ds^2=dt^2+e^{-2t}\,dx^2.
\]
Its area is \(w\). Let \(X,Y\) be independent uniform-area points, and let \(D_w\) be their **intrinsic** shortest-path distance in \(C_w\). Set \(R_0(w)=2\operatorname{arsinh}(w/4)\). For every \(R\ge R_0(w)\), the survival function has the exact single-integral law
\[
\mathbb P(D_w>R)=\int_0^{w/2}
\frac{(4/w)(1-2z/w)}{\cosh R+\sqrt{\sinh^2R-z^2}}\,dz.
\]
As \(R\to\infty\), for every fixed \(w>0\),
\[
\boxed{\mathbb P(D_w>R)=e^{-R}+\frac{w^2}{24}e^{-3R}
 +\left(\frac{w^2}{24}+\frac{w^4}{120}\right)e^{-5R}+O_w(e^{-7R}).}
\]
Consequently the universal leading term hides the cusp width, while the first nonuniversal term recovers it exactly:
\[
\boxed{w=\sqrt{24\lim_{R\to\infty}e^{3R}
\bigl(\mathbb P(D_w>R)-e^{-R}\bigr)}.}
\]
Moreover, whenever \(0<w_1<w_2\), \(D_{w_1}\) is strictly smaller than \(D_{w_2}\) in first-order stochastic order: for **every** \(R>0\),
\[
\mathbb P(D_{w_1}>R)<\mathbb P(D_{w_2}>R).
\]
Finally \(\mathbb E[e^{pD_w}]<\infty\) precisely for real \(p<1\), and all ordinary positive polynomial moments are finite.

## Assumptions and scope

The space is the full *truncated cusp as a manifold with horocyclic boundary*, equipped with its intrinsic path metric, not a cusp sitting inside an unspecified larger complete hyperbolic surface. The curvature is normalized to \(-1\); the boundary horocycle has length \(w\). Points are sampled independently using normalized area measure. Width \(w\) is fixed before taking the large-distance limit. The distribution integral is asserted only at and beyond the explicit threshold \(R_0(w)\); the asymptotic and stochastic-order assertions apply in their indicated ranges.

## Proof

**Hyperbolic distance and the quotient.** In upper half-plane coordinates \((x,y)\) with \(y=e^t\), the lift of \(C_w\) is the horoball \(y\ge1\), which is geodesically convex. Every geodesic between points of this horoball remains in the horoball. Hence quotient shortest-path distance is the minimum of hyperbolic-plane distances between lifts related by integral translations of \(x\) through \(w\). For independent normalized-area points, the height coordinates \(T_1,T_2\) have density \(e^{-t}\) for \(t\ge0\), and their horizontal coordinates are independent uniform variables on the circle of length \(w\). Thus the shortest circular separation \(U\) is uniform on \([0,w/2]\), independently of the heights. The upper half-plane distance formula gives
\[
\cosh D_w=\cosh(T_1-T_2)+\frac{U^2}{2e^{T_1+T_2}}.
\]

**Independent exponential variables and triangular mixing law.** Put \(S=|T_1-T_2|\) and \(M=\min(T_1,T_2)\). The memoryless exponential law or direct change of variables shows that \(S\sim\operatorname{Exp}(1)\) and \(M\sim\operatorname{Exp}(2)\), independently. Let \(Z=Ue^{-M}\). Then
\[
\cosh D_w=\cosh S+\tfrac12 Z^2e^{-S},
\qquad f_Z(z)=\frac4w\left(1-\frac{2z}{w}\right)
\mathbf 1_{[0,w/2]}(z).
\]
For example, the density follows by integrating the conditional uniform density \(2e^m/w\) against \(2e^{-2m}\,dm\) over \(0\le m\le\log(w/(2z))\). In particular \(Z=wV\), where the law of \(V\in[0,1/2]\) is independent of \(w\), and
\[
\mathbb E[Z^k]=\frac{2(w/2)^k}{(k+1)(k+2)}
\quad (k>-1).
\]

**Exact far-tail integral.** Conditional on \(Z=z\), put \(v=e^S\ge1\). For \(R>0\), the inequality \(D_w>R\) is equivalent to
\[
v^2-2(\cosh R)v+(1+z^2)>0.
\]
When \(R\ge2\operatorname{arsinh}(w/4)\) and \(z\in[0,w/2]\), we have \(z\le2\sinh(R/2)\le\sinh R\). The quadratic has real roots \(v_-(R,z)\le1\le v_+(R,z)\), where
\[
v_+(R,z)=\cosh R+\sqrt{\sinh^2 R-z^2}.
\]
Consequently \(D_w>R\) if and only if \(S>\log v_+(R,z)\), apart from null boundary events. Because \(S\sim\operatorname{Exp}(1)\), the conditional probability equals \(1/v_+(R,z)\). Integrating the verified density of \(Z\) proves the claimed exact integral.

**Uniform large-distance expansion.** Write \(\lambda=e^{-R}\). For fixed \(w\), uniformly for \(z\in[0,w/2]\), binomial expansion yields
\[
\cosh R+\sqrt{\sinh^2R-z^2}
=\lambda^{-1}\left(1-z^2\lambda^2-(z^2+z^4)\lambda^4+O_w(\lambda^6)\right).
\]
Inverting gives
\[
\frac1{v_+(R,z)}=\lambda+z^2\lambda^3+(z^2+2z^4)\lambda^5+O_w(\lambda^7).
\]
The triangular mixing law has \(\mathbb E[Z^2]=w^2/24\) and \(\mathbb E[Z^4]=w^4/240\). Integration establishes all coefficients and the \(O_w(e^{-7R})\) remainder. The width-recovery formula is immediate.

**Strict stochastic ordering and moment threshold.** Couple all widths by the *same* \(S\sim\operatorname{Exp}(1)\) and \(V\) with density \(4(1-2v)\) on \([0,1/2]\), using
\[
D_w=\operatorname{arcosh}\!\left(\cosh S+\tfrac12w^2V^2e^{-S}\right).
\]
For positive \(V\), this is strictly increasing in \(w\). To prove strict inequality of survival probabilities at every \(R>0\), choose \(S\) slightly below \(R\); the threshold in \(wV\) at which \(D_w=R\) is positive and tends continuously to zero as \(S\uparrow R\). With \(w_2>w_1\), a positive-measure interval of \(V\) makes \(D_{w_1}<R<D_{w_2}\). The two-dimensional joint law gives such pairs positive probability. Finally, \(\mathbb P(D_w>R)\sim e^{-R}\). Tail integration, \(\mathbb E[e^{pD_w}]=1+p\int_0^\infty e^{pR}\mathbb P(D_w>R)\,dR\) for \(p>0\), yields finiteness exactly for \(p<1\); for \(p\le0\) the exponential moment is bounded. The same tail estimate yields finiteness of all positive polynomial moments.

## Verification

A standalone standard-library Python checker, `check_cusp.py`, evaluates the exact integral via composite Simpson quadrature, simulates independent area-uniform points directly in upper half-plane coordinates, reconstructs the intrinsic quotient distance using the nearest horizontal translate, and independently verifies the exponential-coordinate factorization. Across five width/radius pairs it tests 1,100,000 pairs with conservative binomial tolerances. It also checks the displayed three-term far-tail expansion numerically at multiple radii. The checker returns `TRUNCATED_HYPERBOLIC_CUSP_TAIL_AND_MC_OK 1100000`. Monte Carlo is supplementary; the infinite-range claims rest on the proof above.

## Relationship to prior work

Borthwick (2010), arXiv:1006.5478, identifies truncated hyperbolic cusp coordinates and their role in spectral resonance asymptotics; his results concern Laplacian resonances rather than the distance distribution of two normalized-area points. Gadre (2014), arXiv:1408.5812, studies random geodesic **cusp excursions along a single typical ray**, not independent area-uniform pairs or inverse recovery of the cusp width from the far-distance tail. Both were materially inspected in accessible full-text form, including their introduction and statements of results. Targeted mathematical-literature searches and independent research-record searches found no equivalent exact tail integral or inverse coefficient, but absence from indexed sources is not a proof of historical novelty.

## Limitations

No full-distance CDF for \(0<R<R_0(w)\) is claimed. The result does not identify the distance law for points in a complete finite-area hyperbolic surface when shortest routes may leave a chosen cusp neighborhood. It does not treat nonconstant curvature, variable-shape cross-sections, or higher-dimensional cusps. The expansion is for each fixed \(w\), not uniform as \(w\to\infty\). Independent expert review and a broader historical-priority check have not been performed.

## References

1. D. Borthwick, *Sharp geometric upper bounds on resonances for surfaces with hyperbolic ends*, arXiv:1006.5478 (first submitted 2010-06-28), https://arxiv.org/abs/1006.5478 .
2. V. Gadre, *Partial sums of excursions along random geodesics and volume asymptotics for thin parts of moduli spaces of quadratic differentials*, arXiv:1408.5812 (first submitted 2014-08-25), https://arxiv.org/abs/1408.5812 .
