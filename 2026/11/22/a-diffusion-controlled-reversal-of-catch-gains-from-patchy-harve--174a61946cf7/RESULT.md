# A diffusion-controlled reversal of catch gains from patchy harvesting

## Finding

Fix the *mean* (not the spatial distribution) of fishing effort in a spatial Beverton–Holt population with no-flux dispersal. **Every nonconstant effort allocation strictly raises average biomass at a positive stationary solution**, yet reallocating effort can either increase or decrease aggregate catch. The local catch response changes sign at an exactly computable dispersal threshold, determined by a Laplace eigenvalue and the position of the homogeneous fishery on its yield curve.

In the concrete one-dimensional model
\[
0=D B''+\frac{4B}{1+B}-\left(2+\varepsilon\cos x\right)B,
\qquad x\in(0,\pi),\quad B'(0)=B'(\pi)=0,
\]
the average fishing effort is fixed at \(3/2\) and the local harvest efficiency is one. The unique positive stationary biomass \(B_\varepsilon\), its mean \(\overline B_\varepsilon\), and the mean catch \(Y_\varepsilon=\overline{(3/2+\varepsilon\cos x)B_\varepsilon}\) satisfy
\[
\boxed{\overline B_\varepsilon=1+
\frac{2D+1}{4(1+D)^2}\varepsilon^2+O(\varepsilon^3)},
\]
\[
\boxed{Y_\varepsilon=\frac32+
\frac{2D-1}{8(1+D)^2}\varepsilon^2+O(\varepsilon^3)}.
\]
Thus for each fixed \(D<1/2\) spatial effort heterogeneity decreases catch for sufficiently small nonzero \(\varepsilon\), while for each fixed \(D>1/2\) it increases catch, **even though it raises mean standing biomass on both sides**. No sign of the higher-order catch response at \(D=1/2\) is asserted.

The result extends to arbitrary mean-zero effort profiles with a precisely specified Neumann spectral multiplier, and supplies an exact nonperturbative stock inequality at every positive stationary solution.

## Assumptions and scope

Let \(L,D,a,b,m,\eta,u_0>0\), \(\Omega=(0,L)\), and \(h=m+\eta u_0<a/b\). Define
\[
q=\frac{a}{h}-b>0,\quad r=\frac{bh}{a}\in(0,1),
\quad c=h(1-r)>0.
\]
For a nonzero \(v\in C^2([0,L])\) with \(\overline v=L^{-1}\int_0^L v=0\), take \(u_\varepsilon(x)=u_0+\varepsilon v(x)\); \(|\varepsilon|\) is sufficiently small to keep effort nonnegative. The stationary equation is
\[
0=D B_\varepsilon''+\frac{a B_\varepsilon}{b+B_\varepsilon}
-(m+\eta u_\varepsilon)B_\varepsilon,
\qquad B_\varepsilon'(0)=B_\varepsilon'(L)=0.
\]
Write \(\overline f=L^{-1}\int_0^L f\). The average sustainable catch is \(Y_\varepsilon=\eta\overline{u_\varepsilon B_\varepsilon}\); the effort budget \(\overline{u_\varepsilon}=u_0\) never changes. The Neumann modes are \(\phi_j(x)=\sqrt2\cos(j\pi x/L)\), with eigenvalues \(\lambda_j=(j\pi/L)^2\), \(j\ge1\). Put \(v_j=\overline{v\phi_j}\) and \(A_j=c+D\lambda_j\).

For every fixed \(D>0\), the uniform state \(q\) has a unique strictly positive stationary continuation \(B_\varepsilon\) for all sufficiently small \(|\varepsilon|\), analytic in \(\varepsilon\) with values in Neumann \(C^{2,\gamma}\) for any fixed \(0<\gamma<1\). It is locally linearly stable.

The expansions are
\[
\overline B_\varepsilon=q+
\varepsilon^2\frac{\eta^2 q}{c}
\sum_{j\ge1}|v_j|^2\left(\frac1{A_j}-\frac{rc}{A_j^2}\right)
+O(\varepsilon^3),
\tag{1}
\]
\[
Y_\varepsilon=\eta u_0q+
\varepsilon^2\eta^2q\sum_{j\ge1}\frac{|v_j|^2}{A_j}
\left[\frac{bh^2/a-m}{c}-\frac{(h-m)r}{A_j}\right]
+O(\varepsilon^3).
\tag{2}
\]
The quadratic stock coefficient is strictly positive. If \(bh^2/a\le m\), the quadratic catch coefficient is strictly negative for every finite \(D>0\) and every nonzero \(v\). If \(bh^2/a>m\), the catch coefficient is negative at all sufficiently small diffusion coefficients, and positive at all sufficiently large diffusion coefficients.

