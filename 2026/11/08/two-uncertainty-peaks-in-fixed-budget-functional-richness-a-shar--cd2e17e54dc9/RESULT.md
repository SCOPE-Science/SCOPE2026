# Two uncertainty peaks in fixed-budget functional richness: a sharp 13-species boundary

## Finding

In the fixed-budget random-extinction model of disjoint ecological functional groups, let \(F_k\) be the number of groups with at least one survivor when exactly \(k\) of \(S\) species survive uniformly without replacement, and set \(V_k=\operatorname{Var}(F_k)\). A finite sequence is *unimodal* when it is nondecreasing until some index and nonincreasing thereafter, allowing equal adjacent values.

**Theorem.** For every positive-integer functional-group size profile of total size \(S\le 12\), the sequence \((V_0,\ldots,V_S)\) is unimodal. Among all profiles of total size \(S=13\), the unique non-unimodal profile up to permutation is \((1,6,6)\). For that profile, the sequence has strict local maxima at \(k=3\) and \(k=6\), separated by a strict local minimum at \(k=5\). More strongly, every profile \((1,m,m)\) with integer \(m\ge6\) has a non-unimodal variance sequence.

This identifies the first community size for which the uncertainty in *how many functions survive* can fall and then rise again as a fixed number of species are retained. It is a statement about the conditional finite-population variance, not a claim about variance estimators for an unknown underlying community or independent Bernoulli extinctions.

## Assumptions and scope

There are \(g\ge1\) nonempty, pairwise-disjoint functional groups of integer sizes \(a_1,\ldots,a_g\) with \(S=\sum_i a_i\). Every species belongs to exactly one group; a function survives if and only if at least one member survives. For each integer \(k\in\{0,\ldots,S\}\), a \(k\)-element subset of the \(S\) species is selected uniformly. All claims quantify over every such group profile (and, for the infinite family, every integer \(m\ge6\)). Group names have no effect, so profiles are nondecreasing integer partitions.

## Proof

**1. Exact variance identity.** Adopt \(\binom{r}{k}=0\) for \(k>r\) or \(k<0\) with \(r\ge0\). Write

\[
q_i(k)=\frac{\binom{S-a_i}{k}}{\binom{S}{k}},\qquad
q_{ij}(k)=\frac{\binom{S-a_i-a_j}{k}}{\binom{S}{k}}.
\]

The indicator that group \(i\) is wholly absent has mean \(q_i\), and two such indicators have joint mean \(q_{ij}\). Since \(F_k\) is the number of groups minus the number absent, the following identity is exact for all \(k\), including \(k=0,S\):

\[
\tag{1}
V_k=\sum_i q_i(k)(1-q_i(k))
+2\sum_{i<j}\bigl(q_{ij}(k)-q_i(k)q_j(k)\bigr).
\]

**2. The first non-unimodal profile is of size 13.** For each integer \(S\in\{2,\ldots,12\}\), the executable finite proof in `verify.py` generates every nondecreasing positive-integer partition exactly once, computes (1) in reduced rational arithmetic at every \(k=0,\ldots,S\), deletes zero adjacent differences and tests whether a negative difference is followed by a positive one. This test is equivalent to failure of unimodality. There are exactly 259 partitions having at least two groups over these eleven values of \(S\), and none fails. Single-group and \(S=1\) cases have identically zero variance. At \(S=13\), all 100 partitions with at least two groups are tested, and exactly \((1,6,6)\) fails. The partition recursion selects a smallest part \(a\ge\text{lower}\), then recurses on \(S-a\) with new lower bound \(a\); it is exhaustive and produces no duplicate. All divisions use exact integers and rational numbers. Thus the finite verification covers all profiles, not merely a selection of examples.

For \((1,6,6)\), direct subset enumeration independently confirms

\[
\begin{array}{c|ccccc}
k&3&4&5&6&7\\\hline
V_k&5430/20449&5106/20449&45410/184041&184157/736164&183017/736164
\end{array}
\]

so \(V_2<V_3>V_4>V_5<V_6>V_7\). The sequence has two separated strict local peaks.

**3. An infinite family of two-peak profiles.** Set \(S=2m+1\), take the three group sizes \((1,m,m)\) and consider \(k\ge2\). Let

\[
u_k=\frac{S-k}{S},\quad
b_k=\frac{\binom{m+1}{k}}{\binom{S}{k}},\quad
c_k=\frac{\binom{m}{k}}{\binom{S}{k}}.
\]

The absence probabilities are \(u_k,b_k,b_k\). The singleton and each large group are simultaneously absent with probability \(c_k\); the two large groups cannot both be absent when \(k\ge2\). Substitution in (1) gives

