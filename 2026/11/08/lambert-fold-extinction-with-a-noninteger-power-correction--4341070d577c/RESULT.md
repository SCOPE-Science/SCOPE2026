# Lambert-fold extinction with a noninteger power correction

## Finding

Consider the nondimensional ratio-dependent predator–prey flow of Blyuss, Kyrychko and Blyuss [1]:
\[
\dot u=u(1-u)-a v e^{-\alpha v/u},\qquad
\dot v=v(b e^{-\alpha v/u}-d),\qquad u,v>0.
\]
For arbitrary \(\alpha,d>0\) and \(0<q<d/(d+1)\), tune the two ecological interaction rates to the **exact Lambert-fold surface**
\[
a=\alpha(d+1)e^{1-q},\qquad b=q(d+1)e^{1-q}.
\]
Define
\[
z_*=\frac{1-q}{\alpha},\quad \mu=d-(d+1)q>0,\quad
\kappa=\frac{\alpha(d+1)(1-q)}2>0,\quad
\nu=\frac{2q}{1-q}>0.
\]
There are \(\delta,\varepsilon>0\), depending only on these parameters, such that **every** initial condition with
\[
0<u(0)<\varepsilon,\qquad z_*<\frac{v(0)}{u(0)}<z_*+\delta
\]
has a globally positive solution converging to extinction and satisfying both exact limits
\[
\boxed{\lim_{t\to\infty}t\left(\frac{v(t)}{u(t)}-z_*\right)=\frac1\kappa
=\frac{2}{\alpha(d+1)(1-q)}}
\]
and
\[
\boxed{\lim_{t\to\infty} e^{\mu t}t^{\nu}(u(t),v(t))
=C\,(1,z_*),\qquad 0<C<\infty.}
\]
The positive constant \(C\) depends on the initial state, but the exponential rate, noninteger power and limiting predator-to-prey ratio do not.

At the same fold there is a one-dimensional local strong-stable curve containing positive states, whose graph in ratio coordinates has the exact leading slope
\[
\frac vu=z_*-\frac{z_*}{\mu}u+O(u^2).
\]
Positive trajectories on this exceptional curve instead satisfy
\[
e^{\mu t}(u(t),v(t))\longrightarrow C_{\rm s}(1,z_*),\qquad C_{\rm s}>0,
\]
with no noninteger power factor. When additionally \(b<d\), the prey-only equilibrium \((1,0)\) is locally asymptotically stable, while the displayed open wedge still goes extinct. Consequently both prey survival and total extinction have nonempty open basins **at** the angular saddle-node threshold.

## Assumptions and scope

Parameters, initial data and time are nondimensional as in equation (4) of [1]. All statements concern deterministic physical time \(t\), not a rescaled orbit parameter. The theorem holds for all real \(\alpha,d,q\) in the specified open domain, without requiring \(b<d\) except for the final bistability assertion. The attracting extinction sector is a local, explicitly oriented open family in the positive quadrant; no global basin classification is asserted. The strong-stable curve's expansion refers to the smooth blown-up coordinates \((u,z=v/u)\) with \(u>0\).

For a fully explicit coexistence of prey-only stability and critical extinction, choose
\[
\alpha=d=1,\quad q=\tfrac1{10},\quad a=2e^{9/10},\quad b=\tfrac15e^{9/10}<1.
\]
Then \(z_*=9/10\), \(\mu=4/5\), \(\kappa=9/10\), \(\nu=2/9\), and the universal ratio tail is
\[
\lim_{t\to\infty}t\left(\frac{v(t)}{u(t)}-\frac9{10}\right)=\frac{10}{9}.
\]
The exceptional strong-stable curve begins with \(v/u=9/10-9u/8+O(u^2)\).

## Proof

