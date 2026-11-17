# A triangular record–excedance covariance law for uniform permutations

## Finding

For every integer \(n\geq2\), let \(\Pi\) be uniformly distributed on the permutations of \(\{1,\ldots,n\}\). At position \(i\), let \(R_i=\mathbf1\{\Pi(i)=\max(\Pi(1),\ldots,\Pi(i))\}\) indicate a left-to-right upper record. At position \(j\), let \(E_j=\mathbf1\{\Pi(j)>j\}\) indicate an excedance. The complete positional cross-covariance matrix is

\[
\operatorname{Cov}(R_i,E_j)=
\begin{cases}
-\dfrac{j}{n i(i-1)}, &1\leq j<i\leq n,\\[5pt]
\dfrac1n-\dfrac{1}{i\binom ni}, &1\leq i=j\leq n,\\[5pt]
0, &1\leq i<j\leq n.
\end{cases}
\]

Consequently, later excedances are uncorrelated with an earlier record, earlier excedances are strictly negatively correlated with a later record, and the only potentially positive entries lie on the diagonal. The diagonal is strictly positive at \(2\leq i\leq n-1\); the first and last diagonal entries vanish.

Write \(R=\sum_{i=1}^n R_i\) and \(E=\sum_{j=1}^n E_j\). The row sums, measuring the dependence of a specified record on the total number of excedances, are

\[
\operatorname{Cov}(R_i,E)=
\begin{cases}
0,& i=1,\\[3pt]
\dfrac{1}{2n}-\dfrac{1}{i\binom ni},&2\leq i\leq n.
\end{cases}
\]

For \(n\geq4\), these are positive at every interior position \(2\leq i\leq n-1\) and negative at the final position \(i=n\). When \(n=3\), the sole interior row sum is zero.

The column sums satisfy

\[
\operatorname{Cov}(R,E_j)=\frac{j}{n^2}-\frac{1}{j\binom nj},\qquad 1\leq j\leq n.
\]

For \(n\geq3\), the column sum is negative at \(j=1\), positive for \(2\leq j\leq n-1\), and zero at \(j=n\). Thus the two kinds of positional aggregation have distinct sharp sign boundaries.

As a consequence of the positional formula,

\[
\operatorname{Cov}(R,E)=\frac{n-1}{2n}-\sum_{i=2}^n\frac{1}{i\binom ni}.
\]

This aggregate covariance increases strictly with \(n\), is negative at \(n=2,3,4\), positive at all \(n\geq5\), and tends to \(1/2\). The aggregate identity is included as an implication of the positional result, **not** as an independently novel aggregate distribution theorem.

## Assumptions and scope

The probability law is the uniform law on all \(n!\) permutations; positions and values are the integers from \(1\) through \(n\). A record compares the value at its position with **all earlier positions**, whereas an excedance compares that value with its own position index. The covariance has the ordinary probabilistic normalization \(\mathbb E[XY]-\mathbb E[X]\mathbb E[Y]\). All identities are exact for every \(n\geq2\) and the specified full index ranges. No asymptotic approximation or independence of indicator families is assumed.

## Proof

**Marginals.** By symmetry of the relative order of the first \(i\) entries, \(\Pr(R_i=1)=1/i\). Since the entry at position \(j\) is uniform on \(\{1,\ldots,n\}\), \(\Pr(E_j=1)=(n-j)/n\).

**Later excedances (\(j>i\)).** Conditional on any fixed value \(\Pi(j)=v\), all relative orderings of the first \(i\) entries are equally likely. Thus \(\Pr(R_i=1\mid\Pi(j)=v)=1/i\), independent of \(v\). Consequently \(\operatorname{Cov}(R_i,E_j)=0\).

**Coincident positions (\(j=i\)).** Conditional on the unordered set of the first \(i\) values, the largest lies in position \(i\) with probability \(1/i\). The sample maximum exceeds \(i\), except when the unordered set is exactly \(\{1,\ldots,i\}\), an event of probability \(\binom ni^{-1}\). Hence

\[
\Pr(R_i=1,E_i=1)=\frac1i\left(1-\frac1{\binom ni}\right).
\]

Subtracting \(\Pr(R_i=1)\Pr(E_i=1)=(n-i)/(ni)\) gives \(1/n-1/(i\binom ni)\). Its positivity for \(2\leq i\leq n-1\) follows from \(i\binom ni=n\binom{n-1}{i-1}>n\).

**Earlier excedances (\(j<i\)).** Condition on \(\Pi(j)=v\). The remaining \(i-1\) prefix values form a uniformly selected sample from the other \(n-1\) values. Unless every sampled value is less than \(v\), the largest of those \(i-1\) values is at position \(i\) with probability \(1/(i-1)\). Therefore

\[
\Pr(R_i=1\mid\Pi(j)=v)=\frac{1}{i-1}\left(1-\frac{\binom{v-1}{i-1}}{\binom{n-1}{i-1}}\right).
\]

With the usual convention that out-of-range binomial coefficients vanish, the hockey-stick identity gives, because \(j<i\),

\[
\sum_{v=j+1}^n\binom{v-1}{i-1}
=\binom ni-\binom ji=\binom ni.
\]

Averaging the conditional probability over \(v>j\) yields

\[
\Pr(R_i=1,E_j=1)=\frac{n-j}{n(i-1)}-\frac{1}{i(i-1)}.
\]

