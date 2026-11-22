# Complete near-permutation Burrows–Wheeler run distribution at all lengths

## Finding

Let \(n\ge3\) be an integer and let \(A\) be a totally ordered alphabet of \(r=n-1\) letters. A *near-permutation necklace* is a cyclic-rotation class of a length-\(n\) word on \(A\) in which one letter \(a\) occurs twice and every other letter occurs once. The two symbols immediately clockwise after the two copies of \(a\) are its **successor pair**; their order is disregarded. All these necklaces are primitive.

Write \(\operatorname{BWT}(w)\) for the **sentinel-free circular** Burrows–Wheeler last column obtained by lexicographically sorting the \(n\) cyclic rotations of \(w\). Let \(\rho(v)\) denote the number of maximal constant-letter runs in the **linear** word \(v\), not the cyclic run count. Then for every such necklace \([w]\),

\[
\rho(\operatorname{BWT}(w))=n-\mathbf{1}_{\{b,c\}\text{ is an adjacent-rank pair in }A},
\]

where \(\{b,c\}\) is its successor pair (which always has two distinct members). Consequently, counting different necklaces and retaining the given alphabet order,

\[
\#\{[w]:\rho(\operatorname{BWT}(w))=n\}=\frac{(n-3)(n-1)!}{2},\qquad
\#\{[w]:\rho(\operatorname{BWT}(w))=n-1\}=(n-1)!.
\]

There are \((n-1)(n-1)!/2\) near-permutation necklaces in total. Thus the exact probability of no clustering under uniform sampling from this family is \((n-3)/(n-1)\), tending to one as the length and occupied alphabet grow jointly. If an ordered ambient alphabet has size \(q\ge n-1\), each count is multiplied by \(\binom{q}{n-1}\) when all \(n-1\) selected letters must be occupied.

## Assumptions and scope

Words are taken modulo cyclic rotation only; reflection, symbol renaming, and permutation of alphabet order are **not** identified. The alphabet order determines BWT's row sorting. Exactly one symbol repeats, exactly once in excess of its first occurrence. No terminal sentinel is appended, and runs in the BWT last column are counted linearly. In a primitive necklace all cyclic rotations are distinct, so sorting the BWT matrix has no ties. The restriction \(n\ge3\) is essential for the two successor symbols to be distinct.

## Proof

**1. Primitivity and the repeated symbol's positions in the last column.** Every near-permutation word contains \(n-2\ge1\) symbols of multiplicity one, so it cannot be a proper power. In the cyclic BWT matrix, a row has last-column letter \(a\) precisely when its starting position is immediately after one of the two occurrences of \(a\) in the source circle. Exactly two rows therefore contribute \(a\), and every other last-column symbol occurs exactly once. The last column has \(n-1\) runs precisely when its two \(a\)'s occupy consecutive rows; otherwise it has \(n\).

**2. The successor-order criterion for nonadjacent copies.** If the two copies of \(a\) are not adjacent in the source circle, their successors are distinct symbols \(b,c\ne a\). Each occurs only once in the source, so exactly one sorted row begins with \(b\), and one with \(c\). Those are precisely the two rows whose last-column entry is \(a\). Sorted rows are grouped by first letter in alphabet order. Since both first-letter blocks are singletons, these rows are consecutive exactly when the ranks of \(b,c\) are consecutive.

**3. The successor-order criterion for adjacent copies.** If the circle contains the block \(aa\), its two successors are \(a,c\) with \(c\ne a\). Exactly two rows start with \(a\), with prefixes \(aa\) and \(ac\). The row starting \(ac\) is the one whose last-column letter is \(a\); the other row's predecessor is a different symbol because \(n\ge3\). If \(a<c\), the \(ac\) row is the last row in the \(a\)-starting block, and it is adjacent to the single row starting \(c\) precisely when \(c\) is the immediate next alphabet letter after \(a\). If \(c<a\), it is the first row of that block, and the matching condition is that \(c\) immediately precedes \(a\). Thus the same rank-adjacency condition holds. This exhausts all possible necklace structures.

**4. Uniform distribution of successor pairs.** Fix the repeated letter \(a\) and an unordered two-element subset \(\{b,c\}\subseteq A\). Circular permutations of the \(r-1\) distinct symbols in \(A\setminus\{a\}\) number exactly \((r-2)!\). If \(b,c\ne a\), inserting one copy of \(a\) directly before \(b\) and the other directly before \(c\) gives a bijection onto the near-permutation necklaces with that successor pair. If one member is \(a\), say \(\{a,c\}\), instead insert the block \(aa\) before \(c\). The same bijective count \((r-2)!\) holds. The pair is unique, so no necklaces are counted twice.

