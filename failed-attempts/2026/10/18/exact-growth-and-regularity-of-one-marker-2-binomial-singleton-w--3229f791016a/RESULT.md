# Exact growth and regularity of one-marker 2-binomial singleton words

## Finding
For words over \(\Sigma=\{0,1,2\}\), consider the equivalence relation determined by the counts of **scattered** subsequences of lengths one and two. A word is a *2-binomial singleton* if no different word has all those counts. Let \(S(n)\) count singleton words of length \(n\ge1\) containing **exactly one** occurrence of the symbol \(2\). The comparison class includes all ternary words; the count of the singleton marker itself forces every equivalent word into the same one-marker slice.

The complete singleton language in this slice is
\[
\mathcal L=\mathcal M2\mathcal B\ \cup\ \mathcal B2\mathcal M\ \cup\ 0^+1^+20^+1^+\ \cup\ 1^+0^+21^+0^+,
\]
where juxtaposition denotes concatenation, \(\mathcal M=0^*\cup1^*\), and the binary 2-binomial singleton language is
\[
\mathcal B=0^*1^*\cup1^*0^*\cup0^*10^*\cup1^*01^*\cup0^*101^*\cup1^*010^*.
\]
Here \(0^*\) allows the empty word, whereas \(0^+\) requires at least one zero, and similarly for ones. In particular, \(\mathcal L\) is a regular language.

The exact generating function for all lengths is
\[
\boxed{\displaystyle \sum_{n\ge1}S(n)z^n=\frac{z(1+2z^2+4z^3+3z^4-4z^5-4z^6)}{(1-z)^4}.}
\]
The initial values \(S(1),\ldots,S(12)\) are \(1,4,12,32,74,144,244,376,542,744,984,1264\). For every \(n\ge7\), coefficient extraction gives
\[
\boxed{\displaystyle S(n)=\frac{n^3+27n^2-178n+312}{3}.}
\]
Consequently \(S(n)\sim n^3/3\), and its fraction among the \(n2^{n-1}\) length-\(n\) ternary words with precisely one \(2\) is asymptotic to \(2n^2/(3\cdot2^n)\).

## Assumptions and scope
A scattered occurrence of a two-letter pattern \(xy\) in \(w=w_1\cdots w_n\) is a pair \(i<j\) with \(w_i=x,w_j=y\); its count is denoted \(\binom{w}{xy}\). A scattered one-letter occurrence is its usual letter count. Two words are 2-binomial equivalent if these counts agree for every alphabet word of length one or two. The underlying alphabet is fixed and labeled, and all singleton decisions are taken within the entire set \(\Sigma^n\), not merely within a chosen regular expression. Empty binary segments on either side of the marker are admitted. The theorem concerns only the exactly-one-marker slice, not arbitrary ternary singleton words or longer subsequences.

## Proof
Every input word has a unique decomposition \(w=u2v\) with \(u,v\in\{0,1\}^*\). Write \(a=|u|_0\), \(b=|u|_1\), \(c=|v|_0\), \(d=|v|_1\) and \(I(x)=\binom{x}{01}\). The singleton one-letter subsequence counts prescribe the marker count and the total number of each binary symbol. The two-letter counts \(\binom{w}{02}=a\) and \(\binom{w}{12}=b\) then uniquely determine \(a,b,c,d\). Every other two-letter count is determined by these four numbers together with \(\binom{w}{01}\), since \(\binom{w}{01}=I(u)+ad+I(v)\), and \(\binom{w}{10}= (a+c)(b+d)-\binom{w}{01}\). Counts of repeated symbols depend only on the letter totals; the remaining marker-crossing pair counts are determined by \(c,d\). Thus the number of words equivalent to \(w\) is precisely the number of ordered binary pairs with fixed Parikh vectors \((a,b)\) and \((c,d)\), and prescribed \(I(u)+I(v)\).

For nonnegative \(a,b\), define \(G_{a,b}(t)=\sum_{u:|u|_0=a,|u|_1=b}t^{I(u)}\). This Gaussian-binomial polynomial has every exponent from \(0\) through \(ab\) present. When \(ab=0\), it equals \(1\). If \(\min(a,b)=1\), all coefficients equal \(1\). If \(a,b\ge2\), precisely the coefficients at exponents \(0,1,ab-1,ab\) equal \(1\); all others are at least \(2\). The last assertion follows either from the classical symmetry and unimodality of Gaussian-binomial coefficients (the two distinct partitions of \(2\) inside an \(a\)-by-\(b\) rectangle start a plateau of coefficients at least \(2\)) or from the binary singleton classification documented in the literature [2,3].

