# A sharp correction-order transition for alternating intermittent inverse branches

## Finding

The first subleading correction to the neutral inverse-branch clock of two periodically alternating Liverani–Saussol–Vaienti (LSV) interval maps changes order at the precise resonance \(\beta=2\alpha\). Below resonance it grows with a positive fractional power, at resonance it is a positive logarithm, and above resonance it is a negative logarithm. The leading clock is independent of the larger exponent.

Define \(c=\alpha2^\alpha\) and \(\theta=(\beta-\alpha)/\alpha\). For the inverse orbit specified below, \(u_n=x_n^{-\alpha}\), the complete first-subleading trichotomy is

\[
u_n=\begin{cases}
cn+\dfrac{\alpha2^\beta c^{-\theta}}{1-\theta}n^{1-\theta}+o(n^{1-\theta}),&\alpha<\beta<2\alpha,\\
cn+2^{\alpha-1}(1-\alpha)\log n+O(1),&\beta=2\alpha,\\
cn-2^{\alpha-1}(1+\alpha)\log n+O(1),&\beta>2\alpha.
\end{cases}
\]

The first two coefficients in each regime do not depend on the initial \(x_0\), nor on which of the two inverse branches acts first in a pair.

## Assumptions and scope

Fix real parameters \(0<\alpha<1\), \(\beta>\alpha\). The standard left LSV branch is \(T_a(x)=x(1+2^a x^a)\) for \(0\le x\le1/2\); its increasing inverse \(g_a\colon[0,1]\to[0,1/2]\) is uniquely defined by \(T_a(g_a(y))=y\). Choose any \(x_0\in(0,1/2]\), and set \(x_{n+1}=g_\beta(g_\alpha(x_n))\) for all integers \(n\ge0\). Reversing the branch order is also allowed. Each \(x_n\) is positive, strictly decreases, and tends to zero. The clock \(u_n\) counts *pairs* of inverse branches; it is not the ordinary one-step clock.

## Proof

Set \(A=2^\alpha\), \(B=2^\beta\). The defining inverse equation and elementary Taylor expansion give, for each fixed \(a>0\),
\[
g_a(y)=y-2^a y^{1+a}+(1+a)2^{2a}y^{1+2a}+O(y^{1+3a})\qquad(y\downarrow0).
\]
Since \(\beta>\alpha\), composition in either order yields
\[
g_\beta(g_\alpha(x))=x-Ax^{1+\alpha}-Bx^{1+\beta}+(1+\alpha)A^2x^{1+2\alpha}
+O\bigl(x^{1+\min(3\alpha,\alpha+\beta)}\bigr).
\]
(The term of degree \(1+2\beta\) is of still higher order.) Expanding the inverse power and writing \(u=x^{-\alpha}\) now gives, with \(\theta=(\beta-\alpha)/\alpha>0\),
\[
u_{n+1}-u_n=c+\alpha B u_n^{-\theta}
-\frac{\alpha(1+\alpha)}2A^2u_n^{-1}+O(u_n^{-\eta}),
\qquad c=\alpha A,\quad \eta=\min\{2,\beta/\alpha\}>1.
\tag{1}
\]
The expression is order-independent through all terms displayed. Because both inverse maps are strictly below the identity on positive inputs, \(x_n\downarrow0\). Equation (1) therefore implies \(u_{n+1}-u_n\to c>0\), hence \(u_n\sim cn\) by Cesàro averaging.

If \(0<\theta<1\), summing (1), using \(u_j\sim cj\), and comparing a regularly varying sum to an integral gives
\[
\sum_{j=1}^{n}u_j^{-\theta}\sim\frac{c^{-\theta}}{1-\theta}n^{1-\theta}.
\]
The \(u_j^{-1}\) contribution is \(O(\log n)=o(n^{1-\theta})\), and the last term in (1) is summable. This proves the fractional-power branch.

For \(\theta\ge1\), equation (1) first implies \(u_n=cn+O(\log n)\). Therefore \(u_n^{-1}=(cn)^{-1}+O((\log n)/n^2)\) and \(\sum_{j=1}^{n}u_j^{-1}=c^{-1}\log n+O(1)\). If \(\theta>1\), the \(u_j^{-\theta}\) sum converges, yielding the coefficient \(-\alpha(1+\alpha)A^2/(2c)=-(1+\alpha)A/2\). At \(\theta=1\), necessarily \(B=A^2\); the two \(u_j^{-1}\) coefficients combine to \(\alpha A^2(1-\alpha)/2\), giving the normalized coefficient \(A(1-\alpha)/2\). All other terms in (1) have summable tails. This proves both logarithmic branches, including their bounded remainders and phase independence.

## Verification

The proof above is analytic and uniform in time for each fixed pair of exponents; no finite computation establishes an infinite limit. The standalone `checker.py` numerically inverts each branch by bisection, iterates up to \(30000\) pairs, and tests representative points from the three regimes. It also tests both inverse-branch orders and compares with the exact correction coefficients. The experiment is a stress test and is not a certificate of historical originality or of the asymptotic theorem.

## Relationship to prior work

Ji, *Schmidt games for nonautonomous Liverani–Saussol–Vaienti maps* (arXiv:2611.11758v1; first public 2026-11-09), studies arbitrary parameter schedules and establishes absolute-winning target avoidance, not this periodic two-parameter correction trichotomy. Bahsoun and Bose, *Mixing rates and limit theorems for random intermittent maps* (arXiv:1503.06157), establish leading first-return inverse-branch asymptotics for randomly sampled exponents; their leading law is compatible with the \(cn\) term but does not determine the three distinct subleading regimes for a deterministic alternating schedule. The method is a higher-order parabolic inverse-iteration expansion, not a new leading-order or almost-sure random limit theorem.

## Limitations

Parameters \(\alpha\ge1\) and \(\beta=\alpha\) are excluded from this stated trichotomy; the second produces a different leading clock. The estimates concern a specified deterministic alternating inverse orbit, not the full LSV map's invariant density, a random sequence, or a first-return distribution. The constants hidden in \(O(1)\) depend on parameters and initial condition; no uniformity near \(\beta=2\alpha\) is claimed. Earlier equivalent higher-order parabolic asymptotics may exist beyond the sources inspected, so historical priority is subject to external verification.

## References

1. H. Ji, *Schmidt games for nonautonomous Liverani–Saussol–Vaienti maps*, arXiv:2611.11758v1 (2026), https://arxiv.org/abs/2611.11758.
2. W. Bahsoun and C. Bose, *Mixing rates and limit theorems for random intermittent maps*, arXiv:1503.06157 (2015), https://arxiv.org/abs/1503.06157.
3. A. Korepanov and J. Leppänen, *Improved polynomial rates of memory loss for nonstationary intermittent dynamical systems*, arXiv:2410.20994 (2024), https://arxiv.org/abs/2410.20994. (Context; abstract-level comparison only.)
