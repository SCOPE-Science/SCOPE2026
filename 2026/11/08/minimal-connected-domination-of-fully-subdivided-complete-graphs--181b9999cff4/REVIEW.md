# Review of minimal connected domination in fully subdivided complete graphs

## Correctness
PASS. The written proof establishes that a connected dominating set must select at least all but one original vertex. It excludes minimal sets selecting all originals by a cycle-edge or old-leaf deletion, and shows that omitting exactly one original forces a spanning tree of subdivision vertices plus one pendant subdivision vertex. Conversely, connectivity, domination, and inclusion-minimality of every constructed set are proved by an arbitrary-proper-subset argument. Cayley's labelled-tree count yields the exact enumerator. The independent finite checker agrees on every nonempty candidate subset for orders three through six and checks every constructed order-seven set. Experimental checks alone are not treated as unrestricted proof.

## Originality
PASS on a provisional literature assessment. The central-graph alias \(C(K_n)=S(K_n)\) was explicitly checked. Fujita, Kazemnejad and Pahlavsay (2022, arXiv:2204.10292) address the ordinary domination number of central graphs, not minimal *connected* domination. Abu-Khzam et al. (2022, arXiv:2205.00086 and ESA 2022) give general enumeration algorithms, including 2-degenerate graphs, not this exact family classification. A preprint on ordinary domination of central graphs and literature on connected dominating set enumeration were compared as nearby work. No matching exact classification was found in the inspected materials, but an unindexed or differently named equivalent remains a possible priority risk. Cayley's spanning-tree theorem and the definition of connected domination are established background.

## Mathematical value
PASS. Complete classification of every minimal connected dominating set for the central graphs of complete graphs gives an explicit solution family rather than an isolated extremal number. Its bijection with a labelled spanning tree plus an oriented missing endpoint explains why the count grows as \(n(n-1)^{n-2}\), shows every minimal solution has the same size \(2n-2\), and permits direct generation from Prüfer codes. This sharp all-solutions description is not furnished by a general-purpose enumeration algorithm or the known ordinary domination number. Its scope is an infinite, intrinsically defined graph family, not a randomly selected numerical slice.

## Limitations and closest literature
The claim is restricted to full single subdivisions of complete graphs. It makes no claim of a stronger result for general central graphs, arbitrary subdivisions, or all 2-degenerate graphs. The enumerator depends on classical Cayley counting. The checked sources do not establish absolute publication priority, and the order-seven check verifies constructed examples only. Independent mathematical auditing is outstanding.

Self-review: passed. Independent audit: not yet performed.
