# Independent mathematical audit

## correctness

PASS

For independent local depolarization the Pauli string of weight j decays at j*gamma. On trace-one states the full Poisson reset adds r(rho_D-rho); solving each coefficient gives x/(x+j), including the preserved identity, and uniqueness for r>0. Independent symbolic reproduction (independent_pt.py, Python 3 and SymPy) sums signed Pauli expectations on the six computational Dicke components; only weights 0, 2 and 4 survive. Partial transpose on the leading k qubits negates precisely the strings with an odd number of Y factors there. With Q=(x+2)(x+4), automatic component factorization of the two exact matrices scaled by 12Q gives all factors and multiplicities in RESULT.md §§2–3. In particular, for k=1 the possibly negative scaled roots are 6-9x-6x^2=3(x+2)(1-2x) once and 6-x twice; the remaining linear roots and both roots of the quadratic are positive for x>0. For k=2 the possible negative scaled roots are 6-7x-4x^2 twice and 6-4x-2x^2=2(1-x)(x+3) once. In each sector the residual quadratic has two real roots (Hermiticity), positive root sum and strictly positive product for x>0. Dividing by 12Q and summing negative magnitudes checks both negativity laws. Negative counts are 0/1/3 on (0,1/2], (1/2,6], (6,infinity), and 0/2/3 on (0,beta], (beta,1], (1,infinity), where 1/2<beta=(sqrt(145)-7)/8<1. This verifies the half-open cut-dependent window, including the zero eigenvalues at transition points. Symmetry gives four cuts of type 1|3 and three of type 2|2. The unreset limit is I/16 and the pure-state limits give negativities 1/2 and 5/6. This proof establishes PPT and NPT, not separability of PPT cuts or a multipartite entanglement classification.

## originality

PASS

The checked nearest results share the noise-plus-reset model for other initial states, or the Dicke state for other noise or invariants. The supported distinct claim is the pair of complete stationary cut spectra and their distinct exact PPT and inertia transitions. Neither generic renewal weights nor a Dicke witness gives those eigenvalues. Chen–Jiang full-text coverage remains unresolved; the verdict is bounded by the sources actually inspected.

## value

PASS

Equal noise on all sites need not produce the same PPT behavior on cuts of different sizes. This exact stationary example identifies the sharp interval where all one-versus-three cuts are NPT but every balanced cut is PPT, and locates additional inertia changes invisible to a single witness. The resource state and channel are independently motivated; the full cut-resolved profile is useful for comparing robustness in this reset model without claiming separability or multipartite entanglement beyond the spectral conclusions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
