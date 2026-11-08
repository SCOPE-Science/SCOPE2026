# A universal log-periodic gradient envelope for two-mode Barzilai–Borwein descent

## Finding

The logarithmic convergence rate of matched BB1 descent on a two-eigenvalue quadratic has an exact, nonconstant, log-periodic asymptotic profile. Unlike the already-known qualitative two-dimensional Barzilai–Borwein superlinear convergence and the already-known recurrence for the ratio of spectral energies, this statement describes the **norm itself at every sufficiently late iteration** on the finer doubly-exponential scale.

Let \(0<\ell<L\), \(Q=\operatorname{diag}(L,\ell)\), \(f(x)=\tfrac12 x^TQx\), and \(g_0=Qx_0\). Apply the matched BB1 gradient iteration
\[
 x_{k+1}=x_k-\alpha_k g_k,\qquad g_k=Qx_k,\qquad
 \alpha_0=\frac{\|g_0\|_2^2}{g_0^TQg_0},\quad
 \alpha_k=\frac{\|g_{k-1}\|_2^2}{g_{k-1}^TQg_{k-1}}\quad(k\ge1).
\]
Assume both spectral gradient components are nonzero, and set
\[
 \varepsilon_0=\frac{(g_0^{(1)})^2}{(g_0^{(2)})^2},\quad
 R=\sqrt2,\quad \theta=\arccos\!\left(\frac1{2\sqrt2}\right),\quad
 B(\phi)=\cos\phi-\frac3{\sqrt7}\sin\phi.
\]
Define the absolutely and uniformly convergent series
\[
 U(\phi)=\sum_{m=2}^{\infty}R^{-m}[B(\phi-m\theta)]_+,\qquad
 H(\phi)=\min\{U(\phi),U(\phi+\pi)\},\qquad [z]_+=\max\{z,0\}.
\]
Then \(H\) is strictly positive, continuous, nonconstant and \(\pi\)-periodic. For every fixed \(\varepsilon_0\ne1\), as the integer \(n\to\infty\),
\[
 \boxed{\displaystyle
 -2^{-n/2}\log\frac{\|g_n\|_2}{\|g_0\|_2}
 =|\log\varepsilon_0|\,H(n\theta)+O_{L,\ell,g_0}(n2^{-n/2}).}
\]
In particular, writing \(h_- =\min_{\phi\in[0,\pi]}H(\phi)\) and \(h_+=\max_{\phi\in[0,\pi]}H(\phi)\),
\[
 0<h_-<h_+<\infty,\qquad h_+\ge 2h_-,
\]
and
\[
 \liminf_{n\to\infty}\frac{-\log(\|g_n\|_2/\|g_0\|_2)}{2^{n/2}}=|\log\varepsilon_0|h_-,\qquad
 \limsup_{n\to\infty}\frac{-\log(\|g_n\|_2/\|g_0\|_2)}{2^{n/2}}=|\log\varepsilon_0|h_+.
\]
Thus the decay is \(\exp[-\Theta(2^{n/2})]\) along **all** sufficiently late integer iterates, with persistent angular oscillations of its leading coefficient. The coefficient depends only on initial spectral imbalance, not on the two Hessian eigenvalues; the latter affect lower-order terms. Numerically, \(H(0)\approx0.4095731403\) and \(H(-2\theta)=2H(0)\approx0.8191462806\), with these decimals illustrative rather than needed for the proof.

In the balanced case \(\varepsilon_0=1\), instead
\[
 \|g_n\|_2=\left(\frac{L-\ell}{L+\ell}\right)^n\|g_0\|_2\quad\text{for all }n\ge0.
\]
The conclusion concerns exact arithmetic; all assertions apply to every initial gradient having both components nonzero.

## Assumptions and scope

The Hessian is the real symmetric positive definite diagonal matrix \(Q=\operatorname{diag}(L,\ell)\), with exactly two **distinct** eigenvalues \(L>\ell>0\). The quadratic may be translated to a nonzero minimizer; the present choice sets it at zero. The first step is the matched (undelayed) BB1 Rayleigh step, and every subsequent BB1 step uses the preceding gradient. The ratio \(\varepsilon_0\) is positive; no assumption is made on the component signs. The theorem does not assert a uniform superlinear constant as \(\varepsilon_0\to1\). If a component starts at zero, the first step solves the system exactly; if \(L=\ell\), the matched first step also solves it exactly. These cases are excluded from the nontrivial profile.

