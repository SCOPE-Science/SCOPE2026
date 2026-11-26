# Independent mathematical audit

## correctness

PASS

For unit normal u, support is a sqrt(1-u_z²)+b sqrt(1-u_x²)+c sqrt(1-u_y²). Concavity in the three squared coordinates bounds the support below by the least of the axial supports, b+c. The two z-normal constraints bound every ball radius by b+c, and force maximal centers into z=0. For a fixed unit horizontal direction v and horizontal normal length ρ, h_K is the concave function aρ+b sqrt(1-ρ²v_x²)+c sqrt(1-ρ²v_y²) of ρ in [0,1]. Its chord between 0 and 1 yields h_K(u)-(b+c) ≥ ρ[h_K(v,0)-(b+c)]. Thus the horizontal support inequalities are necessary and sufficient even for balls tested against all spatial normals. Horizontally the inequality is t·v ≤ c|v_x|+b|v_y|+a-b-c, identifying planar disk dilation when a≥b+c and disk erosion otherwise. Erosion against the four rectangle sides gives half widths a-b and a-c, including ties. Strips and quarter circles give the area in the dilated phase. At the transition the slopes are both 4(b+c) and the one-sided second derivatives are 8 and 2π. The argument covers all positive weights after sorting. The frozen CHECK.py probes only finitely many normals and thresholds; it was inspected, not executed. Replay of the unrestricted check is by the chord inequality above and the half-plane support test in RESULT.md lines 40–63.

## originality

PASS

Pass the explicit weighted maximal-center locus and its additive shape/area transition, not the inradius, the coordinate-discotope model, erosion/dilation identities, or the planar parallel-area formula in isolation. The closest inspected statements address the same unweighted body and its boundary/fiber body, the same weighted body and its volume/balancing, or a different orthogonal disk hull. The essential bridge from a three-dimensional erosion to precisely the planar rectangle constraints is not supplied by those statements.

## value

PASS

This gives every permissible translation of a largest ball, not just contact directions or a radius. The full dimension/tie classification and the exact transition between rectangular and rounded loci make a concrete distinction for the geometry of inner parallel bodies of Minkowski sums. The value lies in the all-directions reduction and the resulting complete classification, not in differentiating Steiner's area formula alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
