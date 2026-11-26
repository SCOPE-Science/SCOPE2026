# Independent mathematical audit

## correctness

PASS

At any x, the data-increment representation is a convex combination of the two constant vertices and three steps. For the Lobatto grid, the terminal step (x+1)(4x²−1)/6 has minimum −(10+7√7)/162 at x=(√7−2)/6; its other critical point has positive value and its maximum is 1. The middle-step defect is 7√21/54−1/2, strictly smaller. Unique minimization over vertices and x gives the unique lower data/location pair, and reflection with complementation gives the upper pair. Mixing either step with any strictly increasing admissible vector proves approachability. For the uniform grid the terminal step is (9/16)u(u²−4/9), u=x+1/3, with undershoot √3/27; the middle step is 1/2+[(13/9)x−x³]/(8/9), with minimum at −√39/9 and larger defect 13√39/108−1/2. Independent cardinal evaluation and derivative-root enumeration corroborated both grids. The exact argument, not floating-point comparisons, establishes strictness and uniqueness.

## originality

FAIL

A distinct indexed symmetric four-node record explicitly gives both exact constants on the same full interval and data simplex. Its general proof also implies the unique Lobatto extremizers. Coverage is demonstrated; same-day publication labels do not establish relative priority.

## value

FAIL

The monotone-data envelope is a meaningful shape diagnostic, but this submission supplies no independently useful unknown exact fact beyond the broader symmetric-grid result: the comparison is listed there, and the remaining witness and limit details are direct specializations of its proof. A useful underlying question does not make a covered specialization a separate contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
