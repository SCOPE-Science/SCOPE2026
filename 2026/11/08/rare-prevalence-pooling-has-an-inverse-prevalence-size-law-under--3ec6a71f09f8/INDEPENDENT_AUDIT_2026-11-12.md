# Independent mathematical audit

## correctness

PASS

Under Beta(alpha,beta) latent prevalence, Q_k=(beta)_k/(kappa)_k and C_k=1/k+1-Q_k (k>=2, C_1=1). First differences have sign H_k-1, H_k=alpha k(k+1)Q_k/(kappa+k), with H_(k+1)/H_k=(k+2)(kappa+k-alpha)/[k(kappa+k+1)]. For alpha<1 this strictly exceeds 1, and gamma-ratio asymptotic makes H_k→∞. Thus the first H_k>=1 is the finite global optimum (possible adjacent tie); alpha<1 gives C_k<1 eventually, beating singleton. For alpha=kappa p→0, uniformly for k~t/alpha, log Q_k=-alpha(log k-psi(kappa))+o(alpha), so H_(floor(t/alpha))→t, alpha K_p→1 and min C=alpha[log(1/alpha)+1-psi(kappa)]+o(alpha). Independent exact-rational finite differences and global minimizers in three parameter pairs corroborated. Infinite p→0 follows from uniform logarithmic expansion.

## originality

PASS

Best-of-knowledge PASS ONLY for inverse-prevalence optimizer and p log(1/p) sharp cost at fixed positive intracluster correlation. Crucial stronger prior: published October 18 SCOPE beta-correlated screening theorem ALREADY establishes Q_k, the exact H_k difference, strict increasing H_k for alpha<=1, global first-crossing optimum and arbitrary-pool-size advantage; these are NOT original and must be attributed. Lendle/Basso supply model and formula; Landolfi–Lall gives general finite exchangeable-partition framework but not inspected fixed-kappa unbounded-pooling p→0 asymptotic. The current source RESULT.md and self-review inaccurately present exact unimodality/one-crossing as a contribution and omit October 18. Science survives on the new asymptotic alone; unchanged source package is NOT publication-ready without complete corrected research files and attribution.

## value

PASS

The asymptotic switch from classical independent k~p^-1/2 to positively correlated k~1/(kappa p), with optimum tests kappa p[log(1/(kappa p))+1-psi(kappa)]+o(p), is a meaningful exact scaling law for an established beta-binomial screening model. It answers a natural optimizer limit not mechanically determined by the known finite H crossing without uniform asymptotic analysis. This is mathematically substantive but practically conditional on unlimited clusters and no dilution; the previously known unimodality itself contributes no new value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
