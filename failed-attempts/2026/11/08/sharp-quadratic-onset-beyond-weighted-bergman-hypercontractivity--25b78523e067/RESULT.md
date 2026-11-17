# Sharp quadratic onset beyond weighted Bergman hypercontractivity

## Finding
Fix a real parameter \(\alpha>1\) and let \(dA_\alpha(z)=(\alpha-1)\pi^{-1}(1-|z|^2)^{\alpha-2}\,dx\,dy\) on the unit disk. For the analytic Bergman Hilbert space \(A^2_\alpha\), put \(D_r f(z)=f(rz)\) and
\[
K_\alpha(r)=\sup_{\|f\|_{A^2_\alpha}=1}\|D_rf\|_{L^4(dA_\alpha)},\qquad 0<r<1.
\]
For \(\delta=2r^2-1\downarrow0\) through positive values, the exact supercritical asymptotic is
\[
\boxed{K_\alpha(r)^4=1+(\alpha+1)\delta^2+o_\alpha(\delta^2).}
\]
In particular \(K_\alpha(r)=1+(\alpha+1)\delta^2/4+o_\alpha(\delta^2)\). An optimizer exists for every \(0<r<1\). Write any maximizing function near this threshold as \(f=\sum_{n\ge0}a_ne_n\) in the normalized monomial basis \(e_n(z)=\sqrt{(\alpha)_n/n!}\,z^n\), and choose its overall phase so \(a_0>0\). Every such optimizer obeys
\[
|a_1|^2=(\alpha+1)\delta+o_\alpha(\delta),\qquad
 a_2=\frac12\sqrt{\frac{2\alpha}{\alpha+1}}\,a_1^2+o_\alpha(\delta),\qquad
\sum_{n\ge3}|a_n|^2=o_\alpha(\delta^2).
\]
The complex square \(a_1^2\) in the second formula fixes the asymptotic relative phase of the second mode; it is not \(|a_1|^2\). The assertions are uniform over all maximizing functions for each fixed \(\alpha>1\). No global uniqueness of maximizers is asserted.

## Assumptions and scope
The rising factorial is \((\alpha)_0=1\) and \((\alpha)_n=\alpha(\alpha+1)\cdots(\alpha+n-1)\) for \(n\ge1\). The normalized area measure above has total mass one, so \(\|1\|_{A^2_\alpha}=1\). Set \(v_n=\sqrt{(\alpha)_n/n!}\) and \(m_n=v_n^{-2}=n!/(\alpha)_n\). Norms on the coefficient space use \(\|f\|_{A^2_\alpha}^2=\sum_{n\ge0}|a_n|^2\). The limit is for fixed \(\alpha\); no uniformity as \(\alpha\downarrow1\) or \(\alpha\to\infty\) is claimed. The focal earlier result gives the sharp contractive radius \(r=1/\sqrt2\) for this \(L^2\)-to-\(L^4\) map; the present statement concerns its *noncontractive side*.

## Proof
**1. Exact moment diagonalization.** Radial integration gives \(\int_{\mathbb D}|z|^{2n}\,dA_\alpha=m_n\). Consequently, for every \(f=\sum_{n\ge0}a_ne_n\) and \(r<1\),
\[
\|D_rf\|_4^4=\sum_{k\ge0}r^{2k}m_k\left|\sum_{i+j=k}v_iv_ja_ia_j\right|^2. \tag{1}
\]
The sum converges by analyticity on the smaller disk, or directly by the bounds below.

**2. A quantitative gap at the critical radius.** At \(r_c=2^{-1/2}\), Cauchy--Schwarz and the binomial convolution identity
\[
\sum_{i+j=k}\frac{(\alpha)_i}{i!}\frac{(\alpha)_j}{j!}=\frac{(2\alpha)_k}{k!}
\]
give, for the \(k\)-th nonnegative term \(P_k\) of (1),
\[
P_k\le c_k\sum_{i+j=k}|a_i|^2|a_j|^2,\qquad
c_k=2^{-k}\frac{(2\alpha)_k}{(\alpha)_k}.
\]
Here \(c_0=c_1=1\), \(c_{k+1}/c_k=(2\alpha+k)/(2(\alpha+k))<1\) for \(k\ge1\), and \(c_2=1-[2(\alpha+1)]^{-1}\). Let \(s=\sum_{n\ge1}|a_n|^2\) and \(H=\sum_{n\ge2}|a_n|^2\). For every normalized \(f\), the probability mass of index pairs with \(i+j\ge2\) equals \(s^2+2|a_0|^2H\). Therefore
\[
1-\|D_{r_c}f\|_4^4\ge\frac{s^2+2|a_0|^2H}{2(\alpha+1)}. \tag{2}
\]
In particular, constants are the only normalized optimizers at criticality, up to phase.

**3. Every supercritical optimizer is close to a constant.** If \(\delta>0\), formula (1) equals \(\sum_{k\ge0}(1+\delta)^kP_k\). Since \(c_k=O_\alpha(2^{-k}(1+k)^\alpha)\), for sufficiently small positive \(\delta\),
\[
\sup_{k\ge1}c_k((1+\delta)^k-1)\le C_\alpha\delta.
\]
As the convolution-pair mass for \(k\ge1\) is \(1-|a_0|^4\le2s\), the increase from the critical value is at most \(2C_\alpha\delta s\). A maximizing function has fourth-power norm at least one (the constant trial), so (2) implies \(s=O_\alpha(\delta)\), then \(H=O_\alpha(\delta^2)\). Such a maximizing function exists: for \(r<1\), the dilation maps bounded Hilbert balls into families uniformly bounded on a compactly contained disk, hence is compact into \(L^4(dA_\alpha)\); weak compactness and rescaling yield norm attainment.

