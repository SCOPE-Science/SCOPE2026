# Exact extreme stretch and a thin-cylinder crossover for random sidewall pairs

## Finding

Let \(S_{r,H}\) denote only the lateral surface of the right circular cylinder
\[
S_{r,H}=\{(r\cos\phi,r\sin\phi,z):0\le\phi<2\pi,\ 0\le z\le H\},\qquad r,H>0.
\]
Independently sample \(P,Q\) from its normalized surface area. Write \(d_g(P,Q)\) for intrinsic shortest-path distance **restricted to this sidewall**, \(d_e(P,Q)=\|P-Q\|_2\), and \(Z=d_g/d_e\), defined almost surely. Put \(h=H/r\) and \(\beta=(\pi^2-4)/(16\pi)>0\).

**Exact law and shape ordering.** The essential range is \([1,\pi/2]\), and the upper endpoint is attained exactly by antipodal points at equal heights. For every threshold \(1<t<\pi/2\), let \(\theta_t\in(0,\pi)\) be the unique solution of
\[
\frac{\theta_t}{2\sin(\theta_t/2)}=t,
\quad q_t(\theta)=\sqrt{\frac{\theta^2-4t^2\sin^2(\theta/2)}{t^2-1}}\quad(\theta_t\le\theta\le\pi).
\]
With \(m_t(\theta;h)=\min\{1,q_t(\theta)/h\}\), the complete scale-free exceedance distribution is the one-dimensional quadrature
\[
\boxed{\mathbb P(Z>t)=\frac1\pi\int_{\theta_t}^{\pi}\big[2m_t(\theta;h)-m_t(\theta;h)^2\big]d\theta.}\tag{1}
\]
For each fixed \(t\in(1,\pi/2)\), this probability is continuous and **strictly decreasing** in \(h\), from \((\pi-\theta_t)/\pi\) to zero. Therefore one exceedance probability at any such threshold determines the dimensionless aspect ratio \(H/r\) uniquely.

**Sharp fixed-shape upper tail.** At every fixed \(h>0\),
\[
\boxed{\mathbb P\big(Z>\pi/2-\varepsilon\big)=\frac{32}{3h\sqrt{\pi(\pi^2-4)}}\,\varepsilon^{3/2}+O_h(\varepsilon^2).}\tag{2}
\]
Conditional on this event, define the angular deficit \(\delta=\pi-\theta\) and normalized height difference \(x=|z_P-z_Q|/r\). The three variables
\[
\left(\frac{\delta}{2\varepsilon},\ \frac{\beta x^2}{\varepsilon},\ 1-\frac{\delta}{2\varepsilon}-\frac{\beta x^2}{\varepsilon}\right)
\]
converge jointly in law to \(\operatorname{Dirichlet}(1,\tfrac12,1)\) as \(\varepsilon\downarrow0\). This law records the linear angular and quadratic axial contributions to rare extreme distortion.

**Sharp thin-cylinder transition.** For fixed \(\lambda>0\), put \(H/r=\lambda\sqrt\varepsilon\). Uniformly for \(\lambda\) in each bounded positive interval,
\[
\boxed{\mathbb P\big(Z>\pi/2-\varepsilon\big)
=\varepsilon F(\lambda)+O_{\Lambda}(\varepsilon^2),\qquad
F(\lambda)=\begin{cases}
\dfrac2\pi-\dfrac{\beta\lambda^2}{3\pi},&0\le\lambda\sqrt\beta\le1,\\[4pt]
\dfrac8{3\pi\lambda\sqrt\beta}-\dfrac1{\pi\beta\lambda^2},&\lambda\sqrt\beta\ge1.
\end{cases}}\tag{3}
\]
The value at \(\lambda=0\) denotes the limiting circular boundary model. The crossover function is positive and strictly decreasing, is \(C^2\) but not \(C^3\) at \(\lambda_*=1/\sqrt\beta\), satisfies \(F(0)=2/\pi\), and has \(F(\lambda)\sim 8/(3\pi\sqrt\beta\lambda)\) for large \(\lambda\). Thus fixed positive height has a \(3/2\)-power upper tail whereas a collapsing height of order \(r\sqrt\varepsilon\) has a first-power law with an explicit nonanalytic transition.

## Assumptions and scope

The surface has positive radius and height, with no end disks in either the sampling support or the allowed paths. Boundary circles are included in the metric but have zero area sampling probability. The random endpoints are independent and uniform in the product angular-height surface-area coordinates. The intrinsic metric permits winding around the cylinder but chooses the shortest homotopy class. The Euclidean denominator is the ambient three-dimensional straight chord, not a planar developed chord. The fixed-shape asymptotic keeps \(h>0\) constant. In the critical-window asymptotic \(h=\lambda\sqrt\varepsilon\) is varying and the bound is uniform only for bounded \(\lambda\); no uniform fixed-shape estimate as \(h\downarrow0\) is asserted.

