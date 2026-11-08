# Exact multistability chambers for competitive windmill networks

## Finding

**Theorem (complete hyperbolic-sink phase diagram).** Let \(k\ge 2\) be an integer. In a competitive Lotka–Volterra system on a friendship graph with one hub and \(k\) peripheral pairs, suppose the hub–leaf competition strength is \(\beta>0\) and the competition within each pair is \(\alpha>0\). Excluding the transition curves specified below, the entire family of locally asymptotically stable equilibria is classified by the following chambers.

For \(0<\alpha<1\), write \(b=(1+\alpha)/(2k)\). If \(0<\beta<b\), there is exactly **one** stable equilibrium: every species survives, with hub abundance
\[
h=\frac{1+\alpha-2k\beta}{1+\alpha-2k\beta^2},
\qquad y=\frac{1-\beta}{1+\alpha-2k\beta^2}
\]
at every leaf. If \(b<\beta<1\), the unique stable equilibrium has an extinct hub and every leaf at abundance \(1/(1+\alpha)\). If \(\beta>1\), this peripheral-only state and the hub-only state (hub abundance \(1\)) are exactly the **two** stable equilibria.

For \(\alpha>1\), write \(b=1/k\). If \(0<\beta<b\), there are exactly \(2^k\) stable equilibria: the hub coexists with exactly one selected survivor in each peripheral pair; the hub abundance and each selected-leaf abundance are
\[
h=\frac{1-k\beta}{1-k\beta^2},
\qquad y=\frac{1-\beta}{1-k\beta^2}.
\]
Each of the \(2^k\) independent within-pair choices defines one state. If \(b<\beta<1\), the exactly \(2^k\) stable equilibria have an extinct hub and exactly one leaf of abundance \(1\) in each pair. If \(\beta>1\), these states and the hub-only equilibrium are exactly the \(2^k+1\) stable equilibria.

All equilibria listed are hyperbolic sinks in the full \((2k+1)\)-dimensional system. No other equilibrium is locally asymptotically stable in the specified open chambers. The excluded transition sets are \(\alpha=1\), \(\beta=1\), and \(\beta=(1+\alpha)/(2k)\) when \(\alpha<1\), or \(\beta=1/k\) when \(\alpha>1\). No assertion is made on these sets.

## Assumptions and scope

The graph has vertices \(0,a_1,b_1,\ldots,a_k,b_k\), with \(0\) adjacent to every leaf and \(a_j\) adjacent to \(b_j\) for each \(j\), and no other edges. The nonnegative-orthant system is
\[
\dot x_i=x_i\left(1-\sum_j B_{ij}x_j\right),
\quad B_{ii}=1,\quad
B_{0,a_j}=B_{0,b_j}=\beta,\quad B_{a_j,b_j}=\alpha,
\]
where the matrix is symmetric and all unspecified off-diagonal entries vanish. Here \(x_i\ge0\), \(\alpha,\beta>0\), and asymptotic stability refers to the full nonnegative orthant, including possible introduction of absent species. The statement concerns equilibria, not their global basins or transient times.

## Proof

**1. A support criterion.** For an equilibrium \(x\) with positive support \(I\), the supported coordinates solve \(B_{II}x_I=\mathbf1\), and the linearization has block form with upper-left block \(-\operatorname{diag}(x_I)B_{II}\) and a diagonal lower-right block of invasion exponents \(g_j=1-\sum_{i\in I}B_{ji}x_i\) for \(j\notin I\). Since \(B\) is symmetric, \(-\operatorname{diag}(x_I)B_{II}\) is similar to \(-\operatorname{diag}(\sqrt{x_I})B_{II}\operatorname{diag}(\sqrt{x_I})\). A hyperbolic sink therefore requires and is ensured by \(B_{II}\) positive definite and every missing-species exponent strictly negative. An indefinite principal submatrix rules out an attractor. If \(B_{II}\) is singular, any equilibrium supported on \(I\) is part of a non-isolated local family of supported equilibria, or possesses a zero linear eigenvalue; in either case it cannot be asymptotically stable. The same applies to an absent species with zero exponent if the associated degeneracy could be attracting only nonhyperbolically: on the open parameter chambers considered below, the explicit support equations and signs exclude such cases.

**2. Entire peripheral pairs are forced when \(\alpha<1\).** If exactly one leaf of a pair is present, its absent partner has the identical external hub input and a smaller competition input than the survivor; its growth exponent is \((1-\alpha)y>0\). Thus every stable support contains both or neither leaves of each pair. If \(\alpha>1\), two leaves of one pair cannot both be supported because their principal \(2\times2\) interaction submatrix has eigenvalues \(1\pm\alpha\) and is indefinite. Hence at most one member of each pair survives.

**3. Hub absent.** If the hub is absent and a pair is empty, both species of that pair have invasion exponent \(1\), impossible for stability. Thus all pairs must be occupied: both leaves in each pair when \(\alpha<1\), or one when \(\alpha>1\). Their abundances are respectively \(1/(1+\alpha)\) and \(1\); their supported submatrix is positive definite. The hub invasion exponents are respectively \(1-2k\beta/(1+\alpha)\) and \(1-k\beta\). Missing within-pair partners in the latter case have exponent \(1-\alpha<0\). This proves the peripheral states and their sharp thresholds.

