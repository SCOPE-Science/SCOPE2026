# Maximal commutative subsemigroups of free nilpotent word semigroups: a parity classification

## Finding

For every alphabet \(A\) of size \(a\ge2\) and every integer \(N\ge1\), let \(S_{a,N}\) consist of zero and all nonempty words over \(A\) of length at most \(N\), with concatenation truncated to zero when the resulting length exceeds \(N\). All inclusion-maximal commutative subsemigroups of \(S_{a,N}\) are classified explicitly below. In particular, their number is
\[
\sum_{k=1}^{\lfloor N/2\rfloor}a^k+\mathbf1_{N\text{ odd}}.
\]
Their maximum possible cardinality is
\[
1+\sum_{j=\lfloor N/2\rfloor+1}^{N}a^j+\mathbf1_{N\text{ even}}.
\]
For odd \(N\), there is exactly one maximum; for even \(N\), there are exactly \(a^{N/2}\) maxima. The classification also yields the full size enumerator and element-centralizer spectrum, and an exact formula for ordered commuting pairs.

## Assumptions and scope

Take the free semigroup \(A^+\) on \(A\), without an empty word, and its Rees quotient by the ideal of words of length at least \(N+1\). Thus the product of two nonzero words \(u,v\) is \(uv\) if \(|u|+|v|\le N\), and zero otherwise. Let \(m=\lfloor N/2\rfloor\). Each nonempty word \(w\) has a unique primitive root \(p(w)\), meaning \(w=p(w)^h\) for a maximal positive integer \(h\), and \(p(w)\) is not a proper power. Put \(d(w)=|p(w)|\).

For \(1\le k\le m\) and \(w\in A^k\), define
\[
C_w=\{0\}\cup\{v\in A^+:N-k<|v|\le N\}\cup
\{p(w)^r:r\ge1,\ k\le r d(w)\le N-k\}.
\]
When \(N=2m+1\) is odd, also define
\[
C_*=\{0\}\cup\{v\in A^+:m+1\le|v|\le N\}.
\]
The precise claim is that these and only these are inclusion-maximal commutative subsemigroups; all are distinct. In particular, this is a statement about *maximal by inclusion*, not merely the largest possible order. The empty sums in the formulas below are interpreted as zero, and \(0^0=1\) in computational evaluations where necessary.

Define the primitive-word polynomial \(P_a(d)=\sum_{e\mid d}\mu(e)a^{d/e}\), where \(\mu\) is the number-theoretic Möbius function. Then the multiset of maximal-family cardinalities is encoded exactly by
\[
\begin{aligned}
F_{a,N}(t)={}&\mathbf1_{N\text{ odd}}\,t^{1+\sum_{j=m+1}^{N}a^j}\\
&+\sum_{k=1}^{m}\sum_{d\mid k}P_a(d)
 t^{1+\sum_{j=N-k+1}^{N}a^j+\lfloor(N-k)/d\rfloor-\lfloor(k-1)/d\rfloor}.
\end{aligned}
\]
For every nonzero word \(w\) of length \(k\), its centralizer is exactly
\[
Z_{S_{a,N}}(w)=\{0\}\cup\{v:N-k<|v|\le N\}\cup\{p(w)^r:r d(w)\le N-k\},
\]
so its size is \(1+\sum_{j=N-k+1}^{N}a^j+\lfloor(N-k)/d(w)\rfloor\). The zero element has centralizer \(S_{a,N}\). For each \(k\) and \(d\mid k\), exactly \(P_a(d)\) words have these parameters, giving the complete centralizer-size multiset (combine coincident numerical sizes if desired). With \(s=1+\sum_{j=1}^{N}a^j\), the exact ordered commuting-pair count is
\[
K(a,N)=s^2-\sum_{\substack{i,j\ge1\\i+j\le N}}\bigl(a^{i+j}-a^{\gcd(i,j)}\bigr).
\]

## Proof

**1. Commutation dichotomy.** If \(|u|+|v|>N\), the two products \(uv\) and \(vu\) both vanish, so \(u,v\) commute. Otherwise the products remain distinct free words unless \(uv=vu\) as words. The classical free-word commutation lemma says this equality holds exactly when \(u,v\) are positive powers of one primitive word (equivalently \(p(u)=p(v)\)). One proof compares the overlapping prefixes of \(uv\) and \(vu\) and iteratively uses their common prefix to apply the Euclidean algorithm to the two lengths, reducing to a common period of length \(\gcd(|u|,|v|)\). Conversely, powers of the same word commute.

