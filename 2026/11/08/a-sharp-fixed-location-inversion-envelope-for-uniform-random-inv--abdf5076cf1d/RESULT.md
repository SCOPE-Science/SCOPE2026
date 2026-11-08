# A sharp fixed-location inversion envelope for uniform random involutions

## Finding
For a uniformly random involution \(\Pi\) on \([n]\), condition on its **exact** fixed-point set \(S\), rather than merely its number of fixed points. Let \(R=[n]\setminus S\) have even size \(r\), and for every \(s\in S\) define \(a_s=|\{v\in R:v<s\}|\). For \(r\ge2\), the conditional expected ordinary one-line inversion count is
\[
\mathbb E[\operatorname{inv}(\Pi)\mid\operatorname{Fix}(\Pi)=S]
=\frac{r^2}{4}+\frac{2}{r-1}\sum_{s\in S}a_s(r-a_s).
\]
When \(r=0\), the involution is the identity and the inversion count is zero.

For each fixed \(n\), positive \(k=|S|\), and even \(r=n-k\ge2\), this gives the sharp envelope
\[
\frac{r^2}{4}\le\mathbb E[\operatorname{inv}(\Pi)\mid\operatorname{Fix}(\Pi)=S]
\le\frac{r^2}{4}+\frac{kr^2}{2(r-1)}.
\]
The upper endpoint is attained **only** when the fixed points constitute the central consecutive block \(S=\{r/2+1,\ldots,r/2+k\}\). The lower endpoint is attained **exactly** when the nonfixed labels form a consecutive block of length \(r\), leaving the fixed points at the two ends; there are \(k+1\) such fixed sets. At fixed counts, changing fixed-point *locations* can therefore shift the conditional inversion mean by \(kr^2/[2(r-1)]\), potentially of quadratic order in \(n\).

## Assumptions and scope
An involution is a permutation \(\pi\) with \(\pi^2=\mathrm{id}\). Its fixed-point set is \(\operatorname{Fix}(\pi)=\{i:\pi(i)=i\}\), and its inversion number is \(\operatorname{inv}(\pi)=\#\{(i,j):1\le i<j\le n,\ \pi(i)>\pi(j)\}\). Condition on the event that the fixed-point set is **exactly** \(S\), which has positive probability if and only if \(r=n-|S|\) is even. The restriction to uniform involutions matters: the remaining vertices of \(R\) are paired by a uniform perfect matching.

## Proof
Every involution with exact fixed set \(S\) corresponds bijectively to a perfect matching of \(R\), each matching being equally likely. Set \(b_s=r-a_s\).

For any two distinct nonfixed indices \(u<v\) in \(R\), there is probability \(1/(r-1)\) that they form one matched pair, in which case \(\Pi(u)=v>u=\Pi(v)\). Otherwise their two partners are distinct elements of \(R\setminus\{u,v\}\), uniformly ordered. By symmetry the probability that the first partner exceeds the second is \(1/2\). For \(r\ge4\) the resulting inversion probability is \(1/(r-1)+(r-2)/(2(r-1))=r/(2(r-1))\). At \(r=2\) the single pair is always an inversion and the same formula holds. Summing over the \(\binom r2\) nonfixed pairs gives \(r^2/4\).

Pairs of two fixed points never form inversions. For a fixed \(s\in S\), each of the \(a_s\) nonfixed indices below \(s\) has probability \(b_s/(r-1)\) that its matching partner lies above \(s\). Each of the \(b_s\) nonfixed indices above \(s\) has probability \(a_s/(r-1)\) that its partner lies below \(s\). Thus pairs involving \(s\) contribute \(2a_sb_s/(r-1)\) in expectation. Summing proves the exact conditional mean.

Finally \(a_s\) is an integer in \([0,r]\); because \(r\) is even, the nonnegative product \(a_s(r-a_s)\) has unique maximum \(r^2/4\) at \(a_s=r/2\), and vanishes exactly at \(a_s=0\) or \(r\). The maximum for all fixed points forces precisely \(r/2\) nonfixed labels on either side of one central block containing all fixed labels, giving the unique maximizing set. The minimum forces no fixed label between two nonfixed labels, so all nonfixed labels form one consecutive block, with its starting position among \(k+1\) choices. This proves both endpoint classifications and sharpness.

## Verification
The attached standalone Python program enumerates every exact fixed-point set of all feasible parities for sizes \(2\le n\le12\), enumerates every perfect matching of the complementary labels, and compares the rational average inversion count with the formula. It additionally checks both bounds and the complete equality conditions. The observed run passed 20,414 exact assertions covering 189,078 involutions (counted across conditioned cases). The analytic matching argument above proves all sizes; finite enumeration is only a consistency check.

## Relationship to prior work
Dukes (arXiv:math/0412222v1, Section 2.3), reporting an earlier Desarménien recurrence, gives a bivariate generating function for inversions and **the number** of fixed points in involutions. This determines the average after aggregating all fixed sets of a given size, but does not retain their locations. Forrester–Nagao–Rains (arXiv:math/0503074v1) studies random involutions with prescribed numbers of fixed points and increasing-subsequence correlation functions, a different observable. Pinsky (arXiv:2505.02058v1) studies inversions of unrestricted permutations conditioned on the number of fixed points, not uniform involutions with a prescribed exact fixed set. None of those inspected statements specifies the present location-conditioned mean or its sharp set extremizers. Priority risk from uninspected older refined fixed-location enumerations remains.

## Limitations
This is a conditional **first-moment** and extremal result only; it does not establish a full inversion distribution, variance or concentration law, nor claim that every intermediate mean between the sharp bounds is attainable. The source comparison does not prove historical uniqueness, and an independent external review has not been performed.

## References
- W. M. B. Dukes, *Permutation Statistics on Involutions*, arXiv:math/0412222v1, first posted 2004-12-11; Section 2.3. https://arxiv.org/abs/math/0412222
- P. J. Forrester, T. Nagao and E. M. Rains, *Correlation Functions for Random Involutions*, arXiv:math/0503074v1, first posted 2005-03-04. https://arxiv.org/abs/math/0503074
- R. G. Pinsky, *The Inversion Statistic in Derangements and in Other Permutations with a Prescribed Number of Fixed Points*, arXiv:2505.02058v1, first posted 2025-05-04. https://arxiv.org/abs/2505.02058
