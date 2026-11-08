# Exact deletion-ambiguity spectra and phase ordering for cyclic alphabet words

## Finding

Fix integers \(q\ge2\), \(n\ge1\), and \(1\le h<q\). Let the alphabet be \(\Sigma_q=\{0,1,\ldots,q-1\}\), and form the two words of length \(n\)
\[
U_{q,n}[i]=i\bmod q,\qquad V_{q,n,h}[i]=(i+h)\bmod q,\qquad 0\le i<n.
\]
For a word \(w\), let \(D_t(w)\) be the **set of distinct** words obtained by deleting exactly \(t\) positions. Define
\[
P_q(x)=x+x^2+\cdots+x^q,\qquad
F_{q,k}(T)=\sum_{s=0}^{T}[x^s]P_q(x)^k,
\]
where \(F_{q,k}(T)=0\) for \(T<0\). In particular, \(F_{q,0}(T)=1\) exactly when \(T\ge0\).

**Theorem (all-length common deletion spectrum).** For every \(0\le t\le n\), write \(\ell=n-t\). Then
\[
\left|D_t(U_{q,n})\cap D_t(V_{q,n,h})\right|=
\begin{cases}
1,&\ell=0,\\[3pt]
\displaystyle\sum_{j=h+1}^{q}F_{q,\ell-1}(n-j)
+\sum_{j=q-h+1}^{q}F_{q,\ell-1}(n-j),&1\le\ell\le n.
\end{cases}
\]
Thus, if \(A_{q,n,h}(\ell)\) denotes this number with \(\ell\) retained symbols, its entire length enumerator has the rational coefficient representation
\[
\sum_{\ell=0}^{n} A_{q,n,h}(\ell)z^\ell
=1+z[x^n]\frac{B_{q,h}(x)}{(1-x)(1-zP_q(x))},
\qquad
B_{q,h}(x)=\sum_{j=h+1}^{q}x^j+\sum_{j=q-h+1}^{q}x^j.
\]
The coefficient extraction is formal; the right side is a polynomial in \(z\) of degree at most \(n\).

**Phase-order theorem.** Put \(d=\min\{h,q-h\}\). The full profile is symmetric under \(h\leftrightarrow q-h\), and it is coefficientwise nonincreasing with circular phase distance:
\[
A_{q,n,1}(\ell)\ge A_{q,n,2}(\ell)\ge\cdots\ge
A_{q,n,\lfloor q/2\rfloor}(\ell)
\quad(0\le\ell\le n).
\]
For each \(1\le d<\lfloor q/2\rfloor\) with \(n>d\), the comparison between distances \(d\) and \(d+1\) is strict at \(\ell=n-d\). Moreover,
\[
\operatorname{LCS}(U_{q,n},V_{q,n,h})=\max\{0,n-d\}.
\]
If \(n>d\), there are exactly two distinct longest common subsequences when \(q=2h\), and exactly one otherwise; if \(n\le d\), the empty word is the unique longest common subsequence. In particular, the entire deletion-overlap profile depends on the phase only through its circular distance \(d\).

## Assumptions and scope

The alphabet symbols are distinct and used in the fixed natural cyclic order. Both centers have the same arbitrary length \(n\), which need not be a multiple of \(q\); they are truncations of an infinite repetition of the length-\(q\) cyclic permutation, at phase offsets \(0\) and \(h\). The formula counts **different received words**, not deletion-position masks or embedding multiplicities. The phase-order statement is pointwise in every deletion radius, including radii at which both intersections are empty or coincide.

## Proof

