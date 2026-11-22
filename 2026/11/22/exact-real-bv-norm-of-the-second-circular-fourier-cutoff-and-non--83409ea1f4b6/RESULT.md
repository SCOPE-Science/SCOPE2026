# Exact real-BV norm of the second circular Fourier cutoff and nonantipodal norming jumps

## Finding
Let \(\mathbb T=\mathbb R/(2\pi\mathbb Z)\), let \(BV_{\mathbb R}(\mathbb T)\) be the real-valued functions of bounded distributional variation, modulo additive constants, and put \(V(f)=|Df|(\mathbb T)\). Let \(S_2\) be the real \(L^2\)-orthogonal projector onto the five-dimensional trigonometric space spanned by \(1,\cos t,\sin t,\cos2t,\sin2t\). Its exact induced variation norm is
\[
\boxed{\sup_{V(f)>0}\frac{V(S_2f)}{V(f)}=\frac{\sqrt{71+8\sqrt2}}{2\pi}=1.443963501539\ldots.}
\]
The supremum is attained by the indicator of any circular arc of length \(\delta_*\), or its complementary arc, up to rotation, nonzero real scaling and addition of constants, where
\[
\boxed{\delta_*=2\arccos\sqrt{\frac{2+\sqrt2}{8}}=1.717771517458\ldots\ \text{radians}.}
\]
Among all indicators of nontrivial arcs, these and only these arc lengths maximize the ratio. In particular, a half-circle indicator gives only \(4/\pi\), strictly below the sharp factor. No assertion is made that all BV extremizers must be single arcs.

## Assumptions and scope
All functions, signed measures and operators are **real**. The circle carries arc-length Lebesgue measure \(dt\); its variation is distributional total variation, including jumps across the identified endpoints. Fourier coefficients are \(\widehat f(k)=(2\pi)^{-1}\int_{\mathbb T}f(t)e^{-ikt}\,dt\), and \(S_2f=\sum_{|k|\le2}\widehat f(k)e^{ikt}\). The associated real Dirichlet kernel is \(D_2(t)=1+2\cos t+2\cos2t\), so \(S_2f=(2\pi)^{-1}D_2*f\). Functions differing by a constant are identified, since their variation seminorm is zero. The finite-dimensional projector extends canonically to real \(BV\) through these coefficients.

## Proof
**1. The exact zero-mass kernel-distance reduction.** For \(f\in BV_{\mathbb R}(\mathbb T)\), set \(\mu=Df\), a finite real signed measure with \(\mu(\mathbb T)=0\), and \(V(f)=|\mu|(\mathbb T)\). Write the Jordan decomposition \(\mu=\mu^+-\mu^-\). Each positive part has mass \(a=V(f)/2\). Let \(\gamma\) be any positive coupling of \(\mu^+\) and \(\mu^-\), of total mass \(a\), for instance \(a^{-1}\mu^+\otimes\mu^-\) if \(a>0\). Since differentiation commutes with circular convolution,
\[
(S_2f)'(t)=\frac1{2\pi}\int_{\mathbb T^2}\bigl[D_2(t-x)-D_2(t-y)\bigr]d\gamma(x,y).
\]
Tonelli's theorem and the triangle inequality give
\[
\frac{V(S_2f)}{V(f)}\le \frac1{4\pi}\max_{\delta\in[0,2\pi]}\int_0^{2\pi}|D_2(t)-D_2(t-\delta)|\,dt.\tag{1}
\]
For any distinct \(x,y\), the indicator of the directed arc between them has distributional derivative \(\delta_x-\delta_y\), has variation \(2\), and turns the inequality in (1) into equality at the corresponding separation. Thus (1) is an identity for the **sharp norm**, not merely an upper bound. Reflection permits restricting the maximum to \(0\le\delta\le\pi\).

**2. Evaluate every kernel distance.** Set \(h=\delta/2\), \(c=\cos h\), \(s=\sin h\); here \(0\le h\le\pi/2\). The identity
\[
D_2(u+h)-D_2(u-h)=-4s\sin u\,(1+4c\cos u)
\]
therefore yields, by the substitution \(v=\cos u\) on both half-periods,
\[
\frac1{4\pi}\int_0^{2\pi}|D_2(t)-D_2(t-\delta)|\,dt
=\frac{2s}{\pi}\int_{-1}^{1}|1+4cv|\,dv
=\begin{cases}
\dfrac{4s}{\pi},&0\le c\le\tfrac14,\\[3pt]
\dfrac{2s}{\pi}\left(4c+\dfrac{1}{4c}\right),&\tfrac14\le c\le1.
\end{cases}\tag{2}
\]
The two expressions agree at \(c=1/4\), so (2) also verifies the boundary case.

