# Multipartite random-priority peaks: exact colored-run laws and a growing-palette Gaussian limit

## Finding

A random-priority local-maximum statistic on a complete multipartite graph admits a finite-sample independent-run factorization conditional on its initial color counts. This yields a fixed-palette non-Gaussian limit and, when the number of initial colors grows, a Gaussian limit even though the graph has unbounded degree.

**Finite-sample theorem.** Fix integers \(r\geq 3\), \(k\geq1\), positive integers \(n_1,\ldots,n_r\), and let \(G=K_{n_1,\ldots,n_r}\) have \(n=\sum_i n_i\) vertices. Assign independent uniform initial colors from \(\{1,\ldots,k\}\) and independent distinct uniform random priorities. A peak is a vertex with higher priority than all of its neighbors of the same initial color. Let \(S\) be the number of peaks, and let \(m_{ic}\) be the number of vertices of initial color \(c\) in graph part \(i\); set \(M_c=\sum_i m_{ic}\). Conditional on all \(m_{ic}\), the random contributions \(U_c\) to \(S=\sum_{c=1}^k U_c\) are independent. For integers \(1\leq\ell\leq M_c\),

\[
\Pr(U_c\geq\ell\mid(m_{ic}))=
\frac{\sum_{i=1}^r {m_{ic}\choose\ell}}{{M_c\choose\ell}},
\]

and \(U_c=0\) if \(M_c=0\). Equivalently, its conditional probability mass is the difference of consecutive displayed tails. The exact unconditional mean is

\[
\mathbb E S=\sum_{i=1}^r\frac{n_i k}{n-n_i+1}\left[1-\left(1-\frac1k\right)^{n-n_i+1}\right].
\]

**Fixed-palette and growing-palette theorem.** Fix \(r\geq3\), let \(n\to\infty\), and suppose \(n_i/n\to p_i>0\), with \(\sum_i p_i=1\). For fixed \(k\), \(S\) converges in distribution to a sum of \(k\) independent variables \(G\), where

\[
\Pr(G\geq j)=\sum_{i=1}^r p_i^j\quad(j\geq1),\qquad
\mathbb E z^G=\sum_{i=1}^r\frac{(1-p_i)p_i z}{1-p_i z}.
\]

Thus \(G\) is a mixture of positive geometric variables indexed by the graph part of its first ranked vertex. For balanced parts, \(G\) has geometric success parameter \((r-1)/r\) and the limit is a sum of \(k\) such variables.

Now let the number of initial colors vary with \(n\) so that \(k=k_n\to\infty\) and \(k_n\log n=o(n)\). Define

\[
\mu=\sum_{i=1}^r\frac{p_i}{1-p_i},\qquad
\sigma^2=\sum_{i=1}^r\frac{p_i(1+p_i)}{(1-p_i)^2}-\mu^2>0.
\]

Then

\[
\frac{S-\mathbb E S}{\sqrt{k_n}}\ \Longrightarrow\ N(0,\sigma^2),\qquad
\frac{\operatorname{Var}(S)}{k_n}\longrightarrow\sigma^2.
\]

In the classical random-central-daemon self-stabilizing coloring procedure with a palette of at least \(\Delta(G)+1\) colors, the recoloring count \(T\) has the same law as \(n-S\). Accordingly, the displayed assertions also determine its exact finite mean and asymptotic laws, with the sign reversed on Gaussian fluctuations when \(S\) is replaced by \(T\).

## Assumptions and scope

The graph has \(r\geq3\) nonempty independent parts and every pair of vertices in distinct parts is adjacent. Initial colors are iid uniform with \(k\) a positive integer. Random priorities are iid continuous, independent of colors. In the graph process, all initial colors belong to the allowed palette, and its size \(q\) satisfies \(q\geq \max\{k,\Delta(G)+1\}\); hence an enabled vertex can always recolor to an unused neighboring color and becomes permanently non-conflicting. The known equivalence of the random central daemon's recoloring count to the priority peak count is used rather than claimed anew.

Only fixed \(r\) with all limiting proportions strictly positive is assumed for the limit theorems. The growing-color assertion is proved in the stated sufficient regime \(k_n\log n=o(n)\); no optimality of this boundary is asserted. All stochastic statements use the full randomness of colors and priorities.

## Proof

