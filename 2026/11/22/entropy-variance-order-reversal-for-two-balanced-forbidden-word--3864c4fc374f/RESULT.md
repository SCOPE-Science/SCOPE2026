# Entropy–variance order reversal for two balanced forbidden-word shifts

## Finding

For each integer \(k\ge 2\), let \(X_k^{\mathrm{run}}\subset\{0,1\}^{\mathbb Z}\) be the shift forbidding the single block \(0^k1^k\), and let \(X_k^{\mathrm{alt}}\) forbid \((01)^k\). Write \(h_k^{\square}\) for their topological entropies. Draw \(W_n^{\square}\) uniformly from the length-\(n\) admissible language and put \(N_n^{\square}=\sum_{j=1}^n(W_n^{\square})_j\). The limits \(V_k^{\square}=\lim_{n\to\infty}\operatorname{Var}(N_n^{\square})/n\) exist, and, for every \(k\ge2\),

\[
 h_k^{\mathrm{run}}<h_k^{\mathrm{alt}},\qquad
 V_k^{\mathrm{run}}>V_k^{\mathrm{alt}}>\frac14.
\]

Both uniform finite-word laws have \(\mathbb E N_n^{\square}=n/2\) **exactly at every length**. Nonetheless the fluctuation strengths differ, and as \(k\to\infty\),

\[
\begin{aligned}
 V_k^{\mathrm{run}}&=\frac14+\frac{k}{2}4^{-k}+O(k^2 16^{-k}),\\
 V_k^{\mathrm{alt}}&=\frac14+\frac{3k-1}{8}4^{-k}+O(k^2 16^{-k}),\\
 V_k^{\mathrm{run}}-V_k^{\mathrm{alt}}&=\frac{k+1}{8}4^{-k}+O(k^2 16^{-k}),\\
 h_k^{\mathrm{alt}}-h_k^{\mathrm{run}}&=\frac14 4^{-k}+O(k16^{-k}).
\end{aligned}
\]

The entropy ordering is classical from overlap enumeration; the new result is the all-length variance ordering, including its explicit reversal relative to entropy and its asymptotic gap.

## Assumptions and scope

The shift is bilateral, with the natural left shift. A length-\(n\) word is admissible when it contains no occurrence of the indicated forbidden block. Both finite-state presentations are primitive: the prefix-matching automaton of either word can reach its empty-prefix state by a safe synchronizing continuation (for \((01)^k\), a long zero run followed by a long one run; for \(0^k1^k\), a long zero run, then \(1^{k-1}0\), then a long one run), and from the empty-prefix state every proper forbidden-word prefix is reachable. The empty-prefix state has a one-symbol self-loop. Thus standard Perron–Frobenius pressure and uniform-word asymptotics apply.

For a word \(w\), define its weighted avoidance series

\[
 G_w(z,t)=\sum_{n\ge0}\sum_{v\in\mathcal L_n(X_{\{w\}})}z^n e^{t\lvert v\rvert_1}.
\]

Its exponential-pressure function \(P_w(t)=\lim_{n\to\infty}n^{-1}\log\sum_{v\in\mathcal L_n} e^{t\lvert v\rvert_1}\) is analytic near \(t=0\), satisfies \(h_w=P_w(0)\), and \(V_w=P_w''(0)\). In particular no finite enumeration is used to extrapolate an infinite variance.

## Proof

**1. Exact weighted renewal identities.** The classical weighted border-polynomial identity for a single avoided word (Fact 2.9 of Bóna–Maga–Richey, building on Guibas–Odlyzko) is

\[
G_w(z,t)=\frac{C_w(z,t)}{(1-(1+e^t)z)C_w(z,t)+e^{kt}z^{2k}}
\]

for a balanced forbidden word of length \(2k\), where \(C_w\) enumerates its proper overlaps by shift. For \(w=0^k1^k\), no nonempty proper suffix equals a prefix, so \(C_w=1\). For \(w=(01)^k\), the proper self-overlap shifts are \(2,4,\ldots,2k-2\), each adding one 1 per two positions, so \(C_w=\sum_{j=0}^{k-1}e^{jt}z^{2j}\). These identities can also be checked directly by the Goulden–Jackson cluster recurrence; the bundled exact code compares their coefficient arrays against direct avoidance enumeration.

