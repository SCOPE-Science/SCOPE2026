# Exact mean-square rate of planar Gaussian random-direction line search

## Finding

For every real symmetric positive-definite \(2\times2\) matrix \(H\), every deterministic \(x_0\ne0\), and independent identically distributed directions \(u_n\) uniform on the unit circle, the exact-directional-minimization iteration
\[
x_{n+1}=x_n-\frac{u_n^{\mathsf T}Hx_n}{u_n^{\mathsf T}Hu_n}u_n
\]
has an **exact two-state second-moment law** and a universal, initial-state-independent asymptotic expected-objective rate. Write \(\mu\) and \(L\) for the smallest and largest eigenvalues of \(H\), and \(t=\sqrt{L/\mu}\ge1\). In an orthonormal eigenbasis, set \(a_n=\mathbb E[(\sqrt L\,x_{n,1})^2]\) and \(b_n=\mathbb E[(\sqrt\mu\,x_{n,2})^2]\). Then, for every integer \(n\ge0\),
\[
\begin{pmatrix}a_{n+1}\\b_{n+1}\end{pmatrix}
=\frac1{2(t+1)^2}
\begin{pmatrix}t+2&t\\t&t(2t+1)\end{pmatrix}
\begin{pmatrix}a_n\\b_n\end{pmatrix},
\qquad
\mathbb E[f(x_n)]=\tfrac12(a_n+b_n).
\]
The two eigenvalues of this transfer matrix are
\[
\lambda_\pm(t)=\frac{t^2+t+1\pm\sqrt{t^4-t^2+1}}{2(t+1)^2}.
\]
For every deterministic nonzero initial state, the sharp asymptotic factor is
\[
\boxed{\displaystyle \lim_{n\to\infty}\left(\frac{\mathbb E[f(x_n)]}{f(x_0)}\right)^{1/n}=\lambda_+(t).}
\]
For every \(t>1\), this is **strictly smaller** than the tight worst-case conditional one-step factor \(t/(t+1)\); at \(t=1\) they both equal \(1/2\). As \(t\to\infty\),
\[
\lambda_+(t)=1-\frac{3}{2t}+\frac9{4t^2}+O(t^{-3}),
\qquad \frac{t}{t+1}=1-\frac1t+O(t^{-2}).
\]
Thus the leading contraction gap is \(3/2\) times that suggested by iterating the sharp one-step bound, in the high-contrast limit.

## Assumptions and scope

We take \(f(x)=\frac12 x^{\mathsf T}Hx\), with real \(H\succ0\) of order two, and one fresh independent direction per step. A standard bivariate isotropic Gaussian direction gives exactly the same algorithm because the update is invariant under nonzero rescaling of the direction. All expectations are with respect to the sampled directions, with deterministic \(x_0\). The objective minimum is zero. These are exact line-search, unit-step one-dimensional subspace Newton updates; there is no noise in the objective or gradient. No assertion is made about almost-sure rates, higher dimensions, approximate line search or nonlinear objectives.

## Proof

**1. Whitening and rank-one projection.** Orthogonal diagonalization and rescaling of \(H\) reduce to \(H=\operatorname{diag}(t^2,1)\) without changing the direction distribution. Set \(y_n=H^{1/2}x_n\), \(v=H^{1/2}u/\|H^{1/2}u\|\), and \(w=(-v_2,v_1)\). Exact minimization gives \(y_{n+1}=(I-vv^{\mathsf T})y_n=ww^{\mathsf T}y_n\). For \(u=(\cos\theta,\sin\theta)\) with uniform \(\theta\), put
\[
s=w_1^2=\frac{\sin^2\theta}{t^2\cos^2\theta+\sin^2\theta},\qquad w_2^2=1-s.
\]
Independence of \(u_n\) and \(y_n\), together with reflection symmetry of \(\theta\), cancels the expectations of the odd cross terms \(w_1^3w_2\) and \(w_1w_2^3\). Hence the diagonal second moments evolve by the matrix whose entries are \(\mathbb E[s^2]\), \(\mathbb E[s(1-s)]\), \(\mathbb E[(1-s)^2]\).

**2. Exact angular moments.** For every \(a,b>0\), elementary integration of \((a\cos^2\theta+b\sin^2\theta)^{-1}\) over the circle and the identity \(a\cos^2\theta+b\sin^2\theta=D\) show
\[
F(a,b):=\mathbb E_\theta\left[\frac{\sin^2\theta}{a\cos^2\theta+b\sin^2\theta}\right]
=\frac1{\sqrt b(\sqrt a+\sqrt b)}.
\]
Differentiate under the integral (the denominator is bounded below by \(\min\{a,b\}>0\)) to obtain \(\mathbb E[s^2]=-\partial_b F(t^2,b)|_{b=1}=(t+2)/(2(t+1)^2)\). Also \(\mathbb E[s]=1/(t+1)\), so \(\mathbb E[s(1-s)]=t/(2(t+1)^2)\), and \(\mathbb E[(1-s)^2]=1-2\mathbb E[s]+\mathbb E[s^2]=t(2t+1)/(2(t+1)^2)\). This proves the claimed recurrence for every \(n\), not merely for asymptotically large \(n\).

