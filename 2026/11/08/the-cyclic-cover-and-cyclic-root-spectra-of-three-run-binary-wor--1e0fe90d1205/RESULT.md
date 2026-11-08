# The cyclic-cover and cyclic-root spectra of three-run binary words

## Finding

Let \(X=0^a1^b0^c\), where \(a,c\ge1\) and \(b\ge2\), and put \(n=a+b+c\). A factor \(V\) of \(X\) is a *cyclic cover* if occurrences of its conjugates (cyclic rotations) jointly contain every position of \(X\). A *cyclic root* is a prefix \(V\) for which \(X\) is a concatenation of conjugates of \(V\), all of length \(|V|\). Write \(\mathcal C(X)\) for the set of lengths of cyclic covers, and \(\mathcal R(X)\) for the set of lengths of cyclic roots.

**Theorem.** The complete cyclic-cover length set is the terminal interval
\[
\mathcal C(X)=\{\ell_0,\ell_0+1,\ldots,n\},\qquad
\ell_0=\begin{cases}
 a+\lceil b/2\rceil,&a=c,\\
 b+\max(a,c),&a\ne c.
\end{cases}
\]
For each \(\ell\in\mathcal C(X)\), let \(d_X(\ell)\) count *distinct factor strings* of length \(\ell\) that are cyclic covers (not just rotation classes). Then
\[
d_X(\ell)=\begin{cases}
 2,&a=c\text{ and }\ell<a+b,\\
 n-\ell+1,&\text{otherwise}.
\end{cases}
\]
Consequently the number of distinct cyclic-cover factors, summed over all lengths, is
\[
\sum_{\ell}d_X(\ell)=\begin{cases}
 \dfrac{(a+1)(a+2)}2+2\lfloor b/2\rfloor,&a=c,\\
 \dfrac{(\min(a,c)+1)(\min(a,c)+2)}2,&a\ne c.
\end{cases}
\]
The complete cyclic-root spectrum is
\[
\mathcal R(X)=\begin{cases}
\{n/2,n\},&a=c\text{ and }b\text{ is even},\\
\{n\},&\text{otherwise}.
\end{cases}
\]
In the first case \(n\) is even. Thus symmetric flanks produce more short cyclic covers and, when the middle run is even, an additional cyclic root.

As a sharp sensitivity example, at \(X=0^m1^{2m}0^m\) the shortest cyclic-cover length is \(2m\); extending just the right flank by one zero changes it to \(3m+1\). The minimum jumps by \(m+1\) after a one-letter insertion.

## Assumptions and scope

All words and factors are linear, with no wraparound occurrence in the text itself; rotations are permitted only for the covering *pattern*. The alphabet consists of two different letters, displayed as \(0,1\). The parameters range independently over integers \(a,c\ge1\), \(b\ge2\); the excluded singleton-middle-run example \(0^a10^a\) was already described in prior work. A cyclic cover of length \(\ell\) means any factor string \(V\) whose rotations collectively cover every text position. Every such factor is conjugate to the length-\(\ell\) prefix, so counting distinct cover lengths counts rotation classes, while \(d_X(\ell)\) counts distinct factors themselves. A cyclic root may have just one block, so \(n\) always belongs to \(\mathcal R(X)\).

## Proof

**1. The two endpoints impose a conjugacy condition.** Any cover of length \(\ell\) must have an occurrence of a rotation starting at position zero: no other length-\(\ell\) factor contains that position. Likewise some rotation occurs ending at the last position. Therefore the length-\(\ell\) prefix and suffix must be conjugate and, in particular, must have equal numbers of \(1\)'s. The respective numbers of \(1\)'s are
\[
f_a(\ell)=\min\{b,\max\{0,\ell-a\}\},\qquad
f_c(\ell)=\min\{b,\max\{0,\ell-c\}\}.
\]
If \(a\ne c\), these are equal only for \(\ell\le\min(a,c)\) or \(\ell\ge b+\max(a,c)\). The first range consists entirely of zero-patterns and cannot cover the middle ones. Conversely, if \(\ell\ge b+\max(a,c)\), every length-\(\ell\) factor contains the entire run \(1^b\), and its other \(\ell-b\) symbols are zeros split across the ends. Every such factor is a cyclic rotation of every other one. In particular the prefix and suffix rotations together cover the text, since \(2\ell\ge n\). This proves the asymmetric length formula.

