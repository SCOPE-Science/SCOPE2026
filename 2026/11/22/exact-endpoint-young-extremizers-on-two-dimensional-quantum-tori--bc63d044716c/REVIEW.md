# Scientific review — exact endpoint Young extremizers on two-dimensional quantum tori

## Correctness: PASS

The statement fixes two arbitrary real deformations and finite nonzero Fourier polynomials. The proof uses the established coefficientwise formula for deformation-addition convolution and normalized Weyl orthogonality. Equality in Cauchy–Schwarz forces identical supports with proportional coefficient moduli. A norm-attaining state of the positive square of the output, followed by its GNS construction, turns equality in the unitary triangle inequality into a joint eigenvector of all support-difference Weyl operators; their scalar commutators force integral symplectic products. Conversely, the faithful canonical trace gives full torus joint spectrum on the commuting isotropic subgroup, so any compatible twisted character reaches the sum of coefficient magnitudes. Lattice rank and the exact rational denominator condition follow without approximation. The rank-two phase formula was checked algebraically against the cocycle; finite diagnostics are supporting checks, not an infinite proof.

## Originality: PASS, with stated bibliographic risk

Sukochev–Tastankul–Tulenov–Zanin, arXiv:2611.16350v1, Sections 3–4, establishes the convolution and general optimal constant one but gives the constant input as a sharpness witness rather than a complete endpoint equality classification. The full text's relevant Fourier formula (Proposition 3.5) and proof of Theorem 4.1 were inspected. Liu–Wu (2018), Theorem 4.8, classifies extremizers for a different Kac-algebra convolution, with a hypothesis of equality at an interior Young triple; it does not furnish the present two-deformation, finite-support endpoint lattice-and-cocycle criterion. Huang–Liu–Wu (2022) addresses Frobenius-von-Neumann convolution and entropy. Published mathematical-record comparisons on quantum-torus Young equality, twisted characters and lattice isotropy yielded no dominating claim. The ordinary-torus special case and the general norm-attaining-state argument are established ingredients, not asserted novel. Residual risk is an unindexed equivalent characterization in twisted group algebra or noncommutative Fourier-extremizer literature.

## Mathematical value: PASS

The central structural question is to describe **all** equality cases in a genuinely sharp inequality for a newly introduced operator convolution, rather than supply another sharpness witness. The answer isolates three logically independent obstructions: input magnitude mismatch, noncommuting support differences, and incompatible phases. For three noncollinear frequencies, it yields an exact denominator-versus-lattice-area classification and a sharp rational–irrational change; this phenomenon disappears in classical commutative convolution. The natural finite-polynomial core is fully classified. This does not assert classification of arbitrary \(L_2\) inputs or a general quantitative stability theorem.

## Evidence and remaining limits

The proof is self-contained after standard Weyl relations, faithful trace, and basic \(C^*\)-algebra state existence. `VERIFY.py` runs bounded exact integer checks of the character cocycle and representative half-deformation examples, but these are not substitutes for the proof. The results have not been checked by an independent auditor, and historical priority beyond the inspected sources remains open.

Self-review: passed. Independent audit: not yet performed.