**1. Greedy embedding criterion.** Work with zero-based alphabet residues and one-based word positions. For any phase \(p\in\{0,\ldots,q-1\}\), the first occurrence of symbol \(r\) in the phase-\(p\) infinite periodic word is at position
\[
\beta_p(r)=1+((r-p)\bmod q).
\]
For consecutive chosen symbols \(a,b\), the positive jump from an occurrence of \(a\) to the next occurrence of \(b\) equals the unique number \(\delta_q(a,b)\in\{1,\ldots,q\}\) congruent to \(b-a\) modulo \(q\). This holds also for repetitions of a symbol, where the jump is \(q\). Thus a nonempty received word \(w=(w_1,\ldots,w_\ell)\) is a subsequence of the phase-\(p\) length-\(n\) word if and only if the earliest possible last position
\[
\beta_p(w_1)+\sum_{i=2}^{\ell}\delta_q(w_{i-1},w_i)
\]
does not exceed \(n\). Necessity follows from the forward order of every embedding; sufficiency follows by making each choice greedily at that earliest position. The jump sum is identical for the two phases.

**2. Threshold multiset and distinctness.** Writing \(r=w_1\), the simultaneous first-position requirement is
\[
\alpha_h(r)=\max\{\beta_0(r),\beta_h(r)\}
=\begin{cases}r+q-h+1,&0\le r<h,\\r+1,&h\le r<q.\end{cases}
\]
As \(r\) traverses all alphabet symbols, this gives exactly the multiset of thresholds
\[
M_h=\{h+1,h+2,\ldots,q\}\mathbin{\dot\cup}
\{q-h+1,q-h+2,\ldots,q\},
\]
where \(\dot\cup\) is a multiset union (overlaps count twice). Fixing \(w_1=r\), the next \(\ell-1\) positive jumps may be selected independently from \(\{1,\ldots,q\}\). Conversely, the initial symbol and this jump sequence determine exactly one received word by reduction modulo \(q\); no distinct-word overcounting occurs. Requiring the sum of jumps to be at most \(n-\alpha_h(r)\) gives \(F_{q,\ell-1}(n-\alpha_h(r))\). Summing over the threshold multiset proves the exact formula. For \(\ell=0\), the empty word is always present once.

**3. Rational coefficient extraction.** By the elementary partial-sum identity
\[
F_{q,k}(n-j)=[x^{n-j}]\frac{P_q(x)^k}{1-x},
\]
the sum over all nonempty lengths, weighted by \(z^\ell\), equals
\[
z[x^n]\frac{B_{q,h}(x)}{1-x}
\sum_{k\ge0}\bigl(zP_q(x)\bigr)^k
=z[x^n]\frac{B_{q,h}(x)}{(1-x)(1-zP_q(x))}.
\]
Only finitely many terms contribute to the coefficient of \(x^n\), so no analytic convergence assumptions are needed.

**4. Phase dominance.** Replacing \(h\) by \(q-h\) merely exchanges the two intervals in \(M_h\), proving profile symmetry. For \(1\le d<\lfloor q/2\rfloor\), let \(C_d(s)\) be the number of elements of \(M_d\) no greater than \(s\). Then for every integer \(s\),
\[
C_d(s)=\max\{0,s-d\}+\max\{0,s-q+d\}\qquad (1\le s\le q),
\]
and hence
\[
C_d(s)-C_{d+1}(s)=
\mathbf1_{\{s\ge d+1\}}-\mathbf1_{\{s\ge q-d\}}\ge0.
\]
The final inequality uses \(d+1<q-d\). Therefore the sorted thresholds in \(M_d\) are coordinatewise no larger than the sorted thresholds in \(M_{d+1}\). Since \(F_{q,\ell-1}(n-j)\) is nonincreasing as a function of \(j\), the length-\(\ell\) intersection counts satisfy \(A_{q,n,d}(\ell)\ge A_{q,n,d+1}(\ell)\). The symmetry already proved gives the full ordering.

**5. LCS cutoff and strictness.** The least element of \(M_h\) is \(d+1\), attained by one initial symbol unless \(2h=q\), when it is attained by two. Every jump is at least one, and the all-one jump sequence is unique. Consequently a common word of positive length \(\ell\) exists exactly when \(d+1+(\ell-1)\le n\), yielding the stated LCS and its multiplicity. For neighboring circular distances \(d<d+1\le\lfloor q/2\rfloor\), when \(n>d\), the former has a common word of length \(n-d\) but the latter has none; this proves the asserted strict inequality.

