# A sharp mixed-moment cutoff and alternating final-size order in heterogeneous SIR epidemics

## Finding

Consider the deterministic well-mixed susceptible--infectious--removed (SIR) final-size model with *fixed* individual susceptibility \(X\) and infectivity \(C\), potentially dependent. Fix an integer \(k\ge3\), \(k\) distinct positive susceptibility values \(x_1<\cdots<x_k\), and positive frequencies \(p_i=\Pr(X=x_i)\). Put \(u_i=\mathbb E[C\mathbf1_{\{X=x_i\}}]\) and \(m_j=\mathbb E[CX^j]=\sum_i u_ix_i^j\). Let \(\kappa=\beta/\gamma>0\).

**Sharp mixed-moment comparison.** Suppose two positive joint trait laws \(A,B\) have the same susceptibility values and frequencies, satisfy \(m_j^A=m_j^B\) for every \(0\le j\le k-2\), and have common supercritical threshold \(\kappa m_1>1\). Write \(L_A,L_B\) for the unique positive cumulative infection pressures and \(r_A,r_B\) for their eventual population attack fractions. Then

\[
\operatorname{sgn}(L_A-L_B)
=\operatorname{sgn}(r_A-r_B)
=(-1)^k\operatorname{sgn}(m_{k-1}^A-m_{k-1}^B).
\]

Equality at the final moment gives identical cumulative pressures and attack fractions. Knowing the full vector \((m_0,\ldots,m_{k-1})\) is sufficient to calculate these outcomes for the given susceptibility support and frequencies. For every \(k\ge3\) this cutoff is sharp: there are pairs with **both full trait marginals identical**, all moments through degree \(k-2\) identical, the same supercritical reproduction threshold, and strictly different final sizes. The sign of their size difference follows the indicated odd/even parity for *every* supercritical value of \(\kappa\), not just near invasion.

For \(k=2\), \((m_0,m_1)\) already specifies the entire final-size equation; thus three susceptibility classes are the smallest number permitting a final-size discrepancy at fixed mixed mean and mixed first moment.

## Assumptions and scope

We work with closed deterministic mass-action mixing, constant common infectious exit rate \(\gamma>0\), per-contact transmission scaled by the product of a susceptible's \(X>0\) and an infective's \(C>0\), and an initial infective seed vanishing in the positive-major-outbreak limit. The susceptible trait law is fixed during infection. It is natural, but not needed for the algebra, to normalize \(\mathbb E[X]=\mathbb E[C]=1\). Here each group frequency \(p_i>0\), every susceptibility value is distinct and positive, and each \(u_i>0\). The theorem compares positive epidemic branches, which exist because \(\kappa m_1>1\). Attack fractions refer to the deterministic limit conditional on following that branch, not to probabilities of major outbreaks.

The motivating final-size equations, independently stated in the reference model, are

\[
L=\kappa\sum_{i=1}^k u_i(1-e^{-x_iL}),
\qquad r=\sum_{i=1}^k p_i(1-e^{-x_iL}).
\]

## Proof

