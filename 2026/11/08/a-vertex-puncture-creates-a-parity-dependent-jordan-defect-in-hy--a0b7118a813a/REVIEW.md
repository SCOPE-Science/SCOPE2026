# Scientific review

## Correctness — PASS

For \(d\ge2\) and any finite characteristic-two field, the block identity obtained from the cube adjacency matrix gives \(B^2=(d\bmod2)I+bb^{\mathsf T}\) and \(Bb=0\). When \(d\) is even, this implies \(B^3=0\) and \(\operatorname{rank}B^2=1\); a kernel comparison with the full cube proves \(\operatorname{rank}B=2^{d-1}\) and forces exactly one length-three and \(2^{d-1}-2\) length-two Jordan blocks. When \(d\) is odd, the decomposition \(\mathbb F_q^{2^d-1}=\mathbb F_qb\oplus b^\perp\) is invariant, with one zero direction and an involution on the complement; the full-cube rank establishes that every nonzero block is a length-two unipotent block. The kernel-size and fixed-space formulas then give the claimed counts. Boundary cases \(d=2,3\) are explicitly covered. Two independent scripts directly verify finite cases with exact arithmetic and full configuration enumeration. They do not substitute for the general proof.

## Originality — PASS (qualified)

The closest directly overlapping source is Kim–Reiner–Schoenzeit (arXiv:2608.27887), whose real eigenvalues and eigenspaces concern the same vertex-deleted cube but cannot be reduced to characteristic two to recover generalized eigenspaces: the ordinary Fourier basis is singular modulo two. Lu (arXiv:2609.06747) treats real punctured adjacency-degree algebras, not a modular temporal map. Moreno–Bollman–Aviño-Díaz (arXiv:math/0604534) supplies the general finite-linear-dynamics language but not a cube-specific Jordan decomposition. Istrate (arXiv:1102.1440) studies an asynchronous, mostly odd-modulus process. The closest separately examined hypercube modifications are edge deletion and distance-two/three neighbor operators; these are not the principal submatrix used here. The direct claim and its wider algebraic implications were searched; no equivalent statement was found in the accessible scientific sources. The possibility of a missed older modular rank/Jordan calculation remains.

## Mathematical value — PASS

The punctured Boolean cube is a canonical one-site perturbation of a symmetric product graph. Removing a single vertex produces a parity-dependent qualitative change: a length-three nilpotent delay when the unpunctured model dies in two steps, or a new transient direction when the unpunctured model is a permutation. The full, nontrivial Jordan classification determines every exact first-entry and primitive-orbit population for an infinite family of graphs and field sizes. This answers a natural graph-automaton boundary-defect question rather than an arbitrary fixed-size computation.

## Remaining risks

There is a historical-priority risk from earlier or unindexed studies of punctured hypercube adjacency matrices modulo two. The literature on characteristic-zero spectra cannot establish originality of a modular result by itself; specific comparisons were carried out, not a claim of exhaustive database coverage. No expert or independent audit has been performed.

Self-review: passed. Independent audit: not yet performed.
