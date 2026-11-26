# Independent mathematical audit

## correctness

PASS

Euclidean orthogonal conjugation of the coordinate positive part is indeed the metric projector onto the rotated orthant. Because U is onto, every strict sign mask is realized. Inside its chamber the Jacobian is U^T D U and its induced maximum-row-sum norm is achievable by a sufficiently small displacement in a norming sign direction. On a segment the map is piecewise linear with those slopes; any coordinate that is identically zero along the segment can be designated inactive without changing the slope. Thus the exact Lipschitz coefficient is the maximum across masks, including the all-active identity. A row u gives the singleton mask uu^T, of norm ||u||_infty ||u||_1 >= ||u||_2^2=1. Equality forces all nonzero magnitudes to be equal. The complementary mask has absolute row sums 1+|u_j| ||u||_1-2u_j^2, also valid at zero coordinates. On a flat row with k supported entries this gives 2-2/k at supported coordinates, ruling out k>=3 and proving the expansion certificate. Orthogonal singleton rows occupy entire columns; a row on a pair can have an overlapping orthogonal row only on the identical pair. Column normalization gives exactly one partner and the pair is a signed and permuted Hadamard block. Conversely all masks on a singleton or Hadamard pair are contractive, and signed permutations preserve the norm of the mask collection (row signs do not change a mask projector; row permutations relabel masks). The identity chamber supplies coefficient one, including dimension one. An exact independently checkable expansive example is U=(1/5)[[3,4],[-4,3]]: each of its two singleton masks has maximum absolute row sum 28/25, so the four-mask maximum is 28/25. At x=U^T(1,-1) a step of (1,1)/2 stays in the first singleton chamber and realizes this quotient.

## originality

PASS

The precise supported distinction is the classification of square real orthogonal ReLU conjugations in the coordinate maximum norm, equivalently the Euclidean orthonormal row bases that are 1-suppression unconditional for that norm. I credit the general contractive-projection and basis formulations, the known chamber-norm tools, and Hilbert projector stability. The inspected primary statements did not give the joint all-mask criterion evaluated on these bases or the row-based expansive witness. Earlier equivalent basis-theoretic coverage remains possible.

## value

PASS

Euclidean projector stability is automatic in its own norm, but coordinate maximum-norm stability is a distinct, motivated perturbation requirement. The classification gives a complete structural boundary for tied orthogonal ReLU conjugation: disjoint 45-degree pairs are possible, while all other mixing loses coordinate nonexpansivity. The row certificate gives a witness without inspecting every sign mask, including a dimension-independent gap for a row with fixed flat support k>=3. The conclusion is not merely a low-dimensional calculation or a reassertion of Hilbert nonexpansivity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
