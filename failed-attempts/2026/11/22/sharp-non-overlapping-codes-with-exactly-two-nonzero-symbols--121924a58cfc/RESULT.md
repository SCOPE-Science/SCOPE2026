# Sharp non-overlapping codes with exactly two nonzero symbols

## Finding

Let \(q\ge 2\) and \(n\ge3\) be integers, and distinguish the zero in the alphabet \(\{0,1,\ldots,q-1\}\). A code \(\mathcal C\) comprises length-\(n\) words with exactly two nonzero positions, and is **non-overlapping** if no nonempty proper prefix of any member equals a suffix of equal length of any member, including the same member. Put \(m=q-1\). Its maximum possible size is

\[
M_q(n)=\begin{cases}
\dfrac{n-1}{2}m^2,&n\text{ odd},\\[4pt]
\left(\dfrac n2-1\right)m^2+\left\lfloor\dfrac{m^2}{4}\right\rfloor,&n\text{ even}.
\end{cases}
\]

For odd lengths, this is exactly the full primitive-necklace packing bound. For even lengths, it is below the primitive-necklace packing bound by exactly \(\lfloor(m-1)^2/4\rfloor\). A balanced bipartition of the nonzero alphabet constructs an optimum for every pair \((q,n)\).

## Assumptions and scope

Indices run from \(0\) to \(n-1\). A word has exactly two nonzero **positions**, whose two values can agree or differ; there is no prescribed multiset of the values. For a word \(w\), \(\operatorname{pre}_k(w)\) and \(\operatorname{suf}_k(w)\) denote its prefix and suffix of length \(k\). Every \(1\le k<n\) is forbidden, including self-overlaps; the constraint is stronger than forbidding only the longest overlaps. The alphabet is labeled and zero is distinguished. The formula makes no claim for \(n=2\) or other nonzero weights.

## Proof

**Rotation orbits.** Any two different cyclic rotations of one length-\(n\) word have a nonempty proper prefix–suffix equality, so an admissible code contains at most one word from each cyclic necklace. A word whose cyclic rotation orbit has fewer than \(n\) members has a nontrivial self-overlap and cannot occur in the code.

Each two-marker necklace has cyclic gaps \(t\) and \(n-t\). For each integer \(1\le t<n/2\), the shorter gap has a unique orientation: the first marker bears a value \(a\in\{1,\ldots,m\}\), the marker \(t\) steps later bears \(b\) from the same set, and the long gap returns to the first marker. There are exactly \(m^2\) such necklaces per \(t\); all are primitive because the unequal gap lengths preclude an interchange of the two markers under a nonidentity rotation. Hence the short-gap necklaces contribute at most \(m^2\lfloor(n-1)/2\rfloor\) codewords.

**The even antipodal obstruction.** Suppose \(n=2d\). Two markers separated by \(d\) with equal nonzero values form a periodic word and cannot belong to an admissible code. With distinct values, the corresponding primitive necklaces are indexed by unordered pairs of those values, but one cannot necessarily take one word from each. Every *individually unbordered* word in such a necklace has different first and last symbols. Since the two markers are antipodal, this forces one marker to lie at the first position or one at the last position; otherwise first and last are both zero. Thus the only possible forms are

\[
a0^{d-1}b0^{d-1}\quad\text{(type I)},\qquad
0^{d-1}a0^{d-1}b\quad\text{(type II)},\qquad a\ne b.
\]

No type-I and type-II words can coexist: the last symbol of type I and first symbol of type II are both zero, giving a forbidden length-one overlap. If all chosen antipodal words are type I, their prefixes and suffixes of length \(d\) are \(a0^{d-1}\) and \(b0^{d-1}\). Consequently the set \(A\) of first-marker values and the set \(B\) of second-marker values must be disjoint. There are at most \(|A||B|\le\lfloor m^2/4\rfloor\) such words. Type II yields the same upper bound, using length-\(d\) prefixes \(0^{d-1}a\) and suffixes \(0^{d-1}b\). Adding short-gap and antipodal contributions proves the asserted upper bound for both parities.

**Sharp construction.** For each \(1\le t<n/2\), include *every* word

\[
w(a,b,t)=a0^{t-1}b0^{n-t-1},\qquad a,b\in\{1,\ldots,m\}.
\]

