# Scientific review: 105-vertex path in the order-ten necklace graph

## Correctness — PASS
The order-ten graph has 108 necklace classes, with 56 even and 52 odd under Hamming-weight parity. Every graph edge flips parity, so every simple path uses at most 52 odd and 53 even vertices, giving the upper bound 105. The full explicit 105-line certificate is directly verified, including canonical rotations, 104 edges, all vertices distinct, all 52 odd classes, and exactly three omitted even classes. The transparent standalone script independently regenerates the complete graph by examining all binary length-ten strings. The argument is finite and complete, with no inference from sampling, optimization success, or a time-limited search.

## Originality — PASS, with residual historical risk
The sharp upper bound is already Proposition 7.4 of Karhumäki–Puzynina–Rao–Whiteland (2016); its Conjecture 7.5 is that the bound is attained. Their Table 2 exhibits witnesses for even orders 6 and 8, and the paper says only orders up to 8 have been checked. Whiteland's subsequent 2019 thesis likewise records only those small even cases. Degni–Drisko (2007) construct and analyze a different Gray ordering and near-Gray properties, without an explicit proof or certificate for a 105-vertex path in this quotient graph at order ten in the inspected sections. Searches of primary and indexed literature, as well as semantic research-record queries, found no prior statement that implies this exact lower bound at ten. Unindexed sources or implicit consequences of a more general construction are residual risks; lack of a search hit is not taken as proof of absolute novelty.

## Value — PASS
The result settles the first even case beyond the original table of a natural published open conjecture. The fixed order is motivated by that precise documented frontier, not selected post hoc as an arbitrary graph parameter. The certificate is compact, independently checkable, and determines the exact maximum, leaving the infinite even-order question genuinely open.

## Scope and limitations
This result does not assert a Hamiltonian path, as bipartition imbalance rules one out; it does not solve the general conjecture or Conjecture 7.7 about maximal cycle decompositions. The scientific claim is limited to a single finite graph and an explicit witness. Historical priority and independent verification by other researchers remain open.

Self-review: passed. Independent audit: not yet performed.
