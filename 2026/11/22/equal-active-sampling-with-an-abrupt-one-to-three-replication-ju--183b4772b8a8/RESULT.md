# Equal-active sampling with an abrupt one-to-three replication jump for two-target detection

## Finding
Consider a fixed effort budget allocated among independently viable biological samples, where the goal is to detect **both** of two present taxa at least once. Under the assumptions below, every optimal allocation uses exactly \(k\) equally sized positive samples and leaves all other possible samples unused, for some integer \(1\le k\le n\). The exact optimal success probability is therefore
\[
\max_{1\le k\le n}\left\{1-2(1-p+p e^{-\lambda B/k})^k+(1-p+p e^{-2\lambda B/k})^k\right\}.
\]
This reduction does **not** imply that active sample counts rise one at a time: for three available samples, independent sample viability \(p=4/5\) and budget \(B_*=3\log 3/(2\lambda)\), exactly the one-sample and three-sample allocations tie for global optimality, and every two-sample allocation is strictly suboptimal. The unique optimal support size jumps directly from one to three as the budget increases through \(B_*\), within a nonzero interval around that point.

## Assumptions and scope
Fix an integer \(n\ge1\), a strictly positive effort budget \(B\), a shared viability probability \(0<p<1\), and a common strictly positive capture intensity \(\lambda\). Two target taxa are known to be present. Allocate efforts \(x_1,\ldots,x_n\ge0\) with \(\sum_i x_i=B\). Each biological sample has an independent Bernoulli viability flag \(G_i\), with \(\Pr(G_i=1)=p\), independent of the effort allocated to that sample. A failed sample contributes no detectable copies of either taxon. Conditional on all viability flags, counts of each taxon in each viable sample are mutually independent Poisson variables with mean \(\lambda x_i\); failed samples contribute zero counts.

The objective is the probability that **each** of the two taxa is detected at least once in the union of the independently assayed samples. This is a union of records from separate assays, not laboratory mixing before amplification or sequencing. The cost model charges only effort \(\sum_i x_i\) and imposes no fixed cost per opened sample. The two taxa have equal per-effort capture intensity and share each sample's all-or-nothing viability, but their Poisson counts are conditionally independent. No assumption is made about detecting two taxa in the same bottle.

## Proof
**1. Exact probability.** Define total viable effort \(S=\sum_iG_i x_i\). Conditional on \(S\), each taxon has a Poisson total count with mean \(\lambda S\), and conditional independence gives
\[
f(S)=\Pr(\text{both taxa detected}\mid S)=(1-e^{-\lambda S})^2.
\]
Independence of viability flags yields
\[
F(x)=\mathbb E f(S)=1-2\prod_{i=1}^n(1-p+p e^{-\lambda x_i})+\prod_{i=1}^n(1-p+p e^{-2\lambda x_i}). \tag{1}
\]
The continuous function \(F\) achieves its maximum on the compact effort simplex.

**2. All positive allocations are equal at any maximum.** Suppose an optimizer contains two strictly positive and unequal allocations \(x\ne y\). Hold the other allocations and their independent viability flags fixed in distribution, set \(T=x+y>0\) and \(R=\sum_{i\ne a,b}G_i x_i\). Conditioning on the two selected viability flags shows that the only split-dependent part of \(\mathbb Ef(R+G_a x+G_b y)\) is
\[
p(1-p)\,\mathbb E[f(R+x)+f(R+y)].
\]
Let \(u=e^{-\lambda x}\), \(v=e^{-\lambda y}\), \(r=e^{-\lambda T}=uv\), \(A=\mathbb E e^{-\lambda R}>0\), and \(C=\mathbb E e^{-2\lambda R}>0\). The split-dependent expectation equals
\[
2-2A(u+v)+C\bigl((u+v)^2-2r\bigr).
\]
Writing \(s=u+v\), this is **strictly convex** in \(s\), because its quadratic coefficient is \(C>0\). As \((x,y)\) varies with fixed sum \(T\), \(s\) spans \([2\sqrt r,1+r]\); the lower endpoint corresponds to equal split \(x=y=T/2\) and the upper endpoint to a boundary split \((0,T)\) or \((T,0)\). Both-positive unequal allocations yield \(2\sqrt r<s<1+r\) and therefore a strictly smaller value than at least one endpoint. This contradicts global optimality, since \(p(1-p)>0\). Hence *every* global optimum has \(k\) equal strictly positive entries \(B/k\) and \(n-k\) zeros. Inserting these into (1) proves the finite maximum formula in the Finding.

