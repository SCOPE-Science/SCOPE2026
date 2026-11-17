# Sharp mass-aware concavity law for variation stability of weighted isotonic regression

## Finding
Let \(n\ge2\), let \(\mu_1,\ldots,\mu_n>0\) be observation masses, and let \(w_1,\ldots,w_{n-1}>0\) be edge-variation weights. For real data \(x\in\mathbb R^n\), define weighted least-squares isotonic regression by
\[
\Pi_\mu(x)=\underset{y_1\le\cdots\le y_n}{\operatorname{argmin}}\ \sum_{i=1}^{n}\mu_i(x_i-y_i)^2,
\quad V_w(h)=\sum_{e=1}^{n-1}w_e|h_{e+1}-h_e|.
\]
Set \(s_0=0\), \(s_i=\sum_{r=1}^{i}\mu_r\), and adjoin \(w_0=w_n=0\). Let \(\widehat w\) be the least concave majorant, on \([0,s_n]\), of the points \((s_i,w_i)\), \(0\le i\le n\). Then the **sharp global two-input seminorm modulus** is
\[
\boxed{\operatorname{Lip}_{V_w}(\Pi_\mu)
=\max_{1\le e<n}\frac{\widehat w(s_e)}{w_e}
=\max\left\{1,\max_{\substack{1\le e<n\\0\le j<e<k\le n}}
\frac{(s_k-s_e)w_j+(s_e-s_j)w_k}{(s_k-s_j)w_e}\right\}.}
\]
Here the modulus is the supremum of \(V_w(\Pi_\mu(x)-\Pi_\mu(z))/V_w(x-z)\) over all pairs with positive denominator. **It is attained by a pair of real inputs for every admissible mass and weight profile.**

In particular, \(\Pi_\mu\) is two-input nonexpansive under \(V_w\) if and only if the mass-scaled edge-weight slopes decrease:
\[
\boxed{\frac{w_e-w_{e-1}}{\mu_e}\ \ge\ \frac{w_{e+1}-w_e}{\mu_{e+1}}\qquad(1\le e<n).}
\]
Thus concavity in cumulative observation mass, rather than uniformity of edge weights, is the exact stability criterion. A monotone upper-hull pass evaluates the constant in \(O(n)\) arithmetic operations.

## Assumptions and scope
All vectors and weights are real and finite-dimensional. The shape constraint is the total order \(y_1\le\dots\le y_n\), with observation masses \(\mu_i>0\) independently chosen from variation weights \(w_e>0\). The input and output seminorm is **edge** total variation, not the weighted least-squares metric, and constant vectors form its nullspace. Weighted isotonic regression is translation covariant, so the quotient seminorm modulus is well-defined. The endpoint values \(w_0=w_n=0\) are added for interpolation only and are not graph edges. Multiplying all edge weights by a common positive factor does not change the modulus.

## Proof
**1. Local averaging structure.** The unique weighted least-squares projection onto the monotone cone is continuous and piecewise linear. In a full-dimensional active-set chamber it averages the input on a partition into consecutive blocks, using masses \(\mu\). Write \(A_{\mathcal B}\) for the block-averaging matrix. A line segment meets finitely many chambers; integrating its local derivatives proves
\[
\operatorname{Lip}_{V_w}(\Pi_\mu)\le\max_{\mathcal B}\|A_{\mathcal B}\|_{V_w\to V_w}.
\]
This also follows directly by subdividing segments at the finitely many polyhedral walls. No differentiability assertion is needed at walls.

