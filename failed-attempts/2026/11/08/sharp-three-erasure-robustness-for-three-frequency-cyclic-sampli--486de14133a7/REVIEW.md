# Independent mathematical audit

## correctness

PASS

Roots-of-unity orthogonality makes the normalized sampler an isometry. Erasing E subtracts the erased Gramian from I; dephasing each unnormalized erased row by ω^(−j) makes its row Gramian have diagonal 3 and kernel 1+2cos(2πs/N). For N≥8, |kernel|≤e at all circular distances ≥2. A nonconsecutive triple has at most one adjacent pair; after sorting that pair onto a d-edge, its absolute Gram matrix lies strictly below the consecutive matrix on at least one d-edge. The Rayleigh modulus inequality and irreducible nonnegative comparison give strict loss separation. For N=6,7 the nonadjacent absolute entries are at most 1, so the comparison matrix with edges (d,1,1) has top 3+(d+√(d²+8))/2, below 3+√2 d since d²≥4>2+√2. This is at most L_N. Reflection splits the consecutive block into the odd eigenvalue 3−e and two even roots, the upper of which is simple. Mapping (1,r,1) back by the dephased row adjoint yields precisely the stated centered coefficient vector; translation by t modulates coefficient k by exp(−2πitk/N). Full rank follows from a three-site retained Vandermonde minor, the endpoint follows from d=2,e=0, and expanding d=3−θ²+O(θ⁴), e=3−4θ²+O(θ⁴) yields L_N=9−4θ²+O(θ⁴). The inverse best conditioning factor is the stated reciprocal singular value.

## originality

FAIL

Two distinct same-date Resultary findings state the equivalent sharp minimax bound with the same hypotheses and strict mask classification. The centered coefficient line follows by a two-dimensional reflection calculation for the same three-site block; it does not supply a distinct substantive result. No order or historical priority between the same-day reports is asserted.

## value

FAIL

Sharp worst-mask stability is a useful question for finite Fourier recovery, but the exact minimax fact and unique geometry are independently covered. What remains here is a routine eigenvector of the covered 3-by-3 matrix, its translation phases, and elementary endpoint/asymptotic consequences. No additional independently useful new exact invariant was established.

The dated certificate retains the supplied scientific assessment, sources and limitations.