**3. Explicit three-sample jump.** Set \(n=3\), \(p=4/5\), and \(z=e^{-\lambda B/6}\in(0,1)\). Define the score for exactly \(k\) equally used samples by \(F_k(B)\). Exact polynomial expansion gives
\[
F_3-F_1=-\frac{12}{125}(z-1)^2(z+1)^2(3z^4-1)(z^4+2z^2+2). \tag{2}
\]
The only interior budget at which these two scores agree is \(B_*=3\log 3/(2\lambda)\), for which \(z_*=3^{-1/4}\). Equation (2) shows \(F_1>F_3\) on the lower-budget side and \(F_3>F_1\) on the higher-budget side. Direct exact reduction modulo \(3z^4-1\) yields
\[
F_3(B_*)-F_2(B_*)=\frac8{675}\bigl(54z_*^3-18z_*^2-13\bigr)>0. \tag{3}
\]
For the last strict inequality, \(z_*>759/1000\), since \(3(759/1000)^4<1\). The cubic \(h(z)=54z^3-18z^2-13\) has derivative \(h'(z)=162z^2-36z>0\) for \(z>2/9\), and \(h(759/1000)>0\) by rational arithmetic. Thus, at the crossing, the two-sample score is strictly below both tied maxima. Continuity yields some \(\varepsilon>0\) such that \(k=1\) is the only optimal active sample count for \(B_* -\varepsilon<B<B_*\), \(k=3\) is the only optimal active count for \(B_*<B<B_*+\varepsilon\), and only the \(k=1,3\) patterns tie at \(B=B_*\). All claims are global because part 2 excludes all unequal positive allocations.

## Verification
The standalone standard-library script `check.py` verifies the polynomial factorization (2), the exact algebraic reduction (3), and both rational inequalities. It independently enumerates all sample viability patterns for \(k=1,2,3\) at 27 exact rational test configurations and checks numerical budget points on either side of \(B_*\). Run `python3 check.py` from the extracted package directory. These computations supplement rather than replace the analytic all-parameter proof.

## Relationship to prior work
Courtaillac et al. (2024) empirically compare biological replication and pre-PCR pooling for kelp-forest environmental-DNA communities; they do not give this exact joint two-target, randomly failing-bottle optimization theorem. Moore and McCarthy (2016) optimize ecological survey effort with stochastic detectability, primarily using detection of one species and additive allocation across sites; their aims and stochastic structure differ. Srivastava and Bullo (2013), Corollary 5, already establish equal positive allocations for an **additive sum** of identical sigmoid utilities. That result covers the analogous simpler separable problem, but does not imply the present coupled two-taxon objective or its exact skipped-support transition, because the probability that both taxa appear after *any* bottle creates cross-sample multiplicative terms in (1).

The contrast with separately published independent-Hill inhibitory-allocation results, where active counts pass through intermediate values, should not be read as a universal impossibility for separable objectives: this finding concerns only the explicitly defined nonseparable joint-detection probability. No historical novelty or independence certificate is asserted.

## Limitations
Exactly two present taxa, identical Poisson rates, a common all-or-nothing viability event per bottle, independent bottles, known \(p\) and \(\lambda\), and no fixed per-bottle cost are essential to the stated proof. The theorem does not account for inhibition, sequencing-depth competition, PCR pooling, false positives, correlated sample failure, unequal species rates, or field estimation uncertainty. The three-sample result identifies a local abrupt support-size transition near \(B_*\); it does not assert that two samples are never optimal at other budgets. It is a design theorem under assumed probabilities, not an empirical or clinical recommendation. Historical priority is provisional, and independent external validation has not been performed.

## References
- Courtaillac, K.-L., Landschoff, J., Hull, K. and von der Heyden, S. (2024). *The Effect of Spatio-Temporal Sampling and Biological Replication on the Detection of Kelp Forest Fish Communities Using eDNA Metabarcoding*. *Environmental DNA*. First published 14 October 2024. https://doi.org/10.1002/edn3.70023
- Moore, A. L. and McCarthy, M. A. (2016). *Optimizing ecological survey effort over space and time*. *Methods in Ecology and Evolution*. https://doi.org/10.1111/2041-210X.12564
- Srivastava, V. and Bullo, F. (2013). *Knapsack Problems with Sigmoid Utilities: Approximation Algorithms via Hybrid Optimization*, Corollary 5. https://www.egr.msu.edu/~vaibhav/papers/2012d-sb.pdf
- Sato et al. (2017). A study comparing detection by individual versus pooled environmental-DNA samples. https://doi.org/10.1038/s41598-017-14978-6
