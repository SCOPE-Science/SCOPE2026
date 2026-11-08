# Abelian coincidence islands for equal-period binary run cycles

## Finding

Let \(a,b,c,d\) be positive integers with \(a+b=c+d=L\), and consider the right-infinite periodic words
\[
X=(0^a1^b)^\omega,\qquad Y=(0^c1^d)^\omega.
\]
For \(n\ge1\), let \(C(n)\) be the number of **distinct Parikh vectors** represented by both a length-\(n\) contiguous factor of \(X\) and a length-\(n\) contiguous factor of \(Y\). Thus \(C(n)>0\) exactly when the two words have common *Abelian* factors of length \(n\): the two chosen factors need not have their letters in the same order.

If \(a=c\), then \(b=d\), the two words coincide, and every positive length occurs. For \(n=tL+r\), with integers \(t\ge0\), \(0\le r<L\), one has
\[
C(n)=\min(a,r)-\max(0,r-b)+1.
\]

If \(a\ne c\), exchange \(X\) and \(Y\) if needed so that \(a>c\). Define \(\delta=a-c=d-b>0\) and \(T=\lfloor\min(b,c)/\delta\rfloor\). Then, for all \(n=tL+r\ge1\),
\[
\boxed{C(n)=\max\!\left\{0,\ 1+\min(c,r)-\max(0,r-b)-t\delta\right\}.}
\]
Moreover, the **complete set of admissible positive lengths** is the disjoint union of integer intervals
\[
\boxed{\{n\ge1:C(n)>0\}
=\bigcup_{t=0}^{T}\bigl([\,t(a+d),\ (t+1)(b+c)\,]\cap\mathbb Z_{\ge1}\bigr).}
\]
The gap between intervals indexed by \(t\) and \(t+1\), for \(0\le t<T\), contains exactly \(2(t+1)\delta-1\) forbidden positive lengths. In particular the longest common Abelian factor has length
\[
\boxed{L_{\mathrm{Ab}}=(T+1)(b+c),}
\]
and the number of distinct positive *lengths* admitting common Abelian factors is
\[
\boxed{(T+1)(b+c+1-\delta T)-1.}
\]
The latter count is of admissible lengths, not of distinct factor words or Parikh vectors.

## Assumptions and scope

A factor means a finite contiguous substring, at any nonnegative starting position, of a right-infinite word. In a periodic word it suffices to examine the \(L\) starting positions modulo its period. A Parikh vector over the binary alphabet records the number of zeros and ones; with fixed length it is determined by the zero count. Equalities and intervals are exact for all positive run lengths, including lengths \(n\) much larger than \(L\). No assertion is made about periods of different lengths or alphabets with more than two letters.

## Proof

**Lemma 1 (zero-count interval).** In \(Z=(0^e1^f)^\omega\), with \(e,f\ge1\) and \(e+f=L\), the zero counts attained by length-\(r\) factors for \(0\le r<L\) are exactly all integers in
\[
[\max(0,r-f),\ \min(e,r)].
\]
Indeed, a factor contained as far as possible in the one-run attains the lower bound, and a factor contained as far as possible in the zero-run attains the upper bound (allowing wrapping around the cycle). Sliding its start once around the period changes the zero count at each step by at most one. Since both extrema occur, all intervening integers occur. Adding \(t\) whole periods to a factor adds exactly \(te\) zeros. Hence the zero-count interval for length \(tL+r\) is
\[
I_{e,f}(t,r)=[\,te+\max(0,r-f),\ te+\min(e,r)\,]\cap\mathbb Z.
\]

If \(a=c\), the intervals for \(X\) and \(Y\) coincide and their cardinality is the stated expression.

Suppose \(a>c\), so \(b<d\). For all \(t\ge0\) and \(0\le r<L\), the **lower** endpoint of \(I_{a,b}(t,r)\) is at least the lower endpoint of \(I_{c,d}(t,r)\), while the **upper** endpoint of \(I_{a,b}(t,r)\) is at least the upper endpoint of \(I_{c,d}(t,r)\). The overlap, if nonempty, therefore has lower endpoint \(ta+\max(0,r-b)\) and upper endpoint \(tc+\min(c,r)\). Counting its integer points yields
\[
C(tL+r)=\max\{0,\ 1+\min(c,r)-\max(0,r-b)-t\delta\}.
\]

