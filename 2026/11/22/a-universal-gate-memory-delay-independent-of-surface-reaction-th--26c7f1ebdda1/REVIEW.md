# Independent mathematical audit

## correctness

PASS

In each reset-free excursion there is no reactive local time before the first open boundary encounter. Strong Markov restarting there and independence of the sampled threshold give h_j=c_j Φ for both initial gate states, including the convention for a zero atom. At a positive threshold consumption occurs in the open state almost surely: the independent gate has countably many jumps and the reflected diffusion is almost surely off the boundary at each such jump. For finite-a.s. thresholds there is positive probability of accumulating a finite level in an open sojourn, so h_0,h_1>0, and the killed reset kernel contracts by its row sums. If R is the discounted surviving occupancy, decomposing the free gate occupancy at reaction gives R=(I−h e_1^T)(rI−Q)^(−1). To check the difference independently, set the retained starting-state MFPT vector equal to (rI−Q)v. The renewal equation becomes (−Q+r h e_1^T)v=(1−h)/r. Left multiplication by π gives v_1=(1−πh)/(r²πh); the closed row gives α(v_0−v_1)=(πh−h_0)/(rπh). Since ET_F=rv_1 and ET_K=rπv, this proves β(h_1−h_0)/(Γ(βh_0+αh_1)). The common scalar cancels. The reflecting/open-contact backward ODE gives βc_0+αc_1=Γανe^(−μL)/(αν+βμ) and c_1−c_0=Γμe^(−νL)/(αν+βμ), yielding the stated strictly positive formula. For the individual means, a randomized exponential threshold of rate η imposes h'_1(0)=η(h_1(0)−1), hence the restart factor η/(η+Γμν/(αν+βμ)); the inverse open local time is multiplicative in deterministic threshold level by the same stopping argument, giving the claimed Laplace transform for general laws and the displayed Robin specialization. Fresh thresholds and loss of prior contact progress under both protocols are essential. The symbolic and finite-difference script was inspected, not executed.

## originality

PASS

The numerical gap at zero threshold is preexisting; so are full-refresh partially reactive renewal and the perfect-absorber surviving reset kernel. The distinct assertion is that keeping the gate but refreshing threshold and progress gives the same additive stationary-start gap for every fresh threshold law. Neither the perfect-absorber comparison nor the published partially reactive full-refresh formula gives that arbitrary-law comparison. The kernel proof can be reused, but the new factorization at the first open contact and its cancellation across protocols are essential to the extension.

## value

PASS

Although varying the threshold changes both MFPTs and can greatly change their magnitude, gate persistence contributes an exact positive additive offset unchanged by any fresh contact law. This cleanly separates gate memory from local-time reaction progress in a naturally motivated protocol comparison, not just a single reactivity example or a claim about optimizing reset rates.

The dated certificate retains the supplied scientific assessment, sources and limitations.
