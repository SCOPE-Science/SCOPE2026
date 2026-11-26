# An infinite family of non-unimodal fixed-budget richness variances

## Finding

For every integer \(m\ge 6\), partition \(2m+1\) individuals into three disjoint groups of sizes \((1,m,m)\). Sample exactly \(k\) individuals uniformly without replacement, and let \(V_k\) be the variance of the number of groups represented. Then \(V_3>V_4\) and \(V_m>V_{m-1}\). Consequently \((V_k)_{k=0}^{2m+1}\) is not unimodal, even when unimodality allows equal adjacent values. This does not assert exactly two strict local peaks for every \(m\).

## Assumptions and scope

Every individual belongs to exactly one of the three groups, all samples of a given size are equiprobable, and one sampled member is sufficient to represent a group. The statistic is the conditional richness variance of a fixed partition, not an estimator of the variance of an unknown population. The same model describes rarefied species richness with abundance profile \((1,m,m)\), or the count of retained functions when exactly \(k\) species are retained in a disjoint functional-group model.

## Proof

Put \(N=2m+1\), and write \(u_k=(N-k)/N\), \(b_k=\binom{m+1}{k}/\binom Nk\) and \(c_k=\binom m k/\binom Nk\), taking a binomial coefficient to be zero when its lower argument exceeds its upper one. For \(k\ge2\), the three absence probabilities are \(u_k,b_k,b_k\); each singleton–large group pair is jointly absent with probability \(c_k\), and the two large groups cannot both be absent. Since the number present is three minus the sum of absence indicators, the variance is
\[
V_k=u_k(1-u_k)+2b_k-4b_k^2+4c_k-4u_kb_k.
\]
Substitute \(k=3,4\) into this identity and cancel the binomial factors:
\[
V_3-V_4=\frac{5m^4-42m^3+123m^2-94m+24}{4(2m-1)^2(2m+1)^2}.
\]
At \(m=t+6\), the numerator is \(5t^4+78t^3+447t^2+1166t+1296>0\).

For the second difference write \(B_m=\binom{2m+1}{m}\). At \(k=m-1\) the pair \((b_k,c_k)\) is \(((m+1)(m+2)/(2B_m),(m+2)/B_m)\); at \(k=m\) it is \(((m+1)/B_m,1/B_m)\). Substitution and collection of powers of \(B_m\) gives
\[
V_m-V_{m-1}=\frac{2B_m^2-(10m^3+15m^2+5m)B_m+Q(m)}{B_m^2(2m+1)^2},
\]
where \(Q(m)=4m^6+28m^5+61m^4+58m^3+25m^2+4m>0\). Set \(L_m=(10m^3+15m^2+5m)/2\). At \(m=6\), \(B_m=1716>1365=L_m\). The binomial ratio \(B_{m+1}/B_m=4-2/(m+2)>3\), while \(L_{m+1}/L_m\le(1+1/m)^3<2\) by the positive coefficients of \(L_m\) and \(m\ge6\). Thus \(B_m>L_m\) by induction, making the second difference positive. Since \(m-1\ge5\), the increase from \(m-1\) to \(m\) follows the decrease from 3 to 4, which rules out unimodality.

## Verification

The standard-library script `verify.py` computes both differences from the exact sampling distribution, grouping outcomes by how many individuals each group contributes. It checks the two displayed identities and their signs for \(6\le m\le100\). The finite checks are diagnostics; the sign proof above is for all \(m\ge6\).

## Relationship to prior work and limitations

The fixed-budget variance is the classical rarefaction variance [1]; the functional-group application is prior as well [2]. The earlier rarefaction finding [3] already identifies the sharp first census size 13, its unique exceptional profile \((1,6,6)\), and its two strict peaks. This note does not claim those finite results as new: the contribution is the analytic extension to every \(m\ge6\), identifying a decline at small sample sizes and a renewed rise near the midpoint. The preceding proof certifies these two signs, not a classification of all local extrema or of other profiles. It says nothing about independent extinctions or empirical ecosystem stability. Historical priority for the infinite family is not asserted; in particular the earlier record's full proof was not available for comparison.

## References

1. K. L. Heck Jr., G. van Belle and D. Simberloff, *Explicit Calculation of the Rarefaction Diversity Measurement and the Determination of Sufficient Sample Size*, Ecology 56 (1975), 1459–1461. https://doi.org/10.2307/1934716
2. C. R. Fonseca and G. Ganade, *Species functional redundancy, random extinctions and the stability of ecosystems*, Journal of Ecology 89 (2001), 118–125. https://doi.org/10.1046/j.1365-2745.2001.00528.x
3. *Thirteen individuals are the sharp boundary for two peaks in rarefaction*, record 7d5b7b6433e4 (2026-10-18). https://github.com/Resultary/2026/tree/main/2026/10/18/SCOPE-thirteen-individuals-are-the-sharp-boundary-for-two-peaks-in-rarefaction--7d5b7b6433e4
