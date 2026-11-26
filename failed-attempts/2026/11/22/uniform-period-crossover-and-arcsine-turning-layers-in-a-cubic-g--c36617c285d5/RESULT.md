# Uniform period crossover and arcsine turning layers in a cubic global center

## Finding

**Theorem.** Fix \(\beta>0\). For every \(\alpha\ge0\), consider the cubic polynomial flow in its original time
\[
\dot x=y,\qquad \dot y=-x-\alpha x^3-\beta xy^2.
\]
For each turning amplitude \(A>0\), there is exactly one geometric nonstationary periodic orbit through \((A,0)\). Its least original-time period \(T_{\alpha,\beta}(A)\) is a strictly decreasing continuous bijection from \((0,\infty)\) onto \((0,2\pi)\).

More precisely, the **sharp uniform high-amplitude law** is
\[
\boxed{\lim_{A\to\infty}\ \sup_{\alpha\ge0}\left|\frac{A\sqrt\beta\sqrt{1+\alpha A^2}}{2\pi}\,T_{\alpha,\beta}(A)-1\right|=0.}
\]
It includes both fixed-parameter regimes \(T_{0,\beta}(A)\sim 2\pi/(A\sqrt\beta)\) and \(T_{\alpha,\beta}(A)\sim 2\pi/(A^2\sqrt{\alpha\beta})\) for each fixed \(\alpha>0\), together with the singular crossover \(\alpha=c/A^2\), \(c\ge0\), in which \(A\sqrt\beta\,T_{c/A^2,\beta}(A)\to2\pi/\sqrt{1+c}\).

There is also a **universal physical-time turning-layer law**. Sample a point on the orbit uniformly in original time over one least period. Put
\[
S_A=\beta(A^2-x^2),\qquad Z_A=e^{-S_A}.
\]
For any choice of \(\alpha=\alpha(A)\ge0\), the law of \(S_A\) converges in total variation, uniformly over all such coefficients, to the probability density
\[
\boxed{f(s)=\frac{\mathbf 1_{(0,\infty)}(s)}{\pi}\frac{e^{-s/2}}{\sqrt{1-e^{-s}}}.}
\]
Equivalently \(Z_A\) converges in total variation to the arcsine law with density \(\mathbf 1_{(0,1)}(z)/(\pi\sqrt{z(1-z)})\). In particular, under normalized physical-time sampling, \(|x|/A\to1\) in probability, with equal time mass near each signed turning point.

## Assumptions and scope

All variables and parameters are real; \(\beta>0\) is fixed while \(A\to\infty\), and \(\alpha\) may depend arbitrarily on \(A\) subject only to \(\alpha\ge0\). Period means the **least return time in the displayed differential equations**, without time reparametrization. Total variation uses \(\sup_B|\mu(B)-\nu(B)|=\tfrac12\int|f_\mu-f_\nu|\) when densities exist. The limiting law is not a pointwise trajectory statement, and the assertion of uniformity is only across \(\alpha\), not across \(\beta\) approaching zero.

## Proof

**1. A global periodic foliation.** Define
\[
g(x)=e^{\beta x^2/2},\qquad V(x)=\int_0^x s(1+\alpha s^2)e^{\beta s^2}\,ds,\qquad H(x,y)=\tfrac12g(x)^2y^2+V(x).
\]
Direct differentiation along the stated flow gives
\[
\dot H=e^{\beta x^2}y\bigl(\beta xy^2-x-\alpha x^3-\beta xy^2+x+\alpha x^3\bigr)=0.
\]
The potential \(V\) is even, \(V(0)=0\), strictly increasing in \(|x|\), and tends to \(+\infty\) at each end. Every positive level of \(H\) is a compact simple closed regular curve with no stationary point, and is one periodic orbit. Distinct positive amplitudes give distinct levels; every nonzero point belongs to one such level. The least period is
\[
T_{\alpha,\beta}(A)=4\int_0^A\frac{g(x)}{\sqrt{2(V(A)-V(x))}}\,dx.
\]

