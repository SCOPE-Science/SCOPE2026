# Independent mathematical audit

## correctness

PASS

There are 96 quaternary four-mers with exactly two GC positions, divided into six GC-location masks with 16 variants each. For any three same-mask words, the sum of their three pairwise Hamming distances is at most eight, so minimum distance three permits at most two per mask, hence |C|<=12. To attain equality choose one of 40 distance-compatible unordered pairs in each mask. RC exchanges 0011<->1100, 0101<->1010; the fixed 0110 and 1001 masks each have 4 RC-invariant eligible pairs. Enumerating exactly 40^2*4^2=25,600 possibilities and testing all inter-mask distances yields precisely 16 distinct closed 12-word maxima. A newly written independent Python enumerator confirmed 16 with fixed-RC counts 8 without and 8 with four, and under the natural 64-element action five orbits of sizes (2,2,4,4,4). Each has 18 pair distances four and 48 three. Exactly eight fixed-point-free maxima admit 2^6 orientation choices, giving the 512 conventional oriented six-word optima; no double counting occurs. Source verify_masks.py and verify_graph.py were examined; the bounded exhaustive proof is a complete finite argument, not simulation.

## originality

PASS

King 2003 gives the optimum 12 for GC Hamming only and 6 for RC-separated oriented codes; 2026/10/12 earlier census gives EXACTLY 512 oriented six-word optima and their matching structure. These prior results are explicitly excluded from novelty. The new surviving statement is the full 16-codebook classification of 12-word sets CLOSED under RC (including all eight optima with four self-RC fixed strands), and five symmetry classes for that distinct closure convention. Oriented code conditions exclude self-RC words and cannot imply the other eight closed 12-word codebooks. Qualified because Aboluion–Smith–Perkins 2012 full text is inaccessible.

## value

PASS

Complete equality classification of the natural distinct RC-closure DNA code convention resolves the 16 possible optimal codebooks, their fixed-strand dichotomy and five symmetry classes; it identifies behavior excluded by the earlier RC-separation convention. Exact small extremizer counts and structure are legitimate coding-theory invariants for a constrained four-mer space, rather than a repeated known capacity number.

The dated certificate retains the supplied scientific assessment, sources and limitations.