**3. Prove the unique maximizing separation.** The first branch of (2) is at most \(4/\pi\). On the second, write \(z=c^2\in[1/16,1]\). The squared ratio multiplied by \(4\pi^2\) becomes
\[
G(z)=\frac{(1-z)(16z+1)^2}{z}
=-256z^2+224z+31+\frac1z,
\qquad
G'(z)=-\frac{(16z+1)(32z^2-16z+1)}{z^2}.
\]
Its two positive critical points are \(z_-=(2-\sqrt2)/8\) and \(z_+=(2+\sqrt2)/8\). Both lie strictly between \(1/16\) and \(1\). The factorization gives a strict local minimum at \(z_-\) and a strict local maximum at \(z_+\), with negative derivative before \(z_-\), positive between the roots, and negative after \(z_+\). At \(z_+\), direct exact substitution gives \(G(z_+)=71+8\sqrt2\). Its resulting gain \(\sqrt{71+8\sqrt2}/(2\pi)\) is strictly greater than \(4/\pi\), since \(71+8\sqrt2>64\). The second branch's endpoints cannot be larger (at \(z=1/16\) the first-branch estimate applies, and at \(z=1\) the gain is zero). Hence \(z_+\) yields the unique global optimum for \(\delta\in[0,\pi]\). Reflection gives the complementary separation \(2\pi-\delta_*\). The arc indicator argument in Step 1 establishes attainment and uniqueness **among arc lengths**. This proves the claim.

## Verification
Run `python3 checks/check_bv_fourier2.py` in the directory containing this document. The standalone Python checker uses exact rational arithmetic in \(\mathbb Q(\sqrt2)\) for the critical-point and radical identities, checks the derivative factorization as a polynomial identity, independently integrates absolute differences of translated Dirichlet kernels by dividing at their zeros, checks the optimum and the half-circle comparison, and samples zero-sum real atomic derivatives as a supplemental stress test. The infinite-dimensional norm and all-separation maximum follow from the proof above, not the finite examples.

## Relationship to prior work
The Dirichlet kernel representation of low-pass Fourier projection is classical. Candès and Fernandez-Granda, *Towards a Mathematical Theory of Super-Resolution* (first posted 2012-03-27, arXiv:1203.5871v1), Section 1.2 and the measure-recovery appendices, use the Dirichlet low-pass projector and total variation of recovered measures to prove uniqueness of sparse recovery under separation. That is a different extremal quantity from the induced **real BV variation norm of the projector on functions**. Poon, *On the role of total variation in compressed sensing* (first posted 2014-07-20, arXiv:1407.5339v1), Sections 1 and 2, studies finite-vector gradient-sparse reconstruction from incomplete discrete Fourier data, again without a sharp continuum five-mode BV projection norm. The published result *Sharp harmonic projection constants on finite metric cycles* computes minimal projection norms on a finite cycle equipped with the **Lipschitz maximum-edge** norm and onto one harmonic pair; it does not determine an \(L^1\)-variation norm on the continuous circle for the full five-mode cutoff. The published *Exact three-frequency Fourier projection norm on every cyclic group* computes full-space endpoint \(\ell^1/\ell^\infty\) convolution norms on finite groups, not the zero-mass BV quotient norm and its norming separation. The published *A universal positive Lebesgue-norm penalty for fixed Fourier frequency deletions* addresses large-cutoff \(C\)-norm differences and similarly does not imply the fixed-cutoff real-BV result. A separate previously recorded circular-heat BV contraction formula uses a positive heat kernel, whereas the present oscillatory Dirichlet kernel changes sign. An abstract zero-mass kernel-distance bound is standard; the specific exact two-harmonic optimization and nonantipodal optimum are the substantive asserted contribution.

## Limitations
The result addresses **real**, one-dimensional circular BV and only the five-mode cutoff \(|k|\le2\). It does not classify all possible BV equality cases, assert any formula for arbitrary larger Fourier cutoffs, or extend the result to complex BV, weighted variation, finite cyclic sampling, or the uniform norm. The historical novelty assessment cannot exclude every classical or differently named special-case calculation, especially formulas in older approximation-theory literature; direct comparison with the closest identified works is supplied, but no independent priority validation is claimed.

## References
1. E. J. Candès and C. Fernandez-Granda, *Towards a Mathematical Theory of Super-Resolution*, arXiv:1203.5871v1, first posted 2012-03-27; https://arxiv.org/html/1203.5871v3 (full HTML).
2. C. Poon, *On the role of total variation in compressed sensing*, arXiv:1407.5339v1, first posted 2014-07-20; https://arxiv.org/abs/1407.5339 (full HTML rendering).
3. *Sharp harmonic projection constants on finite metric cycles*, published research record, https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-sharp-harmonic-projection-constants-on-finite-metric-cycles--616f4adc601f.
4. *Exact three-frequency Fourier projection norm on every cyclic group*, published research record, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-exact-three-frequency-fourier-projection-norm-on-every-cyclic-gr--b176a6018242.
5. *A universal positive Lebesgue-norm penalty for fixed Fourier frequency deletions*, published research record, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-a-universal-positive-lebesgue-norm-penalty-for-fixed-fourier-fre--c38977523c90.
