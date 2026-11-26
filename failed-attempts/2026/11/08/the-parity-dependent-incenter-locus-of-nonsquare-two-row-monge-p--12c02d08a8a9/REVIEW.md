# Independent mathematical audit

## correctness

PASS

For the sum-one Euclidean hyperplane each projected coordinate normal has norm alpha_m=sqrt(1-1/(2m)); adjacent Monge normals already lie in the translation space and have norm 2. The polytope is full dimensional there (positive entries with small strictly decreasing row differences suffice), and nonadjacent inequalities telescope. Thus radius r requires entries at least alpha_m r and successive row-difference gaps at least 2r. With d_j=b_j-a_j, the excess entry mass in column j is at least |d_j|, with equality exactly when one entry is at its lower bound. Pairing j with m+1-j gives |d_j|+|d_{m+1-j}| >= 2r(m+1-2j); summing gives r floor(m^2/2), with an additional zero middle term in the odd equality case. This proves the radius bound, attained by the displayed construction. Equality in the outermost pair forces all successive gaps to equal 2r; either the odd middle difference is zero or the even innermost pair has opposite weak signs. This is exactly theta=0 or -1<=theta<=1 respectively. One coordinate per column varies at absolute speed rho_m in the even segment, proving the length 2rho_m sqrt(m). The facet system is irredundant; all adjacent facets and one coordinate facet per column touch, plus a second coordinate facet in the unique zero-difference column when present. The asymptotic follows by division by m^2. The packaged LP checker and recorded assertions were inspected, not executed; the exact result follows from the proof.

## originality

FAIL

The complete two-row result is a direct specialization of the distinct earlier general rectangular inball theorem f4e4e7c33724, which uses the same monotonicity convention, normalization and intrinsic Frobenius metric. It gives the radius, every center, and facet contacts; their specialization also yields the segment length and large-m asymptotics. The cited square theorem is not the relevant upper limit of prior coverage.

## value

FAIL

The parity of incenter uniqueness and the contact pattern are meaningful geometric data, but the exact data are already available for a strictly larger class. Here the interval length, tangency and asymptotics are routine evaluations of the explicit known parametrization. The direct two-row proof explains the specialization but does not establish a separately valuable result beyond it.

The dated certificate retains the supplied scientific assessment, sources and limitations.
