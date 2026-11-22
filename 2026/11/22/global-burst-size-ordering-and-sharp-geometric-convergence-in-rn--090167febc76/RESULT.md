# Global burst-size ordering and sharp geometric convergence in RNA-binding autoregulation

## Finding

For the fast-mRNA, two-state RNA-binding autoregulation law of Jia [1], the **entire conditional protein-burst distribution** is strictly ordered by the pre-burst free-protein count. The direction depends only on the relative translation-to-decay ratios of free and bound mRNA, not on the protein count, the burst threshold, or the binding/unbinding time scales. In addition, the burst law converges to a geometric law with an explicitly bounded total-variation error of optimal order \(n^{-1}\) whenever the regulatory feedback is nonzero.

Precisely, let \(K_n\) denote the number of newly translated proteins in a burst started with \(n\in\mathbb N_0\) free proteins, and put \(\Delta=u_1v_0-u_0v_1\). For every \(n\ge0\) and every integer \(k\ge1\),
\[
\operatorname{sgn}\bigl(\Pr(K_{n+1}\ge k)-\Pr(K_n\ge k)\bigr)=\operatorname{sgn}(\Delta).
\]
If \(\Delta=0\), all the distributions are identical and geometric. For \(n\ge1\), let \(p_i=u_i/(u_i+v_i)\), \(p_*=\max\{p_0,p_1\}<1\), and \(U_i=u_i+v_i\). Then, with geometric probabilities \(\Pr(G=k)=(1-p_1)p_1^k\), \(k=0,1,\ldots\),
\[
d_{\rm TV}(\mathcal L(K_n),\mathcal L(G))
\le \frac{(U_1+b)(u_0+p_1U_0)}{aU_1(1-p_*)^2}\,\frac1n.
\]
Moreover, when \(\Delta\ne0\),
\[
d_{\rm TV}(\mathcal L(K_n),\mathcal L(G))\ge
\frac{|\Delta|(U_1+b)}{U_1[U_0(U_1+b)+anU_1]}
\sim \frac{|\Delta|(U_1+b)}{aU_1^2}\,\frac1n,
\]
so the reciprocal-protein convergence rate is sharp.

## Assumptions and scope

Parameters satisfy \(u_0>0\), \(v_0>0\), \(v_1>0\), \(u_1\ge0\), and \(a,b>0\). The parameters \(u_0,u_1\) are translation rates of free and bound mRNA, \(v_0,v_1\) their degradation rates, and \(a,b\) binding/unbinding rates. Define \(D_j=U_0(U_1+b)+ajU_1\) and
\[
T_j=\frac1{D_j}\begin{pmatrix}
(U_1+b)u_0&aju_1\\
bu_0&(U_0+aj)u_1
\end{pmatrix},\qquad j\ge0.
\]
The conditional burst-size law is defined by the source's exact fast-mRNA reduced model [1, Eq. (5)]:
\[
\Pr(K_n=k)=(1,0)T_nT_{n+1}\cdots T_{n+k-1}(I-T_{n+k})\binom11,
\qquad k\ge0.
\]
The empty product is the identity. Equivalently the survival tails are \(S_k(n):=\Pr(K_n\ge k)=(1,0)T_n\cdots T_{n+k-1}\binom11\) for \(k\ge1\) and \(S_0(n)=1\). This is a theorem about the *reduced burst law*, not a finite-timescale error bound for the full biochemical master equation or a claim about its steady-state protein population.

## Proof

**1. Positivity and normalization.** Each \(T_j\) has nonnegative entries; its row sums are convex combinations of \(p_0=u_0/U_0\) and \(p_1=u_1/U_1\). Hence \(\|T_j\|_\infty\le p_*<1\). Consequently \(S_k(n)\le p_*^k\to0\), and the specified probabilities are nonnegative and sum to one, even when \(u_1=0\).

**2. Sign-preserving cone.** For a vector \(v=(f,g)^{\mathsf T}\), set \(R(v)=U_0u_1g-U_1u_0f\). Direct multiplication and differentiation with respect to real \(j\ge0\) give
\[
(T_jv)_B-(T_jv)_F=\frac{R(v)}{D_j},\qquad
\frac{d}{dj}T_jv=\frac{aR(v)}{D_j^2}\binom{U_1+b}{b}.
\]
If \(\Delta=U_0u_1-U_1u_0>0\), the cone \(C_+=\{(f,g):g\ge f\ge0\}\) is mapped into itself by each \(T_j\), since \(R(v)\ge\Delta f\ge0\). For \(\Delta<0\), \(C_-=\{(f,g):f\ge g\ge0\}\) is preserved, since \(R(v)\le\Delta f\le0\). On either cone the mapping \(j\mapsto T_jv\) is componentwise increasing or decreasing, respectively. If \(f>0\), those comparisons are strict.

