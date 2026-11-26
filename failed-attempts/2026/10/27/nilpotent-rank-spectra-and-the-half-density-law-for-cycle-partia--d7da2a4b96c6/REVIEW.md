# Independent mathematical audit

## correctness

PASS

Fixing one source and image leaves the two possible dihedral orientations. A second source fixes the orientation except at an antipode, and a third distinct source always fixes it. A restriction is nilpotent exactly when it omits some vertex from every ambient permutation cycle. This gives the stated rotation and reflection terms; remove 2n−1 surplus empty restrictions, one surplus restriction per nonidentity singleton map, and n(n−2)/2 for even n from bijections between distinct antipodal pairs. The rotation terms reach rank n−1 only at order n, with coefficient nφ(n); reflections cannot reach it for n≥3. At each nonantipodal distance, the 2n² rank-two maps lose 2n for equal domain and image and 2n for a fixed vertex in a distinct overlapping pair; the antipodal distance contributes n(n−2)/2. For density, orders d≤ceil(2 log₂ n) cost O(log² n) rotations, and the relative deficit 1−(1−2⁻ᵈ)^(n/d) for any larger order is at most 1/n. Reflections contribute at most n·3^(n/2); the duplicate correction and the denominator's departure from 2n·2ⁿ are O(n²). Independent enumeration of partial bijections directly by distance and iterated image gave all rank coefficients for n=3–7 without assuming dihedral extension.

## originality

FAIL

The earlier indexed rank-and-nilpotency-index finding explicitly states the same complete rank polynomial and top-rank count for every n≥4, with an index refinement. The new endpoint n=3 and the low-degree example are direct evaluations, and the density bound is a short tail estimate of that same polynomial at one using the known total size. No independently distinct contribution was established for the frozen claim.

## value

FAIL

The rank distribution is a natural invariant, but the frozen result adds only a triangle endpoint, extracted coefficients and a nonsharp density estimate by a standard bound on the known divisor sum. These do not supply an independently needed new count or asymptotic feature; the earlier result already gives the more informative joint census.

The dated certificate retains the supplied scientific assessment, sources and limitations.