\[
\tag{2}
V_k=u_k(1-u_k)+2b_k-4b_k^2+4c_k-4u_k b_k.
\]

Simplifying (2) at \(k=3,4\) yields

\[
\tag{3}
V_3-V_4=\frac{5m^4-42m^3+123m^2-94m+24}{4(2m-1)^2(2m+1)^2}.
\]

With \(t=m-6\ge0\), the numerator becomes \(5t^4+78t^3+447t^2+1166t+1296>0\). Hence \(V_3>V_4\) for every \(m\ge6\).

Put \(T_m=\binom{2m+1}{m}\). Formula (2) at the consecutive sample sizes \(m-1,m\) gives

\[
\tag{4}
V_m-V_{m-1}=\frac{2T_m^2-(10m^3+15m^2+5m)T_m+Q(m)}{T_m^2(2m+1)^2},
\]

where \(Q(m)=4m^6+28m^5+61m^4+58m^3+25m^2+4m>0\). Let \(H(m)=(10m^3+15m^2+5m)/2\). We have \(T_6=1716>H(6)=1365\), while

\[
\frac{T_{m+1}}{T_m}=4-\frac2{m+2}>3,
\qquad
\frac{H(m+1)}{H(m)}\le\left(1+\frac1m\right)^3<2
\quad(m\ge6).
\]

The second inequality follows term-by-term from the positive coefficients of the degree-three polynomial \(H\). Induction gives \(T_m>H(m)\) for all integers \(m\ge6\), so the first two terms of the numerator in (4) already have a positive sum, and \(V_m>V_{m-1}\).

A sequence which decreases from index \(3\) to \(4\) and increases from index \(m-1\) to \(m\), with \(m-1\ge5\), cannot be unimodal. This proves the infinite-family assertion. The proof does not assert there are exactly two peaks in every member of that family.

## Verification

Run `python3 verify.py` with Python 3 and no nonstandard dependencies. It calculates the exact conditional variance using (1), checks every one of the 259 relevant integer partitions through \(S=12\), and classifies all 100 with at least two groups at \(S=13\). An independent direct enumeration of survivor subsets checks the entire 13-species witness curve and 438 further profile/budget cases through \(S=8\). The checker also tests the algebraic identities in (3) and (4) and their signs for \(6\le m\le100\). The bound for arbitrary \(m\), which cannot follow from finitely many checks, is proved above by induction.

## Relationship to prior work

Heck, van Belle and Simberloff (1975) gave the classical exact rarefaction mean/variance framework. Fonseca and Ganade (first public 2001) explicitly applied fixed-count rarefaction to surviving ecological functional groups, quoting the Heck variance and describing variance as low near both endpoints and high at intermediate attrition. Those general formulas correctly compute every variance here; the present contribution is **not** rediscovery of the formula. It is the sharp global finite-size classification of failure of unimodality, uniqueness of the first exceptional profile, and an analytic infinite family displaying two separated variance peaks. The inspected full text of Fonseca and Ganade does not state these properties. Bogachev, Gnedin and Yakubovich (2006) study asymptotic variance in an infinite, independently sampled occupancy scheme, rather than uniform fixed-count subsampling of a finite group partition.

## Limitations

The ecological interpretation assumes exchangeable survival conditional on a fixed total, disjoint guild membership, and an all-or-nothing one-member functional criterion. Species identity, dependence not induced by fixed-count sampling, unequal survival probabilities and ecological interactions are excluded. The minimality proof is a finite exhaustive computation with auditable exact source code, not an analytic enumeration-free classification. The 1975 Heck paper's primary full text could not be obtained in this research pass; its known abstract and the explicit use of its formula in the accessible 2001 paper leave a historical-priority risk for the exact shape classification. This does not establish novelty in every published source. No empirical ecological data are analyzed.

## References

1. Heck, K. L., van Belle, G., and Simberloff, D. (1975). *Explicit Calculation of the Rarefaction Diversity Measurement and the Determination of Sufficient Sample Size*. Ecology 56, 1459–1461. https://doi.org/10.2307/1934716 (first published 1975-10-01).
2. Fonseca, C. R. and Ganade, G. (2001). *Species functional redundancy, random extinctions and the stability of ecosystems*. Journal of Ecology 89, 118–125. https://doi.org/10.1046/j.1365-2745.2001.00528.x (first published 2001-12-21).
3. Bogachev, L. V., Gnedin, A. V. and Yakubovich, Y. V. (2006). *On the variance of the number of occupied boxes*. https://arxiv.org/abs/math/0609498 (first submitted 2006-09-18).