**2. Exact variation norm of a fixed partition.** The step vectors \(h^{(e)}_i=\mathbf1_{\{i>e\}}\), \(1\le e<n\), form a signed-step basis modulo constants. Because \(A_{\mathcal B}\) preserves constants, the triangle inequality gives, with equality possible on a single step,
\[
\|A_{\mathcal B}\|_{V_w\to V_w}
=\max_{1\le e<n}\frac{V_w(A_{\mathcal B}h^{(e)})}{w_e}.
\]
If the edge \(e\) is a boundary between two blocks, the image of the step is the same step, giving ratio \(1\). Otherwise the unique block crossing \(e\) is \([j+1,k]\) for some \(0\le j<e<k\le n\), and the step average in that block is
\[
\theta=\frac{s_k-s_e}{s_k-s_j}.
\]
The output step has variation only on the edges \(j\) and \(k\) bordering that block. Its variation is \(w_j\theta+w_k(1-\theta)\), with absent exterior edges accounted for by \(w_0=w_n=0\). Hence the ratio is precisely
\[
R_{j,e,k}=\frac{(s_k-s_e)w_j+(s_e-s_j)w_k}{(s_k-s_j)w_e}.
\]
Every local derivative therefore has norm bounded by the maximum claimed in the theorem.

**3. Every chord ratio is realized by an active block.** Fix \(0\le j<e<k\le n\), and put \(l=j+1\), \(r=k\). Choose the fitted vector \(y\) to be strictly increasing by unit steps outside \([l,r]\), with \(y_i=0\) on \([l,r]\); for example, \(y_i=i-l\) for \(i<l\) and \(y_i=i-r\) for \(i>r\). Set input \(x=y+\mu_l^{-1}\mathbf e_l-\mu_r^{-1}\mathbf e_r\). The weighted projection of \(x\) is \(y\): the Karush–Kuhn–Tucker multiplier for each of the active inequalities inside \([l,r]\) equals \(1\), and all other inequalities are strict. These strict inequalities and strictly positive multipliers persist under a sufficiently small perturbation. Consequently, for sufficiently small \(\varepsilon>0\),
\[
\Pi_\mu(x+\varepsilon h^{(e)})-\Pi_\mu(x)
=\varepsilon A_{[l,r]}h^{(e)},
\]
where \(A_{[l,r]}\) averages just the block \([l,r]\) and leaves all other coordinates unchanged. The variation ratio is **exactly** \(R_{j,e,k}\). If the maximum over chord ratios is at most one, take any two strictly increasing data vectors close enough to each other so that projection is the identity, obtaining ratio \(1\). Thus the displayed maximum is sharp and attained.

**4. Concave-majorant identity and characterization.** The value of the least concave majorant at \(s_e\) is the maximum of the original value \(w_e\) and the linear interpolations from pairs of sample positions strictly straddling \(s_e\). Indeed, its hypograph is the upper boundary of the convex hull of the finitely many planar points; an upper boundary point is a convex combination of at most two vertices with abscissas on opposite sides. This proves the first equality. The majorant coincides with all original edge weights exactly when the piecewise-linear interpolation through \((s_i,w_i)\) is concave. Its successive slopes are \((w_i-w_{i-1})/\mu_i\), proving the stated adjacent-slope criterion. Constructing the upper convex hull in increasing abscissa order, deleting middle points whenever successive slopes rise, requires \(O(n)\) operations. A second monotone traversal evaluates the majorant at all interior sample positions in another \(O(n)\) operations.

The result concerns **two-input** differences. One-input bounded variation monotonicity does not by itself establish such a perturbation bound.

## Verification
Run `python verify_weighted_isotonic.py` (Python standard library, no dependencies). The exact-rational checker enumerates all consecutive-block partitions for six graph orders \(n=2,3,4,5,6,7\), nine positive mass/edge-weight profile combinations for each order, and all their step directions. It compares the exact partition operator norm to the chord formula, verifies the mass-concavity criterion and the independently computed upper-hull formula, and checks \(1,134\) strictly pooled, explicitly constructed attaining local perturbations with exact rational arithmetic. It reports:

```
EXACT_ALL_BLOCK_PARTITION_NORMS_PASSED 54
EXACT_ALL_ACTIVE_BLOCK_WITNESSES_PASSED 1134
EXACT_MASS_AWARE_CONCAVITY_EQUIVALENCE_PASSED
LINEAR_TIME_LEAST_CONCAVE_MAJORANT_FORMULA_PASSED
ALL_WEIGHTED_ISOTONIC_VARIATION_CHECKS_PASSED
```

