# A sharp fragmentation law for periodic marsh-elevation viability in a quadratic accretion model

## Finding

Consider an idealized, nonnegative marsh-viability coordinate \(z\) governed by \(\dot z=p^2-z^2\) during a favorable sediment-accretion interval and \(\dot z=-q^2-z^2\) during an adverse relative-sea-level-rise interval. Let \(p,q,L,T>0\). In each repeating macrocycle, allocate total favorable duration \(L\) and adverse duration \(T\) into \(n\ge1\) identical consecutive favorable–adverse pairs, with subinterval lengths \(L/n\) and \(T/n\). A trajectory is removed when it reaches \(z=0\) during an adverse phase.

Define
\[
T_n(p,q,L)=\frac{n}{q}\arctan\!\left(\frac pq\tanh\frac{pL}{n}\right).
\]
There is a unique strictly positive periodic trajectory, attracting every positive initial state, **if and only if** \(0<T<T_n\). If \(T>T_n\), every finite positive initial condition reaches the loss boundary in finite time. At \(T=T_n\), positive initial data remain positive at finite times but their cycle minima tend to zero, and there is no uniformly positive periodic trajectory. The exact thresholds satisfy
\[
0<T_1<T_2<\cdots<\frac{p^2L}{q^2},\qquad
T_n=\frac{p^2L}{q^2}-\frac{p^4(p^2+q^2)L^3}{3q^4n^2}+O(n^{-4}).
\]
In particular, for any adverse duration strictly below \(p^2L/q^2\), sufficiently fine temporal fragmentation of the same total favorable/adverse exposure permits persistence. For every finite \(n\), a nonempty range \(T_n<T<p^2L/q^2\) has **positive time-averaged net forcing but finite-time loss**.

## Assumptions and scope

The state \(z\) is an idealized, dimensionally scaled elevation/viability margin; \(z=0\) is an *imposed* irreversible habitat-loss boundary. The coefficient \(-z^2\) represents a declining accretion advantage as relative elevation increases; seasonal forcing is piecewise constant. The model is not asserted to be the calibrated equation of any particular marsh. Positive \(p,q\), durations \(L,T>0\), integer \(n\ge1\), and initial \(0<z(0)<\infty\) are required. Alternating blocks are in the stated order, and the same pattern repeats indefinitely. The persistence definition requires a positive periodic orbit bounded away from the loss boundary. No instantaneous deposition jumps, memory, channel feedback, spatial flow or stochastic forcing are included.

## Proof

Set \(\ell=L/n\), \(b=T/n\), \(u=\tanh(p\ell)\). On a favorable block, exact separation of variables gives the strictly increasing Möbius map
\[
G(z)=\frac{p(z+pu)}{p+zu},\qquad z\ge0.
\]
On an adverse block, a state \(y>0\) solves \(z(t)=q\tan(\arctan(y/q)-qt)\) until reaching zero. It survives the entire adverse block exactly when \(qb<\arctan(y/q)\). When \(0<qb<\pi/2\), put \(v=\tan(qb)\), so the signed endpoint map (negative values mean the loss boundary was crossed earlier) is
\[
B(y)=\frac{y-qv}{1+yv/q}.
\]
Thus the stroboscopic map \(F=B\circ G\) has the form
\[
F(z)=\frac{Az+B_0}{Cz+D},\quad
A=p-qvu,\quad B_0=p(pu-qv),\quad C=u+pv/q,\quad D=p(1+puv/q).
\]
The positive denominator gives the exact fixed-point equation
\[
Cz^2+\alpha z-B_0=0,\qquad
\alpha=D-A=uv\frac{p^2+q^2}{q}>0,\quad C>0.
\]
The left side is strictly increasing on \(z\ge0\), hence a strictly positive fixed point exists uniquely if and only if \(B_0>0\), equivalently \(v<(p/q)u\). This is equivalent to \(T<T_n\) and automatically implies \(qb<\pi/2\). When it holds, \(F(0)>0\), \(F\) is strictly increasing, and \(F(z)-z\) has the sign of \(z_*-z\), where \(z_*>0\) is the fixed point. Every positive start therefore remains above zero and converges monotonically at the subcycle boundaries to \(z_*\); continuity of both phase flows gives convergence to the unique positive periodic trajectory. A convenient explicit expression is \(z_*=2B_0/(\alpha+\sqrt{\alpha^2+4CB_0})\).

When \(T=T_n\), the endpoint map has \(B_0=0\), and \(0<F(z)<z\) for every \(z>0\). Its iterates converge to the only nonnegative fixed point \(0\), never reaching zero at a finite subcycle, since \(G(z)>G(0)=qv\) whenever \(z>0\). The limiting boundary cycle touches zero exactly at the adverse endpoint. When \(T>T_n\) but \(qb<\pi/2\), the fixed-point quadratic is strictly positive on \(z\ge0\) because \(B_0<0\). Every sequence of surviving nonnegative endpoints strictly decreases; if it survived indefinitely, its limit would be a nonnegative fixed point, a contradiction. Thus a finite adverse block crosses zero. If \(qb\ge\pi/2\), every finite state crosses zero during that adverse block regardless of the preceding favorable block. This proves all three dynamical regimes.

