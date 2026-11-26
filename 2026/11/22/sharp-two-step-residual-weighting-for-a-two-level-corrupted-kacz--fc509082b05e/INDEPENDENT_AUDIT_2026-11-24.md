# Independent mathematical audit

## correctness

PASS

From the row weights the two transition probabilities are α=zt/(1+zt) and β=t/(z+t), respectively clean-to-corrupt and corrupt-to-clean. The difference of the two terminal bad-state probabilities is (1−α−β)², so the corrupt start is worst (tied at t=1); its risk is 1−β(2−α−β). This yields the stated rational function. Separately differentiating the success probability yields zN_z(t)/[(z+t)³(1+zt)²]. For 0<z<1 the strict concavity of N_z, its positive values at 0 and z and its negative value at 1 give a unique crossing and a strict gain over t=1. For z≥1, N_1(t)=2(1−t)(1+t)² and ∂N_z/∂z is positive on [0,1], so t=1 is uniquely optimal, including z=1. At the small-z scale, N_z(az^(1/3))/z tends to 2−a³, bracketing the unique root. The stationary bad probability is asymptotic to pt and the eigenvalue to p/t on that scale; substituting in π_B+(1−π_B)λ² yields the announced p^(4/3) rate and constant. An independent two-state calculation at p=1/10, t=1/2 gave 175/2299; numerical bisection gave t*≈0.52257733 and risk ≈0.07599966. The excluded t=0 has both states absorbing and risk one.

## originality

PASS

Credit the prior residual-weighted framework, two-state reduction and stationarity/relaxation ingredients. The distinct supported claim is the solution of the fixed-ratio, two-update worst-start optimization, including the half-contamination transition and the cubic-root and four-thirds-power laws. Neither an earlier first-hit result nor the closest catalogue statement on long-run bias and relaxation provides those conclusions. The exact catalogue self-hit is not independent coverage, and no order between distinct same-day records is inferred.

## value

PASS

The two-level instance isolates the finite-horizon cost of protecting a bad start: uniform sampling is always best after one update, but after two the optimizer is nonuniform exactly below half contamination. In the rare-corruption regime the optimized risk is of smaller order than uniform sampling, at a precise weight scale. This is a motivated benchmark for fixed residual weighting rather than just a rational two-state transition calculation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
