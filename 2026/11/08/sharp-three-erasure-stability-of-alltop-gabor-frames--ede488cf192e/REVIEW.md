# Scientific review

## Correctness: PASS

For any three deleted vectors the surviving frame operator is \(pI-V_EV_E^*\). The least eigenvalue equals \(p\) minus the erased three-column Gram norm; the largest eigenvalue stays \(p\) because rank is at most three and \(p\ge5\). The proof treats one, two, and three distinct translation classes separately. In the final case the quadratic Gauss-sum formula provides an exact normalized triangle phase, and an explicit degree-three characteristic polynomial yields the norm. Character arithmetic proves both a universal lower bound on the absolute triangle angle and attainment in every prime residue class. The standalone checker reconstructs the actual vectors and agrees for \(308{,}704\) exhaustively checked triples and \(8{,}580\) direct triangle phases. All quantifiers and normalization factors are fixed in `RESULT.md`. The limits and absence of independent audit are stated.

## Originality: PASS relative to inspected evidence

The closest source, Salanevich–Strachan (arXiv:2509.01325, September 1, 2025), proves general robustness bounds (Theorems 1.5 and 5.5) and provides a numerical example for three erasures in dimension five (Table 1). The present claimed difference is the exact infinite-prime sharp formula and explicit parity-dependent attaining phase, not the already-observed dimension-five number. Bengtsson–Blanchfield–Campbell–Howard (arXiv:1407.2713) concern Clifford symmetries and modulo-three orbit splitting, while Filippov–Man'ko (arXiv:1008.2675) establish general MUB triple-product relations, not sharp Alltop triple-erasure conditioning. The closest database records on adversarial erasures concern two-character harmonic frames, not the Alltop orbit. Searches for a three-erasure Alltop formula, Bargmann-phase variants, and sparse Gram formulations found no dominating theorem. Residual risk remains from less-indexed mathematical-physics literature or an equivalent general three-Gram-triangle result.

## Value: PASS

Exact worst-case conditioning under loss of three measurements is a natural deterministic robustness invariant of a widely used structured frame; it directly supplies the optimal reconstruction noise-amplification constant within that measurement design. In contrast to generic coherence-only bounds, this theorem detects a nontrivial quadratic-Gauss phase obstruction that depends on the prime modulo four. The closed formula and constructive extremizers resolve the full infinite family without arbitrary parameter cuts. The numerical dimension-five case already existed and is not the proposed value by itself.

Self-review: passed. Independent audit: not yet performed.
