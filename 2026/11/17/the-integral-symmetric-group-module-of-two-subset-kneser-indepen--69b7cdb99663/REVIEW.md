# Scientific review: integral symmetry of two-subset Kneser independence homology

## Correctness (C): PASS

Every face is either contained in a vertex star or is a unique three-edge triangle. The specified face-poset map to the simplex two-skeleton is simplicial and permutation-equivariant. On the union of stars it is a homotopy equivalence through the complete-graph incidence spine; on every exceptional triangle it is a piecewise-linear homeomorphism to the corresponding two-cell. Cellular gluing establishes the map's ordinary homotopy equivalence. The top homology of the full simplex two-skeleton is the kernel of exterior contraction, identified **integrally** with the third exterior power of the augmentation lattice. Standard representation theory then supplies the hook character; blockwise restriction supplies quotient rational Betti numbers. This is a proof for all integers \(n\ge4\), not an inference from finitely many computations.

Independent finite checks in the accompanying program verify all face-map inclusions and flag bijections through \(n=7\), every automorphism through \(n=6\), every cycle-type character through \(n=7\), modular Betti numbers and all Young-subgroup character averages through \(n=6\). The structural proof remains necessary for arbitrary \(n\) and for the integral assertion.

## Originality (O): PASS, with publication-priority limits

The closest exact-source antecedent is Barmak, arXiv:1007.0418v1, Theorem 4.11, which supplies precisely the ordinary wedge of spheres and therefore already implies all nonequivariant Betti numbers; none are claimed new. The new claim is the **natural symmetric-group action over the integers**, realized by an explicit equivariant simplicial map, and the complete rational homology of every block-permutation quotient. Barmak's specific contraction chooses a fixed ground element, and does not provide this equivariant information. Braun's arXiv:0912.0720v1 analyzes stable Kneser graphs, not the full graph, and Feng–Wang's arXiv:2404.10566v1 explicitly sets its new results at subset size at least three. Relevant published searches also find Schultz's work on stable-Kneser Hom complexes, a different construction.

Closest accessible historical statements were compared by object, coefficient, symmetry group, and logical implication. No indexed result directly covers the relabeling-equivariant map or the integral lattice and Young-subgroup conclusions. A construction equivalent to the present map may nevertheless exist in unindexed or differently phrased sources; this remains a publication-priority risk, not a mathematical independence claim.

## Mathematical value (V): PASS

For the canonical \(\mathrm{KG}(n,2)\) family, Barmak's binomial Betti number does not determine how relabelings act on cycles. The new integral lattice and actual equivariant map give a uniform natural model, not a mere character computation for an arbitrarily chosen finite graph. The sharp four-block threshold for rational homology of orbit spaces is a consequence beyond the nonequivariant wedge classification; it is independent of all block sizes and varies under naturally motivated quotients by within-class relabelings. The scope is an infinite, structurally canonical graph family. The result is not a solution for higher-subset Kneser graphs, nor a computation of integral orbit-space torsion.

Self-review: passed. Independent audit: not yet performed.
