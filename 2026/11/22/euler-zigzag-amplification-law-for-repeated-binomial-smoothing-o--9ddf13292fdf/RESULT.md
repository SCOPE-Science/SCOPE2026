# Euler-zigzag amplification law for repeated binomial smoothing on odd cycles

## Finding
For every odd integer \(N\ge3\) and every integer \(m\ge1\), let \(G_N=\mathbb Z/N\mathbb Z\), with counting-measure convolution, and define
\[
\mu_{m,N}=2^{-m}(\delta_0+\delta_1)^{*m},\qquad T_{m,N}f=\mu_{m,N}*f.
\]
The one-step case has inverse norm \(\|T_{1,N}^{-1}\|_{\infty\to\infty}=N\), as also follows from midpoint sampling of periodic linear splines [4]. The result here concerns **repeated** smoothing (\(m\ge2\)). Its exact worst-case reconstruction-error amplification in \(\ell^\infty(G_N)\) is the \(\ell^1\)-norm of the inverse convolution kernel. Writing \(A_m\) for the positive Euler zigzag numbers defined by
\[
\sec z+\tan z=\sum_{m=0}^\infty A_m z^m/m!,
\]
for each fixed \(m\ge2\), as odd \(N\to\infty\),
\[
\boxed{\|T_{m,N}^{-1}\|_{\ell^\infty\to\ell^\infty}=\frac{A_m}{m!}N^m+O_m(N^{m-1}).}
\]
At smoothing depths \(m=2,3,4\), the exact values for **every** odd \(N\ge3\) are
\[
\boxed{(N^2+1)/2,\quad N(N^2+2)/3,\quad (5N^4+10N^2+9)/24.}
\]
Fourier diagonalization gives the comparison norm \(\|T_{m,N}^{-1}\|_{2\to2}=\sin^{-m}(\pi/(2N))\). Consequently,
\[
\lim_{\substack{N\to\infty\\N\ \mathrm{odd}}}\frac{\|T_{m,N}^{-1}\|_{\infty\to\infty}}{\|T_{m,N}^{-1}\|_{2\to2}}
=\frac{A_m}{m!}\left(\frac{\pi}{2}\right)^m,
\qquad
\lim_{m\to\infty}\frac{A_m}{m!}\left(\frac{\pi}{2}\right)^m=\frac4\pi.
\]
The fixed-depth comparison constant on the right is the classical Favard constant. The assertion is that it arises as the large-cycle norm ratio, not that the constant or its large-\(m\) limit is new. For even \(N\), the smoothing operator is singular already for one step, so the odd-order restriction is essential.

## Assumptions and scope
The cyclic group has odd cardinality \(N\ge3\). Functions may be real- or complex-valued. Convolution is unnormalized counting convolution, and \(\delta_j\) is unit mass at \(j\); the kernel itself is a probability measure. The smoothing depth \(m\) is any fixed positive integer for the first asymptotic; the two limits are sequential (first \(N\), then \(m\)), not a joint-limit claim. The error term permits a constant depending on \(m\).

## Proof
**1. Explicit inverse.** In \(\mathbb C[z]/(z^N-1)\), oddness gives
\[
(1+z)\sum_{j=0}^{N-1}(-z)^j=1-(-z)^N=2.
\]
Hence \((\delta_0+\delta_1)/2\) has inverse \(a_N(j)=(-1)^j\), and the inverse of \(T_{m,N}\) is convolution by \(b_{m,N}=a_N^{*m}\). In particular \(b_{m,N}\) has integer coefficients and \(\|T_{m,N}^{-1}\|_{\infty\to\infty}=\sum_j|b_{m,N}(j)|\). Equality of the operator norm is attained by choosing an input whose phases agree with the kernel terms at a fixed output coordinate.

