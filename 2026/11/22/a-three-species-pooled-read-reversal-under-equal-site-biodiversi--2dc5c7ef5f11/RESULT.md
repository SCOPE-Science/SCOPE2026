# A three-species pooled-read reversal under equal-site biodiversity sampling

## Finding

**Theorem (sharp full-inventory reversal despite marginal detection losses).** Let \(a,b,c>0\) satisfy \(a+b+c=1\). Two sites have idealized error-free, with-replacement read-label distributions \((a,b,c)\) and \((1,0,0)\) for three distinguishable taxa \(A,B,C\). Compare the following designs with **exactly four total reads**:

- **Separate equal allocation (E):** two independent reads from each site; retain the union of detected taxon labels.
- **Equal physical mixing (P):** four independent reads from the pooled composition \(((1+a)/2,b/2,c/2)\).

For each taxon separately, E has **strictly greater** probability of detecting that taxon than P. Nevertheless, the probabilities of detecting **all three taxa in the same four-read experiment** obey the exact identity

\[
\Pr_P(\{A,B,C\}\text{ all observed})-\Pr_E(\{A,B,C\}\text{ all observed})=\frac{bc}{2}(3a-1).
\]

Thus pooling wins for the joint complete-inventory objective exactly when \(a>1/3\), ties at \(a=1/3\), and loses when \(a<1/3\), independently of the relative frequencies of taxa \(B\) and \(C\). For example, \((a,b,c)=(3/5,1/5,1/5)\) gives complete-inventory probabilities \(12/125\) for P and \(2/25\) for E. A reversal of joint-completion ranking under **marginal detection dominance** is impossible with only one or two taxa; three taxa is the sharp minimum.

This advantage of P over *equal* allocation is transient at sufficiently large read depth: for every fixed positive \(a,b,c\), an equal \(n\)-per-site separate design eventually has a higher probability of complete inventory than a \(2n\)-read equal mixture. Moreover, pooling cannot beat an **optimally chosen deterministic read allocation** across the sites, at any fixed total depth. For the displayed four-read family, the deterministic three-reads-at-site-one, one-at-site-two allocation has complete-inventory probability \(3bc(1+a)\), exactly twice the pooled probability. These are scope qualifications, not an empirical assertion that pooling is preferable.

## Assumptions and scope

Read labels are independently and identically distributed conditional on the selected site, with fixed probabilities. Physical pooling is modeled as drawing independently from a **50–50 mixture of the two normalized read compositions**; this requires that the effective DNA contribution of each site to the library be equal after normalization. The four-read budget is identical for both designs, all labels are correctly assigned, sequencing occurs with replacement, and sampling costs, extraction loss, primer bias, contamination, PCR jackpot effects, and molecular saturation are excluded. Taxon \(A\) can occur at both sites, while \(B,C\) are restricted to the first. The objective is the probability that **all three named taxa** occur at least once among the read labels, not average richness, relative abundance estimation, or a comparison of laboratory cost savings.

The strict assumptions \(a,b,c>0\) guarantee that all three taxa are possible and all strict inequalities are meaningful. At the boundary \(bc=0\), complete inventory is impossible in either design; the formula then gives equality, not a strict reversal. All probabilities are unconditional over the idealized sampling law.

## Proof

**Individual taxon detection.** In E, taxon \(A\) is detected with probability one because the second site produces only \(A\). In P, the probability of not observing \(A\) is \(((b+c)/2)^4>0\). For either \(X\in\{B,C\}\), writing its frequency at site one as \(u\in(0,1)\), its absence probabilities under E and P respectively are

\[
(1-u)^2,\qquad (1-u/2)^4.
\]

Since \((1-u/2)^2=1-u+u^2/4>1-u\), the P absence probability is strictly larger. Every single-taxon detection probability is therefore strictly higher under E.

**Joint complete inventory.** E always sees taxon \(A\), and both first-site reads must consist of one \(B\) and one \(C\), in either order. Therefore

\[
P_E=2bc.
\]

For a three-taxon probability vector \((u,v,w)\) with positive entries summing to one, exactly four independent categorical reads contain all three categories if one category appears twice and the other two once. The exact multinomial count is

\[
\Pr(\text{all three in four})=12uvw(u+v+w)=12uvw.
\]

Substitute \((u,v,w)=((1+a)/2,b/2,c/2)\) to obtain \(P_P=\frac32(1+a)bc\). Hence

\[
P_P-P_E=\frac{bc}{2}(3a-1),
\]

whose sign gives the complete sharp classification.

**Minimum number of taxa.** If an experiment produces at least one read and there are exactly two possible taxa \(A,B\), then the events \(E_A\) and \(E_B\) that each taxon appears have union of probability one. The inclusion–exclusion identity

\[
\Pr(E_A\cap E_B)=\Pr(E_A)+\Pr(E_B)-1
\]

