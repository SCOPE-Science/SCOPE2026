# Independent audit — 2026-09-22 campaign

**Record:** `SCOPE-20260908-049` / `2026/09/08/049`  
**Reviewed UTC date:** 2026-09-24  
**Audited public commit:** `f1bee63e7115a5c2a8df4210f09faab70a83c26b`  
**Source tree:** `e3505f8a4a17ea58e359c0551348bf024a74a304`  
**RESULT.md blob:** `786c40ab5639b25a9bf4f9701d012c17375e2287`

## Claim audited

The record claims a complete graded-Betti census for edge ideals of all 112 connected unlabeled graphs on six vertices, distributions of projective dimension and regularity, matching-bound statistics, 55 distinct Betti tables, and an explicit extremal witness.

## Correctness — PASS

I rebuilt the census independently using NetworkX's graph atlas only as the source of the 112 connected unlabeled six-vertex graphs, then used independent mathematical code for every invariant.

For each graph and each vertex subset `W`, I constructed the independence complex of the induced graph and computed reduced simplicial homology over the rationals by exact row reduction. Hochster's formula then produced the Betti table. This reproduced all headline distributions:
- 112 connected unlabeled graphs;
- regularity: 67 with reg 1 and 45 with reg 2;
- projective dimension: 4 with pd 3, 64 with pd 4, 44 with pd 5;
- exactly 55 distinct full Betti tables;
- the reported most-frequent table occurs 8 times.

I separately brute-forced all matchings and all induced matchings. The inequalities `im(G) <= reg(S/I(G)) <= mmm(G)` hold for all 112 graphs; equality with induced matching occurs 107 times, equality with maximal-matching minimum occurs 54 times, and all three quantities equal 2 for 40 graphs.

The canonical witness with edges `{02,04,05,12,13}` independently reproduces its stated Betti table, `pd=4`, `reg=2`, and both matching parameters equal to 2.

## Originality — PASS, narrowly qualified

Queries included `"112 connected graphs Betti tables edge ideals 6 vertices"`, `"connected graphs on 6 vertices edge ideal Betti census"`, and searches for the exact distribution counts and witness table. The inspected literature contains extensive general theory of Betti numbers, regularity, projective dimension, and edge ideals, and the number 112 of connected unlabeled six-vertex graphs is classical, but I did not locate this exact compiled 112-graph Betti census.

The originality finding is therefore only for the compiled finite table/distribution, not for Hochster's formula, graph enumeration, the matching bounds, or the individual invariants.

## Scientific value — FAIL

All substantive outputs are obtained by applying standard finite graph enumeration and standard Hochster-homology computation to the smallest nontrivial atlas-sized class. The record proves no new structural theorem, discovers no new obstruction or bound, and does not reach a regime where the census changes current understanding. The matching inequalities it verifies are pre-existing facts; counting how often equality happens on 112 tiny graphs is useful as a software regression dataset but not a scientifically significant result on its own.

## Final disposition

**FAILED.** The census is correct and appears narrowly original as a compilation, but the scientific-value axis fails. This is a scientific judgment, not an operational failure.