**2. Discrete antiperiodic polynomial.** For \(r=m-1\), put \(p_{r,N}(j)=(-1)^j b_{r+1,N}(j)\), for \(0\le j<N\). Then \(p_{0,N}(j)=1\), and the identity \(((\delta_0+\delta_1)/2)*b_{r+1,N}=b_{r,N}\) yields
\[
p_{r,N}(j)-p_{r,N}(j-1)=2p_{r-1,N}(j)\quad(1\le j<N),
\qquad
p_{r,N}(0)+p_{r,N}(N-1)=2p_{r-1,N}(0).
\]
The first equation determines the new polynomial up to a constant and the second determines that constant. By induction \(p_{r,N}(j)\) is a polynomial in \(j,N\) of total degree at most \(r\).

**3. Uniform Euler-polynomial limit.** Define Euler polynomials by
\[
\frac{2e^{xt}}{1+e^t}=\sum_{r\ge0}E_r(x)t^r/r!.
\]
They obey \(E_0=1\), \(E'_r=rE_{r-1}\), and \(E_r(0)+E_r(1)=0\) for \(r\ge1\). For fixed \(r\), a discrete antidifferentiation and the boundary relation above prove uniformly in \(0\le j<N\):
\[
N^{-r}p_{r,N}(j)=\frac{2^r}{r!}E_r(j/N)+O_r(N^{-1}).
\]
Indeed the forward difference of \(N^{-r}p_{r,N}\) is \((2/N)N^{-(r-1)}p_{r-1,N}\); the induction hypothesis makes this a Riemann sum for the derivative of \(2^rE_r/r!\), with accumulated error \(O_r(N^{-1})\). The antiperiodic boundary condition fixes the integration constant, with the right side of the boundary equation of order \(O_r(N^{-1})\) after normalization. The base \(r=0\) is exact.

**4. Norm and the zigzag constant.** The preceding uniform approximation and the Lipschitz property of absolute value give
\[
\frac{\|b_{m,N}\|_1}{N^m}=\frac{2^{m-1}}{(m-1)!}\int_0^1|E_{m-1}(x)|\,dx+O_m(N^{-1}).
\]
The standard Euler-polynomial sign property also follows inductively from their derivative, reflection symmetry and the antiperiodic endpoint condition: \(E_{2k}\) (for \(k\ge1\)) has constant sign on \((0,1)\), whereas \(E_{2k+1}\) has its sole interior zero at \(1/2\), with opposite signs on the two sides. The case \(E_0=1\) is immediate. Integrating \(E_{m-1}=E'_m/m\), and using the series \(2/(e^t+1)=1-\tanh(t/2)\) and \(1/\cosh(t/2)\), yields
\[
\int_0^1|E_{m-1}(x)|\,dx=\frac{A_m}{m2^{m-1}}.
\]
This proves the stated asymptotic, including its sharp leading constant.

**5. Exact low-depth evaluations.** The first four antiperiodic polynomials are:
\[
\begin{aligned}
p_{0,N}(j)&=1,\\
p_{1,N}(j)&=2j+2-N,\\
p_{2,N}(j)&=2j^2-2(N-3)j+4-3N,\\
p_{3,N}(j)&=\frac43j^3-2(N-4)j^2-\frac{4(6N-11)}3j+\frac{(N-4)(N^2+4N-6)}3.
\end{aligned}
\]
For odd \(N\ge3\), \(p_{2,N}(j)<0\) on \(0\le j\le N-2\), with \(p_{2,N}(N-1)=N>0\); the quadratic is convex and is negative at both endpoints of the first range. For \(N=2k+1\ge5\), \(p_{3,N}(j)\) decreases strictly up to \(j=N-2\). The values at \(j=k-2,k-1\) are respectively \(2k^2+2k+1\) and its negative. The final value \(p_{3,N}(N-1)=2p_{2,N}(0)-p_{3,N}(0)\) is negative, since \(p_{3,N}(0)>0\). Thus the positive range is \(0\le j\le k-2\) and all remaining values are negative. For \(N=3\), the fourth-depth kernel has norm \(21\) by direct substitution. Summing the corresponding polynomial pieces gives, successively,
\[
\sum_j|p_{0,N}(j)|=N,\quad
\sum_j|p_{1,N}(j)|=(N^2+1)/2,\quad
\sum_j|p_{2,N}(j)|=N(N^2+2)/3,
\]
\[
\sum_j|p_{3,N}(j)|=(5N^4+10N^2+9)/24.
\]

**6. Fourier comparison and the second limit.** The character multiplier of \(T_{m,N}\) at frequency \(k\) is \(((1+e^{-2\pi ik/N})/2)^m\), with modulus \(|\cos(\pi k/N)|^m\). For fixed odd \(N\), its minimum over \(k\) is \(\sin^m(\pi/(2N))\). The ratio in the finding thus tends, at fixed \(m\), to \(A_m(\pi/2)^m/m!\). This equals the Favard series \(K_m=(4/\pi)\sum_{\nu\ge0}(-1)^{\nu(m+1)}(2\nu+1)^{-m-1}\): use \(\sec z+\tan z=\tan(\pi/4+z/2)\) and the standard tangent partial fractions. Extraction of the \(m\)-th coefficient gives \(A_m/m!=2\sum_{k\in\mathbb Z}(\pi/2+2\pi k)^{-m-1}\), absolutely convergent for \(m\ge1\); pairing the positive and negative arguments of the sum gives the displayed series after rescaling. The leading term gives \(K_m\to4/\pi\). This is a sequential limit, not a joint-limit assertion.

## Verification
The independent executable `check.py` uses standard Python integer arithmetic to reconstruct the cyclic inverse by convolution and the antiperiodic recurrence, confirm that convolving back by the smoothing kernel yields the identity, and test the four exact norm formulas for every odd \(N\) from 3 through 101. It also checks the Euler zigzag recurrence and supplementary numerical Fourier gap and large-order approximations. Passing finite tests is corroboration, not proof for all \(N,m\); the polynomial recurrence and analysis above establish the infinite statements.

## Relationship to prior work
The midpoint rule in [4] already gives the exact one-step endpoint. The map from knot coefficients to one sample per cell midpoint takes adjacent averages, up to a cyclic index shift; continuous piecewise-linear interpolation preserves the supremum of the absolute knot data. Thus its odd-cycle norm \(N\) and singularity on even cycles apply to one step here. Powers with \(m\ge2\) are not part of that endpoint norm calculation. The classical Favard series describes a continuous sharp comparison constant and its limiting value \(4/\pi\); the repeated discrete inverse supplies its own fixed-depth convergence law, error order, and finite-cycle exact formulas.

Przemysław Ohrysko's 2026 work on norm-controlled inversion in measure algebras studies universal bounds above a spectral threshold, rather than the sharp finite-cycle growth at a multiplier whose minimum tends to zero. Zhu, Hu and Kim (2025) develop Euler-polynomial identities for a continuous alternating convolution; their abstract does not supply the discrete cyclic inverse-operator norms, finite formulas or the two norm-comparison limits here. These classical Euler-polynomial identities are used as background, not asserted as new discoveries.

## Limitations
The result is for the **fair, directed, adjacent two-tap** kernel, positive integer powers, and finite odd cycles. Even cycles are singular. The first asymptotic fixes \(m\); no uniform claim for growing \(m\) with \(N\) is made. An unindexed older result on inverses of circulant Euler splines may imply some or all of the conclusion; bibliographic exhaustiveness and independent verification have not been established.

## References
1. P. Ohrysko, *Norm-Controlled Inversion in Measure Algebras*, arXiv:2609.27714 (first public 2026-09-23), https://arxiv.org/abs/2609.27714.
2. H. Zhu, S. Hu and M.-S. Kim, *On the properties of alternating invariant functions*, arXiv:2505.10985 (first public 2025-05-16), https://arxiv.org/abs/2505.10985.
3. Classical Euler-polynomial generating functions \(2e^{xt}/(e^t+1)\) and Euler zigzag exponential generating function \(\sec t+\tan t\); definitions used explicitly above.
4. *Sharp parity law for two-point discrete projection onto periodic linear splines* (8 November 2026), midpoint endpoint. https://github.com/Resultary/2026/tree/main/2026/11/8/SCOPE-sharp-parity-law-for-two-point-discrete-projection-onto-periodic--56b851fd8a2b
