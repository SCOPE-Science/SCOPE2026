# Independent mathematical audit

## correctness

PASS

For a first rod at u and L=n-1+epsilon, the sum floor(u)+floor(L-u) equals n-1 exactly when the fractional part of u is at most epsilon (up to zero-probability boundaries). Each successful split therefore lies in a stated window, and both daughters must attain their respective integer capacities. Conditioning and independent renewal give the exact recursion. Scaling the slack by epsilon gives a weight v^(q-1) times the daughter asymptote in an edge window or a smooth strictly positive density factor times two daughter asymptotes in an interior window; q>0 and nonnegative exponents give integrable domination. The resulting positive beta coefficients have exactly the powers in the displayed recurrence. For a fixed tree, if b vertices have two children, the number of unary vertices is n-1-2b, giving cost q(n-1)+(1-2q)b. A full binary tree with b internal nodes can be extended by a chain of n-1-2b unary nodes above its root, realizing every allowed b; this verifies all minimizing and tying cases. An actual change of topology occurs for n>=3; for n=2 the two descriptions select the same unary topology, as the stated exponent and proof imply. At n=3 the two edge integrals and the central integral have the stated coefficients; their relative O(epsilon) errors follow by using F_2(s)=2s^q/(q B(q,q)) times (1+O(s)) uniformly over the window. The separate point values at zero slack in the integral do not affect it. Independent replay: python3 /workspace/review_checks.py 4 checks finite tree profiles and rational cost minimization through n=12 and computes the two n=3 terms at q=1/2 by a sine substitution; the normalized terms at epsilon=0.0001 are 0.318293972 and 0.900276929. The frozen checker was inspected, not executed.

## originality

PASS

The supported distinct claim is the sharp fixed-n small-excess asymptotic for all n, including the exact q-dependent classification of leading histories and the asymptotic coefficient recursion. The kernel, general occupation-statistics recursions, and closed low-shell probabilities are credited to prior work, not treated as new. The low-shell examples may be direct expansions of those probabilities and are not required for the distinct contribution.

## value

PASS

Near an integer interval length, capacity attainment is a natural rare event distinct from typical parking density. Determining which deposition geometries contribute to leading order explains the nonanalytic dependence on the charge bias for n>=3. The complete finite-n exponent and coefficients quantify that effect without claims about finite-time dynamics or a uniform thermodynamic limit.

The dated certificate retains the supplied scientific assessment, sources and limitations.
