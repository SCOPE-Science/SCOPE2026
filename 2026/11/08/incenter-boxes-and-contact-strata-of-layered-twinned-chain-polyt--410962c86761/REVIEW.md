# Independent mathematical audit

## correctness

PASS

Since every antichain lies in one block, the polar factors into Q_m=Δ_m−Δ_m, where Δ_m is the simplex on 0 and the coordinate unit vectors. The candidates are 0, signed units and ordered differences. The origin is interior; a signed unit is exposed by a same-sign functional with a unique largest absolute coordinate, and e_a−e_b is exposed by the functional with 1 at a, −1 at b and 0 elsewhere. Thus the list of norms and vertices is exact. All product normals have squared norm at most H, and a pair of opposite farthest normals bounds every possible radius by 1/√H; the origin attains it. At this radius all farthest normals annihilate the center. Comparing normals that differ only by opposite singleton signs or opposite ordered differences gives exactly the indicated zero and block-constant coordinates. If j wide blocks use units, the worst dot product for that subset is the sum of the corresponding |t_i|. Its slack threshold f(j)=1−√(1−j/H) satisfies f(j)>j f(1) for j≥2 by strict convexity, with equality for j=0,1. Thus precisely the singleton bounds determine the center locus; exactly one-unit normals with matching signs can add contacts at an active coordinate. The product choices give both exact counts, and block indicators have mutually orthogonal lengths √m_i. With w=0 only the origin remains and all 2^s farthest facets touch it, including the interval k=m_1=1. These arguments are a universal verification from the polar inequalities in RESULT.md Steps 1–5. The reported 27 profiles, 7,210 test vertices and 121 corner counts were inspected in VERIFICATION.md and verification.py, not rerun. The separate reported 13-profile LP evidence was not needed or independently replayed.

## originality

PASS

The polar/facet list, free-sum structure, and direct consequences for radius and centered contacts are credited. The distinct result is the exact full optimal-center box in the fixed Euclidean metric and the classification and count of contacts at all its strata. The compared prior results do not establish the necessary singleton-reduction and no-extra-contact conclusions.

## value

PASS

The exact set of translated maximum-radius balls is a natural refinement of a single centered radius in canonical Euclidean coordinates. It has unbounded dimension across the family, edge lengths that retain the actual block sizes, and a complete active-coordinate rule for contact counts on every face. These distinctions are not captured by total face counts or the centered insphere alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
