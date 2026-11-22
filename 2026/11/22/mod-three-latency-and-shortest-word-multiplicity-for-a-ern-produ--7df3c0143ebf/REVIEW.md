# Self-review

**Correctness — PASS.** The single-machine lower bound and uniqueness follow from reverse-subset interval growth; the complete known one-letter-slack family is cited and its indexing reconstructed. A three-state subset calculation gives the modular eligibility condition, and direct subtraction counts every allowed split, including the edge cases \(n=3,4,5\). An independent exhaustive BFS of the product subset graph reproduced the minimum and multiplicity for \(3\le n\le16\), with explicit witnesses checked through \(n=200\). No finite search is treated as an infinite proof.

**Originality — PASS (best-knowledge, residual source risk).** The closest published 45-pair exact table covers only \(n\le11\), and the general 2026 product paper gives broad bounds. The published one-letter-slack theorem counts resets of \(C_n\) alone, not the intersection with \(C_3\). The new statement gives an all-length modular intersection, a complete list of shortest common words and exact arithmetic multiplicities. A later section of the relevant product paper could not be reopened; no claim of exhaustive priority is made.

**Value — PASS.** The three-state factor is the first nontrivial shared-control case (the two-state factor resets immediately under \(b\)). The exact zero-versus-one latency transition and quadratic equality-class counts supply a structural all-length answer beyond the earlier finite spectrum, and exhibit arithmetic sensitivity not expressed by generic max/sum bounds.

**Closest literature and limits.** Fernau–Rystsov (2026) studies product thresholds; the published 2026 45-pair spectrum covers \(n\le11\); the 2026 one-letter-slack classification gives the single-factor near-minimal word list. The statement does not extend to arbitrary factor sizes or unrelated automata; unindexed exact work remains possible.

Self-review: passed. Independent audit: not yet performed.
