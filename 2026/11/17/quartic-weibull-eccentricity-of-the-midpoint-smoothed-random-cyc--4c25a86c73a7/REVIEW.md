# Scientific review

## Correctness — PASS

The principal-harmonic projection is justified by the exact midpoint-operator eigenvalues. The two complex Fourier coefficients have ellipse semiaxes equal to the sum and absolute difference of their magnitudes. A functional quantile-process limit and a uniform Taylor remainder give the second angular Fourier mode as the Itô integral \(G=\tfrac12\int_0^1e^{4\pi it}dW(t)\), with independent real and imaginary variances \(1/8\). The continuous-mapping theorem then yields the Rayleigh semiaxis-gap limit and the quartic-Weibull geometric-eccentricity limit, with all factors checked. Rotation-equivariance proves exact finite-sample major-axis-direction independence. Checks in `checker.py` passed. Numerical simulations do not substitute for the proof.

## Originality — PASS, subject to priority risk

The 2010 Elmachtoub–Van Loan paper and 2016 VandeBogert paper give deterministic Fourier/spectral envelope mechanisms; these are credited, not claimed as new. Kostadinov's 2016 article is especially close for its globally normalized complex representation, but accessible material confirms only the deterministic principal-harmonic envelope. The new point is a fully specified random experiment (uniform independent points sorted in cyclic order), its evaluated complex Gaussian fluctuation, the sharp \(n^{-1/4}\) eccentricity scaling and a quartic-Weibull law. published-finding corpus semantic comparisons to published circular quadrature, Fourier polygon approximations and ellipse sampling did not yield an equivalent or stronger probability theorem. The full text of the closest Kostadinov study was unavailable; this limits priority confidence and does not certify uniqueness.

## Value — PASS

A classical polygon-averaging construction leads to an ellipse for deterministic input, but the typical **shape** of that ellipse under natural arclength sampling had no explicit law in the inspected literature. The result identifies a nonstandard geometric exponent: semiaxis imbalance is order \(n^{-1/2}\) but geometric eccentricity is order \(n^{-1/4}\). The exact finite-\(n\) Haar direction law separates random orientation from shape and makes the limit interpretable for stochastic geometric smoothing. This is a natural distributional invariant, not an arbitrary special-point calculation.

## Sources and limitations

Elmachtoub–Van Loan (2010), DOI 10.1137/090746707, full PDF Sections 1 and 4 and conclusions examined; VandeBogert (2016), arXiv:1606.08888v1, full HTML Sections 1–8 examined; Kostadinov (2016), DOI 10.1007/s40819-016-0224-1, CUNY abstract inspected, full download inaccessible. Csörgő (1983) supplies classical uniform quantile weak approximation. The limits are distributional only. The spectral envelope is not a full ellipse Hausdorff limit of a fixed finite-vertex polygon, and no exchange of the two limits is asserted.

Self-review: passed. Independent audit: not yet performed.
