# A two-thirds-power thermal cusp for biased run-and-tumble motion in a harmonic trap

## Finding
Consider a one-dimensional run-and-tumble particle confined by a harmonic restoring force. Let the dimensionless rates of switching from rightward to leftward propulsion and vice versa be \(a\) and \(b\), respectively. For every \(0<a,b<1\), its stationary position density has two strict local maxima at sufficiently small positive thermal variance \(s\), exactly one strict local maximum at sufficiently large \(s\), and a **unique** mode-loss threshold \(s_*(a,b)>0\). The number of modes is two below this threshold and one above it. At a nonsymmetric threshold near \(a=b\), a simple stationary maximum coexists with a double zero of the density derivative: one secondary peak merges with the intervening minimum.

The **new quantitative assertion** is a sharp cusp law near equal switching rates. Fix \(0<\ell<1\) and put \(a=\ell+\varepsilon\), \(b=\ell-\varepsilon\). Write
\[
\phi_\ell(t)={}_1F_1\!\left(\frac12;\ell+\frac12;-t\right),\qquad
\phi_\ell(t_\ell)+2t_\ell\phi_\ell'(t_\ell)=0,\qquad
s_\ell=\frac1{2t_\ell}.
\]
The equation has exactly one positive root \(t_\ell\). Define the probability measure
\[
\nu_\ell(dy)=\frac{e^{-y^2/(2s_\ell)}(1-y^2)^{\ell-1}\mathbf1_{(-1,1)}(y)\,dy}
{\int_{-1}^1e^{-z^2/(2s_\ell)}(1-z^2)^{\ell-1}\,dz}
\]
and the strictly positive constant
\[
A_\ell=\left(\frac{3s_\ell}{1-\ell}\int_{-1}^1 y\operatorname{arctanh}(y)\,\nu_\ell(dy)\right)^{1/3}.
\]
For all sufficiently small nonzero \(\varepsilon\), the mode-loss threshold and the location of the coalescing stationary points satisfy
\[
\boxed{\ s_*(\ell+\varepsilon,\ell-\varepsilon)
=s_\ell-A_\ell^2|\varepsilon|^{2/3}+o(|\varepsilon|^{2/3})\ },
\]
\[
\boxed{\ x_*(\varepsilon)=A_\ell\operatorname{sgn}(\varepsilon)|\varepsilon|^{1/3}
+o(|\varepsilon|^{1/3})\ }.
\]
Thus an arbitrarily weak bias lowers the thermal variance needed to erase one of two peaks by an amount larger than linear in the bias. The critical exponent \(2/3\), the coefficient \(A_\ell^2\), and the sign of the fold displacement are exact. The symmetric critical threshold itself and the stationary beta/Gaussian-convolution structure are **prior results**; the asymmetric global mode classification and explicit cusp unfolding are the claims evaluated here.

## Assumptions and scope
In time units set by the positive trap relaxation rate \(\kappa\), let
\[
dY_t=(-Y_t+S_t)\,dt+\sqrt{2s}\,dW_t,
\]
where \(S_t\in\{-1,+1\}\) is an independent two-state continuous-time Markov chain with transition rates \(+1\to-1\) equal to \(a>0\) and \(-1\to+1\) equal to \(b>0\). Here \(s>0\) is the variance of the stationary thermal Ornstein–Uhlenbeck component. In physical variables, \(Y=\kappa X/v\) and \(s=D\kappa/v^2\), with thermal diffusivity \(D\), propulsion speed \(v\), and trap relaxation rate \(\kappa\). For global mode classification assume \(0<a,b<1\). For the cusp set \(a=\ell+\varepsilon\), \(b=\ell-\varepsilon\), with \(\ell\in(0,1)\) fixed and \(|\varepsilon|<\min(\ell,1-\ell)\).

The unique stationary position law is the convolution
\[
p_{a,b,s}(x)=\int_{-1}^1q_{a,b}(y)\frac{e^{-(x-y)^2/(2s)}}{\sqrt{2\pi s}}\,dy,
\quad
q_{a,b}(y)=\frac{(1-y)^{a-1}(1+y)^{b-1}}{2^{a+b-1}B(a,b)}\mathbf1_{(-1,1)}(y).
\]
The normalization uses \(\int_{-1}^1 (1-y)^{a-1}(1+y)^{b-1}dy=2^{a+b-1}B(a,b)\).

## Proof
**1. The stationary law.** Decompose the stationary causal solution into the independent telegraph and Brownian convolutions, \(Y=\int_0^\infty e^{-u}S_{-u}\,du+\sqrt{2s}\int_0^\infty e^{-u}\,dW_{-u}\). The second term is centered normal with variance \(s\). For the first term let \(q_+\) and \(q_-\) be joint stationary densities on \((-1,1)\). The zero-current equation gives \((1-y)q_+=(1+y)q_-\), while the gain-loss equation gives \(\partial_y[(1-y)q_+]=-aq_++bq_-\). Integration yields \(q_++q_-\propto(1-y)^{a-1}(1+y)^{b-1}\), establishing the formula above. Positivity of both switching rates and the trap contraction give uniqueness of the stationary law.

