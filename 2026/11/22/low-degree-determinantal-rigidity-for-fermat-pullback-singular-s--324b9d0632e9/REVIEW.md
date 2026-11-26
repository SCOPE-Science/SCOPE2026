# Independent mathematical audit

## correctness

PASS

For each A in coefficient degree r, the chain rule turns its relation into a first syzygy with coefficients q_i=A·∇g_i among g_i^{m−1}. The powers are a regular sequence, so all q_i are in their Koszul ideal of initial degree (m−1)a; the cutoff r≤(m−2)a gives deg q_i≤(m−1)a−1, including the endpoint. Then J A^t=0. Its fraction-field kernel is one-dimensional by the nonzero maximal minors, and the gcd-one hypothesis forces the multiple of the cofactor vector to be a polynomial (a prime of a reduced denominator would divide every minor). The converse is the cofactor identity. This gives the claimed homogeneous dimensions and one-dimensional minimum degree since 3a−3 is in range. Separately, the map to value and three tangent derivatives of a form at a fixed projective point is surjective (the homogeneous derivative matrix is equivalent to that jet by Euler's formula in a local chart). Rank ≤2 in the resulting 3×4 full matrix space has codimension two, so the generic projective rank-drop locus has dimension at most one. At a nonbase singularity the nonzero values lie on the smooth punctured Fermat cone in value space and the three derivatives impose three further independent conditions. The bad incidence has codimension at least one after projection and closure. At the transverse base the three local functions are coordinates, giving a^3 distinct singularities with gradient colength (m−1)^3 and F in its gradient ideal. A repeated component or the intersection of two surface components in P^3 would give a positive-dimensional singular locus. As an independent consistency check, g_i=x_{i−1}^a−x_3^a for i=1,2,3 gives minors proportional to the products of all but one x_j^{a−1}, a transverse base of a^3 points, and no off-base singularity: in the affine chart a critical point has each x_j zero or an a-th root of unity and F is nonzero unless all are roots; at infinity the homogeneous partials in x_0,x_1,x_2 cannot simultaneously vanish. The theorem rests on the proof, not execution of the inspected SymPy/modular illustration.

## originality

PASS

The distinct finding is the complete initial graded module for regular three-form Fermat pullbacks with primitive minors, not the generic minimum-degree equality, generic first-jet arguments or local weighted-homogeneous colength. The strongest checked analog is a full syzygy theorem for two-form plane pencils; the general Arnold-exponent vanishing already implies the generic lower bound. Neither covers these all-triple componentwise graded spaces.

## value

PASS

This specifies a whole initial block of graded Jacobian data, of length growing with m, for a naturally composed family with controlled isolated singularities. It shows that these early relations all arise from one derivation tangent to the three inputs, information not given by the generic least-degree bound or local colength. It can serve as concrete input for studying the Jacobian algebra without promising a full resolution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
