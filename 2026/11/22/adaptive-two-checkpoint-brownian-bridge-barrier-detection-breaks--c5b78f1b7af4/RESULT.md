# Adaptive two-checkpoint Brownian-bridge barrier detection breaks midpoint symmetry

## Finding
Consider a Brownian bridge with equal strictly positive endpoints, observed exactly twice at interior locations. The second location may be chosen after seeing the first observation; an alarm is raised if either observed value is nonpositive. The first observation at the midpoint is *never* optimal for maximizing the probability of an alarm: for every positive normalized endpoint clearance it is a strict cusp-shaped local minimum of the best achievable two-observation detection probability. There are at least two global optimal first locations, symmetric and strictly off center.

More precisely, let \(B_t=c+W_t-tW_1\), \(0\le t\le1\), where \(W\) is standard Brownian motion and \(c>0\). Let \(J_c(s)\) be the largest probability that either of two interior observations is \(\le0\), with first time \(s\in(0,1)\) fixed and the second time a measurable function of the first observed value. Then
\[
J_c'(1/2+)=\frac{\Gamma(3/4)}{2^{1/4}\pi}\sqrt c\,e^{-2c^2}>0,
\qquad J_c'(1/2-)=-J_c'(1/2+).
\]
The conditional second-query policy, the exact integral for \(J_c\), and a constructive off-center improvement appear below. For an arbitrary horizon \(T>0\), diffusion amplitude \(\sigma>0\), and equal endpoint height \(a>0\), put \(c=a/(\sigma\sqrt T)\) and \(s=t/T\); the same theorem applies.

## Assumptions and scope
A normalized bridge has \(B_0=B_1=c>0\), continuous sample paths and covariance \(\operatorname{Cov}(B_s,B_t)=\min(s,t)-st\). Sampling is retrospective/offline: after the first observed value, the second sample may be drawn anywhere in \((0,1)\), including at an earlier time, using the usual conditional Brownian-bridge distribution. There are no observation errors, the barrier is zero, and an alarm means at least one *sampled* value is nonpositive. An alarm cannot be a false positive for the event \(\min_{0\le t\le1}B_t\le0\), but a genuine crossing may remain undetected. The objective is alarm probability, equivalently the probability of detecting a crossing. It is not the expected error in the numerical value of the minimum or the accuracy of an exit time.

For \(s\in(0,1)\), write \(Y=B_s\), \(v_s=s(1-s)\), \(L_s=\max\{s,1-s\}\); denote the standard Gaussian CDF and density by \(\Phi\) and \(\phi\).

## Proof
**Step 1 (the exact one-checkpoint lemma).** On an interval of length \(L>0\), a Brownian bridge between strictly positive endpoints \(u,v\) has, at fractional time \(r\in(0,1)\), Gaussian mean \(u+(v-u)r\) and variance \(Lr(1-r)\). Its chance of a nonpositive checkpoint is
\[
\Phi\!\left(-\frac{u+(v-u)r}{\sqrt{Lr(1-r)}}\right).
\]
Because \(\Phi\) is strictly increasing, maximize the chance by minimizing the positive standardized mean. Differentiation of its square gives the unique stationary point \(r=u/(u+v)\), which is the strict global minimum because the ratio diverges at both endpoints. At this point the detection probability is exactly \(\Phi(-2\sqrt{uv/L})\). No reflection-principle assertion is needed for this optimization.

**Step 2 (conditional optimal second sample).** Fix \(s\). If \(Y\le0\), the event is already detected. If \(Y=y>0\), the two conditional path segments are Brownian bridges with endpoints \((c,y)\) and \((y,c)\), of lengths \(s\) and \(1-s\). By Step 1, the maximum second-checkpoint detection chance in the left segment is \(\Phi(-2\sqrt{cy/s})\), and in the right segment it is \(\Phi(-2\sqrt{cy/(1-s)})\). Choose the longer interval. If \(s>1/2\), choose time \(sc/(c+y)\) in the left segment; if \(s<1/2\), choose time \(s+(1-s)y/(c+y)\) in the right segment. At \(s=1/2\), either choice is optimal. These formulas define measurable valid second-query policies for all \(y>0\). The relative order of the two candidate probabilities does not depend on the realized positive value \(y\).

**Step 3 (exact success functional).** The first observation has law \(Y\sim N(c,v_s)\). Integrating the Step 2 conditional optimum yields
\[
J_c(s)=\Phi\!\left(-\frac c{\sqrt{v_s}}\right)
+\int_0^\infty\frac{e^{-(y-c)^2/(2v_s)}}{\sqrt{2\pi v_s}}
\Phi\!\left(-2\sqrt{\frac{cy}{L_s}}\right)\,dy.
\]
This also proves that randomized second-query times cannot improve on the deterministic conditional maximizer. Symmetry gives \(J_c(s)=J_c(1-s)\). The function is continuous on the open interval and extends continuously to the endpoints, with \(J_c(0)=J_c(1)=\Phi(-2c)\), by Gaussian convergence and dominated convergence.