For a fixed quadruple \((a,b,c,d)\), the coefficient of \(t^{I(u)+I(v)}\) in \(G_{a,b}(t)G_{c,d}(t)\) is the equivalence-class size. If both \(ab\) and \(cd\) are positive, any nonextreme exponent has at least two distinct decompositions into supported exponents, since both supports are full integer intervals with positive length. Hence the sole singleton cases are the two total extremes: both \(u\) and \(v\) have all zeros before all ones, or both have all ones before all zeros. These are exactly the two final, disjoint positive-run languages displayed in the finding. If \(ab=0\), then \(u\in\mathcal M\) and the class is a singleton exactly when \(v\in\mathcal B\). The symmetric assertion holds when \(cd=0\). This proves the claimed complete regular-language description (including all zero-length boundary cases).

For exact enumeration, put \(A(z)=\sum_{ab=0}z^{a+b}=(1+z)/(1-z)\), \(B(z)=\sum_{a,b\ge1}z^{a+b}=z^2/(1-z)^2\), and let \(T(z)\) enumerate mixed binary singleton words, where \(a,b\ge1\). If \(\min(a,b)=1\), their number is \(ab+1\); if \(a,b\ge2\), it is \(4\). The coefficient sum evaluates to \(T(z)=2z^2(1+z+z^2)/(1-z)^2\). The cases with both binary segments monochromatic contribute \(zA(z)^2\); cases with exactly one mixed segment contribute \(2zA(z)T(z)\); cases with both mixed segments contribute \(2zB(z)^2\). Summing yields
\[
\sum_{n\ge1}S(n)z^n=z\big(A(z)^2+2A(z)T(z)+2B(z)^2\big)
=\frac{z(1+2z^2+4z^3+3z^4-4z^5-4z^6)}{(1-z)^4}.
\]
For \(n\ge7\), all shifted fourth-pole coefficient terms are present; expanding their binomial coefficients yields the displayed cubic. Since there are exactly \(n2^{n-1}\) words in the one-marker slice, the ratio asymptotic follows.

## Verification
The standalone file `artifacts/verify.py` implements an exact full 2-binomial signature for ternary words, enumerates all one-marker words through length \(12\), and compares the resulting singleton counts with an independent composition count and with coefficients extracted from the rational generating function. It also verifies the formal-series identity and the eventual cubic for lengths through \(200\), using exact integer arithmetic only. Run with `python3 artifacts/verify.py` from the root of the extracted package. Successful execution prints `ALL_CHECKS_PASS direct_lengths=1..12 formal_series=1..200`. This is finite corroboration of the general algebraic proof, not a substitute for that proof.

## Relationship to prior work
Rao, Rigo, and Salimov [1] formulate scattered-subsequence-based binomial equivalence. Lejeune, Rigo, and Rosenfeld [2] classify binary 2-binomial singleton words by a regular expression, develop general equivalence-class computations, and prove that the unrestricted ternary singleton language is not context-free. Richomme [3] gives a partition-theoretic account of the binary singleton criterion. The claim here uses the established binary criterion as an input, but adds an exact marker-conditioned factorization of ternary equivalence classes, an all-length generating function, and the contrasting regularity of a natural ternary slice. None of the materially inspected results states this one-marker classification or its rational enumerator. Publication-priority uncertainty remains for unindexed equivalent descriptions.

## Limitations
The formula does not enumerate singleton words with zero, two, or more markers. The marker is an ordinary third alphabet symbol; if marker indistinguishability, contiguous factors, or subsequence lengths exceeding two are imposed, the statement does not apply. Regularity in the one-marker slice does not imply regularity for all ternary singletons. Exhaustive verification is limited to specified finite lengths; the all-length conclusion follows from the mathematical proof. An unindexed prior expression could already imply this count; no independent priority or correctness validation is claimed.

## References
[1] M. Rao, M. Rigo, and P. Salimov, *Avoiding 2-binomial squares and cubes*, arXiv:1310.4743 (first posted 2013-10-17), https://arxiv.org/abs/1310.4743.

[2] F. Lejeune, M. Rigo, and M. Rosenfeld, *On the binomial equivalence classes of finite words*, arXiv:2001.11732 (2020), https://arxiv.org/abs/2001.11732.

[3] G. Richomme, *On some 2-binomial coefficients of binary words: geometrical interpretation, partitions of integers, and fair words*, arXiv:2510.07159 (2025), https://arxiv.org/abs/2510.07159.
