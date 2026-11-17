# Sharp Gini stability and reciprocal mass thresholds for star-graph fusion denoising

## Finding
Fix an integer \(k\ge 2\), a central observation mass \(a>0\), and arbitrary positive edge penalties \(\beta_1,\ldots,\beta_k>0\). On the star with hub \(o\) and leaves \(v_1,\ldots,v_k\), let \(F_{a,\beta}(z)\) be the unique minimizer, over real \(y\) on all \(k+1\) vertices, of
\[
 \frac a2(y_o-z_o)^2+\frac12\sum_{i=1}^k(y_i-z_i)^2+
 \sum_{i=1}^k\beta_i|y_i-y_o|.
\]
For unweighted pairwise Gini variation \(G(h)=\sum_{u<v}|h_u-h_v|\), its **sharp two-input Lipschitz modulus**, taken over all distinct inputs modulo constants, is
\[
 L_k(a)=\sup_{G(z-z')>0}\frac{G(F_{a,\beta}(z)-F_{a,\beta}(z'))}{G(z-z')}
 =\max\left\{1,\frac{2(k-1)}{k(a+1)},\max_{1\le r<k}\frac{a(r+1)(k-r)}{k(a+r)}\right\}.
\]
In particular, the sharp modulus is **independent of every positive edge penalty**, even if the penalties differ. Every branch contributing the maximum is realized by arbitrarily close real input pairs.

For \(k=2\), \(L_2(a)=1\) for every \(a>0\). For each \(k\ge3\), the denoiser is Gini-nonexpansive for *all* input pairs precisely when
\[
\boxed{\frac{k-2}{k}\le a\le\frac{k}{k-2}}.
\]
Outside this reciprocal interval, some arbitrarily close data pairs have strictly amplified Gini separation. Furthermore,
\[
\sup_{a>0}L_k(a)=\frac1k\max\left\{2(k-1),\left\lfloor\frac{(k+1)^2}{4}\right\rfloor\right\}.
\]
The two extreme-mass mechanisms tie for \(k=2,3,4\); the hub-dominant mechanism is strictly larger starting at **five leaves**. The supremum is generally approached at extreme positive mass ratios rather than attained at finite mass.

## Assumptions and scope
All variables are real. The quadratic loss assigns mass \(a\) to the hub and mass one to each leaf; a common rescaling of all observation masses does not affect the asserted formula when the penalties are rescaled accordingly. Each edge penalty is fixed and strictly positive. There is no restriction on the magnitude or signs of the input data. The quantity \(G\) is the unweighted sum over *all unordered vertex pairs*, not the star-edge total variation. Both the input and output distances are measured by \(G\). Constants are its kernel, and \(F_{a,\beta}(z+c\mathbf1)=F_{a,\beta}(z)+c\mathbf1\), so the quotient seminorm is well-defined. The result concerns a two-input Lipschitz modulus, not the one-input decrease of a regularization objective.

## Proof
**1. Exact local form and accessibility.** For any proposed fitted hub value \(h\), minimizing in a leaf coordinate gives
\[
 y_i=h+\operatorname{soft}(z_i-h,\beta_i),\qquad
 \operatorname{soft}(s,b)=\operatorname{sgn}(s)\max(|s|-b,0).
\]
The optimal hub solves the continuous strictly increasing equation
\[
 a(h-z_o)+\sum_{i=1}^k\operatorname{clip}(h-z_i,-\beta_i,\beta_i)=0.
\]
On an open cell, a set \(R\) of \(r\) leaves is fused to the hub. The other leaves have fixed signs of \(z_i-h\). Thus the derivative in the data is a linear map \(T_R\) which replaces the hub and all leaves in \(R\) by their weighted mean \((a\delta_o+\sum_{i\in R}\delta_i)/(a+r)\) and preserves every remaining leaf perturbation. The cells cover the data space up to finitely many hyperplanes, and the denoiser is continuous piecewise affine. Every \(T_R\) occurs on a nonempty open cell: set fitted hub and fused leaves to zero, each unfused fitted leaf to \(3\beta_i\), fused data to zero, unfused data to \(4\beta_i\), and hub data to \(-\sum_{i\notin R}\beta_i/a\). Strict inequalities in the fused and unfused branches give an open neighborhood. Consequently the global two-input Gini modulus is the maximum of the induced Gini norms of these finitely many maps; local sharpness follows from perturbations within the open cells.

**2. A sharp single-block lemma.** Consider \(T_R\) with \(1\le r<k\), and put \(p=r+1\), \(t=k-r\), and \(n=k+1=p+t\). The identity block \(r=0\) has norm one; the fully fused block \(r=k\) has Gini seminorm zero. By the level-set (discrete coarea) decomposition of an arbitrary real input, the Gini norm of a constant-preserving linear map is the maximum ratio over nontrivial binary cuts \(\mathbf1_U\): decompose an input into its ordered upper level sets, apply the triangle inequality to the output, and use the exact same decomposition of its input Gini variation.

For such a cut, let \(c\in\{0,1\}\) indicate whether the hub belongs to \(U\); let \(A\in\{0,\ldots,r\}\) count selected fused leaves and \(d\in\{0,\ldots,t\}\) count selected unfused leaves. Its fused output level is \(m=(ac+A)/(a+r)\), and exactly
\[
 G(T_R\mathbf1_U)=p[d(1-m)+(t-d)m]+d(t-d),\quad
 G(\mathbf1_U)=(c+A+d)(n-c-A-d).
\]
To prove any candidate bound \(K\ge1\), the difference \(K G(\mathbf1_U)-G(T_R\mathbf1_U)\), viewed as a polynomial in \(d\) with \(c,A\) fixed, has quadratic coefficient \(-(K-1)\). It is concave, so it suffices to verify \(d=0\) and \(d=t\). The latter is equivalent to \(d=0\) after complementing the cut. For \(d=0\) and \(c=0\), the ratio is at most
\[
 B_r(a)=\frac{(r+1)(k-r)}{(a+r)(k-r+1)},
\]
with equality when all \(r\) fused leaves, but not the hub, are selected. For \(d=0\) and \(c=1\), write \(u=A+1\in[1,p]\). The ratio becomes \(pt(a+u-1)/[(a+r)u(n-u)]\). If \(a\le1\), the fused output level is no larger than \(u/p\), making this ratio at most one. If \(a\ge1\), the identity
\[
 \frac{a+u-1}{u(n-u)}=\frac{a-1}{n u}+\frac{1+(a-1)/n}{n-u}
\]
expresses the factor as a convex function of \(u\), whose maximum on \([1,p]\) is at an endpoint. These endpoints give respectively
\[
 C_r(a)=\frac{a(r+1)(k-r)}{k(a+r)}\quad\text{and}\quad 1.
\]
Thus \(\|T_R\|_{G\to G}=\max\{1,B_r(a),C_r(a)\}\). All three candidate values have exact binary-cut witnesses: the entire fused block, all fused leaves without the hub, and the single hub, respectively. For \(a\ge1\), \(B_r(a)\le1\); for \(a\le1\), \(C_r(a)\le1\).

**3. Optimization and boundaries.** When \(a<1\), \(B_r(a)=[(r+1)/(a+r)]\,[(k-r)/(k-r+1)]\) strictly decreases with \(r\), so its maximum is \(B_1(a)=2(k-1)/[k(a+1)]\). For \(a\ge1\), only the \(C_r(a)\) terms can exceed one. Solving \(B_1(a)\le1\) gives \(a\ge(k-2)/k\). For \(1\le r\le k-2\), solving \(C_r(a)\le1\) gives \(a\le k/(k-r-1)\), and the strongest restriction occurs at \(r=1\). The \(r=k-1\) term never exceeds one. This proves the reciprocal interval. Finally \(B_1(a)\) decreases to \(2(k-1)/k\) as \(a\downarrow0\), while each \(C_r(a)\) increases to \((r+1)(k-r)/k\) as \(a\uparrow\infty\). Optimizing the latter product over integers yields \(\lfloor(k+1)^2/4\rfloor/k\). The two limits tie for \(k=2,3,4\) and the latter exceeds the former for all \(k\ge5\), giving the stated envelope.

## Verification
The standalone checker `checks/verify_star_fused_gini.py` uses only the Python standard library and exact rational arithmetic. It independently implements the strictly monotone hub optimality equation, reconstructs every tested proximal solution from its piecewise-affine intervals, checks binary-cut bounds against the formula, exhibits exact two-input witnesses with nonuniform positive edge penalties, and checks arbitrary signed data pairs. Run `python3 checks/verify_star_fused_gini.py`. Its finite tests are corroboration; Step 2 and Step 3 above prove the all-dimension statements.

## Relationship to prior work
Tibshirani, Saunders, Rosset, Zhu and Knight introduced fused regularization for ordered data (first public journal version December 13, 2004). Tibshirani and Taylor developed the generalized-lasso framework including graph differences (arXiv 1005.1971, first submitted May 11, 2010), while Chen and collaborators studied graph-guided fused regularization (arXiv 1005.4717, first submitted May 26, 2010). Their examined results address optimization geometry, paths, and algorithms, not the present sharp two-input complete-pair Gini stability coefficient or reciprocal mass interval. A related quantitative result on weighted isotonic regression obtains Gini stability by analyzing weighted block projections on chains; its active linear pieces share algebra with the present proof. The additional claim here is specifically for star-graph total-variation proximity with any positive, independently chosen fusion edge penalties and its exact sharp mass-ratio phase diagram. A shared block-averaging computation must not be mistaken for independent novelty.

## Limitations
This result applies to a single star with one hub mass and equal positive leaf masses, strictly positive quadratic fidelity, and separate strictly positive absolute-edge penalties. It does not supply the corresponding exact coefficient for arbitrarily unequal leaf masses, general trees, other perturbation seminorms, or nonquadratic fidelities. Historical priority is qualified: independent exhaustive literature assessment has not been performed, and related weighted isotonic block-averaging results could inform a shorter derivation.

## References
1. R. Tibshirani, M. Saunders, S. Rosset, J. Zhu, K. Knight, *Sparsity and smoothness via the fused lasso*, Journal of the Royal Statistical Society B 67 (2005), 91–108. First published 2004-12-13. DOI: 10.1111/j.1467-9868.2005.00490.x. Full author PDF: https://web.stanford.edu/group/SOL/papers/fused-lasso-JRSSB.pdf.
2. R. J. Tibshirani, J. Taylor, *The solution path of the generalized lasso*, arXiv:1005.1971 (first submitted 2010-05-11).
3. X. Chen, Q. Lin, S. Kim, J. G. Carbonell, E. P. Xing, *Smoothing proximal gradient method for general structured sparse regression*, arXiv:1005.4717 (first submitted 2010-05-26).
