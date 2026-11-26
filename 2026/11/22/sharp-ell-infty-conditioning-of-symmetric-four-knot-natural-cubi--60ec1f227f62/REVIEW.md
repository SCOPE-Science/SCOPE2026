# Independent mathematical audit

## correctness

PASS

Reconstructed the interpolant independently with first-derivative cubic Hermite data. If Delta_j are the raw successive data differences, natural ends give m_0=(3 Delta_0-m_1)/2 and m_3=(3 Delta_2-m_2)/2. Matching second derivatives at the two inner knots gives diagonal 3r+4 and off-diagonals 2 in the system for m_1,m_2, with right sides 3r Delta_0+6 Delta_1/r and 3r Delta_2+6 Delta_1/r. This nonsingular system yields all cardinal functions; the replay /workspace/replay/03_hermite.py checks natural conditions, matching, reflection, and both Lebesgue-function identities, and reproduces the optimum numerics. For all r>0, the sole negative cardinal on the open left cell is ell_2; on the open middle cell only the two endpoint cardinals are negative. The factored cardinals verify these signs on the entire cell, with endpoint zeros allowed. Since they sum to one, the excess over one is 2(r+1)t(1-t^2)/(r(3r+2)) on the left and 6r^2 t(1-t)/(3r+2) in the middle, with respective maxima at 1/sqrt(3) and 1/2. The right cell is reflected. The outer maximum is strictly decreasing from infinity to one; the middle maximum strictly increases from one to infinity, so their unique crossing solves the claimed cubic and is the unique minimizer. Sign choices in the nodal cube attain the norm; translating and rescaling [0,1] to [-1,1] using reproduction of constants proves the range-escape claim in both directions. The comparison to equal spacing is strict by uniqueness and the crossing not being at one. Frozen source scripts were inspected, not run.

## originality

PASS

The norm/largest cardinal row-sum principle and range translation are standard; the supported distinct result is the exact two-cell competition for this natural-spline family and its unique optimizer. The closest exact Resultary finding studies the same family with a different norm and gives a different optimum.

## value

PASS

The meaningful result is not the small percentage improvement alone. Exact signed-cell competition explains why equal gaps are not optimal even among reflected-symmetric four-site meshes and why the variation-optimal mesh is unsuitable as a proxy for minimax nodal noise. It gives a sharp condition number and range escape for every positive gap ratio, including near-degenerate meshes. This is an exact design result for the stated natural interpolation operator, not a claim about asymmetric or larger meshes.

The dated certificate retains the supplied scientific assessment, sources and limitations.