**4. Hub present, strong hub competition.** If \(\beta>1\), no leaf can coexist with the hub in a stable state because the principal hub–leaf submatrix has eigenvalues \(1\pm\beta\), one negative. The hub-only equilibrium is stable if and only if \(1-\beta<0\). For \(0<\beta<1\), the hub abundance is at most \(1\), so any empty peripheral pair would have invasion exponent \(1-\beta h>0\). Therefore every pair must be occupied, and the pattern of step 2 completely determines the supported set.

**5. Hub present, weak hub competition.** For \(\alpha<1\), all species are supported. Solving the identical leaf equations and the hub equation gives the stated \(h,y\). The full matrix has \(k\) antisymmetric within-pair eigenvalues \(1-\alpha>0\), \(k-1\) between-pair-sum eigenvalues \(1+\alpha>0\), and a residual hub/symmetric-leaf block whose determinant has the sign of \(1+\alpha-2k\beta^2\). Positivity of the explicit \(h,y\), together with positive definiteness, holds precisely when \(0<\beta<(1+\alpha)/(2k)\). To see the equivalence, note \((1+\alpha)/(2k)<1\) for \(k\ge2\), so throughout this interval both numerators and the denominator are strictly positive. Conversely, beyond this interval with \(\beta<1\) the hub numerator is negative or the solution does not have a positive-definite supported matrix.

For \(\alpha>1\), the supported set contains the hub and exactly one member of each pair. The support matrix is a \((k+1)\)-dimensional arrowhead with \(1\) on its diagonal and hub–leaf entries \(\beta\). It is positive definite exactly when \(1-k\beta^2>0\). Solving gives the stated \(h,y\). Both are positive exactly in the relevant positive-definite range when \(0<\beta<1/k\). Each excluded partner has invasion exponent \((1-\alpha)y<0\). The \(2^k\) independent choices are distinct. This covers all supports, so the classification and hyperbolicity assertions follow.

## Verification

The standalone Python 3 script `verify.py` independently constructs the full symmetric interaction matrix, enumerates every nonempty support, solves supported equilibrium equations over exact rational numbers, tests positive definiteness using exact arithmetic, checks all invasion exponents, and compares the resulting stable support sets with the theorem. It uses only the Python standard library. Run `python3 verify.py`. It successfully checked \(84\) complete support-census cases for \(k\in\{2,3,4\}\), \(\alpha\in\{1/2,2/3,3/2,2\}\), and multiple \(\beta\) choices away from the transition sets. These are finite verification tests, not an infinite proof; the support argument above covers all \(k\ge2\).

## Relationship to prior work

Meng, Horvát, Modes and Haas investigate how ecological interaction-network arrangements govern feasibility and stability, studying small network configurations and their general organization [1]. Hong and Pego establish general exclusion theorems, stability criteria and exponential multistability constructions [2]. In particular, their clique-related strong-rival regime already explains why exponentially many mutually exclusive peripheral choices are possible in principle; that phenomenon alone is **not** asserted as new. Fried, Kessler and Shnerb develop clique interpretations for ecological stable states [3,4]. The narrower result here is an explicit all-size, two-parameter **complete** chamber classification, including exact finite-strength hub-coexistence abundances, extinction thresholds and the addition of the isolated-hub attractor. These exact friendship-graph formulas were not identified in the inspected works; this does not establish global literature priority.

## Limitations

The classification excludes all nonhyperbolic transition curves and is for equal growth and self-competition, symmetric pair and hub couplings, and \(k\ge2\). It does not determine basin volumes, disturbance robustness, or equilibria at the excluded curves. No independent mathematical audit has been performed. An unindexed equivalent classification is possible. The proof uses standard support-stability criteria and special symmetry; no general novelty is claimed for those ingredients.

## References

1. Y. Meng, S. Horvát, C. D. Modes and P. A. Haas, *Impossible ecologies: Interaction networks and stability of coexistence in ecological communities*, arXiv:2309.16261 (first posted 2023-09-28), https://arxiv.org/abs/2309.16261.
2. W. E. Hong and R. L. Pego, *Exclusion and multiplicity for stable communities in Lotka–Volterra systems*, arXiv:2102.00611, https://arxiv.org/abs/2102.00611.
3. Y. Fried, D. A. Kessler and N. M. Shnerb, *Communities as cliques*, arXiv:1605.07479, https://arxiv.org/abs/1605.07479.
4. Y. Fried, N. M. Shnerb and D. A. Kessler, *Alternative steady states in random ecological networks*, arXiv:1703.00940, https://arxiv.org/abs/1703.00940.
5. M. Aguadé-Gorgorió et al., *A taxonomy of multiple stable states in complex ecological communities*, Ecology Letters (2024), https://doi.org/10.1111/ele.14413.
