# Global threshold dynamics and universal critical extinction in a fear–refuge predator–prey flow

## Finding
For the strictly positive parameters and initial data in the next section, put \(P=\beta(1-\delta)\), \(Q=cP\), and let \(U>0\) be the unique solution of
\[
 aU(1+\alpha U)=r.
\]
The *sharp global invasion trichotomy* is as follows.

1. If \(QU>m\), there is exactly one strictly positive equilibrium \((u_*,v_*)\); every strictly positive solution converges to it exponentially (with rate and prefactor allowed to depend on parameters and the initial state).
2. If \(QU<m\), every strictly positive solution converges to \((U,0)\), and \(\lim_{t\to\infty}t^{-1}\log v(t)=QU-m<0\).
3. If \(QU=m\), every strictly positive solution converges to \((U,0)\) with a universal, initial-condition-independent critical amplitude. With
\[
 A=U\left(a+\frac{r\alpha}{(1+\alpha U)^2}\right),\quad
 B=U\left(P+\frac{rk}{(1+\alpha U)^2}\right),\quad
 C=\eta+\frac{QB}{A},
\]
one has
\[
 \lim_{t\to\infty}t v(t)=\frac1C,\qquad
 \lim_{t\to\infty}t\,[U-u(t)]=\frac{B}{AC}.
\]
The assertions hold without the additional cross-interaction smallness condition sometimes used to establish boundedness. Moreover, the flow has no nonconstant periodic orbit contained in the strictly positive quadrant for *any* permitted parameters.

## Assumptions and scope
Consider the exact autonomous planar model
\[
 \dot u=u\left(\frac{r}{1+kv+\alpha u}-au-Pv\right),\qquad
 \dot v=v(Qu-m-\eta v),
\]
where \(r,k,\alpha,a,\beta,m,\eta>0\), \(0\le\delta<1\), \(0<c\le1\), \(P=\beta(1-\delta)>0\), and \(Q=cP>0\). Take arbitrary \(u(0)>0\), \(v(0)>0\). These are the variables, parameters, and functional form of Ramraj--Poornima (2026), not a claim about general prey--predator models, time delays, or stochastic dynamics. The critical case is the exact equality \(QU=m\).

The source's first verifiable public publication is August 10, 2026 (DOI 10.3389/frai.2026.1868693). The paper's receipt and acceptance dates are not substituted for a public release date.

## Proof
**Positive existence and boundedness, with no smallness restriction.** Both equations have the coordinate as a factor; positivity follows by integrating the continuous per-capita rate. Since \(\dot u\le u(r-au)\), for all \(t\ge0\), \(0<u(t)\le M_u=\max\{u(0),r/a\}\). Then \(\dot v\le v(QM_u-m-\eta v)\), so \(0<v(t)\le M_v=\max\{v(0),(QM_u-m)_+/\eta\}\). Smoothness on this compact positive-quadrant box implies global existence. The scalar prey-only field \(u[r/(1+\alpha u)-au]\) has the unique positive fixed point \(U\) and is strictly restoring toward it. Comparison gives \(\limsup_{t\to\infty}u(t)\le U\).

**Equilibria.** Write \(f(u,v)=r/(1+\alpha u+kv)-au-Pv\), \(g(u,v)=Qu-m-\eta v\). The interior predator nullcline is \(v=(Qu-m)/\eta>0\), increasing for \(u>m/Q\). Along it, \(f\) is strictly decreasing because both \(f_u<0\) and \(f_v<0\). If \(QU>m\), its value at \((m/Q,0)\) is positive and its value at \((U,(QU-m)/\eta)\) is negative. Hence it crosses zero once and only once. If \(QU\le m\), for every \(u\ge m/Q\ge U\) it is negative, so no positive equilibrium exists. At the interior equilibrium the Jacobian has entries \(u_*f_u<0\), \(u_*f_v<0\), \(v_*Q>0\), \(-\eta v_*<0\); therefore its trace is strictly negative and determinant strictly positive. It is a hyperbolic sink.

**No positive periodic orbit.** On the simply connected strictly positive quadrant, the Dulac multiplier \(D(u,v)=1/(uv)\) gives the exact identity
\[
 \partial_u(D\dot u)+\partial_v(D\dot v)
 =-\frac{a}{v}-\frac{r\alpha}{v(1+\alpha u+kv)^2}-\frac{\eta}{u}<0.
\]
The Bendixson--Dulac theorem rules out positive cycles and interior homoclinic cycles.

**Global convergence above threshold.** The only boundary equilibria are \((0,0)\) and \((U,0)\). At \((0,0)\), the stable manifold is contained in the invariant predator axis \(u=0\). At \((U,0)\) when \(QU>m\), the stable manifold is contained in the invariant prey axis \(v=0\); this equilibrium is a hyperbolic saddle. Consequently no strictly positive trajectory can approach either boundary equilibrium. A bounded planar omega-limit set that is not a single equilibrium would, by the Poincaré--Bendixson alternative, contain a periodic orbit or a closed graph of connecting orbits. The former is excluded by the Dulac identity. The latter is impossible: any connection entering \((0,0)\) must approach on \(u=0\), and any connection entering \((U,0)\) must approach on \(v=0\), so the sole boundary connection \((0,0)\to(U,0)\) cannot close a graph; the interior equilibrium is a sink and has no outgoing connection. Thus the interior equilibrium attracts every positive orbit. Its hyperbolicity yields eventual exponential convergence.

