# Independent mathematical audit

## correctness

PASS

For iid Exp(lambda) data, exponential spacings E_j=(n-j+1)(X_(j)-X_(j-1)) are iid exponential, T=sum E_j and P_j=E_j/T are independent Dirichlet(1,...,1) proportions. Q_{n,k}=n sum_{j<=k}P_j/(n-j+1) is independent of T/n; exact first and second Dirichlet moments yield EQ=H_n-H_{n-k} and VarQ=[n(H_n^(2)-H_{n-k}^(2))-(H_n-H_{n-k})^2]/(n+1), with n=1 constant, odd median and asymptotic consequences. Independent exact rational examples including n=2,3,10 matched.

## originality

FAIL

FAIL: Lars Holst (1980), On the Lengths of the Pieces of a Stick Broken at Random, Theorem 2.2 explicitly gives normalized exponential order-statistic/spacings equivalence and E[S_(i)^r]=E[X_(i)^r] Gamma(n)/Gamma(n+r) for every positive integer r. Putting S_(i)=X_(i)/sum X_j and Q=nS_(k), the published r=1 and r=2 identities imply exactly the submitted first and second moments for all n,k. Independence from total is also recorded. Harmonic E[X_(k)] and Var[X_(k)] are classical Renyi spacing formulas. Thus the claimed new identity is a direct corollary of a much stronger prior result; failure is scientific coverage, not an access block.

## value

FAIL

FAIL: Although the formulas are correct and statistically interpretable, the submitted all-n exact moments are immediate r=1,2 specializations of Holst’s published all-moments theorem plus elementary harmonic spacing identities, and the finite median-to-mean trend was previously plotted. No distinct sharp obstruction, structural classification or unknown invariant survives to justify treating the submission as a new scientific contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
