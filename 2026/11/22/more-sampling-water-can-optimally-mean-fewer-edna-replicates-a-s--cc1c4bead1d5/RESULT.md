# More sampling water can optimally mean fewer eDNA replicates: a strict log-concavity and false-alarm theorem

## Finding

Consider a survey for a target species that is present in a study area, but whose environmental DNA occurs intermittently in independently sampled patches. Each grab has probability \(p\in(0,1)\) of encountering a DNA-bearing patch. Conditional on encountering one, target molecules are Poisson with mean \(\lambda(v-c)\), where \(v>c>0\) is the assigned water-volume resource and \(c\) is an unavoidable fixed processing loss per grab. A laboratory assay has independent false-positive probability \(f\in(0,1)\). The survey reports detection when **any** individual assay is positive.

For every total volume \(B>c\) and integer number of grabs \(1\le n<B/c\), equal allocation \(v_i=B/n\) uniquely maximizes the *Youden discrimination* between target-present and target-absent conditions. Its value is
\[
J_n(B)=(1-f)^n\left[1-\left(1-p+p e^{-\lambda(B/n-c)}\right)^n\right].
\]
The extension \(n\mapsto J_n(B)\) is strictly log-concave for real \(0<n<B/c\). Consequently, a strictly better score than the two adjacent integers certifies the **unique global integer optimum**, without an enumeration of all feasible sample counts.

**A sharp, certified non-nesting witness:** take \(p=4/5\), \(f=1/400\), \(c=1/50\), \(\lambda=1\). With \(B=8\), the unique optimum is **five** equal grabs; with the larger budget \(B=10\), it is **four** equal grabs. Exact rational Taylor enclosures prove all four needed strict adjacent comparisons. Thus increasing the total available water can *decrease* the uniquely optimal number of independent field replicates, even though every fixed-count design improves with more water.

For every \(p,f\in(0,1)\), \(\lambda,c>0\), the optimal number eventually stabilizes as \(B\to\infty\) at the exact finite integer
\[
 n_\infty=\max\left\{1,\left\lceil
 \frac{\log\!\left[f/(p+f(1-p))\right]}{\log(1-p)}
 \right\rceil\right\}.
\]
If the real quantity inside the ceiling is a positive integer \(k\), the limiting scores for \(k\) and \(k+1\) tie, but \(k\) is the unique finite-budget optimum for all sufficiently large \(B\). In the witness \(n_\infty=4\). In contrast, with \(f=0\) and \(c>0\) the optimum grows proportionally with \(B\); that no-false-alarm phenomenon is already covered by general renewal/encounter-allocation results and is not claimed here as new.

## Assumptions and scope

A fixed positive volume budget \(B\) is split among \(n\) *independently selected* field patches with positive usable volumes \(v_i-c\), \(v_i>c\) and \(\sum_i v_i=B\). Under target presence, each patch independently bears the target with probability \(p\); conditional on bearing the target, molecules detected by its assay follow a Poisson count of mean \(\lambda(v_i-c)\). Under target absence every grab contains no genuine target molecules. Regardless of presence, each assay produces an independent spurious positive with probability \(f\); a genuine target count or spurious result is sufficient for an assay positive. Independence is assumed across field grabs and false-positive events. Rates, occupancy probability and processing loss are known; the sampling plan is predetermined. The objective is the population Youden index (sensitivity plus specificity minus one), not solely sensitivity, prevalence-weighted utility, or inference precision.

The sample count is a positive integer and must obey \(nc<B\); zero-usable-volume grabs are never needed for an optimum. All inequalities are strict except at any explicitly discussed limiting tie. No estimation uncertainty, shared patch correlation, inhibition, dilution from pooling, upper filter-volume constraint, laboratory per-sample monetary ceiling or imperfect specificity dependence is modeled.

## Proof

**1. Exact objective.** Write \(q(v)=1-p+p e^{-\lambda(v-c)}\) and \(\alpha=1-f\). Under absence, the probability every assay reports negative is \(\alpha^n\). Under presence it is \(\alpha^n\prod_i q(v_i)\). Therefore the difference of positive-report probabilities is
\[
J=\alpha^n\left[1-\prod_{i=1}^n q(v_i)\right].
\]
Define \(g(v)=-\log q(v)>0\) for \(v>c\). Then \(J=\alpha^n[1-e^{-\sum_i g(v_i)}]\). Direct differentiation gives
\[
g'(v)=\frac{\lambda p e^{-\lambda(v-c)}}{1-p+p e^{-\lambda(v-c)}}>0,
\quad
g''(v)=-\frac{\lambda^2p(1-p)e^{-\lambda(v-c)}}{(1-p+p e^{-\lambda(v-c)})^2}<0.
\]
Strict Jensen concavity gives \(\sum_i g(v_i)\le n g(B/n)\), with equality exactly when all volumes equal. This proves both the formula and unique within-count allocation.

