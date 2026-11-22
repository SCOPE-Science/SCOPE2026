# The first integer-rounding gap for single-deletion codes on noncrossing set partitions

## Finding

Let \(\mathrm{NC}_n\) be the noncrossing partitions of the linearly ordered ground set \([n]\). A one-element deletion removes an unknown ground-set element and then relabels the survivors in increasing order. Let \(\Delta(\pi)\subseteq\mathrm{NC}_{n-1}\) be the set of distinct outputs of this operation. Write \(M_n\) for the largest number of input partitions whose deletion shadows are pairwise disjoint. Write \(P_n\) for the fractional shadow-packing optimum, with one nonnegative weight for each input and capacity one for each possible output.

**Theorem (complete finite profile and first rounding failure).** For \(1\le n\le6\), the exact profiles are

| \(n\) | \(|\mathrm{NC}_n|\) | \(M_n\) | \(P_n\) |
| --- | ---: | ---: | ---: |
| 1 | 1 | 1 | \(1\) |
| 2 | 2 | 1 | \(1\) |
| 3 | 5 | 2 | \(2\) |
| 4 | 14 | 3 | \(3\) |
| 5 | 42 | 5 | \(95/16\) |
| 6 | 132 | 12 | \(32021/2390\) |

Consequently \(n=5\) is the first strict fractional integrality gap, whereas \(n=6\) is the first failure of the commonly used rounded fractional bound:
\[
M_6=12<\left\lfloor P_6\right\rfloor=13,
\qquad M_n=\left\lfloor P_n\right\rfloor\quad(1\le n\le5).
\]

## Assumptions and scope

A set partition is canonically represented by its restricted-growth word \(w=(w_1,\ldots,w_n)\), with \(w_1=0\) and each subsequent letter at most one greater than the preceding maximum. Two positions receive the same letter precisely when they belong to the same block. A partition is noncrossing precisely when there exist no \(a<b<c<d\) such that \(w_a=w_c\ne w_b=w_d\). Thus \(|\mathrm{NC}_n|=\frac{1}{n+1}\binom{2n}{n}\).

For a word \(w\), delete the letter at position \(i\), and replace the remaining block labels, in order of first occurrence, by \(0,1,\ldots\). The set \(\Delta(w)\) contains each distinct result once, even when different deletion positions coincide. Deletion preserves noncrossing. The channel is a *single unknown deletion*, not a complete-deck observation or deletion with the position known.

The fractional LP uses variables \(x_w\ge0\) for \(w\in\mathrm{NC}_n\) and constraints
\[
\sum_{w:\,z\in\Delta(w)}x_w\le1\quad(z\in\mathrm{NC}_{n-1}),
\qquad P_n=\max\sum_wx_w.
\]
The dual uses \(y_z\ge0\), with \(\sum_{z\in\Delta(w)}y_z\ge1\) for every input and objective \(\min\sum_zy_z\). At \(n=1\), the unique output is the empty partition.

## Proof

**1. Exhaustive and unique source representation.** Start with the word \(0\). Whenever the current largest letter is \(m\), append any letter from \(0\) through \(m+1\). Induction on the word length proves this produces each restricted-growth word exactly once. Reject a word if its labels contain the alternating quadruple specified above. Every partition has exactly one restricted-growth word; the alternating-quadruple condition is exactly the definition of crossing blocks. Hence the retained list is *precisely* \(\mathrm{NC}_n\), not a sampled subset. The checker enumerates, sorts and verifies all \(1,2,5,14,42,132\) inputs at the stated lengths.

**2. Deletion incidence and integer upper bounds.** For each retained word, perform every positional deletion and canonicalize its remaining labels. Build the undirected compatibility graph whose vertices are inputs and whose edges join two inputs exactly when their deletion shadows are disjoint. Any deletion-correcting code is exactly a clique, and conversely. The supplied `verify.py` constructs this graph from the definitions, then performs a complete maximum-clique branch-and-bound search.

At every recursive node, greedily properly color the induced candidate graph by repeatedly forming independent color classes. Each clique contains at most one vertex of each color. The algorithm branches on candidates in reverse color order, intersecting the candidate set with each chosen vertex's neighbors and removing that vertex after its branch. A branch is discarded only when the number already chosen plus its valid coloring upper bound is at most the best clique already found. Induction over the remaining candidate set proves that no clique larger than the resulting incumbent is omitted. The returned maximum values for \(n=1,2,3,4,5,6\) are exactly \(1,1,2,3,5,12\), with respectively \(2,2,3,4,35,34913\) visited recursive nodes. The source code, not the node counts, specifies the exhaustive proof.

For an explicit size-\(12\) witness at \(n=6\), the following canonical words have pairwise disjoint deletion-output sets:

