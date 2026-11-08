# Exact false-pruning law and Gumbel boundary for adjoint-free Gaussian range finding

## Finding

For Smith--Do--Chen's two-lookahead adjoint-free Frobenius range finder (Algorithm 4 with the rank-pruning rule of Algorithm 3), a flat rank-\(b\) input gives an **exact finite-block tolerance-violation probability** and a sharp asymptotic transition. The apparent improvement in the variance of individual Gaussian row-energy estimates does not prevent the **minimum of all row estimates** from triggering an incorrect deletion.

Let \(F_d(t)=\Pr(\chi_d^2\le t)\) be the chi-square distribution function with \(d\) degrees of freedom. For any integer \(b\ge2\) and absolute Frobenius tolerance \(0<\tau<1\), the probability that the algorithm reaches its second lookahead and then returns a basis whose *true* Frobenius projection error exceeds \(\tau\) is exactly

\[
P_b(\tau)=\bigl[1-F_{b^2}(b\tau^2)\bigr]
 \left\{1-\bigl[1-F_b(b\tau^2)\bigr]^b\right\}.
\]

The first factor is the probability of not prematurely stopping before a first basis block exists. Conditional on that event, the second factor is the exact incorrect-pruning probability. No behavior is asserted for the exceptional initial-stop branch, on which the printed pseudocode does not yet define the previous basis.

For every fixed \(0<\tau<1\), \(P_b(\tau)\to0\) as \(b\to\infty\). However, for \(c>0\), if \(\tau_b^2=1-c\sqrt{\log b/b}\), then

\[
\lim_{b\to\infty}P_b(\tau_b)=
\begin{cases}1,&0<c<2,\\0,&c\ge2.\end{cases}
\]

Moreover, for each fixed real \(x\), put

\[
L_b(x)=\log b-\tfrac12\log\log b-\tfrac12\log(4\pi)+x,
\qquad \tau_b^2=1-2\sqrt{L_b(x)/b}.
\]

For sufficiently large \(b\) this is a valid tolerance, and

\[
\lim_{b\to\infty}P_b(\tau_b)=1-\exp(-e^{-x}).
\]

This is a sharp Gumbel-type failure window. The algebra holds as well for any ambient dimension \(N>b\), so the matrix may be highly rank deficient.

## Assumptions and scope

For each \(b\ge2\) choose any integer \(N>b\) and the deterministic real \(N\times N\) matrix

\[
A=\operatorname{diag}(I_b,0_{N-b}).
\]

Use *independent* Gaussian blocks \(\Omega_1,\Omega_2\in\mathbb R^{N\times b}\), each with independent entries of distribution \(N(0,1/b)\). Use exactly the absolute-tolerance version of Smith--Do--Chen Algorithm 4, including its second-lookahead proxy \(\widetilde B=Q_1^{\mathsf T}A\Omega_2\) and the ascending-row-energy pruning test of their Algorithm 3. Work in exact real arithmetic, with a mathematically exact thin orthonormal basis and complete reorthogonalization.

Write \(G_b=\{\|A\Omega_1\|_F>\tau\}\). The theorem concerns the well-defined two-lookahead branch \(G_b\). The intended approximation is the orthogonal projection \(QQ^{\mathsf T}A\); before pruning the exact residual is zero, and the smallest rank giving strict tolerance \(\tau<1\) is precisely \(b\). A single discarded basis column already makes the true error at least \(1\).

## Proof

**Step 1 (reach the defined two-step branch).** The \(b\times b\) leading block of \(A\Omega_1\) is nonsingular almost surely, hence the first orthonormal block \(Q_1\) spans exactly \(\operatorname{range}(A)\). Therefore

\[
\|A\Omega_1\|_F^2\stackrel{d}=\frac{\chi^2_{b^2}}{b},
\qquad \Pr(G_b)=1-F_{b^2}(b\tau^2).
\]

