# Independent mathematical audit

## correctness

PASS

The killed backward equation on the isolated side network has positive-definite B (its quadratic form is the sum of internal edge energies and positive death-plus-target-rate diagonal terms). Solving the updated equation and taking the gateway coordinate gives q_1=(z+alpha*R*p)/(1+alpha*R), where R=(B^-1)_11>0 and z is the isolated gateway success probability. The source equation then makes p a strict convex mixture of P_0 and z with weight beta/(d+kappa+beta)>0 on z, beta=alpha/(1+alpha*R). This verifies the sign and equality cases, arbitrary positive entry rate, and the single-gateway extension under its stated assumptions. The isolated path recurrence has reflecting condition z_0=z_1 and prescribed target z_(n+1)=1; the stated ratio of coshes satisfies both and the interior equation, including n=1. With time rescaling, Z_n(g)=E exp(-kappa*tau_n/g) for an a.s. finite and strictly positive unit-rate hitting time, giving strictly increasing continuity and the two endpoint limits. Z_(n+1)<Z_n pointwise and hence g_c increases strictly. In the critical cosh equation the left side is at least cosh(n*theta_n), so theta_n<=arcosh(1+kappa/d)/n, and the equation then gives the asserted limit of (n+1/2)*theta_n. Using 2(cosh(theta_n)-1)~theta_n^2 gives the sharp coefficient. Series-parallel conductance uses n links of rate g after the entry edge and is strictly increased independently of mortality. An independent n=2 backward solve returned (3/7,2/7,3/7) for the all-unit adverse example and gave detached success g^2/(g^2+3g+1) for kappa=1, hence the stated threshold for d=1. The supplied verify_corridor.py was inspected, not run; its path computations do not verify arbitrary side networks, for which the exact proof suffices.

## originality

PASS

The supported contribution is the coupled all-entry-rate conductance/success comparison and exact homogeneous threshold, including its asymptotic coefficient. First-passage discounting, rank-one inverse updates and electrical monotonicity are standard ingredients, not separate claims of novelty. The closest available results treat different passage models or objectives; priority is not certified.

## value

PASS

Electrical conductance and success before independent death are natural but different connectivity objectives. The model exhibits a strict, exactly quantified failure of the former to track the latter; entry-rate independence and the sharp length-squared scale are informative for comparing possible detours, beyond the existence of one adverse example. The single-gateway sign criterion also applies to non-path side networks. This is an idealized stochastic-network statement, not a calibrated ecological prediction.

The dated certificate retains the supplied scientific assessment, sources and limitations.
