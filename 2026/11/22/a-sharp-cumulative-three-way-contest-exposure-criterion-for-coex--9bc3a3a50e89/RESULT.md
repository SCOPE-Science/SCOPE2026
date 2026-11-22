# A sharp cumulative three-way contest exposure criterion for coexistence under proportional demographic heterogeneity

## Finding

For the well-mixed higher-order plant-competition flow specified below, with arbitrary positive and unequal species turnover rates but proportional birth and mortality rates, **total cumulative exposure** to three-way contests is the exact boundary between global convergence to coexistence and persistent nonzero displacement from coexistence. Let \(\alpha:[0,\infty)\to[0,1]\) be any measurable, externally prescribed three-way contest fraction, \(S(t)=\int_0^t\alpha(s)\,ds\), and \(x^*\) the unique strictly positive coexistence state. For every strictly positive initial state \(x(0)\ne x^*\),

\[
\lim_{t\to\infty}x(t)=x^*\quad\Longleftrightarrow\quad\int_0^\infty\alpha(t)\,dt=\infty.
\]

If that integral is finite, a positive relative-entropy gap survives forever. Irrespective of which regime holds, the long-time average fraction of competing offspring from species \(i\) is exactly \(y_i^*\), the fixed positive null vector of the pairwise competition matrix. In the three-species case, the pure-pairwise system's noncentral interior motions are periodic, and finite cumulative exposure drives every trajectory toward one such fixed positive-entropy periodic *level set* (without asserting asymptotic phase).

## Assumptions and scope

Let \(g\ge3\) be odd. Write \(\Delta_g=\{x\in[0,1]^g:\sum_i x_i=1\}\). Choose \(d_i>0\), a common proportionality constant \(\kappa>0\), and set \(f_i=\kappa d_i\). A pairwise dominance matrix \(H\) has \(H_{ii}=1/2\), \(H_{ij}+H_{ji}=1\), and \(0\le H_{ij}\le1\). Define \(A=H-\tfrac12\mathbf1\mathbf1^{\mathsf T}\), so \(A\) is skew-symmetric. Assume \(\ker A\) is one-dimensional, spanned by a strictly positive vector \(y^*\) with \(\sum_i y_i^*=1\). This condition holds, for example, for a three-species cyclic tournament with positive pairwise strengths. Define

\[
D(x)=\sum_i d_i x_i,\qquad y_i(x)=\frac{d_i x_i}{D(x)},\qquad h_i(x)=\sum_jH_{ij}y_j(x),
\]
\[
B_{ijk}=2H_{ij}H_{ik}+H_{ij}H_{jk}+H_{ik}H_{kj},\qquad L_i(x)=\sum_{j,k}B_{ijk}y_j(x)y_k(x).
\]

The nonautonomous model (the fixed-mixture mean-field model of [1], with its mixture replaced by an external measurable function of time) is

\[
\dot x_i=d_i x_i\bigl[(1-\alpha(t))(2h_i(x)-1)+\alpha(t)(L_i(x)-1)\bigr],\qquad i=1,\ldots,g.
\tag{1}
\]

For each strictly interior initial state there is a unique global positive Carathéodory solution. The stationary coexistence point shared by all mixtures is

\[
x_i^*=\frac{y_i^*/d_i}{\sum_j y_j^*/d_j},\qquad D^*=\sum_i d_i x_i^*=\left(\sum_i\frac{y_i^*}{d_i}\right)^{-1}.
\]

Set the relative entropy \(V(x)=\sum_i x_i^*\log(x_i^*/x_i)\) and the positive dissipation quadratic \(Q(x)=\sum_i y_i^*(h_i(x)-1/2)^2\).

## Proof

**Conservation and interior existence.** Because \(\sum_i y_i(2h_i)=2y^{\mathsf T}Hy=1\), and \(\sum_i y_iL_i=1\) (the normalized three-way winner probabilities from [1]), the right side of (1) sums to zero. It is locally Lipschitz in the population coordinates uniformly in \(\alpha\in[0,1]\). The factor \(x_i\) in each component preserves strict positivity over finite time and the compact simplex prevents finite-time explosion.

**Equilibrium and strict quadratic.** From \(Ay^*=0\), \(Hy^*=\tfrac12\mathbf1\) and \((y^*)^{\mathsf T}H=\tfrac12\mathbf1^{\mathsf T}\). Therefore both \(2h_i(x^*)=1\) and \(L_i(x^*)=1\) hold. Conversely, \(Q(x)=0\) forces \(Ay(x)=0\); the one-dimensional kernel and normalization imply \(y(x)=y^*\) and \(x=x^*\). The map \(x\mapsto y(x)\) is a diffeomorphism on the simplex interior.

**Exact entropy identity.** Direct differentiation, using \(d_i x_i^*=D^*y_i^*\), gives

\[
\dot V=-D^*\sum_i y_i^*\bigl[(1-\alpha)(2h_i-1)+\alpha(L_i-1)\bigr].
\]

The pairwise average vanishes, \(\sum_i y_i^*(2h_i-1)=0\). Write \(h_i=\sum_jH_{ij}y_j\), and use \(\sum_i y_i^*H_{ij}=1/2\), \(\sum_j y_jh_j=1/2\). Expanding the three terms in the tensor \(B\) yields

\[
\sum_i y_i^*L_i=2\sum_i y_i^*h_i^2+\frac12=1+2\sum_i y_i^*\left(h_i-\frac12\right)^2.
\]

Consequently, for almost every time,

\[
\boxed{\dot V(t)=-2D^*\alpha(t)Q(x(t)).}\tag{2}
\]