More sharply, when \(v\) is a nonzero single Neumann mode \(\phi_j\), the quadratic catch coefficient switches sign exactly once, at
\[
\boxed{D_j^*=\frac{hm(1-r)^2}{\lambda_j(bh^2/a-m)}}.
\tag{3}
\]
It is negative for \(0<D<D_j^*\), zero for \(D=D_j^*\), and positive for \(D>D_j^*\). The statement is about the leading quadratic coefficient, not a finite-amplitude global harvest optimum.

For any strictly positive twice differentiable stationary profile \(B\) under any continuous nonnegative effort \(u\) with \(\overline u=u_0\), without requiring small heterogeneity, the exact bound is
\[
\boxed{\overline B\ge
\frac{a}{h-D\overline{|(\log B)'|^2}}-b\ge q},
\tag{4}
\]
where the denominator is positive; the last inequality is strict for any nonconstant \(u\) admitting such a positive solution. This global stock bound is independent of the perturbative catch calculation.

## Proof

**1. Positive branch and uniqueness.** Let \(f(s)=as/(b+s)-hs\). Then \(f(q)=0\) and \(f'(q)=-c<0\). The derivative of the Neumann stationary equation in \(B\) at \((q,0)\) is \(D\partial_{xx}-c\), an isomorphism from Neumann \(C^{2,\gamma}\) to \(C^{0,\gamma}\). The analytic implicit-function theorem therefore yields a positive analytic local stationary branch. Its linearization remains strictly stable for sufficiently small \(|\varepsilon|\). Two positive stationary solutions cannot differ: at a maximum \(k>1\) of their ratio \(B_1/B_2\), we have \((B_1-kB_2)''\le0\), including a Neumann boundary maximum, but the two stationary equations give
\[
D(B_1-kB_2)''=B_1 a\left(\frac1{b+B_2}-\frac1{b+B_1}\right)>0,
\]
a contradiction. Interchange the solutions to exclude the opposite ordering. This proves uniqueness of the positive stationary branch among all positive classical solutions for small perturbations.

**2. Nonperturbative increase in average biomass.** Divide the positive stationary equation by \(B\), integrate, and use Neumann integration by parts:
\[
h=a\overline{\frac1{b+B}}+D\overline{|(\log B)'|^2}.
\]
The map \(s\mapsto (b+s)^{-1}\) is strictly convex. Jensen's inequality gives \(h-D\overline{|(\log B)'|^2}\ge a/(b+\overline B)\), proving (4). A nonconstant effort cannot have constant \(B\), so Jensen is strict and \(\overline B>q\).

**3. Exact perturbative response.** Write \(B_\varepsilon=q+\varepsilon w+\varepsilon^2 z+O(\varepsilon^3)\). With \(\mathcal L=c-D\partial_{xx}\), the first two equations are
\[
\mathcal Lw=-\eta qv,
\qquad \mathcal Lz=\frac{f''(q)}2w^2-\eta vw,
\quad \frac{f''(q)}2=-\frac{bh^3}{a^2}.
\]
Using the orthonormal Neumann modes,
\[
w=-\eta q\sum_{j\ge1}\frac{v_j}{A_j}\phi_j,
\quad \overline w=0,
\quad \overline{vw}=-\eta q\sum_{j\ge1}\frac{|v_j|^2}{A_j},
\quad \overline{w^2}=\eta^2q^2\sum_{j\ge1}\frac{|v_j|^2}{A_j^2}.
\]
Average the second-order equation, noting \(bh^3q/a^2=rc\), to obtain (1). The catch expansion \(Y_\varepsilon=\eta u_0q+\varepsilon^2\eta(u_0\overline z+\overline{vw})+O(\varepsilon^3)\) yields (2) because \(\eta u_0=h-m\). Every term in (1) is positive since \(A_j>c>rc\).

**4. Catch sign and sharp single-mode threshold.** Write the bracket in (2) as \(K-H/A_j\), with \(K=(bh^2/a-m)/c\) and \(H=(h-m)r>0\). If \(K\le0\), all nonzero spectral terms are negative. If \(K>0\), then at \(D\downarrow0\) the bracket tends to \(-m(1-r)/c<0\) in every mode, and at sufficiently large \(D\) it is strictly positive in every mode (since \(A_j\ge c+D\lambda_1\)). Dominated convergence applies by \(\sum|v_j|^2<\infty\). For a single mode, \(K-H/(c+D\lambda_j)\) increases strictly through zero; solving gives (3). For the example, \(h=2,q=c=1,r=1/2\), \(\lambda_1=1\), and \(\overline{\cos^2x}=1/2\). Equations (1)–(3) simplify to the boxed expansions in the Finding and \(D_1^*=1/2\).

## Verification

The standalone `check.py` verifies (i) the exact rational example's symbolic quadratic coefficients and threshold, (ii) the general spectral algebraic identities, and (iii) the response of the full stationary nonlinear Neumann equation by independent cosine pseudospectral collocation and centered finite differences at \(D=1/4\) and \(D=1\). The numerical part is a consistency check; the proof of the infinite-dimensional result is the analytic argument above. The checked comparison concerns fixed diffusivity and small effort amplitude. Remainders are local \(O(\varepsilon^3)\) and are not asserted uniformly in \(D\).

## Relationship to prior work

Aye and Bock (2026) formulate this Beverton–Holt reaction–diffusion harvesting equation, analyze homogeneous equilibrium and linear spatial stability, and develop finite-horizon adjoint optimization. They do not state the fixed-mean spatial-effort stationary spectral yield multiplier (2), its exact one-mode dispersal cutoff (3), or the global inverse-biomass stock inequality (4). Their homogeneous equilibrium and model structure are acknowledged as prior work, not claimed as new.

Hilborn, Fitchett, Hampton and Ovando (2024) already show by spatial fishery simulations that reallocating a fixed total effort to create a protected region can raise biomass while lowering catch, and that catch gains in heavily exploited fisheries depend on movement. Therefore **the qualitative possibility of a diffusion-dependent catch tradeoff is prior art**. Their discrete age-structured, fleet-allocation simulation does not give (1)–(4) for the constant-coefficient Neumann Beverton–Holt diffusion equation, nor the sharp single-eigenmode threshold. Ding and Lenhart (2009) and Kurata and Shi (2008) study related spatial optimal harvesting, but under different growth/boundary or control formulations. A classical perturbative derivation in unindexed sources remains a priority risk; the present novelty claim is confined to the explicit formulas and stock inequality in this defined model.

## Limitations

This is a deterministic, stationary, one-dimensional result with homogeneous intrinsic vital rates, linear catch proportional to effort times biomass, ideal reflecting boundaries, and small effort redistributions for the spectral catch response. It does not identify a globally optimal fishing policy, a finite-amplitude catch threshold, ecological welfare, empirical stock changes, or the sign at the critical diffusion coefficient beyond second order. The stock bound applies only to a strictly positive stationary solution, not necessarily to arbitrary time-dependent states. Historical mathematical priority outside the inspected source set is not independently established.

## References

1. Tin Nwe Aye and Wolfgang Bock, *Spatially Explicit Optimal Harvesting and Adjoint-Based Diagnostics for Nonlinear Biomass Dynamics*, arXiv:2610.08374v1, first public release 2026-10-06. https://arxiv.org/abs/2610.08374
2. Ray Hilborn, Mark Fitchett, John Hampton and Daniel Ovando, *When does spillover from marine protected areas indicate benefits to fish abundance and catch?*, Theoretical Ecology, first released 2024-11-20. https://doi.org/10.1007/s12080-024-00596-2
3. Wandi Ding and Suzanne Lenhart, *Optimal Harvesting of a Spatially Explicit Fishery Model*, Natural Resource Modeling 22 (2009). https://doi.org/10.1111/j.1939-7445.2008.00033.x
4. K. Kurata and J. Shi, *Optimal Spatial Harvesting Strategy and Symmetry-Breaking*, Applied Mathematics & Optimization 58 (2008). https://doi.org/10.1007/s00245-007-9032-7
5. Michael G. Neubert, *Marine Reserves and Optimal Harvesting*, Ecology Letters 6 (2003). https://doi.org/10.1046/j.1461-0248.2003.00493.x
