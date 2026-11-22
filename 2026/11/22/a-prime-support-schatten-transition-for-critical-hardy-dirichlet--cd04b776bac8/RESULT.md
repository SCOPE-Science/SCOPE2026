# A prime-support Schatten transition for critical Hardy–Dirichlet composition limits

## Finding

Let \(r\ge1\), let \(p_1,\ldots,p_r\) be distinct primes, and choose \(\theta_j>0\) with \(\sum_{j=1}^{r}\theta_j=1\). On the Hardy–Hilbert space \(\mathcal H^2\) of Dirichlet series, define
\[
\varphi_{h,\boldsymbol\theta}(s)=\tfrac12+h+h\sum_{j=1}^{r}\theta_jp_j^{-s},\qquad h>0.
\]
Write \(\mathcal H_{\boldsymbol\theta}\) for the positive critical **coefficient-side** operator limit of \(2hC_{\varphi_{h,\boldsymbol\theta}}C_{\varphi_{h,\boldsymbol\theta}}^*\) under the standard coefficient identification. The existence of this limit and the multiprime compactness assertion were established previously. Here its Schatten ideals have a sharp prime-support transition:
\[
\boxed{\begin{array}{c|c}
 r=1 & \mathcal H_{\boldsymbol\theta}\text{ is noncompact},\\
 r=2 & \mathcal H_{\boldsymbol\theta}\in\mathcal S_p\iff p>1,\\
 r\ge3 & \mathcal H_{\boldsymbol\theta}\in\mathcal S_1.
\end{array}}
\]
For \(r=2\), put \(\boldsymbol\theta=(u,1-u)\), where \(0<u<1\). The natural total-degree compression \(B_u\) has the explicit logarithmic trace residue
\[
\boxed{\operatorname{Tr}(P_{\le N}B_uP_{\le N})
=\frac{\log N}{2\pi\sqrt{u(1-u)}}+O_u(1),\qquad N\to\infty.}
\]
Here \(P_{\le N}\) projects onto degrees \(0,1,\ldots,N\). The positive coefficient quantifies the sharp failure of trace-class membership.

## Assumptions and scope

The Hilbert space \(\mathcal H^2\) consists of \(f(s)=\sum_{n\ge1}a_n n^{-s}\) with \(\sum_{n\ge1}|a_n|^2<\infty\). The primes are distinct and all displayed weights are fixed and strictly positive, with total weight one. The symbols act boundedly for each \(h>0\). The limit is taken in the coefficient space indexed by nonnegative prime multiindices; no claim is made about a trace-norm limit as \(h\downarrow0\). Schatten membership of \(\mathcal H_{\boldsymbol\theta}\) is distinct from Schatten membership of the original \(C_{\varphi_{h,\boldsymbol\theta}}\). For \(r\ge3\) the conclusion is trace class, without claiming its optimal quasi-Schatten threshold below one.

Define the positive binomial matrix and the collision probabilities
\[
H_{nm}=\binom{n+m}{n}2^{-(n+m)},\qquad
c_n^2=\sum_{\substack{\alpha\in\mathbb N_0^r\\|\alpha|=n}}
\left(\frac{n!}{\alpha!}\prod_{j=1}^{r}\theta_j^{\alpha_j}\right)^2,
\qquad n,m\ge0.
\]
Set \(D=\operatorname{diag}(c_0,c_1,\ldots)\) and \(B=DHD\). The nonzero spectral part of \(\mathcal H_{\boldsymbol\theta}\) is unitarily equivalent to \(B\); thus the claims can be proved entirely for \(B\). This coefficient reduction is established in the cited critical-norm work and is also verified below directly from the matrix entries.

## Proof

