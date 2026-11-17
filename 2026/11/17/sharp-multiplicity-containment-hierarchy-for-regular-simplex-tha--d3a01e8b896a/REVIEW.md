# Scientific review: sharp multiplicity containment hierarchy

## Correctness — PASS
For each ray the ball membership test reduces exactly to a sorted inner-product threshold. The regular-simplex facet description turns the problem into optimizing a product of the positive \(m\)-th order statistic and the negative minimum. The top-\(m\) mean, regular-simplex Gram matrix, and exact largest eigenvalue of a symmetric rank-two form supply a global bound. Its unique positive eigendirections achieve the sharp constant and yield exactly \((d+1)\binom{d}{m}\) distinct points. Direct finite checks passed 284683 assertions across dimensions 2–11. The proof—not numerical sampling—establishes all dimensions and ranks.

## Originality — PASS (historical priority provisional)
Polyanskii (arXiv:2506.13451, Section 4) and Pirahmad–Polyanskii–Vasilevskii (arXiv:2108.09795) study nonempty intersections of diametral balls induced by graph matchings. Pavlík (arXiv:2611.14277, Theorem 5.1) proves onefold coverage and a subordinate power-diagram tiling, but not the location of every multiple-overlap layer. An existing planar regular-polygon overlap classification contains the \(d=2,m=2\) special case, so that case is not separately claimed. Published-record comparisons found similarly named results on simplex radial distributions and vertex-thickening, but their objects and implications do not supply this hierarchy. Remaining risks: unindexed priority and limited access to full text of two adjacent recorded results.

## Mathematical value — PASS
The question concerns the precise spatial redundancy of a natural family of diameter balls, not merely whether they cover. The whole discrete multiplicity spectrum has exact optimal homothetic factors, a sharp containment threshold, growing exterior leakage in dimension, and complete contact-point counts. This answers a structurally motivated geometric gap left by onefold covering statements.

## Limitations
Regular simplices and central diameter balls only; no classification of arbitrary sources, nonregular simplices, or overlap volumes. No independent mathematical review has been carried out.

Self-review: passed. Independent audit: not yet performed.
