# A unique throughput-optimal reset rate and a sharp membrane-contact crossover on a Brownian ring

## Finding
Consider a Brownian particle diffusing on a ring of circumference \(L>0\), cut at a symmetric semipermeable interface of fixed permeability \(\kappa>0\). Its position is reset independently at Poisson rate \(r>0\) to one fixed interior site \(x_0\ne L/2\). Write \(D>0\) for the diffusivity, \(\ell=\min\{x_0,L-x_0\}\in(0,L/2)\) for the distance from the reset site to the nearest side of the membrane, and \(J(r)\) for the stationary signed diffusive current across the membrane.

**Exact global optimum.** The function \(r\mapsto|J(r)|\) has exactly one maximizer \(r_*\in(0,\infty)\). More precisely, define
\[
 u=1-\frac{2\ell}{L}\in(0,1),\qquad k=\frac{\kappa L}{D}>0,\qquad z=\frac L2\sqrt{\frac rD}>0.
\]
Then the exact current magnitude is
\[
 |J(r)|=\frac{2Dk}{L^2}\,\frac{z^2\sinh(uz)}{z\cosh z+k\sinh z}.
\]
The dimensionless flux profile is **strictly logarithmically concave** on the entire positive half-line. Consequently its unique maximizer \(z_*(u,k)>0\) is the unique solution of
\[
\frac1z+u\coth(uz)-\coth z+
\frac{\operatorname{csch}^2z+k/z^2}{\coth z+k/z}=0,
\qquad r_* =\frac{4Dz_*^2}{L^2}.
\]
For each fixed positive permeability, \(r_*\) increases strictly as the reset point approaches the membrane; for each fixed off-center reset site, \(r_*\) increases strictly with permeability.

**Sharp source-near-membrane scaling.** Allow \(\ell\downarrow0\) and let the positive permeability depend on \(\ell\) in any way such that the dimensionless contact conductance \(\eta_\ell=2\kappa(\ell)\ell/D\) converges to \(\eta\in[0,\infty]\). Then the optimum has the universal limit
\[
\boxed{\lim_{\ell\downarrow0}\frac{r_*(\ell)\ell^2}{D}=G(\eta)^2},
\qquad
G(\eta)=\frac{1-\eta+\sqrt{\eta^2+6\eta+1}}2
\quad(0\le\eta<\infty),\qquad G(\infty)=2.
\]
The function \(G\) is strictly increasing from \(1\) to \(2\). In particular, fixed finite permeability yields \(r_*\ell^2/D\to1\), whereas any family with \(\kappa\ell/D\to\infty\) yields \(r_*\ell^2/D\to4\). Thus the singular near-interface optimum changes by an exact factor four between reflecting-dominated and transparent-dominated contacts. This scaling concerns the **optimal stationary membrane current**, not interfacial entropy production or first-passage search times.

## Assumptions and scope
Use \(x\in(0,L)\) to denote the opened ring, with \(x=0^+\) and \(x=L^-\) the two sides of its single interface. Brownian motion has generator \(D\partial_{xx}\); every reset sets the position to \(x_0\in(0,L)\), independently of the current position and without being screened by the membrane. The unique normalized stationary density solves
\[
 Dp''-rp=-r\delta_{x_0}\quad\text{distributionally in }(0,L),
\qquad -Dp'(0^+)=-Dp'(L^-)=J=\kappa[p(L^-)-p(0^+)].
\]
The effective permeability \(\kappa\) is defined by this exact boundary convention. If a different convention uses half an intrinsic permeability in the jump law, that half is \(\kappa\) here. The source is not at the membrane and is not the midpoint; when \(x_0=L/2\), the current is identically zero and uniqueness of an optimum fails. All statements optimize \(r\) with \(D,L,\kappa,x_0\) otherwise fixed, except that \(\kappa\) may vary in the explicitly declared source-near-membrane limit. The sign of the current depends on which half contains the source; only its magnitude is optimized.

## Proof
**1. Reconstruct the stationary current, including normalization and interface signs.** Put \(a=\sqrt{r/D}=2z/L\). The normalized reflecting-boundary Green density corresponding to a point reset at \(x_0\) is
\[
p_N(x)=\frac{a}{\sinh(aL)}
\cosh(a\min\{x,x_0\})\cosh(a[L-\max\{x,x_0\}]).
\]
It integrates to one, satisfies the distributional stationary equation, and has vanishing endpoint derivatives. Its endpoint difference is
\[
p_N(0)-p_N(L)=
\frac{a\sinh[a(L/2-x_0)]}{\cosh(aL/2)}.
\]
For a prescribed signed current \(J\), the unique mass-zero homogeneous correction with \(-Dp'(0)=-Dp'(L)=J\) is
\[
h_J(x)=-\frac{J\sinh[a(x-L/2)]}{Da\cosh(aL/2)}.
\]
Its contribution to \(p(L)-p(0)\) equals \(-2J\tanh z/(Da)\). Imposing the membrane law gives
\[
 J=\frac{\kappa[p_N(L)-p_N(0)]}{1+\frac{2\kappa}{Da}\tanh z}.
\]
The denominator is strictly positive. The maximum principle for this irreducible reset-diffusion problem, or direct positivity of its transition resolvent, gives the unique normalized positive stationary density. Taking magnitudes, using \(|L/2-x_0|=L/2-\ell\), and substituting the dimensionless variables yields the displayed exact current formula. This Green representation and the qualitative possibility of nonmonotone interfacial observables are established forward ingredients; the optimization conclusions below are separate.

