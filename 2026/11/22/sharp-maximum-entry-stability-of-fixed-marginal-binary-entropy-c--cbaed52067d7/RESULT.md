# Sharp maximum-entry stability of fixed-marginal binary entropy coupling

## Finding

Fix two marginal probabilities \(0<r,c<1\). For each real \(2\times2\) log-kernel \(X\), let \(S_{r,c}(X)\) minimize
\[
\sum_{i,j=1}^{2}P_{ij}(\log P_{ij}-X_{ij})
\]
among all nonnegative matrices whose row sums are \((r,1-r)\) and whose column sums are \((c,1-c)\), with \(0\log0=0\). All four entries of the unique minimizer are strictly positive.

Put \(\ell=\max\{0,r+c-1\}\), \(u=\min\{r,c\}\), and
\[
H_{r,c}(z)=\frac1z+\frac1{r-z}+\frac1{c-z}+\frac1{1-r-c+z},\qquad \ell<z<u.
\]
There is a unique minimizer \(z_*(r,c)\) of \(H_{r,c}\) in this interval. The **smallest global** Lipschitz constant of \(S_{r,c}\) between entrywise maximum norms is exactly
\[
\boxed{\operatorname{Lip}_{\max}(S_{r,c})=\frac{4}{H_{r,c}(z_*)}.}
\]
The minimizer is equivalently the unique solution in \((\ell,u)\) of
\[
-\frac1{z^2}+\frac1{(r-z)^2}+\frac1{(c-z)^2}-\frac1{(1-r-c+z)^2}=0.
\]
This is a complete, one-dimensional strictly convex prescription for the sharp coefficient at every pair of interior marginals; it does not rely on a general upper bound alone.

The coefficient obeys the sharp marginal-variance envelope
\[
\boxed{\operatorname{Lip}_{\max}(S_{r,c})\le\min\{r(1-r),c(1-c)\}.}
\]
Equality holds **if and only if** at least one of the two marginal probabilities is \(1/2\). Otherwise the inequality is strict. Furthermore, writing the maximizing coupling's first entry as \(z_*\), its deviation from the independent coupling satisfies
\[
\boxed{\operatorname{sgn}(z_*-rc)=\operatorname{sgn}((1-2r)(1-2c)).}
\]
Thus the worst-conditioned coupling is independent precisely in the balanced-marginal cases; it has a strictly positive or strictly negative association otherwise, as determined by the marginal-majority alignment.

Equivalently, for entropically regularized transport with cost matrix \(C\) and regularization \(\varepsilon>0\), the sharp maximum-entry cost-to-plan Lipschitz coefficient is \(4/(\varepsilon H_{r,c}(z_*))\), since the log-kernel equals \(-C/\varepsilon\).

## Assumptions and scope

Both marginals are fixed and strictly interior: \(r,c\in(0,1)\). Every real log-kernel entry is allowed without any bounded-contrast restriction. The norm on both the four-dimensional input and output is \(\|A\|_{\max}=\max_{i,j}|A_{ij}|\). All distances compare the optimal plans for two possibly different log-kernels with the **same** two marginals. This is a global nonlinear-operator Lipschitz coefficient, not a convergence factor for iterative matrix scaling. The sharp coefficient is a supremum of finite-pair quotients and is approached by infinitesimal perturbations at an interior log-kernel; finite separated pairs need not attain it.

## Proof

