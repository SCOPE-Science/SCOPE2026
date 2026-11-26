# Independent mathematical audit

## correctness

PASS

On all complex matrices the Hilbert–Schmidt orthonormal Weyl basis is W_(a,b)/sqrt(N). The columns for Tr(PH) are the distinct characters of the shift–modulation group times A(a,b)/sqrt(N) up to phase; the character norm N gives singular values sqrt(N)|A(a,b)|, including zeros. Expanding e_3(x+a)+e_3(x) gives off-diagonal quadratic coefficients t+a_i+a_j, t=|a| mod 2. When t=0 the polar image has dimension two except when a is zero or all ones; the latter case is even-weight only for even n. For t=1 the kernel condition is x=s(1+a)+u1 with s=1·x and u=a·x: consistency forces s=u for odd n, and leaves two independent parameters for even n. Thus the ranks for odd shifts are n-1 and n-2, respectively. Squaring the Walsh transform leaves a radical character sum: its squared modulus is either zero or N times the radical size, so Parseval gives exactly 2^r coefficients of modulus 2^(n-r/2). Counting the N/2 odd shifts and the two types of even shifts gives the three stated multiplicities, including the even exceptional all-ones shift. The levels are distinct for n>=5. Their extrema give the stated positive-subspace condition number and the rank densities follow by division by N^2. This does not assert nonlinear phase-retrieval injectivity. The frozen checker and numeric verification notes were inspected, not rerun; the all-size argument does not depend on them.

## originality

FAIL

Chen–Yan–Zhou already analyze the identical complete three-uniform state's normalized Pauli coefficients by translation parity, not only its global moments. Their Appendix F.1 Eqs. (108)–(110) give the even-shift magnitudes and counts directly. Their Eqs. (106)–(107) give a fourth moment and a first absolute moment for each odd shift. Together with unit per-shift Parseval these saturate Hölder, forcing the precise odd-shift nonzero magnitude and multiplicity. Consequently the whole ambiguity histogram is mechanically recoverable from the prior appendix. The usual Weyl-to-lifting diagonalization rescales it; the compact polar-rank proof is another derivation, not a distinct claimed spectrum.

## value

FAIL

The spectrum, null-space dimension and positive condition number are natural quantities for this lifted operator. However, the exact magnitude census follows from the prior per-shift formulas by one equality case, and putting it on the singular-value scale requires only the standard Weyl diagonalization. The submission establishes no other distinct exact invariant or meaningful extension; the alternative proof does not rescue the covered finding.

The dated certificate retains the supplied scientific assessment, sources and limitations.
