# Scientific review

## Correctness — PASS
The proof covers every positive integer \(n\) and the exact nonnegative unit-rectangle move set. The perfect-matching decomposition supplies the global \(2n\) upper bound, a nine-rectangle signed potential gives an exact lower bound, and the common-cell/disjoint-support split, including a three-switch two-layer compression, proves there are no other diameter pairs. The last step counts exactly six unordered pairs. Both independent finite implementations reconstruct the graphs through margin eight and agree; neither program is used as an infinite proof.

## Originality — PASS, with historical qualifications
The standard 2-by-2 Markov basis, elementary connectivity, and the n=6 diameter twelve were explicitly found as prior results and are credited. The published 3-by-3 small-margin census (published-finding corpus 2026-09-08, full RESULT.md inspected) limits its 9331 margins to entries at most six; it cannot imply a formula for every n, nor does it state the six-pair classification. The transportation-polytope literature treats a distinct real-vertex adjacency graph. Neither inspected result implies the exact all-n theorem. Full public-text priority is not certified; other papers or tables may use alternative terminology.

## Value — PASS
This is a sharp all-scale finite-state reconfiguration theorem in the smallest nontrivial transportation fiber family. Unlike mere connectivity or state counting, it gives a uniform exact worst-case number of elementary Markov moves and characterizes *all* extremal pairs. The six-pair rigidity makes the worst cases transparent and distinguishes the lattice-point Markov metric from the underlying real polytope's skeleton. It supplies a precise benchmark for combinatorial move-path algorithms, without implying a mixing-time result.

## Closest literature and limitations
Diaconis–Sturmfels (1998) supply the fundamental Markov moves and connectivity. De Loera et al. (arXiv:0709.2189v1) treat transportation-polytope graphs, not these unit-step lattice fibers. The 2026 public finite census covers balanced margins only through six. The original Stanford technical report is known to be dated June 1993 without a verified precise first-public day; the chosen exact source date is the verified 2007-09-14 initial arXiv posting among the dated source records considered. Residual priority risk concerns unindexed or synonymous all-margin switch-diameter results. Independent external audit has not been performed.

Self-review: passed. Independent audit: not yet performed.
