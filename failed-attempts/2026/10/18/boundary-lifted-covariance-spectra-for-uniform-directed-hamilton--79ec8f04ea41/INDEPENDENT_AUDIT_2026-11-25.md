# Independent mathematical audit

## correctness

PASS

For n>=3, two distinct arcs are incompatible precisely for a repeated tail, repeated head, or reversal. Otherwise contraction into ordered blocks gives their joint probability q: 1/[n(n−1)] for paths and 1/[(n−1)(n−2)] for cycles. The single-arc probabilities p are 1/n and 1/(n−1). Let B be the tail/head incidence matrix, T arc reversal, and J the all-ones matrix. Counting the diagonal and incompatible pairs gives covariance (p+q)I−q(B^TB+T)+(q−p²)J. Constants are null by the deterministic number of arcs. The orthogonal centered spaces are symmetric and skew vertex potentials and symmetric and skew zero-row-sum residuals. The potential dimensions are n−1 each; the symmetric and skew row-sum maps have ranks n and n−1 respectively, giving residual dimensions n(n−3)/2 and (n−1)(n−2)/2. On either potential space B^TB+T has eigenvalue n−1: symmetric u_a+u_b has B^TB eigenvalue n−2 and T=+1, and skew v_a−v_b has B^TB eigenvalue n and T=−1. On residuals B^TB=0 and T=±1. Thus the centered eigenvalues are p−(n−2)q, p and p+2q, with the first equal to q for paths and zero for cycles. This recovers both spectra and the rank drop, including the absent symmetric residual at n=3. Centered weighted path variance is the Rayleigh numerator, so the extreme values and equality classes follow; a nonzero potential and oriented triangle circulation realize both endpoints for every allowed n. Only the path has the claimed variance envelope. Replay is by the probability and operator calculations in RESULT.md Steps 1–4. The frozen verifier and its reported exact finite evidence for n=3..7 were inspected but not executed.

## originality

FAIL

The separately indexed Resultary record 984ab6d11231 directly gives the entire directed-cycle spectrum and the full covariance operator, not just its eigenvalues. Its arbitrary selected-arc framework includes deleting a distinguished vertex from an (n+1)-cycle. Rotating each cycle to start immediately after this vertex identifies the remaining linear order bijectively with the uniform n-label path. The path covariance is therefore exactly that known operator restricted to remaining arc indices. The restriction leaves B^TB, T and J of the n-label arc space, with p=1/n and q=1/[n(n−1)]. The same residuals and two elementary potential eigenspaces then give the frozen path eigenvalues and multiplicities; the rank comparison and sharp variance equality cases follow, not requiring a new second-moment result. This is mathematical coverage at review, not an assertion that the indexed document (whose directory date is later) had earlier priority or is independent of the frozen record. The uncertain QAP literature is not the reason for failure.

## value

FAIL

Directed path fluctuations and their endpoint and circulation interpretations are naturally motivated. But after crediting the exact indexed operator and its arc-restriction formulation, the numerical spectrum, rank drop and extremizers are obtained by deleting one vertex, evaluating row and column sums on potentials, and ordering the resulting eigenvalues. The frozen record provides no further mathematical consequence beyond those mechanical specializations and interpretations, so it does not meet the value standard for a new exact invariant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