Put \(r(t)=e^t/(1+e^t)^2=1/(4\cosh^2(t/2))\) and \(q=(1+e^t)z\). Denote the pole parameters by \(q_{\mathrm{run}}(t)\) and \(q_{\mathrm{alt}}(t)\). Clearing the nonzero overlap factor gives

\[
q_{\mathrm{run}}-1=r^k q_{\mathrm{run}}^{2k},\qquad
q_{\mathrm{alt}}-1=r^k q_{\mathrm{alt}}^{2k+1}(1-rq_{\mathrm{alt}}).
\]

The relevant roots are the unique roots in \((1,1+2\cdot4^{-k})\) when \(t=0\), and continue analytically for small \(t\). Indeed \(a=4^{-k}\) obeys \(4ka\le1/2\), and the bounds \((1+2a)^{2k}\le e^{4ka}<2\) show the defining residuals have opposite signs at the interval endpoints. Their derivatives are positive there, since the bounds \((2k+1)a e^{4ka}<1\) hold for every \(k\ge2\). Primitivity identifies these smallest positive poles with the Perron pressures:

\[
P_{\square}(t)=\log(1+e^t)-\log q_{\square}(t).
\]

**2. First and second pressure derivatives.** Since \(r\) is even, \(q'_{\square}(0)=0\). Hence \(P'_{\square}(0)=1/2\), agreeing with the finite-length complement–reversal involution. Also \(r''(0)/r(0)=-1/2\). Write \(u_{\square}=q_{\square}(0)-1\), and \(b=q_{\mathrm{alt}}(0)/(4-q_{\mathrm{alt}}(0))\). Twice differentiating the two implicit equations and simplifying yields the exact formulas

\[
\begin{aligned}
V_k^{\mathrm{run}}&=\frac14+\frac{k u_{\mathrm{run}}}{2[1-(2k-1)u_{\mathrm{run}}]},\\
V_k^{\mathrm{alt}}&=\frac14+\frac{(k-b)u_{\mathrm{alt}}}{2[1-(2k-b)u_{\mathrm{alt}}]}.
\end{aligned}
\]

All denominators are positive by the monotonic pole equations. Since \(1<q_{\mathrm{alt}}<2\), we have \(0<b<1\le k\); therefore \(V_k^{\mathrm{alt}}>1/4\).

**3. Entropy order.** For \(1<q<2\), the factor \(q(1-q/4)=1-(q-2)^2/4\) is strictly below 1. Thus the alternating right-hand side in the pole equation is strictly smaller than the run right-hand side at the same \(q\). By strict monotonicity of the residuals on their relevant intervals, \(q_{\mathrm{alt}}(0)<q_{\mathrm{run}}(0)\). Since \(h_{\square}=\log2-\log q_{\square}(0)\), we get \(h_k^{\mathrm{run}}<h_k^{\mathrm{alt}}\).

**4. Variance order for all \(k\).** For \(k\ge8\) write \(a=4^{-k}\). The pole equations, the interval \(0<u_{\square}<2a\), and \(4ka<1/100\) give explicit estimates

\[
\begin{gathered}
 |u_{\mathrm{run}}-a|\le8ka^2,\qquad
 |u_{\mathrm{alt}}-3a/4|\le11ka^2,\qquad
 |b-1/3|\le a,\\
 \left|V_k^{\mathrm{run}}-\frac14-\frac{k}{2}a\right|\le10k^2a^2,\\
 \left|V_k^{\mathrm{alt}}-\frac14-\frac{3k-1}{8}a\right|\le10k^2a^2.
\end{gathered}
\]

For completeness, the first line follows by bounding \(q^{2k+1}\le e^{(2k+1)2a}\le1+10ka\), and inserting this in the two pole identities; also \(b-1/3=4u/[3(3-u)]\). The last two estimates follow by substituting the first line into the exact variance expressions and using the respective denominators at least \(1-4ka>0.99\). Consequently

