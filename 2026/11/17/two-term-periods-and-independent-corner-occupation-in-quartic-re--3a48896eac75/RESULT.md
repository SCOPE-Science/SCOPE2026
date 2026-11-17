# Two-term periods and independent corner occupation in quartic replicator centers

## Finding
Consider the continuous-time two-strategy, two-population system
\[
\dot x=x(1-x)F(y),\qquad \dot y=-y(1-y)G(x),\qquad (x,y)\in(0,1)^2,
\]
where \(F(u)=f_0+f_1u+f_2u^2\) and \(G(u)=g_0+g_1u+g_2u^2\). Assume
\[
F(0)<0<F(1),\quad G(0)<0<G(1),\quad F'(u)>0,\ G'(u)>0\quad(0\le u\le1).
\]
Every nonstationary interior orbit is periodic. Set the positive endpoint slopes
\[
a_-=-G(0),\quad a_+=G(1),\qquad b_-=-F(0),\quad b_+=F(1),
\]
and \(A=a_-^{-1}+a_+^{-1}\), \(C=b_-^{-1}+b_+^{-1}\). Introduce logit coordinates \(p=\log(x/(1-x))\), \(q=\log(y/(1-y))\) and the canonically normalized conserved energy
\[
H(p,q)=V(p)+W(q),\qquad V(p)=\int_0^pG(\sigma(s))\,ds,\quad W(q)=\int_0^q F(\sigma(s))\,ds,
\qquad \sigma(s)=\frac1{1+e^{-s}}.
\]
Let \(T(E)\) be the minimal **original-physical-time** period of the orbit with energy \(E>\min H\). Define the explicit constants
\[
\begin{aligned}
\beta^V_-&=-(g_1+g_2)\log 2+g_2/2,&\beta^V_+&=-(g_1+g_2)\log 2-g_2/2,\\
\beta^W_-&=-(f_1+f_2)\log 2+f_2/2,&\beta^W_+&=-(f_1+f_2)\log 2-f_2/2,\\
B&=\beta^V_-/a_-+\beta^V_+/a_+,&D&=\beta^W_-/b_-+\beta^W_+/b_+.
\end{aligned}
\]
Then the exact **two-term high-energy period law** is
\[
\boxed{T(E)=AC\,E-BC-AD+o(1)\qquad(E\to\infty).}
\]
Furthermore, sample physical time uniformly along one complete energy-\(E\) orbit, producing a random point \((X_E,Y_E)\in(0,1)^2\). Its weak limiting law on the closed square is a product of Bernoulli distributions supported on the four pure-strategy corners:
\[
\boxed{\mathcal L(X_E,Y_E)\ \Longrightarrow\ 
\sum_{i,j\in\{0,1\}}\frac{a_i^{-1}b_j^{-1}}{AC}\,\delta_{(i,j)}.}
\]
Here \(a_0=a_-\), \(a_1=a_+\), \(b_0=b_-\), \(b_1=b_+\). Equivalently, for every fixed \(0<r<1/2\) and each corner \((i,j)\), the probability of Euclidean distance less than \(r\) from that corner tends to \(a_i^{-1}b_j^{-1}/(AC)\). In particular, the limiting corner coordinates are independent, with \(\Pr(X_\infty=1)=a_-/(a_-+a_+)\) and \(\Pr(Y_\infty=1)=b_-/(b_-+b_+)\). The leading period and all four occupation weights depend only on endpoint payoffs, while the period intercept also records the quadratic payoff coefficients.

## Assumptions and scope
All six real payoff coefficients are fixed and satisfy the four displayed strict inequalities. No assumption of symmetry, equal payoff endpoints, or vanishing quadratic coefficients is made. Genuine quartic examples have \(f_2\ne0\) or \(g_2\ne0\). The energy is **not** shifted by its minimum: \(V(0)=W(0)=0\) fixes the additive normalization needed for the constant term. Weak convergence means convergence of integrals against every continuous function on the closed unit square; it is not convergence in total variation. The assertions concern original time in the displayed population equations, not a rescaled Hamiltonian time.

The vector field belongs, after the affine change of square coordinates, to the two-player invariant-square quartic polynomial family studied by Gasull, Gouveia and Santana (2024), and specifically its separable quadratic-payoff subfamily. Its integrability and absence of isolated limit cycles are known; neither is claimed as original here.

