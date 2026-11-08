# A unique transverse third-cumulant reversal under complete resetting of a trapped active Brownian swimmer

## Finding
For every rotational diffusivity \(d>0\) and every isotropic thermal-noise intensity \(h\geq0\), a harmonically trapped planar active Brownian swimmer, jointly reset in position and orientation at dimensionless Poisson rate \(r>0\), has a **unique** reset-rate threshold \(R(d,h)>0\) at which its stationary mixed third cumulant \(\operatorname{cum}(X,Y,Y)=\operatorname{Cov}(X,Y^2)\) changes sign. The cumulant is strictly negative for \(0<r<R(d,h)\), zero precisely at \(r=R(d,h)\), and strictly positive for \(r>R(d,h)\). Here \(X\) is the longitudinal coordinate along the prescribed reset direction, and \(Y\) is the perpendicular coordinate.

The threshold is the unique positive zero of the explicitly factored polynomial
\[
P_{d,h}(r)=2dQ_d(r)+h(r^2+2r-d)(4d+r)(9d+r)(d+r+1)(4d+r+1),
\]
where
\[
Q_d(r)=3r^4+(15d+9)r^3+(12d^2+20d+6)r^2-(58d^2+34d)r-(36d^3+147d^2+30d).
\]
Define \(R_0(d)\) as the unique positive zero of \(Q_d\). Then, with \(r_T(d)=\sqrt{1+d}-1\),
\[
0<r_T(d)<R(d,h)\leq R_0(d),
\]
where equality on the right occurs if and only if \(h=0\). At fixed \(d\), \(R(d,h)\) decreases strictly as \(h\) increases, and \(R(d,h)\to r_T(d)\) as \(h\to\infty\). In the athermal case the sharp limiting scales are
\[
R_0(d)\sim\sqrt{5d}\quad(d\downarrow0),\qquad R_0(d)\sim\sqrt{3d}\quad(d\to\infty).
\]

## Assumptions and scope
In dimensional variables, between reset events the process obeys
\[
\begin{aligned}
\mathrm dX_t&=(-\kappa X_t+v\cos\theta_t)\,\mathrm dt+\sqrt{2D_t}\,\mathrm dW^x_t,\\
\mathrm dY_t&=(-\kappa Y_t+v\sin\theta_t)\,\mathrm dt+\sqrt{2D_t}\,\mathrm dW^y_t,\\
\mathrm d\theta_t&=\sqrt{2D_r}\,\mathrm dB_t\pmod {2\pi},
\end{aligned}
\]
with independent standard Brownian motions \(W^x,W^y,B\), \(\kappa,v,D_r>0\), \(D_t\geq0\). At times of an independent Poisson clock of rate \(\lambda>0\), all three variables are reset to \((0,0,0)\). This regenerative process has a unique stationary law with moments of all orders.

For the formulas below rescale \(t\mapsto\kappa t\), \((X,Y)\mapsto(\kappa/v)(X,Y)\), and set \(d=D_r/\kappa\), \(r=\lambda/\kappa\), \(h=\kappa D_t/v^2\). The dimensionless stationary cumulant is \(C(d,r,h)=\mathbb E[XY^2]-\mathbb E[X]\mathbb E[Y^2]\); reflection in \(Y\) makes this equal to \(\operatorname{cum}(X,Y,Y)\). In physical coordinates multiply \(C\) by \((v/\kappa)^3\), which does not affect its sign.

