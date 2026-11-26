# Independent mathematical audit

## correctness

PASS

Dihedral averaging preserves the feasible symmetric stochastic matrices and lowers the convex norm, so optimizing the two edge weights suffices for the global value. Each Fourier block is (1-beta)I plus entries -2 alpha d on the rim diagonal and beta off-diagonal. Its larger nonstationary eigenvalue at d=delta strictly decreases with beta for alpha>0, so beta=1-2alpha minimizes this lower bound. On that boundary lambda_+(d) decreases and -lambda_-(d) is bounded by sqrt(beta^2+4 alpha^2)=lambda_+(2); this also bounds |1-2beta| since the squared difference is 4 alpha(1-2alpha). The bound is attained for every boundary pair, including the endpoints. For D=4+delta^2, the scalar norm squared is D(alpha-2/D)^2+delta^2/D. Its second derivative is positive; the derivative of the full objective runs from -delta to 2 at the two endpoints. The proposed alpha solves the unsquared stationary equation with norm sqrt(delta)/2, so both weights and the objective are correct, and only uniqueness within the invariant family is asserted. This check applies to the triangle and both parities (only d<=2 is needed). The m=4 substitution gives (3/10,2/5,4/5); expanding delta=2 sin^2(pi/m) yields the stated asymptotics. The uploaded program and frozen numerical output were read, not executed; the universal certificate is RESULT.md lines 35–107, not the sampled spectral tests.

## originality

FAIL

A distinct indexed sunlet result states the same unrestricted symmetric-chain optimum, edge weights, zero rim holds at the displayed solution, and dihedral uniqueness for every size. Its radicals are identical after rationalization. The explicit asymptotic terms are obtained by ordinary Taylor expansion of the same formulas and do not supply a distinct claim. This is demonstrable coverage, not an inference about authorship or priority from dates.

## value

FAIL

Fastest mixing on a cycle with individual pendants is a natural exact optimization problem, and an all-size solution is intrinsically useful. However the submitted contribution reproduces that known solution; the worked example and routine Taylor terms do not give an independently useful new invariant or optimizer classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
