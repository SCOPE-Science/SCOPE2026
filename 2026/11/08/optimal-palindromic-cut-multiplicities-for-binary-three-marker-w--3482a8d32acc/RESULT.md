# Optimal palindromic-cut multiplicities for binary three-marker words

## Finding

Let \(w\) be a binary word, and let \(\operatorname{PL}(w)\) denote the smallest number of **nonempty** palindromic factors in a concatenation equal to \(w\). Let \(M(w)\) count the **distinct ordered lists of cut positions** attaining this minimum. For every quadruple of nonnegative integers \(a,b,c,d\), write
\[
w=0^a1\,0^b1\,0^c1\,0^d.
\]
The exact four-factor regime and its optimal-cut multiplicity are
\[
\operatorname{PL}(w)=4\quad\Longleftrightarrow\quad b\ne c\text{ and }\min(a,d)>\max(b,c),
\]
\[
\boxed{M(w)=b+c+2\quad\text{whenever }\operatorname{PL}(w)=4.}
\]
The eligibility criterion by itself is not claimed to be new: it coincides with the positive-defect region of an earlier fixed-content palindromic-defect classification. The new result is the exact optimal-cut multiplicity and its full finite-length distribution.

For \(n\ge3\), let \(N_{n,k}\) be the number of indexed binary words of length \(n\), containing exactly three ones, with palindromic length four and precisely \(k\) optimal factorizations. Their bivariate generating function is
\[
\boxed{H(z,u)=\sum_{n\ge3}\sum_{k\ge1}N_{n,k}z^nu^k
=\frac{2z^8u^3}{(1-z)^2(1-z^3u)(1-z^4u^2)}.}
\]
In particular, for any integer \(k\ge3\), the multiplicity \(k\) occurs at length \(n\) **if and only if**
\[
 n\ge \tau(k):=k+3+2\left\lceil\frac{k-1}{2}\right\rceil
 =\begin{cases}2k+2,&k\text{ odd},\\2k+3,&k\text{ even}.\end{cases}
\]
No word of length less than eight has palindromic length four. For every length at least eight, the complete set of possible multiplicities is the uninterrupted set of integers \(3\le k\le \max\{j:\tau(j)\le n\}\).

Select a length-\(n\) word uniformly among those containing exactly three ones and having palindromic length four. The random variable \(M(w)/n\) converges weakly to a law with density
\[
 f(t)=\begin{cases}
36t-90t^2,&0<t\le\frac13,\\
18(1-2t)^2,&\frac13<t<\frac12,\\
0,&\text{otherwise}.
\end{cases}
\]
Its mean is \(5/24\), second moment is \(19/360\), and variance is \(3/320\).

## Assumptions and scope

The alphabet is precisely \(\{0,1\}\). A factor must be contiguous and nonempty. Cut positions are indexed: different boundaries constitute different factorizations even if some palindrome strings coincide. We count each indexed source word once, never quotienting by reversal. Only words containing exactly three ones are covered; the asymptotic law is **conditional** on palindromic length four. No result is claimed for arbitrary Hamming weights or for the number of nonminimal factorizations.

## Proof

**1. The length-four regime.** A word with zero or one one is a product of at most two palindromes. A two-one word \(0^p1\,0^q1\,0^r\) is a product of at most two palindromes: if \(p\le r\) split after \(0^p1\,0^q1\,0^p\), leaving \(0^{r-p}\); if \(p>r\), first remove \(0^{p-r}\) and retain the palindrome \(0^r1\,0^q1\,0^r\). Empty all-zero pieces are simply omitted. The corresponding one-one decomposition also holds.

Every three-one word has at most four palindromic pieces: split off \(0^a\), then \(1\,0^b1\), and factor the remaining one-one word \(0^c1\,0^d\) into at most two palindromes. If \(b=c\), the middle three-one word \(1\,0^b1\,0^b1\) is itself a palindrome, so at most three pieces suffice. Suppose now that \(a\le\max(b,c)\). If \(b\ge a\), its initial palindrome \(0^a1\,0^a\) leaves a two-one word, requiring at most two more pieces. If \(c\ge a\), the initial palindrome \(0^a1\,0^b1\,0^a\) leaves a one-one word, again requiring at most two more pieces. The same argument applied to reversal covers \(d\le\max(b,c)\).

Conversely let \(b\ne c\) and \(a,d>\max(b,c)\). No palindromic prefix containing a one can exist: a prefix with exactly one one would require \(b\ge a\), one with exactly two ones would require \(c\ge a\), while one with three ones would require \(b=c\). By reversal no palindromic suffix contains a one. Thus a factorization into at most three palindromes would have nonempty all-zero first and last pieces, with a central three-one palindrome; the latter forces \(b=c\), a contradiction. Hence \(\operatorname{PL}(w)=4\).

**2. Every optimal cut.** In the length-four regime just proved, every optimal factorization begins and ends with positive zero runs. After removing respectively \(r\) and \(s\) terminal zeros, \(1\le r\le a\) and \(1\le s\le d\), write \(p=a-r\), \(q=d-s\). The central word is \(0^p1\,0^b1\,0^c1\,0^q\) and must split into exactly two nonempty palindromes.

Since \(b\ne c\), neither a palindromic prefix nor suffix can contain all three ones. Consequently the two factors distribute the three ones as \((1,2)\) or \((2,1)\). In the first case, the one-one factor is \(0^p1\,0^p\) and the remaining two-one factor is \(0^{b-p}1\,0^c1\,0^q\); these are palindromes precisely when \(b=p+q\). In the second case the factors are \(0^p1\,0^b1\,0^p\) and \(0^{c-p}1\,0^q\), requiring \(c=p+q\). These cases are disjoint because \(b\ne c\), and each admissible pair \((p,q)\) determines **exactly one** internal cut. For each target \(t\in\{b,c\}\), the equation \(p+q=t\) has \(t+1\) nonnegative solutions; all obey \(p<a\) and \(q<d\) because \(t<\min(a,d)\). Therefore \(M(w)=(b+1)+(c+1)=b+c+2\).

