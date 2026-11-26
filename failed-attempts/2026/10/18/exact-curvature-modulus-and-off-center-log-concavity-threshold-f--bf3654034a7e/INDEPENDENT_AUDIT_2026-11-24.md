# Independent mathematical audit

## correctness

PASS

RESULT.md lines 41–99 gives a correct all-parameter proof. Factoring out the centered Gaussian leaves c+cosh(su), with u=y/σ. The potential curvature is σ⁻²[1−s²R_c(z)] for z=cosh(su)≥1 and R_c(z)=(1+cz)/(c+z)^2. R_c' has numerator c²−cz−2, so the unique maximizer in z is 1 for c≤2 and c−2/c for c>2. Substitution verifies both branches and the two off-center minimizing points. Solving s²M(c)≤1 includes the c=2 junction and excludes all finite c at s=2. At s²=3,c=2 the rescaled log curvature is −(z−1)^2/(2+z)^2, giving the claimed quartic contact. For fixed s≥2 and c>sinh(s²) the log derivative is negative on the positive half-line (bound sinh(su)/u on 0<u≤s and use s≤u beyond it); TV is at most 1−w. Independent posterior-variance calculations at 180 deterministic points and four extremizer evaluations gave worst absolute discrepancies 7.77e−16 and 2.22e−16. These corroborate the symbolic proof; the frozen verifier was inspected, not executed.

## originality

FAIL

A distinct indexed record contains the same exact global extremum, phase boundary, optimizer bifurcation and unimodal/non-log-concave phenomenon in equivalent coordinates. This is demonstrated coverage, not a claim about who obtained the result first. The contamination limit and quartic junction do not survive as substantial distinct results: both follow directly from the identical scalar curvature and density formulas.

## value

FAIL

The sharp phase diagram is a useful classification in itself, but the frozen record recomputes the already indexed exact scalar invariant under a reciprocal change of parameter. The elementary mixing bound and quartic Taylor expansion add no independently useful mathematical gap after that comparison; the supplied evidence does not support a valuable distinct repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