On \(G_b\), the algorithm constructs \(Q_1\) and its next residual sketch equals \(A\Omega_2-Q_1Q_1^{\mathsf T}A\Omega_2=0\). Thus the second lookahead terminates and supplies a zero indicator to the pruning rule. The early-stop branch \(G_b^c\) is explicitly excluded.

**Step 2 (conditional independence of the second sketch).** Condition on the entire first Gaussian block. The \(b\) rows of \(Q_1^{\mathsf T}A\Omega_2\) are then independent Gaussian vectors with covariance \(I_b/b\): the restriction of \(Q_1\) to \(\operatorname{range}(A)\) is orthogonal, and \(\Omega_2\) is independent and rotationally invariant. Consequently, the \(b\) squared row norms are independent \(\chi_b^2/b\) random variables. This conditional distribution does not depend on the first block or on the event \(G_b\).

**Step 3 (exact failure event).** With initial pruning indicator zero and tolerance \(\tau\), Algorithm 3 first considers the smallest row norm. It discards at least one column if and only if that norm is strictly below \(\tau\) (ties have probability zero). The corresponding omitted orthonormal columns each have full energy \(1\) for this matrix: if \(r\ge1\) basis columns are removed, then

\[
\|A-QQ^{\mathsf T}A\|_F^2=r\ge1>\tau^2.
\]

If none is removed, the true residual is zero. Thus conditional failure is exactly \(1-[1-F_b(b\tau^2)]^b\), independent of \(G_b\), proving the finite-block probability formula.

**Step 4 (lower chi-square tails).** Write \(X_b=\chi^2_b/b\) and \(\delta\downarrow0\). For \(b\delta^2\to\infty\) and \(b\delta^3\to0\), the chi-square density after rescaling is

\[
f_b(y)=\frac{(b/2)^{b/2}}{\Gamma(b/2)}y^{b/2-1}e^{-by/2}.
\]

Stirling's formula yields

\[
f_b(1-\delta)=\frac{\sqrt b}{2\sqrt\pi(1-\delta)}
 \exp\!\left[-\frac b2\{-\delta-\log(1-\delta)\}\right](1+o(1)).
\]

The logarithmic density increases toward the endpoint \(y_0=1-\delta\) with derivative \(a_b=(b/2-1)/y_0-b/2\sim b\delta/[2(1-\delta)]\). For all \(y\le y_0\), the logarithmic derivative is at least \(a_b\); this bounds the lower-tail integral above by \(f_b(y_0)/a_b\). On the interval \(y_0-M/a_b\le y\le y_0\) for fixed \(M>0\), the derivative differs from \(a_b\) by relative \(O(M/(b\delta^2))=o(1)\). Integration on that interval gives a lower bound of \((1-e^{-M}+o(1))f_b(y_0)/a_b\). Letting first \(b\to\infty\) and then \(M\to\infty\) proves the matching endpoint asymptotic

\[
F_b(b(1-\delta))
 =\frac{1+o(1)}{\delta\sqrt{\pi b}}
 \exp\!\left[-\frac b2\{-\delta-\log(1-\delta)\}\right]
 =\frac{1+o(1)}{\delta\sqrt{\pi b}}e^{-b\delta^2/4}.
\]

For fixed \(\tau^2<1\) instead, the gamma Chernoff bound shows \(F_b(b\tau^2)\le\exp(-b I(\tau^2))\), where \(I(y)=(y-1-\log y)/2>0\). Hence \(bF_b(b\tau^2)\to0\).

**Step 5 (sharp phase and centered window).** For \(\delta_b=c\sqrt{\log b/b}\) with \(c>0\), the previous estimate implies

\[
bF_b(b(1-\delta_b))\sim
\frac{b^{1-c^2/4}}{c\sqrt{\pi\log b}}.
\]

