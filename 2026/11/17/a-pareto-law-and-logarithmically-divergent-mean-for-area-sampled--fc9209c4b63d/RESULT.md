# A Pareto law and logarithmically divergent mean for area-sampled periods of a cubic global center

## Finding
For any \(\kappa>0\), consider the original-time polynomial flow
\[
\dot x=y(1+\kappa x^2),\qquad \dot y=-x(1+\kappa y^2).
\]
Put \(F(x,y)=x^2+y^2+\kappa x^2y^2\). For \(A>0\), write \(\Gamma_A=\{F=A^2\}\), \(T_\kappa(A)\) for its least **original-time** period, and \(S_\kappa(A)\) for the ordinary Euclidean area of \(\{F<A^2\}\). Define the complete elliptic integrals in their **parameter** convention by
\[
K(m)=\int_0^{\pi/2}(1-m\sin^2\theta)^{-1/2}\,d\theta,
\quad
E(m)=\int_0^{\pi/2}(1-m\sin^2\theta)^{1/2}\,d\theta.
\]
Then the following identities hold for every \(A>0\):
\[
T_\kappa(A)=4K(-\kappa A^2),\qquad
S_\kappa(A)=\frac4\kappa\big[(1+\kappa A^2)K(-\kappa A^2)-E(-\kappa A^2)\big],
\qquad S_\kappa'(A)=A T_\kappa(A).
\]
The period decreases strictly from \(2\pi\) to \(0\). For every \(R>0\), choose \((X_R,Y_R)\) according to **normalized planar Lebesgue area** on the canonical invariant sublevel \(\{F<R^2\}\), and let \(P_R=T_\kappa(\sqrt{F(X_R,Y_R)})\). Its entire finite-size distribution is determined exactly: for every \(T_\kappa(R)<t<2\pi\), if \(a_t\in(0,R)\) is the unique solution of \(T_\kappa(a_t)=t\), then
\[
\Pr(P_R>t)=\frac{S_\kappa(a_t)}{S_\kappa(R)},
\]
with survival probability \(1\) for \(t\le T_\kappa(R)\) and \(0\) for \(t\ge2\pi\).

Let \(B=\sqrt\kappa R\), assume \(B>1\), and normalize
\[
Z_R=\frac{B}{4\log B}P_R.
\]
As \(R\to\infty\) with \(\kappa>0\) fixed, \(Z_R\) converges in law to the standard Pareto distribution of shape one:
\[
\Pr(Z_R>z)\longrightarrow
\begin{cases}
1,&0<z\le1,\\
1/z,&z>1.
\end{cases}
\]
Its density is \(z^{-2}\) on \(z>1\). The corresponding **finite-size normalized mean** nevertheless diverges with the exact leading coefficient
\[
\boxed{\quad \mathbb E[Z_R]\sim\frac13\log(\sqrt\kappa R)\quad(R\to\infty).\quad}
\]
Thus ordinary area sampling sees a typical period of scale \(4\log B/B\), but its arithmetic mean is larger by a logarithmic factor.

## Assumptions and scope
Throughout \(\kappa>0\) is fixed. \(A,R>0\) denote the energy-amplitude coordinate \(A=\sqrt F\), **not** the Euclidean radius; the sublevel \(\{F<R^2\}\) is a natural invariant energy disk, not the Euclidean disk \(\{x^2+y^2<R^2\}\). The origin is a measure-zero equilibrium and is excluded from orbital period sampling. All orbit periods are least periods measured in the displayed vector field's original physical time. The spatial probability distribution is uniform in ordinary planar area over the whole energy sublevel; it is emphatically not uniform along any one periodic orbit in time. No uniformity in \(\kappa\) approaching zero is asserted.

