# Oscillatory complex measures and the all-Schatten collapse of Bergman-kernel Cesàro operators

## Finding
For each \(\alpha>-1\) and \(0<s<1/2\), a finite complex measure whose density has the unimodular boundary chirp \(e^{i/(1-t)}\) induces a generalized Bergman-kernel Cesàro operator on \(H^2(\mathbb D)\) belonging to **every** Schatten ideal \(\mathcal S_p\), \(p>0\). The operator induced by its **total variation** does not even send the constant function to \(H^2\). The precise complex moments have a universal stretched-exponential leading law, and the trace and entire Fredholm determinant are independent of the Bergman exponent.

Put
\[
 d\mu_s(t)=(1-t)^{s-1}e^{i/(1-t)}\,dt,\quad
 m_n(s)=\int_0^1t^n\,d\mu_s(t),\quad
 c_j(\alpha)=\frac{(\alpha+2)_j}{j!}.
\]
Then the operator \(T_{\alpha,s}\) below is in \(\bigcap_{p>0}\mathcal S_p\), and
\[
 m_n(s)=\sqrt\pi\,n^{-s/2-1/4}e^{-\sqrt{2n}}
 \exp\!\left(i\left[\sqrt{2n}+\frac12+\pi\left(\frac18-\frac s4\right)\right]\right)
 \left(1+O_s(n^{-1/2})\right),\qquad n\to\infty.
\]
In particular, \(\lim_{n\to\infty} n^{s/2+1/4}e^{\sqrt{2n}}|m_n(s)|=\sqrt\pi\), and, for every complex \(z\),
\[
 \det(I-zT_{\alpha,s})=\prod_{n=0}^{\infty}(1-zm_n(s)),\qquad
 \operatorname{tr}T_{\alpha,s}=(-i)^{s-1}\Gamma(1-s,-i).
\]
The upper incomplete Gamma function is taken with its principal branches. The multiset of nonzero eigenvalues, counted algebraically, is the nonzero part of \(\{m_n(s):n\ge0\}\), independent of \(\alpha\).

## Assumptions and scope
Use normalized area \(dA_\alpha(z)=(\alpha+1)(1-|z|^2)^\alpha\,dx\,dy/\pi\) on the unit disk. Its reproducing kernel at real \(t\in[0,1)\) is \(K_\alpha(t,z)=(1-tz)^{-\alpha-2}\). With \(f\in H^2(\mathbb D)\), define
\[
 (T_{\alpha,s}f)(z)=\int_0^1\frac{f(tz)}{(1-tz)^{\alpha+2}}\,(1-t)^{s-1}e^{i/(1-t)}\,dt.
\]
The integral exists absolutely for each \(|z|<1\) because the total variation \(\|\mu_s\|=1/s\) is finite. This is an operator on the standard coefficient Hilbert space \(H^2\), not an assertion about arbitrary mixed-norm or weighted Bergman domains. The parameter ranges are **every real** \(\alpha>-1\), **every real** \(0<s<1/2\), and every Schatten exponent \(p>0\). All Gamma powers use principal analytic continuation.

## Proof
**1. Exact matrix and the variation obstruction.** Expand the reproducing kernel in absolutely convergent series for \(|z|<1\). If \(f(z)=\sum_{k\ge0}a_kz^k\), the matrix of \(T_{\alpha,s}\) relative to \(1,z,z^2,\ldots\) is lower triangular,
\[
 (T_{\alpha,s})_{nk}=
 \begin{cases}m_n(s)c_{n-k}(\alpha),&0\le k\le n,\\0,&k>n.\end{cases}
\]
The variation measure is \(d|\mu_s|=(1-t)^{s-1}dt\). The coefficient of degree \(n\) in \(T_{\alpha,|\mu_s|}1\) equals
\[
 c_n(\alpha)B(n+1,s)
 \sim\frac{\Gamma(s)}{\Gamma(\alpha+2)}n^{\alpha+1-s}.
\]
Because \(\alpha+1-s>-1/2\) throughout the specified range, these coefficients are not square summable. Thus \(T_{\alpha,|\mu_s|}1\notin H^2\). This is a statement about bounded extension; the positive-measure integral still defines an analytic function.

