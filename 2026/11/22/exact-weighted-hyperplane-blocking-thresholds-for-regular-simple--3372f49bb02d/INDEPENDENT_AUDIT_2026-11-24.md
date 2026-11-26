# Independent mathematical audit

## correctness

PASS

The Gram matrix of the normalized simplex vertices is (N/d) times projection onto the sum-zero subspace. Thus unit normals correspond bijectively to sum-zero profiles with squared norm N/d, and an open ball is avoided exactly when the magnitude of its normalized projection is at least lambda*b_i. In each sign partition the magnitudes divided by lambda have equal group totals and their given positive lower bounds. At a fixed feasible total, the water-filled vector y_i=max(b_i,c) uniquely minimizes squares: for any competitor z, sum y_i(z_i-y_i)=sum (y_i-c)(z_i-y_i)>=0, since y_i>c only at active lower bounds, and the remaining difference of squares is sum (z_i-y_i)^2. Both groups' optimum energies strictly increase with the common total (mass above the bounds can be removed to reach a lesser feasible total), so the minimizing total is the larger sum of bounds. Every avoiding normal therefore gives energy at least E_*, and an energy minimizer rescales to a unit normal avoiding exactly at lambda_* and hence also at lower scales. At equality both energy bounds must be equalities; uniqueness in each partition and reversal of the normal give the listed unoriented planes. In the equal-weight case the energy for sizes p>=q is pN/q and is uniquely minimized in size by balance. For (1,1,1,2) the distinct partition types give energies 12, 22 and 19/2. The maximum over unit u of min_i |<u,v_i/R>|/b_i is the same lambda_* and is continuous in positive b by compactness. The center-distance condition gives pairwise separation, and the neighborhood conclusion follows from this projection maximum and the strict bound on displacement; the equal-weight gap follows from floor(N/2)/ceil(N/2)<=1<N/2. Line 71 overstates a strict inequality at lambda_*: critical avoiding normals furnish counterexamples to that strict clause. The proof explicitly allows and uses the non-strict bound in lines 71–74, which follows from the projection maximum (or a limit from scales above lambda_*), so this error does not invalidate or change the finding.

## originality

PASS

The distinct claim is the exact arbitrary-weights threshold for a fixed regular-simplex arrangement and the classification of every critical profile. The balanced directions already present in classical regular-simplex width theory, spherical covering lower bounds, and the definition of nonconvexity points are prior ingredients, not the originality-bearing claim. The verdict is limited to available comparisons.

## value

PASS

The prescribed-obstacle incidence threshold is a natural inverse problem in convex geometry. Exact arbitrary-weight profiles give more than the standard balanced direction and show which radii become active; the example verifies that multiple distinct magnitudes really occur. The same threshold certifies an open nonconvexity-point region for a family of pairwise disjoint balls, a geometric use of the exact result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