The unbounded family result is proved by the preceding arguments, not by finite computation. For illustration, \(n=3\), \(w=(1,5)\), and observation masses \(\mu=(1,1,1)\) give modulus \(5/2\); the same edge weights with \(\mu=(1,10,1)\) give modulus \(1\). Thus the observation masses genuinely alter nonexpansivity, and not just an estimator's computational implementation.

## Relationship to prior work
Yeganova–Wilbur (2009), Section 2, treats weighted PAV blocks and their means; it does not study the sharp two-input weighted edge-variation modulus. Henzi–Mösching–Dümbgen (2022), Section 2, analyzes weighted isotonic fits and coordinatewise changes, not this modulus. Yang–Barber (2017), Theorem 1 and Section 6, proves the necessary-and-sufficient neighbor-averaging criterion for **unweighted-observation Euclidean** isotonic projection and arbitrary seminorms. In particular the equal-mass qualitative concavity implication here can be derived from that theorem and is **not presented as new in isolation**. Neither their result nor the cited weighted PAV work supplies the joint arbitrary-observation-mass sharp constant, the entire attained chord law, or the corresponding mass-coordinate concave-majorant computation.

Published results on cycle-cover isotonic projection establish that weighted graph-variation contraction on a cycle requires **uniform** edge weights, while the present path theorem admits a full positive cone of concave nonuniform weights. Another result on \(\ell_p\) isotonic projections controls the \(\ell_p\)-to-\(\ell_p\) modulus and does not imply a weighted edge-variation norm. An accessible earlier tree-variation formula treats **unweighted** observation masses and edge variation; its path specialization is the constant \(1\), not the present independent-weight formula.

## Limitations
Only real finite chains, positive observation masses, positive edge-variation weights, and quadratic isotonic regression are considered. Arbitrary posets, multigraphs, other regression losses, and signed edge weights are outside scope. The upper-hull method measures the **global** Lipschitz constant, not the optimal local bound for a fixed dataset. The qualitative equal-mass case overlaps the general 2017 neighbor-averaging criterion. Earlier equivalent formulas may exist under different language, and the mathematical originality review is not an independent audit.

## References
1. L. Yeganova and W. J. Wilbur, *Isotonic Regression under Lipschitz Constraint*, *J. Optim. Theory Appl.* 141 (2009), 429–443; first publicly published January 7, 2009. DOI: 10.1007/s10957-008-9477-0. Full text: https://pmc.ncbi.nlm.nih.gov/articles/PMC5815842/.
2. J. de Leeuw, K. Hornik, and P. Mair, *Isotone Optimization in R: Pool-Adjacent-Violators Algorithm (PAVA) and Active Set Methods*, *J. Stat. Software* 32 (2009), article 5. DOI: 10.18637/jss.v032.i05.
3. F. Yang and R. F. Barber, *Contraction and uniform convergence of isotonic regression*, arXiv:1706.01852, first posted June 6, 2017. Full text: https://arxiv.org/html/1706.01852v3.
4. A. Henzi, A. Mösching, and L. Dümbgen, *Accelerating the Pool-Adjacent-Violators Algorithm for Isotonic Distributional Regression*, *Methodol. Comput. Appl. Probab.* 24 (2022), 2633–2645. DOI: 10.1007/s11009-022-09937-2.
5. *Cyclic-cover rigidity of weighted-variation stability for isotonic regression*, publicly available at https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-cyclic-cover-rigidity-of-weighted-variation-stability-for-isoton--c6a0693fe803.
6. *Sharp \(\ell_p\) isotonic regression stability on every finite partial order*, publicly available at https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-sharp-ell-p-isotonic-regression-stability-on-every-finite-partia--7bfc7f16ca62.