## Proof

1. **Exact two-mode dynamics.** Put \(Q=\operatorname{diag}(L,\ell)\) and \(\Delta=L-\ell>0\). Since \(g_{k+1}=(I-\alpha_kQ)g_k\), a step computed from spectral ratio \(e>0\) multiplies the two components by
\[
 1-\frac{L(1+e)}{Le+\ell}=-\frac\Delta{Le+\ell},\qquad
 1-\frac{\ell(1+e)}{Le+\ell}=\frac{\Delta e}{Le+\ell}.
\]
These multipliers never vanish when the two components are nonzero, so there is no finite termination. With \(\varepsilon_k=(g_k^{(1)}/g_k^{(2)})^2\), the first matched step gives \(\varepsilon_1=\varepsilon_0^{-1}\), and all later steps give
\[
 \varepsilon_{k+1}=\varepsilon_k\varepsilon_{k-1}^{-2}\quad(k\ge1).
\]
The same recurrence was established in earlier BB literature and is explicitly discussed in the motivating 2026 paper; it is used as a starting identity, not claimed as novel.

2. **Exact logarithmic modes.** Set \(t=\log\varepsilon_0\) and \(a_0=1,a_1=-1,a_{k+1}=a_k-2a_{k-1}\). Then \(\log\varepsilon_k=t a_k\). The characteristic roots are \((1\pm i\sqrt7)/2=R e^{\pm i\theta}\), so
\[
 a_k=R^kB(k\theta),\qquad
 B(\phi)=\cos\phi-\frac3{\sqrt7}\sin\phi.
\]
At iterations numbered \(j=0,1,\ldots,n-1\), the step uses ratios with indices \(s_0=s_1=0\) and \(s_j=j-1\) for \(j\ge2\). Writing \(K=L/\ell\), exact multiplication yields
\[
 \log|g_n^{(1)}|=\log|g_0^{(1)}|+n\log(\Delta/\ell)
 -\sum_{j=0}^{n-1}\log(1+Ke^{t a_{s_j}}),
\]
\[
 \log|g_n^{(2)}|=\log|g_0^{(2)}|+n\log(\Delta/\ell)
 +\sum_{j=0}^{n-1}\big[t a_{s_j}-\log(1+Ke^{t a_{s_j}})\big].
\]
For fixed \(K>0\), uniformly in real \(z\),
\[
 \log(1+Ke^z)=[z]_++O_K(1),\quad
 \log(1+Ke^z)-z=[-z]_++O_K(1).
\]
Consequently the leading negative logarithms of the two gradient components are the sums of the positive and negative parts of \(t a_j\), respectively, with total error \(O(n)\).

3. **Uniform phase limit.** Dividing by \(R^n\), shifting \(m=n-j\) and extending the geometric series changes either component expression by at most \(O(nR^{-n})\). Uniformly in integer \(n\),
\[
 -R^{-n}\log|g_n^{(1)}|= [t>0]\,tU(n\theta)+[t<0]\,|t|U(n\theta+\pi)+O(nR^{-n}),
\]
with the analogous formula with \(U(n\theta)\) and \(U(n\theta+\pi)\) swapped for the second component. Here the bracket notation \([t>0]\) denotes an ordinary zero-or-one indicator. Since the logarithm of the Euclidean gradient norm differs from the maximum component logarithm by at most \(\tfrac12\log2\), the minimum of the two scaled negative logarithms is exactly \(|t|H(n\theta)\) up to the stated error. Subtracting \(\log\|g_0\|_2/R^n\) does not alter it.

4. **Strict positivity and genuine phase variation.** The rotation angle is irrational relative to \(\pi\): otherwise \(2\cos\theta=1/\sqrt2\) would be an algebraic integer, whereas its algebraic norm to \(\mathbb Q\) is \(-1/2\). Therefore \(\{m\theta\bmod2\pi\}\) is dense. For each fixed \(\phi\), the values \(B(\phi-m\theta)\) include positive and negative values; hence both series in the definition of \(H\) are positive. Uniform convergence makes \(H\) continuous, so its minimum on the circle is strictly positive.

   For nonconstancy, put \(z=(1-i\sqrt7)/4\). A geometric-series evaluation gives the exact identity
