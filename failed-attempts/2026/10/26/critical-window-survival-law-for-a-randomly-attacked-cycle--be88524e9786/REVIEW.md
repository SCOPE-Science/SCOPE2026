# Independent mathematical audit

## correctness

PASS

Fix the seed by rotational symmetry and let q=1−p. For 1≤k<n the k consecutive intervals of length k containing the seed specify disjoint events: open their k−1 internal edges and close their two boundary edges. Thus Pr(K_n=k)=kq²p^(k−1), and zero or one closed edge gives Pr(K_n=n)=p^n+nqp^(n−1). Summing gives Pr(K_n≥k)=p^(k−1)(1+(k−1)q) for 1≤k≤n. Put q=λ/n and k=ceil(n(1−y)) for 0≤y<1, and take limits; at y=1 the CDF is identically one. This verifies the full law, including the atom and absence of an atom at 1. Differentiation in y and λ gives the displayed density and stochastic order (strict for 0≤y<1, not outside the support). In the record's proof, a uniformly chosen failed edge can anchor the cyclic composition before taking the Dirichlet limit. For benefit, a proper contiguous deletion leaves a connected path in the original purchased graph (not necessarily in the transmission subgraph), giving n²Y_n². By bounded convergence of moments under weak convergence and c_e=O(1), the limit is the integral of λ²x(1−x)²e^(−λx) from 0 to 1. Integration of powers 1,2,3 against the exponential gives the stated closed form; the leading coefficient at zero is ∫₀¹x(1−x)² dx=1/12, and the closed form tends to 1 at infinity. This symbolic finite-law check independently replays the finding; no computation is needed.

## originality

PASS

Best-of-knowledge pass for the explicit full critical-window law as a statement, not a novelty claim for the percolation model, moments alone, or the underlying truncated two-geometric mechanism. No inspected result gives the univariate window law or an already specialized theorem that covers it. A general exact finite-graph iteration needs a cycle-specific evaluation before it can be used asymptotically; the elementary evaluation is important to the separate value decision.

## value

FAIL

The host and window are natural, but the result is a routine two-boundary-edge count followed by the geometric-to-exponential limit, truncation at one, and an elementary bounded moment. The network language does not add a constraint, an optimization result, or an equilibrium implication. The Poisson–Dirichlet derivation does not supply an independent new structural claim beyond this textbook calculation, and retaining just the elementary finite law or welfare formula would not repair the value deficit.

The dated certificate retains the supplied scientific assessment, sources and limitations.