## Proof
**1. Canonical coordinates and periodicity.** The logit change gives exactly
\[
\dot p=F(\sigma(q))=\partial_q H,\qquad \dot q=-G(\sigma(p))=-\partial_p H.
\]
Since \(V''(p)=G'(\sigma(p))\sigma(p)(1-\sigma(p))>0\), and similarly \(W''>0\), both potentials are strictly convex. At negative and positive infinity their derivatives tend respectively to \(-a_-\), \(a_+\) and \(-b_-\), \(b_+\). Thus \(V,W\) are proper, have unique minimizers \(p_*\), \(q_*\), and every regular level above \(\min H=V(p_*)+W(q_*)\) is a compact simple oval without stationary points. The flow is Hamiltonian in original time, so each oval is periodic, with one minimal traversal per period.

**2. Endpoint constants and branch widths.** Direct integration gives the identity, valid for every real \(p\),
\[
V(p)=g_0p+(g_1+g_2)\bigl[\log(1+e^p)-\log2\bigr]
-g_2\bigl[\sigma(p)-\tfrac12\bigr].
\]
Replacing \(g\) by \(f\) gives the analogous identity for \(W\). Consequently
\[
V(p)=\begin{cases}a_-|p|+\beta^V_-+O(e^p),&p\to-\infty,\\ a_+p+\beta^V_++O(e^{-p}),&p\to+\infty,\end{cases}
\]
with analogous expressions for \(W\). Write \(m_V=V(p_*)\), \(m_W=W(q_*)\). For \(s>m_V\), denote the two inverse branches of \(V(p)=s\) by \(p_-(s)<p_*<p_+(s)\), and define the level width \(U_V(s)=p_+(s)-p_-(s)\). Then
\[
U_V(s)=A s-B+o(1),\qquad U'_V(s)=A+\delta_V(s),
\]
where \(\delta_V(s)=1/V'(p_+(s))+1/|V'(p_-(s))|-A\) is nonnegative, decreasing, integrable on \((m_V,\infty)\), and has only an integrable inverse-square-root singularity at \(m_V\). At infinity it decays exponentially, because the slopes approach their finite positive endpoint limits exponentially in the logit coordinates. Integration and \(U_V(m_V)=0\) give
\[
\int_{m_V}^{\infty}\delta_V(s)\,ds=A m_V-B.
\]
Likewise \(U_W(s)=Cs-D+o(1)\), \(U'_W=C+\delta_W(s)\), \(\int_{m_W}^\infty\delta_W=Cm_W-D\). The monotonicity follows from strict convexity: moving either inverse branch outward increases the absolute derivative, so each reciprocal derivative decreases.

**3. Exact physical period and its intercept.** Canonical Hamiltonian speed equals \(|\nabla H|\), hence the coarea identity identifies the period with the energy derivative of enclosed \((p,q)\)-area. Integrating slices gives the exact width-convolution representation
\[
T(E)=\int_{m_V}^{E-m_W}U'_V(s)U'_W(E-s)\,ds.
\]
Expanding both factors yields
\[
\begin{aligned}
T(E)={}&AC(E-m_V-m_W)
+C\int_{m_V}^{E-m_W}\delta_V(s)\,ds
+A\int_{m_W}^{E-m_V}\delta_W(v)\,dv\\
&+\int_{m_V}^{E-m_W}\delta_V(s)\delta_W(E-s)\,ds.
\end{aligned}
\]
Each single-defect integral converges to the value derived in step 2. The final convolution tends to zero. Indeed, after translating the lower endpoints to zero, both defects are nonnegative, decreasing and integrable; splitting the convolution at half its argument bounds it by
\[
\delta_V(m_V+R/2)\|\delta_W\|_1+\delta_W(m_W+R/2)\|\delta_V\|_1\longrightarrow0,
\]
where \(R=E-m_V-m_W\). Collecting terms cancels the minimum-energy shifts and gives \(T(E)=AC E-BC-AD+o(1)\).

**4. Four independent corner occupations.** Decompose each energy oval into four arcs according to whether \(p\) lies on the lower or upper inverse branch of \(V\) and whether \(q\) lies on the lower or upper inverse branch of \(W\). Hamilton's equations give for the traversal time of the arc indexed by \(i,j\in\{0,1\}\):
\[
\tau_{ij}(E)=\int_{m_V}^{E-m_W} d_{V,i}(s)d_{W,j}(E-s)\,ds,
\]
where \(d_{V,0}=|p_-'|\), \(d_{V,1}=p_+'\), and similarly for \(W\). Each reciprocal derivative differs from its asymptotic limit \(1/a_i\) or \(1/b_j\) by an integrable nonnegative defect. The preceding convolution calculation therefore gives
\[
\tau_{ij}(E)=\frac{E}{a_i b_j}+O(1).
\]
For any fixed bound \(L\), the time along an arc with \(|p|\le L\) is uniformly \(O_L(1)\) as \(E\to\infty\): the corresponding potential level \(V(p)\) stays in a fixed compact interval and its inverse derivative has an integrable singularity, while the other inverse derivative is uniformly bounded at the complementary large energy. The same holds for \(|q|\le L\). Away from these bounded-coordinate strips, \(x=\sigma(p)\) is uniformly near \(0\) or \(1\) according to the branch, and likewise for \(y\). Dividing arc durations by \(T(E)\sim AC E\), first sending \(E\to\infty\) and then \(L\to\infty\), proves weak convergence to the four atoms of weights \(a_i^{-1}b_j^{-1}/AC\). These weights factor into their two marginals, proving independence.

## Verification
A self-contained Python checker, `scripts/check_replicator_corner_law.py`, validates the canonical-coordinate derivative and first-integral identities symbolically, then integrates a genuinely quartic asymmetric example at energies \(10\), \(25\), and \(50\) using event-detected physical periods. The payoffs are \(F(y)=-1+3.5y-0.5y^2\), \(G(x)=-2+5.2x-0.2x^2\). Its predicted period is
\[
T(E)=1.25E+7.060638472266\ldots+o(1),
\]
and the predicted corner weights, ordered \((0,0),(0,1),(1,0),(1,1)\), are \(0.4,0.2,4/15,2/15\). The observed absolute period discrepancies are about \(4.28\times10^{-3}\) at \(E=10\), \(4.41\times10^{-6}\) at \(E=25\), and \(3.7\times10^{-9}\) at \(E=50\), with physical-time occupancy close to those four weights. These finite experiments are checks, not proofs of the infinite-energy assertions. Reproduce with `python scripts/check_replicator_corner_law.py` after installing `requirements.txt`.

## Relationship to prior work
Gasull, Gouveia and Santana (2024), specifically their Proposition 2, explain the integrability and center structure of separable polynomial vector fields, but their treatment concerns the number and configuration of centers and limit cycles rather than an explicit high-energy original-time period intercept or corner occupation measures. A published calculation for a distinct invariant-square quartic family with own-coordinate multiplicative factors establishes a two-term period law; that earlier statement does **not** cover the present genuinely quadratic cross-payoff family and does not state its independent Bernoulli corner law. Another published result gives the exact area-sampled period distribution for a symmetric cubic replicator center, a different probability experiment from uniform physical time on a fixed high-energy oval. The extensive general literature on separable Hamiltonian period functions contains related techniques, and may contain an equivalent broad theorem not located here. Therefore no priority claim is made beyond the stated comparison scope.

## Limitations
This is an exact deterministic interior-flow theorem for increasing quadratic payoff functions with strict opposite endpoint signs. No claims are made about boundary initial conditions, perturbed non-Hamiltonian dynamics, discrete-time replicator maps, higher-strategy games, or noisy data. The limit measure is singular and convergence is weak, not in total variation. The period intercept depends on the specific energy normalization \(V(0)=W(0)=0\). The general separable-Hamiltonian treatment of Villadelprat and Zhang (2020) was accessible only through its abstract and metadata, so possible implicit coverage in uninspected full text remains a scientific priority risk. No independent mathematical audit has been performed.

## References
1. A. Gasull, L. F. S. Gouveia and P. Santana, *On the limit cycles of a quartic model for evolutionary stable strategies*, arXiv:2410.15354v1, first posted October 20, 2024, https://arxiv.org/html/2410.15354v1.
2. J. Villadelprat and X. Zhang, *The Period Function of Hamiltonian Systems with Separable Variables*, Journal of Dynamics and Differential Equations **32** (2020), 741–767, https://doi.org/10.1007/s10884-019-09759-w.
3. *Universal two-term period growth in an invariant-square quartic center*, published mathematical record (October 11, 2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-universal-two-term-period-growth-in-an-invariant-square-quartic--73607523fe89.
4. *Exact area-sampled period distribution and a sharp exponential tail in a two-population replicator center*, published mathematical record (November 8, 2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-exact-area-sampled-period-distribution-and-a-sharp-exponential-t--6f2405690e4d.