**4. Uniform quartic normal form.** Choose \(a_0=\sqrt{1-s}>0\), put \(b=a_1\), \(y=|b|^2\), and \(h=(a_n)_{n\ge2}\). Let \(M=\sqrt{2\alpha/(\alpha+1)}\) and \(d_n=2-2^{2-n}\) for \(n\ge2\). The convolution in (1), expressed in the orthonormal coefficient basis, has its degree-\(k\) amplitude for \(k\ge2\) equal to
\[
r^k\bigl(2a_0h_k+\mathbf 1_{k=2}Mb^2+R_k\bigr),
\]
where the contribution from the nonconstant tail pairs has \(\ell^2\)-norm bounded by \(C_\alpha(|b|\|h\|_2+\|h\|_2^2)=O_\alpha(\delta^{3/2})\) after multiplication by \(r^k\). To justify the bound uniformly in degree, apply the same Cauchy/binomial estimate as in step 2 to the polarized quadratic convolution; its operator norm is bounded near \(r_c\) because \(\sup_k(1+\delta)^kc_k<\infty\).

Now use \(y=O_\alpha(\delta)\), \(\|h\|_2=O_\alpha(\delta)\), \(r^2=(1+\delta)/2\), and expand (1). The \(k=0,1\) terms and the leading \(k\ge2\) terms give, with an error \(o_\alpha(\delta^2)\) uniform on this maximizing class,
\[
\|D_rf\|_4^4=1+2\delta y-\frac{\alpha+2}{2(\alpha+1)}y^2
 -\sum_{n\ge2}d_n|h_n|^2+M\operatorname{Re}(b^2\overline{h_2})+o_\alpha(\delta^2). \tag{3}
\]
The coefficient of \(y^2\) includes the degree-two quadratic contribution \(M^2y^2/4\). Since \(d_2=1\) and \(d_n\ge3/2\) for \(n\ge3\), completing the two squares yields the *full* leading deficit:
\[
\begin{aligned}
\|D_rf\|_4^4={}&1+(\alpha+1)\delta^2
-\frac{(y-(\alpha+1)\delta)^2}{\alpha+1}\\
&-\left|h_2-\frac M2b^2\right|^2
-\sum_{n\ge3}d_n|h_n|^2+o_\alpha(\delta^2). \tag{4}
\end{aligned}
\]
The three displayed penalties are nonnegative. A normalized trial with \(b=\sqrt{(\alpha+1)\delta}\), \(h_2=Mb^2/2\), \(h_n=0\) for \(n\ge3\), and \(a_0=\sqrt{1-|b|^2-|h_2|^2}\) is admissible for all sufficiently small positive \(\delta\). Direct substitution in (1) makes every penalty in (4) zero, establishing the matching lower bound. Applying (4) to any maximizer forces each penalty to be \(o_\alpha(\delta^2)\), proving all three coefficient asymptotics and the sharp norm law.

## Verification
The standalone `CHECK.py` uses only Python's standard library. It tests the binomial convolution identity, strict decrease of the critical spectral constants, the exact rational moment formula for several polynomial families and radii, positivity of the high-mode deficits, and the normalized three-mode near-critical trial. The executable test reports `BERGMAN_SUPERCRITICAL_CHECKS_PASS 490`. Those are finite checks, not a proof of the uniform infinite-dimensional estimates; steps 2--4 supply that proof. Running `python3 CHECK.py` reproduces the finite checks.

## Relationship to prior work
Melentijević (2022 preprint, published 2023) established the sharp weighted Bergman contractivity threshold for \(L^p\to L^q\), including \(r_c=1/\sqrt2\) when \(p=2,q=4\). Bayart--Brevig--Haimi--Ortega-Cerdà--Perfekt (2017 preprint) gave contractivity results for special weights. Kulikov (2022) studied contractive Bergman functionals and reproducing-kernel optimizers, and Llinares (2021) studied related weighted Bergman embeddings. Their inspected statements and arguments establish neither the first supercritical excess coefficient \(\alpha+1\) nor the asymptotic optimizer's second-mode resonance for the present fixed-weight dilation norm. The existence of a semantically equivalent calculation elsewhere in the extensive hypercontractivity literature remains a historical-priority risk.

## Limitations
This is an asymptotic for fixed \(\alpha>1\) and \(r\downarrow1/\sqrt2\) from above. The argument gives no effective universal radius, no uniform estimate in \(\alpha\), no full series past quadratic order, no classification of every maximizer at finite supercritical radius, and no corresponding theorem for exponents other than \(L^2\to L^4\). Finite checker computations do not certify the limit and no independent mathematical audit has been performed.

## References
- P. Melentijević, *Hypercontractive inequalities for weighted Bergman spaces*, arXiv:2211.03655v1 (first public November 7, 2022), https://arxiv.org/abs/2211.03655.
- F. Bayart, O. F. Brevig, A. Haimi, J. Ortega-Cerdà and K.-M. Perfekt, *Contractive inequalities for Bergman spaces and multiplicative Hankel forms*, arXiv:1701.06897v1 (2017), https://arxiv.org/abs/1701.06897.
- A. Kulikov, *Functionals with extrema at reproducing kernels*, arXiv:2203.12349v1 (2022), https://arxiv.org/abs/2203.12349.
- A. Llinares, *On a conjecture about contractive inequalities for weighted Bergman spaces*, arXiv:2112.09962v1 (2021), https://arxiv.org/abs/2112.09962.