Subtracting \((n-j)/(ni)\) proves the claimed \(-j/[ni(i-1)]\) covariance. This proves the entire matrix.

**Row and column aggregation.** For \(i\geq2\), sum the preceding negative entries using \(\sum_{j=1}^{i-1}j=i(i-1)/2\) and add the diagonal. For the column sums, apply \(\sum_{i=j+1}^n1/[i(i-1)]=1/j-1/n\). This gives the displayed identities. To prove the column signs, use \(j\binom nj=n\binom{n-1}{j-1}\) and \(\binom{n-1}{j-1}\geq n-1\) for \(2\leq j\leq n-1\); hence \(j^2\binom nj>n^2\) for \(n\geq3\). The row signs follow from \(i\binom ni=n\binom{n-1}{i-1}\): the latter binomial is at least \(n-1\) at interior indices, which exceeds \(2\) if \(n\geq4\). The endpoint cases are direct.

**Aggregate finite-size transition.** Summing row terms yields the aggregate identity. Put \(S_n=\sum_{i=2}^n1/[i\binom ni]\). For every \(n\geq2\), the two endpoint changes from \(i=n\) and the new \(i=n+1\) exactly cancel:

\[
\frac{1}{n\binom{n+1}{n}}+\frac{1}{(n+1)\binom{n+1}{n+1}}-\frac{1}{n\binom nn}=0.
\]

Every remaining term indexed by \(2\leq i\leq n-1\) strictly decreases when \(n\) grows. Thus \(S_{n+1}\leq S_n\), and \((n-1)/(2n)\) strictly increases, so \(\operatorname{Cov}(R,E)\) strictly increases. Its values at \(n=4\) and \(n=5\) are respectively \(-1/24\) and \(1/15\), proving the unique sign transition. Finally, for \(n\geq4\), \(\binom ni\geq\binom n2\) for \(2\leq i\leq n-2\), giving \(S_n=O(1/n)\). Hence the aggregate covariance tends to \(1/2\).

## Verification

The accompanying `verify.py` exhaustively enumerates every permutation of sizes \(2\) through \(8\), checks the exact indicator pair moments and all matrix entries, and additionally checks the row/column/global consequences over a range of sizes using exact rational arithmetic. It reports **640 exact checks passed**, and the enumeration covers \(46{,}232\) permutations in total. This is a finite reproducibility check; all-size validity rests on the preceding proof.

Reproduce with `python3 verify.py` using only the Python standard library. The script tests ordinary integer-valued indicators and `fractions.Fraction` computations, not simulated floating-point estimates.

## Relationship to prior work

The exact excedance-set enumerators of Ehrenborg and Steingrímsson (2000), the mesh-pattern expansions of Brändén and Claesson (2011), and the record-dependent permutation framework of Gnedin and Gorin (2012) establish major separate foundations. Sokal and Zeng (2020) provide a **stronger aggregate bivariate/multivariate generating function** including the counts of records and excedances, so its derivatives cover the aggregate covariance above; that aggregate identity is not claimed separately as original. Their stated generating polynomials mark **counts by categories**, not a distinct variable for each absolute pair of positions. They do not explicitly give or directly specialize to the position-indexed triangular cross-covariance matrix. Jin (2022) supplies further joint Euler–Stirling generating functions involving other aggregate statistics; these do not directly assert the displayed indexed matrix. Brändén and Claesson's general mesh-pattern expansion representation can encode both observables in principle, but a generic representation is not an explicit positional covariance or sign classification.

The contribution assessed here is the exact **position-indexed** covariance and its row/column sign structure. This should be understood in the context of the strong aggregate enumerations just cited; discovery of an earlier equivalent positional refinement would supersede the originality claim.

## Limitations

This is a finite-permutation identity for the *uniform* law. The records are upper records in one-line notation and the excedances use the unmodified diagonal threshold. The analysis does not extend to Ewens, Mallows, nonuniform record-dependent laws, or joint distributional limit theorems. The available comparisons cannot prove exhaustive historical uniqueness, especially against implicit refinements or unexamined older combinatorial enumerations. Independent review has not been performed.

## References

- R. Ehrenborg and E. Steingrímsson, *The Excedance Set of a Permutation*, Advances in Applied Mathematics 24 (2000), 284–299. https://www.ms.uky.edu/~jrge/papers/Excedance.pdf
- P. Brändén and A. Claesson, *Mesh Patterns and the Expansion of Permutation Statistics as Sums of Permutation Patterns*, Electronic Journal of Combinatorics 18(2) (2011), P5, first arXiv version 2011-02-21. https://arxiv.org/abs/1102.4226
- A. Gnedin and V. Gorin, *Record-dependent measures on the symmetric groups*, first arXiv version 2012-02-16. https://arxiv.org/abs/1202.3680
- H. Shin and J. Zeng, *Symmetric unimodal expansions of excedances in colored permutations*, first arXiv version 2014-11-23. https://arxiv.org/abs/1411.6184
- A. D. Sokal and J. Zeng, *Some multivariate master polynomials for permutations, set partitions, and perfect matchings, and their continued fractions*, first arXiv version 2020-03-18; especially Theorem 2.1 and Section 2.3. https://arxiv.org/abs/2003.08192
- E. Y. Jin, *Symmetric generating functions and Euler–Stirling statistics on permutations*, first arXiv version 2022-10-17. https://arxiv.org/abs/2210.08789
