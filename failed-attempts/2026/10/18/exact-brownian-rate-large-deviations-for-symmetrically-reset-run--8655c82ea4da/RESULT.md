# Exact Brownian-rate large deviations for symmetrically reset run-and-tumble occupation

## Finding
Let a one-dimensional run-and-tumble particle start at the origin with velocity equally likely to be \(+v\) or \(-v\), where \(v>0\). Its velocity reverses at Poisson rate \(\alpha\ge0\). Independently, at Poisson rate \(r>0\), reset its position to zero **and** resample its velocity independently and uniformly from \(\{+v,-v\}\). Define the positive occupation time
\[
A_T=\int_0^T\mathbf 1_{\{X_t>0\}}\,dt.
\]
Put
\[
R=\frac{r(r+2\alpha)}{2(r+\alpha)}.
\]
For every real \(\theta\), the scaled cumulant generating function exists and equals
\[
\Lambda(\theta)=\lim_{T\to\infty}\frac1T\log\mathbb E[e^{\theta A_T}]
 =\frac{\theta-2R+\sqrt{\theta^2+4R^2}}2.
\]
The fractions \(A_T/T\) satisfy a full large-deviation principle at speed \(T\) on \([0,1]\), with good rate
\[
I(a)=R\bigl(1-2\sqrt{a(1-a)}\bigr),\quad 0\le a\le1,
\]
and \(I(a)=+\infty\) outside \([0,1]\). In particular, the **whole large-deviation rate function** agrees exactly with that for positive occupation of reset Brownian motion at reset rate \(R\), despite finite persistence and different finite-time laws. The asymptotic variance is
\[
\lim_{T\to\infty}\frac{\operatorname{Var}(A_T)}T=\frac1{4R}=\frac{r+\alpha}{2r(r+2\alpha)}.
\]
At fixed \(r\), \(R\) strictly increases with \(\alpha\) from \(r/2\) to \(r\); the rate-function shape is universal and its scale is strictly increasing. None of these quantities depends on \(v>0\).

## Assumptions and scope
All Poisson processes and velocity redraws are mutually independent. Positive occupation counts elapsed time strictly to the right of zero; changing the indicator at exactly zero leaves \(A_T\) unchanged almost surely. Resetting renews **both** position and direction; position-only resets retaining the incoming direction are a different nonrenewal model. All statements concern the long-time limit, with \(r>0\), \(v>0\), and \(\alpha\ge0\). The \(\alpha=0\) boundary follows by the formulas and directly from independent exponential reset flights. No claim is made that the entire finite-time occupation distribution equals the Brownian distribution.

## Proof
Write \(M_0(t,\theta)=\mathbb E_0[e^{\theta A_t}]\) for a free run-and-tumble flight with a uniformly redrawn initial direction, and \(F(s,\theta)=\int_0^\infty e^{-st}M_0(t,\theta)\,dt\). Initially take \(\alpha>0\) and \(s>\max\{0,\theta\}\). Let \(q=s\), \(p=s-\theta\), and \(D_u=\sqrt{u(u+2\alpha)}\) for \(u>0\). The two conditional resolvents \(u_\pm(x)\) solve
\[
\pm v u_\pm'(x)+\alpha\bigl(u_\mp(x)-u_\pm(x)\bigr)-\bigl(s-\theta\mathbf1_{\{x>0\}}\bigr)u_\pm(x)=-1.
\]
Their bounded solutions have particular values \(1/q\) on the negative half-line and \(1/p\) on the positive half-line. The exponentially decaying homogeneous eigenvectors have minus-to-plus component ratios \((q+\alpha-D_q)/\alpha\) and \((p+\alpha+D_p)/\alpha\), respectively. Continuity of both conditional resolvents at zero and uniform averaging of the two initial directions give the exact simplification
\[
F(s,\theta)=\frac{D_p+D_q}{qD_p+pD_q}. \tag{1}
\]
For \(\alpha=0\), each flight has constant direction, and (1) follows from \(F=(1/p+1/q)/2\). Thus (1) holds for every \(\alpha\ge0\). Notice that the speed \(v\) cancels from the interface matching.

