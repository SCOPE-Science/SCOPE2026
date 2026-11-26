# Independent mathematical audit

## correctness

PASS

Reconstructed the continuous optimization, including equality cases. In the convex covering strip the shortest path is a straight segment to a lift; the closest representatives of the two parities suffice. For u,z nonnegative the rising and falling squared distances cross at t=C/2+2uz/C, so the unique longitudinal maximizer is this point clipped at C. Before 4uz=C² the maximized value increases strictly with z; beyond it the value C²+(u−z)² is strictly convex in z. Thus the only transverse candidates are H/2 and C²/(4u) when admissible; their comparison has sign equal to the sign of 2u−H/2−C²/(4u) for interior minus boundary. At u=α the candidates coalesce, at β they are distinct and both attain the maximum. Since α<C/2<β<H/2 for H>C, monotonicity reduces the global minimum to 0 or β, and equality is 3H(H+sqrt(H²+8C²))=28C², giving H/C=7/sqrt(15), β=sqrt(15)C/6 and radius 4C/sqrt(15). The only maxima for H>C are α and H/2 with equal value, and t=C reflects the partner's sign at the same longitude; for H≤C the boundary offset is (C²+H²)/(2C), including the seam case H=C. Solving the diameter equation for H≥C gives the asserted branch. Read verify.py: it shares the longitudinal reduction and checks a finite transverse mesh, not equality loci or quantifiers; the exact derivation above is the certificate. In proof step 1, 'a path lifts to a straight segment' is read as the minimizing representative, not a statement about arbitrary lifted paths.

## originality

PASS

Best-of-knowledge assessment is for the pointed profile and complete equality loci, especially the coexistence of two center circles, not the known lift kernel or scalar invariants obtainable from the random-pair law. The compared related theorems do not supply the pointed extremum. The underlying constrained optimization is elementary and derivative-priority risk remains.

## value

PASS

The minimal intrinsic enclosing radius is a natural invariant not visible in boundary-only measurements. The analytic classification identifies two different transitions: the type of a farthest point and the global change from core to a separated noncore center, with both loci at the critical aspect ratio. Exact ties and maximizing locations add information beyond a scalar support endpoint.

The dated certificate retains the supplied scientific assessment, sources and limitations.
