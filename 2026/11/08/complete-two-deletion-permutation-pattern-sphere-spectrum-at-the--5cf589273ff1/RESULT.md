# Complete two-deletion permutation-pattern sphere spectrum at the first prolific length

## Finding

For a permutation \(\pi\in S_7\), delete exactly two entries and **standardize** the remaining five values to their relative ranks \(1,\ldots,5\). Write \(\mathcal D_2(\pi)\subseteq S_5\) for the distinct resulting patterns, \(B(\pi)=|\mathcal D_2(\pi)|\), and \(H_7(s)=|\{\pi\in S_7:B(\pi)=s\}|\).

The complete exact distribution is:

| Sphere size \(s\) | Number of source permutations \(H_7(s)\) |
|---:|---:|
| 1 | 2 |
| 2 | 8 |
| 3 | 40 |
| 4 | 52 |
| 5 | 158 |
| 6 | 204 |
| 7 | 388 |
| 8 | 386 |
| 9 | 496 |
| 10 | 674 |
| 11 | 482 |
| 12 | 392 |
| 13 | 724 |
| 14 | 288 |
| 15 | 148 |
| 16 | 232 |
| 17 | 252 |
| 18 | 88 |
| 19 | 24 |
| 20 | 0 |
| 21 | 2 |


Thus the attainable values of \(B(\pi)\) are exactly \(\{1,2,\ldots,19,21\}\): **size 20 does not occur**, even though 19 and the maximal 21 both occur. Exactly two permutations, \(3614725\) and \(5274163\), achieve 21 distinct patterns. Consequently the uniform-source mean is \(\mathbb E[B]=1531/140\).

## Assumptions and scope

The source space is the entire symmetric group \(S_7\), with each symbol \(1,\ldots,7\) appearing once. A channel history is a two-element subset of the seven positions; positions are deleted simultaneously and the surviving sequence is mapped to its unique order-isomorphic permutation in \(S_5\). Distinct histories with identical standardized output are counted once. No receiver retains the original numerical labels of the deleted or surviving symbols.

This is an exact finite classification, not an assertion about other blocklengths, about symbol-invariant deletion, or about optimal code size.

## Proof

For each \(\pi=(\pi_1,\ldots,\pi_7)\in S_7\), enumerate the \(\binom72=21\) choices of two positions to delete. For each retained five-tuple \(v\), define its standardization coordinatewise by

\[
\operatorname{std}(v)_j=1+|\{k:v_k<v_j\}|,\qquad 1\le j\le5.
\]

All values are distinct, so the output lies in \(S_5\); two deletion histories agree at the receiver if and only if their standardized tuples are equal. Therefore the following finite procedure computes exactly \(B(\pi)\): start with an empty set, insert the standardization of all 21 histories, then take the set cardinality.

The accompanying executable `checker.py` implements this specification independently in two ways. Its first implementation enumerates the retained five-position subsets and forms ranks from a sorted list. Its second enumerates deleted position pairs and computes every rank by direct comparisons. The two sets are compared for **each** source permutation, not just their cardinalities. The outer loop visits each of the \(7!=5040\) permutations once by exhaustive lexicographic enumeration. The resulting counts are exactly the table above and sum to 5040, exhausting all cases. The code verifies the table as a complete integer assertion; in particular, \(H_7(20)=0\) and \(H_7(21)=2\). Direct collection of the latter equality cases yields the two stated permutations.

This is a computer-assisted finite proof. Its logical completeness follows from exhaustive coverage of the finite domain and all deletion histories, and does not rely on extrapolating numerical observations to untested lengths.

## Verification

With Python 3 and its standard library, run `python3 checker.py` from a directory containing this file. The command recomputes the full spectrum and fails on any discrepancy between its two independent standardization methods, the stated table, the \(7!\) total, or the two prolific witnesses. It also checks that the sum of the distinct-pattern counts is \(55116\), yielding the stated mean.

## Relationship to prior work

Wu, Bui, Niu, Vu and Wang (arXiv:2609.37578, first posted September 29, 2026) define the permutation-invariant deletion model and study systematic deletion-correcting code constructions; their construction bounds are not a distribution for the standardized deletion sphere of every permutation of length seven. Homberger (arXiv:1211.7117) studies fixed-length permutation patterns and, in the section *Further Questions*, asks about the distribution of distinct \(n-k\) patterns; Theorems 19 and 24 give extremal and near-extremal principles but not this entire length-seven spectrum. Bevan, Homberger and Tenner (arXiv:1608.06931) characterize prolific permutations and the shortest lengths supporting them; their theorem explains why length seven is the **first** length for which all 21 two-deletion histories can be different. The known extremal characterization and examples are acknowledged as prior work; the claim here is the complete frequency table and its one-value gap.

## Limitations

The table is a finite calculation at length seven; it does not provide a closed general formula in source length, a full multivariate generating function, or a code-capacity result. The two prolific permutations and the prolific-length threshold were known. The independent scientific audit and complete historical-priority confirmation have not been performed; an unindexed finite census may exist.

## References

- B. Wu, Q. D. Bui, K. Niu, V. K. Vu and S. Wang, *Order-Optimal Systematic Permutation Codes for Correcting t Deletions*, arXiv:2609.37578, first public version 2026-09-29, https://arxiv.org/abs/2609.37578 .
- D. Bevan, C. Homberger and B. E. Tenner, *Prolific Permutations and Permuted Packings: Downsets Containing Many Large Patterns*, arXiv:1608.06931, https://arxiv.org/abs/1608.06931 .
- C. Homberger, *Counting Fixed-Length Permutation Patterns*, arXiv:1211.7117, https://arxiv.org/abs/1211.7117 .
