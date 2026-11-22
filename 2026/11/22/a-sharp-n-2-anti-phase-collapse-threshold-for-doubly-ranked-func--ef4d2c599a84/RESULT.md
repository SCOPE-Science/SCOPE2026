# A sharp \(N^{-2}\) anti-phase collapse threshold for doubly ranked functional tests

## Finding

Fix two bounded continuous probability densities \(f,g\) on \(\mathbb R\), and write \(h=(f+g)/2\). For every even \(N=2n\), draw independent scalar observations \(X_1,\ldots,X_n\) with density \(f\), and \(X_{n+1},\ldots,X_N\) with density \(g\); draw independent standard Gaussians \(E_1,\ldots,E_N\), independent of the observations. Observe each subject at two times as
\[
\bigl(X_i,\,-X_i+\sigma_N E_i\bigr),\qquad \sigma_N>0,\quad \sigma_N\longrightarrow0.
\]
Let \(r_i,s_i\) be the pooled, increasing ranks at times one and two. The two subject-level summaries from the raw-rank version of the doubly ranked framework are
\[
A_i=\frac{r_i+s_i}{2},\qquad
U_i=\frac{u_N(r_i)+u_N(s_i)}2,\qquad
u_N(r)=\log\frac{r-1/2}{N-r+1/2}.
\]
Define the count of pair-order failures of exact anti-phase reversal,
\[
I_N=\sum_{1\le i<j\le N}
\mathbf 1\!\left\{(X_i-X_j)
\bigl[(X_i-\sigma_NE_i)-(X_j-\sigma_NE_j)\bigr]<0\right\}.
\]
With probability one at every finite \(N\), the following three events are identical:
\[
\{A_1=\cdots=A_N\}=\{U_1=\cdots=U_N\}=\{I_N=0\}.
\]
Put \(\Lambda(f,g)=\pi^{-1/2}\int_{\mathbb R}h(x)^2\,dx\). There is a sharp three-regime threshold:
\[
\Pr(I_N=0)\ \longrightarrow\
\begin{cases}
1,&N^2\sigma_N\to0,\\
\exp[-c\Lambda(f,g)],&N^2\sigma_N\to c\in(0,\infty),\\
0,&N^2\sigma_N\to\infty.
\end{cases}
\]
At the critical scale, the stronger conclusion is
\[
I_N\ \xrightarrow{\mathcal D}\ \mathrm{Poisson}\!\bigl(c\Lambda(f,g)\bigr).
\]
For the smooth fixed alternative \(f=\phi(\cdot+a)\), \(g=\phi(\cdot-a)\) with \(a>0\), \(\phi\) standard normal density, the exact critical intensity is
\[
c\Lambda(f,g)=\frac{c(1+e^{-a^2})}{4\pi}.
\]
In particular, at \(a=3\) and \(\sigma_N=4\pi/N^2\), both proposed subject summaries are *identical across all subjects* with limiting probability
\[
\exp[-(1+e^{-9})]=0.3678340440\ldots.
\]
Therefore any nonrandomized group-label test that uses only either summary vector and never rejects on constant input has limiting rejection probability at most \(1-\exp[-(1+e^{-9})]=0.6321659560\ldots\) against this fixed two-group alternative. In contrast, a test using the original first-time values is consistent, since the groups have means \(-3\) and \(+3\). This power ceiling applies only to the specified raw two-time rank aggregation and not to unrelated functional tests or versions with preprocessing that changes the pointwise ordering.

## Assumptions and scope

The densities \(f,g\) do not vary with \(N\); they are bounded, continuous and integrate to one. The group sizes are equal and independent. Gaussian errors are independent across subjects. Ranks are pooled across both groups at each time, with no preprocessing or random tie-breaking needed: continuous marginals give unique ranks almost surely. The noise satisfies \(\sigma_N\to0\). The group-label test consequence assumes deterministic non-rejection when its input scores are all identical, as in the ordinary nonrandomized permutation-rank test with tie-inclusive \(p\)-value one. No claim is made about randomization at complete ties.

## Proof

**Step 1: exact rank cancellation and its converse.** The transformation \(u_N\) is strictly increasing and satisfies \(u_N(N+1-r)=-u_N(r)\). Because each time-point rank vector is a permutation of \(1,\ldots,N\), \(\sum_i A_i=N(N+1)/2\) and \(\sum_i U_i=0\). If the \(A_i\)'s are all equal, each is \((N+1)/2\), forcing \(s_i=N+1-r_i\). If the \(U_i\)'s are all equal, each is zero, and strict monotonicity similarly forces \(s_i=N+1-r_i\). Conversely this complementary-rank relation makes both summaries constant. The second-time rank vector is the reversal of the rank vector of \(W_i=X_i-\sigma_N E_i\), so complementarity is equivalent to identical ordering of \((X_i)\) and \((W_i)\), or \(I_N=0\).

**Step 2: a rare-pair intensity.** For distinct \(i,j\) having respective densities \(p,q\in\{f,g\}\), let \(B_{ij}\) denote the pair-order inversion event in \(I_N\). With \(Z\sim N(0,2)\), conditioning on the scalar observations gives, as \(\sigma\downarrow0\),
\[
\Pr(B_{ij})=\frac{2\sigma}{\sqrt\pi}\int_{\mathbb R}p(x)q(x)\,dx+o(\sigma).
\]
Indeed, order the pair as \(x<x+d\) for \(d>0\), integrate the two density orientations against \(\Pr(Z>d/\sigma)\), set \(d=\sigma t\), and use boundedness, translation-continuity of density products in \(L^1\), and \(\int_0^\infty\Pr(Z>t)\,dt=\mathbb E Z_+=1/\sqrt\pi\). The remainder is uniform over the four possible density pairs. Summing \(\binom n2\) \(f\)-\(f\) pairs, \(n^2\) \(f\)-\(g\) pairs and \(\binom n2\) \(g\)-\(g\) pairs yields
\[
\mathbb EI_N=(N^2\sigma_N)\left(\frac1{\sqrt\pi}\int h^2+o(1)\right).
\]
This intensity is positive and finite.