## Proof
**1. Hamiltonian ovals and their least periods.** Direct differentiation gives
\[
\dot F=2x(1+\kappa y^2)y(1+\kappa x^2)-2y(1+\kappa x^2)x(1+\kappa y^2)=0.
\]
Indeed \(\dot x=\frac12\partial_yF\) and \(\dot y=-\frac12\partial_xF\). For every \(A>0\), the first-quadrant arc of \(\Gamma_A\) is the graph
\[
y=\sqrt{\frac{A^2-x^2}{1+\kappa x^2}},\qquad0\le x\le A.
\]
Its four reflected arcs form one regular Jordan oval. The vector field has zero divergence, since its two diagonal derivatives are \(2\kappa xy\) and \(-2\kappa xy\); hence planar area and normalized area in every invariant sublevel are flow-invariant. The gradient of \(F\) vanishes only at the origin and the flow is everywhere nonzero on the oval. Thus the orbit runs once around the oval and has a least positive period. On the first-quadrant arc,
\[
\dot x=\sqrt{(A^2-x^2)(1+\kappa x^2)}.
\]
The four arcs take equal times by coordinate reflection and quarter-turn symmetry, so substituting \(x=A\sin\theta\) gives
\[
T_\kappa(A)=4\int_0^A\frac{dx}{\sqrt{(A^2-x^2)(1+\kappa x^2)}}
=4\int_0^{\pi/2}\frac{d\theta}{\sqrt{1+\kappa A^2\sin^2\theta}}=4K(-\kappa A^2).
\]
Differentiation under the final integral proves strict decrease for every \(A>0\). Dominated convergence gives \(T_\kappa(0+)=2\pi\), and the integral tends to zero as \(A\to\infty\).

**2. Exact enclosed area and the action–period identity.** The area of the first quadrant of the sublevel is its vertical section integral, hence
\[
S_\kappa(A)=4\int_0^A\sqrt{\frac{A^2-x^2}{1+\kappa x^2}}\,dx
=4A^2\int_0^{\pi/2}\frac{\cos^2\theta}{\sqrt{1+\kappa A^2\sin^2\theta}}\,d\theta.
\]
The standard identity \(\int_0^{\pi/2}\sin^2\theta/\sqrt{1-m\sin^2\theta}\,d\theta=(K(m)-E(m))/m\) gives the stated exact \(K,E\) expression (interpreted continuously at \(m=0\)). Differentiation of the vertical-section integral in \(A\), with an integrable square-root endpoint, gives
\[
S_\kappa'(A)=4A\int_0^A\frac{dx}{\sqrt{(A^2-x^2)(1+\kappa x^2)}}=A T_\kappa(A).
\]
This identity also gives \(S_\kappa(A)=\int_0^A aT_\kappa(a)\,da\), since \(S_\kappa(0)=0\).

