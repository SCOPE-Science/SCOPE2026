# Independent mathematical audit

## correctness

PASS

In energy coordinates each update is an orthogonal projection, and independence gives the exact expected-energy operator Phi^T(I). At zero coupling the objective is (1-min_i p_i)^T; uniform O(epsilon) perturbation (epsilon=sqrt(delta)) and the zero-sum constraint imply that every optimizer is uniform plus epsilon times bounded z. At uniform sampling the first-order hub-to-leaf averaged entry satisfies h_(t+1)=s h_t+u r^t, h_0=0; other off-diagonal entries have zero derivative. The diagonal derivative is -T r^(T-1) z_i. A direct global check of the minimax step is to use the Rayleigh quotient of the normalized all-ones vector: on sum z_i=0 this gives the lower bound 2 sqrt(m) h_T/(m+1), independent of z. Equality forces constant row sums and uniquely determines z, with hub term (m-1)sqrt(m) h_T/((m+1) T r^(T-1)) and identical leaf terms -z_0/m. That vector of row sums is attained; the positive all-ones eigenvector is the top eigenvector by Perron after a diagonal shift. Uniform Taylor remainder on bounded z and subsequence comparison yield the stated expansions for every minimizer. The geometric-average factor strictly decreases with T, establishing the claimed separation only for fixed T at sufficiently weak coupling. An independent finite check summing all 256 projection words for m=3, T=4 and z=(0.37,-0.12,-0.08,-0.17) gives entrywise errors 8.84e-4 and 8.84e-5 in the scaled first derivative at epsilon=1e-3 and 1e-4. This is corroboration only.

## originality

PASS

The supported distinct claim is the explicit weak-coupling, full-simplex first-order solution for sharp finite-horizon iid single-coordinate descent on a star. The exact one-step optimizer is already covered, and horizon-dependent minimax sampling with strict one-step separation is demonstrably present in a different model. Neither is credited as novel on its own.

## value

PASS

The coupled star is a natural controlled test of whether an optimal stationary one-step sampler remains optimal when its projection updates are composed. The exact leading bias and retention quantify the failure for every fixed T>=2, not just a numerical example or a weaker convergence bound, and the first-order minimax calculation eliminates a hidden equal-leaf assumption. The exact dependence on horizon is useful as a benchmark for finite-horizon sampling designs; it is not a wall-clock or large-T claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
