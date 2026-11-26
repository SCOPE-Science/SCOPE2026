# Independent mathematical audit

## correctness

PASS

The original proof of the three-distinct-side remainder was not correct as written: it asserted that every zero forces coincident samples. For a unit square, assign the points (0,0), (0.4,0), and (1,0) to the left, bottom, and right sides respectively. They are distinct and collinear. These endpoint zeros belong to the compact coordinate box and cannot just be deleted as null events before bounding its small-area neighborhoods. The complete corrected RESULT.md in /workspace/repairs/5 treats both types of zero. At a collision, linear independence of the incident directions and W!=V makes at least one coordinate derivative of signed double area nonzero. At a distinct-point zero the collinear samples must occupy the two endpoints and the interior of one side; an endpoint's assigned side is nonparallel to the line, so its derivative is nonzero. Finite boxes, a uniform local derivative bound, and Fubini give the claimed O_K(t) per distinct-side pattern. Nonadjacent singleton patterns also have O_K(t) volume since their supporting-line distance is bounded below. Independently splitting the adjacent-side product integral at the singleton-length cutoff gives the exact 4 ell_i t/sin(alpha) log(ell_i ell_j sin(alpha)/(2t)) + 4t^2/(ell_j sin(alpha)^2). Multiplying by three label allocations and dividing by P^3, followed by t=P^2 s, gives the coefficient. The zero atom comes only from all points sharing a side, up to null events. Equality in C>=24 requires all angles right, hence exactly four sides. The repaired mark calculation uses the retained Jacobian 4t db du dz/(u sin(alpha)); in log-gap, normalized position and area coordinates the rescaled density tends to the unit-cube density, and integrating s^(q-1) bounds the mass q>1 by O(1/log(1/s)). This proves the joint conditional limit and the pattern weights without changing the stated scope. VERIFICATION.md and check_small_area.py were inspected without execution; their statements and calculations do not require replacement, and none purports to certify the omitted geometric case by simulation. The original package is unmodified.

## originality

PASS

Reassessed the repaired theorem at unchanged scope. Three samples on a triangular host already have an exact law, and the corner-product mechanism on arbitrary polygonal hosts is already used for two-sample chord cuts. Neither covers the repaired result for three perimeter samples on a general m>=4 polygon, its distinct-side control and length-weighted leading coefficient, rectangle-only extremizer, and joint mark including the repeated-side location. These overlaps are credited in the corrected file.

## value

PASS

The surviving repaired claim quantifies a natural random-geometric degeneracy outside the exact triangular special case and separates the positive-area law from the atom. The explicit leading coefficient and rectangle-only equality classify the best shape up to aspect ratio in the natural perimeter normalization. The additional normalized location mark explains the geometric origin of rare triangles beyond the two-endpoint analogue. This remains useful without controlling degenerating polygon families or the full area distribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