\[
 \sum_{m=2}^\infty R^{-m}B(\phi-m\theta)=-\frac12B(\phi).
\]
At \(\phi=0\) the right side is negative, so \(H(0)=U(0)\). The backward recurrence gives \(a_{-2}=0\), \(a_{-3}=-1/2\); hence \(B(-2\theta)=0\) and \(B(-3\theta)<0\). Shifting the defining sum by two indices shows \(U(-2\theta)=R^2U(0)=2U(0)\). The signed-series identity at \(-2\theta\) makes the two positive-part sums equal, so \(H(-2\theta)=2H(0)>H(0)\). In particular \(h_+\ge2h_-\) and \(h_+>h_-\).

5. **Attainment and exceptions.** Density of the irrational rotation and continuity of \(H\) imply that its minimum and maximum occur as the liminf and limsup along \(n\theta\). The exact profile yields both logarithmic limit laws. Positive \(h_-\) gives \(\|g_n\|_2=\exp[-\Theta(R^n)]\) and \(\limsup_{n\to\infty}(\|g_n\|_2/\|g_0\|_2)^{1/n}=0\). When \(\varepsilon_0=1\), the ratio stays one and every step size is \(2/(L+\ell)\), giving precisely the geometric formula in the finding. This completes the proof.

## Verification

Run the standalone script \(\texttt{python3 verify.py}\) using Python 3's standard library. It checks 252 exact rational identities for spectral ratios and component multipliers, 48 late-iteration log-profile comparisons and two independent phase identities (302 checks total). All computations are independent consistency checks; the proof above establishes the infinitely many iteration and positivity claims. The script computes the gradient logarithm without forming numbers too small for floating-point representation. The profile series is truncated only for numerical checks; its exact theorem definition remains infinite and uniformly convergent.

## Relationship to prior work

Yang and Yuan, *The Sharp Worst-Case Asymptotic Rate of the Barzilai–Borwein Method in* \(\mathbb R^d\) *and Hilbert Spaces*, arXiv:2608.07839v1 (2026), prove a sharp uniform root-rate threshold and state the same BB1 logarithmic ratio dynamics (Section 5). Their later paper arXiv:2609.12084v1 establishes a separate BB Lyapunov identity and uniform \(R\)-linear convergence, not the scaled-log-norm profile. Dai (2013) previously investigated the two-dimensional BB method, the exceptional balanced orbit, and generic \(R\)-superlinear convergence; those facts are not new. The contribution here is the exact universal, nonconstant \(2^{n/2}\)-scaled log-norm profile and its attained oscillatory extrema, which are not implied by the previously stated rate bounds without further analysis of the component products. The 2013 article's full subscription text was not accessible; a priority risk remains for an equivalent full-norm asymptotic in that work.

## Limitations

This is a two-eigenvalue, matched-initialization, exact-arithmetic theorem for BB1. It does not cover arbitrarily many distinct eigenvalues, nonquadratic problems, rounding-induced stagnation, or the BB2 method. The result does not claim novelty for the recurrence, balanced orbit, generic superlinear convergence or the BB1 sharp worst-case geometric envelope. The profile is asymptotic for each fixed nonzero imbalance; its error bound is not uniform as the imbalance tends to zero.

## References

- Shutai Yang and Ya-Xiang Yuan, *The Sharp Worst-Case Asymptotic Rate of the Barzilai–Borwein Method in* \(\mathbb R^d\) *and Hilbert Spaces*, arXiv:2608.07839v1, submitted 2026-08-08. https://arxiv.org/abs/2608.07839
- Shutai Yang and Ya-Xiang Yuan, *Lyapunov Functions and R-Linear Convergence for Quadratic Barzilai–Borwein Dynamics*, arXiv:2609.12084v1, submitted 2026-09-10. https://arxiv.org/abs/2609.12084
- Yu-Hong Dai, *A New Analysis on the Barzilai-Borwein Gradient Method*, Journal of the Operations Research Society of China 1 (2013), 187–198, DOI:10.1007/s40305-013-0007-x. https://link.springer.com/article/10.1007/s40305-013-0007-x
