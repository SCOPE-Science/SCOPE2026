# Sharp rare directed-star probabilities and a mean–typicality split in high-dimensional cube orders

## Finding
Fix any integer \(r\ge2\), let \(X_1,\ldots,X_n\) be independent uniform points in \([0,1]^{d_n}\), and write \(X_i\preceq X_j\) if every coordinate of \(X_i\) is at most the corresponding coordinate of \(X_j\). Define the directed domination outdegree \(D_i=\#\{j\ne i:X_i\preceq X_j\}\) and \(H_{n,r}=\{\max_iD_i\ge r\}\). For an integer dimension sequence \(d_n\) satisfying \(d_n/\log n\to c\in(e,r+1)\), the sharp equivalent is

\[
\Pr(H_{n,r})\sim \frac{\Gamma(r+1-c)}{(c-1)\Gamma(r)}\,\frac{(\log n)^{d_n-1}}{\Gamma(d_n)}.
\]

The exact expected number \(W_{n,r}=\sum_i\binom{D_i}{r}\) of directed \(r\)-stars is

\[
\mathbb E W_{n,r}=n\binom{n-1}{r}(r+1)^{-d_n}.
\]

Consequently, for every \(e<c<(r+1)/\log(r+1)\), one has \(\Pr(W_{n,r}>0)\to0\) while \(\mathbb EW_{n,r}\to\infty\). The interval is nonempty for every integer \(r\ge2\). The rarity exponent is \(\lim_{n\to\infty}\log\Pr(H_{n,r})/\log n=c(1-\log c)<0\).

## Assumptions and scope
The sampling coordinates are mutually independent and continuous uniform; there are exactly \(n\) sample points; the partial order is coordinatewise; ties have probability zero. The integer \(r\ge2\) is fixed (not growing with \(n\)). The dimension satisfies only \(d_n/\log n\to c\in(e,r+1)\); no second-order restriction is imposed. The result concerns the probability of *at least one* point dominating \(r\) others and does not describe all higher-degree tail regimes, the boundary cases \(c=e\) or \(c=r+1\), or the law conditioned on the rare event.

## Proof
Write \(L=\log n\) and \(Z_i=\prod_{a=1}^{d_n}(1-X_{ia})\). Conditionally on \(X_i\), the outdegree \(D_i\) has the binomial distribution \(\operatorname{Bin}(n-1,Z_i)\). Since the random variables \(-\log(1-X_{ia})\) are independent unit exponentials,
\[
Y_i=-\log Z_i\sim\operatorname{Gamma}(d_n,\text{rate }1),\qquad f_d(y)=\frac{y^{d-1}e^{-y}}{\Gamma(d)}\mathbf1_{\{y>0\}}.
\]
Let \(q_{n,r}(s)\) be the probability that a binomial variable with \(n-1\) trials and success probability \(e^{-s}/n\) is at least \(r\), for \(s>-L\) (at the endpoint the probability is interpreted by continuity). For each fixed real \(s\),
\[
q_{n,r}(s)\longrightarrow q_r(e^{-s}),\qquad q_r(t)=1-e^{-t}\sum_{j=0}^{r-1}\frac{t^j}{j!}.
\]
Moreover \(0\le q_{n,r}(s)\le\min\{1,e^{-rs}/r!\}\) by the factorial-moment/union bound for a binomial variable. For \(s>-L\), the exact Gamma-density ratio is
\[
\frac{f_{d_n}(L+s)}{f_{d_n}(L)}=(1+s/L)^{d_n-1}e^{-s}\le\exp\big(((d_n-1)/L-1)s\big).
\]
For negative \(s\) the right side has an integrable exponential envelope because \(c>1\); for positive \(s\), multiplication by the factorial-moment bound yields an integrable envelope because \(c<r+1\). Dominated convergence therefore gives, for \(U_n=\sum_{i=1}^n\mathbf1_{\{D_i\ge r\}}\),
\[
\frac{\mathbb EU_n}{n f_{d_n}(L)}\to\int_{-\infty}^{\infty}e^{(c-1)s}q_r(e^{-s})\,ds.
\]
Substitute \(t=e^{-s}\). The integral is \(\int_0^\infty t^{-c}q_r(t)\,dt\). Integration by parts is valid because \(1<c<r+1\), and using \(q_r'(t)=e^{-t}t^{r-1}/\Gamma(r)\) gives
\[
I_{r,c}=\frac{1}{c-1}\int_0^\infty t^{1-c}q_r'(t)\,dt
=\frac{\Gamma(r+1-c)}{(c-1)\Gamma(r)}.
\]

It remains to replace the mean number of qualifying vertices by the probability of existence; dependence among the domination events cannot be ignored globally. For fixed \(K>0\), let \(A_{n,K}\) be the vertices satisfying \(|Y_i-L|\le K\), and let \(U_{n,K}\) count qualifying vertices in this set. The indicators of \(i\in A_{n,K}\) are independent, and their total \(M_{n,K}\) is binomial with \(\mathbb EM_{n,K}=n\int_{L-K}^{L+K}f_{d_n}(y)\,dy=O_K(n f_{d_n}(L))\). Stirling's formula yields
\[
\log(nf_{d_n}(L))=d_n\{1-\log(d_n/L)\}+O(\log L)=c(1-\log c)L+o(L),
\]
which tends to \(-\infty\) since \(c>e\). Since \(U_{n,K}\le M_{n,K}\),
\[
0\le\mathbb EU_{n,K}-\Pr(U_{n,K}>0)\le\mathbb E\binom{M_{n,K}}2=O_K((nf_{d_n}(L))^2)=o(nf_{d_n}(L)).
\]
The same dominated-convergence envelopes above show that \(\mathbb E(U_n-U_{n,K})/(nf_{d_n}(L))\) becomes arbitrarily small as \(K\to\infty\). By Markov's inequality the existence probabilities differ by at most this expectation. Taking \(n\to\infty\) then \(K\to\infty\) proves \(\Pr(U_n>0)\sim I_{r,c}nf_{d_n}(L)\). The exact cancellation \(n f_{d_n}(\log n)=(\log n)^{d_n-1}/\Gamma(d_n)\) proves the displayed equivalent.

For the expected star count, \(\Pr(X_i\preceq X_{j_1},\ldots,X_{j_r})=(r+1)^{-d_n}\): independently in each coordinate, the distinguished point is the minimum among \(r+1\) continuous iid values with probability \(1/(r+1)\). Sum over all distinguished centers and unordered choices of \(r\) leaves. As \(d_n/\log n\to c\), the expectation is \(n^{r+1-c\log(r+1)+o(1)}/r!\); it diverges for \(c<(r+1)/\log(r+1)\), while the sharp probability tends to zero for \(c>e\). Finally \(x/\log x\) has its unique positive minimum \(e\) at \(x=e\), so the claimed nonempty interval follows for integers \(r+1\ge3\).

## Verification
Run `python check.py` using Python 3 standard library. It exhaustively enumerates coordinate rank permutations to confirm the finite exact star expectation for small samples, verifies an independently expanded finite binomial-tail identity in rational arithmetic, and numerically compares the integral constant with the Gamma expression for five parameters. A successful run reports `PASS 203 finite exact / integral checks`. Finite checks are diagnostics and do not replace the dominated-convergence or probability-versus-expectation argument.

## Relationship to prior work
Bhattacharjee, Ilienko, Jin and Molchanov (2026), arXiv:2611.01096v1, study the count of points that are dominated by at least one other point and show multiple fluctuation regimes in growing dimension. Their full text treats non-Pareto counts, not the sharp probability of an \(r\)-fold directed domination center. Bollobás and Brightwell (1995), *Random high-dimensional orders*, give a classical threshold for vertices of fixed degree in high-dimensional random partial orders; the *threshold* is not claimed new. The present statement instead fixes the rare side of a directed-degree event and determines an explicit relative-error sharp equivalent (and a mismatch between the mean star count and its existence probability). The 1995 full text could not be accessed in this research inspection, so unverified overlap beyond its available abstract remains a priority risk. Existing comparison work on Pareto-frontier/comparability covariance addresses different count statistics and does not imply this rare-event equivalent.

## Limitations
No uniqueness or priority claim is established independently. The older fixed-degree literature was inspected at the abstract level only because its full text was unavailable; an unpublished or uninspected sharp asymptotic remains possible. The result uses fixed \(r\), uniform product sampling, and strictly interior \(e<c<r+1\). It does not assert Poisson independence of directed-star events or a limit at either boundary.

## References
- Bhattacharjee, C., Ilienko, A., Jin, B., and Molchanov, I. (2026). *From Gaussian to stable and back: Non-Pareto points in growing dimension*. arXiv:2611.01096v1, https://arxiv.org/html/2611.01096v1 (first public version October 31, 2026; primary MSC2020 60D05).
- Bollobás, B., and Brightwell, G. (1995). *Random high-dimensional orders*. Advances in Applied Probability 27(1), 161–184. https://doi.org/10.2307/1428102.
