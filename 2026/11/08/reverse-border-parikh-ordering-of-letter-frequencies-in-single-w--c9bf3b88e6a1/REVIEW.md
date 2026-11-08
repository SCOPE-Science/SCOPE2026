# Mathematical review

## Correctness — PASS

The claim compares limits of expected symbol proportions in uniformly selected length-\(n\) words avoiding one fixed factor. The proof constructs the exact weighted cluster generating function, identifies a unique simple dominant root using a primitive higher-alphabet de Bruijn presentation, and differentiates its root equation. The full signed difference is a nonzero negative multiple of a weighted border-prefix difference polynomial. Since the root lies strictly below \(1/2\), the last nonzero border contribution dominates all smaller-length contributions, even in the worst case of opposite signs. A separate direct argument handles singleton targets. Every asserted limit, tie, sign and uniformity boundary is covered. Matrix and polynomial computations replayed for all \(703\) tested forbidden words and \(3,129\) tested letter pairs; finite enumeration is a secondary check, not an infinite proof.

## Originality — PASS against inspected evidence; residual priority risk

The June 4, 2026 Bóna–Maga–Richey preprint studies symbol frequency for a **binary** one-pattern shift. A separately available binary balanced-border settlement proves the equal-half case. The new statement is instead a simultaneous full weak ordering for arbitrary \(q\ge3\), including pairs of symbols neither of which need be the most frequent, and it uses a strict \(\rho<1/2\) dominance argument. Known binary conclusions are compatible with, but do not imply, this statement. The September 13, 2024 Chandgotia–Marcus–Richey–Wu preprint was inspected in its full available text for multiletter graphs, entropy/Perron theory and related results: its quantitative comparisons are entropy/hitting-time comparisons between forbidden patterns, not symbol-frequency rankings within one pattern. The classical overlap and marked-cluster papers supply enumeration machinery but not the resulting pairwise sign theorem. Two earlier stopped-first-hit letter-proportion claims concern a distinct probability space and cannot be substituted for an avoidance-conditioned limit. Targeted bibliographic and research-index searches did not expose a prior universal multiletter ranking. The most plausible same-topic 2026 binary preprint was available only as an abstract and tertiary exposition, not complete full text; an implicit equivalent all-alphabet claim remains a genuine risk.

## Value — PASS

A single forbidden word defines a natural family of constrained-word sources. The complete relative order and every tie among its \(q\) stationary alphabet frequencies are structural invariants. The theorem extracts these from border Parikh vectors without matrix eigenvalue computations, and yields an exact necessary-and-sufficient uniform-frequency criterion. It detects asymmetry even for targets with globally balanced symbol counts, such as `011220`. This is a substantive all-parameter structural classification rather than a routine isolated value or an arbitrary finite table.

## Reproducibility and limitations

See `RESULT.md` for the whole proof and `checker.py`/`requirements.txt` for independent transfer-matrix checks. Source priority and complete bibliographic coverage have not been independently certified. The scope is \(q\ge3\), one contiguous pattern and unbiased sampling, with no claim about finite-length convergence speed, binary exceptions, or multi-pattern shifts.

Self-review: passed. Independent audit: not yet performed.