**3. Large-energy asymptotics.** For \(b\to\infty\), splitting the defining integral of \(K(-b^2)\) at fixed small angles and at an angle of order \(1/b\), or using the standard real-axis elliptic-integral asymptotic, yields
\[
K(-b^2)\sim\frac{\log b}{b}.
\]
For clarity about the coefficient: on \(1/b\ll\theta\ll1\), the integrand is asymptotic to \((b\theta)^{-1}\); that logarithmic window contributes \(b^{-1}\log b\), and the two complementary regions contribute lower-order terms after a two-cutoff squeeze. Consequently
\[
T_\kappa(A)\sim\frac{4\log(\sqrt\kappa A)}{\sqrt\kappa A}\quad(A\to\infty),
\qquad
S_\kappa(R)\sim\frac{4R}{\sqrt\kappa}\log(\sqrt\kappa R)\quad(R\to\infty).
\]
The second equivalent follows by integrating \(S_\kappa'(a)=aT_\kappa(a)\) and comparing \(\int^R\log a\,da\sim R\log R\). These asymptotics hold at fixed positive \(\kappa\); their additive lower-energy contributions are negligible.

**4. Exact finite-area ensemble and the Pareto limit.** Define \(A_R=\sqrt{F(X_R,Y_R)}\). By the very definition of area sampling, for each \(0\le a\le R\),
\[
\Pr(A_R\le a)=\frac{S_\kappa(a)}{S_\kappa(R)}.
\]
The strict monotonicity of \(T_\kappa\) immediately gives the exact finite-size survival law in the finding. Moreover the asymptotic for \(S\) implies, for each \(0<u\le1\),
\[
\Pr(A_R/R\le u)=\frac{S_\kappa(uR)}{S_\kappa(R)}\longrightarrow u.
\]
Thus \(A_R/R\) tends in law to a uniform variable \(U\) on \((0,1)\). For every fixed \(u>0\), the period asymptotic gives
\[
\frac{\sqrt\kappa R}{4\log(\sqrt\kappa R)}\,T_\kappa(uR)\longrightarrow\frac1u.
\]
The functions on the left are strictly decreasing in \(u\) and their convergence is uniform on each compact subinterval \([\delta,1]\), by elementary uniformity of the displayed asymptotic. The probability that \(A_R/R<\delta\) approaches \(\delta\). Letting \(\delta\downarrow0\) proves \(Z_R\Rightarrow1/U\); this has exactly the survival function and density stated above. Neither a fixed-sample approximation nor a numerical simulation is used in this limit argument.

**5. A sharp divergent mean.** Area differentiation gives the exact moment identity
\[
\mathbb E[P_R]=\frac1{S_\kappa(R)}\int_0^R T_\kappa(a)\,dS_\kappa(a)
=\frac1{S_\kappa(R)}\int_0^R aT_\kappa(a)^2\,da.
\]
This integral is finite for each finite \(R\), including near \(a=0\). Substituting the period asymptotic for large \(a\), and integrating the resulting logarithmic equivalent with positive integrand, yields
\[
\int_0^R aT_\kappa(a)^2\,da\sim
\frac{16}{3\kappa}[\log(\sqrt\kappa R)]^3.
\]
Combining with the area equivalent gives
\[
\mathbb E[P_R]\sim\frac4{3\sqrt\kappa R}[\log(\sqrt\kappa R)]^2,
\]
and multiplying by the definition of \(Z_R\) proves \(\mathbb E[Z_R]\sim\tfrac13\log(\sqrt\kappa R)\). This also explains why convergence in law to a Pareto distribution cannot be replaced by convergence of first moments: the limiting distribution has infinite mean.

## Verification
The standalone `CHECK.py` carries out exact symbolic conservation and Hamiltonian-gradient checks, numerical comparisons between the independent vertical-section and elliptic expressions for the area, numerical checks of the action–period derivative identity, and finite-parameter evaluations of the predicted limiting scalings. Run `python CHECK.py` with Python 3, `sympy`, and `mpmath`. Numerical tests corroborate the analytic calculation and do not certify the asymptotics or replace the proofs in Sections 3–5.

## Relationship to prior work
The vector field is exactly case (a), equation (11), of Llibre and Rondón [1] under \(\kappa=-c_1>0\). Its global-center property is prior work, not claimed as new. A previous study [2] of **the same** cubic flow already gives the complete-elliptic-integral period formula and large-amplitude asymptotics, and establishes sharp logarithmic phase and time-occupation laws **along a single orbit**. We expressly do **not** claim that exact period formula or its leading asymptotic as an original result. The contribution here is instead the **complete Euclidean-area sampled distribution across all orbits in a growing invariant sublevel**, the exact area formula linking that distribution to period, the shape-one Pareto ensemble limit, and its sharp divergent-mean coefficient. The separate elliptic-period and other-cubic-center results in [3] concern distinct Hamiltonians and do not imply this exact spatial-area law without identifying the present action and sampling geometry. The action–period identity itself is standard Hamiltonian geometry; it is used, not claimed as independently new.

## Limitations
This statement is specific to the displayed integrable cubic flow and the prescribed invariant-energy sublevels. It makes no claim about area sampling in Euclidean disks, parameter perturbations, all cubic centers, or uniformity as \(\kappa\to0\). Existing general Hamiltonian action and regular-variation theory explains the method; no broad universality theorem across Hamiltonians is asserted. The literature comparison supports novelty within inspected sources but cannot exclude an equivalent unindexed calculation. Independent verification is not claimed.

## References
[1] J. Llibre and G. Rondón, *Global centers of a class of cubic polynomial differential systems*, arXiv:2310.07454v1, first public 2023-10-11, Theorem 2(a), equation (11), https://arxiv.org/abs/2310.07454.

[2] *Sharp logarithmic phase and time statistics in a cubic global center* (2026), full publicly available result at https://github.com/published-finding corpus/2026/blob/main/2026/10/11/SCOPE-sharp-logarithmic-phase-and-time-statistics-in-a-cubic-global-ce--35ffbf168a22/RESULT.md. The original-time period formula and its elliptic asymptotic for the same vector field are already documented there.

[3] *Complete monotonicity of the period on four cubic Kolmogorov Hamiltonian centers* (2026), searchable mathematical result at https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-complete-monotonicity-of-the-period-on-four-cubic-kolmogorov-ham--4339a649dd41. This concerns a different cubic family.

[4] NIST Digital Library of Mathematical Functions, §19.12, *Asymptotic Approximations*, https://dlmf.nist.gov/19.12.