**1. Scalar reduction and existence.** Every feasible coupling has the form
\[
P(z)=\begin{pmatrix}z&r-z\\c-z&1-r-c+z\end{pmatrix},\qquad \ell\le z\le u.
\]
The objective is strictly convex in \(z\) on the interior. Its derivative is
\[
\Theta_{r,c}(z)-h(X),\quad
\Theta_{r,c}(z)=\log\frac{z(1-r-c+z)}{(r-z)(c-z)},\quad
h(X)=X_{11}-X_{12}-X_{21}+X_{22}.
\]
The derivative \(\Theta'_{r,c}(z)=H_{r,c}(z)>0\); moreover, \(\Theta_{r,c}(z)\to-\infty\) as \(z\downarrow\ell\) and \(\Theta_{r,c}(z)\to+\infty\) as \(z\uparrow u\). Hence exactly one interior \(z(X)\) solves \(\Theta_{r,c}(z(X))=h(X)\), proving uniqueness and positivity. Conversely, every interior \(z\) is realized by some \(X\), for example \(X_{ij}=\log P(z)_{ij}\).

**2. Exact local and global operator norms.** The implicit-function theorem gives, for any perturbation \(V\),
\[
D z(X)[V]=\frac{V_{11}-V_{12}-V_{21}+V_{22}}{H_{r,c}(z(X))},\qquad
D S_{r,c}(X)[V]=D z(X)[V]\begin{pmatrix}1&-1\\-1&1\end{pmatrix}.
\]
The maximum of the absolute numerator over \(\|V\|_{\max}\le1\) equals exactly \(4\), witnessed by the checkerboard \(V=\bigl(\begin{smallmatrix}1&-1\\-1&1\end{smallmatrix}\bigr)\). Consequently \(\|D S_{r,c}(X)\|_{\max\to\max}=4/H_{r,c}(z(X))\). Integrating the derivative along the straight segment between arbitrary log-kernels yields the global upper bound \(4/\inf_{\ell<z<u}H_{r,c}(z)\). Choosing \(X_{ij}=\log P(z_*)_{ij}\) and then perturbing in the checkerboard direction gives a sequence of nonzero input differences whose output-to-input quotient converges to that same constant. The bound is therefore globally sharp.

**3. Uniqueness of the curvature minimizer.** On the feasible open interval,
\[
H_{r,c}''(z)=2\left(\frac1{z^3}+\frac1{(r-z)^3}+\frac1{(c-z)^3}+\frac1{(1-r-c+z)^3}\right)>0.
\]
Since \(H_{r,c}\to+\infty\) at either endpoint, it has a unique interior minimizer, characterized by the stated first-derivative equation. This also proves that its scalar defining equation admits no additional feasible roots.

**4. The exact balance equality criterion.** For any two positive numbers with sum \(s\), the sum of their reciprocals is at least \(4/s\), with equality exactly when the two numbers agree. Applying this to the first and second rows of \(P(z)\) gives
\[
H_{r,c}(z)\ge\frac4r+\frac4{1-r}=\frac4{r(1-r)}.
\]
Applying it instead to the columns gives \(H_{r,c}(z)\ge4/[c(1-c)]\). Equality in the row inequality requires both row entries equal, which forces \(c=1/2\); conversely, when \(c=1/2\), choosing \(z=r/2\) realizes equality. Similarly, equality in the column inequality occurs exactly when \(r=1/2\). Hence \(4/H_{r,c}(z_*)\le\min\{r(1-r),c(1-c)\}\), with equality precisely when at least one marginal is balanced; both inequalities are strict otherwise.

**5. Association of the maximizing coupling.** The independent coupling has first entry \(z_0=rc\), which is strictly inside \((\ell,u)\). Direct evaluation gives
\[
H_{r,c}'(rc)=-\frac{(1-2r)(1-2c)}{r^2(1-r)^2c^2(1-c)^2}.
\]
Since \(H_{r,c}'\) increases strictly and vanishes only at \(z_*\), the sign of \(z_*-rc\) equals the sign of \((1-2r)(1-2c)\). This proves the sign and exact balance-rigidity statements. The determinant \(P(z)_{11}P(z)_{22}-P(z)_{12}P(z)_{21}=z-rc\), so the sign is precisely the sign of binary association. All boundary, equality, and quantifier cases have thus been included.

## Verification

`CHECK.py` uses standard-library arithmetic and a seeded pseudorandom generator to test the unique curvature minimizer, derivative sign and balance inequalities, global perturbation bounds and checkerboard near-sharpness. On execution it passed 9,675 supplementary numerical assertions, including both balanced and nonbalanced examples. For \(r=0.3\) and \(c=0.4\), the computed minimizer is approximately \(0.14172592173887283\) and the coefficient approximately \(0.20502590955577837\), strictly below \(\min\{0.3(0.7),0.4(0.6)\}=0.21\). Run `python3 CHECK.py` using Python 3 and no additional packages. The infinite-dimensional quantifiers over all log-kernels and all interior marginal pairs are proved analytically above; finite tests are not used as a proof of those assertions.

## Relationship to prior work

Eisenberger, Toker, Leal-Taixé, Bernard and Cremers (2022) derive the general differentiability and KKT Jacobian of Sinkhorn layers; their Lemma 2 and Theorem 3 give a general implicit-gradient mechanism that subsumes the **pointwise differentiation** used here. They do not give the globally optimized maximum-entry coefficient over all binary cost matrices at fixed unequal marginals, nor the strict balance equality and association classification. Ghosal, Nutz and Bernton (first posted June 7, 2021) establish qualitative stability of entropically regularized transport under changing marginals and costs, not the precise finite-dimensional operator modulus derived here. Eckstein and Nutz (2021 preprint, 2022 publication) study quantitative regularized-transport stability, emphasizing marginal perturbations, and convergence of scaling iterations. Related exact two-state Sinkhorn projective contraction results concern the **scaling iteration at fixed kernel**, while this statement concerns **changes in the optimal coupling as the kernel changes**. Those are distinct nonlinear maps and neither statement directly implies the other exact coefficient.

## Limitations

The theorem concerns only strictly interior binary marginals and exact optimizers of positive-kernel entropy regularization. It does not establish a stability formula for general transport table dimensions, changing marginals, unregularized optimal transport, or approximate Sinkhorn iterates. The one-dimensional strict-convex prescription is exact, rather than a simple elementary radical in arbitrary margins. The general implicit-derivative theorem is known; the mathematical contribution is the sharp global optimization and its balance/association structure. Earlier equivalent results in unindexed binary contingency-table, log-linear-model or Sinkhorn literature cannot be excluded. Independent validation is not claimed.

## References

1. Promit Ghosal, Marcel Nutz, Espen Bernton, *Stability of Entropic Optimal Transport and Schrödinger Bridges*, arXiv:2106.03670, first posted 2021-06-07, https://arxiv.org/abs/2106.03670, accessible author full text https://www.math.columbia.edu/~mnutz/docs/EOT-stability.pdf.
2. Marvin Eisenberger, Aysim Toker, Laura Leal-Taixé, Florian Bernard, Daniel Cremers, *A Unified Framework for Implicit Sinkhorn Differentiation*, arXiv:2205.06688, first posted 2022-05-13, CVPR 2022, https://arxiv.org/abs/2205.06688, full published text https://openaccess.thecvf.com/content/CVPR2022/papers/Eisenberger_A_Unified_Framework_for_Implicit_Sinkhorn_Differentiation_CVPR_2022_paper.pdf.
3. Stephan Eckstein, Marcel Nutz, *Quantitative Stability of Regularized Optimal Transport and Convergence of Sinkhorn's Algorithm*, arXiv:2110.06798, first posted 2021-10-13, https://arxiv.org/abs/2110.06798.
4. Tobias Lehmann, Max-K. von Renesse, Alexander Sambale, André Uschmajew, *A Note on Overrelaxation in the Sinkhorn Algorithm*, first online 2021-12-14, https://doi.org/10.1007/s11590-021-01830-0.
