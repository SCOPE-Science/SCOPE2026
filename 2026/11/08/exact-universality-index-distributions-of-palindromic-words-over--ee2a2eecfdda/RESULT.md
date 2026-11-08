# Exact universality-index distributions of palindromic words over every finite alphabet

## Finding
Fix an integer \(q\ge2\) and a labeled alphabet \(\Sigma\) of size \(q\). The scattered-subsequence universality index \(\iota_\Sigma(w)\) is the largest nonnegative integer \(k\) such that every word in \(\Sigma^k\) occurs as a scattered subsequence of \(w\), even if \(w\) does not use every letter. Let \(e_q(h,k)\) and \(o_q(h,k)\) respectively count all palindromes of lengths \(2h\) and \(2h+1\), over this fixed alphabet, with index \(k\), for \(h,k\ge0\). The empty palindrome is counted at \(h=0\) in the even case.

Put
\[
A_q(z)=\frac{q!z^q}{\prod_{j=1}^{q-1}(1-jz)},\quad
R_q(z)=\frac{1-A_q(z)}{1-qz},\quad
S_q(z)=\frac{A_q(z)}{z}.
\]
Then the full length-index distributions are the following *exact formal power-series identities*:
\[
\boxed{\sum_{h,k\ge0}e_q(h,k)z^hu^k=\frac{R_q(z)}{1-u^2A_q(z)}}
\]
and
\[
\boxed{\sum_{h,k\ge0}o_q(h,k)z^hu^k=
\frac{qR_q(z)+(u-1)S_q(z)}{1-u^2A_q(z)}.}
\]
In particular, all even-length palindromes have even index, while at odd length both parities can occur. Every coefficient is a nonnegative integer: the apparent subtraction in the odd formula records a partition into possible and impossible midpoint arch completions.

The binary case reduces to
\[
\boxed{E_2(z,u)=\frac{1+z}{1-z-2u^2z^2},\qquad
O_2(z,u)=\frac{2(1+uz)}{1-z-2u^2z^2}.}
\]
Using the convention that \(\binom ab=0\) when \(a<0\), \(b<0\), or \(b>a\), the nonzero index counts are
\[
\begin{aligned}
e_2(h,2j)&=2^j\left[\binom{h-j}{j}+\binom{h-j-1}{j}\right],\\
o_2(h,2j)&=2^{j+1}\binom{h-j}{j},\\
o_2(h,2j+1)&=2^{j+1}\binom{h-j-1}{j},
\end{aligned}
\]
for integers \(h,j\ge0\), with all other \(e_2(h,k)\) zero.

A probability law follows from the same full distribution. For a uniformly chosen \(q\)-ary palindrome \(P_{2h+1}\) of length \(2h+1\), with \(h\ge0\),
\[
\Pr\bigl(\iota_\Sigma(P_{2h+1})\text{ is odd}\bigr)
=\frac{[z^h]S_q(z)/(1-A_q(z))}{q^{h+1}}
=\frac1{qH_q}+O_q(\eta_q^h),
\]
where \(H_q=\sum_{j=1}^q 1/j\) and some \(0<\eta_q<1\) depends only on fixed \(q\). Exactly, this probability is the renewal mass at time \(h+1\) for independent uniform \(q\)-coupon collection runs. For \(q=2\), the finite-length probability is explicitly
\[
\boxed{\Pr\bigl(\iota_\Sigma(P_{2h+1})\text{ is odd}\bigr)
=\frac{1-(-1/2)^h}{3}.}
\]

## Assumptions and scope
The alphabet is fixed and labeled, with size \(q\ge2\). All words and palindromes are finite; a palindrome is identical to its reversal. Scattered subsequences preserve order but need not be contiguous. Universality always means the entire fixed \(q\)-letter ambient alphabet, not merely the letters present in a particular word. All generating-series equalities are formal in \(z,u\), so pole arguments are used only for the separate asymptotic statement. The constants implicit in the exponential convergence depend on fixed \(q\); no uniform claim in growing \(q\) is made.

