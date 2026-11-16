# Scientific review

## Correctness — PASS

The claimed exact nine-by-nine determinant follows by unitary Fourier reduction on the three- and five-site rings, block elimination of azimuthal orders \(\pm2\), then \(\pm1\), and the three-height Vandermonde determinant for order zero. The displayed normalization produces the constant \(5189853515625/(1073741824\pi^9)\), checked against direct normalized complex harmonic determinants. Strict concavity of \(\log F\) on the two height-ordering chambers proves unique maximizers. The algebraic stationarity resultant has noninterior endpoint factors and the quadratic \(39x^2-11x-14\); exact rational bounds compare both chamber maxima. The standard-library checker passed 83 independently evaluated tests. Risks: numerical tests alone do not prove globality, but that is supplied by the analytic argument.

## Originality — PASS within inspected evidence

The closest 2014 and 2017 source papers use the same ring populations but optimize placement over equiangular candidates and/or order-wise matrix condition numbers, not the unrestricted global determinant. Three related published results treat two mirrored rings with angular offset only, exact-degree-two quadrupole conditioning, or one-ring exact-degree-four conditioning; their complete scientific statements do not imply this nine-column, three-ring, continuous-height optimum. Spherical-design determinant optimization is a differently constrained objective. A historical equivalent in unindexed interpolation/Fekete literature remains a priority risk; indexed search alone is not proof of novelty.

## Value — PASS

For the first nontrivial minimal \(1+3+5\) iso-latitude sampling grid, determinant is a natural information-volume invariant of full quadratic spherical-harmonic reconstruction. The closed factorization identifies all singular height collisions, all optimal shifts, an exact unique radical latitude choice and its nontrivial \(12.36\%\) determinant-square gain over the standard equiangular reference. This does not require a further downstream theorem and does not claim optimal worst-case conditioning.

## Closest literature and scientific limits

See the 2014 Khalid–Kennedy–McEwen scheme, 2017 Nafees et al. improvement, 2024 Haines regression design article, and 2026 An–Zhuang survey. The two-ring and one-ring results compared in the structured audit are mathematically distinct. Domain is a fixed south pole with two free regular ring heights, not arbitrary nine-point sampling. Independent review remains outstanding.

Self-review: passed. Independent audit: not yet performed.