**1. Existence of a unique positive root.** Define \(F_u(z)=\sum_i u_i(1-e^{-x_iz})\) for \(z\ge0\). Then \(F_u(0)=0\), \(F_u'(0)=m_1>0\), \(F_u''(z)=-\sum_i u_ix_i^2e^{-x_iz}<0\), and \(0<F_u(z)<m_0\) for \(z>0\). Therefore \(F_u(z)/z\) is strictly decreasing from \(m_1\) to zero. For \(\kappa m_1>1\), the equation \(z=\kappa F_u(z)\) has exactly one positive solution \(L_u\). At any positive \(z\), the sign of \(\kappa F_u(z)-z\) is positive precisely below \(L_u\).

**2. The one-dimensional moment fiber.** Put \(b_i=\prod_{\ell\ne i}(x_i-x_\ell)^{-1}\). The elementary Lagrange interpolation identities give

\[
\sum_i b_ix_i^j=0\quad(0\le j\le k-2),
\qquad\sum_i b_ix_i^{k-1}=1.
\]

Since the \((k-1)\times k\) truncated Vandermonde matrix on distinct nodes has rank \(k-1\), all differences \(u_i^A-u_i^B\) preserving the first \(k-1\) mixed moments are proportional to \((b_i)\). In fact,

\[
u_i^A-u_i^B=\Delta b_i,\qquad
\Delta=m_{k-1}^A-m_{k-1}^B.
\]

**3. An all-pressure sign, independent of transmission strength.** Set \(f_z(x)=1-e^{-zx}\). Divided-difference interpolation implies

\[
F_A(z)-F_B(z)
=\Delta\sum_i b_i f_z(x_i)
=\Delta\, f_z[x_1,\ldots,x_k].
\]

By the divided-difference mean-value theorem, for some \(\xi\in(x_1,x_k)\),

\[
f_z[x_1,\ldots,x_k]
=\frac{f_z^{(k-1)}(\xi)}{(k-1)!}
=\frac{(-1)^k z^{k-1}e^{-z\xi}}{(k-1)!},
\]

which has strictly the sign \((-1)^k\) for every \(z>0\). Thus \(F_A-F_B\) has a globally fixed strict sign whenever \(\Delta\ne0\).

**4. Ordering and sufficiency.** Evaluate the two zero-crossing functions at either positive root. The root characterization from step 1 converts the global \(F\)-order into the same strict order of \(L_A,L_B\). Since the marginal susceptibility frequencies agree, \(r(z)=\sum_i p_i(1-e^{-x_iz})\) is a common strictly increasing function of \(z\); the final attack fractions inherit the same order. If \(\Delta=0\), the full Vandermonde system is equal, so \(u^A=u^B\) and both outcomes coincide. Conversely, any \(k\) mixed moments \(m_0,\ldots,m_{k-1}\) invert that system, uniquely fixing \(u\) and the final-size equation.

**5. Sharpness even with fixed full trait marginals.** For arbitrary admissible \(k\ge3\), nodes \((x_i)\) and frequencies \((p_i)\), choose \(a\in(0,1)\), let \(C\) take only \(1-a\) and \(1+a\), and set

\[
\Pr_\pm(C=1+a\mid X=x_i)=\frac12\pm\varepsilon\frac{b_i}{p_i},
\]

where \(\varepsilon>0\) is sufficiently small to keep every conditional probability strictly between zero and one. Because \(\sum_i b_i=0\), the marginal of \(C\) assigns probability \(1/2\) to each value under both couplings. Their class infectivity weights are \(u_i^\pm=p_i\pm2a\varepsilon b_i\). The first \(k-1\) mixed moments agree; their degree-\((k-1)\) moments differ by \(4a\varepsilon>0\). In particular, the shared \(m_1\) remains positive and is independent of the perturbation for \(k\ge3\). Any \(\kappa>1/m_1\) gives equal supercritical reproduction thresholds and strictly different final attack fractions. This proves sharpness without changing either marginal. For \(k=2\), the two-by-two Vandermonde matrix shows no such ambiguity once \(m_0,m_1\) are fixed.

## Verification

An exact three-class counterexample takes

\[
(x_1,x_2,x_3)=(1/2,1,3/2),\quad (p_1,p_2,p_3)=(1/3,1/3,1/3),\quad\kappa=2.
\]

Under both laws the infectivity marginal is \(\Pr(C=1/2)=\Pr(C=3/2)=1/2\). The conditional probabilities of \(C=3/2\) in susceptibility order are \((5/8,1/4,5/8)\) for law \(A\) and \((3/8,3/4,3/8)\) for law \(B\). Corresponding \(u\)-vectors are

\[
(u_i^A)=(3/8,1/4,3/8),\quad
(u_i^B)=(7/24,5/12,7/24).
\]

Both have \(m_0=m_1=1\), but \(m_2^A=19/16\) and \(m_2^B=55/48\). The exact difference of all-pressure response functions is

\[
F_A(z)-F_B(z)=-\frac{e^{-z/2}}{12}(1-e^{-z/2})^2<0\quad(z>0).
\]

Consequently \(L_A<L_B\) and \(r_A<r_B\), with no numerical approximation required. As supplementary numerical orientation, \(L_A\approx1.422282716\), \(L_B\approx1.460125743\), \(r_A\approx0.716440887\), and \(r_B\approx0.724672864\). The standalone `checker.py` uses exact rational arithmetic to check Vandermonde identities and fixed-marginal perturbations for \(3\le k\le10\), plus numerical root comparisons for \(k=3,4,5\). These finite checks do not replace the analytic all-integer proof.

## Relationship to prior work

El Khalifi (2026) supplies the positive-branch scalar final-size equation and proves concordance ordering for arbitrary joint susceptibility--infectivity laws. That ordering does not compare the constructed three-class pair: its conditional excess infectivity alternates between low, middle, and high susceptibility classes, so the couplings are not concordance ordered. The exact moment cutoff and the odd/even all-pressure comparison are not stated in the inspected preprint. Standard Vandermonde inversion and the divided-difference sign theorem are pre-existing mathematical tools, not claimed as new.

Novozhilov (2012) explains that matching a few moments of an unrestricted susceptibility distribution does not normally determine final epidemic size. Our result is restricted to *known finite susceptibility support* and gives its exact sufficient moment count and sign of the first unmatched dependence moment. Katriel (2012) studies attack-size orderings for susceptibility distributions, while the present comparison fixes the entire susceptibility marginal and varies its coupling to infectivity. Muslim (2026) establishes finite factorial-moment equivalence for *interaction-group size* under polynomial contagion kernels; those are different variables and epidemic operators from the exponential SIR trait-coupling equation used here. Tuschhoff and Kennedy (2025) study effects of susceptibility--infectivity correlation in stochastic individual-based epidemics, but their accessible descriptions do not establish this deterministic finite-support hierarchy. Remaining historical-priority risk is stated in the review file.

## Limitations

The result concerns final deterministic epidemic size in a closed, well-mixed, rank-one transmission model with time-invariant traits and constant recovery. It is not a theorem for heterogeneous contact matrices, changing susceptibility, nonlinear incidence, finite-population extinction, or outbreak probability. Known susceptibility support and marginal frequencies are essential to the stated finite information cutoff. The theorem does not say that a few moments suffice for arbitrary continuous or unknown support, or that equal final sizes force equal moments under an arbitrary single comparison. The mathematical order is exact, but historical priority remains subject to broader literature review.

## References

1. M. El Khalifi, *Dependence Structure and Epidemic Outcomes in Heterogeneous SIR Models* (2026), arXiv:2601.01549, https://arxiv.org/abs/2601.01549.
2. A. S. Novozhilov, *Epidemiological models with parametric heterogeneity: Deterministic theory for closed populations* (2012), arXiv:1202.2448, https://arxiv.org/abs/1202.2448; doi:10.1051/mmnp/20127310.
3. G. Katriel, *The size of epidemics in populations with heterogeneous susceptibility* (2012), Journal of Mathematical Biology 65, 237--262, doi:10.1007/s00285-011-0460-2.
4. R. Muslim, *Exact moment equivalence and structural nonidentifiability in nonlinear epidemics* (2026), arXiv:2608.04943, https://arxiv.org/abs/2608.04943.
5. B. M. Tuschhoff and D. A. Kennedy, *Heterogeneity in and correlation between host transmissibility and susceptibility can greatly impact epidemic dynamics* (2025), Journal of Theoretical Biology 611, 112186, doi:10.1016/j.jtbi.2025.112186.
6. P. Neal, *Coupling of Two SIR Epidemic Models with Variable Susceptibilities and Infectivities* (2007), Journal of Applied Probability 44, 41--57, doi:10.1239/jap/1175267162.
