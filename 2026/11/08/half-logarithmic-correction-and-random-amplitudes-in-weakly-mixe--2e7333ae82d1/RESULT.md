# Half-logarithmic correction and random amplitudes in weakly mixed urns

## Finding
Consider a two-colour urn with positive integer initial counts, whose replacement rule is independently selected at round \(n\): with probability \(p_n\) use the Friedman rule (add \(a\) balls of the drawn colour and \(b\) of the other), and otherwise use the Pólya rule (add \(c\) balls of the drawn colour). Assume integers \(a\ge b\ge1\), \(c\ge1\) and **unbalanced rule totals** \(\delta=a+b-c\ne0\). Put \(Z_n\) equal to the proportion of the first colour. Fix \(\kappa>0\), \(1/2\le\theta\le1\), and a sufficiently large fixed integer \(n_0\) that \(p_n=\kappa/[\log(n+n_0)]^\theta<1\) for every \(n\ge1\).

For \(n\ge3\), define the following *deterministic* normalizers:

\[
R_{n,\theta}=\begin{cases}
\exp\!\left(\frac{4b\kappa}{c}\sqrt{\log n}\right)
(\log n)^{-2b\delta\kappa^2/c^2},&\theta=\frac12,\\[3pt]
\exp\!\left(\frac{2b\kappa}{c(1-\theta)}(\log n)^{1-\theta}\right),&\frac12<\theta<1,\\[3pt]
(\log n)^{2b\kappa/c},&\theta=1.
\end{cases}
\]

**Theorem.** There is a finite random variable \(L_\theta\) such that
\[
R_{n,\theta}(Z_n-\tfrac12)\longrightarrow L_\theta
\qquad\text{almost surely}.
\]
For almost every realization of the complete replacement-rule sequence, the conditional law of \(L_\theta\) is nondegenerate (indeed it has strictly positive conditional variance). In particular, the normalizations are sharp in the sense that an asymptotically larger deterministic normalizer cannot yield a tight sequence, while an asymptotically smaller one gives zero almost surely.

At \(\theta=1/2\), the unbalanced total additions generate the extra power \((\log n)^{-2b\delta\kappa^2/c^2}\). This factor is absent at \(\theta>1/2\) and identically one for balanced totals \(\delta=0\). No closed-form density or atomlessness of \(L_\theta\) is asserted.

## Assumptions and scope
All parameters are fixed independently of \(n\). At each round a ball is sampled uniformly and returned, then the chosen additions are made. The rule indicators \(\xi_n\) are independent Bernoulli variables with probabilities \(p_n\), independent of the draws. Both initial colour populations are strictly positive. Natural logarithms are used. The restriction \(a\ge b\) guarantees positivity of the exact conditional contraction factors; the claimed theorem is not extended to the opposite parameter order. The assertion is an almost-sure limit and conditional nondegeneracy, not a central limit theorem.

Let \(T_n\) be the total number of balls, \(V_n=Z_n-1/2\), and \(A=a+b\). Given the complete sequence \(\xi=(\xi_1,\xi_2,\ldots)\), the total \(T_n=T_0+cn+\delta\sum_{j\le n}\xi_j\) is deterministic. Put
\[
d_n=\frac{2b\xi_n}{T_{n-1}+A},\qquad J_n=\prod_{j=1}^n(1-d_j),\quad J_0=1.
\]
The factors satisfy \(0<1-d_n\le1\) because \(a\ge b\) and \(T_0>0\).

