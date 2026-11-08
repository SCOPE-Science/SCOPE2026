# Scientific review: All-scale coordinate-fixed spheres in Hamming-cube Vietoris–Rips complexes

## Correctness — PASS

For every integer \(n\geq1\), \(0\leq r<n\), the geometric fixed-space orbit-barycenter construction is valid for a finite simplicial complex under coordinate permutations. The exact intralayer and interlayer Hamming-distance maxima identify the fixed model with the independence complex of a specified bipartite band graph, without losing any orbit simplices. The open-neighborhood folding lemma is proved by ordering elementary free pairs; the deterministic block procedure verifies every required neighborhood inclusion and reduces the band graph to exactly \(1+\lfloor\lfloor r/2\rfloor/(n-r)\rfloor\) disjoint edges. Their independence complex is a cross-polytope boundary, proving the integral homotopy type. The free complement action and its sign follow from the absence of complement-invariant simplices and the Lefschetz identity. Edge cases \(r=0\), \(r=n-1\), and \(n=1\) are included. The standalone checker reproduces 55 direct orbit comparisons, 55 independent mod-two homology checks, 1,220 admissible fold sequences and 28 complete small elementary-collapse calculations. Neither finite checks nor homology alone replace the unrestricted proof.

## Originality — PASS with residual risk

Galetto–Montaño–Wellner, arXiv:2606.20784, Sections 1, 7 and 8, provide the whole-complex rational homology representations at selected radii but do not classify geometric coordinate-fixed spaces. Bendersky–Elia–Grbić, arXiv:2605.00705, Sections 1–2 and 4, establish whole-complex cohomological bounds and generators, not this fixed locus. Adams–Virk, arXiv:2309.06222, Sections 1, 3 and 4, address whole-complex Betti bounds and scale inclusions; those maps are not equivariant fixed-space equivalences. The closest earlier fixed-space statement covers only \(r=n-2\), which the new all-radius theorem recovers while determining every other \(0\leq r<n\), including explicit dimension jumps and the complement character. Relevant direct literature searches and mathematical-result searches did not locate an all-radius equivalent. Searches are not proof of novelty, and equivalent work may be unindexed or described differently.

## Mathematical value — PASS

The complete radius-by-radius fixed-space classification gives an exact, nontrivial topological phase diagram over two unbounded integer parameters, even where ordinary hypercube Rips homotopy remains difficult. The uniform variable-band folding lemma reveals that all nonempty full-coordinate fixed spaces are single spheres, with potentially large jumps in dimension across successive radii. The top-degree integral complement sign distinguishes a residual symmetry not available from the nonequivariant sphere count. This is substantially broader than a single endpoint-scale example and isolates a natural equivariant invariant relevant to current hypercube Rips research.

## Limits and closest sources

The result does not classify arbitrary subgroups, the maps between successive fixed-space stages, or the unrestricted complex at unknown scales. Prior equivalent work not captured by the checked sources remains possible. The most relevant public scientific sources are arXiv:2606.20784, arXiv:2605.00705, and arXiv:2309.06222. All programmatic checks are reproducible with the included Python program.

Self-review: passed. Independent audit: not yet performed.
