# Independent mathematical audit

## correctness

PASS

The even-shore code is the image of the even-weight vertex space under the incidence trace. A dependency among queried edges has degree-parity vector either zero or all ones. The zero case gives the cycle obstruction; on a forest the incidence image is exactly the vectors even on each component, so all ones belongs exactly when every component is even. Isolated vertices are included, and the n=2 empty-rank case agrees. A maximal support is a spanning forest, or it is obtained from one by removing a leaf edge when all original components are even. VC dimension is the rank; fixed basis queries attain that depth in a Littlestone tree and the number of concepts bounds depth above. The dual cycle space is the even-shore code, yielding the stated graft identification in its stated regime. The labeled SET formula counts forests by edges after removing all-even forests. Shellability gives a genuine wedge of top-dimensional spheres; reduced Euler characteristic gives (-1)^rank times the signed face sum, and the even-n rank is even. Independent replay: python3 /workspace/review_checks/cuts.py; direct traces and rank for every simple graph on 2–5 vertices and independent block-partition summation for n=4,6,8,10, producing 7, 511, 98099, 36215281. The frozen Python/C++ sources and output were inspected; their finite evidence is not the proof.

## originality

FAIL

The earlier fixed-cardinality cut record does more than give the separately shattered supports for each shore size: its proof already gives the complete feasible shore-size polynomial for each individual assignment on every forest. Applying the even-coefficient filter is a direct specialization of that stronger statement and yields the headline criterion. The residual dimension and topology statements and the exact polynomial arise by standard rank, labeled-SET and shellability deductions with no additional parity obstruction or nonroutine count. This is a finding of demonstrable prior implication, not a claim to have found the Betti sequence verbatim or a failure caused by inaccessible literature.

## value

FAIL

Shattering under a natural parity constraint is a well-motivated question. However, the criterion is already a direct parity filter of the earlier assignment-level enumerator, and the proposed residual count and homotopy use labeled SET, matroid shellability and Euler characteristic without a new enumerative or topological theorem. The explicit four values are useful checks, but do not establish a distinct, nonmechanically implied invariant here. No separate repair is supported by this comparison.

The dated certificate retains the supplied scientific assessment, sources and limitations.