## Proof

**1. Exact reduction.** Let \(\theta\in[0,\pi]\) be the smaller circular angular separation of two independent uniform angles. The quotient-circle difference is uniform, so \(\theta\) has density \(1/\pi\). If \(V=|z_P-z_Q|/H\), then \(V\in[0,1]\) is independent of \(\theta\) and has density \(2(1-v)\). Writing \(x=hV\), unroll the cylinder's sidewall. Its strip is convex in the axial coordinate; the shortest lifted straight segment uses angular separation \(r\theta\), so
\[
d_g^2=r^2(\theta^2+x^2),\quad d_e^2=r^2(4\sin^2(\theta/2)+x^2),\quad
Z(\theta,x)=\sqrt{\frac{\theta^2+x^2}{4\sin^2(\theta/2)+x^2}}.\tag{4}
\]
All formulas hold for distinct endpoints, a probability-one event. Since \(\theta\ge2\sin(\theta/2)\), \(Z\ge1\). For each \(\theta\in(0,\pi]\), differentiating \(Z^2\) with respect to \(x^2\) gives a negative derivative. Thus \(Z(\theta,x)\le\theta/[2\sin(\theta/2)]\), with equality only at \(x=0\). The last ratio increases strictly from \(1\) to \(\pi/2\) on \((0,\pi]\) because \(\sin u-u\cos u>0\) for \(u\in(0,\pi/2]\). This proves the sharp endpoint and equality configurations.

**2. Full distribution and inverse ordering.** For \(1<t<\pi/2\), inequality \(Z(\theta,hV)>t\) first requires \(\theta>\theta_t\). Squaring and rearranging (4) then gives \(hV<q_t(\theta)\), where \(q_t\) is defined in the finding. The height-difference law satisfies \(\mathbb P(V<u)=2u-u^2\) for \(0\le u\le1\), proving (1). Its integrand is nonincreasing in \(h\), and strictly decreases on a positive-measure interval adjacent to \(\theta_t\) for every pair \(0<h_1<h_2\). Dominated convergence proves continuity and the limits at \(h=0,\infty\). Strict monotonicity gives the asserted shape identification from a fixed threshold.

**3. Local normal form and localization.** Put \(\delta=\pi-\theta\). The unique maximizing configuration in the compact sampling domain \([0,\pi]\times[0,h]\) is \((\delta,x)=(0,0)\). Taylor expansion of the explicit analytic function (4), uniformly near the maximizing corner, gives
\[
\frac\pi2-Z(\pi-\delta,x)
=\frac\delta2+\beta x^2+O(\delta^2+\delta x^2+x^4).\tag{5}
\]
Since the two leading coefficients are strictly positive and there are no other maximizers, the event \(Z>\pi/2-\varepsilon\) is contained, for small \(\varepsilon\), in \(0\le\delta\le C\varepsilon\), \(0\le x\le C\sqrt\varepsilon\). These bounds follow by compactness away from the maximizer and by (5) in a sufficiently small neighborhood. On this event the remainder in (5) is uniformly \(O(\varepsilon^2)\).

**4. Fixed-height asymptotic and joint law.** The joint density of \((\delta,x)\) is
\[
\frac{2}{\pi h}\left(1-\frac{x}{h}\right),\qquad 0<\delta<\pi,\quad0<x<h.
\]
Scale \(\delta=\varepsilon s\) and \(x=\sqrt\varepsilon\,t\). The rescaled event converges to the bounded sublevel domain \(E=\{s,t\ge0:s/2+\beta t^2<1\}\), whose area equals \(4/(3\sqrt\beta)\). The leading constant is \((2/(\pi h))|E|=8/(3\pi h\sqrt\beta)=32/(3h\sqrt{\pi(\pi^2-4)})\). The \(O(\varepsilon^2)\) Taylor remainder perturbs the rescaled boundary by \(O(\varepsilon)\), while the density correction \(-x/h\) contributes \(O_h(\varepsilon^2)\) after integration. This proves (2). Dominated convergence also gives the uniform distribution of \((s,t)\) on \(E\) conditionally on the rare event. The transformation \(u=s/2\), \(v=\beta t^2\) has Jacobian proportional to \(v^{-1/2}\), and the slack \(1-u-v\) has exponent zero. The standard simplex density is exactly \(\operatorname{Dirichlet}(1,\tfrac12,1)\), establishing the conditional limit.