**1. Exact double root.** Set \(z=v/u\) for positive populations. Direct differentiation, without a time reparametrization, gives the smooth system
\[
\dot u=u[\lambda(z)-u],\quad
\dot z=z[h(z)+u],\quad
\lambda(z)=1-az e^{-\alpha z},\quad
h(z)=(b+az)e^{-\alpha z}-(d+1).
\]
At the stated parameters, \(b+az_*=a/\alpha\), \(ae^{-\alpha z_*}=\alpha(d+1)\), and therefore
\[
h(z_*)=h'(z_*)=0,\quad
h''(z_*)=-\alpha^2(d+1)<0,\quad
\lambda(z_*)=-\mu,\quad
\lambda'(z_*)=-\alpha(d+1)q.
\]
Moreover \(h'(z)\) has the sign of \(z_*-z\), so \(h\le0\) for all positive \(z\), with equality only at \(z_*\). Thus the two positive Lambert-W boundary equilibria of [1] have merged in a quadratic maximum at exactly this parameter surface. Writing \(w=z-z_*\), Taylor expansion yields
\[
\dot u=u[-\mu+\lambda'(z_*)w+O(w^2)-u],\qquad
\dot w=-\kappa w^2+z_*u+O(w^3+u|w|).
\]
All Taylor remainders are uniform in a sufficiently small rectangle around \((u,w)=(0,0)\).

**2. An invariant extinction wedge.** Choose \(\delta>0\) small enough that \(\lambda(z)\le-\mu/2\) on \([z_*,z_*+\delta]\). Since \(h(z_*+\delta)<0\), choose \(\varepsilon>0\) with \(\varepsilon<-h(z_*+\delta)\). On the top edge \(z=z_*+\delta\), \(\dot z<0\); on the bottom edge \(z=z_*\) with \(u>0\), \(\dot z=z_*u>0\). Meanwhile \(\dot u\le-\mu u/2\), so \(0<u(t)\le u(0)e^{-\mu t/2}\), and the rectangle remains forward invariant. Positivity and classical continuation give a global solution. The ratio \(z(t)\) must converge to \(z_*\): if it stayed a fixed distance above \(z_*\), the negative term \(z h(z)\) would eventually dominate the exponentially decaying forcing \(zu\), forcing it downward. More formally, for any fixed small \(\eta>0\), the vector field on \(z\in[z_*+\eta,z_*+\delta]\) becomes strictly negative after finite time; the lower edge \(z_*\) cannot be crossed.

**3. Sharp angular tail.** For \(w(t)>0\), the last differential equation gives, with \(\kappa>0\),
\[
\frac{d}{dt}\frac1w=\kappa+O(w)-\frac{(z_*+w)u}{w^2}.
\]
Because \(h(z)\ge-M w^2\) in the trapping rectangle for some \(M>0\), we have \(\dot w\ge-M' w^2\), hence \(w(t)\ge (w(0)^{-1}+M't)^{-1}\). Thus \(u/w^2\) is integrable on \([0,\infty)\). As \(w\to0\), integration first yields \(1/w=\kappa t+o(t)\), hence \(w=O(1/t)\). Integrating once more yields the sharper
\[
\frac1{w(t)}=\kappa t+O(\log t),\qquad
w(t)=\frac1{\kappa t}+O\left(\frac{\log t}{t^2}\right).
\]
In particular \(t w(t)\to1/\kappa\), \(\int_1^\infty w^2(t)\,dt<\infty\), and
\[
\int_1^t w(s)\,ds=\frac1\kappa\log t+B+o(1)
\]
for a finite trajectory-dependent constant \(B\).

**4. Noninteger extinction exponent.** Taking a logarithmic derivative of \(u\),
\[
\frac d{dt}\log u=-\mu+\lambda'(z_*)w+O(w^2)-u.
\]
The two remainder terms are integrable by steps 2–3. The angular integral in step 3 gives
\[
\log u(t)=-\mu t+\frac{\lambda'(z_*)}{\kappa}\log t+L+o(1),
\]
where \(L\) is finite. The exact cancellation
\[
-\frac{\lambda'(z_*)}{\kappa}
=\frac{\alpha(d+1)q}{\alpha(d+1)(1-q)/2}
=\frac{2q}{1-q}=\nu
\]
yields \(C=e^L>0\). Since \(v=zu\) and \(z\to z_*\), the claimed two-component extinction profile follows.

**5. Exceptional strong-stable curve and prey-only phase.** At \((u,z)=(0,z_*)\) the Jacobian is
\[
J=\begin{pmatrix}-\mu&0\\ z_*&0\end{pmatrix}.
\]
The strong-stable manifold theorem applies to its isolated negative eigenvalue \(-\mu\) despite the simultaneous zero eigenvalue. Its stable eigenvector with first coordinate one has second coordinate \(-z_*/\mu\). Thus the strong-stable graph has the asserted expansion and, for sufficiently small \(u>0\), stays in the positive-population region because \(z\) is close to the positive value \(z_*\). On this curve \(u'/u=-\mu+O(u)\), while \(u\) decays exponentially. Integration yields a strictly positive, finite \(C_{\rm s}\) and the stated pure-exponential limit. Finally, at \((u,v)=(1,0)\) the linear eigenvalues are \(-1\) and \(b-d\). When \(b<d\) this state has an open attraction basin, distinct from the extinction wedge constructed in step 2.

## Verification

The included standalone `verify.py` symbolically reconstructs the double-root identities, the negative radial eigenvalue, the coefficient \(\kappa\), the exponent \(\nu\), and the strong-stable tangent. It additionally integrates the smooth blown-up equations for the exact parameter example using a fourth-order Runge–Kutta scheme in logarithmic prey coordinates, checking the predicted ratio limit and convergence of the normalized extinction amplitude. This numerical test corroborates but does not prove the infinite-time limits; steps 1–5 are the mathematical proof. Run with `python verify.py` (requires SymPy for symbolic identities, and Python's standard library for the numerical cross-check).

## Relationship to prior work

Blyuss, Kyrychko and Blyuss [1] introduced the same nondimensional model and its \(z=v/u\) blow-up, gave Lambert-W formulas for two candidate extinction directions and strict eigenvalue conditions, and numerically charted stability and bistability. The formula for a collision of their two Lambert-W branches follows from that work. It does **not** by itself give the nonlinear dynamics at equality, the angular \(1/t\) coefficient, the multiplicative \(t^{-\nu}\) correction to physical population decay, or the exceptional strong-stable trajectory. These critical-time statements are the present claim.

The earlier delay/stochastic study of the same trophic response [2] treats coexistence, delays and stochastic fluctuations, not the undelayed angular fold asymptotics. Jost, Arino and Arditi [3] study deterministic extinction in a different ratio-dependent interaction class, and Xiao and Jennings [4] analyze a constant-harvesting system whose origin is not an equilibrium. General saddle-node normal forms explain the quadratic bottleneck qualitatively; they do not supply the model-dependent coupling coefficient or the exact physical-time population exponent without the calculation here.

## Limitations

This is a local extinction-sector theorem at a tuned codimension-one boundary, not a classification of all positive initial conditions or a result about stochastic extinction times. The coefficient \(C\) depends on initial data and is not claimed to have an elementary closed form. The source article and general saddle-node theory provide necessary background; novelty of the precise joint asymptotic and extinction-wedge result remains subject to unindexed literature and independent scrutiny. A 1999 ratio-dependent extinction paper [3] was available only through abstracts/metadata during this comparison; its full text was not checked. The analytic argument is independent of any numerical calculation.

## References

[1] K. B. Blyuss, Y. N. Kyrychko and O. B. Blyuss, “Complex dynamics near extinction in a predator-prey model with ratio dependence and Holling type III functional response,” *Frontiers in Applied Mathematics and Statistics* **8**, 1083815 (first publicly dated 2022-12-07), DOI: https://doi.org/10.3389/fams.2022.1083815; publicly accessible full text https://www.frontiersin.org/journals/applied-mathematics-and-statistics/articles/10.3389/fams.2022.1083815/full; later arXiv version https://arxiv.org/abs/2305.04053.

[2] K. B. Blyuss, S. N. Kyrychko, Y. N. Kyrychko, “Time-delayed and stochastic effects in a predator–prey model with ratio dependence and Holling type III functional response,” *Chaos* **31**, 073141 (2021), DOI: https://doi.org/10.1063/5.0055623.

[3] C. Jost, O. Arino and R. Arditi, “About deterministic extinction in ratio-dependent predator-prey models,” *Bulletin of Mathematical Biology* **61**, 19–32 (1999), DOI: https://doi.org/10.1006/bulm.1998.0072.

[4] D. Xiao and L. S. Jennings, “Bifurcations of a ratio-dependent predator-prey system with constant rate harvesting,” *SIAM Journal on Applied Mathematics* **65**, 737–753 (2005), DOI: https://doi.org/10.1137/S0036139903428719.
