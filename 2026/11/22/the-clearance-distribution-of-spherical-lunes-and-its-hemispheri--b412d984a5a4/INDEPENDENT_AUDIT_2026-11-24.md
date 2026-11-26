# Independent mathematical audit

## correctness

PASS

Re-audited the repaired theorem. For the farther face at separation above pi/2, maximizing the inner product over that hemisphere projects to the ridge, not to the opposite half of the great sphere. For separation at most pi/2 the ordinary projection is admissible, and among the admissible projections the smaller angular separation wins. This proves sin D=sqrt(Q) sin U, including the hemisphere and the zero-projection limit. Independent Gaussian blocks give U uniform and Z=1-Q of density k z^(k-1). The exact mark density below the graph H_epsilon follows by its Jacobian; the sine-factor product gives convergence uniformly in v, and locally uniformly in lambda, with fixed-opening graph 1-v and critical graph (1-v)(2lambda+1+v). Integrating the absolute unnormalized density difference gives the integral of |H_epsilon^k-H^k| divided by k. The critical normalizer stays bounded below, so normalization preserves the claimed compact-uniform TV convergence even for d=3. Integrating the graph gives the coefficients and exponents; J_0=B(1/2,k+1)/2, and H_lambda/(2lambda) tends uniformly to 1-v. In the overlap epsilon/(pi/2-a)->0 the same sine factors give the claimed matching limit. Replayed python3 /tmp/opencode/frozen_nov24_lune.py: 100 independent disk-slice versus polar survival comparisons (max relative discrepancy 2.8e-12), 25 lower slopes and moments, nine critical tail comparisons and 20 exact-integral TV diagnostics for pairs of finite-epsilon and limiting densities. These are corroboration, not proofs of the limits. The frozen script was read, not executed; the old notes report 5186 versus 5230 in the finding, and independent evaluation of the assertion counter and skipped-tail gates yields 5230. The repaired notes do not use that count.

## originality

PASS

Qualified pass for the repaired marked conditional laws, with their true crossover normalizations and joint angular/radial scaling. The unmarked exact survival distribution is explicitly credited as a known specialization. No covering result for the fixed-opening Dirichlet law, its near-hemisphere curved marked transition, or the compact-uniform TV limit was established in the inspected evidence.

## value

PASS

The incenter rare-event conditioning separates two mechanisms: an aperture-constrained angular interval with a first-order transverse deficit, versus a hemisphere cap with a second-order deficit and a different event exponent. The explicit jointly normalized TV law, including the limiting shapes, aperture crossover and asymptotic matching, describes how to sample or analyze the configurations giving rare clearance; exact cap volumes alone do not answer that conditional question. The repaired contribution does not rely on moment inversion or claim a new volume formula.

The dated certificate retains the supplied scientific assessment, sources and limitations.
