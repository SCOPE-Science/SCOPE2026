# Independent mathematical audit

## correctness

PASS

Read all seven package blobs at their frozen Git snapshot and reconstructed the analytic theorem. For a genuine polygon vertex incident to normals theta_{i-1},theta_i, strictly inward directions form the open arc (theta_i+pi/2,theta_{i-1}+3pi/2), of length pi-(theta_i-theta_{i-1}) in (0,pi); edge-relative-interior illumination follows from the incident vertex arc condition. For equiangular normals with Delta=2pi/m, k=floor((m-1)/2), each open arc has length ell=pi-Delta, (k-1)Delta<ell<=kDelta, so no direction lies in more than k vertex arcs, including the even-side strict-endpoint case. Each cyclic block of k consecutive arcs has a nonempty open intersection; weight 1/k on one point from each of m blocks gives exactly m/k total mass and at least unit vertex coverage. For odd m=2q+1, deviations eta<Delta/4 enlarge each reference arc by <eta at each end; q+1 equispaced arc starts cannot fit inside the expanded length <qDelta, giving the lower bound. Midpoints of the q-reference-arc block intersections have margin Delta/4 from all block endpoints, so remain strictly incident to their q actual arcs, giving the matching upper bound. Finiteness and strict endpoints are respected, also at m=3,4. Independently written exact rational check evaluated 149 finite normal fans for 3<=m<=51 including 100 perturbed odd cases, with zero discrepancies. A separate rational example verified a strictly wider prior-covered odd fan. These finite computations do not substitute for the universal analytic proof.

## originality

FAIL

The full claim is already mathematically implied by published stronger or earlier results. Sriamorn (arXiv:2306.13517, 2023; 2024 Results in Mathematics), Lemma 3.1, proves I^q(P)=2q+1 for every convex (2q+1)-gon, q>=2, whenever each q consecutive exterior angles sum to less than pi. For every odd-sided normal fan in the submitted plateau, set Delta=2pi/(2q+1) and delta_j=theta_j-phi-jDelta. Then each q-angle sum is qDelta+delta_{j+q}-delta_j <qDelta+Delta/2=pi, hence Sriamorn directly yields a q-fold illumination by 2q+1 directions; weighting those directions by 1/q gives I*(P)<=(2q+1)/q. The complementary (q+1)-angle sum is >pi, so no direction can illuminate q+1 consecutive vertices, and the illuminated vertices of a fixed direction form a contiguous block. Thus each direction illuminates at most q vertices, giving I*(P)>=(2q+1)/q. The triangle q=1 is elementary. This argument actually applies on the larger open set defined by all q-consecutive exterior-angle sums <pi, not merely the submitted uniform normal-displacement ball. In the even-sided case, the published "Exact multiple illumination and parity rigidity for polygons with antipodal edge-normal fans" proves I*(P)=2r/(r-1) for ALL polygons with antipodal outward normals, including all equiangular 2r-gons with arbitrary lengths (and a broader non-equiangular family). Sriamorn Theorem 1.8 also already contains the exact regular-polygon multiple-illumination formula. The submitted combination is correct but mathematically covered; absence of its exact title or angular radius from older papers does not establish originality.

## value

PASS

Fractional illumination is a natural convex-geometric invariant measuring optimal weighted illumination of all boundary points. An exact parity-dependent all-m formula for a broad nonregular equiangular polygon family and an open angular stability domain are intrinsically mathematically worthwhile: they characterize sharp cover/packing behavior rather than an arbitrary tiny instance or routine numerical table. This value judgment is independent of priority. The actual formula and sufficient plateau are mathematically covered by the older/broader sources, so value does not rescue originality.

The dated certificate retains the supplied scientific assessment, sources and limitations.