**3. Bivariate enumeration and sharp support.** Let \(h=\max(b,c)\ge1\) and \(\ell=\min(b,c)\), so \(0\le\ell<h\); the two orientations are distinct. For each, write \(a=h+1+\alpha\) and \(d=h+1+\delta\), with \(\alpha,\delta\ge0\). Then
\[
 n=5+3h+\ell+\alpha+\delta,\qquad k=h+\ell+2.
\]
Writing \(h=\ell+1+s\) and summing geometric series in \(s,\ell,\alpha,\delta\) yields the stated \(H(z,u)\). For a proposed multiplicity \(k\), the minimum possible length is obtained by minimizing \(3h+\ell=2h+k-2\) under \(h+\ell=k-2\) and \(0\le\ell<h\), at \(h=\lceil(k-1)/2\rceil\). Hence the sharp threshold \(\tau(k)\). Additional leading or trailing zeros realize every larger length.

**4. Conditional scaling law.** The four nonnegative gaps sum to \(n-3\), and uniform selection of indexed three-one words is uniform on this integer simplex. Restricting to the four-factor region and dividing gaps by \(n\), Riemann-sum convergence gives the continuous simplex region with \(h=\max(b/n,c/n)\), \(\ell=\min(b/n,c/n)\), \(0<\ell<h\), and \(3h+\ell<1\). For each \((h,\ell)\), the total permitted interval of the first outer gap has length \(1-3h-\ell\); there are two orientations, and the volume is \(1/36\). Since \(M(w)/n=h+\ell+2/n\), put \(t=h+\ell\) and integrate the weight \(2(1-t-2h)\) over
\[
 \frac t2<h<\min\left(t,\frac{1-t}{2}\right).
\]
Multiplying by the normalization factor \(36\) gives \(36t-90t^2\) for \(0<t\le1/3\) and \(18(1-2t)^2\) for \(1/3<t<1/2\). Exact polynomial integration yields total mass one, mean \(5/24\), second moment \(19/360\), and variance \(3/320\). Boundary lattices have zero limiting measure. This proves weak convergence.

## Verification

The accompanying `verify.py` is a standalone standard-library program. Its dynamic program computes both the minimum number of palindrome blocks and its minimizing cut-count independently of the gap formulas. For every length from three through twenty-four it checks all \(12{,}650\) three-one indexed words. For the \(330\) four-factor words encountered through length eighteen, it also enumerates **all cut triples** directly. It compares coefficient counts with two independent parameterizations through length one hundred, checks the exact multiplicity thresholds through length one hundred, and integrates the two limiting density polynomials over rational endpoints. The recorded outputs are `VERIFY_OK` and `MOMENT_AND_SHARP_SPECTRUM_OK`. Finite checks do not replace the proof above.

## Relationship to prior work

Ravsky proved extrema and averages of palindromic length for unrestricted binary words; Frid, Puzynina and Zamboni analyzed minimal palindromic factorization chiefly through the behavior of infinite words and explicitly noted nonuniqueness for individual short strings; Fici and coauthors developed an algorithm to find a minimum factorization; Borchert and Rampersad investigated factors that themselves are products of two palindromes. The present statistic counts **all minimum-factor cut lists** in a fixed three-one family, not the minimum length alone, one selected optimum, or the number of palindrome-pair substrings.

The earlier fixed-weight palindromic-defect finding with identifier `d1ffbb20-77e9-4221-864f-c5048aecca42` already determines the same eligibility region for length-four words, as well as its unweighted distribution. Those results are explicitly excluded from novelty here. The multiplicity formula, full bivariate refinement, attainable-multiplicity threshold, and conditional limit law are not implications of that prior defect statement by themselves. An OEIS record, A241211, counts binary words with a unique factorization into palindromes of **length at least two** without a minimum-block restriction; it is a different factorization problem.

## Limitations

The theorem concerns indexed binary words with exactly three ones, and the limit law is conditional on palindromic length four. It does not determine the multiplicity of optimal factorizations outside this domain. No claim is made that indexed literature searches establish absolute historical priority; unindexed equivalent work is possible. Verification is by the stated proof and finite independent-method checks; no independent human mathematical audit has been performed.

## References

1. A. Ravsky, *On the Palindromic Decomposition of Binary Words*, arXiv:1004.1278, first arXiv posting 2010-04-08. https://arxiv.org/abs/1004.1278
2. A. E. Frid, S. Puzynina, L. Zamboni, *On Minimal Factorizations of Words as Products of Palindromes*, arXiv:1210.6179, first posting 2012-10-23. https://arxiv.org/abs/1210.6179
3. G. Fici, T. Gagie, J. Kärkkäinen, D. Kempa, *A Subquadratic Algorithm for Minimum Palindromic Factorization*, arXiv:1403.2431, first posting 2014-03-10. https://arxiv.org/abs/1403.2431
4. A. Borchert, N. Rampersad, *Words with Many Palindrome Pair Factors*, arXiv:1509.05396, first posting 2015-09-17. https://arxiv.org/abs/1509.05396
5. OEIS A241211, *Number of binary strings of length n having exactly one factorization as a concatenation of palindromes of length at least two*. https://oeis.org/A241211
6. *Exact palindromic defect and the richness spectrum of binary three-marker words*, prior scientific result, identifier `d1ffbb20-77e9-4221-864f-c5048aecca42`.
