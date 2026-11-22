# Global parabolic convergence and a sharp normal-stability sign in a cubic Lorenz-like flow

## Finding

Consider the cubic Lorenz-like flow of Wang, Ke, Pan and Su [1]. On its natural parabolic-equilibrium surface, the previously studied zero-mixed-coupling case admits a strict positive-coupling extension. For **every** \(a>0\), \(\beta>0\), \(\gamma\ge0\) and **every** initial condition in \(\mathbb R^3\), the system
\[
\dot x=a(y-x),\qquad
\dot y=-(2a\beta+\gamma)yz+\gamma xz+\beta x^2y,\qquad
\dot z=-2az+y^2
\]
is forward complete and converges exponentially to a **single, initial-condition-dependent** point of the equilibrium parabola
\[
\mathcal P=\left\{(s,s,s^2/(2a)):s\in\mathbb R\right\}.
\]
The convergence admits an explicit estimate even when the initial height \(z_0\) is negative. Every invariant Borel probability measure is supported on \(\mathcal P\), and every compact invariant set for the flow consists entirely of equilibria. The boundary \(\gamma=0\) is sharp for **normal stability of every equilibrium**: for every \(\gamma<0\), sufficiently far-out points of the same parabola have an unstable transverse eigenvalue. This last statement does **not** assert a classification of all nonlinear trajectories when \(\gamma<0\).

## Assumptions and scope

The coefficients \(a,\beta\) are any strictly positive real numbers and \(\gamma\ge0\). Time is real and initial data \((x_0,y_0,z_0)\in\mathbb R^3\) are unrestricted. We use the source's parameter notation \(c=2a\), \(b_1=0\), \(b_4=\beta\), \(b_3=\gamma\), \(b_2=-2a\beta-\gamma\). This is precisely the parabolic-equilibrium condition \(cb_4+b_3+b_2=0\); it retains the original \(xz\) coupling whenever \(\gamma>0\).

Put \(u=y-x\), \(w=2az-x^2\), \(E=au^2+(\beta/2)w^2\), and \(Z_-=\max\{0,-z_0\}\). At all forward times,
\[
\boxed{ E(t)\le E(0)\exp\!\left[-2at+\frac{\gamma Z_-}{a}(1-e^{-2at})\right]
\le E(0)e^{\gamma Z_-/a}e^{-2at}. }
\]
There is a well-defined \(s=s(x_0,y_0,z_0)\) with
\[
\boxed{ |x(t)-s|\le \sqrt{E(0)/a}\,e^{\gamma Z_-/(2a)}e^{-at}. }
\]
Consequently \(y(t)\to s\) and \(z(t)\to s^2/(2a)\), both at least exponentially in time. The limiting-point selection \((x_0,y_0,z_0)\mapsto(s,s,s^2/(2a))\) is a continuous retraction onto \(\mathcal P\), constant along forward orbits.

## Proof

**Exact error equations.** Substitution into the polynomial vector field gives, with no approximation,
\[
\dot x=au,\quad
\dot u=-(a+\gamma z)u-\beta yw,\quad
\dot w=-2aw+2ayu.
\]
Differentiate \(E\); the mixed \(uyw\) terms cancel exactly:
\[
\boxed{\dot E=-2a(a+\gamma z)u^2-2a\beta w^2.}
\]
The scalar height equation has the exact variation-of-constants formula
\[
 z(t)=z_0e^{-2at}+\int_0^t e^{-2a(t-r)}y(r)^2\,dr
 \ge -Z_-e^{-2at}.
\]
As \(au^2\le E\) and \(\gamma\ge0\),
\[
\dot E\le \left(-2a+2\gamma Z_-e^{-2at}\right)E.
\]
Gronwall integration gives the displayed sharp-form energy estimate. If \(E(0)=0\), the initial point is on \(\mathcal P\) and is stationary, so all conclusions also hold.

**Global existence and phase selection.** On any finite positive time interval, the energy bound controls \(u,w\), and \(\dot x=au\) then controls \(x\). The identities \(y=x+u\) and \(z=(w+x^2)/(2a)\) control the original state; a maximal finite-time solution cannot blow up. Further,
\[
|\dot x(t)|=a|u(t)|\le \sqrt{aE(0)}\,e^{\gamma Z_-/(2a)}e^{-at},
\]
so \(x(t)\) is Cauchy as \(t\to\infty\), with limit \(s\) and the stated tail estimate. Both \(u,w\) decay as \(O(e^{-at})\), proving the componentwise convergence. On each compact initial-state set the estimates are uniform; the limit of the continuous maps \(x(t;\cdot)\) is continuous. Since \(\mathcal P\) consists of equilibria, the limiting projection fixes \(\mathcal P\), and invariance under advancing time follows from the semigroup property.

