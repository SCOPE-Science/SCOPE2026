# Independent mathematical audit

## correctness

PASS

Use the conjugate of the polynomial coefficient vector in the Hermitian lift v(z)*Hv(z). The six-point DFT separates modes 0, ±1 and ±2 and combines ±3 into one real Nyquist equation per ring. When sin(3(ψ−φ))≠0 the two Nyquist equations kill h03. At distinct a=r² and b=s² the second-superdiagonal linear coefficient polynomial vanishes identically; the first-superdiagonal quadratic is c(t−a)(t−b), and the diagonal cubic is (t−a)(t−b)(u+vt). This characterizes the entire kernel and gives real dimension four. If c≠0 the three adjacent entries are nonzero and the tridiagonal recurrence shows nullity at most one. If c=0, a nonzero diagonal polynomial cannot have at most two monomials and two distinct positive roots. Hence no nonzero difference of two rank-one lifts can lie in the kernel. For equal radii, 1 and (z/r)^3 have equal sampled moduli; for angular resonance e^(−3iφ)z³ is real at every node and 1±i e^(−3iφ)z³ are an ambiguity. These witnesses are inequivalent, and the lift covers zero and lower degrees. VERIFY.py was read, not run: its rank and generator checks are finite floating-point tests, and the random-signal conditional comparison is not a universal collision check.

## originality

FAIL

A distinct indexed all-degree theorem states the same all-signals if-and-only-if for the same two labeled regular 2d-gons, with arbitrary positive radii. Substituting d=3 gives the frozen criterion. Its angular demixing also supplies the full linear Fourier constraints; the particular four-parameter kernel, while not explicitly located as a statement in that theorem, is their direct cubic radial interpolation. This establishes existing coverage, not authorship or provenance. No independently substantive remainder is proposed.

## value

PASS

The complete injectivity and degeneracy criterion for a naturally balanced sampling design is useful, and the tridiagonal proof provides a concise algebraic explanation. This does not make the covered special case novel, nor does merely writing out the direct four-parameter kernel warrant a separate repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
