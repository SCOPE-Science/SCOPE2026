# Scientific review: horocycle-triangle area limit

## Correctness

**PASS.** The exact upper-half-plane geodesic tangent angles and Gauss--Bonnet give formula (1). The independent \(\operatorname{Beta}(2,2)\)--uniform span-ratio representation follows from the full joint ordered-statistic Jacobian. The limiting cdf, tail constant \(24\), critical moment exponent \(1\), and mean correction \(24\log(L/2)-24\) follow by explicit integrals. The rare-event law has an exact conditional density that converges in \(L^1\), giving the stated total-variation assertion. A numerical checker independently recomputed areas using the hyperbolic cosine law and compared the mean expansion with quadrature and tested limiting marks with seeded sampling. Risks: the finite tests do not certify infinite claims, but all limiting steps have analytic domination or exact density arguments; the marked result is deliberately an iterated limit, not a simultaneous scaling theorem.

## Originality

**PASS, conditional on the inspected literature.** Bao--Chen (2014) prove deterministic vertex-coordinate area formulas; Beardon (2022) studies horocyclic circumcycle classification. The published volume-uniform expanding-hyperbolic-ball Pareto area-deficit result has a different radial/angular sampling mechanism, not three uniform finite-horocycle positions. The nearest accessible prior horocycle sampling statement concerns Steiner topology, not triangle area. No inspected statement implies the independent \(\operatorname{Beta}(2,2)\)--uniform limiting variable, its complete cdf, exact constant \(24\), logarithmic mean correction, and conditional marked law. Risks: mathematical literature search is not exhaustive; independent historical priority assessment remains necessary.

## Value

**PASS.** The ideal-triangle area \(\pi\) is the canonical hyperbolic upper boundary, and horocycles provide a geometrically natural family approaching it. The result explicitly links geometry to an inverse-gap distribution, proves a sharp non-integrability threshold, and quantifies a non-uniform-integrability effect: the typical scaled deficit has a limit yet the mean diverges logarithmically with an exact finite correction. The marked theorem identifies one rare short adjacent gap as the mechanism, including its location and relative scale. These are natural complete distributional and geometric invariants, not arbitrarily chosen finite slices.

## Closest literature and limitations

The closest geometric sources are Bao and Chen (2014, DOI 10.1155/2014/838497), Beardon (2022, DOI 10.1007/s00013-022-01761-x), and University of Glasgow horocycle geometry notes. The nearest probabilistic comparison is the public hyperbolic-ball Pareto area-deficit result (2026), whose volume-uniform sampling does not imply this fixed-horocycle limit. The result does not claim a uniform two-parameter \(L,z\) limit, rates, nonuniform sampling, higher dimensions, or definitive historical priority.

Self-review: passed. Independent audit: not yet performed.