**Sharp exposure criterion.** The function \(V\) is continuous, nonnegative, strictly convex, and divergent at the boundary of the simplex. The trajectory stays in its compact interior sublevel \(K=\{x:V(x)\le V(x(0))\}\). On that set, \(Q\) is strictly positive off \(x^*\), and the ratio \(Q/V\) extends to bounded positive comparison constants near \(x^*\): both have positive-definite quadratic expansions on the tangent space, since \(A\) has trivial tangent kernel. Thus there are \(0<m_K\le M_K<\infty\) for which \(m_K V\le Q\le M_K V\) on \(K\). Integrating (2) gives the two-sided inequality

\[
V(0)e^{-2D^*M_KS(t)}\le V(t)\le V(0)e^{-2D^*m_KS(t)}.\tag{3}
\]

If \(S(\infty)=\infty\), the upper bound tends to zero, forcing \(x(t)\to x^*\). If \(S(\infty)<\infty\) and \(V(0)>0\), the lower bound gives \(V(\infty)>0\). This proves the if-and-only-if assertion for every noncentral initial state. Integrating (2) exactly also yields

\[
\int_0^\infty \alpha(t)Q(x(t))\,dt=\frac{V(0)-V(\infty)}{2D^*},\tag{4}
\]

with \(V(\infty)=0\) precisely in the infinite-exposure case for noncentral states.

**Long-time mean offspring composition.** Put \(R_i(x)=L_i(x)-1-2(Ay(x))_i\), a uniformly bounded function on the simplex. From (1),

\[
\frac{1}{d_i}\frac{d}{dt}\log x_i(t)=2(Ay(x(t)))_i+\alpha(t)R_i(x(t)).\tag{5}
\]

If \(S(\infty)<\infty\), the compact entropy sublevel bounds each \(\log x_i(t)\), and division of the integrated (5) by \(T\) gives \(A\,T^{-1}\int_0^T y(x(t))\,dt\to0\). Every limit point of these normalized time averages belongs to \(\ker A\), hence equals \(y^*\). If \(S(\infty)=\infty\), convergence of \(x(t)\) implies the same average immediately. Thus, in both cases,

\[
\lim_{T\to\infty}\frac1T\int_0^T\frac{d_i x_i(t)}{\sum_jd_jx_j(t)}\,dt=y_i^*\qquad(1\le i\le g).\tag{6}
\]

**Three-species periodic boundary.** When \(g=3\), the simplex interior is two-dimensional, and \(V\) is strictly convex with compact smooth simple closed positive levels. For \(\alpha\equiv0\), (2) makes the flow tangent to these levels; its vector field has no zeros away from \(x^*\), since \(Ay=0\) has only one normalized solution. Each positive level is therefore one periodic orbit. For finite total exposure, continuity and compactness imply \(\operatorname{dist}(x(t),\{x:V(x)=V(\infty)\})\to0\); the limiting level is exactly a periodic orbit of the pure-pairwise vector field.

## Verification

The standalone `checker.py` uses exact rational arithmetic to verify conservation, equilibrium, the expanded dissipation identity and strictness for 1,200 reproducible randomly generated positive three-species cases, including unequal demographic rates, four mixture fractions and differing pairwise strengths. Its current outcome was `PASS 1200 exact-rational drift, conservation, equilibrium and strictness tests`. This is an independent algebraic cross-check of the nonstandard identity, **not** a numerical proof of the all-time assertions; (3)–(6) follow from the analytical argument above. The code requires Python's standard library only: `python checker.py`.

For an explicit example take \(A_{12}=1/4\), \(A_{23}=1/3\), \(A_{31}=1/5\), \(d=(1,4,9)\), \(\kappa=2\). Then \(y^*=(20,12,15)/47\), \(x^*=(30/37,9/74,5/74)\). Both \(\alpha(t)=1/(1+t)\) and \(\alpha(t)=1/(1+t)^2\) tend to zero, but only the first has divergent total exposure and consequently forces global convergence. The second keeps a strictly positive entropy gap for every noncentral interior initial state.

## Relationship to prior work

Source [1] supplies the contest tensor and fixed-mixture mean-field dynamics and observes that proportional birth and mortality rates eliminate a destabilizing term in its Appendix B; it notes numerical stabilization for any fixed positive mixture. It does **not** establish the criterion for arbitrary measurable vanishing mixtures, the exact global exposure bounds, the all-schedule time-average identity, or the finite-exposure orbit-level conclusion. Source [2] treats higher-order stabilization and classical neutral competition in the earlier equal-rate framework. This finding neither reclaims those source models nor purports to introduce relative entropy as a new general method. The claim concerns a nonautonomous exact threshold in the source's particular three-seed contest tensor, with a specified exceptional class of heterogeneous rates.

## Limitations

The proportional rate condition \(f_i/d_i=\kappa\) is essential; the conclusion is **not** established for arbitrary independent birth and mortality heterogeneity. The theorem assumes an interior one-dimensional kernel of \(A\) and interior initial conditions. The mean-field model omits finite-population demographic noise, spatial correlations and adaptive contest fractions that depend on the state. When total exposure is finite, only approach to a closed periodic level is asserted, not convergence to a unique point or a selected asymptotic phase. The convergence comparison constants depend on the initial entropy sublevel. Literature inspection supports a bounded originality conclusion, not a guarantee of historical priority.

## References

1. Duran-Sala, M., Meloni, S., and Calleja-Solanas, V., "Species differences dilute the stabilizing effect of higher-order interactions in competitive communities," arXiv:2501.09172 (first public version 2025-01-15), Eq. (3), Appendix B.
2. Grilli, J., Barabás, G., Michalska-Smith, M. J., and Allesina, S., "Higher-order interactions stabilize dynamics in competitive network models," Nature 548 (2017), 210–213, supplemental methods; full OA: https://michalska-smith.com/pdfs/higherorder.pdf.
