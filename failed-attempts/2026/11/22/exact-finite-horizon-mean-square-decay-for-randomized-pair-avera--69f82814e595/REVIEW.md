# Independent mathematical audit

## correctness

PASS

The claim for iid uniform star-edge choices at discrete interactions is correct. The energy observable is T^k(I-J), where T(B)=m^-1 sum_i W_i B W_i. Leaf symmetry makes it scalar on the hub-contrast line and leaf-contrast subspace. For a unit hub contrast, the W_i image has hub component alpha=(m-1)/(2m) and squared leaf component alpha-alpha^2. The projector trace identity then gives exactly the displayed matrix. Its row sums are alpha and nu_m. Subtracting the two rows on (q,r) gives r_next-q_next=q/2+3(m-1)(r-q)/(4m); positivity of the matrix yields the strict maximizing eigenspace from horizon one. The trace and determinant give the stated distinct positive eigenvalues for m>=3. The characteristic polynomial is positive at nu_m, with nu_m to the right of the trace midpoint, so nu_m exceeds both roots. Therefore the coefficient of the smaller-root power is negative, yielding strict log-concavity and ratios decreasing from nu_m to lambda_+. Expanding the radical verifies the large-m rate gap. The separately stated m=2 trajectory has a zero smaller root; strict log-concavity for all horizons is scoped to m>=3. Exact bounded replay: python3 /workspace/independent_checks.py 1 follows individual edge histories, including mixed inputs, for m=2 through 5 and horizons 0 through 5. The source checker was inspected rather than executed.

## originality

FAIL

The distinct indexed complete-bipartite record c93f751b4cab explicitly excludes the star from its formal theorem, but its transfer-matrix identity and proof mechanically give the star recurrence when the one-vertex shore's zero subspace is removed. This is demonstrated mathematical coverage, not an inference of publication order from two same-day records. The details of the two-root expression, gap, optimizer, log-concavity and limiting ratio follow by elementary algebra from that identical matrix. The general gossip literature alone would not justify this disposition.

## value

FAIL

The sharp finite-horizon rate is a natural quantity, but the matched bipartite operator reduction already computes it at the star boundary after deleting a zero sector. The remaining star-only statements amount to subtracting two rows, solving a quadratic and expanding its root. No distinct substantial invariant or boundary phenomenon remains beyond this mechanically inherited law.

The dated certificate retains the supplied scientific assessment, sources and limitations.
