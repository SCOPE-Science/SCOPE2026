# A quenched harmonic threshold for vanishing Friedman reinforcement

## Finding
Fix positive integers \(a,b\), put \(s=a+b\), and start a two-colour urn with positive integer populations \(U_0,V_0\). At each time \(n\ge1\), draw one ball uniformly, return it, and add \(s\) more balls of the drawn colour if \(\xi_n=0\); if \(\xi_n=1\), add \(a\) balls of the drawn colour and \(b\) of the opposite colour. Put \(Z_n=U_n/(U_n+V_n)\). The rule sequence may be any fixed binary sequence, or independent binary choices with arbitrary probabilities \(p_n=\Pr(\xi_n=1)\).

**Quenched theorem.** For every fixed binary rule sequence \((\xi_n)_{n\ge1}\), over the randomness of the successive colour draws:

\[
\sum_{n\ge1}\frac{\xi_n}{n}=\infty
\quad\Longrightarrow\quad Z_n\longrightarrow\frac12\ \text{almost surely};
\]
\[
\sum_{n\ge1}\frac{\xi_n}{n}<\infty
\quad\Longrightarrow\quad Z_n\longrightarrow Z_\infty\ \text{almost surely},
\qquad \operatorname{Var}(Z_\infty)>0.
\]
In the second case the limiting distribution is nondegenerate; it is not asserted to have a density or to avoid the point \(1/2\).

**Independent-rule corollary.** If \(\xi_n\) are independent Bernoulli variables with deterministic \(p_n\in[0,1]\), independent of all colour-draw randomness, then \(Z_n\to1/2\) almost surely precisely when \(\sum_{n\ge1}p_n/n=\infty\). If the series converges, the conditional law of \(Z_\infty\) given the complete rule sequence is nondegenerate for almost every rule realization. For instance, for \(p_n=\min\{1,(\log(n+2))^{-\theta}\}\), the deterministic limit occurs for \(0<\theta\le1\), and a genuinely random limit occurs for \(\theta>1\).

This is a sharp harmonic-frequency criterion: the proportion of opposite-colour replacement steps can tend to zero and nevertheless eliminate the random Pólya limit.

## Assumptions and scope
The initial counts \(U_0,V_0\) and reinforcements \(a,b\) are strictly positive integers. In both rules, the total number of balls added in each round is the same positive integer \(s\), so \(T_n=U_0+V_0+ns\). Draws are uniform from the current composition and conditionally independent given the past. In the quenched assertion, \((\xi_n)\) is fixed in advance and not chosen in response to observed colours. In the independent-rule assertion, the choices are mutually independent and independent of colour draws, but their probabilities need not converge or be monotone.

Let \(x_n=2Z_n-1=(U_n-V_n)/T_n\), and define \(\eta_n=+1\) if the sampled ball is of the first colour, otherwise \(-1\). Thus \(\mathbb E(\eta_n\mid\mathcal F_{n-1},\xi)=x_{n-1}\), where \(\xi\) denotes a fixed complete rule sequence. Positive initial populations and additions ensure \(|x_n|<1\) at every finite time.

## Proof
**1. Exact recursion and summable noise.** Write \(K_n=s-2b\xi_n\), \(r_n=2b\xi_n/T_n\). The colour difference changes by \(K_n\eta_n\). Since \(T_n=T_{n-1}+s\), algebra gives
\[
x_n=(1-r_n)x_{n-1}+\varepsilon_n,
\qquad
\varepsilon_n=\frac{K_n}{T_n}(\eta_n-x_{n-1}).
\]
Conditional on the rule sequence, \((\varepsilon_n)\) is a martingale-difference sequence. Because \(|K_n|\le s\), \(|\eta_n-x_{n-1}|\le2\), and \(T_n\ge ns\),
\[
|\varepsilon_n|\le \frac{2s}{T_n}\le\frac2n,
\qquad
\sum_{n=1}^{\infty}\mathbb E(\varepsilon_n^2\mid\mathcal F_{n-1},\xi)
\le 4s^2\sum_{n=1}^{\infty}T_n^{-2}<\infty.
\]
Hence \(\sum_n\varepsilon_n\) converges almost surely and in \(L^2\), for *each fixed* rule sequence.

**2. Divergent weighted intervention frequency.** Since \(T_n/(sn)\to1\), the divergence of \(\sum \xi_n/n\) is equivalent to that of \(\sum r_n\). For all sufficiently large \(n\), \(0\le r_n\le1/2\). Set \(P_{k,n}=\prod_{j=k+1}^{n}(1-r_j)\). Then \(P_{k,n}\to0\) for every fixed \(k\). Iterating the recursion from a sufficiently large fixed \(N\) yields
\[
x_n=P_{N,n}x_N+\sum_{k=N+1}^{n}P_{k,n}\varepsilon_k.
\]
For each \(n\), \(P_{k,n}\) increases from \(k=N\) to \(k=n\), stays in \([0,1]\), and \(P_{n,n}=1\). A summation-by-parts argument shows that these monotone Toeplitz weights send every convergent series \(\sum\varepsilon_k\) to zero: split off finitely many terms (their individual weights vanish) and bound the remaining weighted sum by twice the largest tail partial sum. Thus \(x_n\to0\) almost surely.

