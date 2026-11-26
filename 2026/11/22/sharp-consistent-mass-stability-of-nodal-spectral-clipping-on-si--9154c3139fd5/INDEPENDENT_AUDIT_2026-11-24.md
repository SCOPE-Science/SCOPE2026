# Independent mathematical audit

## correctness

PASS

The affine simplex mass matrix is proportional to G=I+11^T on the n=d+1 nodes and has metric ratio κ=n+1. A nodal input/output difference pair (u,v) of the convex projection satisfies ||v||²≤<u,v>, so vv^T/<u,v> (or zero) is a positive contraction taking u to v. Orthogonal projections have G-norm at most (κ+1)/(2√κ) by the Wielandt angle estimate; the spectral-layer integral transfers this to contractions and the sum of element norms gives the mesh estimate. For exact attainment, the stated identity/zero blocks (even n) or the three rank-one directions plus cancelling blocks (odd n) give sum D_i h=nh/2. For the normalized constant mode e, z=2De−e is a unit mean-zero mode; δ=e/κ+z gives Dδ=(1+1/κ)(e+z)/2 and ratio (κ+1)/(2√κ). The rank-one perturbations commute with their nodal bases, so a sufficiently small finite perturbation realizes these actions by actual clipping, including after fixed-coordinate embedding for m>2. For the scalar selector with 1≤k≤n active nodes, eliminating inactive inputs by a Schur complement gives denominator metric I+11^T/(n−k+1) on the active coordinates and numerator metric I+11^T; the constant active direction gives squared factor (k+1)(n−k+1)/(n+1). The empty selector has norm zero, not one as the unqualified selector expression in the proof would suggest; it is immaterial to the maximum, attained by the balanced nonempty selector and realizable by finite scalar clipping differences. Positive lumped weights preserve nodewise nonexpansivity, with equality on interval-interior fields. All sharpness claims are universal over meshes, not assertions of sharpness on every mesh. These are analytic checks of the arbitrary-dimension proof and exact witnesses; the supplied diagnostic code was inspected, not executed.

## originality

PASS

The relevant antecedents cover nodal truncation, other metrics or the general metric-change inequality. The supported distinct combination is sharp finite realization by clipping in the consistent mass metric, with the exact different scalar constant where d is even. No covering statement was found in the inspected evidence; this is not a priority certificate.

## value

PASS

This gives the exact worst-case L² sensitivity of a natural nodal postprocessing operation, with explicit pairs showing the amplification is real despite Frobenius nonexpansivity at each node. The scalar/tensor parity difference identifies an amplification mechanism available only to matrix data in even dimensions. This is useful for choosing or analyzing consistent versus lumped norms without claiming PDE stability beyond the stated setting.

The dated certificate retains the supplied scientific assessment, sources and limitations.
