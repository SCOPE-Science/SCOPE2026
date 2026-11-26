# Independent mathematical audit

## correctness

PASS

Strict negativity of each invasion payoff at e_j is equivalent almost surely to pure ESS, and given its diagonal D_j the N-1 outside comparisons are independent with acceptance probability Phi(D_j/sqrt(v_mu)). Independent row maxima give the zero-ratio endpoint. For m=N-1>=2 the symmetrized integrand z on |Z| involves p^m+(1-p)^m, strictly increasing for p=Phi(t|Z|)>1/2 as t=v_mu^(-1/2) increases; this independently proves the monotonicity direction. The expectation is even in t with bounded second derivative near zero, giving O_N(mu^-2) one-site error. For each pair the independent Gaussian antisymmetric contrast has density 1/sqrt(pi) at zero, interval width (D_i+D_j-2U)_+/(1+2mu), and the N-2 outside tests for each resident multiply to leading term 4^(-(N-2)). The width numerator is the positive part of N(0,4), of mean sqrt(2/pi). Bounded Gaussian CDF derivatives, finite moments and the Lipschitz estimate for the outside factors give the claimed integrable O_N(mu^-2) pair error. At least two independent contrast intervals are required for a triple, so its error bound suffices: summing one-site probabilities and distinct pair overlaps gives probabilities 1-q_N+C_N/mu, q_N-2C_N/mu and C_N/mu at the stated precision. The N=2 orthant law reduces to arctan(1/sqrt(v_mu))/pi, independently confirming its leading constant (python /workspace/branches/independent-algebra.py, item 4). All probability comparisons are fixed-N and count pure ESSs only; the script spot check is not an all-N proof.

## originality

PASS

The zero-ratio binomial law and the limiting tournament probability are existing coverage. The distinct contribution is fixed-N positive-ratio Gaussian expectation together with the explicit inverse-ratio rare-pair coefficient and resulting trichotomy. The exact same-ensemble primary model and all-support simulations do not give that finite-ratio analytic law. Bounded search does not establish historical priority.

## value

PASS

The primary numerical study motivates understanding rare multiplicity, and the pure-strategy restriction permits an exact distribution-level benchmark. The first nonzero correction is meaningful where the limiting tournament assigns zero mass to multiplicity. This does not solve mixed-support multiplicities, uniform large-N estimates, or real-system outcomes.

The dated certificate retains the supplied scientific assessment, sources and limitations.
