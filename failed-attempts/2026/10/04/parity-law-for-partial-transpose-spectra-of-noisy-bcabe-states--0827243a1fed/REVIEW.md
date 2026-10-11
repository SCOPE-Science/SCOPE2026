# Independent mathematical audit

## correctness

PASS

The four vertices are the four joint eigenspaces of the commuting global Pauli strings, each of dimension \(4^N\), so the original eigenvalues are \(p_i/4^N\). Partial transpose flips only the global \(Y\) coefficient once per transposed qubit; an odd flip reflects the tetrahedron to its antipodes and gives \((1/2-p_i)/4^N\), while an even number returns the original state. Summing the only possible negative block gives the two negativity formulas. Fresh direct matrix construction for \(N=1,2\) independently reproduced every parity spectrum for a nontrivial weight vector.

## originality

FAIL

Hiesmayr et al. already publish the exact three-Pauli simplex representation and explicitly state that partial transpose of one qubit flips the \(Y\) coefficient, any odd number of transposes is equivalent to one, and any even number returns the original positivity geometry. Bandyopadhyay et al. explicitly map the noisy four-weight BCABE family to two-qubit Bell-diagonal entanglement. Reading the four affine tetrahedron eigenvalues and applying the standard Bell-diagonal trace-norm formula is therefore a direct corollary of the combined prior statements, even though the multiplicity-scaled spectrum is not printed in the same notation.

## value

FAIL

The parity-uniform negativity formula is useful exposition, but after the published Pauli-tetrahedron representation, odd/even PT rule and Bell-diagonal mapping are in hand, obtaining the eigenvalues and trace norm is routine diagonalization. Under the common value bar this is not a new structural gap independent of the known geometry.

The dated certificate retains the supplied scientific assessment, sources and limitations.
