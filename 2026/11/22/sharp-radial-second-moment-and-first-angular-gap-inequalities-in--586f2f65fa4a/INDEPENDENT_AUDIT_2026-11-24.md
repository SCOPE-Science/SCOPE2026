# Independent mathematical audit

## correctness

PASS

The nonnegative frequency m has q radial polynomial coordinates with weight t^m(1-t)^alpha; the negative frequency -r has q-r with exponent r. Compression of multiplication by t has simple Jacobi-zero eigenvalues: dividing the degree-n orthogonal polynomial by t minus a zero gives the eigenpolynomial by orthogonality. Strict covariance with log t raises the Rayleigh quotient with the exponent (test the minimizer for the larger exponent). Strict consecutive-degree interlacing at exponent 1 handles even frequency -1, where monotonicity in the exponent alone would not give strictness; larger negative frequencies follow by the degree/exponent comparisons. The Christoffel numerator Q_(q+1)+Q_q changes sign between consecutive radial zeros. All ordered eigenvalues increase strictly with the exponent by min-max (strictness is uniform on the compact unit sphere at fixed block dimension). Thus the lowest exponent-one root lies before the second radial zero. For q=1 there are no negative blocks or higher radial roots. This puts exactly one simple ground state and one simple first excited state at the bottom. Testing these two eigenstates respectively proves sharpness and the spectral decomposition gives equality. Jacobi reflection and fixed-parameter Mehler-Heine place each smallest shifted zero at j_(beta,1)^2/(4 q^2) to leading order; their difference has the stated limit. An independent SciPy quadrature/compression diagnostic (/workspace/reproductions/frozen_diagnostics.py 1) passed 50 angular-block scenarios and ten hard-edge spot checks at q=256. Numerical checks are not the all-order argument. The frozen checker was inspected, not run. RESULT.md line 51 contains a malformed beta glyph; context and equations make the exponent unambiguous.

## originality

PASS

Best of current knowledge for the combined globally ordered first two simple levels and sharp stability theorem. The block representation, Gaussian-quadrature spectral identification, classical Jacobi comparisons and separate hard-edge formulas are antecedents or standard tools, not independently novel claims.

## value

PASS

The square-radius moment directly measures radial localization. The theorem distinguishes the radial minimizer from the unique first angular competitor on the full function space, supplying the exact coercivity and equality data that a per-frequency spectrum does not itself provide. The leading ground and stability scales hold for every fixed admissible weight; neither a uniform-in-alpha limit nor the ordering of the higher spectrum is asserted.

The dated certificate retains the supplied scientific assessment, sources and limitations.
