# Independent mathematical audit

## correctness

PASS

Each image of the entire direct product is the Cartesian product of the two coordinate images. In the first factor, equality of terminal states means that the counts of b-moves from n−1 have all n different residues; one trajectory therefore makes at least n−1 such moves. Between consecutive such moves it needs at least n−1 rotations, forcing the scattered subsequence R; swapping letters forces its mate. In an embedding of a common subsequence in R, each selected a-run uses a source a-run distinct from those used by the other selected a-runs, and each consecutive pair within a selected b-run skips a distinct source a-run disjoint from those. The swapped inequality gives the bound 2(n−2) on the shared subsequence length, attained by (ab)^(n−2). Shared positions in any two embeddings form a common subsequence, so their union gives the claimed lower bound independently of the reset construction. For n≥5, the first prefix leaves {0,1} and a second image missing 0 and n−2; after a² these are {2,3} and {0,…,n−3}. Each of the next n−5 blocks advances the first pair and reduces the second interval by one; the final blocks then produce {1},{0}. The total length is 3+n(n−3)+2+n(n−5)+(n−1)+2+n=2(n²−3n+3). The three small words act as claimed. Independent multi-target backward preimage BFS in /workspace/review_checks/5.py confirms lengths 2,6,14,26,42,62,86,114 for n=2,…,9 and replays the witnesses through n=32. Finite checks are corroboration, not proof for all n.

## originality

PASS

Credit the product/intersection equivalence, general bounds, and the known single-factor forced subsequence. The supported distinct claim is the exact threshold for the crossed equal-size family, using a two-pattern LCS and a matching actual reset word. The frozen citation's proposition label is imprecise for the inspected v1 PDF: Proposition 7 on p. 5 is the stated general bound, rather than Proposition 3.4. This is bibliographic, not a defect in the mathematical argument.

## value

PASS

Two individually extremal factors share one input but disagree on the roles of both letters. The result determines an exact infinite-family synchronization cost: nearly additive, yet with a sharp saving of 2n−4 over separate resetting. The matched LCS obstruction and image-set witness explain why the saving is attainable, beyond numerical observation or the generic max-to-sum interval. No general product classification or shortest-word multiplicities are claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
