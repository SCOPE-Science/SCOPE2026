# Independent mathematical audit

## correctness

PASS

U_j=product of absent incoming edges and V_i=product of absent outgoing edges. Each U_j family and each V_i family are independent separately, while Cov(U_j,V_i)=p q^{n+j-i-2} for i<j and 0 otherwise. Summing geometric series produces E=(1-q^n)/p, Var=E-(1-q^{2n})/[p(1+q)] and Cov=q^{n-1}(np-1+q^n)/p>0. At p=c/n, finite formulas give A=(1-e^{-c})^2/(2c) and B=e^{-c}(c-1+e^{-c})/c. Target-edge filtration martingale increments have predictable covariance sums concentrating by Var(R_j)<=n, p=c/n; Lindeberg from uniformly bounded conditional fourth moments and Cramér-Wold gives joint CLT. Symbolic derivative of rho matches -2 exp(c)[c(exp(c)+1)-2(exp(c)-1)]/(exp(c)-1)^3<0 by tanh(x)<x. Fresh independent exact enumeration on n=3..5 at p=1/3,1/2 verified all 1st/2nd moments. Endpoint rho limits 1 and 0; no other DAG sampling law is claimed.

## originality

PASS

The same preordered Bernoulli DAG model is classical, but inspected Barak–Erdős and Denisov–Foss–Konstantopoulos studies concern maximal strongly independent sets and longest-path/regeneration, respectively; Ralaivaosaona works with different conditioned ensemble and source means. The explicit bivariate source/sink CLT and strictly monotone sparse correlation curve were not established in those texts. Bollobás–Brightwell random graph orders primary full text inaccessible (Oxford VPN disconnected), a named significant implicit-coverage risk. Best-of-knowledge qualified PASS.

## value

PASS

Identifies an exact dependence law and nontrivial bivariate Gaussian fluctuation regime for two fundamental extremal vertex statistics in a natural classical ordered DAG, with an explicit strictly decreasing correlation curve across every fixed positive sparse density; relevant for probabilistic combinatorics and random orders.

The dated certificate retains the supplied scientific assessment, sources and limitations.
