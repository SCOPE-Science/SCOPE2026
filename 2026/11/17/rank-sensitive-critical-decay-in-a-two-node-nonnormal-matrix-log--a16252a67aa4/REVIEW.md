# Independent mathematical audit

## correctness

PASS

PASS: For 0<c<3/2 the largest singular value of B_c=(sqrt(c²+4)+c)/2<2, so H↦B_c H(I-H)B_c* maps 0<=H<I into itself and preserves rank. For full-rank Q=H^-1, exact inverse identity Q_(n+1)=S*(Q_n+(I-H_n)^-1)S with S=B^-1 yields Q_n>=G_n=sum_{k=1}^n S^{*k}S^k. Direct summation G11=n,G12=-cn(n+1)/2,G22=n+c²n(n+1)(2n+1)/6 and det G=n²[12+c²(n²-1)]/12 imply ||H_n||=O(1/n). The inverse remainder is O(1/(n+1)), its summed (11),(12),(22) corrections are O(log n),O(n log n),O(n² log n), negligible against n,n²,n³. Therefore Q leading block [[n,-cn²/2],[-cn²/2,c²n³/3]] has det c²n^4/12, giving H scaled 4,6,12, determinant and eigenvalue asymptotics. For rank-one transverse w_2≠0, u_(n+1)-u_n=||B^n w||²/(1-rho_n), and ||B^n w||²∼c²|w2|² n²; summation gives rho=O(1/n), u∼c²|w2|² n³/3 and scaled entries 3,3,3. The eigenline obeys scalar logistic x↦x(1-x), giving limit 1; rank zero is fixed. H0=epsilon I transient trace formula is exact. Independently reproduced Gramian determinant and asymptotic inverse amplitudes (4,6,12) symbolically. No larger Jordan blocks or c=0 claim.

## originality

PASS

PASS best-of-knowledge: Pawela–Życzkowski introduce the nonlinear matrix logistic iteration, and in their Appendix A analyze a two-node upper-triangular coupling at a distinctly chaotic diagonal value (>1). Their prior study of invariant spectral densities and transfer of chaos does not state the nilpotent Jordan neutral eigenvalue-one extinction theorem or rank-conditioned amplitudes. The inverse-Gramian step is familiar linear-control mathematics, but its nonlinear state-dependent remainder and rank-one scalar quotient give new fixed-parameter critical asymptotics. No stronger Resultary or literature coverage was found.

## value

PASS

PASS: Global extinction at a neutral nonnormal Jordan coupling has a natural dynamical question distinct from the chaotic phase studied earlier. The exact 4/3/1 amplitudes and n^-1 vs n^-3 eigenvalue separation reveal how initial rank changes universal critical decay; the transient amplification example clarifies that one-step monotonicity is not required. These precise asymptotics are structurally informative for matrix population recurrences, not merely a scalar logistic substitution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
