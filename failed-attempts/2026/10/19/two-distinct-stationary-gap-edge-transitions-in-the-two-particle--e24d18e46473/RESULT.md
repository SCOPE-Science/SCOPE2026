# Two distinct stationary gap-edge transitions in the two-particle active Dyson model

## Finding

Consider two ordered independent run-and-tumble spins, with logarithmically repelling particles and harmonic confinement as specified below. Their stationary **interparticle separation**, rather than either particle's individual-position density, exhibits two distinct edge-shape transitions. For all parameters \(\lambda,g,v,\gamma>0\), set
\[
h=\sqrt{v^2+2\lambda g},\qquad a=\frac{h-v}{\lambda},\qquad b=\frac{h+v}{\lambda}.
\]
The unique stationary separation law is supported on \([a,b]\) and has an interior density \(p\). There are constants \(C_a,C_b\in(0,\infty)\) such that
\[
 p(a+z)=C_a z^{\theta_a-1}(1+O(z)),\qquad
 p(b-z)=C_b z^{\theta_b-1}(1+O(z))\qquad (z\downarrow0),
\]
where
\[
 \theta_a=\frac{\gamma}{\lambda}\left(1-\frac{v}{h}\right),\qquad
 \theta_b=\frac{\gamma}{\lambda}\left(1+\frac{v}{h}\right).
\]
Consequently the density diverges at both edges for \(0<\gamma<\gamma_b\), diverges at the smaller-gap edge and vanishes at the larger-gap edge for \(\gamma_b<\gamma<\gamma_a\), and vanishes at both edges for \(\gamma>\gamma_a\), with the exact transition rates
\[
 \gamma_b=\frac{\lambda}{1+v/h}<\lambda<\frac{\lambda}{1-v/h}=\gamma_a.
\]
At either equality the density tends to a strictly positive finite limit at the corresponding edge. Both edge exponents obey the exact parameter-independent sum rule
\[
 (\theta_a-1)+(\theta_b-1)=\frac{2\gamma}{\lambda}-2,
 \qquad \frac{\gamma_a}{\gamma_b}=\frac{b}{a}.
\]
The separation density has no atoms at either boundary. The result concerns the one-sided endpoint limits; it does not assert global smoothness or a shape classification at any interior point.

## Assumptions and scope

Let \(X_1(t)<X_2(t)\) solve the deterministic equations between spin flips
\[
 \dot X_i=-\lambda X_i+\frac{g}{X_i-X_j}+v\sigma_i(t),\qquad j\ne i,
\]
with \(\lambda,g,v,\gamma>0\), and independent spin chains \(\sigma_i\in\{-1,+1\}\), each flipping sign at Poisson rate \(\gamma\). There is no thermal Brownian noise, no crossing, and no interaction apart from the specified reciprocal force. The separation \(Y=X_2-X_1>0\) satisfies
\[
 \dot Y=f_S(Y),\qquad f_s(y)=-\lambda y+\frac{2g}{y}+2vs,
\]
where \(S=(\sigma_2-\sigma_1)/2\in\{-1,0,+1\}\) jumps from \(\pm1\) to zero at rate \(2\gamma\), and from zero to either extremal state at rate \(\gamma\). This is the relative-coordinate subsystem of the two-particle all-to-all-interacting active-Dyson model, with a fixed normalization spelled out here.

The drift \(f_{-1}\) vanishes at \(a\), and \(f_{+1}\) vanishes at \(b\). All three drifts point into \([a,b]\) at the relevant boundaries. Between spin switches all solutions preserve strict separation. The interval is invariant, and solutions from arbitrary positive initial separation are attracted into it. Under a shared spin path, any two positive-gap solutions contract because
\[
 \frac{d}{dt}(Y_1-Y_2)=-\left(\lambda+\frac{2g}{Y_1Y_2}\right)(Y_1-Y_2).
\]
The switching chain is irreducible. Coupling and compactness give uniqueness of the invariant joint law, and accessibility by positive-duration spin intervals gives positive stationary density in each spin state in each sufficiently small open one-sided neighborhood of the corresponding accessible endpoint. The only boundaries considered are the actual gap support edges \(a,b\), not the centers of single-particle marginals.

## Proof

