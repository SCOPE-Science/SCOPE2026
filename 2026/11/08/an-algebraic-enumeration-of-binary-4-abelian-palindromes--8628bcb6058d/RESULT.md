# An algebraic enumeration of binary \(4\)-abelian palindromes

## Finding

Let \(a_n\) be the number of binary words \(w\in\{0,1\}^n\) whose multiset of contiguous factors of every length from one through four agrees with the corresponding multiset for the reversed word \(w^{\mathrm R}\). For \(n\ge1\),

\[
\sum_{n\ge1}a_nz^n=2z+4z^3+\frac{2z^2-4z^3+4z^4-8z^6}{\sqrt{(1-2z)(1-2z+4z^6)}}.
\]

The square root has constant coefficient one. In particular,

\[
a_n\sim\frac{2^{n-1}}{\sqrt{\pi n}},\qquad
\mathbb P\{W_n\text{ is }4\text{-abelian palindromic}\}\sim\frac1{2\sqrt{\pi n}},
\]

for a uniform binary word \(W_n\). A structural characterization is part of the theorem: when \(n\ge3\), a word qualifies if and only if its first three symbols equal the reversal of its last three symbols **and** the number of overlapping occurrences of `0011` equals that of `1100`. For \(n=1,2\), ordinary palindromicity is necessary and sufficient. The initial values for \(n=1,\ldots,16\) are

`2, 2, 4, 4, 8, 8, 16, 28, 56, 104, 192, 368, 704, 1356, 2608, 5032`.

## Assumptions and scope

All words are linear (not cyclic), over the fixed labeled binary alphabet, and positions are distinguished. Factor occurrences overlap and are counted with multiplicity. Reversal does not complement symbols. For a finite word \(w\), let \(N_w(v)\) denote the number of contiguous occurrences of \(v\), including overlapping occurrences. The condition is \(N_w(v)=N_{w^{\mathrm R}}(v)\) for every binary \(v\) of length at most four. This is ordinary \(4\)-abelian equivalence to reversal, not equality of scattered-subsequence decks or the number of distinct palindromic factors.

## Proof

**Boundary reduction.** For \(n\ge4\), equality of the factors of lengths three and four for \(w\) and \(w^{\mathrm R}\) forces equality of their first three symbols. Indeed, for any triple \(v\), its total occurrence count minus the number of four-factors having suffix \(v\) is the indicator that the first three symbols equal \(v\). Consequently \(\operatorname{pref}_3(w)=\operatorname{rev}(\operatorname{suff}_3(w))\). Conversely, assume this boundary condition. Factor-count flow identities then imply all length-three and lower count equalities under reversal. For the six non-palindromic reversal pairs of four-letter factors, put

\[
\begin{aligned}
D_1&=N(0001)-N(1000),&D_2&=N(0010)-N(0100),\\
D_3&=N(0011)-N(1100),&D_4&=N(0101)-N(1010),\\
D_5&=N(0111)-N(1110),&D_6&=N(1011)-N(1101).
\end{aligned}
\]

Here \(N=N_w\). Summing extensions of each three-letter factor and using the mirrored boundary gives

\[
(D_1,D_2,D_3,D_4,D_5,D_6)=(0,-h,h,-h,0,-h),\qquad h=D_3.
\]

Thus every four-letter reversal-pair equality holds exactly when \(h=0\). A three-letter word satisfying the mirrored-boundary condition is itself a palindrome; the case \(n=3\) follows directly. For \(n=1,2\), equality with the reversal is equivalent to ordinary palindromicity.

**Exact generating function.** Index the eight binary triples \(s\) and form the weighted de Bruijn transition matrix \(M(t)\). For each bit \(b\), there is one edge from \(s\) to the last three symbols of \(sb\), weighted by \(t\) if \(sb=0011\), by \(t^{-1}\) if \(sb=1100\), and by one otherwise. Let \(s^{\mathrm R}\) mean reversal of the three symbols. With \(u=2-t-t^{-1}\), an exact finite matrix calculation yields

\[
\det(I-zM(t))=1-2z+uz^6
\]

and

\[
\sum_{s\in\{0,1\}^3}(I-zM(t))^{-1}_{s,s^{\mathrm R}}
=\frac{4-4z-8z^3-2uz^5+4uz^6}{1-2z+uz^6}.
\]