**2. At most two modes and exactly one loss event.** The log derivative of \(q_{a,b}\) is
\[
\frac{q'_{a,b}(y)}{q_{a,b}(y)}=\frac{1-a}{1-y}-\frac{1-b}{1+y},
\]
which increases strictly for \(0<a,b<1\); it has exactly one zero in \((-1,1)\). The density diverges at both endpoints and has an interior strict minimum. Approximate this compactly supported endpoint-singular density in \(L^1\) by smooth compactly supported densities having a rise–fall–rise–fall derivative-sign pattern and no more than three derivative sign changes. Gaussian convolution is strictly variation diminishing; therefore \(p'_{a,b,s}\) has at most three sign-changing zeros for every \(s>0\), and \(p_{a,b,s}\) has at most two modes. The small-variance limit agrees locally in the interior with \(q_{a,b}\); in combination with the always-positive derivative to the left of \(-1\) and always-negative derivative to the right of \(1\), this produces three alternating derivative zeros for sufficiently small \(s\). Thus two modes genuinely exist.

For any \(s>1\), the posterior law of \(Z\in[-1,1]\) given \(Z+\sqrt{s}G=x\) has variance at most one. Twice differentiating the Gaussian mixture gives
\[
\frac{d^2}{dx^2}\log p_{a,b,s}(x)=\frac{\operatorname{Var}(Z\mid Z+\sqrt{s}G=x)-s}{s^2}<0,
\]
so there is exactly one maximum. As \(s\) grows, \(p'\) solves \(\partial_s p'=(1/2)\partial_x^2p'\). The classical one-dimensional parabolic zero-number/strict variation-diminishing principle says that simple sign-changing zeros cannot be created, and multiple zeros strictly decrease their number. All derivative zeros lie in \((-1,1)\), because the integrand of \(p'\) has a fixed sign for \(x\notin[-1,1]\). Thus there is precisely one mode-count transition from two maxima to one, at a positive finite \(s_*(a,b)\). The general strict zero-number theorem is a standard external ingredient, not proved here from first principles.

**3. The symmetric threshold.** At \(a=b=\ell\), symmetry forces \(p'(0)=\partial_x^3p(0)=0\). The curvature condition \(p''(0)=0\) can be expressed using \(t=1/(2s)\) as \(w_\ell(t)=\phi_\ell(t)+2t\phi_\ell'(t)=0\). For \(0<\ell<1\), \(w_\ell(0)=1\) and \(w_\ell(t)<0\) for sufficiently large \(t\) by the large-\(t\) Laplace expansion of \((1-y^2)^{\ell-1}\) around zero. Kummer's differential equation for \(\phi\) implies that at every positive zero of \(w_\ell\), \(w_\ell'(t)=2(1-\ell)\phi_\ell'(t)<0\). All such roots would be strict downward crossings, so there is exactly one, \(t_\ell\). This symmetric transition is already discussed in the cited 2026 literature.

**4. A nondegenerate quartic coefficient.** Let \(p_0=p_{\ell,\ell,s_\ell}(0)>0\). Under the Gaussian-tilted law \(\nu_\ell\), differentiation of \(\phi_\ell\) at \(t_\ell\), followed by Kummer's equation, gives
\[
\mathbb E_{\nu_\ell}Y^2=s_\ell,
\qquad \mathbb E_{\nu_\ell}Y^4=(2\ell+1)s_\ell^2.
\]
Consequently the fourth spatial derivative is
\[
K:=\partial_x^4p_{\ell,\ell,s_\ell}(0)
=\frac{2(\ell-1)p_0}{s_\ell^2}<0.
\]
Also \(\partial_\varepsilon\log q_{\ell+\varepsilon,\ell-\varepsilon}(y)|_{0}=\log[(1-y)/(1+y)]=-2\operatorname{arctanh}(y)\), since its symmetric normalization derivative vanishes. Differentiating the integral at \(x=0\) yields
\[
B:=\left.\partial_\varepsilon\partial_xp_{\ell+\varepsilon,\ell-\varepsilon,s_\ell}(0)\right|_{\varepsilon=0}
=-\frac{2p_0}{s_\ell}\mathbb E_{\nu_\ell}[Y\operatorname{arctanh}Y]<0.
\]
The integral is strictly positive, finite and contains only endpoint logarithmic singularities.

**5. The cusp.** Define \(F(x,s,\varepsilon)=\partial_xp_{\ell+\varepsilon,\ell-\varepsilon,s}(x)\), and let \(\tau=s-s_\ell\). By reflection symmetry and the heat equation,
\[
F(x,s_\ell+\tau,\varepsilon)
=B\varepsilon+\frac K2\tau x+\frac K6x^3
+o(|\varepsilon|+|\tau x|+|x|^3)
\]
in the natural cusp scaling \(x=O(|\varepsilon|^{1/3})\), \(\tau=O(|\varepsilon|^{2/3})\). A fold solves \(F=F_x=0\). Setting \(\delta=|\varepsilon|^{1/3}\), \(x=\delta u\), \(\tau=\delta^2v\), the leading equations give
\[
v=-u^2,\qquad u^3=\frac{3B}{K}\operatorname{sgn}(\varepsilon)
=\frac{3s_\ell}{1-\ell}\mathbb E_{\nu_\ell}[Y\operatorname{arctanh}Y]\operatorname{sgn}(\varepsilon).
\]
The two-equation Jacobian in \((u,v)\) is nonzero at this solution (its determinant is \(-K^2u^2/2\)). The implicit-function theorem, applied after rescaling, produces the actual local fold and the two asserted asymptotics. Step 2 makes it the only global mode-loss transition. For positive \(\varepsilon\) it occurs to the right, where the weaker peak vanishes; for negative \(\varepsilon\) the picture is reflected. The proof is for fixed \(\ell\); no uniformity as \(\ell\to0\) or \(\ell\to1\) is asserted.

## Verification
For \(\ell=1/2\), the critical variance is \(s_{1/2}=0.3164643403484473\ldots\), and the cusp coefficient is \(A_{1/2}=1.0116863052989679\ldots\). The attached standalone `VERIFY.py` uses Gauss–Jacobi integration, independent two-state generator moment identities, adaptive quadrature for the endpoint-logarithmic coefficient and numerical solutions of \(p'=p''=0\) for both bias signs. It checks three distinct symmetric base rates and four small signed asymmetries per rate. These numerical tests check formulas and implementation, not the global infinite-parameter claims; those follow from the analytic proof and the cited zero-number theorem.

## Relationship to prior work
Guéneau, Majumdar and Schehr (arXiv:2602.08436, first public February 9, 2026) provide general discrete-state stationary distributions via Dirichlet weights, including unequal two-state weights as a special case, and the Gaussian thermal convolution. They also explicitly analyze the **symmetric** one-dimensional thermal bimodal-to-unimodal crossover in Sec. V. Thus neither the beta convolution, the symmetric critical temperature nor a generic stationary distribution formula is asserted to be new here. Sevilla and Meléndez Mora (arXiv:2608.21781, first public August 22, 2026) independently present the exact thermal OU convolution and symmetric-rate stationary shape analysis. The present theorem concerns the **global two-peak classification under distinct flip rates and the explicit asymmetric cusp exponent and coefficient**. Garcia-Millan and Pruessner (arXiv:2012.02900) provide earlier field-theoretic treatments of trapped run-and-tumble motion, while Angenent's parabolic zero-set theorem is the classical variation-diminishing tool used in the proof. The cubical local fold shape is a standard catastrophe-theory normal form; only its specific exact coefficients and physical model application are considered potentially new. No priority or independence certification is claimed.

## Limitations
The result requires an infinite-line harmonic trap, constant two-state propulsion speeds, Markov switching, independent thermal white noise and \(0<a,b<1\). The global classification relies on standard strict Gaussian variation diminution and parabolic zero-number results. The asymptotic coefficients depend on the fixed base rate \(\ell\). The analysis treats the **number of stationary density modes**, not mixing rates, first-passage distributions, information-theoretic functionals or experimentally finite-resolution peak recognition. Additional overlapping results in unindexed or inaccessible literature could affect publication priority. A separate independent audit has not been performed.

## References
1. F. J. Sevilla and J. A. Meléndez Mora, *Nonequilibrium statistics of harmonically trapped run-and-tumble particles: An exact convolution approach*, arXiv:2608.21781v1 (first publicly submitted 2026-08-22), https://arxiv.org/abs/2608.21781.
2. M. Guéneau, S. N. Majumdar and G. Schehr, *Exact Stationary State of a d-dimensional Run-and-Tumble Particle in a Harmonic Potential*, arXiv:2602.08436 (first publicly submitted 2026-02-09), https://arxiv.org/abs/2602.08436.
3. R. Garcia-Millan and G. Pruessner, *Run-and-tumble motion: field theory and entropy production*, arXiv:2012.02900 (first publicly submitted 2020-12-04), https://arxiv.org/abs/2012.02900.
4. S. Angenent, *The zero set of a solution of a parabolic equation*, Journal für die reine und angewandte Mathematik 390 (1988), 79–96, https://doi.org/10.1515/crll.1988.390.79.
5. B. Lou, *The Zero Number Diminishing Property under General Boundary Conditions*, arXiv:1809.00309 (2018), https://arxiv.org/abs/1809.00309 (background on classical strict zero-number principle).