**2. Strict global logarithmic concavity.** Ignoring the positive constant \(2Dk/L^2\), factor the flux profile exactly as
\[
F_{u,k}(z)=
\underbrace{\frac{z\sinh(uz)}{\sinh z}}_{A_u(z)}
\underbrace{\frac1{\coth z+k/z}}_{B_k(z)}.
\]
For \(0<u<1\),
\[
\frac{d^2}{dz^2}\log A_u(z)
=-\frac1{z^2}-u^2\operatorname{csch}^2(uz)+\operatorname{csch}^2z<0.
\]
Indeed \(\sinh(uz)<u\sinh z\) for positive \(z\) (strict convexity of \(\sinh\) and \(0<u<1\)); consequently \(u\operatorname{csch}(uz)>\operatorname{csch}z\). The two functions \(\coth z\) and \(k/z\) are positive and log-convex on \((0,\infty)\):
\[
\frac{d^2}{dz^2}\log\coth z=\operatorname{sech}^2z+\operatorname{csch}^2z>0,
\qquad\frac{d^2}{dz^2}\log(k/z)=\frac1{z^2}>0.
\]
A sum of positive log-convex functions is log-convex (apply Hölder's inequality to their log-convex interpolations). Therefore \(\log B_k=-\log(\coth z+k/z)\) is concave, and \(\log F_{u,k}\) is strictly concave. Near zero, \(F_{u,k}(z)\sim uz^2/(1+k)\to0\); at infinity, \(F_{u,k}(z)\sim z e^{-(1-u)z}\to0\). The strict concavity and both zero endpoints imply that one and only one interior critical point exists, and it is the unique global maximum. Differentiation gives precisely the stated scalar root equation.

**3. Strict shifts of the clock optimum.** Let \(H(z,u,k)=\partial_z\log F_{u,k}(z)\). Step 2 gives \(H_z<0\). Direct differentiation at fixed \(z,k\) gives
\[
H_u=\coth(uz)-uz\operatorname{csch}^2(uz)
=\frac{\sinh(uz)\cosh(uz)-uz}{\sinh^2(uz)}>0.
\]
Similarly, at fixed \(z,u\), differentiation using the denominator \(\coth z+k/z\) gives
\[
H_k=\frac{\coth z-z\operatorname{csch}^2z}{(z\coth z+k)^2}>0,
\]
where positivity follows from \(\sinh z\cosh z>z\). Applying implicit differentiation to the unique root \(H(z_*,u,k)=0\) shows \(\partial_u z_*>0\) and \(\partial_k z_*>0\). Since \(u=1-2\ell/L\), proximity to either side of the membrane strictly increases the maximizing reset rate; increasing permeability does likewise. Neither inference requires numerical mode counting.

**4. The universal singular contact layer.** Put \(\delta=2\ell/L=1-u\downarrow0\), \(y=\delta z\), and \(\eta_\ell=\delta k=2\kappa\ell/D\). From the exact derivative formula of step 2, for every fixed \(0<y<\infty\), as \(\delta\downarrow0\) one has uniformly when \(\eta_\ell\) approaches any finite nonnegative \(\eta\),
\[
\frac1\delta H\!\left(\frac y\delta,1-\delta,\frac{\eta_\ell}{\delta}\right)
\longrightarrow\frac2y-1-\frac1{y+\eta}.
\]
If \(\eta_\ell\to\infty\), the last summand vanishes. To see the limit directly, rewrite
\[
H(z,u,k)=\frac2z+u\coth(uz)-\coth z
-\frac{\coth z-z\operatorname{csch}^2z}{z\coth z+k}.
\]
With \(z=y/\delta\), both hyperbolic cotangents approach one exponentially, while \(u=1-\delta\); the last fraction divided by \(\delta\) approaches \(1/(y+\eta)\), or zero when \(\eta=\infty\). All these convergences are uniform for \(y\) in a fixed compact subset of \((0,\infty)\).

The limiting function \(h_\eta(y)=2/y-1-1/(y+\eta)\), with its obvious \(\eta=\infty\) version, decreases strictly from positive infinity to \(-1\), since \(h_\eta'(y)=-2/y^2+1/(y+\eta)^2<0\). It has precisely one positive root, obtained from \(y^2+(\eta-1)y-2\eta=0\) when \(\eta<\infty\), namely \(G(\eta)\), and root \(2\) at \(\eta=\infty\). For any two fixed points bracketing that root, uniform derivative convergence fixes opposite signs at the corresponding rescaled positions for sufficiently small \(\delta\). Strict negativity of \(H_z\) then traps the unique root between them. Thus \(\delta z_*\to G(\eta)\), and because \(r_*\ell^2/D=(\delta z_*)^2\), the boxed limit follows.

Finally, for finite \(\eta\), implicit differentiation of \(h_\eta(G(\eta))=0\) yields \(G'(\eta)>0\), since \(\partial_\eta h_\eta=1/(y+\eta)^2>0\) and \(\partial_yh_\eta<0\). The continuous endpoint values are \(G(0)=1\), \(G(\infty)=2\); their squared ratio is four. This proves all asserted sharp contact limits.

## Verification
Run `python verify_flux.py` with Python 3 and only its standard library. The checker independently evaluates the current from the Neumann endpoint formula and from the reduced flux, solves the strictly monotone derivative equation by bisection, verifies strict local optimality and parameter ordering on deterministic grids, and checks the three contact-layer regimes. It passed **313 deterministic assertions**. This finite testing is diagnostic only; uniqueness, strict inequalities, and arbitrary-family limits are proved in the preceding analytic argument. The code avoids any dependence on other research files.

## Relationship to prior work
P. C. Bressloff (2024) derives the stationary reset diffusion equation, permeable-interface boundary law and interfacial entropy production for a ring. The exact forward membrane current follows from those formulas; it is not claimed new. Bressloff also reports nonmonotonic interfacial entropy in resetting rate and permeability, and that qualitative fact is prior work. Published analyses titled *Unique optimal membrane permeability and sharp universal bounds for resetting diffusion on a ring* (2026) and *A universal unique membrane-permeability optimizer for reset diffusion on a circle* (2026) use the same stationary object but optimize **permeability at fixed resetting rate** for **interfacial entropy**, not resetting rate at fixed permeability for **absolute transmitted current**. Another published result, *Boundary-current tomography and its reflection-blind subspace in a resetting diffusion ring* (2026), gives the exact current-vs-reset-rate transform and its inverse equivalence classes, not the strict log-concavity, unique clock optimum, monotone control law or singular contact-crossover profile. Thus the forward current itself is explicitly credited to prior work. The present mathematical assertion concerns a distinct nontrivial optimization and singular limit, and does not follow as a stated corollary of those prior classifications.

Bressloff (2022/2023) also studies absorption times under resetting screened by a permeable interface. Those first-passage objectives and geometries do not determine the stationary ring-current optimum. The additional all-parameter log-concavity and singular matching could potentially be derived from known forward equations by specialists; absence from the checked works is not a proof of publication priority.

## Limitations
The strict optimum holds for a single point reset away from the midpoint, one symmetric membrane, constant diffusivity, and a constant permeability independent of the varied reset rate. For a reset at the midpoint, the stationary current vanishes at all rates. No uniqueness claim is made for arbitrary random reset distributions, multiple membranes, position-dependent diffusion, non-Poisson resets, or clocks whose permeability changes with the reset rate. The source-near-interface theorem allows permeability scaling only through its stated positive family and convergence of the indicated dimensionless product. The result optimizes transmitted stationary probability current, not entropy production, physical work, or first-passage statistics. The inverse-square law concerns an optimal parameter as \(\ell\downarrow0\), not uniform interchange of finite-rate and endpoint-source limits. There has been no independent scientific audit; overlapping unindexed work remains possible.

## References
1. P. C. Bressloff, *Entropy production for diffusion processes across a semipermeable interface*, arXiv:2402.16403v1 (first public 2024-02-26), *Physical Review Research* **6**, 023283 (2024), DOI:10.1103/PhysRevResearch.6.023283. Particularly the full stationary resetting-on-a-circle section and membrane-current equations. https://arxiv.org/abs/2402.16403
2. P. C. Bressloff, *Diffusion with stochastic resetting screened by a semipermeable interface*, arXiv:2211.12468v1 (2022-11-22), *Journal of Physics A* **56**, 105001 (2023). https://arxiv.org/abs/2211.12468
3. *Unique optimal membrane permeability and sharp universal bounds for resetting diffusion on a ring* (2026), public mathematical record: https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-unique-optimal-membrane-permeability-and-sharp-universal-bounds--3bb98581842f
4. *A universal unique membrane-permeability optimizer for reset diffusion on a circle* (2026), public mathematical record: https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-a-universal-unique-membrane-permeability-optimizer-for-reset-dif--9bd1a590e00a
5. *Boundary-current tomography and its reflection-blind subspace in a resetting diffusion ring* (2026), public mathematical record: https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-boundary-current-tomography-and-its-reflection-blind-subspace-in--6de9da8f8562