When \(n=2d\), choose a partition \(A\sqcup B=\{1,\ldots,m\}\) with \(|A|=\lfloor m/2\rfloor\) and \(|B|=\lceil m/2\rceil\), and also include all \(w(a,b,d)\) for \(a\in A\), \(b\in B\). These are distinct words, with precisely the claimed count.

To check *all* overlaps, note that every constructed word starts with a nonzero symbol, while its every proper suffix excludes that first nonzero symbol. A prefix of length \(k\) contains both markers if \(k>t\), whereas a proper suffix contains at most one; therefore equality requires \(k\le t\). The suffix contains any nonzero marker only when \(k\ge n-s\), where \(s\) is the second-marker position of the suffix-providing word. Hence a matching prefix and suffix would require \(n-s\le k\le t\). Yet \(s,t\le n/2\), so this is impossible except when \(n\) is even and \(s=t=k=n/2\). In that one case, the first letters in the compared length-half pieces are respectively \(a\in A\) and \(b\in B\), which cannot agree. Thus the code has no overlap, including self-overlaps, and meets the upper bound.

**Necklace deficit.** At even length, the short-gap primitive necklaces number \((d-1)m^2\), and antipodal primitive necklaces number \(\binom m2\) (distinct value pairs). The additional antipodal codewords number only \(\lfloor m^2/4\rfloor\), so the deficit is \(\binom m2-\lfloor m^2/4\rfloor=\lfloor(m-1)^2/4\rfloor\). At odd length, all two-marker necklaces have unequal gaps, are primitive, and are represented by the construction.

## Verification

Two standalone Python 3 standard-library programs accompany this document. `verify/exhaustive.py` enumerates the complete two-nonzero-word layer, removes individually bordered words and finds the exact maximum compatible set by exhaustive clique branch-and-bound for \(17\) small parameter pairs: \(2\le q\le5\), with \(3\le n\le9,7,5,4\) respectively. `verify/construct.py` independently builds the proposed codes and checks every ordered pair of words at every possible overlap length for \(84\) cases \(2\le q\le7\), \(3\le n\le16\). It independently enumerates primitive rotation orbits for \(35\) cases \(2\le q\le6\), \(3\le n\le9\). Captured reproducible standard output is included. Both scripts return `PASS`. These finite checks corroborate, but cannot replace, the all-parameter proof above.

## Relationship to prior work

Zakharov (first publicly posted 2026-02-23) bounds products of word-set densities under overlap exclusion; that is a bipartite asymptotic statement, not an exact extremum within the two-nonzero layer. Blackburn studies general non-overlapping codes, including asymptotic constructions and small unrestricted lengths; Chee–Kiah–Purkayastha–Wang give general cross-bifix-free constructions. Yang–Ding give generalized restricted-overlap code constructions and their generating functions; their exact formulas count a specified code family, not the optimum under the present two-marker condition. A separately indexed exact binary weight-two result prohibits only the two *longest* overlaps and consequently has a different optimum; a different exact fixed-weight result treats three nonzero binary positions rather than two. Neither can imply the present answer by a change of notation, by replacing the alphabet size, or by overlooking the shorter forbidden overlaps.

## Limitations

The alphabet has one distinguished zero and precisely two nonzero *positions*. The proof does not optimize other constant-composition layers, unrestricted codes, or restricted subsets of overlap lengths. It establishes existence and the numerical optimum but does not classify *every* optimal codebook. Searches and full-text comparisons cannot exclude all unindexed earlier equivalent results. Independent external validation has not been performed.

## References

1. D. Zakharov, *An isoperimetric inequality for word overlap*, arXiv:2602.20143v1, first posted 2026-02-23, https://arxiv.org/abs/2602.20143.
2. S. R. Blackburn, *Non-overlapping codes*, arXiv:1303.1026, https://arxiv.org/abs/1303.1026.
3. Y. M. Chee, H. M. Kiah, P. Purkayastha and C. Wang, *Cross-Bifix-Free Codes Within a Constant Factor of Optimality*, arXiv:1209.0236, https://arxiv.org/abs/1209.0236.
4. H. Yang and Y. Ding, *Q-Ary (t1, t2)-Overlap-Free Codes*, IEICE Transactions on Fundamentals E109-A (2026), 757–762, first publicized 2025-09-22, https://doi.org/10.1587/transfun.2025EAL2050.
