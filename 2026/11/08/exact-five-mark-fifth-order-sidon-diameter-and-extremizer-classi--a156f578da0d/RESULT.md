# Exact five-mark fifth-order Sidon diameter and extremizer classification

## Finding

Let \(B\) be a strictly increasing five-element set of integers. It is a \(B_5\)-set if any equality between two sums of five (not necessarily distinct) members of \(B\) forces the same multiset of five summands on each side. Let \(L_5(5)\) denote the least possible diameter \(\max B-\min B\) of such a set.

**Theorem.** The exact diameter is
\[
L_5(5)=72.
\]
Among all \(B_5\)-sets normalized by translation so that the least element is \(0\), the only sets of diameter at most \(72\) are
\[
\{0,1,16,66,72\}\quad\text{and}\quad\{0,6,56,71,72\}.
\]
They are reflections of one another. Thus there is one extremizer up to translation and reflection, and none with smaller diameter. Both are primitive because their positive elements have greatest common divisor \(1\).

## Assumptions and scope

All set elements and all sums are integers. A five-term sum permits repetitions and is indexed by a weakly increasing five-tuple of indices. There are precisely \(\binom{9}{5}=126\) such multisets. The \(B_5\) condition is that these \(126\) sums are pairwise distinct. Translating a set does not affect that condition or its diameter, so every candidate can be written uniquely as \(B=\{0,a,b,c,d\}\) with integers \(1\le a<b<c<d\). The result concerns the relation-free rank-zero five-letter invariant \(L_5(5)\), not the universal radius \(H_5(5)=150\) for arbitrary prescribed additive-relation profiles.

## Proof

The following exact exhaustive argument is a finite certificate; the standalone checkers are included so that every loop bound, summation and comparison can be independently inspected and reproduced.

For any increasing \(r\)-tuple \(u=(u_0,\ldots,u_{r-1})\), let \(\mathcal T_{r,5}\) be the set of weakly increasing tuples \(0\le i_1\le\cdots\le i_5<r\). Define
\[
\mathcal S_5(u)=\left\{\sum_{j=1}^{5}u_{i_j}:(i_1,\ldots,i_5)\in\mathcal T_{r,5}\right\}.
\]
The tuple \(u\) is \(B_5\) precisely if \(|\mathcal S_5(u)|=|\mathcal T_{r,5}|=\binom{r+4}{5}\). If a tuple is \(B_5\), every subtuple is \(B_5\), since a collision in the smaller tuple would be a collision in the original tuple. Hence the four-mark test for \((0,a,b,c)\) is a logically necessary preliminary filter.

Exhaust exactly the ranges
\[
4\le d\le72,\quad 1\le a\le d-3,\quad a+1\le b\le d-2,\quad b+1\le c\le d-1.
\]
For each \((a,b,c,d)\), enumerate all \(\binom{8}{5}=56\) weakly increasing five-tuples on \((0,a,b,c)\). Reject a candidate if two sums agree. For each survivor, enumerate all \(126\) weakly increasing five-tuples on \((0,a,b,c,d)\). Record the candidate if and only if no two sums agree. Each possible normalized five-element set with diameter \(d\le72\) occurs exactly once in this traversal. Its decision is exact, because the sums are computed using integers and every allowed index multiset is visited exactly once.

The transparent Python implementation `verify.py` reports \(1{,}028{,}790\) candidate quadruples, of which \(342{,}414\) pass the necessary four-mark test. Exactly two candidates pass the full five-mark test: \((0,1,16,66,72)\) and \((0,6,56,71,72)\). In particular, it finds no solution with \(d<72\). The first candidate's \(126\) computed sums are distinct, which also establishes existence without relying on a previous classification.

For a distinct independent check, `verify_fast.cpp` regenerates the multisets using recursive nondecreasing index enumeration and a stamped integer collision array, rather than Python's combination iterator and hash set. It reduces the search by the valid reflection symmetry \((0,a,b,c,d)\mapsto(0,d-c,d-b,d-a,d)\), for which the reverse-gap representative has \(a\le d-c\). The independent search finds one canonical minimum at \(d=72\), with \(528{,}990\) four-mark tests and \(139{,}508\) survivors. The code additionally reproduces the known exact minima \(L_5(2)=11\), \(L_5(3)=23\), and \(L_5(4)=41\). The unrestricted finite theorem follows from the exhaustiveness and exactness of these enumerations, not from extrapolation.

## Verification

The complete scripts `verify.py` and `verify_fast.cpp` use only Python's standard library and a C++17 standard-library compiler, respectively. From the directory containing these files, run:

```bash
python3 verify.py
c++ -std=c++17 -O2 -o verify_fast verify_fast.cpp
./verify_fast
```

The Python output ends with `EXACT_5SUM_DISTINCT=126`, `QUADRUPLES_EXHAUSTED=1028790`, `FOUR_MARK_PRUNING_SURVIVORS=342414`, `OPTIMAL_SETS=0,1,16,66,72;0,6,56,71,72`, `VERIFY_OK`. The C++ output reports minima \(11,23,41,72\) for orders \(2,3,4,5\) and ends in `VERIFY_OK`. All arithmetic is exact. Both implementations explicitly assert the output; a normal return means the enumerated certificate agrees with the theorem.

## Relationship to prior work

Enkai Zhang, *Sharp order-preserving integer models for short additive equalities*, arXiv:2609.08915v1, Section 12.2, explicitly asks for exact \(L_5(q)\), providing \(L_5(2)=11\), \(L_5(3)=23\), and \(L_5(4)=41\), but not \(L_5(5)\). The paper's Theorem B instead determines the **universal** five-letter modeling radius \(H_5(q)=q^2(q+1)\); that stronger-in-one-direction universal statement does not determine the smaller rank-zero minimum. The present result supplies the first remaining exact instance and classifies its minimizers.

Kevin O'Bryant's *Constructing Thick \(B_h\)-sets*, arXiv:2308.12406v2, treats general constructions and bounds for small-cardinality \(B_h\)-sets; *Bounds for Greedy \(B_h\)-sets*, arXiv:2312.10910v3, studies the greedy construction, not the exact minimum five-mark span at order five. Matching only the terms “Sidon” or “diameter” would be insufficient: the specific set cardinality, order, normalization, and optimality assertion were compared. A historical equivalent in less accessible tables has not been excluded by an exhaustive archival survey.

## Limitations

The proof is a transparent exhaustive finite proof for the fixed natural parameter pair \((5,5)\). It is not a closed-form classification for arbitrary \(q\), does not resolve all instances of Zhang's Question 12.2, and does not improve the universal radius \(H_5(5)\). The exact finite verification is reproducible but independent peer review and exhaustive historical-priority assessment have not been performed. The record makes no claim to either.

## References

1. E. Zhang, *Sharp order-preserving integer models for short additive equalities*, arXiv:2609.08915v1 (2026), especially Sections 2.1, 6.4, and 12.2. https://arxiv.org/abs/2609.08915
2. K. O'Bryant, *Constructing Thick \(B_h\)-sets*, arXiv:2308.12406v2 (2024). https://arxiv.org/abs/2308.12406
3. K. O'Bryant, *Bounds for Greedy \(B_h\)-sets*, arXiv:2312.10910v3 (2024). https://arxiv.org/abs/2312.10910
