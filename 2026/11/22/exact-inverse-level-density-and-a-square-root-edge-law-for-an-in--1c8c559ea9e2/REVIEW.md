# Independent mathematical audit

## correctness

PASS

RESULT.md lines 4–27 and 29–60 concern distinct roots on the entire real input line, at fixed A, shift and level. Irrationality gives a dense torus orbit, while simultaneous attainment of the two same-sign sine extrema would force a rational frequency ratio; continuity gives the open image. For the proof's crossing-flux step, the needed control near tangencies can be verified by short-cell averaging: choose a small length h such that translation by h(α,β) is ergodic (exclude countably many lengths). The first, second and third time derivatives of sin(θ+αt)+sin(ψ+βt) cannot all vanish anywhere: the first and third force both cosines to vanish, and the second is then nonzero since α≠β. Compactness and Rolle therefore bound the distinct roots in every sufficiently short half-open cell by three, uniformly in the initial phases. The count as a function of initial phases is continuous off the endpoint-level curves and the backward sweeps of the finitely many tangent points; all these sets have area zero. Tangency finiteness follows from α²(1−s²)=β²(1−(c−s)²), a nonzero quadratic. Equidistribution applies to this bounded Riemann-integrable cell count, and the two incomplete cells contribute O(1). By the area formula on (p,t)↦p−t(α,β), p on the regular level and 0≤t<h, the mean cell count is h times the level flux with Jacobian |(α,β)·n(p)| on the curve. Thus multiple and exact tangent roots cause no unaccounted density. Averaging the four cosine sign pairs gives the maximum stated in the record; multiplying by the two arcsine densities gives the factor π^{-2}. At c=0 the sum-to-product factorization has two disjoint progressions, whose densities sum to max(α,β)/π. At c=2−δ, setting s=1−δx in the exact integral reduces the coefficient after division by √δ to (π²√2)^{-1} times the integral over [0,1] of max{α/√(1−x),β/√x}; dominated convergence applies and the two terms switch at x=β²/(α²+β²), giving integral 2√(α²+β²). Reflection gives the opposite edge. The frozen VERIFICATION.md and check.py were inspected, not executed: sign changes on a mesh can miss roots, and the numerical test for one frequency pair is not the proof of the limit.

## originality

PASS

The supported distinct claim is the explicit level-resolved density and edge constant for the specified incommensurate sine sum. The underlying equidistribution, absolute flux and local extrema methods are standard; the same-map earlier fixed-point coefficient is materially related and credited.

## value

PASS

For a published nonlinear map the exact density distinguishes how attainable targets vary in inverse abundance, going beyond both dense-range existence and the earlier level-integrated fixed-point coefficient. In particular the central density and the explicit square-root depletion at the formal endpoints give quantitative information unavailable from the aggregate. The value is for unrestricted one-step inversion, not for bounded backward histories, stability or chaos claims.

The dated certificate retains the supplied scientific assessment, sources and limitations.