**1. Support and stationarity.** The three drifts are strictly decreasing, since \(f'_s(y)=-\lambda-2g/y^2<0\). For \(y<a\), every drift is strictly positive, while for \(y>b\), every drift is strictly negative. At \(a\), \(f_{-1}(a)=0\) and the remaining drifts point right; at \(b\), \(f_{+1}(b)=0\) and the remaining drifts point left. Coupling under the same stationary switching environment yields exponential contraction, and the stationary regime is uniquely selected. Long intervals of the \(-1\) (respectively \(+1\)) mode produce configurations arbitrarily near \(a\) (respectively \(b\)); irreducibility and continuously distributed switching times provide nonzero stationary mass in every open interior subinterval and locally absolutely continuous joint densities near the two edges. Because deterministic trajectories approach an equilibrium edge only asymptotically in a fixed mode, no trajectory starting in the interior hits either edge; stationary boundary atoms are impossible.

Write \(p_-,p_0,p_+\) for stationary joint densities of gap and reduced spin. Integrating the forward transport equations on an edge neighborhood gives
\[
 \begin{aligned}
 (f_-p_-)'&=-2\gamma p_-+\gamma p_0,\\
 (f_0p_0)'&=2\gamma p_-+2\gamma p_+-2\gamma p_0,\\
 (f_+p_+)'&=-2\gamma p_++\gamma p_0.
 \end{aligned}
\]
Their total spatial current \(f_-p_-+f_0p_0+f_+p_+\) is constant, and it is zero by stationarity on a compact nonperiodic interval with inaccessible endpoints. (The dynamics is irreducible in its switching modes; the reduced mode \(0\) comprises the two equal-spin microscopic states.)

**2. Left endpoint.** Fix a small interval immediately to the right of \(a\). There \(f_-<0\) and \(f_0,f_+>0\). Define the nonnegative fluxes
\[
 q=-f_-p_-,\qquad u=f_0p_0,\qquad w=f_+p_+.
\]
Current conservation gives \(q=u+w\), hence \(0\le u/q\le1\) wherever \(q>0\). The \(-1\)-state transport equation implies the scalar logarithmic derivative identity
\[
 \frac{q'}{q}=\frac{2\gamma}{-f_-}-\frac{\gamma}{f_0}\frac{u}{q}.
\]
As \(z=y-a\downarrow0\), Taylor expansion gives
\[
 -f_-(a+z)=\kappa_a z+O(z^2),\qquad
 \kappa_a=\lambda+\frac{2g}{a^2}=\frac{2\lambda h}{h-v}>0.
\]
The second term in the logarithmic derivative is bounded, because \(f_0(a)=2v>0\) and \(0\le u/q\le1\). Therefore
\[
 \frac{q'(a+z)}{q(a+z)}=\frac{2\gamma/\kappa_a}{z}+O(1).
\]
Subtract \((2\gamma/\kappa_a)\log z\) from \(\log q(a+z)\) and integrate: the remainder has bounded derivative, so it converges to a finite real constant. As \(q>0\) on this interval, the asymptotic coefficient is strictly positive. In fact
\[
 q(a+z)=d_a z^{2\gamma/\kappa_a}(1+O(z)),\qquad 0<d_a<\infty.
\]
Dividing by \(-f_-\) yields
\[
 p_-(a+z)=\frac{d_a}{\kappa_a}z^{2\gamma/\kappa_a-1}(1+O(z)).
\]
Since \(p_0=u/f_0=O(q)\) and \(p_+=w/f_+=O(q)\), the total gap density has this same leading term. Using \(2\gamma/\kappa_a=\gamma(1-v/h)/\lambda\) proves the left formula.

**3. Right endpoint.** Just to the left of \(b\), the extreme drift \(f_+>0\) and both \(f_0,f_-<0\). Define \(q=f_+p_+\), \(u=-f_0p_0\), \(w=-f_-p_-\). Again \(q=u+w\) and \(0\le u/q\le1\). The \(+1\)-state equation gives
\[
 \frac{q'}q=-\frac{2\gamma}{f_+}+\frac{\gamma}{-f_0}\frac{u}q.
\]
With \(z=b-y\),
\[
 f_+(b-z)=\kappa_bz+O(z^2),\qquad
 \kappa_b=\lambda+\frac{2g}{b^2}=\frac{2\lambda h}{h+v}.
\]
The bounded second term has no effect on the logarithmic coefficient. Integration towards \(b\) gives \(q(b-z)=d_b z^{2\gamma/\kappa_b}(1+O(z))\) with \(0<d_b<\infty\). As before the other modes contribute only \(O(q)\), so \(p(b-z)=d_b z^{2\gamma/\kappa_b-1}/\kappa_b\,(1+O(z))\). This yields \(\theta_b=\gamma(1+v/h)/\lambda\).

**4. Sharp transition and sum rules.** The sign of each \(\theta_{a,b}-1\) determines divergence, finite nonzero limit, or vanishing. Since \(v<h\), the two equalities occur at distinct positive rates \(\gamma_b<\lambda<\gamma_a\). Direct algebra proves the sum rule and \(\gamma_a/\gamma_b=b/a\). No numerical continuum extrapolation is used in these conclusions. \(\square\)

## Verification

The accompanying standalone `CHECK.py` uses only Python, NumPy, and SciPy. It checks algebraic boundary and exponent formulas across five contrasting parameter quadruples, plus an independent conservative finite-volume discretization of the coupled stationary transport equations. There are 96 assertions, all passed in the recorded execution. For \(\lambda=g=v=\gamma=1\), the exact cumulative endpoint slopes are \(0.4226497308\ldots\) and \(1.5773502692\ldots\). A 20,000-cell conservative solve gave \(0.4368107103\ldots\) and \(1.5723018734\ldots\) when fitted over finite boundary windows; the discrepancy reflects spatial-discretization error. Additional tests at two further tumbling rates check both other phase regimes. The continuum theorem rests on the flux-ratio proof, not on these finite tests.

To reproduce, place `CHECK.py` beside this file and run `python CHECK.py` with installed `numpy` and `scipy`. Only the code provided here is needed; no simulation logs, online tables, or unpublished files are dependencies.

## Relationship to prior work

Le Doussal, Majumdar, and Schehr (arXiv:2105.11838v1, 2021) derived the general relative-coordinate equation for two interacting run-and-tumble particles and a second-order stationary differential-equation treatment, including an analysis of harmonic *attraction* and potential-dependent forces. These established equations and the general three-state reduction are prior mathematical tools, not claimed here. Touzo, Le Doussal, and Schehr (arXiv:2302.02937v1, 2023) introduced active Dyson Brownian motion and investigated finite-particle and large-particle stationary **position densities** under logarithmic repulsion. Das, Dhar, and Kundu (arXiv:1912.13269v1, 2019) studied two-particle **gap statistics** under hard-core rather than logarithmic repulsion, including thermal diffusion and ring geometry. Basu et al. (arXiv:1910.10083v1, 2019) studied stationary edge exponents of a three-state run-and-tumble particle under a *linear* restoring drift, for which the two edge slopes coincide.

The precise contribution assessed here is an **explicit two-edge separation-density phase diagram with unequal drift linearizations for the logarithmically repulsive ordered pair**, together with positive finite prefactors, a universal exponent-sum identity, and threshold-ratio identity. It specializes earlier general transport equations and should not be interpreted as a new model or a new general PDMP boundary principle. Published general equations can imply the claimed special case after additional local analysis; independent literature-priority review remains warranted.

## Limitations

The theorem concerns exactly two ordered particles, identical positive independent tumbling rates, reciprocal inverse-distance repulsion, quadratic external confinement, no thermal diffusion, and one-dimensional infinite space. It does not classify interior singularities, the full gap-density formula, multi-particle gaps, rank-interaction variants, or finite-temperature regularization. The sharp endpoint asymptotics require strictly positive repulsion and hopping speed; limits in which either vanishes are singular and must be taken separately. The symbolic and finite-volume tests corroborate but cannot replace the asymptotic proof. No independent literature-priority determination is asserted.

## References

1. P. Le Doussal, S. N. Majumdar, and G. Schehr, *Stationary nonequilibrium bound state of a pair of run and tumble particles*, arXiv:2105.11838v1 (first public May 25, 2021). https://arxiv.org/abs/2105.11838
2. L. Touzo, P. Le Doussal, and G. Schehr, *Interacting, running and tumbling: the active Dyson Brownian motion*, arXiv:2302.02937v1 (first public February 6, 2023). https://arxiv.org/abs/2302.02937
3. A. Das, A. Dhar, and A. Kundu, *Gap statistics of two interacting run and tumble particles in one dimension*, arXiv:1912.13269v1 (first public December 31, 2019). https://arxiv.org/abs/1912.13269
4. U. Basu, S. N. Majumdar, A. Rosso, S. Sabhapandit, and G. Schehr, *Exact stationary state of a run-and-tumble particle with three internal states in a harmonic trap*, arXiv:1910.10083v1 (first public October 22, 2019). https://arxiv.org/abs/1910.10083
