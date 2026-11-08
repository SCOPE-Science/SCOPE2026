# Self-review

## Correctness — PASS
The Zak normalization is explicit, and the degree-three spline's knot pieces agree at each boundary. For parameters \(4/7\le\lambda\le1\), the exact Bernstein certificate checks two inequalities on every rational knot cell. Their consequences exclude all interior and right-boundary zeros with nonzero frequency below one-half. A nonnegative sinc-to-the-fourth Poisson representation excludes left-boundary zeros, and direct positivity excludes zero-frequency zeros. The published midpoint-frequency formula and the even-spline symmetries complete the proof and show the sharp subthreshold continuum. The checker was executed with exact SymPy rational arithmetic and returned the advertised 8 cells, 10 triangles, 200 coefficients, 39 exact zeros, and 42 positive vertex assertions. The certificate is an exhaustive continuum-polynomial argument, not finite sampling.

## Originality — PASS relative to inspected evidence
Hasannasab–Lemvig, arXiv:2609.13116v1, is the closest primary source. Its Proposition 4.3 provides only the one-dimensional \(\nu=1/2\) slice for the order-four spline; its complete higher-order zero-set theorem assumes scale at least one. The new result proves the nonvanishing of all remaining two-dimensional points for \(4/7\le\lambda<1\). Earlier Lemvig–Nielsen and Gröchenig frame obstruction results do not imply this precise two-variable conclusion. A previously unindexed equivalent result remains possible; no claim of universal publication priority is made.

## Value — PASS
The threshold is the first sharp transition for order-four cubic spline uniqueness on a full nontrivial subunit interval. The previously known below-threshold horizontal obstruction does not solve the difficult converse, which now has an explicit strict positivity certificate. The classification specifies a motivated natural zero-set invariant over a continuum of parameters, not a finite numerical curiosity.

## Limitations
No assertion about smaller scales, higher spline orders, noise stability, or a full Gabor-frame set. The midpoint line uses a previously published identity. Independent scientific audit has not taken place.

Self-review: passed. Independent audit: not yet performed.
