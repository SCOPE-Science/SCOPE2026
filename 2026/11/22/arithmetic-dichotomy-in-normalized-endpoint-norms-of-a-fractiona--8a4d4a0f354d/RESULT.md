# Arithmetic dichotomy in normalized endpoint norms of a fractional unilateral-shift semigroup

## Finding

Let \(1<\alpha<2\), let \(S_p\) be the unilateral right shift on complex \(\ell^p(\mathbb N_0)\), and put \(T_{\alpha,p}(t)=\exp[-t(I-S_p)^\alpha]\), \(t\geq 0\), with the binomial fractional power. Define
\[
\phi=\frac{\pi}{\alpha+1},\qquad \theta=\pi-2\phi,\qquad \delta=2\cos\phi,
\qquad c=\delta^\alpha\cos\phi,\quad b=\delta^\alpha\sin\phi,\quad v=\alpha\delta^{\alpha-1},
\]
\[
K=\frac v2\big((\alpha+1)-i(\alpha-1)\tan\phi\big),\qquad
\nu=\operatorname{Re}(K^{-1}),\qquad \omega=\operatorname{Im}(K^{-1}).
\]
The numbers \(b,c,v,\nu,\omega,\operatorname{Re}K\) are positive. For every \(t\geq0\), \(\|T_{\alpha,2}(t)\|=e^{ct}\). Write \(R_\alpha(t)=e^{-ct}\|T_{\alpha,1}(t)\|\) and
\[
C_\alpha=\frac4\pi\sqrt{\frac{|K|}{\operatorname{Re}K}}
=\frac4\pi\left(1+\frac{(\alpha-1)^2\tan^2\phi}{(\alpha+1)^2}\right)^{1/4}.
\]
If \(\alpha\) is irrational, \(R_\alpha(t)\to C_\alpha\) as \(t\to\infty\). If \(\alpha\) is rational, write \(\theta/\pi=a/q\) in lowest terms (so \(q\ge4\)) and put
\[
F_{\alpha,q}(s)=\frac{2}{q\sqrt{2\pi|K|}}\sum_{r=0}^{q-1}\int_{\mathbb R}
 e^{-\nu y^2/2}\left|\cos\left(s-r\theta-\frac{\arg K}{2}-\frac{\omega y^2}{2}\right)\right|\,dy.
\]
Then \(R_\alpha(t)=F_{\alpha,q}(bt)+o(1)\). The profile is positive, continuous and nonconstant, has fundamental period \(\pi/q\) and has mean \(C_\alpha\). In particular \(R_\alpha(t)\) does not converge in the rational case; its liminf and limsup are the minimum and maximum of the profile.

## Assumptions and scope

The shift is \(S_p(x_0,x_1,\ldots)=(0,x_0,x_1,\ldots)\). The fractional power is the operator-norm convergent series \(\sum_{k\ge0}(-1)^k\binom\alpha k S_p^k\), using binomial coefficients of size \(O(k^{-\alpha-1})\). The scalar fractional power is the principal branch on the right half-plane, with its value at zero defined by continuity. Time tends to \(+\infty\) through real values, at fixed \(\alpha\). The integer endpoints, other orders, and norms on other \(\ell^p\) spaces are outside the result.

## Proof

**Norms and maxima.** Write \(f_t(z)=\exp[-t(1-z)^\alpha]=\sum_{n\ge0}a_n(t)z^n\). The Wiener algebra is complete and closed under exponentiation, so the coefficients are absolutely summable. Acting on the first unit vector shows the \(\ell^1\) convolution norm equals \(\sum_n|a_n(t)|\). Under the \(H^2\) identification, the \(\ell^2\) operator is multiplication by \(f_t\) and its norm is the maximum boundary modulus.

