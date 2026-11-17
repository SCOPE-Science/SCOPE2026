# Two deadbeat gains and a singular stability frontier in alternating sampled feedback

## Finding

A scalar linear negative-feedback equation with a periodically sampled, generalized piecewise-constant argument can have **two distinct finite-time-extinction gains**, although the first sampling interval is entirely retarded. Its full gain-stability domain can be computed exactly. As the second sample approaches its right endpoint, the finite stability ceiling diverges with an explicit reciprocal law; at the endpoint, all finite positive gains are stable.

Let \(\alpha>0\), \(g>0\), \(0\le\theta\le1\), and consider
\[
\dot x(t)=-\alpha x(t)-g x(\gamma_\theta(t)),\qquad t\ge0,
\]
with initial value \(x(0)=x_0\in\mathbb R\). For every integer \(j\ge0\), define \(\gamma_\theta(t)=2j\) on \([2j,2j+1)\), and \(\gamma_\theta(t)=2j+1+\theta\) on \([2j+1,2j+2)\). At \(\theta=1\), the sample at \(2j+2\) is the continuous left-hand endpoint value. Thus the first step samples its left endpoint and the second step samples an adjustable point, with alternating period two.

Define
\[
r=e^{-\alpha},\quad q=e^{-\alpha\theta},\quad u=1-r,\quad v=1-q,\quad w=q-r,\quad c=g/\alpha.
\]
The one-step factors and the exact two-step multiplier are
\[
M_0(c)=r-uc,\quad M_\theta(c)=\frac{r-wc}{1+vc},\qquad
P_\theta(c)=\frac{(r-uc)(r-wc)}{1+vc}.
\]
They satisfy \(P_\theta(c)>-r>-1\) for every \(c\ge0\) and \(0\le\theta\le1\). For \(0\le\theta<1\), the equilibrium is globally exponentially attracting **if and only if** \(0<c<c_*(\theta)\), where
\[
c_*(\theta)=\frac{B+\sqrt{B^2+4uw(1-r^2)}}{2uw},\qquad B=r(u+w)+v.
\]
The threshold \(c_*(\theta)\) is strictly increasing in \(\theta\), from \((1+r)/(1-r)\) at \(\theta=0\) to infinity as \(\theta\uparrow1\). At the boundary \(c=c_*(\theta)\), the two-step multiplier is exactly \(+1\), so nonzero mesh states do not decay; above it they grow exponentially. At \(\theta=1\), every finite \(c\ge0\) is exponentially stable and \(P_1(c)\in(-r,r^2]\).

For every \(0<\theta<1\), there are precisely **two** positive deadbeat gains,
\[
c_1=\frac r{1-r},\qquad c_2(\theta)=\frac r{e^{-\alpha\theta}-e^{-\alpha}},\qquad
0<c_1<c_2(\theta)<c_*(\theta).
\]
At \(c_1\), every trajectory is identically zero from time \(1\) onward; at \(c_2\), every trajectory is identically zero from time \(2\) onward. When \(\theta=0\), these gains coincide; when \(\theta=1\), only \(c_1\) is finite. The stability ceiling has the sharp singular law
\[
\lim_{\theta\uparrow1}(1-\theta)\,g_*(\theta)=1+e^{\alpha},
\qquad g_*(\theta)=\alpha c_*(\theta).
\]

For a rationally checkable witness, choose \(\alpha=\log2\) and \(\theta=\log(4/3)/\log2\). Then \(r=1/2\), \(q=3/4\), and
\[
P_\theta(c)=\frac{(1-c)(2-c)}{2(4+c)}.
\]
The two exact extinction gains are \(c=1\) and \(c=2\), and the sharp stability threshold is \(c=6\). All claims refer to the explicitly stated linear nonimpulsive scalar equation.

## Assumptions and scope

The solution is continuous and piecewise continuously differentiable on the half-line, with the differential equation interpreted separately on each half-open unit cell. The case \(\theta=1\) uses the left endpoint limit for the advanced sample, so no jump or extra initial datum is introduced. The parameters \(\alpha>0\), \(g>0\), and \(\theta\in[0,1]\) are constant, and the sign of the sampled feedback is inhibitory. The stability criterion concerns exponential decay of every trajectory at physical time, not just the sampling instants.

## Proof

**One-cell propagation.** In a cell of length one starting at time \(k\), with sampled point \(k+\vartheta\) and incoming state \(y=x(k)\), solve the linear equation with constant sampled value \(z=x(k+\vartheta)\):
\[
x(k+s)=e^{-\alpha s}y-c(1-e^{-\alpha s})z,\quad 0\le s\le1.
\]
Putting \(s=\vartheta\) gives the uniquely soluble consistency relation
\[
z=\frac{e^{-\alpha\vartheta}}{1+c(1-e^{-\alpha\vartheta})}y.
\]
Its denominator is strictly positive. Evaluating at \(s=1\) proves \(M_\vartheta(c)=(r-c(e^{-\alpha\vartheta}-r))/(1+c(1-e^{-\alpha\vartheta}))\). Iterating with phases \(0,\theta\) gives \(x(2n)=P_\theta(c)^n x_0\) for every integer \(n\ge0\), without omitting any initial values.

**The strict lower Floquet bound.** Since \(0\le w\le u\) and \(1+vc>0\), direct completion of a square yields
\[
(1+vc)(P_\theta(c)+r)=uw(c-r/u)^2+r(1+r)-wr^2/u\ \ge r>0.
\]
Therefore \(P_\theta(c)>-r>-1\). This excludes every negative-unit-multiplier crossing, including at the endpoints of the parameter range.

