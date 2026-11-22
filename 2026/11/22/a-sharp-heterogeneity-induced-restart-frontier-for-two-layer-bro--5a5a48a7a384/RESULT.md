# A sharp heterogeneity-induced restart frontier for two-layer Brownian escape

## Finding

Consider one-dimensional Fickian Brownian diffusion on the bounded interval \((-a,b)\), \(a,b>0\), killed at either endpoint, with constant diffusion coefficients \(D_->0\) on \((-a,0)\) and \(D_+>0\) on \((0,b)\). Start from the material interface at \(0\). Independently restart the position at \(0\) at Poisson rate \(r\geq0\). Write \(T_r\) for the resulting absorption time.

Put \(P=D_-^{-1}\), \(Q=D_+^{-1}\), \(H=aP+bQ\), \(z=a^2P/(b^2Q)\), and \(B=4+a/b+b/a\). Then, as \(r\downarrow0\),
\[
\mathbb E T_r=\frac{abPQ(a+b)}{2H}+c_1r+O(r^2),\qquad
c_1=\frac{abPQ}{24H^2}\bigl[ab(a^2+4ab+b^2)PQ-a^4P^2-b^4Q^2\bigr].
\]
Consequently weak resetting **strictly speeds absorption** (\(c_1<0\)) exactly for
\[
0<z<z_-\quad\text{or}\quad z>z_+,\qquad z_\pm=\frac{B\pm\sqrt{B^2-4}}2.
\]
It **strictly delays absorption** for \(z_-<z<z_+\). At either equality the derivative vanishes, so the general-length assertion is only a first-order classification; no second-order conclusion is claimed there.

In particular, for equal layer widths \(a=b=\ell>0\), \(z=D_+/D_-\) and \(B=6\). Hence weak restarting speeds escape exactly when
\[
\frac{D_+}{D_-}<3-2\sqrt2\quad\text{or}\quad\frac{D_+}{D_-}>3+2\sqrt2.
\]
At either *critical* contrast, let \(t_0=\ell^2/(D_-+D_+)\). Then
\[
\mathbb E T_r=t_0+\frac{2}{45}t_0^3r^2+O(r^3),
\]
so restarting strictly delays escape for all sufficiently small \(r>0\), even on the critical boundary. If \(w=D_+/D_-+D_-/D_+-6>0\) tends to zero from either accelerating side, there is exactly one local minimizing reset rate in a fixed sufficiently small neighborhood of zero, and its location and improvement obey
\[
r_{\mathrm{loc}}t_0=\frac{15}{32}w+O(w^2),\qquad
\frac{\mathbb E T_{r_{\mathrm{loc}}}}{t_0}=1-\frac5{512}w^2+O(w^3).
\]
This is a local statement, not a global optimality assertion.

## Assumptions and scope