**3. Convergent weighted intervention frequency and strict randomness.** If \(\sum \xi_n/n<\infty\), then \(\sum r_n<\infty\). The drift series \(\sum_n r_nx_{n-1}\) converges absolutely because \(|x_{n-1}|\le1\), while \(\sum_n\varepsilon_n\) converges by step 1. Consequently \(x_n\to x_\infty\) almost surely, also in \(L^2\) by bounded convergence.

Choose a sufficiently late \(k\) such that \(\xi_k=0\) and every subsequent factor \(1-r_j\) is positive. Such a \(k\) exists because finite harmonic weight of the ones forces infinitely many zeros. Put \(A_k=\prod_{j=k+1}^{\infty}(1-r_j)>0\). Iterated conditional means and bounded convergence imply
\[
\mathbb E(x_\infty\mid\mathcal F_k,\xi)=A_kx_k.
\]
At the selected Pólya step \(k\), conditional on the preceding history, the two colour draws have strictly positive probabilities, and
\[
\operatorname{Var}(x_k\mid\mathcal F_{k-1},\xi)
=\left(\frac{s}{T_k}\right)^2(1-x_{k-1}^2)>0.
\]
Therefore \(\operatorname{Var}(x_k\mid\xi)>0\), and the law of total variance gives
\[
\operatorname{Var}(x_\infty\mid\xi)
\ge \operatorname{Var}(\mathbb E(x_\infty\mid\mathcal F_k,\xi)\mid\xi)
=A_k^2\operatorname{Var}(x_k\mid\xi)>0.
\]
Rescaling \(Z_\infty=(1+x_\infty)/2\) preserves strict nondegeneracy.

**4. Independent varying rule probabilities.** For independent Bernoulli rules, the series
\[
\sum_{n=1}^{\infty}\frac{\xi_n-p_n}{n}
\]
converges almost surely by the independent mean-zero series convergence theorem: its variance sum is at most \(\sum n^{-2}<\infty\). Thus the nonnegative series \(\sum\xi_n/n\) and \(\sum p_n/n\) have the same convergence/divergence status almost surely. Conditional on almost every rule realization, steps 1–3 apply, proving both claims. The logarithmic example follows from the integral test for \(\sum_{n\ge2}1/[n(\log n)^\theta]\). \(\square\)

## Verification
Run `python3 check.py` with Python 3 and no external dependencies. It enumerates all rule strings of lengths zero through six for five sets of initial urn counts and reinforcement parameters, computes exact conditional means and second moments using rational probabilities, and checks the closed recurrences. It additionally integrates over independently randomized rule strings with rational time-varying probabilities in three parameter sets. At package creation, the script returned **1,950 exact assertions passed**. Finite enumeration tests the algebra, not the infinite-series/martingale arguments; the latter are established above.

## Relationship to prior work
Alves and Rosales, *Friedman vs Pólya* (first arXiv posting 2025-02-24, arXiv:2502.16768), prove convergence to one half for **fixed positive** mixture probability. Shi, Yin, and Miao, *Central Limit Theorem for a Pólya-Friedman Mixed Urn Model* (2026-05-26, arXiv:2605.26669), study a **fixed** mixture parameter and its Gaussian fluctuations. Neither theorem directly covers vanishing or arbitrary nonhomogeneous mixing probabilities, much less the conditional limit-law dichotomy.

Gao and Aguech, *Multiple-drawing dynamic Friedman urns with opposite-reinforcement* (2023 online, DOI 10.1017/S0269964822000535), allow time-dependent additions under assumptions maintaining strict opposing reinforcement in the mean and obtain convergence to one half; that regime excludes the vanishing-strength opposing drift at issue here. Crimaldi, Louis, and Minelli, *Urn models with random multiple drawing and random addition* (arXiv:2102.06287; 2022 journal), permit random time-dependent **same-colour** amplification but do not include the opposite-colour additions here. The present proof is elementary martingale analysis; it does not claim a new general convergence principle or an explicit limiting distribution.

## Limitations
The sharp criterion requires *balanced* additions \(c=a+b\). No assertion is made for the unbalanced mixed urn or rule choices adaptive to observed colours. The finite-weight regime gives strict nondegeneracy, not absolute continuity, absence of atoms, an explicit limit density, or almost-sure separation of the limit from one half. The proof and code have not undergone an independent mathematical audit. The historical comparison does not exclude every possible earlier formulation under general stochastic-approximation theory; priority remains subject to external review.

## References
1. R. Alves and R. A. Rosales, *Friedman vs Pólya*, arXiv:2502.16768, first version 2025-02-24, https://arxiv.org/html/2502.16768v1.
2. J. Shi, Q. Yin, and Y. Miao, *Central Limit Theorem for a Pólya-Friedman Mixed Urn Model*, arXiv:2605.26669, 2026-05-26, https://arxiv.org/abs/2605.26669.
3. S. Gao and R. Aguech, *Multiple-drawing dynamic Friedman urns with opposite-reinforcement*, *Probability in the Engineering and Informational Sciences* 38 (2024), 115–129, first published online 2023-01-26, https://doi.org/10.1017/S0269964822000535.
4. I. Crimaldi, P.-Y. Louis, and I. G. Minelli, *Urn models with random multiple drawing and random addition*, arXiv:2102.06287, first version 2021-02-11, https://arxiv.org/abs/2102.06287.