**2. Strict period monotonicity in the same physical time.** The odd coordinate \(q=\Phi(x)=\int_0^xg(s)\,ds\) is an increasing diffeomorphism of the line. The transformed equations in the *same* time are \(\ddot q+h(q)=0\), where \(h(\Phi(x))=g(x)x(1+\alpha x^2)\). Differentiating with respect to \(q\) gives
\[
h'(\Phi(x))=1+(\beta+3\alpha)x^2+\alpha\beta x^4.
\]
This is strictly increasing for \(x>0\), because \(\beta>0\). Therefore \(k(q)=h(q)/q=\int_0^1h'(\theta q)\,d\theta\) is strictly increasing for \(q>0\), and positive. Write \(R=\Phi(A)\). The turning-point quadrature is exactly
\[
T_{\alpha,\beta}(A)=4\int_0^1\left[2\int_u^1t\,k(Rt)\,dt\right]^{-1/2}du.
\]
For every \(u<1\) the inner integral strictly increases as \(R\) increases, so the whole period strictly decreases. Continuity follows from the finite regular quadratures. As \(A\downarrow0\), \(k(0)=1\) gives \(T\to2\pi\). The high-amplitude limit \(T\to0\) follows from Step 4, completing the bijection claim.

**3. Exact turning-layer quadrature and finite-amplitude distribution.** Fix \(A>0\) and abbreviate
\[
B=\beta A^2,\qquad m=1+\alpha A^2,\qquad c=\frac{\alpha}{\beta m}\in[0,1/B].
\]
Along a quarter orbit, make the exact substitution \(s=\beta(A^2-x^2)\), so \(0<s<B\). A single integration gives
\[
\begin{aligned}
V(A)-V(x)&=\frac{e^{\beta A^2}}{2\beta}J_A(s),\\
J_A(s)&=m(1-e^{-s})-\frac\alpha\beta\bigl[1-(1+s)e^{-s}\bigr]
=\int_0^s\left(m-\frac\alpha\beta u\right)e^{-u}du.
\end{aligned}
\]
The integrand in the last expression is strictly positive for \(u<B\). Thus the quarter-period is
\[
\frac{T_{\alpha,\beta}(A)}4
=\frac1{2A\sqrt{\beta m}}I_A,
\quad I_A=\int_0^B K_A(s)\,ds,
\quad K_A(s)=\frac{e^{-s/2}}{\sqrt{1-s/B}\sqrt{J_A(s)/m}}.
\]
Reflection and time reversal give four equal quarter arcs, each with the same distribution of \(s=\beta(A^2-x^2)\). Therefore the **exact** normalized original-time density of \(S_A\) is \(K_A(s)\mathbf1_{(0,B)}(s)/I_A\); the formula does not involve any random initialization beyond uniform phase sampling.

**4. Uniform dominated convergence.** Set \(K(s)=e^{-s/2}/\sqrt{1-e^{-s}}\), \(s>0\). For \(0<s\le B/2\), the bound \(c\le1/B\) gives
\[
\frac{J_A(s)}m=\int_0^s(1-cu)e^{-u}du\ge\frac12(1-e^{-s}),
\qquad K_A(s)\le2K(s).
\]
For \(B\ge2\) and \(B/2\le s<B\), the same integral, restricted to \(u\in[0,1]\), yields \(J_A(s)/m\ge(1-e^{-1})/2\). Consequently
\[
\int_{B/2}^{B}K_A(s)ds\le C\int_{B/2}^B\frac{e^{-s/2}}{\sqrt{1-s/B}}ds
\le C\sqrt2 B e^{-B/4}\longrightarrow0,
\]
with an absolute constant independent of \(\alpha\). On every fixed interval \([\eta,L]\subset(0,\infty)\), \(c\le1/B\) and the explicit formula for \(J_A/m\) show uniform convergence \(K_A\to K\) as \(B\to\infty\). The bound \(2K\) on the first half, its integrability near zero, and the just-established tail estimate imply
\[
\sup_{\alpha\ge0}\int_0^\infty\left|K_A(s)\mathbf1_{(0,B)}(s)-K(s)\right|ds\longrightarrow0.
\]
Finally, \(z=e^{-s}\) gives
\[
\int_0^\infty K(s)ds=\int_0^1\frac{dz}{\sqrt{z(1-z)}}=\pi.
\]
Thus \(I_A\to\pi\) uniformly in \(\alpha\ge0\). The exact formula \(T=2I_A/(A\sqrt{\beta m})\) yields the stated sharp period limit and its crossover cases. Dividing the \(L^1\) limit by \(I_A\) establishes total-variation convergence of the probability densities. Since the transformation \(s\mapsto e^{-s}\) is a measurable bijection between \((0,\infty)\) and \((0,1)\), it preserves total-variation distance and carries the limiting density to the stated arcsine density. As \(S_A\) is tight and \(|x|/A=\sqrt{1-S_A/B}\), the relative coordinate tends to one in probability. The exact half-turn symmetry divides physical-time mass equally between the two signs. This proves every assertion.

## Verification

The standalone `checker.py` (Python 3 standard library) tests the polynomial cancellation in the conserved energy, the exact transformed-force derivative, finite-amplitude strict period ordering, sharp period normalization across fixed and amplitude-dependent coefficients, and sample turning-layer CDFs. The script prints `CHECK_OK` on completion. The analytic proof is in Steps 1–4; finite numerical tests do not prove infinitely many amplitudes, parameter uniformity, or total-variation convergence.

## Relationship to prior work

Appis and Llibre [1], Theorem 4(c,d), classify this cubic subfamily as having a global center, with their coefficients \(a_4=-\alpha\), \(a_6=-\beta\) and the others zero. **That existence result is prior work, not a new finding here.** Chanda, Ghose-Choudhury and Guha [2] give the general Jacobi-multiplier and unit-mass transformation for velocity-squared Liénard equations; neither transformation is claimed as original here. The new statement is the combined **strict full-amplitude period map, uniform restoring-coefficient crossover, and explicit total-variation arcsine turning layer**.

A published high-energy result for \(\dot y=-x+(a-\kappa x)y^2\) [3] includes the \(\alpha=0\) axis of this family and proves an inverse-square-root-log-energy period and a two-peak square-wave limit; it does not assert the \(\alpha>0\) period law, the uniform \(\alpha A^2\) crossover or the microscopic arcsine layer. A separate published two-parameter *quintic* center result [4] gives strict period decrease and a different asymptotic boundary layer; its degree-five restoring and velocity terms are not the present cubic family. Another cubic center [5] has beta-distributed high-energy time layers but a distinct Kolmogorov vector field and logarithmic coordinate. General work on separable-Hamiltonian period criteria [6] is relevant methodologically, but no family-specific crossover or this total-variation distribution was found in the material inspected. No statement is made about priority against all unindexed publications.

## Limitations

The theorem is for \(\beta>0\), \(\alpha\ge0\), and no other cubic perturbation terms. No uniformity as \(\beta\downarrow0\), no explicit finite-amplitude special-function period, and no rate of total-variation convergence is claimed. The central \(\alpha=0\) *marginal* high-energy period behavior is covered in [3]; the new claim is a simultaneous full-family and uniform crossover theorem with a separate time-layer law. Broad Hamiltonian-period criteria and differently phrased prior literature could affect publication priority; the evidence inspected is not an exhaustive global uniqueness guarantee.

## References

1. R. F. Appis and J. Llibre, *Global centers of a family of cubic systems*, Aequationes Mathematicae 98 (2024), 1373–1389, DOI `10.1007/s00010-024-01051-7`, published 2024-04-05, full OA `https://link.springer.com/article/10.1007/s00010-024-01051-7`.
2. S. Chanda, A. Ghose-Choudhury and P. Guha, *Jacobi-Maupertuis metric of Liénard type equations and Jacobi last multiplier*, Electronic Journal of Differential Equations 2018, no. 120, `https://ejde.math.txstate.edu/Volumes/2018/120/chanda.pdf`.
3. *Universal logarithmic frequency and square-wave limit at a cubic global center*, published mathematical result, `https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-universal-logarithmic-frequency-and-square-wave-limit-at-a-cubic--5ef7d7af5678`.
4. *Strict period decrease and sharp large-amplitude laws for quintic global centers*, published mathematical result, `https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-strict-period-decrease-and-sharp-large-amplitude-laws-for-quinti--ffe383da977f`.
5. *Beta-layer concentration transition in asymmetric cubic global centers*, published mathematical result, `https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-beta-layer-concentration-transition-in-asymmetric-cubic-global-c--241e91583a30`.
6. J. Villadelprat and X. Zhang, *The period function of Hamiltonian systems with separable variables*, Journal of Dynamics and Differential Equations 32 (2020), 741–767, DOI `10.1007/s10884-019-09759-w`.