## Proof
**1. Greedy complete-alphabet arches.** Factor any word \(v\) uniquely as \(a_1\cdots a_mr\), each \(a_i\) being the shortest remaining prefix containing every letter of \(\Sigma\), and \(r\) missing at least one letter. Then \(m=\iota_\Sigma(v)\). The arch condition yields this characterization because each complete block contributes one arbitrary subsequence letter, while if there are only \(m\) full blocks, selecting the sequence of last new symbols followed by an absent letter prevents universality at length \(m+1\). The standard arch characterization is also established in the cited literature.

An arch of length \(\ell\) is uniquely a word of length \(\ell-1\) using exactly the \(q-1\) symbols other than its final letter, followed by that missing final letter. The ordinary generating function for surjections from a positive-length position set onto a prescribed \(s\)-symbol alphabet is \(s!z^s/\prod_{j=1}^s(1-jz)\). Choosing the missing symbol gives the arch generating function \(A_q(z)\) above.

Let \(R_q(z)\) enumerate all incomplete-alphabet residual words, including the empty word. Uniqueness of greedy arch factorization gives
\[
\frac1{1-qz}=\frac{R_q(z)}{1-A_q(z)},
\]
proving \(R_q(z)=(1-A_q(z))/(1-qz)\). Let \(S_q(z)\) enumerate residual words using exactly \(q-1\) distinct alphabet symbols. Appending their unique missing symbol gives a bijection onto arches, hence \(S_q(z)=A_q(z)/z\).

**2. The midpoint arch lemma (known structural fact, with boundaries explicit).** If \(v=a_1\cdots a_mr\), let \(v^R\) denote reversal and \(c\in\Sigma\). Then
\[
\iota_\Sigma(vv^R)=2m,\qquad
\iota_\Sigma(vcv^R)=2m+\mathbf1_{\{\operatorname{alph}(r)\cup\{c\}=\Sigma\}}.
\]
The midpoint lemma appears as Proposition 15 of Barker et al. (2020) and is not claimed as new here. For completeness, its cut argument can be reconstructed directly: the original \(m\) complete blocks on each side yield \(2m\) complete blocks. If a partition of the whole palindrome into \(2m+1\) complete blocks exists, its middle block must cross the midpoint, while exactly \(m\) blocks occur entirely on either side (otherwise one half admits \(m+1\) complete blocks). The portion of the crossing block in the left half is contained in the maximal incomplete suffix \(r\) after greedily finishing \(m\) blocks; the right portion is contained in \(r^R\) by reversal. Their alphabets are therefore contained in \(\operatorname{alph}(r)\). At an odd midpoint, the single center letter \(c\) is the only possible additional letter. Conversely, if \(\operatorname{alph}(r)\cup\{c\}=\Sigma\), the \(m\) left arches, the middle word \(rcr^R\), and the \(m\) reversed arches on the right exhibit \(2m+1\) blocks. More than \(2m+1\) would force \(m+1\) complete blocks wholly into one half. The argument also handles \(m=0\), empty halves, and words omitting alphabet letters.

**3. Count both parity classes.** There are \([z^h]A_q(z)^mR_q(z)\) halves of length \(h\) with exactly \(m\) arches. Each determines one even palindrome and the even index is \(2m\), giving \(E_q\). For each half, there are \(q\) possible middle symbols in an odd palindrome. Exactly one middle symbol raises the index by one if and only if the residual contains exactly \(q-1\) letters; otherwise no middle symbol raises it. The corresponding length enumerator is \(A_q(z)^mS_q(z)\). Therefore the odd-index contribution acquires a factor \(u\) instead of \(1\) for precisely those halves. Summing over \(m\) gives \(O_q\).

**4. Binary specialization.** Set \(q=2\): \(A_2=2z^2/(1-z)\), \(R_2=(1+z)/(1-z)\), and \(S_2=2z/(1-z)\). Substitution and cancellation yield the displayed \(E_2,O_2\). Expanding
\[
(1-z-2u^2z^2)^{-1}=\sum_{j\ge0}2^ju^{2j}z^{2j}(1-z)^{-j-1}
\]
and taking coefficients proves all three binomial formulas.

**5. Center parity as a renewal event.** Generate the half \(v\in\Sigma^h\) and center \(c\in\Sigma\) independently and uniformly. By the midpoint lemma, the full palindromic index is odd exactly when the center \(c\) completes the current greedy arch after reading the half. A random arch length is the usual time \(T\) needed to collect all \(q\) equally likely coupons. Successive complete-arch lengths are independent copies of \(T\), because the source letters are independent. Thus the parity probability is the renewal probability that a completed arch ends exactly at time \(h+1\).

