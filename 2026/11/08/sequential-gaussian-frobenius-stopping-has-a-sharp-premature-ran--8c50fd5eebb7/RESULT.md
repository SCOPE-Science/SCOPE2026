# Sequential Gaussian Frobenius stopping has a sharp premature-rank law

## Finding

Consider a fresh-batch relative-Frobenius stopping rule for adaptive randomized range finding. For a real matrix with exactly \(r\) equal nonzero singular values, and a fixed number \(b\) of Gaussian probes per fresh look, the entire first-stopping-rank distribution is explicit. More consequentially, the stopping rank systematically undershoots the deterministic Frobenius-error threshold by a sharp \(\sqrt{r\log r}\) scale.

Fix \(b\in\mathbb N\), \(0<\tau<1\), and let \(r\to\infty\) through positive multiples of \(b\). For the procedure and matrix specified below, let \(K_r\) be its first accepted rank. Then

\[
\frac{(1-\tau)r-K_r}{\sqrt{r\log r}}
\xrightarrow{\mathbb P}
\sqrt{\frac{2\tau(1-\tau)}{b}}.
\]

Consequently, the probability that the returned basis **violates the intended relative Frobenius tolerance** tends to one. This is an exact-arithmetic phenomenon; finite precision and subspace approximation errors are not needed.

For every finite admissible \(r\), put

\[
 p_0=0,\qquad p_r=1,\qquad
 p_k=I_{\tau}\!\left(\frac{b(r-k)}2,\frac{bk}2\right),
 \quad k=b,2b,\ldots,r-b,
\]

where \(I_{\tau}(a,c)\) denotes the regularized incomplete beta function. The exact distribution is

\[
 \mathbb P\{K_r=jb\}=p_{jb}\prod_{i=0}^{j-1}(1-p_{ib}),
 \qquad j=0,1,\ldots,r/b.
\]

Let \(k_*=b\lceil (1-\tau)r/b\rceil\) be the smallest allowed rank meeting the actual target. Then the exact probability of falsely accepting a rank is

\[
 \mathbb P\{K_r<k_*\}=1-\prod_{\substack{0\le j<r/b\\jb<k_*}}(1-p_{jb}).
\]

For illustration, \(r=2048\), \(b=2\) and \(\tau=1/4\) give a computed false-acceptance probability of approximately \(0.987911\); this is an exact finite-sum evaluation of the displayed beta law, not a universal probability for other spectra or algorithms.

## Assumptions and scope

Let \(b\ge1\) and \(r\ge b\) be integers with \(b\mid r\). Choose any \(q\ge0\) and \(\sigma>0\). The real target matrix is

\[
 M=\sigma\begin{bmatrix}I_r&0_{r\times q}\end{bmatrix}
 \in\mathbb R^{r\times(r+q)}.
\]

Start with the empty orthonormal basis \(U_0\). At each reached rank \(k\in\{0,b,\ldots,r\}\), draw a **new independent** standard-real-Gaussian test matrix \(\Omega_k\in\mathbb R^{(r+q)\times b}\), set \(G_k=M\Omega_k\) and \(E_k=(I-U_kU_k^{\mathsf T})G_k\), and stop if

\[
 T_k:=\frac{\|E_k\|_F^2}{\|G_k\|_F^2}\le\tau.
\]

Otherwise append an orthonormal basis of all \(b\) columns of \(E_k\) and proceed. Here \(\tau=\varepsilon^2\), where \(\varepsilon\) is the desired relative Frobenius-norm tolerance. Each denominator uses the **same fresh batch as that look's numerator**, not an average of earlier estimates. All operations are in exact arithmetic. Because \(r\) is a multiple of \(b\), the residual has at least \(b\) dimensions at every nonterminal rank; Gaussian columns have full residual rank almost surely. At \(k=r\) the numerator is zero.

The model isolates the elementary single-node fresh-batch stopping rule in Do and Chen (2026, Section 4.3, equations (4.7)–(4.11)); it **does not** model their implementation's averaging of the denominator, later rank pruning, freeze margins, level-wide decisions, or correlated sketches at coarser hierarchical levels. Nothing is asserted about those modifications or about general singular spectra.

The actual relative-squared Frobenius error of every rank-\(k\) orthogonal projection basis produced here is deterministically \((r-k)/r\), since \(MM^{\mathsf T}=\sigma^2 I_r\). Hence the true target holds precisely when \(k\ge (1-\tau)r\).

## Proof

**1. Fresh-look law.** Condition on the complete algorithmic history just before a reached rank \(k\). The basis \(U_k\) is orthonormal, of dimension \(k\), and independent of the fresh \(\Omega_k\). Since \(M\Omega_k\) is an isotropic Gaussian matrix with covariance \(\sigma^2 I_r\), orthogonal invariance and Pythagoras yield independent variables

