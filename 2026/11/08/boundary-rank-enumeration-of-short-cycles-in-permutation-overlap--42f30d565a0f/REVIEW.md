# Scientific assessment of boundary-rank short-walk enumeration

## Correctness — PASS

The decisive lemma is the unique order-preserving map between the values in the length-\(n-k\) prefix and suffix. Once an ordered first-\(k\) tuple and the set of final \(k\) values are fixed, the map forces every term of every residue-class chain, and a simple rejection test establishes sufficiency. The map is defined between rank complements of **equal cardinality**, and each surviving chain is verified to terminate exactly when the map becomes undefined; distinctness ensures that all ranks are used exactly once. The labeled insertion-rank enumeration counts parallel edges separately and gives an exact finite algorithm. The complexity claim is polynomial only for fixed \(k\), not an unqualified polynomial bound uniform in \(k\).

The verification comprises a 19-row C++ exact census, direct construction of the entire directed multigraph for six orders, and 19 identity checks reconciling three-cycles with rooted closed three-walks. Full graph and boundary-reconstruction methods agree at all common orders. The categorical distinction between candidate vertices, rooted labeled walks and cycles is maintained in every file.

## Originality — PASS, with historical-priority risk

Asplund–Fox's arXiv:1609.02210 (2016), full text and specifically Sections 3–6, treats this exact graph. Its results include the standardization necessary/sufficient condition, a two-cycle census and estimates for vertices in some longer closed walks. It explicitly asks for \(k\)-cycle counts when \(3\le k<n\). Its Theorem 18 is in the nonoverlapping-window range \(n\le2k\), whereas the algorithmic contribution works in the complementary \(n\ge2k\) range and counts **edge-distinguished rooted walks** rather than merely eligible vertices. Its Theorem 19 presents bounds and highlights unresolved complications, not the ordered-prefix/unordered-suffix reconstruction method or the supplied all-orders-through-24 cycle census.

Ehrenborg–Kitaev–Steingrímsson (arXiv:1310.1520, full-text introduction and Section 5) count cycles in the smaller 312-avoiding subgraph, not the full graph. Borga–Penaguiao (DOI 10.5802/alco.135) study the cycle polytope for limiting pattern frequencies; available article information and its abstract do not give this exact walk-count algorithm or these cycle coefficients. Searches with the exact graph name, three-cycle aliases, order-pattern shifts, and edge-labeled variants did not uncover a dominating theorem. Search incompleteness, unavailable publisher details, and potentially unindexed computational reports remain risks; independent assessment of historical priority has not been performed.

## Value — PASS

The starting paper poses exact counting of short cycles as an open-ended challenge and states that exhaustive permutation enumeration is difficult. The new boundary-rank lemma replaces \(n!\) candidate vertices by \(O_k(n^{2k})\) descriptions and gives a uniform, reproducible fixed-\(k\) polynomial algorithm for the entire unrestricted permutation-overlap multigraph. The finite three-cycle census provides exact counts over 19 consecutive natural graph orders, with 312-avoiding counts and small-order examples separated as earlier results. This answers a substantive algorithmic part of the stated counting problem without claiming an unproved all-order three-cycle formula.

## Sources and limitations

The principal original source is Asplund and Fox, *Enumerating cycles in the graph of overlapping permutations*, arXiv:1609.02210v1 (2016-09-07). The earliest day-verified open-source problem statement is Ehrenborg, Kitaev and Steingrímsson, arXiv:1310.1520v1 (2013-10-05). The later cycle-polytope comparison is Borga and Penaguiao (2020), DOI 10.5802/alco.135.

The exact finite table stops at \(n=24\), and the implementation specializes to \(k=3\). The general fixed-\(k\) algorithm has an exponent depending on \(k\). Published literature could contain an unnoticed equivalent algorithm; literature searches cannot prove novelty, and no independent validation has been performed.

Self-review: passed. Independent audit: not yet performed.
