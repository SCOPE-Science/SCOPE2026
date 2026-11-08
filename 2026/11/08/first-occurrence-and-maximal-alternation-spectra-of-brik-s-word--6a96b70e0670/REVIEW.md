# Scientific review

## Correctness

**PASS.** The substitution stages have exactly known lengths, a permanent four-symbol suffix from stage three onward, and no `00`. A new alternating even factor starting in `0` must cross the unique end-site of the previous stage. This yields the sharp recursion from the first occurrence of the shorter pattern. The exceptional six-symbol base is verified by the printed complete sixth iterate; the remaining cases follow by induction, and the orientation and finite-maximum formulas follow from the no-`00` boundary rule. The executable finite checks reproduced the 19 computed construction stages; no gigantic word was assumed to have been exhaustively built.

## Originality

**PASS (best knowledge, with residual priority risk).** Shallit's 2026 first-public version establishes that all binary words without `00` occur, and gives first positions of the constant factors \(1^k\). The new theorem treats every alternating factor, including explicit first positions and the complete stagewise maximum; these do not follow numerically from the constant-run first-position theorem, the golden-mean factor-language statement, or a worst-case first-position bound. The OEIS and its associated earlier sequence-code page were inspected for competing formulas; none of the inspected material states this spectrum. An unindexed equivalent argument cannot be ruled out. The result has no claim to precedence over the underlying word construction.

## Value

**PASS.** A binary word with every legal golden-mean factor has unusually delayed appearances of longer alternating powers. The complete spectrum shows exactly how an alternating factor first arrives at each replication boundary, and the finite-stage maximum jumps at thresholds governed by iterated exponentials. This determines the complete maximal-alternation invariant at every canonical stage, complementing the known constant-run phenomenon, rather than enumerating an arbitrary small slice.

## Closest literature and limitations

Shallit (2026), arXiv:2605.07542v1, Theorems 4 and 7, establishes constant-run first-occurrence positions and the legal factor language but not the listed alternating first-position formulas. OEIS A334820 and Ryde's 2020/2021 code document the underlying replication sequence. The result is restricted to alternating factors and complete finite iterates. All independent mathematical review and exhaustive historical priority verification remain outstanding.

Self-review: passed. Independent audit: not yet performed.