There are \(\binom{r}{2}\) successor pairs for each of the \(r\) possible repeated letters, of which precisely \(r-1\) consist of neighboring alphabet ranks. Hence the number with an adjacent last-column \(aa\) is

\[
r(r-1)(r-2)!=r!=(n-1)!.
\]

The total number is \(r\binom{r}{2}(r-2)!=r\,r!/2\), and subtracting gives \((r-2)r!/2=(n-3)(n-1)!/2\) completely unclustered cases. Choosing the occupied \(r\)-element subset of an ambient ordered alphabet multiplies the count by \(\binom{q}{r}\); the induced order preserves all rank-adjacency comparisons. This proves the theorem.

## Verification

Two independent exhaustive constructions corroborate every formula for \(3\le n\le9\): `verify_near_permutation.py` generates source necklaces, lexicographically sorts full cyclic rotations and checks the successor-pair equivalence and uniform fibers; `verify_last_columns.cpp` generates all words of the specified fixed content as possible last columns, uses the independent stable LF mapping to test the one-cycle condition and counts BWT runs. The scripts' outputs, reproduced directly from the packaged sources, appear in `verification_output.txt`.

| \(n\) | BWT has \(n\) runs | BWT has \(n-1\) runs |
|---:|---:|---:|
| 3 | 0 | 2 |
| 4 | 3 | 6 |
| 5 | 24 | 24 |
| 6 | 180 | 120 |
| 7 | 1,440 | 720 |
| 8 | 12,600 | 5,040 |
| 9 | 120,960 | 40,320 |

For example, with \(A=\{0,1,2,3,4\}\), the necklace represented by `002134` has BWT last column `402013`, which has six runs, whereas `001234` has BWT last column `400123`, with five runs. The exhaustive checks validate small cases but are not used to infer the all-length result; the four-step proof establishes that independently.

## Relationship to prior work

Fici and Gabory introduced generalized de Bruijn BWT structures, not the one-repeated-symbol content classification [1]. Fici, Gabory, Romana and Sciortino proved existence of completely unclustered BWT images over nonbinary alphabets for all lengths and a lower bound for certain ternary necklaces [2], and explicitly posed further classification and counting questions. This theorem isolates and completely enumerates the first non-permutation fixed-content family, where one symbol has multiplicity two and all others have multiplicity one. Kumallagov studied the **minimum input cyclic run count** among completely unclustered BWTs and gave an unrestricted fixed-Parikh one-cycle baseline (Proposition 5.5), expressly distinguishing that baseline from a count with the unclustered constraint [3]. That result does not imply the present exact two-point output-run distribution. Specialized fixed-length BWT censuses and general bijective standard-permutation machinery may cover individual low-length instances; the asserted contribution is the all-length structural rule and counting law, not any isolated small count.

## Limitations

The required alphabet support grows as \(n-1\); the limit \((n-3)/(n-1)\to1\) does **not** describe fixed-size alphabets. Only the single-repeat content profile is classified, and no formula for an arbitrary Parikh vector, larger repeated multiplicity or minimum source run count is claimed. The two-run-number alternative is a special feature of this profile, not a statement for general words. The priority comparison is limited to inspected sources; an earlier equivalent characterization in unindexed literature remains possible.

## References

[1] G. Fici and E. Gabory, *Generalized De Bruijn Words, Invertible Necklaces, and the Burrows–Wheeler Transform*, first public arXiv version 2025-02-18. https://arxiv.org/abs/2502.12844

[2] G. Fici, E. Gabory, G. Romana and M. Sciortino, *Unclustered BWTs of any Length over Non-Binary Alphabets*, first public arXiv version 2025-08-28. https://arxiv.org/abs/2508.20879 ; conference full text https://drops.dagstuhl.de/storage/00lipics/lipics-vol369-cpm2026/html/LIPIcs.CPM.2026.13/LIPIcs.CPM.2026.13.html

[3] D. Kumallagov, *An extremal problem for completely unclustered Burrows–Wheeler images*, first public arXiv version 2026-05-31, MSC2020 68R15. https://arxiv.org/abs/2606.01267