**Measure and recurrence rigidity.** Let \(\phi_t\) be this forward flow. For any invariant Borel probability \(\mu\), and any bounded continuous nonnegative function \(h\) that vanishes exactly on \(\mathcal P\), such as \(h(p)=\min\{1,\operatorname{dist}(p,\mathcal P)\}\), invariance and dominated convergence yield
\[
\int h\,d\mu=\int h(\phi_t(p))\,d\mu(p)\longrightarrow0.
\]
Thus \(\mu(\mathcal P)=1\); conversely every probability on the equilibrium parabola is invariant. For any compact set \(K\) with \(\phi_tK=K\) for every \(t\ge0\), let \(M=\max_K E\) and \(C=\max_K \gamma\max(0,-z)/a\). For any \(p\in K\) and \(t\ge0\), choose \(q\in K\) satisfying \(\phi_t(q)=p\). The energy estimate gives \(E(p)\le Me^{C-2at}\). Letting \(t\to\infty\) shows \(K\subset\mathcal P\). In particular no nonstationary periodic orbit, compact chaotic recurrent set or positive-entropy compact invariant set occurs.

**Sharpness of the universal normal-stability sign.** Extend the same balanced family to real \(\gamma\), retaining \(a,\beta>0\). At \(p_s=(s,s,s^2/(2a))\), the two-dimensional normal linearization in coordinates \((u,w)\) is
\[
N_s=\begin{pmatrix}
-a-\gamma s^2/(2a)&-\beta s\\
2as&-2a
\end{pmatrix},\qquad
\operatorname{tr}N_s=-3a-\frac{\gamma s^2}{2a},\quad
\det N_s=2a^2+(2a\beta+\gamma)s^2.
\]
If \(\gamma\ge0\), its trace is strictly negative and determinant strictly positive for all \(s\), so each point is normally attracting. For every \(\gamma<0\), any \(s\) with \(s^2>6a^2/(-\gamma)\) makes the trace positive; hence at least one transverse eigenvalue has positive real part. Therefore \(\gamma\ge0\) is **exactly** the parameter range for all equilibria of this natural family to have stable transverse spectra.

## Verification

The exact polynomial identity for \(\dot E\) and the transformed error equations were independently expanded with symbolic algebra. A standalone standard-library checker, `verify.py`, constructs the complete polynomial identities over rational coefficients (not merely sampled numerical points) and checks the displayed normal trace and determinant, including negative-coupling witnesses. It is embedded with this result and can be executed using `python verify.py`. The actual infinite-dimensional dynamical conclusions follow from the estimates above, not from finite numerical tests.

## Relationship to prior work

Wang, Ke, Pan and Su [1, Proposition 4.1] identify the parabolic equilibrium surface. Their Proposition 4.4(1) treats the transverse linear eigenvalues at general balanced coefficients; their global Lyapunov proof in Proposition 4.4(2) takes the special choice \(b_3=0\), \(c=2a\), \(b_2=-cb_4\), \(b_4>0\). The present result retains **every \(b_3>0\)** while preserving the equilibrium constraint, controls arbitrary negative initial height, and classifies all invariant probabilities and compact recurrent dynamics. The sign boundary is a direct consequence of the source's spectral trace formula after specializing to the balanced surface; it is included as the exact scope limit, not claimed as an independent spectral discovery.

Related published analyses of stabilization and parabolic confinement in other Lorenz-like flows [2,3] use different vector fields and do not imply the full-real-data convergence estimate for this cubic system. Searches by source identity, parameter equalities, transformed error dynamics, normal-spectrum aliases and recurrence consequences identified no stronger covering statement in the literature inspected. This is a best-knowledge originality assessment, not a guarantee of publication priority.

## Limitations

The theorem concerns the balanced surface \(c=2a\), \(b_1=0\), \(b_2=-2a\beta-\gamma\), rather than arbitrary six-parameter cubic flows. The negative-\(\gamma\) conclusion is **only** the existence of transversely unstable equilibria, not a proof of recurrent chaos or failure of attraction to the equilibrium set for every orbit. The source paper's indexed Proposition 4.1, Proposition 4.4 and proof, and accessible summaries were inspected; a complete independent full-text inspection beyond those material sections was limited by publisher access. Other unindexed equivalent derivations may exist. No independent mathematical audit has been performed.

## References

[1] Wang, H., Ke, G., Pan, J., and Su, Q. (2023). *Modeling, dynamical analysis and numerical simulation of a new 3D cubic Lorenz-like system*. Scientific Reports **13**, 6671. https://doi.org/10.1038/s41598-023-33826-4 (first public April 24, 2023).

[2] *Sharp global stabilization and logarithmic critical relaxation in a quadratic Lorenz-like flow*. Public mathematical research record, 2026. https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-sharp-global-stabilization-and-logarithmic-critical-relaxation-i--6e81d619c507

[3] *Parabolic confinement of bounded complete trajectories in a Lorenz-like flow*. Public mathematical research record, 2026. https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-parabolic-confinement-of-bounded-complete-trajectories-in-a-lore--6f4764b80cf0
