# Independent mathematical audit

## correctness

PASS

A nonresolving set is contained in a distance bisector, so the threshold is the largest bisector size plus one. At n=7 intersections of size 0,1,2,3 give distances 1,3,2,0. In the distance-three case with endpoints abc and ade and remaining points f,g, the path through def and bcg proves the upper bound, and no common disjoint triple exists. Equal distances then mean equal counts in the exclusive parts. For exclusive size k=3,2,1, the sum of binom(k,j)^2 binom(7−2k,3−2j) is 9,13,15 respectively. The 15-sets depend only on the pair of switched points, recoverable by their multiplicities 5 rather than 7. For n≥8 all nonadjacent distinct pairs have distance two. With q=binom(n−3,3) and c_r=binom(n−6+r,3), the number of distinguishers for overlap r is 2(q−c_r) plus two if r>0 (adjacent endpoints are already counted). This is strictly minimized at r=2, since c2>c1 and c2−c0>1, already at n=8. Its value is 2+2 binom(n−4,2). For overlap two, distinguishers are the two endpoints and the triples avoiding their shared pair K and choosing exactly one switch point in T. Ground-point frequencies on K, the complement of K∪T, and T are 2, 2(n−5), and 1+binom(n−4,2) in strictly increasing order, even at n=8. Thus both K and T are uniquely recoverable and the labelled census follows.

## originality

PASS

The supported distinction is the rank-three minimum-distinguishing-neighbourhood calculation together with the labelled largest-bisector classification and the exact loss of witness uniqueness at n=7. Known Kneser distances, abstract threshold reductions and constructions of small resolving sets are not claimed as new.

## value

PASS

For this natural connected Kneser family the universal landmark threshold is a worst-case guarantee not determined by ordinary metric dimension. The exact count and characterization also identify all obstructions at the sharp bound and explain why they merge tenfold only at the odd graph. This is a full natural rank family with a genuine exceptional order, rather than an isolated table entry.

The dated certificate retains the supplied scientific assessment, sources and limitations.
