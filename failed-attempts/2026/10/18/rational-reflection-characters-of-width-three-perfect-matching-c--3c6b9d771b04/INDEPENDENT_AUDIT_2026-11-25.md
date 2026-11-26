# Independent mathematical audit

## correctness

PASS

Reconstructed the exact four complexes using column-profile tiling generation and independent subset and incidence enumeration (replay: python /workspace/check_grid_morse.py 2 4 6 8). Perfect matching counts (3,11,41,153), augmented face and incidence totals, every greedy stage and all four critical-face sets matched. There is also a direct acyclicity proof: no directed path can take two upward arrows consecutively, so any directed cycle must alternate upward matched arrows and downward unmatched arrows. Take the earliest matching stage represented among its arrows. A downward arrow deleting that stage's coordinate would connect two faces still present at that stage, so it would have been paired and oriented upward. Thus the cycle adds this coordinate without being able to delete it, a contradiction. Removing the empty face frees one vertex; the resulting Morse CW complex has just this vertex and the indicated 0,1,1,2 positive-dimensional cells, with no intermediate cells and hence constant attaching maps. Independently constructing invariant faces as unions of orbits of each edge involution reproduced all fixed-face counts and reduced traces. An invariant face consisting of b edge orbits contributes (−1)^(b−1), including −1 at the empty face; this equals its chain degree sign times its orientation sign. By homological concentration the reduced Lefschetz vectors at widths 4,6,8 multiply by (−1)^(n/2−1) to give (1,−1,1,−1), (1,−1,−1,1), (2,0,0,2). The last decomposes as ++ and −−. This checks exactly the finite widths and rational characters, not equivariant homotopy. The packaged support scripts were inspected as source, not executed.

## originality

FAIL

Verified existing coverage of all four homotopy types and all nonzero character vectors. The exact theorem of arXiv:2611.18058 and the all-width character formulas of the distinct Resultary record eda18ed068e3 specialize to the frozen result. Those sources are in later-dated records; this is a coverage assessment, not a conclusion that this computation was derivative or that those sources established historical priority over it. The tempting earlier results on ordinary matching complexes are not coverage. No separate novel claim about the certificate algorithm or equivariant topology is established in the frozen finding.

## value

FAIL

These natural finite tests and rational reflection actions would be useful as unknown base cases, but the precise data and substantially stronger results already exist. The frozen record neither improves the invariant nor presents a motivated new property of the certificate or a new boundary regime. Recomputing covered cases does not meet the scientific-value standard for a distinct final finding.

The dated certificate retains the supplied scientific assessment, sources and limitations.
