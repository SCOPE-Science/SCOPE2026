# Scientific review of the five-prism swapping metric

**Correctness: PASS.** The configuration space is exactly the permutation set on ten labels, with each allowed transition an edge transposition on \(C_5\square K_2\). Standard FIFO breadth-first search determines true shortest-path distance. The factoradic and bit-packed exhaustive implementations both visited all \(10!\) placements, produced the same eighteen-shell vector, the same four natural antipodes, and the same transport-gap maximum and multiplicity. The seventeen-swap explicit witness was checked as a legal path. Vertex transitivity extends the census to every starting placement. No statements about larger networks are inferred from the finite data.

**Originality: PASS, with historical-priority risk.** Queries considered five-prism, circular ladder, \(GP(5,1)\), sorting with edge transpositions, diameter seventeen, and four antipodes. The closest inspected work addresses general token swapping or different graphs: Petersen \(GP(5,2)\), the tree-generating case, and circular sorting modulo a rotation. The Petersen exact metric concerns a different generator set and does not imply the present numbers; complexity and general-search results do not state the prism census. An unindexed or differently named earlier exact computation remains possible. Indexed absence alone is not treated as proof of priority.

**Value: PASS.** The pentagonal prism is a standard, nontrivial, three-regular ten-node interconnection network. Determining the complete shortest-swap spectrum and precisely characterizing its four antipodes yields an exact finite stress-test for permutation-routing algorithms; the identified transport-bound deficit quantifies how far a common lower bound falls short. The characterization goes beyond a one-number computation while remaining honest about its fixed-graph scope.

References and limitations are given in `RESULT.md`. Computational reproducibility is not independent external scientific validation.

Self-review: passed. Independent audit: not yet performed.