**2. Each proposed family is commutative and closed.** Within \(C_w\), every word of length at most \(N-k\) is a power of \(p(w)\), hence these shorter words commute, even if their product is truncated. Any such word has length at least \(k\), so its product with any member of the complete long-word tier \(\{|v|>N-k\}\) vanishes. Products of long words also vanish since \(2(N-k+1)>N\) for \(k\le N/2\). A nonzero product of two short powers is again a power of \(p(w)\) and either has length at most \(N-k\) or lies in the included long tier. Thus \(C_w\) is a commutative subsemigroup. For odd \(N\), every two words of length at least \(m+1\) have total length at least \(2m+2>N\), showing the same for \(C_*\).

**3. Each proposed family is inclusion-maximal.** Consider \(C_w\) with \(|w|=k\le m\). An omitted word \(v\) with \(k\le|v|\le N-k\) is not a positive power of \(p(w)\) of the requisite length. Since \(k+|v|\le N\), it fails to commute with \(w\). If instead \(1\le |v|=h<k\), choose any word \(u\) of length \(j=N-k+1\). Here \(h+j\le N\). For a fixed \(v\), at most one word \(u\) of any specified length \(j\) commutes with it, because a commuting \(u\) would have to be the unique power of \(p(v)\) with that length. As \(a^j\ge2\), at least one such \(u\) lies in \(C_w\) but does not commute with \(v\). All other nonzero words are included, hence \(C_w\) is maximal. For odd \(N=2m+1\), an excluded word \(v\) has length \(h\le m\). It fails to commute with some word of length \(m+1\) already in \(C_*\), by the same argument, since \(h+m+1\le N\). When \(m=0\), \(C_*=S_{a,1}\), so maximality is immediate.

**4. Exhaustion.** Let \(C\) be a maximal commutative subsemigroup. Zero commutes with all, so \(0\in C\). If \(C\ne\{0\}\), choose a nonzero word \(w\in C\) of minimum length \(k\). If \(k\le m\), every \(v\in C\) of length at most \(N-k\) must commute with \(w\) without truncation, and hence must be a power of \(p(w)\). Since \(|v|\ge k\), we obtain \(C\subseteq C_w\). Maximality and step 2 give equality. If \(k>m\) and \(N\) is odd, then \(C\subseteq C_*\) and maximality gives equality. If \(k>m\) and \(N=2m\) is even, every word of \(C\) has length at least \(m+1\), so adjoining any word of length \(m\) preserves commutativity and generates a strictly larger commutative subsemigroup, contradicting maximality. The singleton \(\{0\}\) is not maximal, since the semigroup has nonzero words. Therefore the list is exhaustive.

**5. Distinctness and enumerations.** In \(C_w\) the unique word of shortest positive length \(k\) is \(w\). This determines \(w\) from \(C_w\), and distinguishes it from \(C_*\), whose shortest positive length is \(m+1\). Counting words \(w\) by their length gives \(\sum_{k=1}^m a^k+\mathbf1_{N\text{ odd}}\) families. A word of length \(k\) has primitive-root length \(d\mid k\); there are precisely \(P_a(d)\) such words, by Möbius inversion of \(a^k=\sum_{d\mid k}P_a(d)\). The number of short powers in \(C_w\) is \(\lfloor (N-k)/d\rfloor-\lfloor (k-1)/d\rfloor\); adding the long tier and zero gives \(F_{a,N}\). The centralizer formula follows from step 1 without the lower bound \(|v|\ge k\). For a pair of word lengths \(i,j\) with \(i+j\le N\), the commuting pairs are exactly those \((u,v)\) determined by an arbitrary length-\(\gcd(i,j)\) word \(z\) through \(u=z^{i/\gcd(i,j)}\), \(v=z^{j/\gcd(i,j)}\). There are \(a^{\gcd(i,j)}\) such pairs; all \(a^{i+j}\) are noncommuting except these. Summing these losses over all eligible lengths, from the total \(s^2\) ordered pairs, proves \(K(a,N)\).