\[
V_k^{\mathrm{run}}-V_k^{\mathrm{alt}}\ge
\frac{k+1}{8}a-20k^2a^2>0
\]

because \(160k^2 4^{-k}<k+1\) for all \(k\ge8\); the last inequality holds at 8 and improves thereafter. For each remaining \(2\le k\le7\), exact rational bisection of the two defining polynomials, followed by monotone rational interval evaluation of the variance formulas, gives disjoint intervals in the indicated order (see `check.py`):

| \(k\) | Certified lower bound on \(V_k^{\mathrm{run}}-V_k^{\mathrm{alt}}\) |
|---|---|
| 2 | 0.05280184 |
| 3 | 0.01015938 |
| 4 | 0.00266200 |
| 5 | 0.00075292 |
| 6 | 0.00021544 |
| 7 | 0.00006119 |

These decimal displays are deliberately rounded *down* from exact rational certificates. The code uses 44 dyadic bisections and performs all inequalities on rational numbers, not floating-point output.

**5. Asymptotics.** The first-line estimates in Step 4 inserted into the exact variance expressions give the stated variance expansions. The pole expansions \(q_{\mathrm{run}}(0)=1+a+O(ka^2)\) and \(q_{\mathrm{alt}}(0)=1+3a/4+O(ka^2)\) give \(h_k^{\mathrm{alt}}-h_k^{\mathrm{run}}=a/4+O(ka^2)\) via the logarithm. This proves the theorem.

## Verification

Run `python3 check.py` alongside this document; it requires only the Python standard library. It computes exact rational isolating intervals for the six small cases, proves nonoverlap of rational variance bounds, checks the explicit all-large-modulus inequality for 8 through 100 as a diagnostic (the proof establishes it for *every* modulus at least eight), and independently enumerates the complete binary weighted languages through length 13 for \(k=2,3,4\). The analytic steps are essential: finite calculations alone do not prove the infinite or all-modulus conclusions.

## Relationship to prior work

Guibas–Odlyzko's autocorrelation formulas and Chandgotia–Marcus–Richey–Wu's shift-theoretic treatment determine single-word avoidance counts and their topological entropies. The entropy inequality itself is a classical overlap consequence. Bóna–Maga–Richey (2026), Fact 2.9, supplies a two-variable border generating function and studies **first** derivatives (mean one-frequencies); their Fact 3.1 already covers complement–reversal symmetry and the equality of first moments for the length-four pair. This result uses that common framework but identifies a distinct **second-derivative** invariant and proves a strict, all-modulus inequality opposite the entropy order, with a precise large-modulus gap. Its own contribution is not the cluster identity, primitive SFT central limit theory, mean one-half, or the entropy order.

## Limitations

The comparison concerns these two canonical balanced forbidden-word families only; it does not order all balanced words, claim optimality among all forbidden patterns, or classify their full pressure functions. The variance is the linear growth coefficient for digit counts under *uniform admissible finite words*, equivalently the Green–Kubo variance for the unique maximal-entropy measure; it is not variance of hitting time or of occurrences of the forbidden pattern. Prior-literature priority remains subject to independently locating unforeseen equivalent fluctuation inequalities. No independent audit is claimed.

## References

1. M. Bóna, B. Maga, J. Richey, *Letter frequency in shifts of finite type with one forbidden word*, arXiv:2606.06655 (first public version 2026-06-04), https://arxiv.org/abs/2606.06655.
2. N. Chandgotia, B. Marcus, J. Richey, C. Wu, *Shifts of Finite Type Obtained by Forbidding a Single Pattern*, arXiv:2409.09024 (first public version 2024-09-13), https://arxiv.org/abs/2409.09024.
3. L. J. Guibas and A. M. Odlyzko, *String overlaps, pattern matching, and nontransitive games*, Journal of Combinatorial Theory, Series A **30** (1981), 183–208.
4. D. Lind and B. Marcus, *An Introduction to Symbolic Dynamics and Coding*, 2nd ed., Cambridge University Press, 2021.
