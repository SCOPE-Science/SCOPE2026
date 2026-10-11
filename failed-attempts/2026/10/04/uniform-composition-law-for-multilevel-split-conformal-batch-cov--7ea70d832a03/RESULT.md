# Uniform-composition law for multilevel split-conformal batch coverage
## Finding
Let \(S_1,\ldots,S_n\) be the calibration scores and let \(S_{n+1},\ldots,S_{n+m}\) be a future batch. Assume that, after conditioning on the proper-training information used to construct the score, the whole score sequence is exchangeable and almost surely tie-free. Write the ordered calibration scores as \(S_{(1)}<\cdots<S_{(n)}\).

For \(h=1,\ldots,n+1\), let \(K_h\) count future scores in the \(h\)-th gap cut out by the calibration order statistics: below \(S_{(1)}\), between successive calibration scores, or above \(S_{(n)}\). Then
\[
(K_1,\ldots,K_{n+1})
\]
is exactly uniform over all weak compositions of \(m\) into \(n+1\) parts. Thus every composition has probability
\[
\binom{m+n}{n}^{-1}.
\]

More generally, choose distinct calibration ranks \(1\le b_1<\cdots<b_r\le n\), put \(b_0=0\), \(b_{r+1}=n+1\), and define
\[
a_h=b_h-b_{h-1},\qquad h=1,\ldots,r+1.
\]
If \(G_h\) is the number of future scores in the block of fine gaps associated with \(a_h\), then
\[
(G_1,\ldots,G_{r+1})\sim\operatorname{DirichletMultinomial}(m;a_1,\ldots,a_{r+1}).
\]
In particular,
\[
\Pr(G_1=g_1,\ldots,G_{r+1}=g_{r+1})
=
\frac{m!}{\prod_h g_h!}\frac{\Gamma(n+1)}{\Gamma(n+m+1)}
\prod_h\frac{\Gamma(a_h+g_h)}{\Gamma(a_h)}.
\]

The empirical coverage at calibration rank \(b_j\) is
\[
C_{m,j}=\frac{1}{m}\sum_{h=1}^{j}G_h.
\]
Writing \(p_j=b_j/(n+1)\), for \(j\le \ell\),
\[
\mathbb E[C_{m,j}]=p_j,
\qquad
\operatorname{Cov}(C_{m,j},C_{m,\ell})
=
\frac{m+n+1}{m(n+2)}p_j(1-p_\ell).
\]
Hence the usual one-level beta-binomial law is a marginal of a complete multilevel finite-sample law.

For the full rank grid, define \(T_b=K_1+\cdots+K_b=mC_{m,b}\). Given arbitrary integer bands \(L_b\le T_b\le U_b\), their simultaneous probability can be evaluated exactly in \(O(nm)\) arithmetic operations. Set \(d_0(0)=1\), \(d_0(s)=0\) for \(s>0\), and for \(b=1,\ldots,n\),
\[
d_b(s)=\mathbf 1\{L_b\le s\le U_b\}\sum_{t=0}^{s}d_{b-1}(t),\qquad 0\le s\le m.
\]
The number of admissible weak compositions is \(\sum_{s=0}^{m}d_n(s)\), so the exact simultaneous-band probability is
\[
\frac{\sum_{s=0}^{m}d_n(s)}{\binom{m+n}{n}}.
\]
Each row of the recurrence is computed from prefix sums, giving the stated \(O(nm)\) cost.

## Assumptions and scope
The statement concerns ordinary split conformal prediction after the proper-training stage has fixed the scoring rule. The required assumptions are exchangeability of the calibration-plus-future score sequence and almost-sure absence of ties. Random tie-breaking can be used only if it preserves exchangeability. Rank thresholds must be fixed functions of the calibration size and desired nominal levels; if several nominal levels map to the same calibration rank, they represent the same prediction set and should be collapsed before applying the multilevel formula.

The result is distribution-free within those assumptions. It does not cover covariate shift, weighted exchangeability, adaptive reuse of future labels to change the score, or dependent time-series settings that break exchangeability.

## Proof
Because the \(n+m\) scores are exchangeable and tie-free, their labeled total ordering is uniform over all \((n+m)!\) permutations. Forget the identities within the calibration labels and within the future labels, retaining only whether each location in the total score order is calibration or future. Every binary interleaving with \(n\) calibration symbols and \(m\) future symbols is induced by exactly \(n!m!\) labeled permutations. Therefore the \(\binom{n+m}{n}\) calibration/future interleavings are equiprobable.