**3. Spectral analysis and sharpness for every start.** The transfer is strictly entrywise positive for every \(t\ge1\), with trace \((t^2+t+1)/(t+1)^2\) and determinant \(t/(2(t+1)^2)\). The quadratic formula gives \(\lambda_\pm\) above. Perron–Frobenius theory implies \(0\le\lambda_-<\lambda_+<1\) and strictly positive left and right Perron eigenvectors. Since \((a_0,b_0)\) is nonnegative and nonzero, its projection on the positive left Perron vector is strictly positive. Thus \(\mathbb E[f(x_n)]\) has strictly positive leading \(\lambda_+^n\) coefficient for every deterministic \(x_0\ne0\), proving the root limit. At \(t=1\), the matrix row sums are \(1/2\), so \(\mathbb E[f(x_n)]=2^{-n}f(x_0)\) exactly.

**4. The gap to the one-step bound.** The conditional one-step expected loss is \(\tfrac12 y_n^{\mathsf T}\operatorname{diag}(1/(t+1),t/(t+1))y_n\); the largest factor \(t/(t+1)\) is attained by a current state along the second whitened eigenvector. However,
\[
\left(t^2+t-1\right)^2-(t^4-t^2+1)=2t(t-1)(t+1)>0\quad(t>1).
\]
Rearranging this identity gives \(\lambda_+(t)<t/(t+1)\). Taylor expansion of the explicit root at infinity gives the stated asymptotics. At \(t=2\), for example, \(\lambda_+=(7+\sqrt{13})/18\approx0.5891972931\), versus the sharp one-step upper bound \(2/3\).

## Verification

`verify.py` is a standalone Python 3 standard-library checker. It tests exact rational traces, determinants, moment constraints and boundary examples; independently approximates the defining angular fourth-moment integrals and the direct one-step covariance update; and verifies iteration-ratio convergence on test cases. The companion `verify_output.txt` records 111 passing deterministic checks. These finite checks support but do not replace the analytic moment identities and Perron argument, which prove the all-parameter, all-time statements.

## Relationship to prior work

The update is the one-column Gaussian specialization of the randomized subspace Newton algorithm of Gower, Kovalev, Lieder and Richtárik (2019), and is equivalent to Gaussian random pursuit with exact line search. This equivalence is established prior work, **not** a claimed discovery. Gower and Richtárik (2015), especially Section 4 and Appendix B, derive the exact two-dimensional **first moment** of the normalized Gaussian projection and an expected-squared-error upper bound obtained by iterating the worst-case one-step contraction. Their first-moment identity does not itself determine the iterated second-moment transfer or its Perron root. Stich, Müller and Gärtner (2011) give random-pursuit convergence theory and numerical quadratic tests without this explicit sharp asymptotic planar second-moment factor. The result above is the exact fourth-projection-moment and long-run refinement for this natural specialization, subject to the precedence limits below.

## Limitations

The proof only concerns independent isotropic directions in dimension two and exact directional minimization. It does not imply analogous rates in higher dimensions, almost-sure rates, uniformly bounded finite-time ratios by \(\lambda_+\) for all initial states, or performance superiority against tuned coordinate sampling. The one-step quantity \(t/(t+1)\) is a valid and sharp **conditional** bound; the finding strictly refines its asymptotic exponent rather than invalidating it. Specialist work on random planar projection products may contain an equivalent reformulation not captured by the checked sources; independent literature review remains appropriate.

## References

- R. M. Gower, D. Kovalev, F. Lieder, and P. Richtárik, *RSN: Randomized Subspace Newton*, first public preprint May 26, 2019, arXiv:1905.10874, https://arxiv.org/abs/1905.10874. Algorithm 1 and Theorem 2.
- R. M. Gower and P. Richtárik, *Randomized Iterative Methods for Linear Systems*, 2015, arXiv:1506.03296, https://arxiv.org/html/1506.03296v5. Sections 4.3, 4.4, 6.3, and Appendix B (Lemma 12).
- S. U. Stich, C. L. Müller, and B. Gärtner, *Optimization of Convex Functions with Random Pursuit*, preprint November 1, 2011, arXiv:1111.0194, https://arxiv.org/abs/1111.0194. Sections 4–6.
- M. Fuji, P.-L. Poirion, and A. Takeda, *Randomized Subspace Regularized Newton Method for Unconstrained Non-convex Optimization*, September 9, 2022, arXiv:2209.04170, https://arxiv.org/abs/2209.04170. Sections 4–5.