**2. Precise oscillatory-moment lemma.** Set \(v=(1-t)^{-1}\). Then, for \(n\ge1\),
\[
 m_n(s)=\int_1^\infty \left(1-\frac1v\right)^n v^{-s-1}e^{iv}\,dv.
\]
The integrand is analytic in the sector swept by rotating \(v-1\) from the positive real ray to angle \(\pi/4\), with the indicated principal powers. On large connecting arcs, it is \(O(R^{-s-1})\) times a nonexpanding exponential, and their lengths are \(O(R)\); therefore those contributions tend to zero since \(s>0\). The contour rotation is exact. With \(\eta=e^{i\pi/4}\), substitute \(v=1+\eta\sqrt n\,x\) on the new ray. For \(x\) in any fixed compact subset of \((0,\infty)\), expansion of the logarithm gives
\[
 iv-n\log\!\left(1+\frac1{\eta\sqrt n\,x}\right)
 =-e^{-i\pi/4}\sqrt n(x+x^{-1})
 +i-\frac{i}{2x^2}+O(n^{-1/2}),
\]
while \(v^{-s-1}\,dv=e^{-i\pi s/4}n^{-s/2}x^{-s-1}(1+O(n^{-1/2}))\,dx\). The real part of the leading phase has a **unique** maximum at \(x=1\), where its value is \(-\sqrt{2n}\), and its quadratic expansion is \(-e^{-i\pi/4}\sqrt n(x-1)^2\). The factor of order one at \(x=1\) is \(e^{i/2}\).

For rigor in the tails, let \(0<\delta<1<M\). On \([\delta,M]\) the real part decreases by a fixed positive multiple of \(\sqrt n\) away from a fixed neighborhood of \(1\). For \(0<x<\delta\), the elementary bound
\( |1+1/(\eta\sqrt n\,x)|^{-n}\le\exp[-c n/(1+\sqrt n\,x)]\)
controls the small end, and for \(x>M\) the factor \(|e^{i\eta\sqrt n x}|=e^{-\sqrt{n/2}x}\) controls the large end; choosing \(\delta\) sufficiently small and \(M\) sufficiently large makes both tails exponentially smaller than \(e^{-\sqrt{2n}}\). One-dimensional complex Laplace expansion at \(x=1\), with \(\lambda=e^{-i\pi/4}\sqrt n\), therefore yields
\[
 m_n(s)=e^{i/2}e^{-i\pi s/4}n^{-s/2}e^{-2\lambda}
 \sqrt{\frac\pi\lambda}\left(1+O_s(n^{-1/2})\right),
\]
which is precisely the displayed asymptotic after simplification. This proves the needed uniform upper bound for all sufficiently large integer \(n\).

**3. Every Schatten ideal.** The norm of the \(n\)-th matrix row is
\[
 R_n=|m_n(s)|\left(\sum_{j=0}^n c_j(\alpha)^2\right)^{1/2}
 =O_{\alpha,s}\!\left(n^{\alpha+3/2-s/2-1/4}e^{-\sqrt{2n}}\right).
\]
Represent the matrix as a sum of rank-one row operators \(T_{\alpha,s}=\sum_{n\ge0}e_n\otimes r_n^*\). For \(0<p\le1\), the Schatten \(p\)-quasi-triangle inequality bounds the \(p\)-th power of the quasi-norm of a finite sum by \(\sum R_n^p\); for \(p\ge1\), \(\sum R_n<\infty\) gives convergence in trace norm and hence in every \(\mathcal S_p\). Thus the series converges to the integral-defined operator in every \(\mathcal S_p\), \(p>0\).