There is a bijection between such interleavings and weak compositions \((K_1,\ldots,K_{n+1})\) of \(m\): \(K_1\) is the number of future symbols before the first calibration symbol, \(K_h\) for \(2\le h\le n\) is the number between the \((h-1)\)-st and \(h\)-th calibration symbols, and \(K_{n+1}\) is the number after the last calibration symbol. This proves the uniform-composition law.

Now group consecutive fine gaps into \(r+1\) blocks of sizes \(a_1,\ldots,a_{r+1}\). For fixed block totals \(g_1,\ldots,g_{r+1}\), stars-and-bars gives
\[
\prod_{h=1}^{r+1}\binom{g_h+a_h-1}{a_h-1}
\]
fine compositions with those totals. Dividing by \(\binom{m+n}{n}\) and simplifying factorials yields exactly the displayed Dirichlet-multinomial mass function.

The mean and covariance formulas are the standard first two moments of that Dirichlet-multinomial law after aggregating the first \(j\) and first \(\ell\) blocks. Finally, the dynamic program counts fine compositions by their successive prefix sums. If a valid prefix of length \(b-1\) has total \(t\le s\), there is exactly one choice \(K_b=s-t\ge0\) that extends it to total \(s\). Summing over \(t\) gives the recurrence, and the last gap is then forced to be \(m-s\).

## Verification
The accompanying `verify.py` uses only the Python standard library and exact rational arithmetic. It exhaustively enumerates all \(7!\) labeled score orderings for \(n=4\), \(m=3\), verifies that every one of the \(\binom{7}{4}=35\) fine-gap compositions occurs equally often, checks the aggregated Dirichlet-multinomial law at ranks \((1,3)\), verifies the cross-level covariance \(8/225\), and compares the \(O(nm)\) band dynamic program with brute-force composition enumeration on a separate finite case.

Run:

`python3 verify.py`

The expected first output line is `VERIFY_OK`.

## Relationship to prior work
Marques (arXiv:2303.02770) proves the exact beta-binomial law for empirical coverage at one split-conformal nominal level and derives its beta limit. Its proof explicitly uses the Pólya-urn-style predictive probability \((b+k)/(m+n+1)\). The present finding identifies the full calibration-gap occupancy vector, from which all nominal levels can be read jointly; the one-level beta-binomial law is recovered by summing the first \(b\) fine gaps.

Hulsman (arXiv:2210.14735) relates split conformal prediction to classical tolerance regions and beta-distributed conditional coverage. Gupta, Kuchibhotla, and Ramdas (arXiv:1910.10562) formulate conformal prediction through nested sets. These works motivate the order-statistic and nested-set viewpoint, but the inspected text did not state the finite joint multilevel Dirichlet-multinomial law, the uniform weak-composition representation, or the exact simultaneous-band dynamic program above.

The combinatorial and Dirichlet-multinomial ingredients themselves are classical. The contribution claimed here is their exact identification with the full split-conformal batch coverage curve and the resulting finite-sample simultaneous-band evaluator, not priority for those classical probability distributions.

## Limitations
The originality search cannot exclude an equivalent theorem hidden in older multivariate tolerance-region or order-statistics literature under different terminology. This is a residual literature risk, not a mathematical gap in the proof. The result also depends critically on exchangeability and tie-free scores; without them, the uniform interleaving argument can fail.

The dynamic program evaluates bands whose boundaries are integer constraints on the empirical counts. Real-valued coverage bands must first be converted to the corresponding integer lower and upper bounds with explicit floor/ceiling choices.

## References
1. Paulo C. Marques F., *Universal distribution of the empirical coverage in split conformal prediction*, arXiv:2303.02770, first posted 2023-03-05.
2. Roel Hulsman, *Distribution-Free Finite-Sample Guarantees and Split Conformal Prediction*, arXiv:2210.14735, first posted 2022-10-26.
3. Chirag Gupta, Arun K. Kuchibhotla, and Aaditya K. Ramdas, *Nested conformal prediction and quantile out-of-bag ensemble methods*, arXiv:1910.10562, first posted 2019-10-23.
