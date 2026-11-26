# Independent mathematical audit

## correctness

PASS

The free Fourier energies are 2J cos((2πl+phi)/N); their monic characteristic polynomial is 2J^N[T_N(z/(2J))-cos(phi)]. Cyclic translation makes all diagonal cofactors equal, so adding the absorbing site adds i gamma/N times the free polynomial derivative, including at poles by polynomial identity. Independently, at the protected flux put E=2J cos(q), and write the free polynomial locally as the product of the two crossing factors and the remaining factor R, with R(E) nonzero. The secular derivative in z there is (2i gamma/N)R(E), proving simplicity. At fixed z=E the two detuned free energies have opposite slopes ±2J sin(q)/N; the free part of the secular polynomial therefore contributes -(2J sin(q)/N)^2 R(E) delta². The cofactor is flux independent (deleting the absorbing site leaves a path with gauge-removable phases). Solving the implicit equation gives -i 2J² sin²(q)/(gamma N) times delta². Flux enters through cos(phi), and uniqueness gives evenness and thus O(delta⁴). The real shift is at most O(delta⁴), not necessarily a nonzero quartic term. A real eigenvalue forces the trap amplitude to vanish by the dissipative identity; off 0 or pi the free spectrum is simple and each Fourier eigenvector has nonzero trap amplitude. Unpaired band-edge modes are likewise not dark. The probability rate is twice the eigenvalue linewidth in this convention. This is fixed-parameter and mode-local; the supplied numerical checks were inspected, not executed.

## originality

FAIL

The bound coefficient is not stated verbatim in the inspected early literature, but it is a mechanical specialization of an earlier exact transfer-matrix equation. Heinrichs, arXiv:cond-mat/0106437v1, Eqs. (12)–(18), gives the exact trace condition for a tight-binding ring with general diagonal site potentials, before making a weak-disorder expansion. That derivation uses unimodularity and the linear recurrence, not reality of the potentials, and therefore extends algebraically to a single imaginary potential. The single rank-one insertion produces precisely the bound secular polynomial, from which simplicity, evenness, the coefficient and the restriction on real eigenvalues follow directly. This failure is based on an inspected governing result, not on the unavailable 1996 article or on dating a later equivalent catalogue entry.

## value

FAIL

The mode-resolved linewidth is physically useful, and its normalization is worth getting right. As the contribution claimed here, however, it is the direct simple-root expansion of a prior general spectral condition with one rank-one matrix insertion. The symmetry and no-dark conclusion follow from that same specialized equation. No genuinely distinct mathematical remainder (such as a uniform detuning/loss limit or survival theorem) is part of the frozen claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
