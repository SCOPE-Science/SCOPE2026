# Scientific review: arm-permutation cohomology of star nilmanifolds

## Correctness — PASS

The group law, integer lattice, Lie brackets and finite arm-permutation action are explicit. The Chevalley–Eilenberg differential is \(d=a\wedge E\), so the degreewise equivariant kernel/cokernel decomposition is immediate. A degree-zero \(\mathfrak{sl}_2\)-triple commuting with the arm action proves the coefficient-extraction lemma on **all** exterior powers; the super-symmetric-power generating series then yields the closed orbit-space Betti polynomial. The exact stand-alone modular checker independently tests the chain-level trace identities for every permutation of up to four arms (304 degree/element comparisons), while the proof—not an extrapolation—handles all arm counts in characteristic zero. The cohomology of a finite smooth group quotient equals the invariant rational cohomology by averaging on equivariant triangulations. Rational coefficients, rank bounds and the special \(n=1\) case are stated explicitly.

## Originality — PASS (best-knowledge comparison)

The 1997 Armstrong–Cairns–Jessup paper already computes the star Lie algebra's ordinary Betti numbers using the degree-zero derivation, and its kernel/cokernel framework must not be presented as new. The 2024 Aldi et al. paper provides the star cohomology calculation through induced subgraphs, with no arm-permutation character statement in the inspected relevant sections. The November 2026 paper concentrates on path graph nilmanifolds and cites star results as known; no arm-permutation characters or orbit-space Betti spectrum were located in the relevant full text. Targeted literature and research-record searches did not identify the cycle-type trace formula or the topological quotient's linear cohomology spectrum. The new nontrivial work is the commuting \(\mathfrak{sl}_2\) and super-symmetric invariants refinement, which is not implied by the numerical Betti polynomials. Residual risk: the 1997 source was materially inspected only through accessible excerpts rather than every page, and equivalent unpublished or unindexed representation results are possible.

## Mathematical value — PASS

The unrefined total rational cohomology grows as \(2\binom{2n+1}{n}\), whereas the naturally defined permutation quotient retains exactly \(6n\) dimensions. The closed trace formula further determines invariants for *every* subgroup of the arm-permutation group by character averaging, not merely its full quotient. This is a meaningful topological symmetry refinement for a canonical graph-nilmanifold family relevant to the developing explicit Poincaré-polynomial theory, rather than a recomputation of known Betti numbers. The quotient's characteristic-zero cohomology is genuinely distinct information not recoverable from the ordinary Betti polynomial.

## Closest literature and limits

- Armstrong, Cairns and Jessup (1997), *Explicit Betti numbers for a family of nilpotent Lie algebras*: ordinary dimensions and derivative-kernel method, strong prior coverage of the nonequivariant part.
- Aldi et al., arXiv:2402.14188v2, §4: existing complete star Betti calculation by a different method.
- Aldi et al., arXiv:2611.17014v1: new formulas for *path* nilmanifolds; star formulas cited as previously known.

This is a characteristic-zero representation and orbit-space Betti theorem, not an integral ring calculation. Unindexed equivalent work is a publication-priority risk. The code provides bounded finite-field tests but no infinite proof; the infinite proof is supplied in the result text.

Self-review: passed. Independent audit: not yet performed.
