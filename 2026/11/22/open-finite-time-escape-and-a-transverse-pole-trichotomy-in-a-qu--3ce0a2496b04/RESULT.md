# Open finite-time escape and a transverse pole trichotomy in a quadratic chameleon flow

## Finding

For the polynomial system
\[
\dot x=y,\qquad \dot y=-x+zy,\qquad
\dot z=a-bz+cz^2-5xy+xz,\qquad a,b\in\mathbb R,\ c>0,
\]
there is an invariant axial family of **finite-time escaping trajectories**. Their transverse variational equations exhibit a critical exponent at \(c=1\). For every \(c>1\), finite-time escape is not confined to the axis: a specified nonempty open subset of three-dimensional initial conditions also escapes, with a sharp nonlinear asymptotic transverse amplitude.

More precisely, choose any axial height \(z_0\) with \(q(z)=a-bz+cz^2>0\) for every \(z\ge z_0\). The axial orbit has a finite forward endpoint \(T\), and, writing \(s=T-t\),
\[
T=\int_{z_0}^{\infty}\frac{d\zeta}{q(\zeta)},\qquad
z(T-s)=\frac{1}{cs}+O(1).
\]
The linearized transverse system \(\dot u=v,\ \dot v=-u+z(t)v\) has a basis consisting of a bounded mode
\[
u_b(T-s)=1-\frac{c}{2(c+1)}s^2+O(s^3),\qquad
v_b(T-s)=\frac{c}{c+1}s+O(s^2)
\]
and a singular mode normalized by \(v_f(T-s)\sim-s^{-1/c}\), for which
\[
u_f(T-s)\sim
\begin{cases}
\dfrac{c}{c-1}s^{1-1/c},& c\ne 1,\\
\log s,&c=1.
\end{cases}
\]
Thus the singular position decays to zero for \(c>1\), diverges logarithmically at \(c=1\), and diverges by a power for \(0<c<1\), while its vertical velocity always diverges. The quotient \(|v_f|/z\) tends to zero, a positive finite limit, or infinity in these respective regimes.

For \(c>1\), let \(1/c<p<1\), \(1/p<\kappa<c\), and \(X,Y>0\). For every sufficiently large \(Z\), the entire open set
\[
\mathcal U=\{(x_0,y_0,z_0):z_0>Z,\ |x_0|<X/2,\ |y_0|<Yz_0^p/2\}
\]
escapes through \(z(t)\to+\infty\) at a finite time \(T\le1/(\kappa z_0)\). Each such solution has constants \(C\in\mathbb R\) and \(x_\infty\in\mathbb R\) satisfying
\[
z(t)\sim\frac1{c(T-t)},\qquad
y(t)=Cz(t)^{1/c}+o(z(t)^{1/c}),\qquad
x_\infty-x(t)=\frac{C}{c-1}z(t)^{1/c-1}+o(z(t)^{1/c-1}).
\]
A nonempty open subregion of \(\mathcal U\) has \(C>0\), so the last two displayed leading terms can be nonzero.

## Assumptions and scope

All assertions concern classical solutions of the displayed autonomous polynomial ODE. The constants \(a,b\) are arbitrary real numbers and \(c>0\). The axial theorem applies to heights above all relevant positive roots of \(q\); such heights always exist. The transverse trichotomy is for the **linearized** equations along these axial solutions and does not assert nonlinear stability when \(c\le1\). The open-set nonlinear asymptotics require \(c>1\) and sufficiently large positive initial height.

For explicit numerical choices \(a=1\), \(b=0\), \(c=2\), one can take \(p=3/4\), \(\kappa=3/2\), \(X=Y=1\), and \(Z=10^4\). At the published no-equilibrium parameter choice \((a,b,c)=(0.1,0.195,0.1)\), the scalar axial polynomial \(q\) is positive on all of \(\mathbb R\), so **every axial initial height** escapes in finite forward time; the singular transverse position has the power \(s^{-9}\). This does not claim that the attracting numerical orbit shown for other initial data escapes.

## Proof