Independence and full renewal at each reset give the Laplace transform of the reset moment generating function:
\[
\widetilde M_r(z,\theta)
 =\frac{F(z+r,\theta)}{1-rF(z+r,\theta)}.\tag{2}
\]
The function \(F(s,\theta)\) is strictly decreasing as a function of \(s>\max\{0,\theta\}\); it diverges as \(s\downarrow\max\{0,\theta\}\), and tends to zero as \(s\to\infty\). Consequently there is a unique \(\lambda>\max\{0,\theta\}-r\) satisfying \(rF(\lambda+r,\theta)=1\). With \(q=\lambda+r\), \(p=q-\theta\), equation (1) rewrites this as
\[
\lambda D_p+(\lambda-\theta)D_q=0.\tag{3}
\]
For positive \(\theta\), positivity of the moment generating function gives \(0<\lambda<\theta\); for negative \(\theta\), it gives \(\theta<\lambda<0\). Thus the two sides of (3) have matching signs, and squaring introduces no ambiguity when the correct root is chosen. Explicit expansion yields, for \(\theta\ne0\),
\[
0=2\theta\Bigl[(r+\alpha)\lambda^2+\bigl(r(r+2\alpha)-(r+\alpha)\theta\bigr)\lambda-\frac{r(r+2\alpha)}2\theta\Bigr].\tag{4}
\]
At \(\theta=0\), equation (2) directly gives \(\lambda=0\). For nonzero \(\theta\), the uniquely admissible root of (4) is
\[
\lambda=\frac{\theta-2R+\sqrt{\theta^2+4R^2}}2.\tag{5}
\]
The other quadratic root fails the sign and normalization conditions.

For completeness, equation (5) is genuinely the exponential growth rate, not merely a candidate pole. Multiplying the renewal equation in time by \(e^{-\lambda t}\) gives a proper nonlattice renewal kernel \(r e^{-(r+\lambda)t}M_0(t,\theta)\,dt\) of total mass one. Since \(\lambda+r>\max\{0,\theta\}\), this kernel has finite positive mean and the forcing term is directly Riemann integrable. The key renewal theorem therefore yields \(e^{-\lambda T}M_r(T,\theta)\to c(\theta)\in(0,\infty)\), establishing \(\Lambda=\lambda\).

The function \(\Lambda\) in (5) is differentiable for every real \(\theta\), with derivative increasing from zero to one. The Gärtner–Ellis theorem and boundedness of \(A_T/T\) give the full large-deviation principle, including the endpoints by approximation from interior points. Its Legendre transform gives \(I\) as displayed. Renewal-reward central limit theory (or differentiating the analytic local renewal pole) gives the asymptotic variance \(\Lambda''(0)=1/(4R)\). Finally \(dR/d\alpha=r^2/[2(r+\alpha)^2]>0\), proving strict monotonicity.

## Verification
The standalone `check.py` checks equation (4) with 256 exact rational substitutions, independently compares interface-matched and simplified resolvents at 72 points, checks 192 nonlinear pole evaluations, and performs seeded event-driven trajectory simulations at three tumbling rates. All tests passed. The numerical comparisons are checks of formulas and normalization, not a proof of the infinite-time large-deviation principle; that principle follows from the renewal and convex-duality arguments above.

## Relationship to prior work
Bressloff (2020), arXiv:2009.01968v1, derived the general direction-dependent Feynman–Kac resolvent and renewal transform for reset run-and-tumble positive occupation, including numerical evaluation of the leading pole; equations (3.10), (4.12), and (4.16) are the relevant starting points. The precise contribution here is the **explicit all-tilt elementary reduction** for independent symmetric velocity redraws and its exact Brownian-effective-rate identification for every finite switching rate. The general earlier transform implicitly encodes the specialization, so the claim does **not** assert a new resetting framework. Den Hollander, Majumdar, Meylahn, and Touchette (2019), arXiv:1801.09909, established the Brownian occupation rate; it is used for comparison rather than claimed as new. Di Bello and collaborators (2023), arXiv:2302.06696, studied currents of ensembles of independently resetting particles, an observable different from one-particle positive occupation time.

## Limitations
Exactness here is for a single free particle, constant speed magnitude, homogeneous tumbles, exponential reset times, independent *symmetric* direction redraws, and positive-half-line occupation. It does not establish equivalent finite-time distributions, position-only resets, biased direction redraws, confinement, coupled particles, or general reset waiting laws. The explicit expression is an algebraic specialization of a previously published general resolvent: implicit coverage is a real scientific-priority consideration. Independent validation and priority assessment have not been performed.

## References
1. P. C. Bressloff, *Occupation time of a run-and-tumble particle with resetting*, Phys. Rev. E **102**, 042135 (2020); arXiv:2009.01968v1 (first public 2020-09-04). https://arxiv.org/abs/2009.01968
2. F. den Hollander, S. N. Majumdar, J. M. Meylahn, and H. Touchette, *Properties of additive functionals of Brownian motion with resetting*, J. Phys. A **52**, 175001 (2019); arXiv:1801.09909. https://arxiv.org/abs/1801.09909
3. C. Di Bello et al., *Current fluctuations in stochastically resetting particle systems*, Phys. Rev. E **108**, 014112 (2023); arXiv:2302.06696. https://arxiv.org/abs/2302.06696