**Complete sharp stability domain.** For \(\theta<1\), \(w>0\), and the sign of \(P_\theta(c)-1\) equals that of
\[
uwc^2-[r(u+w)+v]c+(r^2-1).
\]
This upward quadratic has negative constant and positive leading coefficient, hence exactly one positive root, equal to the stated \(c_*(\theta)\). Combining this with the strict lower Floquet bound proves \(|P_\theta(c)|<1\) precisely below the root, equals one precisely at the root, and exceeds one above it. For fixed finite gain, all between-mesh solutions have bounded one-cell linear propagation factors, so the same exponential convergence or instability holds in physical time. If \(\theta=1\), \(w=0\), and \(P_1(c)=r(r-uc)/(1+uc)\) decreases from \(r^2\) toward \(-r\) without reaching it, proving stability at every finite gain.

**Monotone stability budget.** For fixed \(c>0\), the expression \(M_\theta(c)=(r(1+c)-cq)/(1+c-cq)\) has derivative \(\partial_q M_\theta(c)=c(r-1)(1+c)/(1+c-cq)^2<0\). Because \(q=e^{-\alpha\theta}\) strictly decreases with \(\theta\), the factor \(M_\theta(c)\) strictly increases with \(\theta\). For every \(c>r/u\), the other factor \(M_0(c)<0\), so the product \(P_\theta(c)\) strictly decreases as \(\theta\) increases. Each threshold satisfies \(c_*(\theta)>r/u\); at a threshold for one phase, larger phases make the product strictly less than one while it remains above negative one. Hence the unique positive stability threshold is strictly increasing in \(\theta\). Its initial value is \(c_*(0)=(1+r)/u\) by the retarded-square formula.

**Two deadbeat gains.** The denominator of \(P_\theta(c)\) is positive. Its zeros are exactly the zeros of its two independent numerator factors. For \(0<\theta<1\), \(0<w<u\), so they are distinct, positive, and ordered as stated. A vanishing first factor makes the state zero after the first cell; a vanishing second factor makes it zero after the second. Both are strictly below the positive stability boundary because \(P=0<1\) there. At \(\theta=0\), \(w=u\), and the roots coincide; at \(\theta=1\), \(w=0\), and the second root disappears to infinity.

**Sharp endpoint scaling.** As \(\theta\uparrow1\), \(w=q-r\sim\alpha r(1-\theta)\), \(v\to u\), and \(B\to u(1+r)\). The quadratic positive-root formula gives \(w c_*(\theta)\to1+r\). Thus \((1-\theta)\alpha c_*(\theta)\to(1+r)/r=1+e^{\alpha}\). The rational witness follows by direct substitution, and the stability boundary is the positive root of \(c^2-5c-6=0\). This completes the proof.

## Verification

Run the standalone Python 3 program `verify.py` with no external dependencies. It checks 1,250 independently seeded combinations of decay, sampling phase, gain, and initial values; verifies cell solutions and differential residuals, exact one-cell factors and the Floquet inequality, stability threshold signs, endpoint and deadbeat cases, an exact-rational witness, and the singular scaling. The logical conclusions for every admissible parameter follow from the analytic inequalities above, not from finite sampling. The checker's floating-point threshold tests use tolerances and are not an interval-arithmetic certificate.

## Relationship to prior work

Torres Naranjo and Castillo Apolonio (2026) study periodic Hopfield-type equations with generalized piecewise-constant arguments and give sufficient Green-function and Lipschitz criteria for exponential attraction. They include both interior advanced samples and the nonimpulsive case, but the inspected results do not specify this two-phase exact spectral/stability classification, the two distinct extinction gains, or the singular gain ceiling.

The classical endpoint-alternating model appears explicitly in Song and Liu (2012), which studies its analytic and Runge–Kutta stability region. **The \(\theta=1\) limit by itself is not claimed as new.** The contribution here is the complete interior-phase interpolation \(0<\theta<1\), the two distinct exact deadbeat gains, the strict lower Floquet inequality throughout the phase–gain plane, and the precise singular approach to that previously studied endpoint. Existing single-phase gain thresholds address a different (nonalternating) return map and do not, by themselves, give this period-two phase diagram.

## Limitations

The exact conclusions assume a scalar linear inhibitory equation, unit-length cells, constant coefficients, a retarded first cell, and an adjustable second-cell sample. They do not imply the same all-gain behavior for nonlinear activation, arbitrary periodic sampling sequences, impulses, or coupled multidimensional networks. Exponential rates are not uniform in the gain over the entire positive half-line. The older literature on advanced–retarded hybrid equations is extensive; absence of an equivalent interior-phase formula from the inspected sources is not an absolute priority guarantee.

## References

1. R. Torres Naranjo and S. Castillo Apolonio, *Periodic Solutions and Exponential Attractivity in Hopfield-Type Neural Networks with Generalized Piecewise Constant Arguments: Impulsive and Nonimpulsive Cases*, arXiv:2610.36560v1, first publicly submitted 2026-10-27. https://arxiv.org/abs/2610.36560
2. M. Song and M. Liu, *Numerical stability and oscillation of the Runge-Kutta methods for the differential equations with piecewise continuous arguments alternately of retarded and advanced type*, Journal of Inequalities and Applications 2012, 290, DOI:10.1186/1029-242X-2012-290. https://link.springer.com/article/10.1186/1029-242X-2012-290
3. K.-S. Chiu and M. Pinto, *Periodic solutions of differential equations with a general piecewise constant argument and applications*, Electronic Journal of Qualitative Theory of Differential Equations 2010, 46, 1–19. https://acta.bibl.u-szeged.hu/42269/
