# A sparse slow-class crossover in the many-copy coupon collector

## Finding

Fix \(c>0\), \(0<r<1\), and \(\kappa>0\). There is a unique \(y>c\) satisfying \(y-c-c\log(y/c)=1\). Assume \(r>c/y\), and set
\[
a=1-c/y,\qquad b=r-c/y,\qquad
\delta=ry-c-c\log(ry/c),\qquad \eta=(1-b/a)/2.
\]
Thus \(0<b<a\), \(0<\delta<1\), and \(0<\eta<1/2\). For each sufficiently large integer \(n\), set \(m_n=\lfloor c\log n\rfloor\) and
\[
Q_m(z)=e^{-z}\sum_{j=0}^{m-1}\frac{z^j}{j!},\qquad
nQ_{m_n}(u_n)=1,\qquad
M_n=\left\lfloor\frac{\kappa}{Q_{m_n}(ru_n)}\right\rfloor,
\qquad D_n=n+rM_n.
\]
Draw coupons independently with replacement from \(n\) fast types of individual probability \(1/D_n\) and \(M_n\) slow types of individual probability \(r/D_n\). Let \(T_n\) be the first draw at which every type has appeared at least \(m_n\) times, and let \(J_n\) denote the class, fast \(F\) or slow \(S\), of the type receiving the finishing draw.

Then \(M_n=\Theta(n^\delta(\log n)^\eta)\), and the centered completion time and identity of the final class converge jointly:
\[
\left(\frac{T_n-D_nu_n}{D_n},J_n\right)\Rightarrow(X,J).
\]
The limit is the maximum point and its color in the superposition of two independent Poisson point processes on \(\mathbb R\), with respective intensities
\[
\mu_F(dx)=a e^{-ax}\,dx,\qquad
\mu_S(dx)=\kappa b e^{-bx}\,dx.
\]
In particular,
\[
\mathbb P(X\le x)=\exp\{-e^{-ax}-\kappa e^{-bx}\},\qquad x\in\mathbb R,
\]
and the probability that the last completed coupon is slow satisfies
\[
\mathbb P(J=S)=\frac{\kappa b}{a}\int_0^\infty
v^{b/a-1}\exp\{-v-\kappa v^{b/a}\}\,dv\in(0,1).
\]
The distribution of \(X\) is not an affine Gumbel law. Moreover the exponent \(\eta\) is the sharp logarithmic boundary: for any alternative positive integer counts \(L_n\), keeping \(m_n\), \(n\), \(r\) and the same fast normalization, if \(L_n=o(n^\delta(\log n)^\eta)\) then the last class is fast with probability tending to one, whereas if \(L_n\gg n^\delta(\log n)^\eta\) the last class is slow with probability tending to one. In the latter two comparisons the total sampling normalizer is \(n+rL_n\).

## Assumptions and scope

All parameters \(c,r,\kappa\) are fixed independently of \(n\). The condition \(r>c/y\) places the slow-class Gamma tail in its strictly large-deviation regime and guarantees a genuine two-class crossover with a sublinear number of slow types. The quota \(m_n\) is the same for every type. The asymptotic probability, not the sample size, defines the rate normalization \(D_n\). The equality \(nQ_{m_n}(u_n)=1\) has a unique positive solution for all \(n>1\), because \(Q_{m_n}\) decreases continuously from one to zero. Statements involving \(m_n\) require \(m_n\ge1\), hence sufficiently large \(n\).

## Proof