**6. Maximum orders and parity.** The common complete tail \(T=\{0\}\cup\{v:|v|\ge m+1\}\) has size \(1+\sum_{j=m+1}^N a^j\). When \(N=2m+1\), \(C_*=T\). A family \(C_w\) with \(|w|=k\le m\) includes the entire tail above length \(N-k\), while at intermediate lengths \(m+1,\ldots,N-k\) it includes only certain powers of \(p(w)\). Therefore \(|T|-|C_w|\) equals the sum of the full numbers of words at those intermediate lengths, minus the total number of selected powers at lengths \(k,\ldots,N-k\). This sum includes at least \(a^{m+1}\), while the number of selected powers is at most \(N-2k+1\le2m\). Since \(a^{m+1}>2m\) for \(m\ge1\) and \(a\ge2\), \(|C_w|<|T|\). When \(N=2m\), for \(k=m\) the long tier is exactly the tail of lengths \(m+1,\ldots,N\), and the sole short word is \(w\), giving size \(|T|+1\). For \(k<m\), the difference \((|T|+1)-|C_w|\) equals \(1\) plus the total number of words in lengths \(m+1,\ldots,N-k\), minus the total number of short powers selected in lengths \(k,\ldots,N-k\). The full-word contribution includes at least \(a^{m+1}\) words, while the number of short powers is at most \(N-2k+1\le2m-1\). Thus \(|C_w|<|T|+1\). There are \(a^m\) words of length \(m\), proving the sharp even case. The case \(N=1\) is directly \(C_*=S_{a,1}\).

## Verification

The accompanying `CHECKER.py` independently constructs the truncated multiplication table, evaluates centralizers by direct products, enumerates all maximal cliques in the pairwise-commutation graph (including the zero element), and compares the resulting families exactly with the stated classification. It also independently counts commuting pairs by direct multiplication and by the closed length-gcd formula. The recorded output `CHECKER_OUTPUT.txt` verifies all eight cases with \((a,N)=(2,1),(2,2),(2,3),(2,4),(2,5),(3,1),(3,2),(3,3)\); these test sets have up to \(63\) elements. The mathematical proof, not finite enumeration, establishes the statement for every \(a\ge2,N\ge1\). Reproduce with `python CHECKER.py` using Python 3 (standard library only).

## Relationship to prior work

Jackson and Kilibarda establish the untruncated free-word commuting criterion (their Lemma 16 and subsequent theorem on commutative subsemigroups), a prerequisite here, but that result alone does not classify maximal commuting families *after* long products collapse to zero. Steindl explicitly introduces the same free nilpotent Rees quotient \(\mathrm{FN}_{N+1}(A)\) in his Section 2, but studies finite relatedness and nilpotent monoids rather than maximal commutative subsemigroups. Bauer and Greenfeld construct monomial semigroups with prescribed commuting-graph behavior, without classifying the above uniform length-ideal quotients. Published work on commuting graphs of symmetric inverse semigroups and on commutative nilpotent transformation semigroups concerns different ambient structures. The primitive-root step is established classical mathematics, not an originality claim; the contribution assessed is the exhaustive family classification, parity-rigid extrema, and complete derived enumerators for the truncated quotient.

## Limitations

The theorem requires a finite alphabet with at least two letters, a *uniform length cutoff*, and no identity element. It does not assert a classification for arbitrary monomial Rees ideals, arbitrary nilpotent semigroups, or infinite alphabets. Finite tests are consistency checks, not a proof. Exhaustive historical priority cannot be certified: related treatments of truncated free-word commutation may exist under different terminology, and an earlier inverse-semigroup Rees-quotient abstract was not sufficient to assess its full text.

## References

1. D. A. Jackson and V. Kilibarda, *Ends for monoids and semigroups*, Journal of the Australian Mathematical Society **87** (2009), 101–127, DOI: https://doi.org/10.1017/S1446788708081020 (published online 2009-08-01; free-word commutation lemma).
2. M. Steindl, *Not all nilpotent monoids are finitely related*, Algebra Universalis **85** (2024), article 13, DOI: https://doi.org/10.1007/s00012-023-00841-5 (Section 2: definition of free nilpotent semigroup).
3. T. Bauer and B. Greenfeld, *Commuting graphs of boundedly generated semigroups*, arXiv:1710.05250 (2017), https://arxiv.org/abs/1710.05250.
4. J. Araújo, W. Bentz and J. Konieczny, *The commuting graph of the symmetric inverse semigroup*, arXiv:1205.1664 (2012), https://arxiv.org/abs/1205.1664.
5. *Commutative nilpotent transformation semigroups*, DOI: https://doi.org/10.1007/s00233-024-10444-8 (different ambient semigroup).
