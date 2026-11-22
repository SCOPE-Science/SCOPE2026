# Scientific review: Endpoint rigidity for orthogonal ReLU projection

## Correctness — PASS

Every strict orthant sign mask occurs because the orthogonal transform is onto. The global coordinatewise Lipschitz coefficient is therefore the maximum maximum-row-sum norm of the finitely many masked orthogonal projectors. For each row, singleton and complementary active masks enforce equal absolute values on its support and then support size at most two. Orthogonality forces each two-coordinate support to be a complete disjoint Hadamard pair. Every mask on these blocks has maximum row sum at most one, completing the reverse implication. The proof covers finite-input quotients and sign-boundary continuity. The supplementary checker covers finite sample cases only.

## Originality — PASS, with priority qualification

The nearest located related works are Hasannasab et al., *Parseval Proximal Neural Networks* (arXiv:1912.10480), which discusses Hilbert-norm nonexpansivity of proximal networks; Anil et al., *Sorting Out Lipschitz Function Approximation* (arXiv:1811.05381), which addresses constrained neural architectures and induced norms; and Randrianantoanina, *Norm One Projections in Banach Spaces* (arXiv:math/0110171), which surveys much broader contractive-projection theory. The sections inspected do not directly establish the classification of real orthogonal conjugates of ReLU that remain nonexpansive in the coordinate maximum norm. Searches using the equivalent notions of suppression-unconditional orthonormal bases, all-coordinate-subspace norm-one projections, and rotated orthant projection found no direct matching theorem. An earlier equivalent characterization in classical unconditional-basis literature remains a genuine priority risk. A failed search is not a proof of novelty.

## Mathematical value — PASS

This is a complete all-dimensional rigidity classification for a canonical Euclidean proximal map under a non-Hilbert robustness norm. It distinguishes the exceptional admissible 45-degree pair rotations from all generic rotations, and supplies explicit row-based expansion certificates. It gives a structural design constraint for orthogonal activation layers rather than a routine rephrasing of Hilbert-norm nonexpansivity. It does not claim a formula for the expansive constants, rectangular frames or multilayer compositions.

Self-review: passed. Independent audit: not yet performed.