**5. Thin-cylinder transition.** Now set \(h=\lambda\sqrt\varepsilon\), so \(x=\lambda\sqrt\varepsilon V\) with the same triangular density for \(V\). Using (5), for bounded \(\lambda\), the allowed angular deficit at fixed \(V=v\) is
\[
0\le\delta<2\varepsilon(1-\beta\lambda^2v^2)_++O_\Lambda(\varepsilon^2).
\]
The angular density is \(1/\pi\), hence integration against \(2(1-v)\,dv\) gives
\[
\mathbb P(Z>\pi/2-\varepsilon)=\frac{4\varepsilon}{\pi}\int_0^1(1-v)(1-\beta\lambda^2v^2)_+dv+O_\Lambda(\varepsilon^2).\tag{6}
\]
For \(L=\lambda\sqrt\beta\le1\), the integral is \(1/2-L^2/12\). For \(L\ge1\), integrating only up to \(v=1/L\) gives \(2/(3L)-1/(4L^2)\). These are (3). Elementary differentiation at \(L=1\) shows matching derivatives through order two and a nonzero third-derivative jump \(8/\pi\) in the variable \(L\). The endpoint and large-\(\lambda\) conclusions are immediate.

## Verification

The independent numerical implementations in `verify.py` use the exact single-quadrature CDF, direct two-dimensional midpoint quadrature of the original stretch condition, and a separate sampling of the limiting parabolic sublevel set. Tests compare three aspect-threshold combinations by different integrals, fixed-shape upper tails at multiple deficits, thin-height crossover values across the transition, strict stochastic ordering, inverse recovery, and limiting Dirichlet means. The standard-library-only checker prints `CYLINDER_STRETCH_TAIL_CHECKS_OK 22 Dirichlet_samples 99896` when executed with its fixed random seed. These tests illustrate and check calculations; the infinite-limit claims follow from the analytic argument above, not numerical extrapolation.

## Relationship to prior work

Sijbers, Verdonk and Huysmans (WSCG 2005) explicitly use the right circular cylinder as an intrinsic geodesic domain, describe helical geodesics, and exploit local plane isometry. Chen and Chen (arXiv:1011.5320v1, 2010-11-24) develop algorithms for shortest paths on periodic parametric surfaces. Neither study presents an independent uniform-pair distribution of the **ratio** of surface geodesic distance to ambient chord distance, or its thin-height limit.

The published *Full intrinsic pair-distance law on a finite circular cylinder* concerns the marginal law of \(d_g\) alone. The published *A sharp two-moment ambiguity transition and rational three-moment inverse for cylinder sidewalls* concerns ambient \(d_e\) moments alone. These separate marginal statistics do not determine the joint law of \((d_g,d_e)\), hence cannot determine the ratio distribution or conditional extreme configurations without additional coupling information. *Sharp all-power geodesic-distance aspect ratios for fixed-area flat cylinders* likewise involves the marginal intrinsic law and fixed-area moment optimization, not the ratio distribution. Random invariant-line chord results use a different sampling measure. Some earlier product-circle distortion research treats closed products with uniform circular differences, not the triangular height-difference law of a finite cylinder. The contribution here is the exact coupled ratio law, sharp \(3/2\)-tail, Dirichlet limit, and explicit \(C^2\)-but-not-\(C^3\) collapsing-height crossover. Historical coverage outside accessible full texts is not ruled out.

## Limitations

No claim is made for capped cylinders whose paths may traverse end disks, arbitrary developable embeddings, nonuniform endpoint densities, the complete joint distribution of \((d_g,d_e)\), or asymptotic uniformity when the critical parameter \(\lambda\) diverges with \(\varepsilon\downarrow0\). The result is for a fixed right circular sidewall and for its specified controlled thin-height collapse. The exact first public date of the older WSCG2005 proceedings was not established; the precisely documented dated archival starting reference is the 2010-11-24 arXiv posting of Chen and Chen. Independent mathematical verification and comprehensive historical-priority checking remain outstanding.

## References

1. W.-H. Chen and S.-G. Chen, *Computation of the shortest path between two curves on a parametric surface by geodesic-like method*, arXiv:1011.5320v1, first posted 2010-11-24. https://arxiv.org/abs/1011.5320
2. J. Sijbers, B. Verdonk and T. Huysmans, *Parameterization of Tubular Surfaces on the Cylinder*, Journal of WSCG 13 (WSCG2005 conference held January 31–February 4, 2005). https://visielab.uantwerpen.be/sites/default/files/huysmans2005.pdf
3. *Full intrinsic pair-distance law on a finite circular cylinder*, public mathematical-result record (2026). https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-full-intrinsic-pair-distance-law-on-a-finite-circular-cylinder--fff233fea091
4. *A sharp two-moment ambiguity transition and rational three-moment inverse for cylinder sidewalls*, public mathematical-result record (2026). https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-a-sharp-two-moment-ambiguity-transition-and-rational-three-momen--99e743811ab8
5. *Sharp all-power geodesic-distance aspect ratios for fixed-area flat cylinders*, public mathematical-result record (2026). https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-sharp-all-power-geodesic-distance-aspect-ratios-for-fixed-area-f--a201cfb22c94
