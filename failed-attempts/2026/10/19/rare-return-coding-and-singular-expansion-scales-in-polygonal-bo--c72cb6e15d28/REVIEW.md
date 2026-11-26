# Independent mathematical audit

## correctness

PASS

The 2011 source gives the exact transition graph immediately after Theorem 2; its last relation is F(M_{n+3})=F(M_1)=M_2. Deleting vertex 2 leaves a DAG. From 2 the forced chain to n has n−2 edges, and each of the two choices of successor of n has two routes back, of three and four more edges. Schur complementation at vertex 2 gives det(I−zA)=1−2z^(n+1)−2z^(n+2), since the deleted graph contributes determinant one; the trace identity then gives the stated symbolic zeta. The positive Perron root is the unique root above 1 of λ^(n+2)=2(λ+1), and decreases with n. The graph is irreducible (and the return lengths are coprime), so the Parry measure is the unique symbolic measure of maximal entropy. Along a return to vertex 2, the product of the transition probabilities telescopes in the right Perron eigenvector, giving exactly λ^(−ℓ) conditional on starting there. Summing the two short and two long paths yields the stated probabilities and mean. Setting h=log λ gives (m−1/2)h=log 4+log cosh(h/2); h=O(1/m) and the expansion follows. For the parameter root, g_n(1)=−4π²/m²+O(m^−4), g_n′(1)=m+O(m^−1), and g_n′ is positive on [1,∞) for large n. Taylor's remainder on [1,1+C/m³] is O(m²(r−1)²); bracket the root with C>4π², then divide by g_n′(1) to obtain r−1=4π²/m³+O(m^−5). Now D_R=r² and E=(r−1)²+2r(1−cos θ)=4π²/m²+O(m^−4), while r^(2−n)=1+O(m^−2). These give both determinant expansions and the stated ratio. Reducing q via sin(nθ)=−sin(2θ) in the primary parameter equations also gives the stated T_L. No identification with physical zeta or planar entropy is needed.

## originality

FAIL

The claimed symbolic structure is mechanically specified by the already published transition relations, and its zeta, entropy and return probabilities are standard, direct evaluations of that graph. The two branch expressions are supplied in the same paper, including left divergence and eventual area expansion; their numerical scaling coefficients and the entropy comparison are obtainable directly by a one-step Taylor estimate at the explicit scalar root and substitution. The formulas are not claimed to be printed verbatim in that paper. The failure is mechanical implication on the exact same family, not an inference from missing search results or inaccessible literature.

## value

FAIL

The formulas are useful exposition for the known partition, but all the symbolic outputs follow from reading four routes in the published covers and applying standard finite-state formulas. The asymptotic coefficients use the explicit scalar root and its first derivative at 1; their ratio does not establish a dynamical link between physical entropy and expansion. No independent mathematical question is resolved by a remainder beyond these direct evaluations. Rewording it as a comparison of scales would not change that.

The dated certificate retains the supplied scientific assessment, sources and limitations.