\[
 X_k:=\sigma^{-2}\|E_k\|_F^2\sim\chi^2_{b(r-k)},\qquad
 Y_k:=\sigma^{-2}\|U_kU_k^{\mathsf T}G_k\|_F^2\sim\chi^2_{bk}.
\]

Thus \(T_k=X_k/(X_k+Y_k)\) has the stated beta distribution for \(0<k<r\). The conditional acceptance probability depends only on \(k\), not on the previous basis or survival event. The endpoint cases \(T_0=1\) and \(T_r=0\) are deterministic. Multiplying successive conditional survival probabilities gives the finite first-passage law and its false-acceptance formula, without requiring unconditional independence of the entire history.

**2. An exact upper bound for one look.** Put \(n=br/2\), \(u=(r-k)/r\), and suppose \(u>\tau\). Using the independent chi-square variables in Step 1 and applying the exponential Markov inequality to \((1-\tau)X_k-\tau Y_k\), the optimizing transform parameter is \((u-\tau)/(2\tau(1-\tau))\). Consequently

\[
 p_k\le \exp\{-n D(u\Vert\tau)\},\qquad
 D(u\Vert\tau)=u\log\frac{u}{\tau}+(1-u)\log\frac{1-u}{1-\tau}.
\]

For \(u\) near \(\tau\), Taylor's theorem gives

\[
 D(u\Vert\tau)=\frac{(u-\tau)^2}{2\tau(1-\tau)}+O((u-\tau)^3).
\]

**3. Uniform moderate-deviation lower estimate.** Write \(u=\tau+c\sqrt{\log r/r}+O(r^{-1})\), where \(c\) ranges over any compact subset of \((0,\infty)\). With \(a=nu\), \(d=n(1-u)\), the beta density at \(\tau\), from Stirling's formula uniformly in this range, is

\[
 f_{a,d}(\tau)=(1+o(1))
 \sqrt{\frac{n}{2\pi}}\frac{\sqrt{u(1-u)}}{\tau(1-\tau)}
 \exp\{-nD(u\Vert\tau)\}.
\]

Its logarithmic derivative at \(\tau\) is \(n(u-\tau)/(\tau(1-\tau))+O(1)\). Integration of the beta density to the left of \(\tau\) is localized on width \(\tau(1-\tau)/[n(u-\tau)]\): on this width the relative change of the logarithmic derivative is \(o(1)\), and its remaining left tail is negligible by concavity of the beta log-density. Because \(n(u-\tau)^2\asymp\log r\to\infty\), this one-sided Laplace estimate is uniform. Therefore

\[
 p_k=(1+o(1))
 \frac{\sqrt{\tau(1-\tau)}}{c\sqrt{\pi b\log r}}
 r^{-\frac{bc^2}{4\tau(1-\tau)}}.
\]

This estimate is an asymptotic **single-look** probability; no independence assumption about successive adapted bases is used. The conditional fresh-probe law in Step 1 supplies the survival-product identity.

**4. Sharp first-acceptance location.** Set \(k_0=(1-\tau)r\), \(s_r=\sqrt{r\log r}\), and \(c_*=\sqrt{2\tau(1-\tau)/b}\). For every fixed \(c>c_*\), the event \(K_r\le k_0-cs_r\) requires an accepted look at or before that rank. The Chernoff bound in Step 2 and monotonicity of \(D(u\Vert\tau)\) for \(u>\tau\) imply that the largest acceptance probability among these looks lies at the rightmost eligible rank. At that rank, \(nD(u\Vert\tau)=[bc^2/(4\tau(1-\tau))+o(1)]\log r\). Moreover, strict convexity of \(D\) implies that successive earlier looks, separated by \(b\) ranks, increase the Chernoff exponent by at least

\[
 n\,\frac{b}{r}D'(\tau+c\sqrt{\log r/r})
 =\Theta(\sqrt{\log r/r}),
\]

uniformly up to the endpoints (the displayed derivative is positive for large \(r\)). Summing the resulting geometrically decreasing upper bounds over all earlier looks yields

\[
 \mathbb P\{K_r\le k_0-cs_r\}
 \le O\!\left(\sqrt{\frac r{\log r}}\right)
 r^{-\frac{bc^2}{4\tau(1-\tau)}+o(1)}\longrightarrow0.
\]

The limit holds since \(bc^2/[4\tau(1-\tau)]>1/2\).

Conversely, fix \(0<c<c_*\). Choose \(h>0\) such that \(c+h<c_*\). In the interval of eligible ranks

\[
 k_0-(c+h)s_r\le k\le k_0-cs_r
\]

