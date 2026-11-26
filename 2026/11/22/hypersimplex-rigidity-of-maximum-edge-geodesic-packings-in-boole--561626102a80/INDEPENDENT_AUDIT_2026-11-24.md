# Independent mathematical audit

## correctness

PASS

Independently reconstructed the equality case in RESULT.md §§1–5. For any fixed coordinate order and a uniform starting vertex, the edge sampled in each direction is uniform in that direction. Averaging gives the upper bound t·2^(d−1); a union of t directions attains it. At equality, for every order every antipodal path has weight t. In a square, compare both routes from 00 to 11 and append a common suffix of unused flips. Repeat from 10 to 01. For weights a,b at 00 and c,h on the corresponding perpendicular continuations, these comparisons give a+c=b+h and a+b=c+h, hence c=b and h=a. For d=2 the suffix is empty. The remaining coordinates of an i-edge can be changed one at a time across such squares, so every i-edge has the same c_i. Antipodal saturation gives sum c_i=t; conversely a geodesic uses each direction at most once and c_i≥0, proving feasibility. Integral t and the box bounds imply every vertex of the slice is zero-one: two fractional entries admit an opposite perturbation, and one alone cannot sum to an integer with the others. This gives exactly binom(d,t) integral maximizers, dimension d−1 for t<d by the interior point c_i=t/d, and a singleton for t=d. The frozen VERIFICATION.md records checks on Q₂, Q₃ and Q₄ (six optima at Q₄,t=2 and four at Q₄,t=3); the all-d result rests on the analytical argument, not a rerun or a formal certificate.

## originality

PASS

Pass for the all-dimension, all-capacity equality characterization and fractional face, not the classical maximum value or the specific integral census at d=4,t=2. In the inspected prior proofs a union of coordinate classes is a construction, not the conclusion of an equality analysis; no general classification or fractional face was established by the inspected matches.

## value

PASS

An equality classification answers which optima exist, not just how large they can be. More strongly it identifies the entire optimal face of the natural geodesic LP and shows that no new fractional extreme optimizer occurs. The result holds uniformly across dimensions and capacities and explains the fixed four-cube census.

The dated certificate retains the supplied scientific assessment, sources and limitations.