**2. Strict log-concavity across counts.** Extend \(n\) to a real argument in \((0,B/c)\), put \(v=B/n\), and set \(E(n)=n g(B/n)>0\). Then
\[
E''(n)=\frac{v^2}{n}g''(v)<0.
\]
The scalar map \(h(z)=\log(1-e^{-z})\), for \(z>0\), is strictly increasing and strictly concave, since \(h'(z)=1/(e^z-1)>0\) and \(h''(z)=-e^z/(e^z-1)^2<0\). Consequently
\[
\log J_n(B)=n\log\alpha+h(E(n))
\]
is strictly concave. For any interior integer \(n\), strict inequalities \(J_n>J_{n-1}\) and \(J_n>J_{n+1}\) imply \(J_n>J_j\) for every other feasible integer \(j\); the analogous one-sided conclusion holds at the feasible endpoints.

**3. Exact counterexample certificates.** In the stated rational example, the four relevant strict inequalities are
\[
J_5(8)>J_4(8),\quad J_5(8)>J_6(8),\quad
J_4(10)>J_3(10),\quad J_4(10)>J_5(10).
\]
They are proved by the standalone pure-Python checker \(\texttt{verify\_nonnesting.py}\), which uses **rational endpoints**, not floating-point rounding: for each positive rational argument \(x\), the positive Taylor sum \(S_N(x)=\sum_{j=0}^N x^j/j!\) and the geometric majorant
\[
S_N(x)<e^x<S_N(x)+\frac{x^{N+1}/(N+1)!}{1-x/(N+2)}
\]
apply when \(N+2>x\). Reciprocals enclose \(e^{-x}\), and monotonic rational powers enclose every \(J_n\). Using \(N=60\), the exact rational lower bounds on the four winning margins, evaluated only for readability, exceed respectively \(0.0003434316\), \(0.0011327059\), \(0.0044248467\), and \(0.0002921463\). They are each strictly positive **as fractions**, establishing the four inequalities; strict log-concavity then proves global optimality at the two budgets. No finite search is treated as a global proof.

**4. False-positive replication ceiling.** At each fixed \(n\), as \(B\to\infty\),
\[
J_n(B)\longrightarrow C_n=\alpha^n\left[1-(1-p)^n\right].
\]
Let \(\beta=1-p\). An exact adjacent difference is
\[
C_{n+1}-C_n=\alpha^n\bigl[(1-\alpha\beta)\beta^n-f\bigr].
\]
Since \(0<\beta<1\), this difference changes sign at most once, determining the unique maximizing integer \(n_\infty\), apart from a possible adjacent tie at integer logarithmic threshold. To justify passage from fixed \(n\) to the global finite-budget optimum, observe \(J_n(B)\le\alpha^n\), while \(J_1(B)\to\alpha p>0\). All sufficiently large \(n\) are therefore uniformly dominated when \(B\) is large, so only finitely many counts need be compared. The strict limiting winner persists. If the limit ties at \(k,k+1\), then their positive deficits below \(C_k=C_{k+1}\) are respectively of order \(e^{-\lambda B/k}\) and \(e^{-\lambda B/(k+1)}\), with positive coefficients; the latter decays more slowly. Thus \(k\) wins at every sufficiently large finite budget. This proves the formula, eventual stabilization, and the witness value \(n_\infty=4\).

## Verification

Run \(\texttt{python3 verify\_nonnesting.py}\) using the standard Python library. The script computes strict **exact-fraction** interval certificates for the four comparisons and checks the threshold formula, plus 3,900 randomized supplementary finite-design tests. The exact rational inequalities are sufficient for the explicit example; the analytic proof above, not the random tests, establishes the universal log-concavity and limiting integer formula. No imported experiment, unprovided data, or external numerical solver is required.

## Relationship to prior work

How and colleagues (2024) compare sampled volume and replication experimentally for fish eDNA and report that both design dimensions matter; their sampled combinations do not supply this exact fixed-loss, independent-patch, false-positive Youden model or its analytic count reversal. Davis and colleagues (2018) explicitly separate DNA availability from capture and laboratory detection, but study adaptive detection/occupancy under a different objective. Buxton and colleagues (2021) study false positives and replication for occupancy-inference bias and uncertainty, distinct from the population Youden objective here. Ficetola and colleagues (2015) analyze replicate false presences and false negatives and are a relevant qualitative predecessor; published exact statements were not verified to subsume this specific comparison.

The no-false-positive equal-visit allocation and ordinary budget staircase are **not new** as statements: they are covered by a more general independent-site exponential-encounter optimization. Similarly, a related mathematical finding establishes optimal allocations among Poisson monitoring modalities whose false-alarm intensities are proportional to effort; this does not specialize to a **fixed independent false-alarm probability per additional assay** with patchy DNA and per-grab volume loss. The contribution asserted here is the joint strict-log-concavity certificate, exact non-nesting under positive fixed false alarms, and the corresponding capped large-budget law, not a claim that Jensen's inequality or basic binomial testing is new.

## Limitations

This is an idealized *single-target*, single-report, expected-discrimination calculation. Independent patch availability and fixed false-positive probability across all assays can fail for real sampling; persistent DNA contamination can correlate both genuine and spurious signals. Youden discrimination gives equal marginal weight to sensitivity and specificity and need not match ecological costs. The exact numerical example uses dimensionless resource units and does not infer field-calibrated processing losses or assay false-alarm rates. The proof does not classify every finite-budget transition for every parameter choice; only strict log-concavity, a certified nonmonotonic witness, and eventual replication count are claimed. Scientific priority is subject to further literature assessment, particularly for generalized resource-allocation results not written in eDNA terminology.

## References

1. How, C. M., et al. (2024), *Refining Sampling Efforts for Fish Diversity Assessment in Subtropical Urban Estuarine and Oceanic Waters Using Environmental DNA With Multiple Primers*, Environmental DNA, DOI: https://doi.org/10.1002/edn3.70013 (first public 2024-09-18).
2. Davis, A. J., et al. (2018), *Accounting for observation processes across multiple levels of uncertainty improves inference of species distributions and guides adaptive sampling of environmental DNA*, Ecology and Evolution. https://doi.org/10.1002/ece3.4552.
3. Buxton, A. S., et al. (2021), *Optimising sampling and analysis protocols in environmental DNA studies*, Scientific Reports. https://doi.org/10.1038/s41598-021-91166-7.
4. Ficetola, G. F., et al. (2015), *Replication levels, false presences and the estimation of the presence/absence from eDNA metabarcoding data*, Molecular Ecology Resources. https://doi.org/10.1111/1755-0998.12338.