These identities are polynomial/rational identities over \(\mathbb Q(z,t)\), independently checkable by multiplying the displayed eight-by-eight matrix, not fitted recurrences. Start with an arbitrary triple, follow the weighted path, require the terminal triple to be the reversed starting triple, and select exponent zero in \(t\). The generating function for lengths at least three is therefore

\[
\operatorname{CT}_{t}\!\left(z^3\sum_s(I-zM(t))^{-1}_{s,s^{\mathrm R}}\right),
\]

where \(\operatorname{CT}_{t}\) extracts the constant term in the variable \(t\). Algebraic rearrangement gives

\[
z^3\sum_s(I-zM(t))^{-1}_{s,s^{\mathrm R}}=
4z^3-2z^2+\frac{2z^2-4z^3+4z^4-8z^6}{1-2z+z^6(2-t-t^{-1})}.
\]

The standard formal constant-term identity

\[
\operatorname{CT}_{t}\frac1{A-B(t+t^{-1})}=\frac1{\sqrt{A^2-4B^2}}
\]

for \(A\) with constant coefficient one and \(B\) with zero constant coefficient, yields the square root \(\sqrt{(1-2z)(1-2z+4z^6)}\). Adding the two length-one words and the two length-two palindromes produces the claimed all-length series.

**Dominant singularity.** The polynomial \(1-2z+4z^6\) has no root in \(|z|\le1/2\). Otherwise \(y=2z\) would satisfy \(|y|\le1\), \(y=1+y^6/16\), and \(|y-1|\le1/16\). The latter bounds \(|\arg y|\le\arctan(1/15)\), hence \(\Re(y^6)>0\), while the equation forces \(\Re y>1\), a contradiction. Therefore the sole singularity on the circle of convergence is the first square-root factor at \(z=1/2\). The numerator of the non-polynomial term equals \(1/8\) at \(z=1/2\), and the other square root equals \(1/4\). The singular expansion is \(\tfrac12(1-2z)^{-1/2}+O(1)\), with other terms less singular. Standard central-binomial coefficient asymptotics give the asserted limit.

## Verification

Run `python verify.py` with SymPy installed. It constructs the specified eight-state matrix and checks the determinant and rational trace **symbolically**, then computes the first sixteen coefficients of the algebraic generating function. Independently, it enumerates all \(131070\) binary words of lengths one through sixteen, directly compares factor-frequency counters against reversed words, checks the boundary/imbalance equivalence for each word of length at least three, and matches every enumerated count with the generating-function coefficients. The observed completion marker is `VERIFY_OK symbolic_det_trace_gf, finite_n=1..16`.

## Relationship to prior work

Karhumäki and Puzynina (2014) introduced and studied \(k\)-abelian palindromic richness and poorness, including quadratic factor-richness and existence/nonexistence questions. Cassaigne, Karhumäki and Puzynina's publicly accessible 2016 presentation develops equivalent definitions, the \((4,2)\) poorness case and further richness questions. Those results concern properties of factors inside words or existence of infinite words, not the total number of length-\(n\) binary words equivalent to their reversals under \(4\)-abelian equivalence. The present result enumerates this finite language, exhibits the first non-boundary constraint at level four, and establishes its exponential-square-root probability law. The accessible text does not establish priority against inaccessible complete versions of the closest publications; this remains a limitation.

## Limitations

No classification is asserted for alphabets larger than two or for levels greater than four. No claim is made about maximizing distinct palindromic factors within a word. Full text of the 2014 conference chapter and a later related journal treatment could not be inspected through the available sources, so an equivalent result hidden there or in unindexed literature remains a historical-priority risk. The proof and exact arithmetic verification do not constitute independent mathematical validation.

## References

1. J. Karhumäki and S. Puzynina, *On k-Abelian Palindromic Rich and Poor Words*, DLT 2014, LNCS 8633, pp. 191–202. DOI: https://doi.org/10.1007/978-3-319-09698-8_17 (proceedings eBook release publicly listed as 2014-08-18).
2. J. Cassaigne, J. Karhumäki and S. Puzynina, *On k-abelian palindromes*, public presentation (2016), https://paperzz.com/doc/8313879/on-k-abelian-palindromes ; public talk recorded 2016-03-16 and published 2016-03-31, https://www.carmin.tv/en/collections/combinatorics-on-words-combinatoire-des-mots/video/on-k-abelian-palindromes .
3. J. Cassaigne, J. Karhumäki and S. Puzynina, *On k-abelian palindromes*, *Information and Computation* (2018), DOI: https://doi.org/10.1016/j.ic.2018.04.001 (full text unavailable in this review).