**1. The initial-run identity.** Fix the initial colors and inspect the vertices of one color \(c\) in *decreasing* order of priority. A vertex in part \(i\) is adjacent to every same-colored vertex in every other part, and to none in its own part. The first vertex is a peak. Every following vertex of the same part is a peak until a vertex of another part appears; after that, each later vertex has an earlier, higher-priority same-colored neighbor (the first vertex or the first different-part vertex). Consequently \(U_c\) is precisely the length of the maximal initial monochromatic *part* run. Within color \(c\) all orderings of its \(M_c\) vertices are equiprobable. The probability that the first \(\ell\) are all in part \(i\) is \((m_{ic})_{\underline\ell}/(M_c)_{\underline\ell}\); summing over disjoint part choices gives the stated tail. Restricted priority permutations in distinct color classes are independent conditional on the colors (and therefore conditional on color counts), proving factorization. For \(M_c=0\), \(U_c=0\).

The exact conditional expectation, also useful below, is

\[
A(m)=\mathbb E[S\mid m]=\sum_{c=1}^k g(m_{1c},\ldots,m_{rc}),\qquad
g(a_1,\ldots,a_r)=\sum_{i=1}^r\frac{a_i}{M-a_i+1},\quad M=\sum_i a_i.
\]

For a fixed part \(i\), if \(m_i\) denotes the number of occurrences of that part in a random \(M\)-element part word, summing the run-tail hypergeometric probabilities gives \(m_i/(M-m_i+1)\), equivalently the expected number before the first non-\(i\) entry.

**2. Exact unconditional mean.** For a given vertex in part \(i\), the number \(B\) of its same-colored neighbors is \(\operatorname{Bin}(n-n_i,1/k)\). Its priority is highest among these \(B+1\) iid continuous priorities with probability \(1/(B+1)\). The beta integral \(1/(b+1)=\int_0^1 t^b\,dt\) yields

\[
\mathbb E\frac1{B+1}=\int_0^1\left(1-\frac1k+\frac tk\right)^{n-n_i}dt
=\frac{k}{n-n_i+1}\left[1-\left(1-\frac1k\right)^{n-n_i+1}\right].
\]

Summation over vertices proves the mean formula, including \(k=1\).

**3. Fixed-palette limit.** When \(k\) is fixed, the law of large numbers gives \(m_{ic}/n\to p_i/k\) simultaneously in probability. For each fixed \(\ell\), conditional on those counts the run tail tends to \(\sum_i p_i^\ell\). The tails of each \(U_c\) are uniformly tight because all limiting part proportions are strictly below one. The conditional joint probability generating function is the product of its \(k\) color-factor pgfs; its limit is the stated product of iid geometric-mixture pgfs. For a geometric variable supported on positive integers with success probability \(1-p_i\), its tail is \(p_i^{\ell-1}\); weighting by first-part probability \(p_i\) gives \(\sum_i p_i^\ell\). Its variance is the displayed \(\sigma^2\), positive because a positive mixture of nondegenerate geometric variables has positive variance.

**4. Growing-palette concentration of counts.** Put \(k=k_n\) and \(b_n=n/k\), so \(b_n/\log n\to\infty\). Choose \(\varepsilon_n=(\log n/b_n)^{1/4}\to0\). Each \(m_{ic}\sim\operatorname{Bin}(n_i,1/k)\) has mean \(n_i/k\). Chernoff's inequality followed by a union bound over \(rk\) cells gives a good event \(E_n\) on which all cell counts differ from their expectations by at most the relative fraction \(\varepsilon_n\), with \(\Pr(E_n^c)=o(n^{-A})\) for every fixed \(A>0\). In fact its exponential factor is \(\exp(-c\sqrt{b_n\log n})\), which dominates all polynomial factors because \(b_n/\log n\to\infty\). On \(E_n\), uniformly over colors, their within-color part proportions converge to \((p_i)_i\); their maxima are bounded above by a constant \(\rho<1\); all color totals are at least a constant times \(b_n\).

**5. Conditional Gaussian fluctuations.** For any color and every \(j\ge1\), the run survival probability on \(E_n\) is at most \(r\rho^j\). Consequently all conditional third moments are uniformly bounded, and each \(U_c\)'s conditional mean and variance converge uniformly to \(\mu\) and \(\sigma^2\), respectively, by dominated convergence of the discrete tail sums. Conditioned on counts on \(E_n\), the \(U_c\)'s are independent. Their variance sum is \(k\sigma^2(1+o(1))\) and their total centered third absolute moment is \(O(k)\). The Berry–Esseen inequality for independent nonidentical summands therefore gives, uniformly on \(E_n\),

\[
\frac{S-A(m)}{\sqrt{k}}\Longrightarrow N(0,\sigma^2).
\]

