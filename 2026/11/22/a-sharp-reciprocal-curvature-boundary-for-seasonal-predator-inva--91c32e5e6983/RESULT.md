# A sharp reciprocal-curvature boundary for seasonal predator invasion

## Finding

Consider logistic prey subject to any positive, continuous, nonconstant periodic carrying capacity and an initially rare predator with the generalized Holling-III feeding law derived from density-mediated predator activation. The sign of
\[
\boxed{C^2-BD}
\]
is the **sharp universal boundary** for whether a fluctuating environment can lower the predator's invasion exponent relative to the constant environment having the same *harmonic-mean carrying capacity*.

For every positive waveform and every forcing period, when \(C^2\ge BD\) the rare-predator invasion exponent is **strictly greater** than its constant-harmonic-capacity counterpart. Conversely, when \(C^2<BD\), a positive smooth periodic capacity exists for which it is strictly smaller. At identical neutral static benchmarks, the two signs produce strict invasion versus exclusion, respectively. The conclusion is about **linear invasion of the predator-free periodic state**; it is not a statement of nonlinear global coexistence or extinction.

## Assumptions and scope

Let \(r,e,m,A,B,C,D>0\), let \(K:\mathbb R\to(0,\infty)\) be continuous and periodic with some period \(T>0\), and consider, for \(x>0\), \(y\ge0\),
\[
\dot x=rx\left(1-\frac{x}{K(t)}\right)-f(x)y,
\qquad \dot y=y(ef(x)-m),\qquad
f(x)=\frac{Ax^2}{B+Cx+Dx^2}.
\]
These are the spatially homogeneous predator–prey reactions with the density-modulated activation law, now permitting a periodically changing prey capacity. They impose no particular amplitude, waveform, or forcing frequency. The constant case is allowed for equality.

Denote by \(x_p(t)>0\) the unique positive periodic predator-free prey solution; it exists for every such \(K\). Define
\[
K_{\mathrm H}:=\left(\frac1T\int_0^T\frac{dt}{K(t)}\right)^{-1},\quad
\lambda_K:=\frac eT\int_0^T f(x_p(t))\,dt-m,\quad
\lambda_{\mathrm H}:=e f(K_{\mathrm H})-m.
\]
Here \(K_{\mathrm H}\) denotes a harmonic mean, **not** a Hopf bifurcation value. The exponent \(\lambda_K\) governs the Floquet multiplier \(\exp(T\lambda_K)\) for a rare predator; the prey-only periodic orbit is transversely attracting for \(\lambda_K<0\) and repelling for \(\lambda_K>0\).

## Proof

Set \(u(t)=1/x_p(t)\). The predator-free logistic equation becomes the linear scalar equation
\[
\dot u=-ru+\frac r{K(t)}.
\]
It has a unique positive periodic solution, obtained by convolution with the positive exponentially decaying Green kernel. Any solution with positive initial data converges to this solution. Integrating over a period yields the exact identity
\[
\overline{u}=\frac1T\int_0^T\frac{dt}{K(t)}=\frac1{K_{\mathrm H}}.
\]
The per-capita intake written in reciprocal prey is
\[
g(u):=f(1/u)=\frac A{Bu^2+Cu+D},
\qquad g''(u)=\frac{2A(3B^2u^2+3BCu+C^2-BD)}{(Bu^2+Cu+D)^3}.
\]
When \(C^2\ge BD\), \(g''(u)>0\) for every \(u>0\). Hence strict Jensen convexity gives
\[
\lambda_K-\lambda_{\mathrm H}
=e\big(\overline{g(u)}-g(\overline u)\big)\ge0,
\]
with equality exactly for constant \(u\), equivalently constant \(K\). No high-frequency averaging approximation is used. This establishes the frequency-independent guarantee, including the strict result at the neutral benchmark \(m=ef(K_{\mathrm H})\).