## Verification

The standalone `checker.py` builds deletion descendants directly as sets of coordinate-subsequence tuples and independently computes the proposed polynomial formula from bounded-composition coefficients. It checks all \(q\in\{2,\ldots,8\}\), \(n\in\{1,\ldots,10\}\), \(1\le h<q\), and \(0\le\ell\le n\): 280 parameter profiles and 1,820 length entries. It additionally verifies longest-common-subsequence lengths, longest-word multiplicities, phase symmetry and coefficientwise phase dominance. A representative nontrivial case at \(q=6,n=12\) has deletion-descendant profiles, indexed by retained length \(0\) through \(12\),
\[
\begin{aligned}
h=1:&\ (1,6,36,140,320,467,467,331,165,55,11,1,0),\\
h=2:&\ (1,6,36,128,247,296,236,128,46,10,1,0,0),\\
h=3:&\ (1,6,36,124,222,240,166,72,18,2,0,0,0).
\end{aligned}
\]
Finite enumeration verifies examples and is not used to infer the infinite theorem. The five proof steps above establish the claims for all parameters.

## Relationship to prior work

Sun and Ge (2026) study general intersections of deletion balls and establish finite/asymptotic **upper bounds**, under additional lower-order-intersection and run-count constraints. Their first public preprint is dated June 24, 2026. Their primary paper includes broad common-subsequence bounds but does not give the exact all-length overlap profiles or their phase order for truncated cyclic alphabet permutations. Its general bounds alone do not imply those equalities.

Gaevoy, Zolotov and Tiskin (2025) give an algorithm for LCS scores of doubly periodic strings. Their framework covers the two input strings as periodic strings for **LCS length only**, but neither counts the number of distinct longest words nor determines every lower-length common-descendant count or the coefficientwise phase comparison. The particular LCS formula here can also be obtained from general LCS algorithms; the complete intersection profile is the additional content.

Wang, Li and Fu (2026, preprint submitted September 15) determine extremal intersection sizes for pairs satisfying a prescribed minimum deletion distance in the nonbinary reconstruction problem, and classify extremizers. A maximization over pairs does not specify these phase-resolved **individual-pair** intersection profiles; moreover, adjacent phases have deletion distance one and need not satisfy their separation hypothesis. Its original full text was inaccessible during comparison, leaving a residual priority risk.

## Limitations

Only equal-length truncations of a single fixed cyclic permutation on an alphabet with pairwise distinct symbols are considered. The theorem does not determine arbitrary pairs of periodic words, insertion-ball intersections, optimal sizes of reconstruction codes, or the number of deletion masks producing an individual descendant. It is a self-contained mathematical claim whose historical priority and independent validation have not been certified.

## References

1. Y. Sun and G. Ge, *Extremal Deletion-Ball Intersections under Run-Count and Lower-Order Deletion-Ball Intersection Constraints*, arXiv:2606.25822v1, first posted 2026-06-24. https://arxiv.org/abs/2606.25822 ; accessible PDF: https://pdfs.assets.alphaxiv.org/2606.25822v1.pdf
2. N. Gaevoy, B. Zolotov and A. Tiskin, *Doubly-Periodic String Comparison*, CPM 2025, LIPIcs 331, Article 13. https://doi.org/10.4230/LIPIcs.CPM.2025.13 ; full text: https://drops.dagstuhl.de/storage/00lipics/lipics-vol331-cpm2025/html/LIPIcs.CPM.2025.13/LIPIcs.CPM.2025.13.html
3. X. Wang, H. Li and F.-W. Fu, *On Sequence Reconstruction Problem for q-ary Deletion Channels*, arXiv:2609.16837, first posted 2026-09-15. https://arxiv.org/abs/2609.16837