**2. The symmetric threshold.** Suppose \(a=c\). If \(\ell\le a\), every rotation of the prefix is all zeros, so no cyclic cover is possible. If \(a<\ell<a+b\), write \(r=\ell-a\). The prefix \(0^a1^r\) and suffix \(1^r0^a\) are rotations and cover respectively the first and last \(r\) letters of the central \(1^b\). They cover all positions exactly when \(2r\ge b\). If \(2r<b\), any occurrence of a rotation of \(0^a1^r\) contains exactly \(r\) ones and at least one zero. It cannot reach a central \(1\) positioned more than \(r\) letters from either edge of the central run: to reach a zero on either flank it would have to include at least \(r+1\) consecutive ones. Such a central position exists, so no cover is possible. For \(\ell\ge a+b\), both prefix and suffix contain the full run \(1^b\), are conjugate, and overlap. Thus the symmetric threshold is exactly \(a+\lceil b/2\rceil\).

**3. Distinct cover factors.** In the asymmetric case every admissible length is at least \(b+\max(a,c)\); in the symmetric case every length at least \(a+b\) has the same property. All \(n-\ell+1\) factors of such a length contain the single entire \(1^b\) run and are mutually conjugate. They are distinct: their numbers of initial zeros differ with their starting positions. At a symmetric admissible shorter length \(\ell=a+r<a+b\), a factor conjugate to the prefix must have precisely \(a\) zeros and \(r<b\) ones. Only the prefix \(0^a1^r\) and suffix \(1^r0^a\) can do so. Both are covers by Step 2, giving precisely two distinct cover factors. Summing the indicated finite arithmetic progressions proves the total counts.

**4. Cyclic roots.** If \(\ell\) is a root length, then \(\ell\mid n\) and all \(n/\ell\) consecutive length-\(\ell\) blocks have the same positive number of zeros and the same positive number of ones. There is only one contiguous run of ones and two outer zero runs. For three or more blocks, either some block misses all ones or an interior block lies entirely in ones, contradicting the required common positive counts for both symbols. Thus at most two blocks are possible. With exactly two blocks, equal counts force \(b\) even and the cut between blocks to lie halfway through \(1^b\), which forces \(a=c\). Conversely \(0^a1^{b/2}\) and \(1^{b/2}0^a\) are conjugate when \(b\) is even, giving the half-length root. The one-block root is always present.

## Verification

The standalone standard-library script `verify_cyclic_three_runs.py` independently constructs the conjugates of every prefix, enumerates all length-matched occurrences and their covered positions, counts distinct covering factor strings, and checks all equal-block cyclic roots. It compares these direct definitions with the closed formulas on every triple \(1\le a,b,c\le10\), plus 250 seeded larger triples with entries at most \(25\): 1,250 parameter triples, covering 26,029 candidate lengths. All comparisons passed. These finite checks illustrate boundary handling and are not substituted for the unrestricted proof above. Run `python3 verify_cyclic_three_runs.py` from the extracted package directory.

## Relationship to prior work

Grossi, Iliopoulos, Jansson, Lim, Sung and Zuba introduced the distinct-length cyclic-cover problem, established the endpoint-conjugacy observation, and gave a general algorithm. Their original manuscript explicitly treats the special symmetric singleton-middle-run family \(0^m10^m\), whose covers are represented by lengths \(m+1\) through \(2m+1\). That prior case is acknowledged and excluded by the assumption \(b\ge2\). Iliopoulos, Kociumaka, Radoszewski, Rytter, Waleń and Zuba later gave linear-time algorithms for cyclic roots and covers of arbitrary strings. These algorithms compute finite-instance answers but do not directly state the above parameter-uniform two-transition classification, length-refined factor census, root dichotomy, or one-letter instability. No matching closed classification was located in the examined sources; external priority has not been independently established.

## Limitations

The theorem applies only to binary words with exactly two letter transitions and a central run of length at least two. It does not classify arbitrary words, words with more runs, or approximate covers. The general algorithms and the singleton-middle-run case are earlier results, not claimed as new. The absence of an equivalent in the examined literature or searchable records is not a proof of global novelty. Independent review is not yet available.

## References

1. R. Grossi, C. S. Iliopoulos, J. Jansson, Z. Lim, W.-K. Sung and W. Zuba, *Finding the Cyclic Covers of a String*, WALCOM 2023, LNCS 13973, 139–150, DOI: 10.1007/978-3-031-27051-2_13, author manuscript: https://ir.cwi.nl/pub/32986/32986.pdf (public repository entry dated 2023-03-13).
2. C. S. Iliopoulos, T. Kociumaka, J. Radoszewski, W. Rytter, T. Waleń and W. Zuba, *Linear-Time Computation of Cyclic Roots and Cyclic Covers of a String*, CPM 2023, LIPIcs 259, Article 15, DOI: 10.4230/LIPIcs.CPM.2023.15, https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.CPM.2023.15.
3. R. Grossi et al., *Finding the cyclic covers of a string*, Information Processing Letters 191 (2026), 106594, final open-access version: https://ir.cwi.nl/pub/35209/35209.pdf (online 2025-06-16; later version of Reference 1, not a distinct early-publication date).