It diverges for \(c<2\) and tends to zero for \(c\ge2\). For the refined choice \(\delta_b=2\sqrt{L_b(x)/b}\), the same tail formula gives \(bF_b(b(1-\delta_b))\to e^{-x}\), so the minimum-of-rows survival probability tends to \(\exp(-e^{-x})\). Finally \(\Pr(G_b)\to1\), since \(\chi^2_{b^2}\) is concentrated near \(b^2\), whereas the first-stop cutoff is at most \(b\). Multiplying the independent factors completes the theorem.

## Verification

The accompanying `verify.py` reconstructs the actual first-block QR and exact-zero second lookahead on the diagonal test matrices, implements the specified ascending-row-energy pruning, and checks that the true squared residual equals the number of removed basis columns. It also compares the closed probability formula with independent chi-square simulations and tests the large-block boundary and refined window. These are finite numerical checks; the infinite claims follow from the above probability and asymptotic arguments.

For illustration, at \(b=16\) and \(\tau=0.9\), the exact two-lookahead failure probability is approximately \(0.9981126219\). At \(b=16\) and \(\tau=0.99\) it is approximately \(0.9999931943\). The algorithm's row-energy estimates are individually unbiased in both examples, but taking the minimum across all rows makes incorrect deletion likely.

## Relationship to prior work

Smith, Do, and Chen (2026), Section 3.3 and Algorithms 3--4, introduce precisely the adjoint-free projected-row estimates analyzed here, establish their individual unbiasedness and variance \(2\|b_j\|_2^4/b\), and discuss possible rank over-retention. Their results do not give this exact *under-retention* and true-tolerance failure law on flat singular clusters or its extreme-value transition. The probability analysis uses standard chi-square and extreme-value tools; those tools alone are not claimed novel.

Yu, Gu, and Li (2016) analyze fixed-precision QB approximations using explicit coefficient energies and subtraction-based error indicators, rather than proxy rows of an independent second sketch. Pearce, Chen, Dong, and Martinsson (2023) develop adaptive interpolative decomposition via partially pivoted LU, not the analyzed row-pruning rule. Gorman and collaborators (2018/2019) develop Gaussian projection stopping criteria in hierarchical compression, including tail estimates for a *single projected Frobenius norm*, but do not specify the same coordinatewise minimum-based final pruning. None of these results implies the exact two-lookahead event or its centered extreme-value window by direct specialization.

## Limitations

The example has a flat nonzero singular spectrum and exact rank equal to the block size. It is not a universal failure bound for arbitrary matrices or tolerances; fixed tolerances strictly below \(1\) become safe asymptotically. The initial-stop branch is excluded from the failure event because the written algorithm has not created a first basis on that branch. The result assumes independent real Gaussian sketches and exact arithmetic, not finite-precision orthogonalization, correlated sketches, alternative safety margins, or the full matrix-free variant with exact coefficient rows. The extreme-value limit is a consequence of a standard classical tail law, while the method-specific identification of the failure event is the new content.

## References

1. A. I. Smith, E. Do, and C. Chen, *Adaptive, Matrix-Free Low-Rank Approximation*, arXiv:2607.06758v1 (first posted 2026-07-07), Sections 3.2--3.3, Algorithms 3--4. https://arxiv.org/html/2607.06758v1
2. W. Yu, Y. Gu, and Y. Li, *Efficient Randomized Algorithms for the Fixed-Precision Low-Rank Matrix Approximation*, arXiv:1606.09402 (2016). https://arxiv.org/abs/1606.09402
3. K. J. Pearce, C. Chen, Y. Dong, and P.-G. Martinsson, *Adaptive Parallelizable Algorithms for Interpolative Decompositions via Partially Pivoted LU*, arXiv:2310.09417 (2023). https://arxiv.org/abs/2310.09417
4. C. Gorman et al., *Matrix-free construction of HSS representation using adaptive randomized sampling*, arXiv:1810.04125 (2018); journal version *Robust and Accurate Stopping Criteria for Adaptive Randomized Sampling in Matrix-Free Hierarchically Semiseparable Construction* (2019). https://arxiv.org/abs/1810.04125
