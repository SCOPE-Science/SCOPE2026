# Independent mathematical audit

## correctness

PASS

PASS applies only to the complete corrected files under /workspace/repairs/4, not to the frozen prism classification. The frozen finding is false at n=4: the facet over the second-coordinate edge from 1 to i has its two caps rotated by π/2. A quadrilateral side would require a shared outward edge normal of the triangles, and there is none. More generally the caps have relative angle 2π/n, a symmetry only at n=3; otherwise their horizontal edge normals strictly alternate. This gives six triangular side faces and two triangular caps, with each vertex incident to four faces, giving the octahedral graph and face structure. The b=0 family has the same cap geometry after exchanging the coordinates. Independently, normalizing support to cos(π/n) constrains the three coefficients w_j=b+aω^j to the polar polygon W. For a pair of edge contacts with directed offset m, the remaining coefficient lies strictly inside W for 0<m<n/3: its modulus is 2cos(π/3+δ) with δ≥π/(3n), strictly below the inradius. It is outside for m>n/3 and is another W vertex at each allowed endpoint. Thus there is no five-vertex facet, all six-vertex facets are counted by n(1+1_{3|n}), and all other facets are tetrahedra. Complementary component planes give affine independence of the two-edge tetrahedra; counting starting edges and strict offsets gives 3n floor((n−1)/3). The same constraints express b+aμ_3⊂W, establishing the polar interpretation including zero-scale placements. The frozen checker counted contacts but did not test prism type. The new checker tests contact counts and the cap-face structure over 3≤n≤80; run python3 /workspace/repairs/4/verify_facets.py, with output in /workspace/checks/facets4_audit.out. It is numerical corroboration, not the all-n proof.

## originality

PASS

Assessed the repaired classification, not the false old prism count. The placement-polytope interpretation and the centered maximal-scale family when 3|n are credited to earlier work. The distinct surviving claim classifies all six-vertex facets by type and count and gives the exact two-edge tetrahedral count, including the nongeneric resonances. No broader theorem demonstrated to imply that claim was found; the finite bicyclic alias has residual access risk.

## value

PASS

The corrected result identifies exactly how symmetry creates nonsimplicial facets in a natural family of containment duals outside the general-position model; it distinguishes actual prisms from octahedra despite the same number of vertices. The exact number of two-edge tetrahedra quantifies a quadratic family of dual vertices representing two exact boundary-corner contacts. These are useful invariants of the full placement problem and are not supplied by a maximum-scale computation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