**Step 3: dependent pairs do not create extra Poisson clusters at the critical scale.** Indicators \(B_{ij}\) and \(B_{k\ell}\) are independent for disjoint index sets. For any fixed connected graph with \(v\ge2\) vertices, requiring the inversion event on each graph edge implies that all \(v\) underlying scalar values lie within an interval of length at most \(\sigma_N\) times the sum of the absolute Gaussian mark differences along a spanning tree. Conditional on the marks and one scalar root, bounded densities give a probability at most \(C_v\sigma_N^{v-1}\); Gaussian moments make \(C_v\) finite. A fixed collection of \(k\) distinct pair-events whose graph has \(v\) vertices and \(b\) connected components consequently has joint probability \(O(\sigma_N^{v-b})\). At \(\sigma_N=c/N^2+o(N^{-2})\), the sum of contributions from such configurations is \(O(N^{2b-v})\), which vanishes whenever any component contains at least three vertices. The remaining configurations are \(k\) vertex-disjoint pairs, whose contributions tend to \((c\Lambda(f,g))^k\). Thus all fixed factorial moments of \(I_N\) converge to those of the stated Poisson law, proving the critical distribution and its zero atom.

**Step 4: the two outer regimes.** If \(N^2\sigma_N\to0\), Markov's inequality and Step 2 give \(\Pr(I_N>0)\to0\). If \(N^2\sigma_N\to\infty\) while \(\sigma_N\to0\), the same pair estimates give \(\mathbb EI_N\sim N^2\sigma_N\Lambda\to\infty\). For overlapping pairs the two inversion events force three scalar values into a Gaussian-mark-determined interval of length \(O(\sigma_N)\), hence their joint probability is \(O(\sigma_N^2)\). It follows that
\[
\operatorname{Var}(I_N)\le \mathbb EI_N+C N^3\sigma_N^2,
\]
so \(\operatorname{Var}(I_N)/(\mathbb EI_N)^2\to0\). Chebyshev's inequality gives \(\Pr(I_N=0)\to0\).

**Step 5: Gaussian coefficient and testing implication.** Completing the square gives \(\int\phi(x-a)^2\,dx=1/(2\sqrt\pi)\) and \(\int\phi(x-a)\phi(x+a)\,dx=e^{-a^2}/(2\sqrt\pi)\). Therefore \(\Lambda=[1+e^{-a^2}]/(4\pi)\). On the all-equal-score event a nonrandomized test satisfying the specified rule cannot reject; hence its power is at most \(1-\Pr(I_N=0)\). Under the Gaussian two-group alternative, the sample difference of first-time means converges in probability to \(2a>0\), showing that the underlying group distinction itself is consistently detectable.

## Verification

Run `python verify.py` using the Python standard library. The code exhaustively checks the rank-complementarity identity for all second-time permutations through five subjects, checks independent random finite configurations, independently integrates the Gaussian overlap, and illustrates the critical zero-inversion probability at four increasing sample sizes. All 457 checks passed. Simulation confirms plausibility but is not used to prove the Poisson limit; the factorial-moment and variance arguments above are the infinite-sample proof.

## Relationship to prior work

Meyer's 2023 doubly ranked functional-data framework defines precisely the two raw pointwise-rank summaries analyzed here, but does not analyze anti-phase cancellation or the joint growing-sample, vanishing-noise threshold. Jeong, Dytso and Cardone (2021) derive exact formulas for recovering a noisy ordering and the leading *fixed-dimension* small-Gaussian-noise error slope, including quadratic dimension dependence; their sequential limit does not by itself give the finite, positive Poisson crossing mass when dimension and inverse noise co-vary. Classical Poisson theorems for small-distance U-statistics explain the rare-pair mechanism; after marking they may supply an alternative proof of the Poisson component. The asserted contribution is the joint exact characterization and crossover probability for **both specific functional rank summaries**, together with its inference consequence, rather than a claim to have invented Poisson approximation or rank anti-symmetry.

## Limitations

This is a sharply specified adverse measurement geometry, not a general power theorem. The asymptotic collapse probability is not the test's exact rejection probability. The paper's optional smoothing/preprocessing may change the order relations; no assertion is made for those variants. Equal time-point weights and two measurement times are essential to the displayed identity. Some classical Poisson approximation tools give broader coverage of the rare-event portion, and independent historical-priority review remains necessary. Ordinary Gaussian approximation with complete score ties may be undefined in particular software; the testing consequence is explicitly for procedures that do not reject constant score vectors.

## References

1. M. J. Meyer, *Doubly ranked tests of location for grouped functional data* (first public version 2023-06-26), https://arxiv.org/abs/2306.14761.
2. M. Jeong, A. Dytso and M. Cardone, *Retrieving Data Permutations from Noisy Observations: High and Low Noise Asymptotics* (2021-05-07), https://arxiv.org/abs/2105.03015.
3. B. Silverman and T. Brown, *Short distances, flat triangles and Poisson limits*, Journal of Applied Probability 15 (1978), 815–825, https://www.cambridge.org/core/journals/journal-of-applied-probability/article/abs/short-distances-flat-triangles-and-poisson-limits/A053AD5D9363B62A654350283A295A00.
4. L. Decreusefond, M. Schulte and C. Thäle, *Functional Poisson approximation in Kantorovich-Rubinstein distance with applications to U-statistics and stochastic geometry* (first public version 2014-06-20), https://arxiv.org/abs/1406.5484.
