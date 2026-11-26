# Independent mathematical audit

## correctness

PASS

For A={1 and 2 in the same block}, the predictive rule gives P(A)=(1-α)/(θ+1) and P(Aᶜ)=(θ+α)/(θ+1), both strictly positive on the stated domain, including admissible negative θ. The mean richness at m+1 conditional on either event is its mean at m multiplied by 1+α/(θ+m), plus θ/(θ+m). The difference starts at 2−1 and is precisely R_n, with the empty product for n=2. Centering the two conditional means gives the signed shifts in the Finding. Cov(K_n,1_A) is minus the product of the two event probabilities and the gap. Label exchangeability makes all pair covariances equal; averaging therefore produces exactly the sample Q_n covariance. D_n and the squared-frequency statistic follow respectively from a sign change and the deterministic identity Ĥ_n=1/n+(n−1)Q_n/n. At α=0 the product is always one, yielding the Ewens and uniform-permutation values; the ratio of shifted gamma functions gives the stated α>0 asymptotic with positive arguments. The isolated malformed fraction at frozen Proof line 170 is a rendering error: the same product is well defined in the Finding and follows from the recursion. The archived rational checker and output were inspected, not executed. The enumeration is supplementary; its recurrence replay compares adjacent evaluations of the same product and is not an independent all-n proof.

## originality

FAIL

The full two-parameter conditional-gap result is a direct corollary of Sibuya's published exact restart mean, and the displayed covariance follows from that mean by the covariance identity for one indicator and exchangeable averaging. To see this without relying on keyword matches, write K'_s(m,k)=(K_{m+s}−K_m | K_m=k). In Proposition 2, Eq. (13), set moment order r=1, m=2, s=n−2. For α>0 this gives E[K'_s(2,k)]=(θ/α+k)(R_n−1). Adding k and subtracting the instances k=2 and k=1 gives exactly R_n; A={K_2=1} and Aᶜ={K_2=2}. For α=0 the restart transition probability for a new block is independent of k, so the gap is one (also the limit of the same formula for θ>0). Thus the covariance and its stated conditional refinements are mechanically covered even though the earlier source does not print them in Simpson notation. The later two-time Resultary hit is explicit equivalent coverage on the diagonal and is not the reason for the failure. Inaccessible literature is not needed for this decision.

## value

FAIL

The statistic is natural and the succinct presentation may be useful exposition, but the narrow exact claim is mechanically implied by the known conditional first moment and an elementary identity for an indicator. Both the allegedly stronger gap and the same-sample covariance are covered, including the Ewens and normalized variants. The candidate adds no surviving worthwhile mathematical gap by itself, and merely reframing it as a Simpson statistic would not repair the finding.

The dated certificate retains the supplied scientific assessment, sources and limitations.
