# A logarithmic neutral-flip clock and a fear-dependent fast-decay separatrix

## Finding

Consider the discrete fear-dependent predator–prey map of Du, Han and Lei [1], with the prey reproduction parameter fixed at the neutral flip value \(r=2\) and predator intrinsic growth strictly below mortality, \(\alpha<d\). The boundary equilibrium \((K,0)\) has one neutral multiplier \(-1\) and one contracting multiplier \(q=e^{\alpha-d}\in(0,1)\). There is a neighborhood \(U\) of \((K,0)\) in the biologically nonnegative half-plane with the following properties.

Every trajectory starting at \((u_0,v_0)\in U\), \(u_0>0\) and \(v_0\geq0\), remains positive in prey, nonnegative in predator, and converges to \((K,0)\). Exactly one local \(C^2\) curve \(u/K-1=h(v)\), through \((K,0)\), separates trajectories having exponentially fast prey recovery from those having critical algebraic recovery. The curve is uniquely characterized locally by exponential convergence, is tangent to the contracting eigendirection, and has the expansion

\[
 h(v)=-\frac{p}{1+q}v
 +\frac{\tfrac12p^2-\frac{p}{1+q}\bigl[2k+p(1+\theta)+q\eta\bigr]}{1+q^2}v^2
 +O(v^3),
 \quad p=\frac{\beta}{K+\gamma},\quad
 \theta=\frac K{K+\gamma},\quad
 \eta=\frac a{bK+c}.
\]

For every initial condition in \(U\) outside this curve there is a finite, initial-condition-dependent real constant \(C\) such that

\[
 \boxed{\left(\frac{u_{2n}}K-1\right)^{-2}
 =\frac83 n+\frac85\log n+C+o(1)}\qquad(n\longrightarrow\infty).
\]

For these trajectories, \(u_{2n}/K-1\) eventually has a constant nonzero sign \(\sigma\in\{-1,1\}\), with \(\sqrt n\,(u_{2n}/K-1)\to\sigma\sqrt{3/8}\). The predator component satisfies \(0\le v_n\le q^n v_0\) throughout. On the exceptional curve, both deviations converge exponentially; away from it, the algebraic clock is universal, although the curve's quadratic coefficient depends genuinely on fear strength \(k\).

## Assumptions and scope

The exact map is

\[
\begin{aligned}
 u_{n+1}&=u_n\exp\!\left[\frac{2}{1+kv_n}\left(1-\frac{u_n}{K}\right)-\frac{\beta v_n}{u_n+\gamma}\right],\\
 v_{n+1}&=v_n\exp\!\left(\alpha-d-\frac{a v_n}{bu_n+c}\right).
\end{aligned}
\]

Here \(K,\beta,\gamma,a,b,c>0\), \(k\geq0\), \(\alpha,d>0\), and \(\alpha<d\). Statements hold for each fixed such parameter choice, with a sufficiently small neighborhood depending on that choice. The relative neighborhood is taken in \(\{u>0,v\geq0\}\); it is not an assertion about all positive initial data. In particular, the case \(\alpha=d\), where the transverse multiplier is one, is excluded.

