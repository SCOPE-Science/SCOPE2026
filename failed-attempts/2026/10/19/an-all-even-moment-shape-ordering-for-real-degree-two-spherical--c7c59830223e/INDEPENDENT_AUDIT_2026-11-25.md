# Independent mathematical audit

## correctness

PASS

For a standard 3D Gaussian the independent angular direction is uniform and the radial factor for the degree-4m integrand is (4m+1)!!. Expanding the trace-zero determinant in the Gaussian transform gives (1−2s₂t²−8 det(A)t³)^(-1/2); the terms contributing to t^(2m) choose 2j cubic and m−3j quadratic factors. The m=1 normalization is 2s₂/15. At m=3 the resulting affine polynomial is (5625+54000u)/1001. Its higher-order analogues have a strictly positive linear term for every m≥3. The real-root discriminant is s₂³/2−27 det(A)²; equality at the two extremes characterizes zero determinant and a repeated eigenvalue, respectively, and the fixed-s₂ trace-zero spectral circle is connected. Harmonic degrees zero and one have only one real fixed-L² shape up to sign and rotation. Read checker.py and its recorded 368 exact checks; no frozen code was run. The proof holds for all stated m, not just the checked cases.

## originality

FAIL

The numerical-shadow literature already provides the exact all-order transform of this same spherical quadratic form, not just a Gaussian analogy. Substituting dimension three, Dirichlet parameters 1/2 and trace zero, then extracting even coefficients by the binomial theorem, gives the identical positive-coefficient polynomial, including its order of first variation. Standard cubic discriminant and compactness identify the range and equality cases. The claimed full ordering is a direct corollary of the older general moment formula with the elementary range restriction; no independent new claim survives.

## value

FAIL

The transition from fourth to sixth order is a natural question and the constants are convenient, but the proposed finding is a routine exact specialization of the older spherical quadratic-form moment generator: parity in a two-term binomial expansion and the cubic discriminant eliminate the comparison problem. There is no surviving nonmechanical invariant, new extremal principle, or extension beyond that coverage.

The dated certificate retains the supplied scientific assessment, sources and limitations.