## Proof
**1. Exact quenched martingale.** Condition on \(\xi\) and the first \(n-1\) colour draws. If the next draw is from the first colour, this happens with probability \(Z_{n-1}\). For a Pólya round the conditional expectation of \(Z_n\) is exactly \(Z_{n-1}\). For a Friedman round it is
\[
\frac{Z_{n-1}(T_{n-1}+a)+(1-Z_{n-1})b}{T_{n-1}+A}
=\frac12+\left(1-\frac{2b}{T_{n-1}+A}\right)V_{n-1}.
\]
Therefore \(\mathbb E(V_n\mid\mathcal F_{n-1},\xi)=(1-d_n)V_{n-1}\), and \(W_n=V_n/J_n\) is a martingale, conditionally on \(\xi\). Since the number of balls added in a step is at most \(M=\max(A,c)\), and the total is at least \(T_0+n\min(A,c)\), its centered increments satisfy
\[
|V_n-\mathbb E(V_n\mid\mathcal F_{n-1},\xi)|\le \frac{C}{n}
\]
for a deterministic constant \(C\) and all \(n\ge1\) after harmless adjustment for the first few steps.

**2. Quenched total and switch sums.** For \(\theta\in[1/2,1]\), independence and Hoeffding's inequality give
\[
\sum_{j\le n}\xi_j=\frac{\kappa n}{(\log n)^\theta}
+O\!\left(\frac{n}{(\log n)^{\theta+1}}\right)
\quad\text{almost surely}.
\]
Indeed \(\sum_{j\le n}p_j=\kappa n/(\log n)^\theta+O(n/(\log n)^{\theta+1})\), and the centered partial sums are \(O(\sqrt{n\log n})\) eventually almost surely by a summable Hoeffding bound. Thus, with \(\delta=A-c\),
\[
\frac{1}{T_{j-1}+A}
=\frac{1}{cj}-\frac{\delta\kappa}{c^2j(\log j)^\theta}
+O\!\left(\frac{1}{j(\log j)^{2\theta}}\right)
\quad\text{almost surely},
\]
where all displayed asymptotics involving logarithms apply for sufficiently large indices. The remainder, multiplied by \(\xi_j\), is absolutely summable almost surely: its expected nonnegative majorant has order \(\sum_j1/[j(\log j)^{3\theta}]<\infty\).

Moreover, for any \(r\ge0\), the series
\[
\sum_{j\ge3}\frac{\xi_j-p_j}{j(\log j)^r}
\]
converges almost surely by independence and the square-summability of its variances. The elementary integral test, with the fixed shift \(n_0\), consequently gives
\[
\sum_{j=3}^n\frac{\xi_j}{j}
=\begin{cases}
\frac{\kappa}{1-\theta}(\log n)^{1-\theta}+C_1+o(1),&\theta<1,\\
\kappa\log\log n+C_1+o(1),&\theta=1,
\end{cases}
\]
and
\[
\sum_{j=3}^n\frac{\xi_j}{j(\log j)^\theta}
=\begin{cases}
\kappa\log\log n+C_2+o(1),&\theta=1/2,\\
C_2+o(1),&\theta>1/2,
\end{cases}
\]
with finite, possibly random constants \(C_1,C_2\).

**3. The sharp product asymptotic.** As \(d_j=O(1/j)\), the series \(\sum d_j^2\) converges. Expanding \(-\log(1-d_j)\), inserting the reciprocal-total expansion, and using the two switch sums yields
\[
-\log J_n
=\frac{2b}{c}\sum_{j\le n}\frac{\xi_j}{j}
-\frac{2b\delta\kappa}{c^2}\sum_{j\le n}\frac{\xi_j}{j(\log j)^\theta}
+C_3+o(1).
\]
In particular, the precise cancellation built into \(R_{n,\theta}\) proves that
\[
J_nR_{n,\theta}\longrightarrow K(\xi)\in(0,\infty)
\qquad\text{almost surely}.
\]
For \(\theta=1/2\), the second sum grows as \(\kappa\log\log n\), producing the stated correction with its sign. When \(\theta>1/2\), it converges, so no logarithmic-power correction remains.

**4. Conditional convergence and strict randomness.** For almost every switch sequence, step 3 implies \(J_n^{-1}=n^{o(1)}\). Consequently the conditional martingale \(W_n=V_n/J_n\) has square-summable conditional increment variances:
\[
\sum_{n\ge1}\mathbb E\bigl[(W_n-W_{n-1})^2\mid\mathcal F_{n-1},\xi\bigr]
\le C^2\sum_{n\ge1}\frac{1}{n^2J_n^2}<\infty.
\]
Hence \(W_n\to W_\infty\) almost surely and in conditional \(L^2\). Combined with step 3 this gives \(L_\theta=K(\xi)W_\infty\).