Write \(z=u/K-1\). On the invariant boundary \(v=0\), the exact scalar map is \(f(z)=(1+z)e^{-2z}-1\). Its fixed point has derivative \(f'(0)=-1\), and \(f\) is a local real-analytic diffeomorphism. The predator update is exactly bounded by \(v_{n+1}\le q v_n\) for nonnegative prey and predator.

## Proof

**1. A genuinely attracting but neutral boundary return.** Direct Taylor expansion of the exact scalar restriction gives

\[
 G(z):=f(f(z))=z-\frac43z^3+\frac8{15}z^5+\frac49z^6+O(z^7).
\]

The quartic term vanishes. For sufficiently small \(|z|\), \(G\) preserves sign and
\( |G(z)|\le |z|-c_0|z|^3\) for some \(c_0>0\). Hence scalar even iterates of every small nonzero starting value keep their sign and converge to zero, while odd iterates converge with the opposite sign.

**2. Positivity, small-data attraction and exponentially decaying forcing.** The second component satisfies \(0\le v_n\le q^n v_0\). On a small compact rectangle around the boundary equilibrium, the difference between the actual first component and \(f(z_n)\) is bounded by \(C_0v_n\). Consequently

\[
 |z_{2m+2}|\le |z_{2m}|-c_0|z_{2m}|^3+C_1q^{2m}v_0.
\]

Shrink the initial rectangle so that the total geometric forcing is less than its trapping margin. This inequality proves the even states remain inside the rectangle; the one-step bound also traps the odd states. Summing the inequality gives \(\sum_{m\geq0}|z_{2m}|^3<\infty\), since the total forcing is summable. Therefore both parities converge to zero. No global basin property is used.

**3. Exponentially accurate scalar shadowing.** Restrict \(f\) to a small interval around zero such that its local inverse has Lipschitz constant \(L>1\) with \(Lq<1\). This is possible because the inverse derivative has modulus one at zero. With \(e_n=z_{n+1}-f(z_n)\), the first-component equation gives \(|e_n|\le C_2q^n v_0\). Starting from \(z_N\), iterate the local inverse of \(f\) backward \(N\) times. Each reconstructed segment remains in the inverse interval by the trapping bounds and the geometric estimate \(\sum_{j\ge0}L^{j+1}q^j<\infty\); the inverse reconstructions are Cauchy because successive differences are at most \(C_3L^{N+1}q^N v_0\).

Their limit is an initial value \(\zeta_0\) of a true scalar orbit \(\zeta_{n+1}=f(\zeta_n)\), uniquely determined by the requirement

\[
 |z_n-\zeta_n|\le C_4q^n v_0\quad\text{for all }n\ge0.
\]

Uniqueness follows by backward propagation of the discrepancy, because \(Lq<1\). A standard local strong-stable-manifold theorem (the stable multiplier \(q\) is strictly dominated by the tangential modulus one) supplies a unique smooth curve of exponentially converging initial conditions. Equivalently it is the local zero set of the scalar shadowing coordinate \(\zeta_0\): if \(\zeta_0=0\) then the shadowing bound gives exponential convergence of both components; if \(\zeta_0\neq0\) then the scalar orbit has algebraic rather than exponential decay, so the original orbit cannot converge exponentially. The invariant boundary \(v=0\) maps to \(\zeta_0=z_0\), hence the curve is a local graph \(z=h(v)\). Smoothness can also be recovered by differentiating the inverse reconstruction after choosing the interval with \(qL^j<1\) for the finite derivative orders required.

**4. Explicit separatrix curvature.** Set \(p=\beta/(K+\gamma)\), \(\theta=K/(K+\gamma)\), and \(\eta=a/(bK+c)\). Expanding to total degree two near the equilibrium gives

\[
\begin{aligned}
 z'&=-z-pv+\bigl[2k+p(1+\theta)\bigr]zv+\tfrac12p^2v^2+O((|z|+v)^3),\\
 v'&=qv-q\eta v^2+O((|z|+v)^3).
\end{aligned}
\]

Insert \(h(v)=h_1v+h_2v^2+O(v^3)\) into the invariance equation \(h(v')=z'|_{z=h(v)}\). Comparison of coefficients yields

\[
 (1+q)h_1=-p,\qquad
 (1+q^2)h_2=h_1[2k+p(1+\theta)+q\eta]+\tfrac12p^2.
\]

This is exactly the stated curvature. Its derivative with respect to the fear coefficient is
\(\partial_k h_2=-2p/[(1+q)(1+q^2)]<0\), with all other parameters fixed. Thus the dependence on fear is not a merely notational dependence.

**5. Sharp critical clock.** For a scalar orbit with \(\zeta_0\neq0\), set \(s_m=\zeta_{2m}\) and \(w_m=s_m^{-2}\). The Taylor expansion in Step 1 gives

\[
 w_{m+1}=w_m+\frac83+\frac{64}{15w_m}+O(w_m^{-3/2}).
\]

The positive leading increment implies \(w_m\sim (8/3)m\); substituting back yields \(w_m=(8/3)m+O(\log m)\). Thus

\[
 \sum_{m\ge1}\left(\frac1{w_m}-\frac3{8m}\right)
\]

converges absolutely, and the remainder \(O(w_m^{-3/2})\) is summable. Consequently

\[
 w_m-\frac83m-\frac85\log m\longrightarrow C_\zeta\in\mathbb R.
\]

Finally, the exponentially accurate shadowing estimate and \(|s_m|\asymp m^{-1/2}\) imply

\[
 \left|z_{2m}^{-2}-s_m^{-2}\right|
 =O(q^{2m}m^{3/2})\longrightarrow0.
\]

This transfers the exact constant-order asymptotic, its sign, and the universal leading amplitude to the original map. Exponential shadowing when \(\zeta_0=0\) proves the complementary fast-decay branch. These cases exhaust the small-data neighborhood.

## Verification

`verify.py` is standalone Python/SymPy code. It checks by exact symbolic series the cubic, quintic and sextic coefficients of the two-step scalar return; the \(8/5\) reciprocal-clock coefficient; and both invariant-graph coefficient equations. Finite numerical trajectories with strictly positive predator component on either side of the fast-decay curve exhibit converging renormalized clocks. A direct quadratic graph-invariance residual scales cubically with the predator coordinate. The checker prints `VERIFY_OK` on successful completion. Its finite trajectories are diagnostics, not an independent proof of the infinite-time conclusions.

## Relationship to prior work

Du, Han and Lei [1] introduced the exact fear-modulated system and recorded the boundary fixed point's multipliers, including the nonhyperbolic classification at \(r=2\). Their analysis addresses equilibrium and interior flip/Neimark–Sacker bifurcations, boundedness, controls and numerical diagrams; it does not provide the logarithmically renormalized critical clock or the explicit strong-stable boundary curvature in the predator-extinction regime. The closely related fear-map study [2] uses a different additive discretization rather than this exponential map and does not imply the stated exact return.

The competitive planar Ricker study [3] proves global convergence and describes invariant manifolds for a distinct exponential competition map. Its identification of the classical scalar \(r=2\) convergence boundary is consistent with Step 1, but neither establishes the \(8/5\) logarithmic correction for the present fear model nor the explicit fear-dependent quadratic strong-stable graph. Existing research on simultaneous prey flip and predator neutrality addresses \(\alpha=d\), whereas the present theorem assumes \(\alpha<d\); those results therefore do not yield the exponentially forced shadowing claim. Standard normal-form and stable-manifold methods are background machinery rather than claimed as new discoveries.

## Limitations

The conclusion is **local** for each fixed parameter tuple; the neighborhood is not uniform as \(\alpha\uparrow d\). No global basin classification, persistence, ecological forecasting or interior positive equilibrium analysis is asserted. The fast-decay curve is a relative arc in the nonnegative predator half-plane, and no statement is made about negative predator densities. The logarithmic clock applies only to nonexceptional trajectories, while the exceptional curve exhibits exponential decay. Existing general theories of parabolic iterates and stable foliations may contain equivalent implications not explicitly indexed by the searches; publication priority would need wider expert comparison. The symbolic computation does not substitute for the analytic shadowing and summability arguments.

## References

[1] X. Du, X. Han and C. Lei, "Dynamics of a nonlinear discrete predator-prey system with fear effect," *AIMS Mathematics* 8 (2023), 23953–23973, first published 2023-08-07. https://doi.org/10.3934/math.20231221. Primary text: https://aimspress.com/aimspress-data/math/2023/10/PDF/math-08-10-1221.pdf.

[2] C. Lei, X. Han and W. Wang, "Bifurcation analysis and chaos control of a discrete-time prey-predator model with fear factor," *Mathematical Biosciences and Engineering* 19 (2022), 6659–6679. https://doi.org/10.3934/mbe.2022313.

[3] S. Baigent, Z. Hou, S. Elaydi, E. C. Balreira and R. Luís, "A global picture for the planar Ricker map: convergence to fixed points and identification of the stable/unstable manifolds," *Journal of Difference Equations and Applications* 29 (2023), 575–591. https://doi.org/10.1080/10236198.2023.2222855.