**1. Gamma-tail estimates and the threshold scale.** Write \(L=\log n\) and \(H_c(z)=z-c-c\log(z/c)\) for \(z>c\). When \(m=\lfloor cL\rfloor\) and \(z=wL+O(\log L)\) with fixed \(w>c\), write \(Q_m(z)\) as its final Poisson term times a backward sum:
\[
Q_m(z)=\frac{e^{-z}z^{m-1}}{(m-1)!}
\sum_{j=0}^{m-1}\frac{(m-1)_{\underline j}}{z^j}.
\]
The summands converge to \((c/w)^j\) and, on a fixed neighborhood of \(w\), are dominated by a geometric sequence of ratio strictly below one. The multiplier therefore tends to \((1-c/w)^{-1}\). Stirling's formula yields, uniformly for \(z=wL+O(\log L)\),
\[
\log Q_m(z)=-L H_c(w)-(1-c/w)(z-wL)-\tfrac12\log L+O(1).
\]
The bounded remainder includes the possible variation of \(\lfloor cL\rfloor-cL\); no convergence of that fractional part is assumed. Since \(H_c(y)=1\), monotonicity and this estimate give
\[
u_n=yL-\frac{\log L}{2a}+O(1).
\]
For fixed \(x\), the same backward-sum representation or logarithmic derivative gives, locally uniformly in \(x\),
\[
\frac{Q_{m_n}(u_n+x)}{Q_{m_n}(u_n)}\to e^{-ax},\qquad
\frac{Q_{m_n}(r(u_n+x))}{Q_{m_n}(ru_n)}\to e^{-bx}.
\]
Apply the log-tail estimate with \(w=ry>c\) and \(z=ru_n\). The result is
\[
\log Q_{m_n}(ru_n)=-\delta L-\eta\log L+O(1).
\]
Consequently \(Q_{m_n}(ru_n)=\Theta(n^{-\delta}(\log n)^{-\eta})\). The strict inequalities on \(\delta\) follow from \(H_c(c)=0\), strict increase on \((c,\infty)\), and \(c<ry<y\). Thus \(M_n\to\infty\), \(M_n=o(n)\), and \(D_n\sim n\).

**2. Independent colored extremal point processes.** Introduce an independent unit-rate Poisson clock for drawing coupons. Poisson thinning makes the type-specific arrival processes independent, with rates \(1/D_n\) for fast coupons and \(r/D_n\) for slow ones. Divide time by \(D_n\). The \(m_n\)-th arrival times are independent \(\operatorname{Gamma}(m_n,\mathrm{rate}\ 1)\) for fast types and \(\operatorname{Gamma}(m_n,\mathrm{rate}\ r)\) for slow types. Subtract \(u_n\) from each of these times and mark it by class.

For every fixed \(x\), the expected counts of points exceeding \(x\) are
\[
nQ_{m_n}(u_n+x)\to e^{-ax},\qquad
M_nQ_{m_n}(r(u_n+x))\to\kappa e^{-bx}.
\]
Each individual exceedance probability tends to zero. More generally, counts in finitely many disjoint bounded intervals are multinomial within each class and independent across classes; their joint generating functions converge to those of independent Poisson counts, since the interval probabilities vanish and their group-multiplied probabilities converge. This proves convergence of the two colored point processes on bounded windows to independent Poisson processes of the displayed intensities.

The maximum and its color converge jointly: the probability of any point above \(R\) tends to at most \(e^{-aR}+\kappa e^{-bR}\), and the probability of having no points above \(-R\) tends to \(\exp(-e^{aR}-\kappa e^{bR})\); both errors vanish as \(R\to\infty\). The limiting processes have almost surely a unique greatest point. Their no-points-above-\(x\) probability gives the asserted distribution. The probability that the greatest point belongs to the slow process is the integral over \(x\) of
\[
\kappa b e^{-bx}\exp(-e^{-ax}-\kappa e^{-bx})\,dx.
\]
The substitution \(v=e^{-ax}\) gives the stated formula. Distinct slopes \(a\ne b\) force \(\log[-\log\mathbb P(X\le x)]\) to be non-affine, excluding any shifted or scaled Gumbel law.

**3. Return to the discrete draw clock.** Let \(S_k\) be the time of the \(k\)-th rate-one Poisson clock event and \(T_n\) the completion index of the marked event stream. The Poissonized completion time is precisely \(S_{T_n}\), and its final coupon class is exactly \(J_n\). As the marked coupon sequence is independent of all exponential interarrival times, conditioning on \(T_n\) gives \(\mathbb E[S_{T_n}\mid T_n]=T_n\) and \(\operatorname{Var}(S_{T_n}\mid T_n)=T_n\).

