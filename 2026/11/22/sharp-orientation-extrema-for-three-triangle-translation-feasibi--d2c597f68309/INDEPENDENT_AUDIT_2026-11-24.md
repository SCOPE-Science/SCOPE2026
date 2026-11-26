# Independent mathematical audit

## correctness

PASS

For x in K0−K1 the y-section is (K0 ∩ (K1+x))−K2. Its area is the area of the intersection plus the mixed-area term plus |K2|. Integrating produces |K0||K1| and |K2||K0−K1| for the first and last terms. For polygons and almost every x the intersection boundary consists of surviving edge portions of the two originals: exceptional collinear/coincident edges and degenerate intersections occur on a null set. For each edge point the x-measure of survival is the area of the other polygon, proving the remaining mixed-area terms. Hausdorff continuity via the Minkowski-sum description extends the identity, although the triangle claim only needs polygons. The three equilateral normals give 2V2(T,−RφT)=4A cos δ. For the angular minimum, circular gaps sum to 2π/3; on the cell where each is at most π/3 the objective is strictly concave and the gap vertices are permutations of (0,π/3,π/3). In a long-gap cell the other two gaps p,q give a strictly concave combination of cos p, cos q and cos(p+q) on p+q≤π/3; its vertices give the same minimizing pattern or the strictly larger aligned value. The singleton scale is exactly the coefficient of the coincident pair, so it must be minimal, with all possible ties. Positive weights force full alignment for the maximum. Continuity on the connected angle torus gives every value between the endpoints. Independent projected-product hull checks (python /workspace/independent_checks.py 1) corroborate both endpoints, including alternative tied smallest scales; these are diagnostics, not the analytic proof. No uploaded verifier was executed.

## originality

PASS

Best-of-knowledge pass on the distinct independently scaled and oriented equilateral profile with the weighted sharp minimum and complete equality classification. Neither the equal coincident simplex bound nor the general existence of a mixed-volume polynomial is claimed as a new theorem here. Priority of the general planar identity remains unresolved; direct retrieval failures do not count as evidence against overlap.

## value

PASS

The 4D feasibility volume measures robustness to relative translations, which a peak overlap does not. The sharp minimum detects a scale-order effect not apparent from equal-body bounds: making every pair as far apart as possible is not optimal; two align and the smallest body is singled out. The exact all-scale range and equality pattern provide a structural benchmark for more general translative-intersection volume problems.

The dated certificate retains the supplied scientific assessment, sources and limitations.