**4. Determinant, spectrum, trace.** Finite compressions \(P_NT_{\alpha,s}P_N\) are triangular with diagonal \(m_0(s),\ldots,m_N(s)\), and converge to \(T_{\alpha,s}\) in trace norm. Continuity of the Fredholm determinant gives \(\det(I-zT_{\alpha,s})=\prod_{n\ge0}(1-zm_n(s))\), locally uniformly in \(z\). Its zeros determine the nonzero point spectrum with algebraic multiplicities, independent of \(\alpha\).

To evaluate its trace, note that \(\sum|m_n(s)|<\infty\), while a direct unregulated exchange of the geometric series and the original complex integral is **not** absolutely justified. Instead, for each \(N\),
\[
 \sum_{n=0}^N m_n(s)
 =\int_1^\infty v^{-s}e^{iv}\left[1-(1-v^{-1})^{N+1}\right]dv.
\]
The remainder against the improper oscillatory integral \(I_s=\int_1^\infty v^{-s}e^{iv}dv\) is the integral of \(e^{iv}h_N(v)\), with \(h_N(v)=v^{-s}(1-v^{-1})^{N+1}\). This is nonnegative, vanishes at both endpoints, and has a unique maximum at \(v=1+(N+1)/s\). By integration by parts, the remainder modulus is at most the total variation \(2\max h_N=O_s(N^{-s})\). Hence the trace is \(I_s=(-i)^{s-1}\Gamma(1-s,-i)\) by analytic continuation of the incomplete-Gamma integral. No assertion about a positive variation operator's spectrum is needed.

## Verification
`CHECK.py` reproduces the finite matrix coefficients, validates selected contour-integral moments against the stated asymptotic and the trace against the incomplete-Gamma expression. It uses Python 3 with `mpmath`. Its finitely many numerical tests are consistency checks and do not replace the contour-deformation, Laplace, tail, or Schatten-class proofs above.

## Relationship to prior work
Blasco and Pennanen (2026) introduce the Bergman-kernel-induced Cesàro operator and prove broad boundedness characterizations **assuming a positive Borel measure**. Blasco and Mas (2025) use exactly the power-kernel family in mixed-norm spaces, also **with a positive measure**. The current construction retains the same kernel family but introduces a complex boundary-chirp measure whose moments are smaller than those of its variation by a stretched-exponential factor. Earlier works by Blasco and by Lin–Xie allow complex measures for Cesàro-type operators, typically with the **Cauchy kernel**. The present claim is not a general complex-measure boundedness criterion, and it does not claim to originate the idea of oscillatory regularization. The contribution is this explicit non-Carleson-variation example across **all** Bergman powers, with precise moment asymptotics, all-Schatten regularity, a Fredholm determinant, and a closed trace formula. No currently inspected comparison entails these conclusions.

## Limitations
The concrete measure family has density \((1-t)^{s-1}e^{i/(1-t)}\) with \(0<s<1/2\); no characterization of all complex measures is asserted. Schatten membership is proved on \(H^2\), not arbitrary analytic function spaces. The moment asymptotic is a fixed-\(s\) assertion, not uniform as \(s\) approaches either endpoint. Exact values of individual moments are given by convergent integrals, not elementary closed forms. Prior-coverage searches are not a proof of publication priority; earlier work on complex moments or nonselfadjoint Cesàro operators may contain equivalent versions.

## References
1. O. Blasco and A. Pennanen, *Cesàro operator induced by a Bergman kernel*, arXiv:2609.21657, first posted 2026-09-18, https://arxiv.org/abs/2609.21657.
2. O. Blasco and A. Mas, *Cesàro-type operators on mixed norm spaces*, arXiv:2507.20586, first posted 2025-07-28, https://arxiv.org/abs/2507.20586.
3. Q. Lin and H. Xie, *Cesàro-type operators on derivative-type Hilbert spaces of analytic functions: The proof of a conjecture*, Journal of Functional Analysis (2025), DOI:10.1016/j.jfa.2024.110813.
4. NIST Digital Library of Mathematical Functions, sections on the incomplete Gamma function and complex asymptotic expansions, https://dlmf.nist.gov/8 and https://dlmf.nist.gov/2.