**3. Ordering of every tail.** Define \(V_0(j)=(1,1)^{\mathsf T}\) and \(V_{k+1}(j)=T_jV_k(j+1)\). Inductively \(V_k(j)\) belongs to the appropriate cone, its first coordinate is positive, and it is componentwise monotone with \(j\) in the sign of \(\Delta\). Indeed, in the positive case,
\[
T_{j+1}V_k(j+2)\ge T_{j+1}V_k(j+1)\ge T_jV_k(j+1),
\]
with a strict first-coordinate inequality; both inequalities reverse in the negative case. Since \(S_k(j)=(V_k(j))_F\), the asserted strict tail ordering follows. If \(\Delta=0\), then \(T_j(1,1)^{\mathsf T}=p_1(1,1)^{\mathsf T}\) for every \(j\), and \(S_k(n)=p_1^k\) identically.

**4. Uniform geometric approximation.** Let \(T_\infty=\begin{pmatrix}0&p_1\\0&p_1\end{pmatrix}\). Direct subtraction gives, for \(j\ge1\),
\[
\|T_j-T_\infty\|_\infty
=\frac{(U_1+b)(u_0+p_1U_0)}{D_j}
\le\frac{C}{j},\qquad C=\frac{(U_1+b)(u_0+p_1U_0)}{aU_1}.
\]
A telescoping matrix-product expansion, using \(\|T_j\|_\infty\le p_*\) and \(\|T_\infty\|_\infty=p_1\le p_*\), yields
\[
|S_k(n)-p_1^k|\le \frac Cn\,k p_*^{k-1}.
\]
For nonnegative integer laws, total variation is bounded by the sum of absolute differences of positive-index survival tails: \(d_{\rm TV}\le\sum_{k\ge1}|S_k(n)-p_1^k|\). The geometric series \(\sum_{k\ge1}kp_*^{k-1}=(1-p_*)^{-2}\) gives the upper bound.

**5. Sharpness.** The exact first tail is \(S_1(n)=[(U_1+b)u_0+anu_1]/D_n\), and simple algebra gives
\[
S_1(n)-p_1=-\frac{\Delta(U_1+b)}{U_1D_n}.
\]
The event \(\{K\ge1\}\) witnesses the stated total-variation lower bound, whose positive asymptotic coefficient is explicit when \(\Delta\ne0\). This proves \(d_{\rm TV}=\Theta(n^{-1})\) for nonzero feedback, and zero distance for \(\Delta=0\).

## Verification

A standalone exact-rational checker, `CHECK.py`, reconstructs the burst matrices independently from the displayed parameters, tests 6,000 distinct finite tail comparisons across both feedback signs and neutral cases, and checks the one-step identity including the complete translation-repression boundary \(u_1=0\). It also performs independent symbolic checks of the cone-difference and derivative identities, matrix limiting difference and finite-step bounds. These computations corroborate the algebra; the all-parameter and all-threshold assertions are proved by the preceding cone and matrix-product arguments, not inferred from testing.

## Relationship to prior work

Jia [1] derives the two-state, state-dependent burst-size law used as the starting definition, the unregulated geometric case, and an *approximate* large-initial-protein geometric shape. Those are prior results, not claimed here. The present theorem supplies a whole-distribution stochastic order for every initial count and every tail, and an explicit uniform total-variation estimate of sharp reciprocal-protein order for the same biochemical law. The source's figures and stationary mean/noise comparisons do not establish these quantified laws. Bokes–Singh [2] analyzes continuous-concentration, piecewise-deterministic burst-size feedback and noise suppression, rather than this exact two-state discrete RNA-binding product law. Later general treatments of bursting feedback and steady-state statistics [3] remain a plausible place for related principles, but do not automatically imply this specified comparison and rate.

## Limitations

This result assumes the exact *fast-mRNA reduction* of [1] and positive mRNA degradation and binding/unbinding rates; it does not bound errors in that reduction, characterize the full protein stationary law, or claim that protein-burst sizes in real cells satisfy these assumptions. Its novelty assessment is literature-bounded; independent historical priority and independent scientific audit have not been performed. The total-variation constant is an explicit universal bound, not asserted optimal; only its order \(n^{-1}\) is sharp.

## References

[1] Chen Jia, *Exact Stochastic Theory of Post-Transcriptional Gene Autoregulation Mediated by RNA-Binding Proteins*, arXiv:2611.18062v1 (first public release 2026-11-13), https://arxiv.org/pdf/2611.18062 . Especially Eq. (5) and the burst-size discussion on p. 2, and the derivations in the End Matter.

[2] Pavol Bokes and Abhyudai Singh, *Gene expression noise is affected differentially by feedback in burst frequency and burst size*, Journal of Mathematical Biology 74 (2017), 1483–1509; first public preprint https://arxiv.org/abs/1602.08568 ; author-hosted https://davinci.fmph.uniba.sk/~bokes3/papers/bokes2016gene.pdf .

[3] Pavol Bokes, *Exact and WKB-approximate distributions in a gene expression model with feedback in burst frequency, burst size, and protein stability*, Discrete and Continuous Dynamical Systems - B 27 (2022), 2129–2145, https://doi.org/10.3934/dcdsb.2021126 .
