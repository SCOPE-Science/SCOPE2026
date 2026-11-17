# Gini-metric amplification by weighted isotonic regression

## Finding

For every integer \(n\ge2\) and positive observation masses \(\mu_1,\ldots,\mu_n\), let \(\Pi_\mu:\mathbb R^n\to\mathbb R^n\) minimize \(\sum_{i=1}^n\mu_i(y_i-x_i)^2\) over \(y_1\le\cdots\le y_n\). Define the unweighted complete-graph Gini seminorm
\[
G_n(h)=\sum_{1\le i<j\le n}|h_i-h_j|,
\qquad
L_n(\mu)=\sup_{G_n(x-y)>0}\frac{G_n(\Pi_\mu x-\Pi_\mu y)}{G_n(x-y)}.
\]

The exact fixed-mass modulus admits a finite, explicit partition-and-cut formula. For any partition \(\mathcal P\) of \(\{1,\dots,n\}\) into nonempty consecutive blocks and any nonempty proper subset \(S\), put \(p_B(S)=\sum_{i\in B\cap S}\mu_i/\sum_{i\in B}\mu_i\). Then
\[
\boxed{L_n(\mu)=\max_{\mathcal P}\max_{\varnothing\ne S\subsetneq[n]}
\frac{\sum_{\{B,C\}\subset\mathcal P}|B|\,|C|\,|p_B(S)-p_C(S)|}{|S|(n-|S|)}.}
\]
The formula is finite for all positive masses and requires no optimization over real input data. It uses at most \(2^{n-1}(2^n-2)\) explicitly rational candidates for rational masses. Each maximizing candidate corresponds to arbitrarily close input pairs in a locally stable pooling regime.

Across **all** positive mass vectors, the optimal dimension-only bound is
\[
\boxed{\sup_{\mu_i>0}L_n(\mu)=C_n:=\frac{\lfloor n^2/4\rfloor}{n-1}.}
\]
For \(n\ge4\), every fixed positive mass vector satisfies \(L_n(\mu)<C_n\), but the bound is approached by concentrating mass on one coordinate of a contiguous block of \(\lfloor n/2\rfloor\) observations. Thus the worst amplification grows as \(n/4+O(1)\). In contrast, equal observation masses always give \(L_n(\mu)=1\). For \(n=2,3\), every positive mass vector also gives \(L_n(\mu)=1\).

At the first dimension where amplification is possible, there is an exact closed classification:
\[
\boxed{L_4(\mu)=\max\left\{1,\frac43\max_{1\le i\le3}\frac{\max(\mu_i,\mu_{i+1})}{\mu_i+\mu_{i+1}}\right\}.}
\]
Consequently four-observation weighted isotonic regression is Gini-nonexpansive if and only if every adjacent mass ratio is at most three, in either direction. For example, masses \((4,1,1,1)\) give \(L_4=16/15\).

## Assumptions and scope

All signals are real, all masses are fixed strictly positive numbers, and isotonic inequalities are imposed along the total order \(1<\cdots<n\). The fitted sequence minimizes a **weighted quadratic** objective; the perturbation seminorm is deliberately **unweighted** Gini mean difference, not the quadratic objective norm, not a path variation seminorm, and not a comparison between fitted and unfitted individual Gini values. Translation by constants does not change any quotient.

## Proof

**1. Locally attainable averaging branches.** Standard weighted pool-adjacent-violators geometry makes \(\Pi_\mu\) continuous and piecewise linear. On the interior of any stable consecutive-block pooling regime \(\mathcal P\), its derivative is the linear block-averaging matrix \(P_\mathcal P\), where
\[
(P_\mathcal P h)_i=\frac{\sum_{j\in B}\mu_j h_j}{\mu(B)}\quad(i\in B),
\qquad\mu(B)=\sum_{j\in B}\mu_j.
\]
Every consecutive-block partition occurs on a nonempty open set: choose input values strictly decreasing inside each prescribed block and keep each later block at a much higher level than its predecessor. The weighted mean of any earlier subblock is then strictly larger than that of any later subblock, so each prescribed block pools completely, while distinct prescribed blocks remain separated. Strict inequalities persist under sufficiently small input perturbations. Hence the global quotient Lipschitz constant equals the largest \(G_n\)-operator seminorm among these finitely many matrices. The upper direction follows by subdividing the segment joining two inputs at the finitely many linear regimes; the lower direction follows from a small perturbation inside an open regime.

**2. Coarea reduction to cuts.** For any constant-preserving real matrix \(P\), any \(h\in\mathbb R^n\), and any \(a=\min_i h_i\), the finite coarea decomposition is
\[
h=a\mathbf1+\int_a^{\max h}\mathbf1_{\{i:h_i>t\}}\,dt,
\quad
G_n(h)=\int_a^{\max h}|S_t|(n-|S_t|)\,dt.
\]
The triangle inequality and \(P\mathbf1=\mathbf1\) imply
\[
\frac{G_n(Ph)}{G_n(h)}\le
\max_{\varnothing\ne S\subsetneq[n]}\frac{G_n(P\mathbf1_S)}{|S|(n-|S|)}.
\]
The reverse inequality follows by taking \(h=\mathbf1_S\). For a block matrix, \(P_\mathcal P\mathbf1_S\) is constant with value \(p_B(S)\) on each block. Summing its interblock pairwise differences proves the displayed exact fixed-mass formula. Its maximizers are locally realizable by Step 1.