Set \(\psi(x)=-(1-e^{ix})^\alpha\). On \(0<x<\pi\), write \(1-e^{ix}=2\cos\varphi\,e^{-i\varphi}\), \(\varphi=(\pi-x)/2\). The derivative of \(\operatorname{Re}\psi\) in \(\varphi\) is \(\alpha 2^\alpha(\cos\varphi)^{\alpha-1}\sin((\alpha+1)\varphi)\), which changes from positive to negative at \(\phi\) on \((0,\pi/2)\). Conjugation gives exactly two maxima at \(\pm\theta\), both of height \(c\). At the positive saddle \(\psi(\theta)=c+ib\), and \(\psi'(\theta)=iv\) since \(\theta=(\alpha-1)\phi\). For \(z=e^{i\theta}\), \(z/(1-z)=-1/2+i\tan\phi/2\), and \(-\psi''(\theta)=v(1-(\alpha-1)z/(1-z))=K\). At the negative saddle the value and curvature are conjugated and the drift is still \(iv\). This gives the exact Hilbert-space norm.

**Two-saddle coefficient asymptotic.** Fourier inversion gives \(a_n(t)=(2\pi)^{-1}\int_{-\pi}^{\pi}e^{t\psi(x)-inx}\,dx\). Put \(y=(n-vt)/\sqrt t\). For bounded \(y\), set \(x=\theta+z/\sqrt t\) near the positive saddle. After removing the constant and linear phases the integrand tends to \(\exp(-Kz^2/2-iyz)\), bounded by a real Gaussian on the rescaled local interval for sufficiently small fixed saddle neighborhoods. This limit can be integrated uniformly on bounded \(y\) intervals: Taylor expansion controls compact \(z\) intervals and the real Gaussian controls their complement. The contribution is \(e^{t(c+ib)-in\theta}(2\pi tK)^{-1/2}e^{-y^2/(2K)}\) up to \(o(e^{ct}t^{-1/2})\), using the square root of \(K\) with positive real part. The negative saddle gives its conjugate. The remaining circle is exponentially smaller by strictness of the two maxima. Hence, uniformly for \(|y|\le L\) at each fixed \(L\),
\[
a_n(t)=\frac{2e^{ct}}{\sqrt{2\pi t|K|}}e^{-\nu y^2/2}
 \cos\left(bt-n\theta-\frac{\arg K}{2}-\frac{\omega y^2}{2}\right)+o_L(e^{ct}t^{-1/2}).
\]

**Control of the whole coefficient sum.** Parseval and real Gaussian localization give \(\sum_{n\ge0}|a_n(t)|^2=O(e^{2ct}t^{-1/2})\). The boundary function \(\psi\) has a bounded continuous first derivative, including at zero in the angular coordinate, since \(\alpha>1\). Applying Parseval to \((-i\partial_x-vt)e^{t\psi(x)}\) gives
\[
\sum_{n\ge0}(n-vt)^2|a_n(t)|^2=O(e^{2ct}t^{1/2}).
\]
In fact the differentiated function is \(t(-i\psi'(x)-v)e^{t\psi(x)}\); the factor after \(t\) vanishes to at least first order at both saddles, so its squared norm has the stated bound. Outside the saddle neighborhoods there is an exponential gap. Cauchy–Schwarz with \(\sum_{|n-vt|>L\sqrt t}|n-vt|^{-2}=O((L\sqrt t)^{-1})\) gives \(e^{-ct}\sum_{|n-vt|>L\sqrt t}|a_n(t)|=O(L^{-1/2})\) for \(L\ge1\), \(t\ge1\). Thus one can first sum the local asymptotic on a fixed window and then send \(L\) to infinity.

**Irrational orders.** The angle \(\theta/\pi=(\alpha-1)/(\alpha+1)\) is irrational exactly when \(\alpha\) is. The uniformly absolutely convergent Fourier series
\[
|\cos x|=\frac2\pi+\frac4\pi\sum_{k\ge1}\frac{(-1)^k}{1-4k^2}\cos(2kx)
\]
reduces the window sum to an ordinary Gaussian Riemann sum for the constant term and oscillatory sums for each fixed \(k\ne0\). The partial sums of \(e^{-2ikn\theta}\) are bounded. Abel summation on the window against the weight \(e^{-(\nu+2ik\omega)y^2/2}\) gives a bounded sum before division by \(\sqrt t\): the total variation of the weight there is bounded at fixed \(L,k\). This estimate is uniform in the time-dependent phase. Absolute summability handles the Fourier tail, and the coefficient tail bound allows \(L\to\infty\). The normalized norm tends to \(2(2/\pi)(2\pi|K|)^{-1/2}\int_{\mathbb R}e^{-\nu y^2/2}\,dy=C_\alpha\).

**Rational orders.** Group by \(n\bmod q\) on the window. On each class the residue phase is fixed modulo \(\pi\); the window sum is a Riemann sum of mesh \(q/\sqrt t\), uniform in \(bt\) by periodicity and uniform continuity of the integrand on compact \(y\) intervals and a full phase period. The tail bounds then yield \(F_{\alpha,q}(bt)+o(1)\). Shifting by \(\pi/q\) permutes the residues. In the displayed Fourier series only indices divisible by \(q\) survive the residue average. In particular the coefficient at frequency \(2q\) is a nonzero multiple of
\[
\int_{\mathbb R}e^{-\nu y^2/2-iq\omega y^2}\,dy=\sqrt{\frac{2\pi}{\nu+2iq\omega}},
\]
so every period must be a multiple of \(\pi/q\), which is therefore fundamental. Continuity follows by dominated convergence; positivity follows because \(\omega>0\) and the integrand is positive on an interval for every phase. The constant Fourier term gives the same mean as in the irrational case. Since \(b>0\), real times tending to infinity attain every profile phase repeatedly, giving the limiting extrema and nonconvergence.

## Verification and limitations

The proof establishes the fixed-order limit and makes no assertion of a rate uniform near rational orders or near the integer endpoints. The accompanying NumPy script `CHECK.py` supplies finite diagnostics of saddle identities, the rational profile and coefficient approximations (expected line `FRACTIONAL_WIENER_ARITHMETIC_DIAGNOSTIC_OK 49`). It uses \(u=\operatorname{Re}(1/K)\) as a local variable for the quantity denoted \(\nu\) in this proof; the finite FFT diagnostic is not an aliasing bound or a proof of the asymptotic.

## Relationship to prior work

Barberán and Miana [1] provide the fractional-shift coefficients and Hardy-space framework; they do not give this normalized \(\ell^1\) asymptotic. Girard [2, §4] establishes additivity for multiple spectral maxima with distinct drift slopes and notes that convergence can fail without separation. Here the drifts coincide, so the interference must be evaluated before taking absolute values. Complex-sequence local limits [3,4] provide related Gaussian methods; their stated finite-support or exponential-decay assumptions do not directly cover this fractional symbol with a boundary branch point. The present result is the fixed-order sharp constant and explicit surviving periodic interference for this continuous-time family. Equivalent earlier results under other terminology are not ruled out.

## References

1. R. Barberán and P. J. Miana, *Entire groups generated by fractional powers of operators*, https://arxiv.org/abs/2606.16895.
2. D. M. Girard, *The asymptotic behavior of norms of powers of absolutely convergent Fourier series*, Pacific J. Math. 37 (1971), 357–381, §4, pp. 379–380. https://msp.org/pjm/1971/37-2/pjm-v37-n2-p09-p.pdf
3. L. Coeuret, *Local limit theorem for complex valued sequences*, https://arxiv.org/abs/2201.01514.
4. J.-F. Coulombel and G. Faye, *The local limit theorem for complex valued sequences: the parabolic case*, https://arxiv.org/abs/2408.12876.