Step 2 shows \(S_{T_n}/D_n=u_n+O_{\mathbb P}(1)=O_{\mathbb P}(\log n)\). Comparing to a deterministic clock index \(K_n=\lceil C D_n\log n\rceil\) for large fixed \(C\), with \(S_{K_n}/K_n\to1\), yields \(T_n=O_{\mathbb P}(D_n\log n)\). For fixed \(\varepsilon>0\), conditional Chebyshev on \(T_n\le K_n\) gives
\[
\mathbb P(|S_{T_n}-T_n|>\varepsilon D_n,\ T_n\le K_n)
\le\frac{K_n}{\varepsilon^2 D_n^2}
=O\left(\frac{\log n}{D_n}\right)=o(1).
\]
Hence \((S_{T_n}-T_n)/D_n\to0\) in probability; the class mark is unchanged, proving the discrete joint limit.

**4. Sharp class-count threshold.** Set \(R_n=1/Q_{m_n}(ru_n)=\Theta(n^\delta(\log n)^\eta)\). For an arbitrary slow-class count \(L_n\), the fast maximum centered at \(u_n\) remains tight. If \(L_n/R_n\to0\), for every fixed \(R>0\) the chance of any slow point above \(u_n-R\) tends to zero, while the fast maximum is above \(u_n-R\) with limiting probability approaching one as \(R\to\infty\). Thus the slow class cannot finish last with nonvanishing probability. If \(L_n/R_n\to\infty\), for every fixed \(R>0\) the chance of a slow point exceeding \(u_n+R\) tends to one, while the fast maximum is below \(u_n+R\) with limiting probability approaching one as \(R\to\infty\). Therefore the slow class finishes last with probability tending to one. These comparisons concern the relative ordering of the coupon completion clocks, and hence hold regardless of the corresponding total rate normalizers.

## Verification

A standalone numerical diagnostic script `VERIFY.py` checks the exact finite-N no-defect product, interval-ordering and mixture-density identities, the limiting threshold exponents and class-mark integral, and convergence of scaled Erlang tail ratios in several growing examples. These finite calculations are diagnostics, not a substitute for the analytic argument. Run `python VERIFY.py` with Python 3 and SciPy. The proof above establishes the infinite limit and all stated strict parameter ranges.

## Relationship to prior work

Castro and Marinho (2026) prove a Gumbel completion profile with many copies under *uniform* sampling. Long (2026) gives the stronger general unequal-probability terminal-defect transfer theorem (Theorem 4.1), which already implies the **unmarked** limiting completion CDF once the defect profile here is computed. This CDF alone is therefore not claimed as a new general theorem. The present result identifies a sharp sparse-class power-and-log threshold, a genuinely two-slope profile in that regime, and the **joint last-class mark** via the colored extremal process. Earlier point-process methods of Ilienko (2019) address uniformly sampled coupons with fixed multiplicity. Neal (2008), Section 4, extends defect-count arguments to fixed-order \(K\)-coupon collection for unequal sampling probabilities, but does not identify the growing-quota sparse-class crossover or its marked law. The two-speed model with a logarithmically growing quota is distinct. No new Poissonization identity, independent-Gamma representation, or general terminal-defect transfer principle is claimed.

## Limitations

The restriction \(r>c/y\) excludes the boundary \(ry=c\) and the slower-rate regime \(ry<c\); these may have different scales. The fractional part of \(c\log n\) prevents replacing the exact quantile-based critical count by a universal constant times \(n^\delta(\log n)^\eta\) without subsequence information. We do not claim an error rate for the joint limit, expectation asymptotics, or a full classification of arbitrary heterogeneous sampling vectors. Historical priority of the explicit marked critical window requires independent checking against broader extreme-value and coupon-collector literature.

## References

- M. E. Castro and R. Marinho, *Cutoff profile for the coupon collector with many collections*, arXiv:2610.33199 (2026), https://arxiv.org/abs/2610.33199.
- C. D. Long, *Terminal Defects, Growing Multiplicity, and Variance Extremality in the Double Dixie Cup Problem*, arXiv:2604.25108 (2026), https://arxiv.org/abs/2604.25108.
- A. Ilienko, *Convergence of point processes associated with coupon collector's and Dixie cup problems*, arXiv:1904.12954 (2019), https://arxiv.org/abs/1904.12954.
- A. Doumas, *Dixie cup problem in an interlacing process*, arXiv:2510.25900 (2025), https://arxiv.org/abs/2510.25900.
- P. Neal, *The generalized coupon collector problem*, Journal of Applied Probability 45 (2008), 621–629, https://doi.org/10.1239/jap/1222441818 (Section 4 inspected).
