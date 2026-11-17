# Independent mathematical audit

## correctness

PASS

Independently solved the stationarity equations z=P^T diag((1-h_+)^2,(1-h_-)^2) z + sigma^2 P^T(h_+^2,h_-^2)/2 using exact symbolic inversion. The submitted V(p)-V0 factor 2sigma^2 h^2 delta^2[2-t+2p(t-1)]/((2-h)D) and derivative dV/dp=8sigma^2 delta^2 h^4(1-delta^2)(h-1)/D^2 were both verified symbolically. D=p(1-alpha)(1-beta)+(1-p)(1-alpha beta)>0 throughout. Thus V<V0 iff t>2 and p<(t-2)/(2(t-1)); equality at t=2,p=0 or threshold for t>2; p=1/2 always loses. The periodic case p=0 requires a random stationary phase, explicitly assumed, and r<2 individual stability ensures convergence.

## originality

PASS

Gürbüzbalaban–Hu–Şimşekli–Zhu (2023) analyzes the same family of Markovian two-step learning-rate schedules but for tail indices in stochastic linear regression with random Hessian noise. Its §3 and Appendix B.4 give tail-index and infinite-variance conditions, not the exact finite stationary second-moment comparison for an additive independent gradient-noise scalar quadratic, which has uniformly contractive multipliers. Hence the 2023 schedule classification is not a direct implication of this noise-floor frontier.

## value

PASS

A natural controlled comparison holds the marginal stepsize distribution and oracle cost fixed while changing temporal persistence, yielding exact improvement and monotonicity frontiers relevant to noisy optimization dynamics.

The dated certificate retains the supplied scientific assessment, sources and limitations.