implies that a design with at least as great detection probability for each of the two taxa must have at least as great probability of detecting both. The one-taxon case is immediate. The strict three-taxon construction above shows that the lower bound is attained.

**Eventual reversal at larger equal depths.** With \(n\) reads per site, E has \(A\) automatically and its failure probability is at most \((1-b)^n+(1-c)^n\). Put \(s=\min(b,c)>0\). This is at most \(2(1-s)^n\). With \(2n\) pooled reads, the probability of failing to observe the rarer one of \(B,C\) is exactly \((1-s/2)^{2n}\), a lower bound on pooling's complete-inventory failure probability. Since

\[
\frac{(1-s/2)^2}{1-s}=1+\frac{s^2}{4(1-s)}>1,
\]

for every integer \(n>\log 2/\log[((1-s/2)^2)/(1-s)]\), pooled failure is strictly greater than separate failure. Therefore at sufficiently high read depths E strictly wins, including whenever P wins at depth four.

**Why pooling is not globally optimal.** At any total depth \(N\), generate the pooled reads by first selecting their site labels independently with probability one half each, then drawing a taxon label according to the selected site. Conditional on exactly \(k\) reads having chosen site one, the law of the pooled read-label multiset equals that of \(k\) independent first-site and \(N-k\) independent second-site reads. Hence, for every event depending only on observed taxa, pooling's event probability is a binomially weighted convex combination of the deterministic allocation probabilities. It cannot exceed their maximum. At \(N=4\), allocating three reads to site one and one to site two detects all taxa exactly when the first-site three reads contain both \(B,C\); enumeration of the possible remaining category yields \(3bc(1+a)=2P_P>P_P\). This completes the proof.

## Verification

The standalone Python 3 checker `checker.py` enumerates every possible ordered read sequence with `fractions.Fraction`, independently of the four-read multinomial shortcut. It checks 1,771 positive rational composition triples, including equalities, strict threshold signs, all three single-taxon marginals, the three-plus-one allocation, the binomial-mixture identity, the three-read control, and a rigorous high-depth failure comparison. Run `python checker.py` from the artifact directory; it prints an explicit PASS marker. Finite testing is supplementary: unrestricted real parameters, the minimum-taxon statement, and eventual high-depth reversal follow from the displayed algebra and inequalities, not a finite grid.

## Relationship to prior work

The sampling question is motivated by empirical studies of individual versus pooled environmental-DNA samples. Courtaillac and collaborators (2024) measured species-label differences between pooled and individually sequenced kelp-forest eDNA extracts; Sato and collaborators (2017) experimentally documented limitations and missed rare taxa in pooled freshwater eDNA; and Altermatt and collaborators (2023) analyzed sampling volume, replication and sequencing depth. Those results concern laboratory measurements, observed richness, or empirical detection patterns, rather than this exact idealized multinomial implication paradox and its \(a=1/3\) frontier.

Classical stratified sampling, coupon-collector inclusion–exclusion, and multinomial counting supply the elementary ingredients of the proof and are not claimed as new. Relevant mathematical comparisons address expected richness under two-site budgets and three-species coupon-collector completion-time variance, but neither objective controls the comparison between individual marginal detection probabilities and a **joint** all-taxa detection event under equal versus pooled read allocation. The contribution asserted here is narrowly the sharp three-taxon/equal-four-read counterexample and its mathematical scope controls, not a general new sampling framework or practical sequencing recommendation.

## Limitations

This is an exactly solvable idealization with fixed independent read composition and exactly equal effective mixture weights. Real eDNA sampling includes capture variability, extraction losses, unequal library concentrations, amplification bias, false positives and negatives, and spatially varying occupancy. Actual biological replicates and pooled DNA libraries may have unequal total usable reads and substantially different costs. No empirical samples were analyzed; there is no assertion that a particular laboratory would improve complete species recovery by pooling. Existing general probability and stratified-sampling theory could imply pieces of the algebra; historical priority of the exact stated combination remains subject to independent specialist review. The comparison favors P only over the specified equal allocation, not over an optimized allocation.

## References

- K.-L. Courtaillac, J. Landschoff, K. Hull and S. von der Heyden, “The Effect of Spatio-Temporal Sampling and Biological Replication on the Detection of Kelp Forest Fish Communities Using eDNA Metabarcoding,” *Environmental DNA* 6 (2024), e70023; first published 2024-10-14; https://doi.org/10.1002/edn3.70023.
- H. Sato, Y. Sogo, H. Doi and H. Yamanaka, “Usefulness and limitations of sample pooling for environmental DNA metabarcoding of freshwater fish communities,” *Scientific Reports* 7 (2017), 14860; https://doi.org/10.1038/s41598-017-14978-6.
- F. Altermatt and collaborators, “Quantifying biodiversity using eDNA from water bodies: General principles and recommendations for sampling designs,” *Environmental DNA* 5 (2023), 671–682; https://doi.org/10.1002/edn3.430.
