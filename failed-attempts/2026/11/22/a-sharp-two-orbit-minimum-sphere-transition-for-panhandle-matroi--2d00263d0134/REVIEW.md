# Independent mathematical audit

## correctness

PASS

The indicators all have squared norm r; each is a vertex (a 0/1 vector cannot be a nontrivial convex combination of different 0/1 vectors). For the minimum-norm point c of their hull, ⟨c,v−c⟩≥0 for every vertex v. Any convex representation of c therefore has positive coefficients only on vertices with equality. Those are precisely the contacts at squared distance r−||c||²; their weighted squared distances to any candidate y average to r−||c||²+||y−c||², proving unique optimality. For handle mass h the within-block means minimize the squared norm and attain (r−h)²/p+h²/t; they are in the hull for every 0≤h≤1 by interpolation between the two orbit barycenters. This strictly convex quadratic has unconstrained minimum at rt/(p+t), so h=min(rt/(p+t),1). This gives both stated centers, the two radii, and the squared-radius deficit by completing the square. In the capped regime, the inner products of the two types differ by (r−1)/p−1/t, giving the exact positive squared-distance clearance. At equality c is uniform and both orbits contact, including the orbit not needed to support c. Orbit sizes and parameter scope are correct. The supplement contains four off-center probes and one centered probe, rather than five off-center probes as described; this has no bearing on the analytic theorem. The supplement was inspected read-only.

## originality

FAIL

The exact formula and contact criterion are a direct specialization of the published constant-norm minimum-enclosing-ball dual combined with the published two-block inequality description of panhandle polytopes. This is demonstrated broader coverage by a mechanical scalar constrained quadratic calculation, not a claim that an earlier panhandle paper printed the formula for p>r.

## value

FAIL

The canonical Euclidean invariant is a legitimate question, and the contact pattern is stated accurately, but its computation is a routine equal-norm-ball conversion and a one-constraint scalar projection. The sharp threshold, departures, and deficit are direct consequences of the already available geometry and constraints; the frozen record adds no independent obstruction, mechanism, or unknown exact invariant beyond that calculation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
