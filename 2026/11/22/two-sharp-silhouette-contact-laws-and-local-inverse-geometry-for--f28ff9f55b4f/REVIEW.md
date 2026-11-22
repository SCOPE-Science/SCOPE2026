# Review — Two sharp silhouette-contact laws and local inverse geometry for circular frusta

## Correctness — PASS

The exact projected hull has an affine reduction to two translated disks. Direct area integration and the support function/Cauchy perimeter integral produce complete angular formulas, including the contact boundary and both endpoint limits. Taylor expansion gives two positive sharp \(3/2\)-power coefficients; elementary inversion recovers every dimension. The standalone checker passed 156 independently constructed finite tests. Those numerical checks do not substitute for the analytic proof.

## Originality — PASS (provisional historical priority)

The March 31, 2011 truncated-cone silhouette discussion **already contains the qualitative projected-ellipse/tangent criterion** and is credited for that. Vickers and Brown's 2001 full accessible paper treats other solids' planar projected area/perimeter, including right cones and cylinders, but not proper frusta. Full publicly available results d2f25b7ec7c9 and 8de6145eb223 treat frustum **line widths**, while 9a216c99bcc1 treats a tapered family of mean widths. They do not give the paired sharp planar area/perimeter contact constants or the stated local inverse. An older equivalent under an alternate formulation may exist; no general priority guarantee is claimed. The specific statement-versus-prior comparisons and source inspections appear in AUDIT.json.

## Value — PASS

Two exact nonanalytic silhouettes at the same physically meaningful first-contact angle characterize a natural geometric change, and the perimeter coefficient together with the first-contact angle and axial silhouette length gives a sharp 3-parameter reconstruction. This is a full-family inverse law rather than an arbitrary parameter sample; no robustness to noisy estimates is claimed.

## Scientific limitations

The analysis assumes exact Euclidean orthographic projections, positive unequal coaxial circular rims, and fixed height. The \(3/2\)-power error bounds are pointwise in the geometry. The finite checker is a consistency check, not proof or external validation. Independent mathematical and comprehensive historical-priority reviews remain outstanding.

Self-review: passed. Independent audit: not yet performed.
