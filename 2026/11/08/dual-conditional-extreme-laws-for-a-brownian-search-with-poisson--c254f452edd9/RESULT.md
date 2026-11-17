# A singular low-reset-rate Bernoulli law for extreme pre-absorption Brownian excursions

## Finding

Let \(X\) be one-dimensional Brownian motion with generator \(D\partial_{xx}\), initially at \(a>0\), killed on first reaching zero, and instantaneously returned to \(a\) at independent Poisson times of rate \(r>0\) while it survives. Write \(T\) for the absorption time, \(M=\sup_{0\le t\le T}X_t\) for the pre-absorption maximum, and \(N\) for the number of completed resets before absorption. Fix \(a,D>0\), put \(\kappa=\sqrt{r/D}\), and let \(m_r>a\) satisfy \(\kappa m_r\to u\in(0,\infty)\) as \(r\downarrow0\). Then

\[
\boxed{\quad\Pr(M>m_r)\sim\frac{\kappa a}{\sinh u},\qquad
\Pr(N=0\mid M>m_r)\longrightarrow e^{-u},\qquad
\Pr(N=1\mid M>m_r)\longrightarrow1-e^{-u},\qquad
\Pr(N\ge2\mid M>m_r)\longrightarrow0.\quad}
\]

Equivalently, the conditional reset count converges in total variation to a Bernoulli random variable with success probability \(1-e^{-u}\). This is a **singular low-rate crossover**: for every fixed \(r>0\), letting \(m\to\infty\) instead makes \(\Pr(N=0\mid M>m)\to0\), so the fixed-rate rare-maximum limit and the low-rate scaling do not commute. Only the singular crossover is advanced here as the new finding.

## Assumptions and scope

The diffusion coefficient \(D>0\), initial/reset point \(a>0\) and target zero are fixed, and the reset clocks and Brownian excursions are independent. The threshold satisfies \(m_r>a\) and \(\kappa m_r\to u\in(0,\infty)\); neither the endpoint \(u=0\) nor \(u=\infty\) is included. Reset at absorption has probability zero. There is no drift, refractory delay, random reset location, or claim about other restart laws. The stated limit concerns a conditional law under a vanishing-probability high-maximum event.

## Proof

For fixed \(r\) and \(m>a\), set \(z=\kappa a\), \(L=\kappa m\), and
\[
A=\frac{\sinh(L-z)}{\sinh L},\qquad B=\frac{\sinh z}{\sinh L},\qquad C=1-A-B,\qquad p=e^{-z},\quad q=1-p.
\]
The standard killed-interval boundary-value equations \(Df''=rf\), with endpoint data \((1,0)\) and \((0,1)\), give \(A\) as the probability that an excursion hits zero before either level \(m\) or its reset clock, and \(B\) as the corresponding probability for first reaching \(m\). The complementary event is reset before either boundary, with probability \(C\). In the half-line without an upper boundary, hitting zero before an exponential reset has probability \(p=\mathbb E_a e^{-r\tau_0}=e^{-z}\), so \(N\) has mass \(pq^n\).

Independence after each restart gives the elementary renewal identity
\[
\Pr(N=n,M<m)=A C^n,\qquad
\Pr(M>m)=1-\frac A{1-C}=\frac B{A+B},\qquad
\Pr(N=0,M>m)=p-A.
\]
These fixed-rate renewal identities and associated standard conditional Gumbel and geometric-size-bias mechanisms are **prior work** or consequences of established formulas; their derivation here supplies the input to the singular limit, not a separate novelty claim.

Now let \(r\downarrow0\), so \(z\to0\) and \(L\to u\in(0,\infty)\). Uniform continuity of the elementary hyperbolic functions in a neighborhood of \(u\) gives
\[
A=1-z\coth u+o(z),\quad B=z\,\operatorname{csch}u+o(z),\quad p=1-z+o(z),\quad q=z+o(z),
\]
and \(C=z\tanh(u/2)+o(z)\). Consequently
\[
\Pr(M>m_r)=\frac B{A+B}\sim\frac z{\sinh u},
\]
while the no-reset contribution is
\[
\Pr(N=0,M>m_r)=p-A=z(\coth u-1)+o(z).
\]
Dividing yields \(\sinh u(\coth u-1)=\cosh u-\sinh u=e^{-u}\). Also
\[
0\le\Pr(N\ge2\mid M>m_r)\le\frac{\Pr(N\ge2)}{\Pr(M>m_r)}=\frac{q^2}{B/(A+B)}=O(z)\longrightarrow0.
\]
The residual conditional mass therefore converges to \(1-e^{-u}\) at \(N=1\). Convergence of all masses of a distribution concentrated asymptotically on \(\{0,1\}\) establishes total-variation convergence.

For the claimed noncommutation, fix \(r>0\) and let \(L\to\infty\). One has \(p-A=O(e^{-2L})\), whereas \(B/(A+B)\asymp e^{-L}\). Hence the conditional zero-reset probability tends to zero at every fixed positive reset rate, unlike \(e^{-u}>0\) in the simultaneous limit. \(\square\)

## Verification and limits

The independent algebraic checks are the hyperbolic first-exit boundary solutions, exact renewal summation, and asymptotic comparison above. Numerical diagnostic substitution at \(u=2\) for decreasing rates corroborates the crossover but does not replace the small-\(r\) proof. No statement about simultaneous fluctuations of reset count at growing \(u\), or about general renewal-clock families, is established.

## Relationship to earlier literature

Guo, Yan and Chen (2023) establish the stopped Brownian maximum marginal. Sunil, Blythe, Evans and Majumdar (2023) establish the geometric count of completed resets before first passage. The established renewal identity for \(\Pr(N=n,M<m)\), the high-reset-count Gumbel mechanism, and the extreme-event geometric-size-bias mechanism are also present in broader renewal resetting analysis: *Erlang resetting creates a clock-order logarithmic correction in first-passage spatial extremes* (public 2026-10-25) proves the general \(p_mq_m^n\) framework and explains the single-exponential-clock specialization. **None of these are claimed as novel here.** The exact new assertion is the nonuniform, low-Poisson-rate/high-threshold Bernoulli crossover with its explicit \(e^{-u}\) zero-reset probability. No inspected earlier statement establishes that two-parameter boundary regime; a more general unindexed simultaneous-scaling result remains a historical-priority risk.

## References

- W. Guo, H. Yan, H. Chen, *Extremal statistics for a resetting Brownian motion before its first-passage time*, arXiv:2306.15929 (2023), https://arxiv.org/abs/2306.15929 .
- J. C. Sunil, R. A. Blythe, M. R. Evans, S. N. Majumdar, *The cost of stochastic resetting*, arXiv:2304.09348 (2023), https://arxiv.org/abs/2304.09348 .
- *Erlang resetting creates a clock-order logarithmic correction in first-passage spatial extremes*, 2026-10-25, https://github.com/Resultary/2026/blob/main/2026/10/25/SCOPE-erlang-resetting-creates-a-clock-order-logarithmic-correction-in--28e1e568a79f/RESULT.md .
