# Independent mathematical audit

## correctness

PASS

A rook distance is the sum of the coordinate mismatches. If the targets share a row, after excluding the endpoints a witness must lie in a target column outside that row; this gives condition 1 including empty columns. The same-column test gives condition 2. If both coordinates differ, the other corners of the target rectangle give equal distances and the two endpoints are forbidden. A witness has exactly one coordinate among the two target rows or columns, so its edge crosses the corresponding (2,2) root shore. The selected boundary is empty exactly when the shore is a union of spanning incidence components, including isolated roots. For the 4×4 lower bound, an isolate forces degree at least two at each of the three other roots on its side, already requiring six edges. Without isolates, at most five edges on eight roots force at least three components; orders three and four are forbidden by the same-side leaf or (2,2)-shore obstructions, and a component of order at least five would require at least nine roots in total. Two order-two components also form a forbidden shore. A six-vertex path of profile (3,3) plus an edge meets all conditions, proving sharpness. The separate direct-distance enumeration of all 65,536 subsets reproduced the size-6-through-16 coefficients 2016, 6912, 10872, 10960, 7960, 4368, 1820, 560, 120, 16, 1 and total 45,605, as well as the orbit sizes 96,192,576,576,576 and weak-only/both/total-only/neither counts 1168/864/1152/4824 among six-sets. The independent replay includes endpoints for weak 2-resolution but excludes both for total resolution.

## originality

PASS

The established notion is total resolution, not this new definition. The distinct claim is its rectangular-rook incidence characterization including the two local neighborhood conditions, together with the full 4×4 census. The closest same-family work instead allows endpoints under an additive weak-2 condition; the closest same-parameter cut formulation studied here uses triangular graphs and different shores. Neither supplies the claimed result.

## value

PASS

For a natural product family, the theorem replaces all metric witness comparisons by local incidence restrictions and a bounded-profile component obstruction. It yields a sharp small-square optimum and an exact benchmark by size and symmetry. The overlap counts resolve a concrete ambiguity at equal optimum: weak 2-resolution does not select the same candidates as a third-party landmark requirement.

The dated certificate retains the supplied scientific assessment, sources and limitations.