To prove the boundary sharp, suppose \(C^2<BD\). The numerator of \(g''(u)\) is then negative on some interval \((0,u_c)\). Choose \(u_0>0\) there, a frequency \(\omega>0\), and an amplitude \(\delta>0\) small enough that \(u_0\pm\delta>0\), \(g''<0\) throughout that interval, and \(\delta\sqrt{1+(\omega/r)^2}<u_0\). Set
\[
u(t)=u_0+\delta\cos(\omega t),\qquad
K(t)=\frac1{u_0+\delta\cos(\omega t)-(\delta\omega/r)\sin(\omega t)}.
\]
This capacity is positive and smooth. Direct differentiation gives \(\dot u=-ru+r/K\), so \(u\) is precisely the positive periodic inverse-prey solution. Its mean is \(u_0\). Strict Jensen **concavity** on its full range gives
\[
\lambda_K-\lambda_{\mathrm H}=e(\overline{g(u)}-g(u_0))<0.
\]
Thus the parameter condition is necessary as well as sufficient for the claimed universal nonnegative comparison, and the reverse sign is achieved by a legitimate periodic capacity.

For a fully explicit reversal, take \(r=e=A=B=C=1\), \(D=4\), \(u_0=1/4\), \(\delta=1/10\), \(\omega=1\), and
\[
K(t)=\left(\frac14+\frac1{10}(\cos t-\sin t)\right)^{-1}.
\]
Its inverse is everywhere positive because \(1/4>\sqrt2/10\), and \(K_{\mathrm H}=4\). On \(u\in[3/20,7/20]\), \(3u^2+3u-3<0\). Thus, at mortality \(m=f(4)=16/69\), the constant-capacity benchmark is neutral but the seasonal predator Floquet exponent is **strictly negative**. With the same \(K(t)\) and \(r=e=A=B=C=D=1\), take \(m=f(4)=16/21\); strict convexity instead gives a **strictly positive** seasonal invasion exponent relative to the same neutral benchmark. Both examples lie within positive mechanistic parameter ranges.

## Verification

The accompanying `verify.py` checks the exact reciprocal-curvature polynomial and the signs on the stated rational example intervals using rational arithmetic. It also independently integrates the periodic intake numerically for each example and verifies the period-averaged inverse capacity. Finite numerical quadrature is supplementary; the mathematical inequalities follow from the analytic proof and exact curvature bounds.

## Relationship to prior work

Buttà (2026) derives the generalized type-III response from density-modulated activation of predators; its homogeneous reaction is the starting object here. In the source's kinetic notation, \(A=\alpha\kappa a\), \(B=\beta\), \(C=\alpha\), \(D=\alpha\beta\kappa h\). Consequently, the sharp curvature boundary reads \(\alpha\ge\beta^2\kappa h\). The result concerns the predator-free periodic state when the prey capacity is seasonally varying, a setting distinct from that source's kinetic derivation.

Sarrah, Alanazi, Yavuz and Saber (2026) investigate periodic carrying capacity in a generalized Holling-III model, emphasizing numerical bifurcations. Lamontagne, Coutu and Rousseau (2008) analyze bifurcations of the corresponding autonomous generalized Holling-III system; their autonomous Hopf conditions are not a uniform comparison of invasion exponents under arbitrary positive periodic capacities. The present result compares the seasonal and constant **harmonic-capacity** environments exactly, establishes a sharp handling–activation coefficient boundary for **all periods**, and supplies a smooth counterexample on the other side. It does not claim the feeding function or logistic reciprocal transformation as new.

## Limitations

The comparison is local to invasion near the predator-free periodic orbit. It does not prove persistence of both populations after successful invasion, nor exclusion from every positive initial condition after negative invasion. It assumes a strictly positive continuous periodic capacity, a logistic prey-only equation, and the stated generalized type-III response with positive coefficients. The condition \(C^2<BD\) proves the *existence* of a counterexample waveform, not that every waveform reverses the inequality. The theorem is analytic but has not undergone independent audit. Historical priority beyond the inspected literature may require further review.

## References

1. P. Buttà, *From kinetic activation dynamics to Holling type reaction-diffusion predator-prey systems*, arXiv:2610.32603v1 (first released 2026-10-23), https://arxiv.org/abs/2610.32603.
2. A. Sarrah, F. J. Alanazi, M. Yavuz, S. Saber, *The Effects of Fluctuating Carrying Capacity on the Dynamics of a Holling-Type III Predator–Prey Model*, Journal of Mathematics (2026), doi:10.1155/jom/5067259, https://doi.org/10.1155/jom/5067259.
3. Y. Lamontagne, C. Coutu, C. Rousseau, *Bifurcation Analysis of a Predator–Prey System with Generalised Holling Type III Functional Response*, Journal of Dynamics and Differential Equations 20 (2008), 535–571, doi:10.1007/s10884-008-9102-9, https://dms.umontreal.ca/~rousseac/LCR.pdf.