**1. Exact axial solution.** The set \(x=y=0\) is invariant and restricts the flow to \(\dot z=q(z)\). Above sufficiently high \(z_0\), the quadratic is positive and \(q(z)\sim cz^2\), so the displayed integral gives a finite maximal forward time and \(z\to+\infty\). Setting \(w=1/z\), and viewing \(s=T-t\) as the independent variable, gives the *analytic* initial-value equation
\[
\frac{dw}{ds}=c-bw+aw^2,\qquad w(0)=0.
\]
It follows that \(w(s)=cs+O(s^2)\), hence \(z(T-s)=1/(cs)+O(1)\).

**2. Transverse fundamental system.** The full linearization has a height component satisfying \(\dot\xi=z(t)u+q'(z(t))\xi\), which does not feed back into the normal quotient. The differential of \((\dot x,\dot y)\) on the axis is
\[
\dot u=v,\qquad\dot v=-u+z(t)v.
\]
For \(u(s)=u(T-s)\), eliminating \(v\) yields
\[
u_{ss}+z(T-s)u_s+u=0,\qquad v=-u_s.
\]
Since \(z(T-s)=1/(cs)+O(1)\) with an analytic regular part, the origin is regular singular. Its indicial equation \(r(r-1)+r/c=0\) has roots \(0\) and \(1-1/c\). Substituting a power series with constant term one gives the analytic bounded solution with zero linear term and second coefficient \(-c/[2(c+1)]\). A linearly independent solution follows directly by reduction of order:
\[
 u_f(s)=u_b(s)\int^s \frac{\exp(-\int^r z(T-\eta)\,d\eta)}{u_b(r)^2}\,dr.
\]
The integrand equals \(r^{-1/c}(1+O(r))\), up to a constant chosen as one. If \(c>1\), choose the outer integration constant to remove the bounded component. Integration gives the power law for \(c\ne1\) and the logarithm for \(c=1\); differentiation gives \(v_f=-u_{f,s}\sim-s^{-1/c}\). These two solutions have nonzero Wronskian, so they span all transverse linearizations. A possible subleading resonance logarithm does not alter the displayed leading laws.

**3. A robust open escaping tube.** Fix \(c>1\), \(p,\kappa,X,Y\) as in the statement. Increase \(Z\) until the following inequalities hold for every \(z\ge Z\):
\[
cz^2-(|b|+X)z-|a|-5XYz^p\ge\kappa z^2,
\]
\[
(p\kappa-1)Yz\ge Xz^{-p},\qquad
\frac{Y}{\kappa(1-p)}Z^{p-1}<\frac X2.
\]
They are eventually true since \(p<1\), \(p\kappa>1\) and \(\kappa<c\). In the tube \(z\ge Z\), \(|x|<X\), \(|y|<Yz^p\), the equation gives \(z'\ge\kappa z^2>0\). On a hypothetical first lateral boundary \(|y|/z^p=Y\), the upper right derivative obeys
\[
D^+\left(\frac{|y|}{z^p}\right)
\le Xz^{-p}+(1-p\kappa)zY\le0.
\]
A strict inequality follows by enlarging \(Z\) when necessary. Meanwhile
\[
|x(t)-x_0|\le\int_0^t|y|\,d\tau
\le\frac Y\kappa\int_{z_0}^{z(t)}\zeta^{p-2}\,d\zeta
\le\frac{Y}{\kappa(1-p)}z_0^{p-1}<X/2.
\]
Thus no first tube exit is possible, and the positive differential inequality forces a finite forward endpoint \(T\le1/(\kappa z_0)\), with \(z\uparrow\infty\). The upper bound \(z'=O(z^2)\) follows from the same tube, and together with \(z'=cz^2[1+O(1/z)]\), gives \(z(T-s)\sim1/(cs)\).

**4. Sharp nonlinear amplitudes.** Use increasing \(z\) as independent variable and put \(Q=cz^2-bz+a-5xy+xz\). In the tube, \(Q=cz^2[1+O(1/z)]\). For \(Y_*(z)=y(z)z^{-1/c}\), direct differentiation shows
\[
\frac{dY_*}{dz}=
\left(\frac zQ-\frac1{cz}\right)Y_*-\frac{x}{Qz^{1/c}}.
\]
The first coefficient is \(O(z^{-2})\), and the forcing is \(O(z^{-2-1/c})\). Variation of constants on a half-line gives a finite limit \(Y_*(z)\to C\). Since \(y=O(z^p)\) with \(p<1\), the function \(x(z)\) converges, and integrating \(dx/dz=y/Q\) from \(z\) to infinity yields the claimed \(x_\infty-x\) expansion. The logarithmic derivative of \(e^{\int_0^t z(\tau)d\tau}/z(t)^{1/c}\), with respect to \(z\), is \(z/Q-1/(cz)=O(z^{-2})\); hence that quotient tends to a finite positive constant. The identity
\[
y(t)e^{-\int_0^t z(\tau)d\tau}
=y_0-\int_0^t x(\sigma)e^{-\int_0^\sigma z(\tau)d\tau}\,d\sigma
\]
therefore shows \(C>0\) whenever \(y_0>X/(\kappa z_0)\), since \(T\le1/(\kappa z_0)\) and \(|x|<X\). Such \(y_0\) occur in a nonempty open part of the stated set.

**5. Source-parameter specialization.** At \((a,b,c)=(0.1,0.195,0.1)\), the quadratic discriminant is \(b^2-4ac=-0.001975<0\), proving \(q(z)>0\) for all real \(z\). Its critical singular-position exponent is \(1-1/c=-9\), as stated.

## Verification

The companion `checks/escape_checker.py` checks the local series identities symbolically, verifies all inequalities for an explicit rational-parameter tube, and integrates the regularized equations with \(z\) as independent variable to test the nonlinear asymptotic laws. It is supplemental numerical/symbolic evidence, not a substitute for the quantified analytic inequalities and ODE proof. A reproducible command is `python checks/escape_checker.py`, with Python, SymPy and SciPy installed.

## Relationship to prior work

Zhang, Sang, Li, Liu, Fan and Wang introduced this exact three-dimensional family and described equilibria, Hopf bifurcations, numerical chaotic attractors, and a circuit realization [1]. The published calculations concern bounded numerical behavior for selected initial states and do not state the present finite-time axial and open-set escape theorem or its transverse singular-mode threshold. General Riccati comparison, regular-singular ODE theory and variation of constants are classical techniques; novelty is claimed only for their mathematically explicit combination and phase threshold **for this particular published flow**. A later chameleon-family study [2] was compared using the author-uploaded full text: its defining system has \(\dot x=z\), \(\dot y=x-yz\), and different quadratic nonlinearities, so its Hopf and numerical-bifurcation conclusions do not imply this theorem for the displayed model. General unindexed equivalences remain a publication-priority risk.

## Limitations

No statement is made about the global basin of attraction, all initial data, the existence/nonexistence of a chaotic compact invariant set, or nonlinear transverse stability at \(c\le1\). The exceptional linearized singular solution need not be realized as an infinitesimal approximation uniformly up to the finite-time endpoint. The stable-looking linearized position for \(c>1\) does not by itself prove nonlinear stability; the open tube provides a separate nonlinear conclusion. The strict positive-constant asymptotic holds on the specified open subregion, while \(C\) may vanish elsewhere. Publication priority is conditional on the literature inspected and is not a mathematical uniqueness proof.

## References

[1] X. Zhang, B. Sang, B. Li, J. Liu, L. Fan and N. Wang, “Hidden chaotic mechanisms for a family of chameleon systems,” *Mathematical Modelling and Control* **3** (2023), 400–415, DOI: https://doi.org/10.3934/mmc.2023032, open article https://www.aimspress.com/article/doi/10.3934/mmc.2023032 and full text https://www.aimspress.com/aimspress-data/mmc/2023/4/PDF/mmc-03-04-032.pdf.

[2] L. Fan et al., “Bifurcation Patterns in Some Chameleon Systems,” *International Journal of Bifurcation and Chaos* (2024), DOI: https://doi.org/10.1142/S0218127424501499; author-uploaded text https://www.researchgate.net/publication/378183099_Bifurcation_patterns_in_some_chameleon_systems (equations and principal results inspected).
