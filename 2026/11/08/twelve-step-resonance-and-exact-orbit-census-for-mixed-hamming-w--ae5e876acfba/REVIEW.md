# Scientific assessment

## Correctness — PASS

For each even coordinate the all-ones operator squares to zero and has one length-two Jordan summand. A tensor contracting homotopy proves that the sum of these operators has rank \((V-C)/2\), rather than merely bounding it. For each odd coordinate the all-ones operator is diagonalizable with eigenvalues zero and one; parity-weighted binomial expansion yields the exact \(h_0,h_1\) multiplicities. The two corresponding wave summands satisfy respectively \(T^4=I\) and \(T^6=I\). A direct fixed-kernel calculation produces all six \(F(t)\), and Möbius inversion then gives exact primitive orbit populations. Nonzero even-coordinate rank and positive odd-coordinate primary dimensions exhibit states of exact periods four and three, so their direct sum has period twelve. All quantifiers and graph conventions are explicit in RESULT.md. Independent finite implementations gave matching output in `check_matrices.stdout.txt` and `check_bruteforce.stdout.txt` (nineteen binary graph families through 36 vertices, plus direct dynamics on 266,576 states). These experiments are corroboration, not the infinite proof.

## Originality — PASS, qualified

Vlasov (arXiv:1311.4297, 2013, Sections 3 and 6.1) develops the standard reversible two-time-level construction but does not provide the mixed-arity Hamming-graph fixed-point census. Klavžar–Peterin (DOI 10.1002/jgt.20084, 2005, Sections 1–4) characterizes Hamming graph embeddings, not finite-field wave orbits. Valyuzhenich (arXiv:2003.01571, 2020, eigenfunction material) treats ordinary real Hamming eigenfunctions and minimum bitrades; real eigenvalue multiplicities alone do not give nonsemisimple characteristic-two Jordan ranks when factors have even size. Related published complete-multipartite reversible-wave, strongly-regular-graph reversible-wave, and reversible hypertorus results concern, respectively, different edges, diameter at most two, or cyclic factors with distinct nilpotent structures. The present uniform fixed-census with sharp period twelve for mixed-parity Cartesian-clique graphs is not implied by their statements. Relevant semantically indexed published mathematical findings and accessible prior claims were compared by operator and graph family, not just by title. Residual risk: unindexed historical results or unexamined wider algebraic wave frameworks may subsume the claim; the review does not assert exhaustive world-wide priority.

## Mathematical value — PASS

This is a complete two-parameter-style (indeed arbitrary-dimensional and mixed-alphabet) recurrent-orbit classification for a canonical graph product family. The parity of the factor cardinalities forces two competing wave clocks, with a sharp period-twelve resonance, and the full labelled period census resolves every recurrence class, not merely the global order or one small example. The characteristic-two tensor-rank lemma is an explanatory mechanism that separates these dynamics from ordinary real-spectral descriptions. The unrestricted all-parity variants and spatial-symmetry quotients remain outside the claim.

## Scope and residual limits

The theorem is for \(d\ge3\), at least one odd and one even \(q_i\), and finite fields of characteristic two. The graph is loopless, vertex-labelled, and uses unit neighbor-sum weights. All six least periods arise; no statement on arbitrary graph products, external disturbances, or infinite alphabets is made. Numerical checks use only binary fields. Publication searches and full-text comparisons reduce but cannot eliminate historical-priority uncertainty.

Self-review: passed. Independent audit: not yet performed.
