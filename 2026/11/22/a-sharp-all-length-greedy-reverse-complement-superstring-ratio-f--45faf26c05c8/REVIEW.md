# Scientific review

## Correctness — PASS

For three distinct reverse-complement length-\(k\) classes, a shortest superstring of length \(k+d\) has \(d\ge2\). When \(d\ge3\), its witness placements supply a first overlap of at least \(k-\lfloor d/2\rfloor\), giving the required ratio. For the critical \(d=2\) case, a complete eight-case symbolic analysis of three consecutive windows proves that any legal first greedy merge leaves a positive oriented overlap with the third. The explicit family has optimum \(k+2\) and a legal greedy output \(2k\). The independent finite checker agrees for all class triples through \(k=7\) and every critical window through \(k=12\); it is only corroboration, not the infinite proof. Risk: alternative greedy conventions may differ when substrings occur; this proof is for the stated maximum-overlap, orientation-aware model.

## Originality — PASS on inspected evidence

The accessible primary texts of Yamano–Shibuya (2026) and Fici–Kociumaka–Radoszewski–Rytter–Waleń (2015) discuss orientation-aware algorithms and a broader compression guarantee. Neither inspected result states or directly entails the sharp three-read all-length binary ratio, its critical three-window lemma, or the explicit all-length witness. Previously recorded binary four-mer finite computations give the \(k=4\) instance but do not imply the theorem for arbitrary \(k\). An additional 2026 related manuscript was inspected at abstract level only; implicit prior derivation or an unindexed equivalent remains a residual risk, so external priority review is warranted.

## Value — PASS

The example proves that the worst-case ratio of ordinary maximum-overlap reverse-complement greedy merging approaches two even when only three classes are present, while the matching upper bound identifies a sharp length-\(k+2\) obstruction across every \(k\ge3\). This supplies an exact parametric performance guarantee rather than a numerical finite census or a routine substitution. The result is relevant to fixed-read superstring heuristics and orientation-aware sequence assembly; it does not claim a practical benchmark advantage or a broader approximation algorithm.

Self-review: passed. Independent audit: not yet performed.
