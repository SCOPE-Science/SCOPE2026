# Independent mathematical audit

## correctness

PASS

The thinning proof needs the two Poisson release counts to keep their product law conditional on the environmental pair. This was implicit in the frozen computation, but marginal mutual independence alone does not give it. For example, take independent fair E1,E2 marginally, independent Poisson N1,N2 marginally, and let E2 be independent of everything else while P(E1=G|N1)=1/2+ε(1_{N1≥2}−P(N1≥2)), with 0<ε≤1/2. Keep survival independent given counts and environments. For any B>0, concentration at date 2 receives the fair-survival mixture, whereas concentration at date 1 increases its success strictly: the favorable-minus-unfavorable binomial tail is zero for N1<2, positive for N1≥2, when the favorable probability has been increased. The ensemble has the required marginal environmental symmetry, but even at B=1, ℓ=1/4,h=3/4 the two endpoints no longer tie. The repaired RESULT.md and VERIFICATION.md under /workspace/repairs/1/ specify the exogenous count law and conditional survival. Under this law the four-state mixture reduces to F(m+t)+F(m−t) times a strictly positive discordance weight plus an allocation-independent term. Its derivative for t>0 has the sign of t coth t−m, strictly increasing in t, so a nonzero interior critical point can only be a minimum and only center/endpoints can maximize. The endpoint gap has the sign of H(B)=βB coth(βB/2)−1−αB. The factor coth u−u csch²u lies in (0,1), hence H′<−ℓ, H(0+)=1 and H(∞)=−∞. Using 2<T coth(T/2)<T+2 with T=βB gives the strict threshold bounds. Symmetry and the strict derivative signs establish the three-way tie and exclude others. For a one-survivor threshold the only variable term decreases strictly with |t|; zero discordance or zero contrast instead makes all allocations tie. Own replay python3 /workspace/branches/review_checks.py reproduced B*≈2.09064648697929 and the displayed example probabilities via the original state mixture. Finite replay is only corroboration; the supplied checker was read, not executed. This theorem concerns a pooled census proxy and exactly the ≥2 event, not arbitrary higher quorums or establishment.

## originality

PASS

The distinct claim is a continuous fixed-expected-budget switch with no strictly unequal interior optimum for the pooled two-date Poisson threshold event, with an explicit unique root unchanged by positive discordance. Other release/Allee results, or one-founder diversification, are not claimed as new. The checked nearest claims do not give this classification; source access and scope limit the historical judgment.

## value

PASS

The fixed expected-budget allocation problem has natural extreme and symmetric strategies, but nonconcavity leaves open unequal optima and a continuous or abrupt transition. The proved classification gives no intermediate maximizer, a strict three-way tie at a single threshold, and independence of the optimizer from the degree of discordance. The contrast with one-survivor success explains why this threshold choice matters. It is a useful exact benchmark under exogenous releases, not an ecological intervention recommendation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