**Step 4 (strict cusp).** At \(s=1/2\), the derivative of \(v_s\) vanishes, as does the derivative of the first term and that of the Gaussian density under the integral. For \(s>1/2\), \(L_s=s\). Differentiating the conditional Gaussian CDF, justified locally by a Gaussian integrable envelope, gives
\[
J_c'(1/2+)=\int_0^\infty\sqrt{\frac2\pi}
 e^{-2(y-c)^2}\, 2\sqrt{2cy}\,\phi(2\sqrt{2cy})\,dy.
\]
The exponents combine to \(-2y^2-2c^2\). Consequently
\[
J_c'(1/2+)=\frac{2\sqrt{2c}}\pi e^{-2c^2}
\int_0^\infty y^{1/2}e^{-2y^2}\,dy
=\frac{\Gamma(3/4)}{2^{1/4}\pi}\sqrt c\,e^{-2c^2}>0.
\]
Symmetry gives the negative left derivative. Thus the midpoint is a strict local minimum rather than an optimum.

**Step 5 (global off-center optimizers exist).** At the midpoint, the probability of a negative first observation is \(\Phi(-2c)\); the second query has strictly positive extra success probability conditional on the first being positive. Therefore \(J_c(1/2)>\Phi(-2c)=J_c(0)=J_c(1)\). Continuity on the closed interval, strict cusp improvement on either side of \(1/2\), and endpoint strict inequality force a maximum at some \(s_c\in(0,1/2)\); by reflection, \(1-s_c\in(1/2,1)\) is also a maximizer. This proves existence but *not uniqueness* of the maximizer on either half.

## Verification
Run `python3 verification.py`. The standalone Python-standard-library script checks the exact one-checkpoint formula against a dense finite grid in three endpoint configurations, evaluates the exact success functional by smooth-variable Simpson quadrature, compares one-sided slopes with the gamma constant for five positive clearances, and checks reflection symmetry and a strict off-center improvement. These computations are checks, not a substitute for the all-parameter proof above. At \(c=1/2\), the integral gives \(J_c(1/2)\approx0.235721748459\) and \(J_c(1/3)\approx0.246462033900\), an approximately \(4.56\%\) relative increase in alarm probability. The analytically proved strict cusp applies to *every* \(c>0\); the numerical example only illustrates it.

## Relationship to prior work
The conditional Brownian-bridge construction and minimum laws are classical. Alabert and Caballero (first arXiv version 2015) treat bridge minima and compare *nonadaptive* point selection for minimum-value approximation. Calvin, Hefter and Herzwurm (first arXiv version 2016) analyze adaptive approximation of a Brownian *minimum*, using a midpoint-based interval-refinement strategy with an error criterion and asymptotic rates. Hoel and Ragunathan (first arXiv version 2022) study adaptive numerical approximation of diffusion exit times by time-stepping. None of these stated results supplies the exact finite-two-query, binary-barrier-detection functional and its strict midpoint symmetry breaking. The bridge marginal law used in the derivation is acknowledged as standard and is not claimed as new. The uninspected full original text of the Calvin--Hefter--Herzwurm paper is a residual priority risk.

## Limitations
This is a statement about retrospective conditional sampling under a Brownian-bridge law, not a causal online monitoring schedule. It does not identify the unique globally best off-center first time, claim optimality for noisy values, asymmetric endpoints, other barriers, non-Brownian diffusion bridges, arbitrary budgets, or estimation of the continuous minimum. In particular, conditional Brownian-bridge sampling of the exact path minimum can circumvent the need to detect crossings by finite point inspections. No historical-priority or independent validation is certified here.

## References
1. H. Hoel and S. Ragunathan, *Higher-order adaptive methods for exit times of Itô diffusions*, arXiv:2208.11288, first public 2022-08-24. https://arxiv.org/abs/2208.11288
2. A. Alabert and R. Caballero, *On the minimum of a conditioned Brownian bridge*, arXiv:1511.05735, first public 2015-11-18; accessible 2017 preprint https://mat.uab.cat/dpt/Publ/prep/p07_17.pdf
3. J. M. Calvin, M. Hefter and A. Herzwurm, *Adaptive approximation of the minimum of Brownian motion*, arXiv:1601.01276, first public 2016-01-06. https://arxiv.org/abs/1601.01276