## Proof
**Stationary renewal and moment recursion.** Because resets arrive at rate \(r>0\), the last-reset age is exponentially distributed and the stationary state is the corresponding mixture of evolutions starting at \((0,0,0)\). Harmonic confinement bounds the active contribution; the thermal contribution is conditionally Gaussian with bounded variance, so all polynomial moments exist. The normalized stationary generator is
\[
\mathcal L f=(-x+\cos\theta)\partial_x f+(-y+\sin\theta)\partial_y f+h(\partial_{xx}+\partial_{yy})f+d\partial_{\theta\theta}f+r[f(0,0,0)-f(x,y,\theta)].
\]
For integers \(p,q\geq0\), \(n\in\mathbb Z\), put \(F_{p,q,n}=\mathbb E[X^pY^q e^{in\theta}]\). Their zero-degree values are \(F_{0,0,0}=1\) and \(F_{0,0,n}=r/(r+dn^2)\) for \(n\ne0\). For \(p+q>0\), stationarity gives the triangular relation
\[
\begin{aligned}
(r+p+q+dn^2)F_{p,q,n}={}&\tfrac p2(F_{p-1,q,n+1}+F_{p-1,q,n-1})\\
&+\tfrac q{2i}(F_{p,q-1,n+1}-F_{p,q-1,n-1})\\
&+h\{p(p-1)F_{p-2,q,n}+q(q-1)F_{p,q-2,n}\},
\end{aligned}
\]
with negative indices interpreted as zero. The denominators are strictly positive and this recurrence determines each needed moment without any moment-closure assumption.

**Exact third mixed cumulant.** Recursion through total spatial degree three yields
\[
\begin{aligned}
m:=\mathbb E[X]&=\frac{r}{(d+r)(1+r)},\\
u:=\mathbb E[Y^2]&=\frac{4d}{(4d+r)(r+2)(d+r+1)}+\frac{2h}{r+2},\\
w:=\mathbb E[XY^2]&=\frac{4dr(9d+4r+3)}{(d+r)(9d+r)(r+1)(r+3)(d+r+2)(4d+r+1)}\\
&\quad+\frac{2rh(d+2r+3)}{(d+r)(r+1)(r+3)(d+r+2)}.
\end{aligned}
\]
Direct rational reduction of \(C=w-m\,u\) gives the exact factorization
\[
\boxed{C(d,r,h)=\frac{2rP_{d,h}(r)}{\mathcal D(d,r)}},
\]
where every factor of the denominator
\[
\mathcal D(d,r)=(d+r)(4d+r)(9d+r)(r+1)(r+2)(r+3)(d+r+1)(d+r+2)(4d+r+1)
\]
is strictly positive on the stated domain. Thus the sign of the cumulant is precisely the sign of \(P_{d,h}(r)\).

**Exactly one sign change.** In increasing powers of \(r\), the coefficients of \(P_{d,h}\) are
\[
\begin{aligned}
a_0&=-6d^2\{h(24d^3+30d^2+6d)+12d^2+49d+10\},\\
a_1&=d^2\{h(56d^2+223d+59)-116d-68\},\\
a_2&=d\{h(144d^3+539d^2+279d+25)+24d^2+40d+12\},\\
a_3&=h(232d^3+329d^2+73d+2)+30d^2+18d,\\
a_4&=h(105d^2+66d+5)+6d,\\
a_5&=2h(9d+2),\qquad a_6=h.
\end{aligned}
\]
Here \(a_0<0\), \(a_2,a_3,a_4>0\), and \(a_5,a_6\geq0\); \(a_1\) may have either sign. After removing zero coefficients, the coefficient sequence has **exactly one sign variation**, irrespective of the sign of \(a_1\). Descartes' rule permits at most one positive root counted with multiplicity. Since \(P_{d,h}(0)<0\) and its highest nonzero coefficient is positive, the intermediate value theorem supplies a positive root. Consequently that root is unique and simple and the signs on either side are as claimed. For \(h=0\), the same argument applies to \(Q_d\).

