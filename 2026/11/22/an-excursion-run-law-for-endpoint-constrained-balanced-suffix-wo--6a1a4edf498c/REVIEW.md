# Scientific review

## Correctness — PASS
The normal-play move reduction is exact: in the reversed walk an eligible suffix corresponds to a prefix consisting of complete excursions, whose first excursion is positive and last is negative. The mex induction over negative-excursion runs proves every attainable option value and excludes higher ones. An unambiguous run grammar proves the full formal generating function. Its even/odd identity and sharp maximum follow from even-length primitives and the four-letter cost of each negative run. The factorial-moment proof for zero returns together with the conditional independent excursion signs proves the mixed half-normal limit. Independent standalone exhaustive-mex and renewal-series checks agree. Their finite extent is acknowledged.

## Originality — PASS against inspected sources, with priority risk
The closest full primary text, Inoue–Inazu, *Word Subtraction Games*, arXiv:2611.09157 (2026), supplies the game framework but no result equating the nimber with an endpoint-constrained excursion-run statistic or yielding the stated two-variable series and limit law. Published results on full zero-sum suffix games and Dyck-suffix games impose different move languages, and their Grundy laws do not imply this endpoint-constrained result. Searches for balanced-endpoint suffix subtraction games, primitive-excursion runs and return-weighted Grundy distributions revealed no equivalent indexed theorem. Hetyei's older truncation-game paper was not fully accessible, so its possible unindexed special cases remain a residual risk. Novelty is not inferred from failed search alone.

## Value — PASS
The game is a natural boundary-sensitive refinement of binary balanced-word subtraction: forbidding zero-sum suffixes with the wrong endpoints changes the mex from return counts to a nonlinear run statistic. The result gives a complete exact outcome distribution, a four-symbol sharp bound and, strikingly, an atom of mass one half combined with diffusive half-normal positive values. These distinctions are not mere restatements of standard random-walk return enumeration and supply a tractable model of nonregular word subtraction.

## Scientific limitations and closest literature
The theorem assumes precisely the binary alphabet, full contiguous suffix deletion, equality of two letter counts and both endpoints \(a\); it does not cover broader endpoint or alphabet classes. Bibliographic priority could be affected by an unindexed equivalent or the inaccessible full text of arXiv:0912.0573. Numerical verification is finite, not an infinite certificate.

Self-review: passed. Independent audit: not yet performed.
