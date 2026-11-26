# Independent mathematical audit

## correctness

PASS

For either epoch map, the H-norm squared of a synchronous difference is c²(1−c²) times the square of the retained input coordinate, bounded by c² times the original H-norm squared. Hence the Wasserstein contraction gives existence and convergence within finite second moments; coupling arbitrary finite-valued states and using bounded Lipschitz tests proves unrestricted uniqueness. The equations a=c²d+u and d=c²a+v have the stated positive solution and both second moments are preserved by each individual update, using fresh centered independent noise. Under order 12 the final square (X2′+cX1′)² is ξ2² exactly, so the stationary conditional loss is [(1−c²)a+v]/2. The reverse loss is [(1−c²)d+u]/2; subtraction gives c²(u−v)/(1+c²), yielding the exact risk, penalty and every tie case. Independent arithmetic check at c=1/2,u=9,v=4 gives a=32/3, d=20/3, losses 6 and 7 and uniform-order loss 6.5. Original covariance mixture is consistent with applying the last conditional kernel to its Gaussian marginal, and Isserlis gives the reported cumulant; these are not needed for the repair. The frozen SymPy and simulation code and its verification notes were read, not executed.

## originality

PASS

Only the repaired stationary quadratic loss and exact heteroscedastic order criterion are accepted as distinct on the reviewed evidence. The scan-law precedents and exact two-variable protocol equivalence are credited, not treated as novelty. The earlier scalar stationary-order result does not model fresh coordinate-oracle noise; the Gibbs antecedents work with different criteria, such as recovering a joint or minimizing divergence to prescribed conditionals.

## value

PASS

This is a small but natural benchmark with an order choice available to any method that sweeps coordinates against an oracle of unequal precision. The marginal variances are unchanged by order, so comparing their sizes alone cannot guide the policy. The exact loss decomposes the effects of first and last update noise, yields the operational noisier-first rule, and quantifies precisely the cost of uniform reshuffling or any mixed order. The result is scoped to stationary epoch-boundary objective, not transient convergence or adaptive schemes.

The dated certificate retains the supplied scientific assessment, sources and limitations.
