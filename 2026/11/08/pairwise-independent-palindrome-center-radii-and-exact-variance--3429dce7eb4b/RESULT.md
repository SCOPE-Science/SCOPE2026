# Pairwise independent palindrome-center radii and exact variance of palindrome occurrences

## Finding

Let \(X_0,\ldots,X_{n-1}\) be independent uniform symbols from an alphabet of \(q\ge 2\) letters, where \(n\ge1\). For each integer or half-integer center \(c\) in the word, let \(R_c\) denote the number of *nontrivial* palindromic substring occurrences centered at \(c\), with occurrences at the same center of different lengths counted separately. Thus odd palindromes have length at least three, and even palindromes have length at least two. **Any two distinct center radii \(R_c,R_d\) are independent**, even when the intervals of possible palindromes overlap. The family is generally not mutually independent.

Let \(T_n=\sum_cR_c\), the total number of palindrome occurrences of length at least two (not the number of distinct palindromic factors). Then for every integer \(q\ge2\),
\[
\sum_{n\ge1}\operatorname{Var}(T_n)z^n
=\frac{q(q-1)z^2(1+z)(q+z^2)}{(1-z)^2(q-z^2)^2(q^2-z^2)}.
\]
In particular,
\[
\operatorname{Var}(T_n)=\frac{2q}{(q-1)^2}n+O_q(1)
\qquad(n\to\infty).
\]
The same variance holds when the \(n\) trivial length-one palindrome occurrences are included, because this adds a deterministic constant.

## Assumptions and scope

Words are *linear* (no cyclic wraparound). Symbol probabilities are identical and uniform, positions are independent, and all positions are indexed. A palindrome occurrence is an interval \([i,j]\) such that \(X_i=X_j, X_{i+1}=X_{j-1},\ldots\). Different intervals are distinct occurrences even when their contents are identical. Centers range over \(\{0,\frac12,1,\ldots,n-1\}\), with half-integer centers relevant only to even lengths. Set \(R_c=0\) if no nontrivial palindrome centered there fits in the word.

## Proof

Write \(E_{c,r}\) for the event that the palindrome of positive radius \(r\) about center \(c\) fits and occurs. Such a radius imposes exactly \(r\) equalities on \(2r\) distinct positions. These equalities are edges of a matching, with each edge's midpoint equal to \(c\). Thus \(\mathbb P(E_{c,r})=q^{-r}\).

**Two-center forest lemma.** The union of the equality matchings for \(E_{c,r}\) and \(E_{d,s}\) with \(c\ne d\) is a forest. There are no repeated edges since an edge's midpoint determines its center. Any cycle in the union of two matchings must alternate between their edges. If an edge of midpoint \(c\) carries a position \(i\) to \(2c-i\), then a successive edge of midpoint \(d\) carries it to \(i+2(d-c)\). Along a purported alternating cycle, successive pairs of edges therefore translate the integer position by the same nonzero amount \(2(d-c)\), so they cannot return to their starting position. Hence a cycle is impossible.

For a forest on the \(n\) positions with \(e\) edges, independent uniform labeling gives equality probability \(q^{-e}\): each tree of \(v\) vertices must be monochromatic, with probability \(q^{-(v-1)}\), and the trees are independent. Our two-center union has \(r+s\) edges. Consequently
\[
\mathbb P(E_{c,r}\cap E_{d,s})=q^{-(r+s)}
=\mathbb P(E_{c,r})\mathbb P(E_{d,s}).
\]
For every permitted \(r\), \(\{R_c\ge r\}=E_{c,r}\). Joint tail probabilities determine the law of a pair of bounded nonnegative integer random variables, so \(R_c\) and \(R_d\) are independent. They are not generally jointly independent: for \(n=3\), the one-radius events at centers \(\frac12,1,\frac32\) require respectively \(X_0=X_1\), \(X_0=X_2\), and \(X_1=X_2\). Their triple intersection has probability \(q^{-2}\), rather than \(q^{-3}\).