**3. Universal sharp envelope.** Every block matrix has nonnegative rows of sum one. Therefore \(P_\mathcal P\mathbf1_S\in[0,1]^n\). The maximum over \([0,1]^n\) of \(G_n\) is exactly \(\lfloor n^2/4\rfloor\): since \(G_n\) is convex in each coordinate, its maximum occurs at a binary corner, and a corner with \(k\) ones has value \(k(n-k)\). Meanwhile \(|S|(n-|S|)\ge n-1\). Step 2 gives \(L_n(\mu)\le C_n\).

For sharpness, put \(k=\lfloor n/2\rfloor\), choose the first \(k\) observations as a pooled block, choose all other blocks singleton, and set the first mass to \(M\) and the other masses to one. At the binary perturbation \(h=e_1\), the ratio of output to input Gini variation is exactly
\[
\frac{k(n-k)}{n-1}\frac{M}{M+k-1}.
\]
This is witnessed by arbitrarily close pairs in the indicated pooling regime. Letting \(M\to\infty\) gives \(C_n\), with an exact positive deficit of \(C_n(k-1)/(M+k-1)\). The dimension envelope therefore cannot be improved.

For \(n\ge4\) the bound is never attained at finite positive masses. Indeed, a cut of size \(2\) through \(n-2\) has denominator at least \(2(n-2)>n-1\), so its ratio is strictly below \(C_n\). A singleton cut \(e_r\) has output \(q\mathbf1_B\), with \(q=\mu_r/\mu(B)\). If \(|B|=1\), its Gini value is \(n-1<\lfloor n^2/4\rfloor\); if \(|B|\ge2\), then \(0<q<1\) and \(G_n(q\mathbf1_B)=q|B|(n-|B|)<\lfloor n^2/4\rfloor\). A complementary singleton cut has the same output Gini value. There are finitely many branches and cuts, so their maximum is strictly below \(C_n\).

**4. Equal masses and the small-dimensional boundary.** If all masses are equal, every block matrix is doubly stochastic. By its decomposition into permutation matrices and convexity plus permutation invariance of \(G_n\), it is Gini-nonexpansive. A strictly increasing input lies in an identity branch, so the sharp constant is one. The universal bound gives the same value automatically for \(n=2,3\).

For \(n=4\), every binary cut with two ones has denominator four, while its output Gini is at most four; these cuts cannot amplify. A singleton cut at coordinate \(r\) inside a block of size \(k\) yields ratio \(k(4-k)\mu_r/[3\mu(B)]\). A singleton block gives one; a three-observation block gives at most one; a four-observation block gives zero. Only two-observation adjacent blocks can produce amplification, with factor \(4\mu_r/[3(\mu_i+\mu_{i+1})]\). Every adjacent pair is realizable as its own pooled block. This proves the exact formula and the mass-ratio-three criterion.

## Verification

The accompanying standalone standard-library Python program `verify_weighted_isotonic_gini.py` performs exact rational checks of the finite partition-and-cut formula, the four-point closed formula on 256 mass configurations, strict universal bounds on further rational data, limiting dominant-mass witness identities, and an independent rational implementation of pool-adjacent-violators regression producing arbitrarily small two-input witnesses. It prints `ALL_WEIGHTED_ISOTONIC_GINI_DIAGNOSTICS_PASSED` when successful. These are finite diagnostics; the statements for every dimension, every positive real mass vector, and all real inputs are proved in Steps 1–4.

## Relationship to prior work

Weighted PAV and its consecutive-block weighted-average formula are classical; see Yeganova–Wilbur (2009) and de Leeuw–Hornik–Mair (2009). Németh–Németh (2015) proves coordinatewise isotonicity of weighted isotonic projections, a different type of order preservation. Guyader et al. (2012) analyze iterative isotone regression in bounded variation, not complete-pair Gini perturbation norms. Yang–Barber (2017/2018) characterize norm contraction for the **unweighted Euclidean** isotonic projection and hence conceptually cover the equal-mass Gini nonexpansivity conclusion. Their theorem does not determine the weighted-quadratic projection's Gini amplification, its optimal dimension envelope, or the four-point mass-ratio criterion. The equal-mass case and classical PAV geometry are not claimed as novel.

## Limitations

The exact arbitrary-mass formula is finite but exponential, not an efficient polynomial-time algorithm. The full dimension envelope is a supremum over mass vectors and is not attained at strictly positive finite masses for \(n\ge4\). Exact closed fixed-mass formulas for all dimensions beyond four are not asserted. The results do not cover partial orders, zero masses, nonlinear loss functions, or Gini seminorms weighted consistently with the observation masses. Historical priority remains subject to further bibliographic examination.

## References

1. L. Yeganova and W. J. Wilbur, “Isotonic Regression under Lipschitz Constraint,” *Journal of Optimization Theory and Applications* 141 (2009), 429–443. DOI: `10.1007/s10957-008-9477-0`. First public online date verified: 2009-01-07. In particular, Section 2 provides weighted block averages and PAV geometry.
2. J. de Leeuw, K. Hornik, and P. Mair, “Isotone Optimization in R: Pool-Adjacent-Violators Algorithm (PAVA) and Active Set Methods,” *Journal of Statistical Software* 32(5) (2009). DOI: `10.18637/jss.v032.i05`.
3. A. Guyader, N. Jégou, A. B. Németh, and S. Z. Németh, “A Geometrical Approach to Iterative Isotone Regression,” arXiv:`1211.3930` (2012).
4. A. B. Németh and S. Z. Németh, “Isotonic regression and isotonic projection,” arXiv:`1503.08458` (2015).
5. F. Yang and R. F. Barber, “Contraction and uniform convergence of isotonic regression,” arXiv:`1706.01852` (first posted 2017); specifically the unweighted projection contraction theorem.