The diffusion is the conservative transmission diffusion with generator \(\mathcal Lf=\partial_x(D(x)\partial_xf)\) in each open layer. Its backward domain requires continuity of \(f\) and of the flux \(D f'\) at \(0\); this matters because alternate interface conventions define different processes. Both endpoints are absorbing. Restarts redraw only the position, which returns to exactly the initial interface; independent exponential restart times have parameter \(r\). All geometric and diffusivity parameters are fixed and strictly positive. For \(r=0\) there is no restarting. Conclusions about sign of the small-\(r\) response refer to \(\mathbb E T_r-\mathbb E T_0\) for all sufficiently small positive \(r\).

## Proof

Let \(\tau=T_0\), and \(m_j(x)=\mathbb E_x\tau^j\) with \(m_0(x)=1\). Standard stopped-diffusion backward equations give, on both layers, \(D(x)m_j''(x)=-j m_{j-1}(x)\), with \(m_j(-a)=m_j(b)=0\), continuity of \(m_j\), and continuity of \(D m_j'\) at zero. These are polynomial boundary-value problems with unique solutions. For \(j=1\), their restrictions are
\[
m_1^-(x)=-Px^2/2+P(b^2Q-a^2P)x/(2H)+m_1(0),
\]
\[
m_1^+(x)=-Qx^2/2+Q(b^2Q-a^2P)x/(2H)+m_1(0).
\]
Substitution of the endpoints fixes \(m_1=m_1(0)\). Solving the same matching equations for \(j=2\), using these explicit quadratics as sources, yields
\[
m_1=\frac{abPQ(a+b)}{2H},\qquad
m_2=\frac{abPQ\bigl(a^4P^2+5a^3bPQ+8a^2b^2PQ+5ab^3PQ+b^4Q^2\bigr)}{12H^2}.
\]
These expressions can also be checked by differentiating the following independently derived Laplace transform of the unreset exit time, valid for every \(s>0\):
\[
\phi(s)=\mathbb E_0e^{-s\tau}=
\frac{\sqrt{D_-}\operatorname{csch}\bigl(a\sqrt{s/D_-}\bigr)+\sqrt{D_+}\operatorname{csch}\bigl(b\sqrt{s/D_+}\bigr)}{\sqrt{D_-}\operatorname{coth}\bigl(a\sqrt{s/D_-}\bigr)+\sqrt{D_+}\operatorname{coth}\bigl(b\sqrt{s/D_+}\bigr)}.
\]
Indeed \(\phi(s)\) is the interface value of the solution of \((D f')'=sf\) with \(f(-a)=f(b)=1\), obtained by matching both interface fluxes. Compactness and uniform ellipticity imply exit moments of all orders and analyticity of \(\phi\) near zero.

For independent Poisson restarts, the first successful excursion has probability \(\phi(r)\), and renewal conditioning gives the exact identity
\[
\mathbb E T_r=\frac{1-\phi(r)}{r\phi(r)}\quad(r>0).
\]
Expand \(\phi(r)=1-rm_1+r^2m_2/2-r^3m_3/6+O(r^4)\). Then
\[
\mathbb E T_r=m_1+\left(m_1^2-\frac{m_2}2\right)r+\left(m_1^3-m_1m_2+\frac{m_3}6\right)r^2+O(r^3).
\]
Replacing the first two moments by their explicit formulas gives \(c_1\). Its strictly positive prefactor leaves the sign of \(B-z-z^{-1}\). Since \(B\ge6>2\), the two reciprocal positive roots \(z_\pm\) are distinct and delimit the signs exactly, including the strict boundaries.

For \(a=b=\ell\), the third backward equation gives
\[
m_3=\frac{\ell^6PQ\bigl(3P^4+42P^3Q+398P^2Q^2+42PQ^3+3Q^4\bigr)}{120(P+Q)^3}.
\]
At either critical contrast \(P/Q+Q/P=6\), the first two moments satisfy \(m_2=2m_1^2\); simplifying the above expression gives \(m_3=(94/15)m_1^3\). Therefore the coefficient of \(r^2\) is \(m_1^3-m_1m_2+m_3/6=(2/45)t_0^3>0\).

Finally, put \(s=r t_0\) for equal widths and \(w=P/Q+Q/P-6\). The normalized mean has the analytic expansion, uniform near either critical contrast,
\[
\frac{\mathbb E T_r}{t_0}=1-\frac w{24}s+\left(\frac2{45}+O(w)\right)s^2+O(s^3).
\]
At \((w,s)=(0,0)\), the derivative with respect to \(s\) vanishes and its next derivative is \(4/45>0\). The analytic implicit-function theorem gives exactly one nearby critical point, a strict local minimum on the accelerating side \(w>0\). Solving the stationarity equation and substituting yields \(s=15w/32+O(w^2)\) and improvement \(5w^2/512+O(w^3)\).

## Verification

Execute \(\texttt{python checker.py}\) with Python, SymPy and mpmath installed. The supplied independent checker solves the first two moment transmission equations symbolically, checks the symmetric third moment and critical polynomial reduction, compares the moment values against high-precision derivatives of the independent hyperbolic Laplace transform on ten heterogeneous choices, and tests the weak-rate and two critical-boundary expansions. All 51 assertions/parameter cases passed in the reported execution. These tests support the exact algebra but are not a substitute for the all-parameter proof above.

## Relationship to prior work

General first-passage restart renewal identities and the small-rate coefficient-of-variation criterion are established prior theory (Ray, Mondal and Reuveni, 2018). Layered diffusion transmission and first-passage methods are also established (Carr, 2018; Bressloff, 2023). Lenzi and collaborators (2022), and Ray (2020), treat spatially varying diffusivity under stochastic resetting, principally power-law diffusivity and first passage to a single target, rather than the finite two-layer interface geometry with two absorbing ends. The present mathematical claim concerns the explicit sharp two-material contrast domain, its geometric dependence, and the positive critical curvature and local onset; the general renewal mechanism, hyperbolic matching, and universal restart criterion are not claimed as new.

## Limitations

The assertion for unequal layer widths is a weak-reset first-derivative classification, not a global characterization of optimal reset rates, and it leaves second order at the asymmetric equality cases undetermined. Critical curvature and local onset are established specifically for equal widths. No claims are made for semipermeable membranes, drift, partial absorption, mixed boundary conditions, or interface dynamics violating flux matching. This is a theoretical model-level classification, not a finite-sample or experimental feasibility result. A sufficiently general published exit-time moment theorem could imply these parameter formulas implicitly, so publication priority warrants independent literature review.

## References

- Lenzi, E. K. et al., *Transient anomalous diffusion in heterogeneous media with stochastic resetting* (first public preprint January 14, 2022), https://arxiv.org/abs/2201.05598.
- Bressloff, P. C., *Renewal equations for single-particle diffusion in multi-layered media* (2023), https://arxiv.org/abs/2301.02895.
- Carr, E. J., *Characteristic time scales for diffusion processes through layers and across interfaces* (2018), https://arxiv.org/abs/1801.08213.
- Ray, S., *Space-dependent diffusion with stochastic resetting: A first-passage study* (2020), https://arxiv.org/abs/2010.14237.
- Ray, S., Mondal, D. and Reuveni, S., *Péclet number governs transition to acceleratory restart in drift-diffusion* (2018), https://arxiv.org/abs/1811.08239.