Let \(m_c\) be the maximum number of nontrivial palindrome radii fitting about \(c\), and put \(t=1/q\). The tail of \(R_c\) is \(\mathbb P(R_c\ge r)=t^r\) for \(1\le r\le m_c\). The tail-sum identities
\[
\mathbb ER_c=\sum_{r=1}^{m_c}t^r,
\qquad\mathbb ER_c^2=\sum_{r=1}^{m_c}(2r-1)t^r
\]
give, by finite geometric summation,
\[
V_m:=\operatorname{Var}(R_c)
=\frac{t-(2m+1)(1-t)t^{m+1}-t^{2m+2}}{(1-t)^2},\quad m=m_c\ge0.
\]
Each integer center \(i\) has \(m_i=\min(i,n-1-i)\). Each half-integer center \(i-\frac12\), with \(1\le i\le n-1\), has \(m_{i-1/2}=\min(i,n-i)\). Thus the multiplicities of maximum radius \(m\) can be counted directly. Pairwise independence eliminates all off-diagonal covariance terms:
\[
\operatorname{Var}(T_{2k})=4\sum_{m=1}^{k-1}V_m+V_k\ (k\ge1),
\quad
\operatorname{Var}(T_{2k+1})=4\sum_{m=1}^{k-1}V_m+3V_k\ (k\ge1),
\]
with \(\operatorname{Var}(T_1)=0\).

Summing the displayed expression for \(V_m\) yields
\[
H(u):=\sum_{m\ge1}V_mu^m
=\frac{t(1-t)u(1+tu)}{(1-u)(1-tu)^2(1-t^2u)}.
\]
Substitution into the parity formulas gives
\[
\sum_{n\ge1}\operatorname{Var}(T_n)z^n
=\frac{(1+z)^2}{1-z}H(z^2)
=\frac{q(q-1)z^2(1+z)(q+z^2)}{(1-z)^2(q-z^2)^2(q^2-z^2)}.
\]
Finally \(V_m=q/(q-1)^2+O_q(mq^{-m})\). The sum of the absolute deviations over all centers is bounded independently of \(n\), while there are \(2n-1\) centers. Hence \(\operatorname{Var}(T_n)=2nq/(q-1)^2+O_q(1)\), as claimed.

## Verification

Run `python3 verify.py` using Python 3 and no third-party packages. Expected result: `VERIFY_OK forest_checks=24668 brute_variance_cases=27 gf_cases=474`. The checker independently enumerates equality graphs for all possible two-center radius combinations in words of lengths \(2\) through \(16\); counts all palindrome occurrences in every word over alphabets of size \(2\) (lengths \(1\) through \(12\)), size \(3\) (lengths \(1\) through \(8\)) and size \(4\) (lengths \(1\) through \(7\)); and checks exact rational coefficients of the variance generating function through length \(79\) for alphabet sizes \(2\) through \(7\). Finite checks are not the proof of the infinite statements; the forest lemma and generating-function identities above provide that proof.

## Relationship to prior work

Rubinchik and Shur study the expectation of **distinct palindromic factors** of uniform random words, deriving a markedly different order of growth. Their fixed-length occurrence counting observations do not imply pairwise independence of *center-radius counts* or the above exact variance of all occurrence counts. Leung, Choi, Xia and Chen analyze overlapping reverse-complement DNA palindrome indicators of specified lengths and Poisson approximations; this is a related overlap-probability framework, but it concerns a different involution and observable. Anisiu, Anisiu and Kása study palindromic complexity of finite words, primarily counting distinct factors rather than second moments of all occurrences. General pattern-count moment methods could in principle specialize to occurrence variance; no exact all-length expression covering the joint structural claim was identified in the inspected sources.

## Limitations

The theorem requires a uniform independent alphabet and a linear word. It does not establish mutual independence of all centers, a central limit theorem, concentration estimates beyond the exact variance, distribution laws for distinct palindromic factors, or validity under nonuniform or correlated sources. The novelty assessment is based on the cited inspected sources and searchable published records; an unindexed equivalent formulation may exist. No independent mathematical audit has been performed.

## References

1. M. Rubinchik and A. M. Shur, *The Number of Distinct Subpalindromes in Random Words*, arXiv:1505.08043, initial public version 2015-05-29. https://arxiv.org/abs/1505.08043
2. M.-Y. Leung, K. P. Choi, A. Xia and L. H. Y. Chen, *Nonrandom Clusters of Palindromes in Herpesvirus Genomes*, Journal of Computational Biology 12 (2005), 331–354. https://pmc.ncbi.nlm.nih.gov/articles/PMC4032367/
3. M.-C. Anisiu, V. Anisiu and Z. Kása, *Properties of palindromes in finite words*, Pure Mathematics and Applications 17 (2006), 183–195. https://ictp.acad.ro/properties-of-palindromes-in-finite-words/