For fragmentation, put \(c=p/q\) and \(f(x)=\arctan(c\tanh x)\). Since
\[
f'(x)=\frac{c(1-\tanh^2x)}{1+c^2\tanh^2x}
\]
is strictly positive and strictly decreasing on \(x>0\), \(f\) is strictly concave and \(f(0)=0\). Consequently \(n f(pL/n)\) is strictly increasing in \(n\): the chord slope \(f(x)/x\) is strictly decreasing in \(x\), and \(x=pL/n\) decreases with \(n\). Since \(f(x)<cx\), \(T_n<p^2L/q^2\). The small-argument expansions \(\tanh x=x-x^3/3+O(x^5)\) and \(\arctan y=y-y^3/3+O(y^5)\) yield
\[
f(x)=cx-\frac{c+c^3}{3}x^3+O(x^5),
\]
and hence the asserted \(n^{-2}\) coefficient and \(O(n^{-4})\) remainder. This also proves the strict average-forcing gap, because the macrocycle mean of the constant source term equals \((p^2L-q^2T)/(L+T)\).

## Verification

The standalone `checker.py` tests exact map identities at 65-digit precision, existence and uniqueness of positive fixed points, strict threshold ordering, mean-positive loss intervals, the inverse-square coefficient, and independently integrates each piecewise differential equation numerically with high tolerances. Execute `python checker.py` with Python 3, `mpmath` and `scipy`. The recorded replay completed 802 assertions without error. These finite diagnostics check formula implementation; the continuous and all-parameter assertions follow from the analytic proof above.

For \(p=q=L=1\), the critical total adverse durations are \(T_1=0.65088016802300755\ldots\) and \(T_2=0.86576948323965862\ldots\). At \(T=0.8\), mean source forcing is positive, but every positive starting state is eventually lost for one uninterrupted pair; the two-pair schedule has a unique positive periodic minimum \(z_*=0.0844745267942605\ldots\). These values can be regenerated by the checker.

## Relationship to prior work

Mudd, D'Alpaos and Morris (2010) detail sedimentation feedbacks, motivating a decreasing deposition advantage with elevation. D'Alpaos, Mudd and Carniello (2011) study dynamic marsh-elevation response to step changes in relative sea-level rise, sediment and productivity. Their inspected full-text analyses concern physical and analytical accretion response; neither states the exact square-wave quadratic viability threshold together with strict fragmentation ordering and its \(n^{-2}\) penalty. More general theory of periodic Riccati equations and periodically switched systems provides a mathematical background for existence, fixed-point and fast-switching arguments, but no inspected primary source established the joint closed-form threshold, all-\(n\) monotonicity and sharp finite-frequency correction for this prescribed positive-boundary model. This is a provisional originality assessment, not a proof of historical priority.

## Limitations

The quadratic feedback and imposed absorbing margin are stylized, not directly fitted to marsh data. Real marshes may have elevations outside the quadratic regime, sediment pulses, threshold-dependent plant productivity, irreversible regime shifts away from the designated boundary, nonstationary mean forcing, stochastic disturbances and spatial transport. Increasing \(n\) here does not add transition costs; if physical switching incurs a cost, infinitely rapid alternation need not be preferable. At equality the state survives each finite interval but loses any uniform positive safety margin, so calling equality persistent would change the statement. The general Riccati literature is broad; a historical formulation of the same monotonic comparison may exist beyond inspected text. No field prediction or independent validation is claimed.

## References

1. S. M. Mudd, A. D'Alpaos and J. T. Morris, “How does vegetation affect sedimentation on tidal marshes? Investigating particle capture and hydrodynamic controls on biologically mediated sedimentation,” *Journal of Geophysical Research: Earth Surface* 115 (2010), doi:10.1029/2009JF001566. First published 28 August 2010. https://doi.org/10.1029/2009JF001566
2. A. D'Alpaos, S. M. Mudd and L. Carniello, “Dynamic response of marshes to perturbations in suspended sediment concentrations and rates of relative sea level rise,” *Journal of Geophysical Research: Earth Surface* 116 (2011), doi:10.1029/2011JF002093. First published 12 November 2011. https://doi.org/10.1029/2011JF002093
3. M. A. Shayman, “On the Phase Portrait of the Matrix Riccati Equation Arising from the Periodic Control Problem,” *SIAM Journal on Control and Optimization* 23 (1985), 717–751, doi:10.1137/0323045. Relevant abstract accessible; full text not inspected. https://doi.org/10.1137/0323045
4. H. Ni, “The Existence and Stability of Two Periodic Solutions on a Class of Riccati’s Equation,” *Mathematical Problems in Engineering* (2018), 2805161, doi:10.1155/2018/2805161. https://doi.org/10.1155/2018/2805161
5. C. Gökçek, “Stability analysis of periodically switched linear systems using Floquet theory,” *Mathematical Problems in Engineering* (2004), 1–10, doi:10.1155/S1024123X04401069. https://doi.org/10.1155/S1024123X04401069
