# Sharp leave-one-out batch sampling for a correlated column pair

## Finding

For an invertible least-squares matrix containing one pair of correlated unit columns and otherwise orthogonal unit columns, the unique distribution of size-\(n-1\) coordinate blocks minimizing the *sharp worst-case one-step expected squared residual* is explicit. Determinant-volume sampling is strictly inferior and can become arbitrarily slow while the optimum remains uniformly contracting. A fixed initial residual witnesses the same separation for every finite iteration count.

Put \(D_*=n+(n-2)\rho\) and \(D_{\rm vol}=2+(n-2)(1-\rho^2)\). The unique optimal probabilities for omitting coordinate \(i\), their sharp objective, and the volume-sampling values are
\[
 p_1^*=p_2^*=D_*^{-1},\qquad p_j^*=(1+\rho)D_*^{-1}\ (3\le j\le n),\qquad \Gamma_*=(1+\rho)D_*^{-1},
\]
\[
 p_1^{\rm vol}=p_2^{\rm vol}=D_{\rm vol}^{-1},\qquad p_j^{\rm vol}=(1-\rho^2)D_{\rm vol}^{-1},\qquad \Gamma_{\rm vol}=(1+\rho)D_{\rm vol}^{-1}>\Gamma_*.
\]
For a common unit-norm initial residual \(r_0\), the exact \(k\)-step expectations for these two independently resampled methods are respectively
\[
 \mathbb E\|r_k^*\|_2^2=\big((1+\rho^2)/D_*\big)^k,
 \qquad \mathbb E\|r_k^{\rm vol}\|_2^2=\big((1+\rho^2)/D_{\rm vol}\big)^k\quad(k\in\mathbb Z_{\ge0}).
\]
Thus when \(\rho\uparrow1\), the volume-sampling one-step and fixed-data multi-step factors approach \(1\), whereas the corresponding optimal factors approach \(1/(n-1)\). The smallest case showing a strict separation is dimension \(n=3\).

## Assumptions and scope

Take integers \(n\ge3\), real \(0<\rho<1\), \(\sigma=\sqrt{1-\rho^2}\), standard Euclidean basis vectors \(e_1,\ldots,e_n\), and the nonsingular matrix \(A\in\mathbb R^{n\times n}\) with columns
\[
 a_1=e_1,\quad a_2=\rho e_1+\sigma e_2,\quad a_j=e_j\quad(3\le j\le n).
\]
Given any \(b\in\mathbb R^n\), minimize \(f(x)=\frac12\|Ax-b\|_2^2\). In each iteration, independently choose a block \(S_i=\{1,\ldots,n\}\setminus\{i\}\) with fixed probability \(p_i\ge0\), \(\sum_{i=1}^np_i=1\); exactly minimize over coordinates indexed by the chosen block. The residual \(r=Ax-b\) then becomes \((I-P_{S_i})r\), where \(P_{S_i}=A_{S_i}(A_{S_i}^{\mathsf T}A_{S_i})^{-1}A_{S_i}^{\mathsf T}\). The objective is the smallest possible \(\Gamma(p)\) such that \(\mathbb E[\|r^+\|_2^2\mid r]\le\Gamma(p)\|r\|_2^2\) for *all* \(r\in\mathbb R^n\). Every such residual is attainable since \(A\) is nonsingular. Volume sampling means \(p_i\) proportional to \(\det(A_{S_i}^{\mathsf T}A_{S_i})\). All statements assume exact arithmetic, exact inner block solves, independent identically distributed block selections, and no switching or block-cost penalty.

## Proof

**1. Exact residual directions and their spectrum.** Each \(n-1\)-column block has an orthogonal-complement unit vector
\[
 w_1=\sigma e_1-\rho e_2,\qquad w_2=e_2,\qquad w_j=e_j\ (j\ge3).
\]
Consequently \(I-P_{S_i}=w_iw_i^{\mathsf T}\), and the exact expected squared residual is \(r^{\mathsf T}M(p)r\), with \(M(p)=\sum_{i=1}^np_iw_iw_i^{\mathsf T}\). It follows from the Rayleigh principle that \(\Gamma(p)=\lambda_{\max}(M(p))\) without slack. The \(e_1,e_2\) block has eigenvalues
\[
 \frac{p_1+p_2\pm\sqrt{\rho^2(p_1+p_2)^2+(1-\rho^2)(p_1-p_2)^2}}2,
\]
and its other eigenvalues are exactly \(p_3,\ldots,p_n\).

**2. Sharp minimax and equality conditions.** Set \(t=p_1+p_2\). The larger two-dimensional eigenvalue obeys \(\lambda_+\ge(1+\rho)t/2\), with equality exactly when \(p_1=p_2\) for \(0<\rho<1\) (including \(t=0\)). Also \(\max_{j\ge3}p_j\ge(1-t)/(n-2)\), with equality precisely when all those probabilities coincide. Therefore
\[
 \Gamma(p)\ge\max\!\left\{\frac{(1+\rho)t}{2},\frac{1-t}{n-2}\right\}.
\]
On \(0\le t\le1\), the unique minimizing \(t\) is where the increasing and decreasing terms agree, namely \(t=2/D_*\). Taking the equality distributions gives \(p_1=p_2=1/D_*\) and \(p_j=(1+\rho)/D_*\) for all \(j\ge3\). Strict monotonicity in the two bounds and their exact equality conditions prove uniqueness, including over zero-probability candidates.

