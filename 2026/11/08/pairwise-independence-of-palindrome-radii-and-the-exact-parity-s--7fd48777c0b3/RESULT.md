# Pairwise independence of palindrome radii and the exact parity-split covariance spectrum

## Finding

Let \(n\ge3\) and let \(X_1,\ldots,X_n\) be independent identically distributed letters from a finite alphabet. The radius \(R_c\) at a letter or interletter center \(c\in\{1,3/2,2,5/2,\ldots,n\}\) is the maximal number of outward symmetric **pairs of letters** that agree, before the first mismatch or a word boundary. Then the family \((R_c)_c\) is pairwise independent **if and only if** the letter distribution is uniform on its positive-probability support. For \(n=2\), pairwise independence instead holds for every iid letter law because only one center has a nonzero radius.

Under a uniform law on \(q\ge2\) letters, let \(P_j\) count the palindromic substring **occurrences**, including repeats, of length \(j\), and put \(P_1=n\). For all integers \(r,s\ge1\), with \((x)_+=\max\{x,0\}\),

\[
\begin{aligned}
\operatorname{Cov}(P_{2r},P_{2s})
&=(n-2\max\{r,s\}+1)_+
\left(q^{-\max\{r,s\}}-q^{-(r+s)}\right),\\
\operatorname{Cov}(P_{2r+1},P_{2s+1})
&=(n-2\max\{r,s\})_+
\left(q^{-\max\{r,s\}}-q^{-(r+s)}\right),\\
\operatorname{Cov}(P_{2r},P_{2s+1})&=0.
\end{aligned}
\]

Counts at opposite length parities are therefore *exactly uncorrelated* at every finite word length, although the radius family is not generally three-wise independent. With \(T_n=\sum_{j=1}^nP_j\), the total number of positional palindromic substrings,

\[
\mathbb E T_n=n+\sum_{r=1}^{\lfloor n/2\rfloor}(2n-4r+1)q^{-r},
\]

and, writing \(h_c\) for the largest geometrically available radius at center \(c\),

\[
\operatorname{Var}(T_n)=\sum_c\left[\sum_{r=1}^{h_c}(2r-1)q^{-r}-\left(\sum_{r=1}^{h_c}q^{-r}\right)^2\right].
\]

In particular, for every fixed \(q\ge2\),

\[
\lim_{n\to\infty}\frac{\mathbb E T_n}{n}=\frac{q+1}{q-1},\qquad
\lim_{n\to\infty}\frac{\operatorname{Var}(T_n)}n=\frac{2q}{(q-1)^2}.
\]

## Assumptions and scope

Indices are \(1,\ldots,n\). A center is a number \(c\) that is either an integer or a half-integer between \(1\) and \(n\), giving \(2n-1\) centers in all. At integer \(c\), the \(r\)-th pair is \((c-r,c+r)\); at half-integer \(c=k+1/2\), it is \((k-r+1,k+r)\). A radius of zero is possible. The capacity \(h_c\) is the number of such geometrically valid pairs. The law may contain zero-probability symbols, which are removed when defining its positive support. No Markov, stationarity beyond iid, or asymptotic assumption is needed for the exact results. By a palindrome we mean literal equality with its reversal, **not** reverse-complement equality from molecular biology. The result counts occurrences at positions, not distinct palindrome *words*.

## Proof

