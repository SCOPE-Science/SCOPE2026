# Independent mathematical audit

## correctness

PASS

The distinct centered-ball counts on the open path are 4,3,3,4, with no exterior padding. A selector preserves constants, hence on the edge quotient its induced l1 norm is the maximum absolute column sum; the standard coordinate columns are the edge responses to the three path steps. Exact enumeration reconstructed from distances over all 144 masks gave individual step maxima (3/2,2,3/2), and precisely (3,0,0,3) exceeds 11/6. To rule out that mask, full-ball optimality at each endpoint forces the opposite endpoint to be at least the global mean by comparison with the three-point ball; the interior singleton choices force each interior value to be at least that mean too. All then equal the mean, even allowing ties. On a nonconstant segment this mask cannot govern an open piece, and persistent ties give identical slopes; on a constant-in-space segment the output differences have zero variation. Integrating the piecewise slopes controls the nonlinear map for every admissible pair. The exact witness has outputs (18,26,25,24) and (37/2,26,26,74/3), giving output variation 11/6 for input variation 1. The witness is nonnegative as supplied (or strictly positive on adding a common constant). Replay: python3 /workspace/checks/frozen_exact.py 3. The submitted checker was read, not executed. The theorem is for nonnegative inputs and adjacent l1 variation, not general signed absolute-value input, uncentered balls, or other graphs.

## originality

PASS

The checked sources support a distinct sharp two-input l1 coefficient for the centered four-site open path. The exact same assignment entry does not count as an independent match. The closest works are distinguished by graph geometry, choice of seminorm, averaging rule, or one-input quantifier, as detailed below. This is not an exhaustive priority claim.

## value

PASS

The first non-star open path is a natural place to test sharp two-input BV sensitivity beyond complete and star geometries. The difference between the true 11/6 gain and the naively allowed derivative norm 2 isolates a meaningful issue: rowwise available averages need not be jointly active. Exact attainment makes this a useful benchmark for sharper finite-graph arguments.

The dated certificate retains the supplied scientific assessment, sources and limitations.