Because \(p_n\to0\), almost every switch sequence contains a Pólya round \(j\) (in fact infinitely many). The two possible colour draws at that round have positive probabilities. Conditionally on the past and \(\xi\), they give a strictly positive variance
\[
\operatorname{Var}(W_j\mid\mathcal F_{j-1},\xi)
=\frac{c^2 Z_{j-1}(1-Z_{j-1})}{J_j^2(T_{j-1}+c)^2}>0.
\]
Since \(W_j=\mathbb E(W_\infty\mid\mathcal F_j,\xi)\), the conditional law of \(W_\infty\), and therefore of \(L_\theta\), has strictly positive variance. Its nondegeneracy proves the sharp-scaling assertion: on a positive-probability event \(|L_\theta|>\varepsilon\), any larger deterministic scaling diverges in absolute value, while every smaller scaling converges to zero.

## Verification
The included `check.py` uses exact rational arithmetic to test the one-step conditional expectation, positivity of the factors, quenched-martingale means, monotonicity of second moments, and positive variance after a Pólya step for unequal rule totals. Its finite exhaustive checks do not establish infinite-series convergence or the almost-sure theorem; steps 2–4 supply those arguments. Running `python3 check.py` with Python 3 requires only the standard library and returns 9,404 passed exact assertions.

## Relationship to prior work
Alves and Rosales, *Friedman vs Pólya*, arXiv:2502.16768 (first posted 2025-02-24), prove convergence of the colour proportion for a **fixed positive** switching probability. Shi, Yin and Miao, *Central Limit Theorem for a Pólya-Friedman Mixed Urn Model*, arXiv:2605.26669 (first posted 2026-05-26), establish Gaussian fluctuations in a fixed-probability regime. Neither paper states the logarithmically decaying switching law or the conditional, non-Gaussian random-amplitude scaling and its half-logarithmic correction. A qualitative harmonic-frequency criterion in the balanced-total regime does not itself fix the normalization asserted here; the theorem does not claim that criterion as a new result. Gangopadhyay and Maulik, arXiv:1709.00467 (2017), treat random replacement matrices under assumptions including approximation to an irreducible limiting matrix; here the expected matrix approaches the reducible Pólya replacement at vanishing switch probability. A more general time-inhomogeneous urn theorem could still imply this special limit, so historical priority is not certified.

## Limitations
The result concerns two colours and exogenous independent switches; it does not treat feedback-dependent switching, arbitrary negative additions, or parameters with \(a<b\). The limit variable is specified by a martingale and a random positive factor, not an explicit law. The endpoint \(\theta<1/2\) requires further diverging terms and is not claimed. Finite exact checks cannot certify asymptotic conclusions. No independent mathematical verification or definitive historical-priority audit has been performed.

## References
1. R. Alves and R. A. Rosales, *Friedman vs Pólya*, first posted 2025-02-24, arXiv:2502.16768, https://arxiv.org/abs/2502.16768.
2. J. Shi, Q. Yin, and Y. Miao, *Central Limit Theorem for a Pólya-Friedman Mixed Urn Model*, first posted 2026-05-26, arXiv:2605.26669, https://arxiv.org/abs/2605.26669.
3. U. Gangopadhyay and K. Maulik, *Stochastic Approximation with Random Step Sizes and Urn Models with Random Replacement Matrices Having Finite Mean*, first posted 2017-09-01, arXiv:1709.00467, https://arxiv.org/abs/1709.00467.
4. S. Gao and R. Aguech, *Multiple-drawing dynamic Friedman urns with opposite-reinforcement*, first online 2023-01-26, DOI:10.1017/S0269964822000535, https://doi.org/10.1017/S0269964822000535.