**1. Exact reduction and boundedness.** The critical coefficient matrix from the elementary Dirichlet expansion is
\[
(\mathcal H_{\boldsymbol\theta})_{\alpha\beta}
=(-1)^{|\alpha|+|\beta|}
\frac{(|\alpha|+|\beta|)!}{\alpha!\beta!}
\prod_{j=1}^{r}\left(\frac{\theta_j}{2}\right)^{\alpha_j+\beta_j}.
\]
Within each fixed total degree, this is rank one. An orthonormal unit vector along the coefficient vector
\(\bigl((\boldsymbol\theta/2)^\alpha/\alpha!\bigr)_{|\alpha|=n}\)
identifies its nonzero compression with the signed version of \(DHD\); conjugating by \(e_n\mapsto(-1)^ne_n\) removes the signs. The matrix \(H\) is positive because
\[
H_{nm}=\int_0^\infty e^{-x}\frac{(x/2)^n}{n!}\frac{(x/2)^m}{m!}\,dx.
\]
It is bounded with \(\|H\|\le2\): for \(0<q<1\), the positive matrices \(\bigl(\binom{n+m}{n}(q/2)^{n+m}\bigr)\) have norm \(2/(1+\sqrt{1-q^2})\le2\), as follows from their Laguerre-kernel diagonalization; passing to finite quadratic forms as \(q\uparrow1\) yields the bound for \(H\). Hence \(B\) is bounded and positive.

**2. Sharp collision asymptotic.** The number \(c_n^2\) is the collision probability for two independent multinomial random vectors with \(n\) trials and category probabilities \(\boldsymbol\theta\). By Fourier inversion, fixing the last phase at zero,
\[
c_n^2=\frac1{(2\pi)^{r-1}}\int_{[-\pi,\pi]^{r-1}}
\left|\theta_r+\sum_{j=1}^{r-1}\theta_j e^{it_j}\right|^{2n}\,d\boldsymbol t.
\]
For \(r\ge2\), the modulus has its unique maximum one at the origin modulo the torus. Its square is
\[
1-\boldsymbol t^T\Sigma\boldsymbol t+O(|\boldsymbol t|^3),\qquad
\Sigma=\operatorname{diag}(\theta_1,\ldots,\theta_{r-1})-
(\theta_i\theta_j)_{1\le i,j<r}.
\]
The matrix-determinant lemma gives \(\det\Sigma=\prod_{j=1}^r\theta_j>0\). Uniform exponential decay away from the maximizer, a quadratic Gaussian bound near it, and rescaling by \(\sqrt n\) justify the multivariate Laplace estimate
\[
\boxed{c_n^2\sim\frac{1}{(4\pi n)^{(r-1)/2}\sqrt{\prod_{j=1}^{r}\theta_j}}.}\tag{1}
\]
For fixed weights the smooth nondegenerate stationary point also gives relative error \(O(n^{-1})\), by the usual even-order Gaussian expansion (odd terms integrate to zero). This quantitative remainder is needed only for the stated \(O(1)\) trace remainder. For \(r=1\), one has exactly \(c_n=1\).

