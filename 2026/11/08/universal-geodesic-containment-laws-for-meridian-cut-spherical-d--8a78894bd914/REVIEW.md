# Self-review

## Correctness — PASS

The normalized affine interpolation of two nonantipodal points on the round sphere has the same trace as the minimizing great-circle arc. Projection to a fixed coordinate plane gives a segment joining two nonopposite planar rays; its azimuth traces their shorter circular arc independently of latitude or dimension. For independent uniform azimuths on E, different components never survive and a pair in one component of angular length l survives precisely when its coordinate gap does not exceed pi. The two excluded triangular corners of the parameter square have total area (l-pi)_+^2. Summing with weights (l/theta)^2 gives the exact formula. The function f(l)=l^2-(l-pi)_+^2 is convex and has f(l)/l strictly increasing on (0,2pi]; Jensen proves the unique k-equal lower optimizer and strict superadditivity the unattained upper supremum. The single-meridian case is l=theta=2pi and yields 3/4; equal k-component cuts yield 1/k. Exceptional antipodal, opposite-azimuth, and axial points have probability zero under the stated measures. The standalone checker directly interpolates sampled sphere points and tests 225000 cases in dimensions 2,3,5,6, with agreement at tolerance 0.013.

## Originality — PASS (historical priority provisional)

Prior own findings on latitude-defined spherical caps and equatorial zones concern different domain geometries and have no implication for arbitrary finite unions of meridian sectors, especially zero-area cuts and sharp component-count extremizers. Published work on spherical width and lunes establishes convex-geometric background but its inspected materials do not derive this random-geodesic survival law. Targeted published-finding corpus queries found no equivalent or stronger coverage among returned records, but indexed-search absence is not a guarantee of historical priority. Meridian-convexity of individual sectors narrower than pi is elementary and is not claimed as novel; the novelty claim is the full classification and sharp fragmentation/measure-zero-cut phenomena.

The closest inspected sources were Lassak's spherical convexity/width treatment (2013; DOI 10.1007/s00010-013-0237-3) and Lassak–Musielak's study of reduced spherical convex bodies (2016; arXiv:1607.00132). Earlier latitude-cap and equatorial-zone probability results address distinct spherical regions, without implications for this azimuthal classification.

## Mathematical value — PASS

The problem quantifies a geometric connectivity statistic that depends on whether a random shortest ambient geodesic stays within a domain, rather than merely whether endpoints lie inside it. Deleted zero-area meridians alter this probability discontinuously, giving an instructive contrast with area-invariant statistics; the exact all-dimensional classification makes this nonlocal effect measurable. The best/worst arrangement for a fixed angular budget and number of components is solved sharply, including uniqueness and the unattained supremum, and the result applies to all sphere dimensions and latitude sampling laws with uniform azimuth. This is a complete structural family, not a single numerical example or a routine restatement of spherical convexity.

## Risks and limitations

Specialized unindexed probability literature may contain an equivalent result, and independent historical review remains needed. The theorem concerns ambient round-sphere geodesics and angular unions; there is no assertion for arbitrary spherical subsets or nonuniform angular sampling. Numerical trials support but do not establish infinite-dimensional validity.

Self-review: passed. Independent audit: not yet performed.