there are \(\Theta(s_r/b)\) looks. By the uniform estimate in Step 3, each has conditional acceptance probability at least \(r^{-\frac{b(c+h)^2}{4\tau(1-\tau)}+o(1)}\) up to a logarithmic factor. The sum of these probabilities diverges because the exponent is strictly less than \(1/2\). Therefore the conditional survival product across the interval is at most the exponential of minus a divergent sum and tends to zero. In particular \(\Pr\{K_r\ge k_0-cs_r\}\to0\). Combining both sides for every \(c\) straddling \(c_*\) proves the asserted convergence in probability.

**5. Failure of the actual tolerance.** The preceding limit implies \(k_0-K_r\to+\infty\) in probability. The smallest admissible successful rank \(k_*\) differs from \(k_0\) by less than \(b\), so \(\Pr\{K_r<k_*\}\to1\). At every such rank, the actual relative-squared Frobenius projection error is strictly above \(\tau\), completing the proof. \(\square\)

## Verification

The included `verify.py` tests the beta/chi-square law against exact binomial identities at integer beta parameters, verifies the first-passage probabilities and the finite false-acceptance formula, simulates the actual adaptive QR procedure with independent Gaussian looks for small ranks, and checks the predicted moderate-deviation exponent numerically. Run `python verify.py` in an environment with Python 3, NumPy and SciPy. It prints a count of passed assertions. The finite checks are supplementary to Steps 1–5 and cannot certify the infinite-rank limit.

## Relationship to prior work

Do and Chen (2026) introduce the single-node Gaussian residual-versus-total Frobenius stopping ratio and prove the fresh look's independence, which are **pre-existing premises** of this calculation. Their full text, Sections 2.2 and 4.3–4.5 and Appendix A.2, was inspected. The derived contribution is the exact whole-run first-passage law and the sharp early-stop scale for a flat-spectrum family; these are not asserted by their per-look unbiasedness and concentration results. Their practical denominator is averaged over earlier batches, and later level-wise safeguards change the tested random process. Therefore this result makes no claim about the deployed full algorithm.

Gorman et al. (2018/2019) treat adaptive HSS random sampling, absolute/relative Gaussian Frobenius stopping tests and probabilistic concentration; these are background rather than novelty claims. Smith, Do and Chen (2026) study an adjoint-free adaptive low-rank method with a different final row-energy pruning mechanism; exact false-pruning probabilities for that distinct mechanism do not imply this successive fresh-look first-passage law. Penke and Herten (2026) instead maintain the actual Frobenius residual via Householder QB updates and stop using deterministic residual bookkeeping, so their superficially similar adaptive rank method does not obey the present random stopping ratio. The beta-gamma identity, Chernoff bound and one-sided Laplace method are classical tools, not new probability theorems. A previously published general sequential triangular-array extreme-value theorem could imply the asymptotic after nontrivial specialization; historical priority has not been conclusively excluded.

## Limitations

The probability-one failure limit concerns fixed batch size, fixed relative tolerance strictly between zero and one, flat nonzero singular values, unmodified same-block numerator and denominator, independent real Gaussian batches and exact rank increments. It is not a lower bound for algorithms with confidence-adjusted stopping, an averaged denominator, a separate validation batch, rank pruning, freeze margins, non-Gaussian probes, or hierarchical coupling. Finite-rank probabilities may be substantially below one and convergence in rank is slow. No bound on full HSS factorization or solve residuals is asserted, and the theorem does not claim novelty for the underlying beta distributions or generic multiple-look effects.

## References

1. E. Do and C. Chen, *Simultaneous Matrix-Free HSS Compression and Factorization with Adaptive Ranks*, arXiv:2610.16913v1, first posted 2026-10-12, Sections 2.2, 4.3–4.5 and Appendix A.2. https://arxiv.org/html/2610.16913v1
2. C. Gorman, G. Chávez, P. Ghysels, T. Mary, F.-H. Rouet, and X. S. Li, *Matrix-free construction of HSS representation using adaptive randomized sampling*, arXiv:1810.04125, first posted 2018-10-09; journal version *Robust and Accurate Stopping Criteria for Adaptive Randomized Sampling in Matrix-Free Hierarchically Semiseparable Construction*, SIAM Journal on Scientific Computing 41 (2019). https://arxiv.org/abs/1810.04125
3. A. Smith, E. Do and C. Chen, *Adaptive, Matrix-Free Low-Rank Approximation*, arXiv:2607.06758, first posted 2026-07-07. https://arxiv.org/html/2607.06758v1
4. C. Penke and A. Herten, *A GPU-Accelerated Blocked Adaptive Randomized Range Finder Based on an Implicit Householder QR Decomposition*, arXiv:2608.28941, first posted 2026-08-28, Sections II–IV. https://arxiv.org/html/2608.28941v2
