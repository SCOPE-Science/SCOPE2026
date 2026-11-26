# Independent mathematical audit

## correctness

PASS

The simplex-volume determinant identity follows by writing the centered columns in terms of the n columns of vertex differences; the resulting n-by-n Gram factor has eigenvalues 1 (multiplicity n−1) and 1/(n+1). Trace AM–GM and the equality Gram matrix give exactly the inscribed regular simplices in the unit ball. Independently checked the cap ellipsoid comparison: its quadratic transverse-radius surplus vanishes at z=1 and z=−t and has leading coefficient 1−a²/b²=−2(1−nt)/((n−1)(1+t)); it is strictly positive in the intervening open interval when t<1/n. The affine images of the apex and base rim are the north pole and the latitude −1/n, with transverse radius sqrt(1−1/n²), so a centered regular base yields an attaining regular simplex. Transforming the volume back gives the first formula, and all attaining vertices must be on the contact set, which forces the claimed apex/base equality geometry. At t=1/n, nonnegative shifted heights w_i have sum squared equal to their sum of squares by the regular simplex frame identity, forcing exactly one nonzero height shift. For larger caps that regular simplex remains feasible and the full-ball equality case is both necessary and sufficient. The finite checker was inspected, not executed.

## originality

FAIL

The direct MathOverflow answer is only a prior lower bound, but the finding is a routine exact corollary of the earlier slab enclosing-ellipsoid theorem of Güler–Gürtuna combined with the classical maximum-simplex theorem in a ball. The earlier ellipsoid theorem literally includes a one-sided cap and already gives the same ellipsoid, boundary transition, and contact layers. The specialization gives base contact latitude −1/n after normalization, exactly the latitude of a regular simplex opposite its top vertex, so the standard volume bound is attained with the frozen equality geometry. This is established prior implication, not a conclusion from an inaccessible paper or a search snippet.

## value

FAIL

The solid-cap optimization is a well-motivated question, and the frozen exposition is useful. But as an exact-invariant contribution the result is determined mechanically by the prior explicit slab ellipsoid and its end contacts, affine invariance of the ball-simplex bound, and the already computed lower-bound construction. The threshold equality is an elementary regular-frame consequence; no independent unknown invariant or new regime survives in the frozen finding as stated.

The dated certificate retains the supplied scientific assessment, sources and limitations.
