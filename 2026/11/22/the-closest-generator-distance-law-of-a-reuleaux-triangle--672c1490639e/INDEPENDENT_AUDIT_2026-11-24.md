# Independent mathematical audit

## correctness

PASS

In polar coordinates about one vertex, bisecting the two unit directions to the other vertices, their dot products with the radius unit vector are cos(π/6±φ). Disk membership requires both dot products ≥r/2 and nearest-site membership requires both ≤1/(2r). For r>0 in the body the former gives |φ|≤Φ(r)<π/3; the greater dot product on that interval is at least √3/2, hence r≤R from the latter constraint (and the centroid attains R). Above 1/2 the latter inequality removes the band between π/6−α and π/6+α on each angular half; α(r₀)=π/12 and Φ(r₀)=π/4 give the unique disappearance of the outer intervals. The central interval persists to R. This gives the three nonnegative angular lengths. Three disjoint cells up to null ties and the polar Jacobian give the factor 3r/A, with A from the generator triangle and three circular segments; level sets have zero area. Direct differentiation gives H′=rΦ and Q′=rα, with H(0)=Q(1/2)=0. Matching primitives gives the stated CDF; its normalization follows from partitioning the entire body. Near 1/2, α=2√ε+O(ε^(3/2)), so the CDF correction is −8ε^(3/2)/A. At r₀, α′=r₀^(−3), Φ′=−r₀ and r₀²+r₀^(−2)=4, so the second derivative jump is 24/A. The small-r angle tends to 2π/3, and α′(R)=3 gives the stated quadratic upper-tail coefficient. Independent adaptive radial-cap quadrature from the disk and Voronoi constraints returned 0.9359080043314900 and 0.9693460623242492 at the two breakpoints (double precision, not a certified error bound); replay with Python 3 at /workspace/branches/bd6fa360-394e-47b4-b23e-e226f5200d00/independent_cdf_check.py. The frozen log and script were inspected, not rerun.

## originality

PASS

The closest inspected same-body result is centered at the centroid rather than taking the minimum over the three generating sites; the closest inspected nearest-vertex result is a different statistic on a different class of bodies. The exact three-branch law, including its two interior transitions, survives the bounded comparison.

## value

PASS

Nearest-generator distance is the natural radius for covering this constant-width body by three generator-centered disks. The exact coverage fractions and locations and orders of both changes in the radial law require resolving separate Voronoi intervals and their disappearance; neither the area nor a center-distance profile gives this information. The full law, not just a selected radius or numeric fit, is useful for area coverage or sampling comparisons in a standard geometry.

The dated certificate retains the supplied scientific assessment, sources and limitations.
