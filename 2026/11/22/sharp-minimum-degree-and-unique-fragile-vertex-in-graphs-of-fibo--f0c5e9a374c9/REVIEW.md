# Self-review

**Correctness — PASS.** The proof fixes the maximal run convention, both endpoint cases and all quantifiers for integer \(q\ge2\). It proves a degree lower bound by counting distinct legal bit flips; an explicit all-one witness proves sharpness. Deleting the one or three forbidden cube vertices gives the two short boundary multiplicities, and a separate exhaustive case analysis by number and distribution of ones establishes uniqueness for all larger lengths. The standalone direct word-and-edge test completed 63 parameter instances (16,018 admissible words), without being substituted for proof.

**Originality — PASS, with residual priority risk.** The primary source arXiv:2010.09505v1 studies exactly these words and their enumeration/Gray listings, but the inspected relevant sections do not classify the *induced one-flip graph's* minimum degree and minimizing vertices. The related 2024 two-change cyclic Gray-code result does not imply the local one-change degree formula. Fibonacci-run graph degree enumerators concern a distinct graph/restriction; even an equal-sized vertex set is insufficient for adjacency equivalence. Semantic database comparisons returned no matching implication, although missing aliases or older papers remain possible.

**Value — PASS.** Minimum Hamming-neighbor degree is a natural structural robustness parameter of constrained-word state graphs used for exhaustive Gray-code generation. The result exposes a parameter-uniform sharp transition at \(n=q+3\), with a unique locally fragile vertex thereafter, beyond a mere finite computation. It distinguishes local bottlenecks from stronger Hamiltonicity or coding assertions, which remain outside scope.

The closest literature is Baril–Kirgizov–Vajnovszki (2020; arXiv:2010.09505), Wong–Liu–Lam–Im (2024; DOI:10.1007/978-981-97-0566-5_8), and Eğecioğlu–Iršič (2020; arXiv:2010.05521). Priority risk: other descriptions of the same induced word graph or unindexed degree arguments may exist. No expert or independent review was conducted.

Self-review: passed. Independent audit: not yet performed.