**3. Trace and compactness thresholds.** Stirling's formula gives
\[
H_{nn}=\binom{2n}{n}4^{-n}=\frac1{\sqrt{\pi n}}\bigl(1+O(n^{-1})\bigr).
\]
As \(B\ge0\), its trace is finite precisely when its diagonal sum converges. Equations (1) and the displayed diagonal formula imply
\[
B_{nn}\sim\frac{1}{(4\pi)^{(r-1)/2}\sqrt{\pi\prod_j\theta_j}}n^{-r/2}.
\]
Thus \(B\in\mathcal S_1\) for \(r\ge3\), whereas \(B\notin\mathcal S_1\) for \(r=2\). In the two-prime case this yields
\[
B_{nn}=\frac{1}{2\pi\sqrt{u(1-u)}}\frac1n+O_u(n^{-2}),
\]
which sums to the claimed logarithmic trace law. For \(r\ge2\), (1) gives \(c_n\to0\), hence \(D\) and \(DHD\) are compact. When \(r=1\), \(B=H\) is not compact: let \(v^{(N)}\) be the normalized indicator of \([N,2N]\) in \(\ell^2\). This sequence is weakly null. The elementary central-binomial local estimate
\[
\binom{n+m}{n}2^{-(n+m)}\ge cN^{-1/2}
\quad(N\le n,m\le2N,\ |n-m|\le\sqrt N)
\]
with a fixed \(c>0\), gives \(\langle Hv^{(N)},v^{(N)}\rangle\ge c'>0\). Therefore \(H\) is not compact.

**4. Every Schatten exponent above one in the two-prime case.** Let \(R=B^{1/2}\), so \(B=R^*R\). For \(j\ge0\), let \(P_j\) project onto indices \(2^j\le n<2^{j+1}\), with \(P_{-1}\) projecting onto index zero. From \(\|H\|\le2\), the collision asymptotic and positivity,
\[
\|RP_j\|^2=\|P_jBP_j\|\le2\sup_{2^j\le n<2^{j+1}}c_n^2\le C2^{-j/2},
\]
while
\[
\|RP_j\|_{\mathcal S_2}^2
=\operatorname{Tr}(P_jBP_j)=\sum_{2^j\le n<2^{j+1}}B_{nn}\le C.
\]
For any fixed \(p>1\), the elementary singular-value inequality
\(\|T\|_{\mathcal S_{2p}}^{2p}\le\|T\|^{2p-2}\|T\|_{\mathcal S_2}^2\)
therefore yields
\[
\|RP_j\|_{\mathcal S_{2p}}\le C_p2^{-j(p-1)/(4p)}.
\]
The sum of these bounds over \(j\) converges. The finite partial sums of \(R\sum_{j\le J}P_j\) therefore converge in \(\mathcal S_{2p}\); they converge strongly to \(R\), so \(R\in\mathcal S_{2p}\) and \(B=R^*R\in\mathcal S_p\). Conversely, \(0<p\le1\) implies \(\mathcal S_p\subseteq\mathcal S_1\); failure of trace class excludes every such \(p\). This completes the sharp two-prime criterion.

## Verification

The self-contained script `check_collision.py` checks the exact multinomial collision sums for two and three prime weights, their Gaussian asymptotic constants, the exact central-binomial diagonal, positivity of finite compressions and consistency of spectral and diagonal traces. The finite checks are illustrative, not proof of the infinite ideal classification. Reproduce with Python 3, NumPy, and `python check_collision.py`; the file `requirements.txt` gives the minimal dependency. The proof uses only Fourier Laplace asymptotics, the bounded binomial Hankel matrix, positive traces and dyadic Schatten estimates.

## Relationship to prior work

Bayart–Kouroupis (arXiv:2306.05733, 2023-06-09) supplies the motivating Schatten-ideal theory for Dirichlet-series composition operators. Fang–Guo–Mishra–Muthukumar (arXiv:2608.26041, 2026-08-26), Theorem 3.9 and Proposition 3.10, establishes the exact critical limiting matrix, its reduction \(DHD\), and qualitative multiprime compactness; these are credited, not claimed new. The present calculation adds the local-Gaussian collision constant, a *sharp* two-prime \(\mathcal S_p\) threshold, the explicit logarithmic trace residue, and nuclearity starting with three active primes. A related published two-prime fourth-Schatten cusp treats a different scaling regime: fixed amplitudes as the boundary translation tends to zero, rather than the critical coefficient-limit ideals here.

## Limitations

No sharp \(\mathcal S_p\) threshold below \(p=1\) is asserted for three or more active primes. The results concern the critical limiting operator, not the Schatten ideals of an individual original composition operator at fixed positive \(h\). The \(O_u(1)\) remainder is for fixed \(0<u<1\), not uniformly as an amplitude vanishes. The cited structural reduction is independently checked from the coefficient entries, but the existence of the operator-norm limit is prior work. The originality assessment is conditional on the inspected primary literature; unindexed results on weighted binomial Hankel operators remain a historical-priority risk. No independent mathematical audit has been performed.

## References

- F. Bayart and A. Kouroupis, *Schatten class composition operators on the Hardy space of Dirichlet series and a comparison-type principle*, arXiv:2306.05733, first posted 2023-06-09, https://arxiv.org/abs/2306.05733.
- X. Fang, F. Guo, A. Mishra and P. Muthukumar, *Critical Norm Profiles for Finite-Prime Composition Operators on the Hardy Space of Dirichlet Series*, arXiv:2608.26041, first posted 2026-08-26, https://arxiv.org/abs/2608.26041, especially Theorem 3.9 and Proposition 3.10.
- *A sharp two-prime Schatten-four boundary cusp for Dirichlet composition operators*, publicly available research result, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-a-sharp-two-prime-schatten-four-boundary-cusp-for-dirichlet-comp--c52ca777e421 (different fixed-amplitude boundary regime).