**Thermal ordering and endpoints.** Set \(t=\sqrt{1+d}-1>0\), so \(d=t(t+2)\). Polynomial substitution gives
\[
Q_{t(t+2)}(t)=-t(t+2)(24t^4+163t^3+384t^2+325t+30)<0.
\]
Hence \(t<R_0(d)\). At \(r=t\) the entire term multiplying \(h\) vanishes, so \(P_{d,h}(t)=2dQ_d(t)<0\). At \(r=R_0(d)\), its term multiplying \(h\) is nonnegative and strictly positive for \(h>0\). Therefore \(t<R(d,h)\leq R_0(d)\). If \(h_2>h_1\), evaluating \(P_{d,h_2}\) at \(R(d,h_1)>t\) makes it strictly positive; uniqueness and the negative-to-positive sign orientation force \(R(d,h_2)<R(d,h_1)\). Dividing the defining equation by \(h\) and using the uniform bounds shows the limit must be the only positive root of \(r^2+2r-d\), namely \(t\). Finally, in \(Q_d(R_0(d))=0\), the substitutions \(R_0=\sqrt d\,z\) in the small- and large-\(d\) limits give respectively leading equations \(6z^2-30=0\) and \(12z^2-36=0\). Uniqueness and uniform root bracketing imply the stated sharp asymptotics.

## Verification
The accompanying standalone \`verify.py\` constructs the generator separately in Cartesian monomials \(X^pY^qe^{in\theta}\), with rational real and imaginary arithmetic, and checks the three raw-moment formulas and the factored cumulant for 100 distinct exact-rational parameter triples. It also checks the polynomial coefficient identities and sign pattern, the boundary substitution identity, illustrative root ordering, and limiting scales. Run \`python3 verify.py\` with Python 3 and no external dependencies. The observed output reports 713 passed assertions, with \(R(1,0)\approx2.01118948367523\), \(R(1,1)\approx0.655238951413433\), and the thermal lower bound \(\sqrt2-1\approx0.414213562373095\). The infinite-domain claims are proved above; finite checks are corroboration rather than a substitute for proof.

## Relationship to prior work
Shee, *Active Brownian particle under stochastic position and orientation resetting in a harmonic trap* (first public 2024-09-11), treats this resetting protocol and derives mean, second, radial fourth moment, and radial kurtosis phase diagrams. Its general moment-generator method is pertinent, but the inspected main text and appendices do not state the mixed third-cumulant factorization, its unique reset-rate zero for every positive \(d\) and nonnegative \(h\), or the strict thermal threshold ordering proved here. Kumar, Sadekar, and Basu (2020) analyze the untrapped complete-reset model and the longitudinal marginal third moment, without the harmonic-trap transverse mixed-cumulant theorem. Chaudhuri and Dhar (2020) derive trapped active-particle moments without complete resetting; their recurrence methodology is related, but not the reset-dependent sign classification. The later anisotropic-reset paper of Ghosh and Mandal (2025) studies a different free-space model. Generic moment recurrences can imply pointwise moments without spelling out this global sign classification; implicit derivability and uncatalogued literature remain priority risks.

## Limitations
This theorem requires isotropic harmonic confinement, positive rotational diffusion, a positive constant Poisson joint-reset rate, and a fixed heading at reset. It does not assert the same behavior under orientation-only resetting, position-only resetting, non-Poisson resetting, anisotropic trapping, or rotational torque. The observable is the unstandardized mixed third cumulant, not radial excess kurtosis, a marginal third cumulant, or a globally optimal directional skewness. The positive and negative regimes refer to the correlation between longitudinal displacement and **squared transverse** displacement, not the sign of an ordinary covariance between the two coordinates. The proof is mathematical and not independent experimental validation; explicit global precedence over all published work is not asserted.

## References
1. A. Shee, *Active Brownian particle under stochastic position and orientation resetting in a harmonic trap*, arXiv:2409.06920, first submitted 2024-09-11. https://arxiv.org/abs/2409.06920
2. V. Kumar, O. Sadekar, and U. Basu, *Active Brownian Motion in two-dimensions under Stochastic Resetting*, arXiv:2008.03294, first submitted 2020-08-07. https://arxiv.org/abs/2008.03294
3. D. Chaudhuri and A. Dhar, *Active Brownian particle in harmonic trap: exact computation of moments, and re-entrant transition*, arXiv:2005.14234, first submitted 2020-05-28. https://arxiv.org/abs/2005.14234
4. A. Ghosh and S. Mandal, *Anisotropic active Brownian particle in two dimensions under stochastic resetting*, arXiv:2501.05149, first submitted 2025-01-09. https://arxiv.org/abs/2501.05149