**1. Equality graphs and pairwise independence.** For any event \(R_c\ge r\), draw edges between each of the \(r\) mirrored index pairs. These edges form a matching, all with endpoint sum \(2c\). For distinct centers \(c\ne d\), the two matchings have no common edges. Their union has no cycle: any cycle would alternate the two edge colors, whereas composing the two reflections \(x\mapsto2c-x\) and \(x\mapsto2d-x\) translates every index by the nonzero displacement \(2(d-c)\), and repeated translations cannot return to the starting index. Thus the union is a forest with exactly \(r+s\) edges. With iid uniform \(q\)-letter labels, the probability that labels coincide along every edge of any forest equals \(q^{-\#\text{edges}}\): there are \(q\) choices per connected component. Therefore

\[
\Pr(R_c\ge r,R_d\ge s)=q^{-(r+s)}
=\Pr(R_c\ge r)\Pr(R_d\ge s)
\]

for all admissible positive thresholds at distinct centers. Upper-tail events generate the full finite-state sigma-fields of the radii, proving pairwise independence.

**2. Necessity of uniform letters and the sharp word-length boundary.** For \(n\ge3\), the centers \(3/2\) and \(2\) yield the radius-one events \(X_1=X_2\) and \(X_1=X_3\). Writing \(p_a=\Pr(X_i=a)\), their covariance is

\[
\sum_a p_a^3-\left(\sum_a p_a^2\right)^2
=\operatorname{Var}(p_{X_1})\ge0.
\]

It vanishes only if all positive \(p_a\) coincide. Thus any nonuniform iid law on its support prevents pairwise independence. For \(n=2\), only the interletter center has a nonconstant radius, so all centers are automatically pairwise independent without uniformity.

**3. Exact covariance of length counts.** At a given center, palindrome indicators at radii \(r,s\) are nested, so their joint probability is \(q^{-\max\{r,s\}}\) and their covariance is the bracketed factor in the displayed formula. Indicators at distinct centers have zero covariance by Step 1. Even-length palindromes have half-integer centers, whereas odd-length palindromes have integer centers. There are \((n-2\max\{r,s\}+1)_+\) eligible half-integer centers for both even lengths, and \((n-2\max\{r,s\})_+\) eligible integer centers for both odd lengths. Summing centerwise gives all three covariance identities, including the opposite-parity zero.

**4. Exact total-count moments.** Every letter is one trivial palindrome, and at center \(c\) every successful symmetric pair adds exactly one longer palindrome, hence \(T_n=n+\sum_cR_c\). Each radius obeys \(\Pr(R_c\ge r)=q^{-r}\) for \(1\le r\le h_c\). Thus \(\mathbb E R_c=\sum_{r=1}^{h_c}q^{-r}\), while the tail-sum identity \(\mathbb E R_c^2=\sum_{r=1}^{h_c}(2r-1)q^{-r}\) yields the exact variance through pairwise independence. For each integer \(r\le\lfloor n/2\rfloor\), exactly \(2n-4r+1\) centers have \(h_c\ge r\), giving the mean formula.

**5. Asymptotic slopes.** Put \(t=q^{-1}\in(0,1)\). The unlimited geometric radius \(G\), with \(\Pr(G\ge r)=t^r\), has \(\mathbb EG=t/(1-t)\) and \(\operatorname{Var}(G)=t/(1-t)^2\). A center with capacity \(h\) has radius distributed as \(\min\{G,h\}\). Its variance deficit from \(\operatorname{Var}(G)\) is exactly

\[
\frac{(2h+1)t^{h+1}}{1-t}+\frac{t^{2h+2}}{(1-t)^2}.
\]

There are at most four centers of any given finite capacity. The sum of all these deficits is bounded uniformly in \(n\), because the displayed quantity decays geometrically in \(h\). It follows that \(\operatorname{Var}(T_n)=(2n-1)t/(1-t)^2+O_q(1)\). The mean sum in Step 4 similarly equals \(n+2nt/(1-t)+O_q(1)\). Division by \(n\) gives the two limits.

**6. Non-mutual independence.** In a three-letter word, the radius-one events at centers \(3/2,2,5/2\) are respectively \(X_1=X_2\), \(X_1=X_3\), and \(X_2=X_3\). Under uniform \(q\)-letter sampling, each has probability \(q^{-1}\), every pair has joint probability \(q^{-2}\), but all three occur with probability \(q^{-2}\ne q^{-3}\). This proves the claimed precise distinction between pairwise and joint independence.

## Verification

The standalone `check_palindromes.py` computes radii directly from each word, independently accumulates palindrome-count covariance matrices and pairwise radius survival frequencies, and checks all displayed finite exact identities using integer/rational arithmetic. It exhausts all binary words through length eight and ternary words through length six. It separately verifies the two-reflection union-forest lemma for all distinct centers and valid radii in word lengths through fourteen, an explicitly biased three-letter-word obstruction, and the three-center lack of mutual independence. Its final report is `PASS: 13735 independently computed exact checks`. This enumeration is a consistency check, **not** an all-length proof: Steps 1–6 provide that proof.

## Relationship to prior work

Rubinchik and Shur's 2015 paper addresses the expected count of **distinct palindrome words**, while its Lemma 3.2 also gives the first moment of positional palindrome occurrences at one length. The result here concerns the joint distribution of different centered radii, an exact covariance matrix of occurrence counts across lengths, and the uniform-only independence classification; these statements are not implied by the stated distinct-word expectation theorem or its one-length first moment alone. Leung, Choi, Xia, and Chen (2005) derive joint occurrence probabilities for **reverse-complement** DNA palindromes of one fixed length; their uniform-case overlapping-indicator equality is a close and important precedent, but the published proposition is not the all-centers, all-lengths covariance theorem for ordinary palindromes. The 2013 Špoljarić–Ugrina paper treats reverse-complement DNA palindrome counts at fixed length; its full text could not be checked, so implicit historical coverage remains a specific priority risk. No independent priority or external validation is claimed.

## Limitations

The pairwise-independence theorem assumes iid letters and literal reversal. Nonuniform iid letters generally destroy independence at distinct centers, as proved, and radius independence does not extend to three or more centers even under uniform letters. The formulas describe positional occurrence counts, not the number of distinct palindrome values. They do not themselves establish a central limit theorem or a Poisson approximation. The literature comparison does not rule out equivalent formulas in other uninspected sources; in particular the 2013 fixed-length DNA treatment remains an access-limited comparison. Independent validation has not been performed.

## References

1. M. Rubinchik and A. M. Shur, *The Number of Distinct Subpalindromes in Random Words*, arXiv:1505.08043v1 (first posted 2015-05-29), especially Section 3, Lemma 3.2, and Section 6. https://arxiv.org/pdf/1505.08043
2. M.-Y. Leung, K. P. Choi, A. Xia, and L. H. Y. Chen, *Nonrandom Clusters of Palindromes in Herpesvirus Genomes*, Journal of Computational Biology 12 (2005), 331–354, Proposition 1 and the remark following Lemma 1. https://pmc.ncbi.nlm.nih.gov/articles/PMC4032367/
3. D. Špoljarić and I. Ugrina, *On Statistical Properties of Palindromes in DNA*, Communications in Statistics—Theory and Methods 42 (2013), 1373–1385. https://doi.org/10.1080/03610926.2012.739253 (abstract inspected; complete text unavailable at review).