**Lemma 2 (trapezoidal level sets).** For a nonnegative integer \(h\),
\[
\min(c,r)-\max(0,r-b)\ge h
\]
holds for an integer \(0\le r<L\) if and only if
\[
h\le\min(b,c)\quad\text{and}\quad h\le r\le b+c-h.
\]
For necessity, the left side cannot exceed either \(b\) or \(c\), and is at most \(r\). It is also at most \(b+c-r\): for \(r\le b\) use \(\min(c,r)\le c\le b+c-r\), and for \(r>b\) use \(\min(c,r)+b-r\le c+b-r\). Conversely, if \(h\le\min(b,c)\) and \(h\le r\le b+c-h\), then for \(r\le b\) the left side is \(\min(c,r)\ge h\); for \(r>b\), it equals \(\min(c,r)+b-r\), which is at least \(h\) by the bounds \(h\le b\) when \(r\le c\), and \(r\le b+c-h\) when \(r\ge c\). This proves the equivalence.

Apply Lemma 2 with \(h=t\delta\). A common Parikh vector is possible exactly for \(0\le t\le T\) and \(t\delta\le r\le b+c-t\delta\). Converting from \(r\) to \(n=tL+r\), and using \(L+\delta=a+d\) and \(L-\delta=b+c\), gives the displayed disjoint intervals.

For adjacent intervals, the number of omitted integers is
\[
(t+1)(a+d)-(t+1)(b+c)-1=2(t+1)\delta-1>0.
\]
The last interval ends at \((T+1)(b+c)\), proving the longest-length formula. The \(t\)-th interval contains \(b+c+1-2t\delta\) integers. Summing over \(0\le t\le T\), and subtracting one for the empty length \(n=0\) in the first interval, yields the stated total count. All conclusions follow. \(\square\)

## Verification

The bundled `verify.py` independently constructs cyclic factors and their zero-count sets, without using Lemma 1 to calculate those observed sets. It compares the observed number of shared Parikh vectors with the closed formula, and verifies interval membership, disjointness, and gap behavior. Executed with Python 3, it reports `VERIFY_OK parameter_pairs=2870 length_and_class_checks=123682 internal_gap_checks=13540` for every pair of binary two-run profiles with common period \(2\le L\le21\), and lengths extending beyond the predicted last match. These finite tests check implementations and boundaries; the proof above establishes the unbounded parameter claim.

For example, \(X=(001)^\omega\) and \(Y=(011)^\omega\) have admissible common-Abelian-factor lengths exactly \(1,2,4\). Length \(3\) fails because the two words have different zero counts in one entire period, yet length \(4\) works through nonaligned phase choices. This nonmonotonicity is visible directly in the interval theorem.

## Relationship to prior work

Longest common Abelian factors of two finite strings were studied algorithmically by Grabowski (2015), Alatabbi–Iliopoulos–Langiu–Rahman (2016), and Sugimoto–Noda–Inenaga–Bannai–Takeda (arXiv first version 2017; later revised). The last paper's Section 5 gives arithmetic criteria and an \(O(m^2n)\) algorithm for finite RLE inputs. Its main theorem does not state the complete all-length spectrum for two infinite equal-period run cycles or the disjoint-island formulas. The survey of Fici and Puzynina (2022 preprint) develops the language of Parikh vectors and Abelian complexity, including periodicity, but explicitly excludes detailed Abelian stringology algorithms. The present classification is a closed symbolic specialization to an infinite family, not a claim to have invented longest-common-Abelian-factor algorithms, Parikh intervals, or the basic definition of Abelian matching.

## Limitations

This is a theorem only for two positive binary run profiles with the same total period. When \(a=c\), the factor languages coincide; the finite-island conclusion requires unequal profiles. A finite matching example alone cannot establish a general exact bound; that claim is proved by the interval lemmas. The comparison with prior work is best-knowledge rather than a proof of absolute novelty: an unindexed equivalent result or an implicit corollary in broader literature may exist.

## References

1. S. Sugimoto, N. Noda, S. Inenaga, H. Bannai, M. Takeda. *Computing Abelian regularities on RLE strings.* arXiv:1701.02836, first submitted 2017-01-11. https://arxiv.org/abs/1701.02836
2. G. Fici, S. Puzynina. *Abelian Combinatorics on Words: a Survey.* arXiv:2207.09937, first submitted 2022-07-20. https://arxiv.org/abs/2207.09937
3. S. Grabowski. *A note on the longest common Abelian factor problem.* arXiv:1503.01093, first submitted 2015-03-03. https://arxiv.org/abs/1503.01093
4. A. Alatabbi, C. S. Iliopoulos, A. Langiu, M. S. Rahman. *Algorithms for Longest Common Abelian Factors.* Int. J. Found. Comput. Sci. 27 (2016), 529–543. https://doi.org/10.1142/S0129054116500143
