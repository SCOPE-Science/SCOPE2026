# Scientific review: Exact online shattering rank of the shift-graph adjacency relation

## Correctness — PASS

The theorem uses the correct deterministic realizable online notion, with query centers and hypothesis centers both from the ordinary increasing-pair shift graph. For each root query the two disjoint arms exhaust the positive center fiber. Selecting from both arms requires \(d<a<b<c\) and \(c<d\), an impossibility, proving the decisive single-positive-or-full-arm lemma. Thus the positive subtree has rank at most two, so rank four is impossible. Sizes of positive fibers settle small-order upper bounds. Explicit depth-two and depth-three decision trees give matching lower bounds and persist in all larger orders. The independent finite checker verified all eight rank values from two to nine, both tree certificates, and the fiber lemma through order twelve; it does not replace the all-order proof.

## Originality — PASS within accessible literature

The most closely related sources are Halevi–Kaplan–Shelah (arXiv:2103.13931) on shift graphs in stable graph theory, Walker (arXiv:2203.12211) on general tree/Littlestone shattering, and Wu's 2025 thesis (Warwick 195162, Proposition 3.4) on static neighborhood VC dimension two. None of the examined relevant portions states the all-order numerical Littlestone sequence or the first depth-three threshold. Targeted scientific searches did not identify an equivalent statement; a negative search cannot prove worldwide priority. Alternative terminology and unindexed results remain a historical-priority risk.

## Mathematical value — PASS

The exact rank of the *adjacency formula* is a motivated invariant for canonical shift graphs, whose chromatic number is unbounded. The sharp finite threshold and complete online rank are not supplied by their static VC dimension. The universal positive-fiber lemma and explicit adaptive witnesses give reusable structural information beyond an isolated computation. The theorem deliberately avoids claiming stability of the complete infinite graph theory.

## Scientific limitations

Only rank-two ordinary shift-graph open-neighborhood concepts are covered. No independent mathematical review or comprehensive historical-priority certification has occurred. The associated finite computation verifies a bounded sample and separate exact witness data but is not an induction proof.

Self-review: passed. Independent audit: not yet performed.