**6. Random centering is negligible.** On \(E_n\), each denominator \(M_c-m_{ic}+1\) in \(g\) is bounded below by a constant times \(b_n\). Differentiate the explicit rational function \(g\) with respect to each nonnegative cell argument: each partial derivative is bounded in absolute value by \(C/b_n=Ck/n\) along the segment between any two count vectors satisfying the good-event bounds. Two initial-color assignments at Hamming distance \(d\) change at most \(2d\) count entries in total. Therefore the function \(A\) restricted to the set of good color assignments is \(2Ck/n\)-Lipschitz in Hamming distance. Extend this Lipschitz function to all color assignments by the elementary McShane infimum formula and clip it to \([0,n]\), without changing it on the good set. The Efron–Stein bounded-difference inequality yields variance at most \(C' n(k/n)^2=O(k^2/n)\) for the extension. Since the original \(A\) and its clipped extension are both in \([0,n]\) and disagree only on an event of superpolynomially small probability,

\[
\operatorname{Var}(A)=O(k^2/n)+o(1)=o(k).
\]

Thus \((A-\mathbb EA)/\sqrt{k}\to0\) in probability. Combining this with conditional Berry–Esseen and \(\mathbb EA=\mathbb ES\) proves the stated normal convergence. Finally, conditional variances satisfy \(\mathbb E[\operatorname{Var}(S\mid m)]/k\to\sigma^2\): on \(E_n\) this follows uniformly from step 5, while on \(E_n^c\) its total is bounded by \(n^2\) and the event is superpolynomially small. Apply the total-variance identity and step 6 to obtain \(\operatorname{Var}(S)/k\to\sigma^2\).

**7. Algorithmic interpretation.** The random-priority peak/recoloring equivalence for the specified central daemon is established in the motivating reference. All the probabilistic results above apply to its exact peak count, so \(T=n-S\) inherits the stated laws without any additional stochastic assumptions.

## Verification

The standalone pure-Python `check.py` enumerates random orderings and named initial color assignments on six small complete multipartite part profiles (including a three-part graph), checks every finite conditional distribution against the exact survival-convolution formula using rational arithmetic, and independently checks the mean identity and conditional mean identity. Run `python3 check.py` with Python 3.10 or later; no third-party modules or external files are required. Finite enumeration confirms finite cases only. Steps 3–6, particularly the triangular-array limit, depend on the written analytical estimates rather than simulation or finite checks.

## Relationship to prior work

De Panafieu, Mathieu, Potop-Butucaru and Tixeuil (2026), Section 2 and Lemma 1, provide the general peak/recoloring equivalence, all-graph mean and variance statements, and Section 5.4/Proposition 9 gives a bipartite Erdős–Rényi generating function and a fixed-palette limit. In the complete-bipartite case this implies parts of the fixed-palette result here; none of those ingredients is claimed as new. The focus here is the **exact color-count factorization on multipartite graphs with three or more parts and the growing-palette Gaussian regime** with its explicit composition-dependent variance. Classical normal approximation for local maxima (Baldi–Rinott–Stein, 1989) treats random rankings on graphs; its accessible published result does not itself contain the random-color partitioned growing-palette theorem. A separate published random-greedy maximal independent-set result on complete multipartite graphs describes a sequential selection problem rather than the present nonsequential local-maximum count.

## Limitations

The result assumes complete adjacency between parts, independent uniform colors, independent continuous priorities, fixed number of parts, and positive asymptotic proportions. It does not establish a general graph theorem, a sharp boundary for how fast the palette can grow, or normal convergence for palettes of order \(n\). The novelty comparison is based on accessible inspected sources and cannot exclude every older equivalent result. Independent mathematical assessment has not been performed.

## References

1. É. de Panafieu, F. Mathieu, M. Gradinariu Potop-Butucaru, and S. Tixeuil, *The Exact Stabilization Time of Self-Stabilizing Coloring: Mean, Variance, and Distribution*, arXiv:2611.17989v1, 13 November 2026. https://arxiv.org/abs/2611.17989 ; primary PDF https://arxiv.org/pdf/2611.17989 .
2. P. Baldi, Y. Rinott, and C. Stein, *On the Distribution of the Number of Local Minima of a Random Function on a Graph*, Neural Information Processing Systems, 1989, pp. 727–732. https://papers.neurips.cc/paper_files/paper/1989/file/d947bf06a885db0d477d707121934ff8-Paper.pdf .
3. P. Baldi and Y. Rinott, *Asymptotic Normality of Some Graph-Related Statistics*, Journal of Applied Probability **26** (1989), 171–175. https://doi.org/10.2307/3214327 .