**Global convergence at and below threshold.** For \(QU<m\), comparison and the limsup inequality yield \(Qu(t)-m\le(QU-m)/2<0\) eventually. Hence \(v(t)\) vanishes exponentially. For \(QU=m\), the same limsup inequality gives \(\dot v\le v(Q\epsilon-\eta v)\) eventually for any \(\epsilon>0\); scalar logistic comparison gives \(\limsup v\le Q\epsilon/\eta\), hence \(v\to0\). In either case, the prey equation is squeezed between the prey-only equation and the equation with \(v\) replaced by arbitrarily small positive constants. Their positive globally attracting scalar equilibria converge to \(U\), so \(u\to U\). If \(QU<m\), integrating \(d\log v/dt=Qu-m-\eta v\) and taking Cesàro limits gives the asserted logarithmic exponential-decay rate.

**The sharp critical constant.** At \(QU=m\), set \(x=u-U\) and \(y=v\). A Taylor expansion of the *exact* vector field at \((U,0)\), with explicit positive coefficients \(A,B\) above, gives
\[
 x'=-Ax-By+O(x^2+|xy|+y^2),\qquad y'=y(Qx-\eta y).
\]
Global convergence already proved implies \(x,y\to0\) with \(y>0\), so \(y'/y=Qx-\eta y\to0\). The first equation is a uniformly exponentially stable scalar linear equation forced by \(-By\) plus quadratic terms. To justify the precise ratio, take any \(\epsilon>0\) small and a time beyond which \(|y'/y|<\epsilon\), \(|x|+y\) is small. The variation-of-constants estimate for \(x\) first implies \(|x(t)|\le C_1y(t)+C_2e^{-A(t-T)/2}\); since \(y'/y\to0\), \(e^{-A(t-T)/2}/y(t)\to0\), so \(x=O(y)\). Hence the Taylor remainder is \(o(y)\). Dividing the variation-of-constants integral by \(y(t)\), using \(y(t-h)/y(t)\to1\) for each fixed \(h\) and the integrable bound \(e^{-(A-\epsilon)h}\), dominated convergence gives \(x(t)/y(t)\to-B/A\). It follows that
\[
 y'=-\left(\eta+QB/A+o(1)\right)y^2=-\left(C+o(1)\right)y^2.
\]
Therefore \((1/y)'\to C\), whence \(t y(t)\to1/C\) and \(t[U-u(t)]\to B/(AC)\), as claimed.

## Verification
The exact Dulac divergence, critical Jacobian coefficients and representative rational parameter evaluation can be checked by running `python3 verify.py` with SymPy and SciPy. The executable independently reconstructs three parameter regimes from the stated equations and confirms the expected critical asymptotic numerically, including \((r,a,\alpha,k,\beta,\delta,c,m,\eta)=(2,1,1,1,2,1/2,1/2,1/2,1)\), for which \(U=1\), \(A=B=C=3/2\), and \(tv\to2/3\), \(t(1-u)\to2/3\). Finite numerical trajectories are illustrative, not a proof of convergence for all parameters or initial conditions. The full proof is analytical above.

## Relationship to prior work
Ramraj and Poornima (2026) introduced this precise fear--refuge--crowding--interference system, gave positivity, conditional boundedness, equilibrium conditions and local stability, and explicitly identified rigorous global stability as future work. This result concerns the same equation but proves a global phase portrait without their auxiliary boundedness restriction and quantifies the *critical* neutral-invasion extinction rate. The Bendixson--Dulac and Poincaré--Bendixson tools are classical and are not claimed new. Earlier general global-stability methods of Kuang (1990) and Hou--Baigent (2015) may cover parts of the attraction argument; no comparison inspected establishes the explicit threshold equality and two universal leading constants for this exact fear--refuge--crowding model. Related fear/refuge predator--prey studies use different growth and predator-response functions and are not identified here as proofs of the present equality-case asymptotic.

## Limitations
This is a deterministic, two-species autonomous theorem with strictly positive initial populations and strictly positive \(a,\eta,\alpha,k\). The critical amplitude depends on the specified functional response. No extension to gestation delays, stochastic processes, spatial PDEs, or a vanishing competition coefficient is asserted. The literature comparison does not guarantee absolute historical priority, particularly against general stability theorems whose full statements were not accessible. Independent validation has not been performed.

## References
1. G. Ramraj and T. Poornima, *Fear-driven predator–prey dynamics with prey refuge: analytical framework and physics-informed neural network approach*, Frontiers in Artificial Intelligence **9** (2026), 1868693, first published 2026-08-10. DOI: 10.3389/frai.2026.1868693. Full text: https://www.frontiersin.org/journals/artificial-intelligence/articles/10.3389/frai.2026.1868693/full.
2. Y. Kuang, *Global stability of Gause-type predator-prey systems*, Journal of Mathematical Biology **28** (1990), 463–474. DOI: 10.1007/BF00178329.
3. Z. Hou and S. Baigent, *Global stability and repulsion in autonomous Kolmogorov systems*, Communications on Pure and Applied Analysis **14** (2015), 1205–1238. DOI: 10.3934/cpaa.2015.14.1205.
4. Anuj Kumar Umrao et al., *Nonlinear dynamics in a fear-driven predator–prey system: bistability, bifurcations, hydra effect, and optimal harvesting*, Mathematical Methods in the Applied Sciences **48** (2025), 2194–2223, first published 2024-08-31. DOI: 10.1002/mma.10431.