```
012345  012321  012330  011211
011020  012000  011123  001203
001122  001110  000011  000000
```

Their shadows contain \(38\) distinct outputs. At \(n=5\), the five-word witness is `01234`, `01222`, `01100`, `00120`, `00001`.

**3. Exact fractional optima.** `certificate.json` gives, for each \(n\), integer vectors \(p\) indexed by the lexicographically sorted sources and \(q\) indexed by the sorted deletion outputs, together with positive integer denominators \(d_p,d_q\). The exact checker tests
\[
 p_w\ge0,\quad\sum_{w:z\in\Delta(w)}p_w\le d_p\quad\forall z,
\qquad q_z\ge0,\quad\sum_{z\in\Delta(w)}q_z\ge d_q\quad\forall w,
\]
and confirms the integer identity
\[
 (\sum_wp_w)d_q=(\sum_zq_z)d_p.
\]
Thus \(p/d_p\) and \(q/d_q\) are respectively primal-feasible and dual-feasible with exactly equal rational objectives. Weak LP duality yields the exact fractional optimum, without relying on floating-point solvers. The certificates give \(P_5=95/16\) with denominators \(16\) and \(16\), and \(P_6=32021/2390\) with denominators \(2390\) and \(14340\). The same argument certifies all smaller cases.

The table and first-rounding-failure statement follow directly. \(\square\)

## Verification

Both `verify.py` and `certificate.json` are standalone files supplied with this result. With Python 3 and only its standard library, place them in the same directory and execute `python3 verify.py`. The script recomputes all canonical source words, tests each noncrossing criterion, constructs every distinct deletion shadow, checks each displayed code, recomputes the exact maximum-clique bound, and verifies all primal and dual rational inequalities. Its final line is `VERIFY_OK`. The length-six search makes \(34913\) recursive calls. All assertions are exact integer operations. For transparency, the reproducibility bundle certifies **only** source lengths \(1\) through \(6\); it does not extrapolate a general formula.

## Relationship to prior work

Jelínek and Mansour's *On Pattern-Avoiding Partitions* (first posted 2007-03-29) describes canonical set-partition words, the \(1212\) crossing pattern and Catalan enumeration, but does not compute deletion-code capacities or fractional shadow-packing values. Kulkarni and Kiyavash's *Non-asymptotic Upper Bounds for Deletion Correcting Codes* (first posted 2012-11-13) supplies the general deletion-hypergraph and fractional-cover approach, including constrained string sources, without analyzing the recanonicalized noncrossing-partition channel here. Gabrys and collaborators study rank-standardized deletion on permutations, not the same block-incidence channel.

Related studies of noncrossing-partition pair-equality query shattering concern which Boolean query sets are realizable, not packing input partitions with disjoint one-point deletion shadows. Results for all set partitions or pattern-avoiding permutations do not imply this theorem: the former has additional source words and the latter has a different observation map despite Catalan equinumerosity. The precise new claim is the six-length capacity/fractional profile and its sharp first integer-rounding failure; no claim is made that the LP method itself or the Catalan enumeration is new.

## Limitations

This is a finite exact classification for \(1\le n\le6\), not a formula for larger values, multiple deletions, or arbitrary set partitions. A machine-checkable exhaustive search is used for the integer upper bounds; the checker and the displayed pruning invariant are both necessary to reproduce the argument. Although relevant indexed papers and closely related results were compared by their mathematical implications, earlier equivalent work outside the inspected sources cannot be excluded. The scientific assessment has not received independent external validation.

## References

1. V. Jelínek and T. Mansour, *On Pattern-Avoiding Partitions*, arXiv:math/0703898v1, first public 2007-03-29, https://arxiv.org/abs/math/0703898. See canonical words, crossing-pattern avoidance and finite pattern classifications.
2. A. A. Kulkarni and N. Kiyavash, *Non-asymptotic Upper Bounds for Deletion Correcting Codes*, arXiv:1211.3128v1, first public 2012-11-13, https://arxiv.org/abs/1211.3128. See the deletion-incidence hypergraph, LP duality and constrained sources.
3. R. Gabrys, E. Yaakobi, F. Farnoud, F. Sala, J. Bruck and L. Dolecek, *Single-Deletion-Correcting Codes over Permutations*, ISIT 2014, https://yaakobi.net.technion.ac.il/files/2015/04/40_Single_Deletion_Permutations_ISIT14.pdf.
4. Z. Lin and D. Kim, *A combinatorial bijection on \(k\)-noncrossing partitions*, arXiv:1905.10526, https://arxiv.org/abs/1905.10526 (background on noncrossing partitions and enumerative equivalences).
