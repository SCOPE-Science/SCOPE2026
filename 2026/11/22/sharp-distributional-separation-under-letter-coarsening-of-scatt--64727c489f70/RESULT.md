# Sharp distributional separation under letter coarsening of scattered patterns

## Finding

Consider a uniformly random word \(X=X_1\cdots X_n\) over a fixed alphabet of size \(q\ge2\). For a fixed length-\(m\) pattern \(p\), \(m\ge2\), let \(Z_p\) be the number of *indexed scattered occurrences* of \(p\) in \(X\). Thus each increasing \(m\)-tuple of positions matching \(p\) contributes one, even when different tuples yield identical letters.

**Coarsening-and-threshold theorem.** Suppose \(p'=f(p)\) for a map of alphabet symbols \(f\), and the equality relation of \(p'\) properly contains that of \(p\). Define
\[
d=\min\{j-i:1\le i<j\le m,\ p_i\ne p_j,\ p'_i=p'_j\}.
\]
Then \(1\le d\le m-1\) and, for every \(n\ge0\),
\[
\mathbb E\!\left[t^{Z_p}\right]\le\mathbb E\!\left[t^{Z_{p'}}\right]\quad(t\ge1),\qquad
\mathbb E[Z_p^r]\le\mathbb E[Z_{p'}^r]\quad(r=2,3,\ldots).
\]
The two random variables have **exactly the same probability distribution** for \(n<m+d\). For \(n\ge m+d\), both inequalities are strict whenever \(t>1\) or \(r\ge2\), respectively. Thus \(m+d\) is the first host length at which the distributions separate, as well as the first at which their variances separate. The mean is always
\[
\mathbb E Z_p=\binom{n}{m} q^{-m}\quad(n\ge m),
\]
and zero for \(n<m\), regardless of the pattern.

**Sharp extrema.** Among all length-\(m\) patterns, the constant patterns uniquely maximize these positive higher moments and exponential moments (up to relabeling), once \(n\ge m+1\). When \(q\ge m\), the patterns whose \(m\) letters are pairwise distinct uniquely minimize the same quantities (up to relabeling) for \(n\ge2m-1\). The latter threshold is uniform in the pattern; individual noninjective patterns separate sooner, at \(m\) plus their shortest repeated-letter distance.

Two explicit finite second-moment formulas accompany this order. Put \(L=2m-k\). For \(n\ge m\), the constant-pattern value is
\[
\mathbb E Z_{\mathrm{const}}^2=\sum_{k=\max(0,2m-n)}^m\binom{n}{L}\frac{L!}{k!(m-k)!^2}\,q^{-L}.
\]
For \(q\ge m\), the injective-pattern value is
\[
\mathbb E Z_{\mathrm{inj}}^2=\sum_{k=\max(0,2m-n)}^m\binom{n}{L}\,[z^{m-k}](1-4z)^{-(k+1)/2}\,q^{-L}.
\]
Their corresponding variances are these quantities minus \(\binom{n}{m}^2q^{-2m}\). Both formulas include every boundary case \(n\ge m\), not only asymptotic regimes.

## Assumptions and scope

The letters \(X_i\) are mutually independent and **uniformly** distributed over the same alphabet, and \(f\) need not be injective or surjective. Only equalities among positions of each pattern matter; actual labels are immaterial by alphabet symmetry. For \(n<m\), both embedding counts vanish. The distributional equality and strict exponential-moment order are **not** a claim of ordinary stochastic dominance, convex order, or validity under arbitrary biased letter laws.

## Proof

For an increasing \(m\)-element subset \(S=(s_1<\cdots<s_m)\) of \([n]\), write \(I_S(p)=\mathbf1\{X_{s_i}=p_i\text{ for all }i\}\). Then \(Z_p=\sum_S I_S(p)\). If \(F\) is any finite family of distinct choices of \(S\), let \(U(F)\) be the union of their host positions. The joint expectation has the exact form
\[
\mathbb E\prod_{S\in F}I_S(p)=
\begin{cases}
q^{-|U(F)|},&\text{if all pattern letters assigned to each shared position agree},\\
0,&\text{otherwise}.
\end{cases}
\]
Applying \(f\) to the required letters never destroys a compatible family, and does not change the positive weight. For \(t\ge1\), expanding
\[
 t^{Z_p}=\prod_{S\in\binom{[n]}{m}}\left(1+(t-1)I_S(p)\right)
\]
shows the asserted exponential-moment inequality coefficientwise in \(t-1\). Expanding \(Z_p^r\) over ordered (possibly repeated) \(r\)-tuples of embeddings likewise proves each raw-moment inequality. A common first moment follows by linearity.

Next, every position of the \(i\)-th selected rank in an \(m\)-subset satisfies \(i\le s_i\le n-m+i\). If two embeddings assign ranks \(i\) and \(j\) to the same host position, necessarily \(|i-j|\le n-m\). Thus whenever \(n<m+d\), no newly identified pair of distinct original letters can be assigned to a shared host coordinate. All joint expectations in the preceding product expansion are therefore **equal** for \(p\) and \(p'\). Their probability generating polynomials are equal, hence their full laws agree.

For sharpness choose ranks \(i<j\) with \(j-i=d\), \(p_i\ne p_j\) and \(p'_i=p'_j\). Construct two embeddings in \(m+d\) host coordinates as follows: first share the ranks \(1,\ldots,i-1\); place the \(d\) ranks \(i,\ldots,j-1\) belonging only to the second embedding; use one shared coordinate for rank \(i\) in the first embedding and rank \(j\) in the second; place the \(d\) ranks \(i+1,\ldots,j\) belonging only to the first; finally share the ranks \(j+1,\ldots,m\). Each embedding uses exactly \(m\) coordinates. All shared rank assignments agree except the central conflict, which is incompatible for \(p\) but compatible for \(p'\). Consequently one pair term in the generating-polynomial expansion increases by \(q^{-(m+d)}\). For every longer host, append unused positions; all other differences remain nonnegative. Therefore the exponential-moment gap is positive at \(t>1\), and the raw-moment gap is positive at all integer orders \(r\ge2\) (repeat either member of this pair as necessary). Means coincide, so variances also separate at precisely this length.

To obtain the extrema, merge every alphabet symbol into one: any nonconstant pattern has adjacent unequal letters, giving \(d=1\). For the other direction, when \(q\ge m\), begin with an all-distinct pattern and map its symbols to the desired pattern. Any noninjective target has a repeated pair of ranks separated by at most \(m-1\). Applying the strict threshold gives uniqueness and the specified ranges.

Finally, expand the second moment as a sum over ordered pairs of embeddings. Let \(k\) be their number of shared selected host coordinates, and \(L=2m-k\) their union size. There are \(\binom{n}{L}\) choices of host positions for the union, and each compatible pair contributes \(q^{-L}\). For a constant pattern every ordered pair is compatible: the union is partitioned into \(k\) shared coordinates, \(m-k\) first-only and \(m-k\) second-only coordinates, in \(L!/(k!(m-k)!^2)\) ways. For an injective pattern, a shared coordinate must have the **same pattern rank** in both embeddings. Between consecutive shared coordinates (also before the first and after the last), each gap must contain equally many first-only and second-only coordinates, say \(r\), which can be interleaved in \(\binom{2r}{r}\) ways. There are \(k+1\) gaps and \(\sum r=m-k\); their product generating function is \((\sum_{r\ge0}\binom{2r}{r} z^r)^{k+1}=(1-4z)^{-(k+1)/2}\), giving the claimed formula. This exhausts all possible pairs, with no computational inference used for the infinite claims.

## Verification

The standalone `verification.py` independently enumerates host words and embeddings, computes raw moments as rational numbers, and separately computes them from pair-compatibility constraints. It checks 310 host-pattern distribution instances, 310 independent second-moment comparisons, 160 extremal formula cases, and 3,192 coarsening threshold instances, including third moments. An explicit delayed-divergence example is \(p=0120\) versus the injective \(0123\), \(q=4\), \(m=4\): the laws coincide through \(n=6\), while their second moments first differ by \(1/8192\) at \(n=7\). The exact terminal output is preserved in `verification_output.txt`. These finite checks test the definitions and formulas; the preceding argument establishes the all-length results.

## Relationship to prior work

Flajolet, Szpankowski and Vallée (2006) developed general mean, variance, generating-function and limit-law machinery for subsequence occurrences in random texts. Janson and Szpankowski (2020/2021) investigated the variable-pattern-length asymptotic law using projection methods. Jeong and Pernice (first available April 8, 2026) study a random-subsequence embedding partition function with jointly random patterns and hosts, including annealed and planted free energies. A more specific previously reported classification compares the variances of all binary four-letter patterns. These works motivate the fixed-pattern question but the examined statements do not furnish the general **coarsening poset monotonicity with a sharp first-law-separation length** given here. The existing pattern-by-pattern second-moment machinery is not claimed as novel in itself. An equivalent implicit consequence of more general hidden-pattern theory is a residual priority risk.

## Limitations

The result concerns uniform independent hosts and indexed scattered embeddings. It gives a hierarchy of positive integer and exponential moments, not an arbitrary convex-order or stochastic-order comparison. The special injective minimum requires \(q\ge m\); no minimizer is classified for smaller alphabets. Scientific priority is assessed against inspected sources and may be revised if an earlier equivalent finite-law monotonicity theorem is located. Independent audit has not been performed.

## References

1. R. Jeong and F. Pernice, *The Random Subsequence Model and Uniform Codes for the Deletion Channel*, arXiv:2604.07234v1, publicly available April 8, 2026. https://arxiv.org/html/2604.07234
2. P. Flajolet, W. Szpankowski and B. Vallée, *Hidden Word Statistics*, Journal of the ACM 53 (2006), 147–183. https://doi.org/10.1145/1120582.1120586
3. S. Janson and W. Szpankowski, *Hidden Words Statistics for Large Patterns*, arXiv:2003.09584v1 (March 21, 2020); Electronic Journal of Combinatorics 28 (2021), P2.36. https://arxiv.org/abs/2003.09584
4. *Exact variance hierarchy for all binary four-symbol subsequence patterns*, public result dated November 2, 2026. A restricted finite binary comparison; no attribution of the present general theorem is intended.