**3. Determinants, sharp volume factor, and collapse.** Directly from the displayed columns, \(\det(A_{S_1}^{\mathsf T}A_{S_1})=\det(A_{S_2}^{\mathsf T}A_{S_2})=1\); for each \(j\ge3\) the determinant is \(1-\rho^2\). Hence the volume probabilities and \(D_{\rm vol}\) are as stated. The maximal eigenvalue is \((1+\rho)/D_{\rm vol}\), since this exceeds \((1-\rho^2)/D_{\rm vol}\). Because \(D_*>D_{\rm vol}\) for \(0<\rho<1\) and \(n\ge3\), volume sampling is strictly suboptimal. In the limit \(\rho\uparrow1\), \(D_*\to2(n-1)\) and \(D_{\rm vol}\to2\), giving \(\Gamma_*\to1/(n-1)\) and \(\Gamma_{\rm vol}\to1\). The matrix remains nonsingular at every parameter strictly less than one; the singular endpoint is a limit, not an included instance.

**4. An exact all-iteration witness.** Choose \(r_0=w_1\), which is a legitimate initial residual. For any omission law with \(p_1=p_2=q\), the residual after every nonzero step lies on the line spanned by \(w_1\) or \(w_2\); choosing an index \(j\ge3\) kills it. From either of the two unit residual lines, the one-step expected squared-norm multiplier is \(q(1+\rho^2)\): self-projection retains squared norm with probability \(q\), and cross-projection retains fraction \((w_1^{\mathsf T}w_2)^2=\rho^2\) with probability \(q\). Conditional expectation and induction yield the exact expressions for all integers \(k\ge0\). In particular the base of the volume-sampled exponential approaches one, but the optimized base approaches \(1/(n-1)\). More precisely, the volume base equals \(1-(n-1)(1-\rho^2)/D_{\rm vol}\), so its iteration count to reduce the expectation below any fixed fraction in \((0,1)\) diverges as \(\rho\uparrow1\); the optimized count remains bounded in that limit.

## Verification

The standalone `verify.py` uses SymPy exact-rational arithmetic to construct actual block projectors, Gram determinants, expected operators, sharp spectra, and finite-step transition laws. It checks several dimensions and rational on-circle parameterizations and reports 646 successful exact identities. Run `python verify.py` with Python 3 and SymPy installed. Those checks corroborate algebra in finite samples; the preceding symbolic proof establishes all parameter values and all iteration counts.

## Relationship to prior work

The October 2026 randomized batch-sampling coordinate-descent paper of Xie and Yang motivates the comparison between sampling policies for least squares, including data-driven policies [1]. Earlier volume-sampled coordinate descent by Rodomanov and Kropotov [2] and spectral equalization analyses for volume sampling by Entezari, Banerjee, and Kalantari [3] already cover volume-sampling methods and general spectral identities. **Neither the definition of determinant-volume sampling nor its expected-projector formula is claimed new.** The present contribution is the complete unique minimax law for the naturally first-nontrivial leave-one-out correlated-pair family, its strict comparison to determinant-volume sampling, and its exact all-iteration fixed-data separation. General arbitrary-sampling coordinate-descent convergence frameworks [4] supply broader settings but do not by themselves determine this exact optimized spectrum. Some potentially relevant original full texts could not be examined in their entirety, so no definitive historical-priority assertion is made.

## Limitations

This is a structured family of square full-rank matrices, not an all-matrix theorem. Its minimax criterion is the worst-case *one-step expected squared residual*, not expected runtime, cost-normalized work, or the exact asymptotic rate for every initial residual. The multi-step identities apply to the particular initial residual and the two displayed symmetric omission laws; they do not assert that the one-step minimax policy globally minimizes each finite-horizon criterion. The near-collinear endpoint \(\rho=1\) is excluded. Near that endpoint, computing the exact block least-squares solution can be ill-conditioned in floating-point arithmetic; the theorem makes no finite-precision performance guarantee. Primary-paper full-text coverage and unindexed-priority risk remain open.

## References

[1] D.-Y. Xie and X. Yang, *On randomized batch-sampling coordinate descent methods for solving linear least-squares problems*, arXiv:2610.04685 (first posted October 3, 2026). https://arxiv.org/abs/2610.04685

[2] A. Rodomanov and D. Kropotov, *A Randomized Coordinate Descent Method with Volume Sampling*, arXiv:1904.04587 (2019). https://arxiv.org/abs/1904.04587

[3] A. Entezari, A. Banerjee and B. Kalantari, *Volume Sampling and Spectral Equalization in Randomized Alternating Projections*, arXiv:2610.12346 (October 2026). https://arxiv.org/abs/2610.12346

[4] Z. Qu and P. Richtárik, *Coordinate Descent with Arbitrary Sampling I: Algorithms and Complexity*, Optimization Methods and Software (2016), arXiv:1412.8060. https://arxiv.org/abs/1412.8060