Let \(f_q(t)=A_q(t/q)=\mathbb E[t^T]\). Then
\[
\sum_{h\ge0}\Pr(\iota_\Sigma(P_{2h+1})\text{ odd})t^h
=\frac{f_q(t)}{t(1-f_q(t))}.
\]
The expectation \(\mathbb ET=qH_q\) follows by summing the geometric waiting times when \(0,1,\ldots,q-1\) distinct coupons have been collected. Since every integer \(\ell\ge q\) is a possible arch length and the distribution has exponential tails, \(f_q(t)\) is rational and analytic in a disk of radius greater than one, with aperiodic positive coefficients. Its equation \(f_q(t)=1\) has, on \(|t|\le1\), only the simple solution \(t=1\). Consequently the renewal generating function has a unique pole at \(t=1\) within some larger disk, of principal part \((qH_q)^{-1}(1-t)^{-1}\). Coefficient extraction gives the asserted exponential approach to \(1/(qH_q)\). At \(q=2\), \(f_2(t)=t^2/(2-t)\), so the renewal series is \(t/(2-t-t^2)\), whose partial fractions give the stated exact binary probability.

## Verification
The accompanying self-contained Python verifier `verify_palindromes.py` reconstructs the rational generating functions coefficientwise using integer arithmetic, independently enumerates all palindromes for half lengths through \(11\) (binary), \(7\) (ternary), and \(6\) (four-letter alphabets), and checks index counts and total counts. It evaluates \(52{,}710\) palindrome-index configurations via greedy arches and, for half lengths at most \(3\), rechecks \(630\) configurations by explicitly building all distinct scattered subsequences, independently of greedy arches. These finite checks corroborate rather than replace the all-length argument. The probability limit follows from an analytic proof, not a numerical fit.

To reproduce from the extracted package, use `python verify_palindromes.py` in Python 3. No third-party packages or datasets are required. The script returns a nonzero exit code on failed assertions.

## Relationship to prior work
Barker, Fleischmann, Harwardt, Manea, and Nowotka (2020), Proposition 15, already prove the palindrome midpoint relation between a palindrome's universality index and its half's arch remainder. That relation is an expressly acknowledged premise, **not** a novelty claim. Adamson (2023), Section 3, gives arch counts and algorithms for counting unrestricted \(k\)-subsequence-universal words; it does not state the full two-parity palindrome-restricted bivariate series or their center-parity renewal law. Fleischmann, Germann, and Nowotka (2021) analyze remainders and circular universality for repetitions, not the present all-length palindrome distribution. The contribution here is the integrated exact enumeration of the unrestricted palindromic class for every finite alphabet size, including an explicit asymptotic midpoint parity law.

Related exact counts for adjacency-distinct palindromes and reverse-complement symmetric words concern **properly constrained or differently symmetric** languages. They do not give the unrestricted ordinary-palindrome distribution. This distinction is at the level of the class of words being counted, not merely different parameter names. An unindexed explicit equivalent remains a possible literature risk.

## Limitations
The midpoint structural lemma and standard coupon-collector mean are known; the statement does not claim new proofs of those facts. The finite verifier does not establish any identity beyond its tested instances; the all-length proof is symbolic. The exponential-convergence error constant is only asserted for each fixed \(q\). No claim is made about the uniform large-alphabet regime, nonuniform letter probabilities, or independent mathematical audit.

## References
1. L. Barker, P. Fleischmann, K. Harwardt, F. Manea, D. Nowotka, *Scattered Factor-Universality of Words*, first public arXiv posting March 10, 2020, arXiv:2003.04629v1, especially Proposition 15, https://arxiv.org/abs/2003.04629 .
2. D. Adamson, *Ranking and Unranking k-subsequence universal words*, first public arXiv posting April 10, 2023, arXiv:2304.04583v1, especially Sections 2 and 3, https://arxiv.org/abs/2304.04583 .
3. P. Fleischmann, S. B. Germann, D. Nowotka, *Scattered Factor Universality - The Power of the Remainder*, first public arXiv posting April 19, 2021, arXiv:2104.09063v1, https://arxiv.org/abs/2104.09063 .
