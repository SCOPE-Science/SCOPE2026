# Exact one-pole Hardy approximation of a Blaschke delay with one displaced zero

## Finding

For every integer \(N\ge2\) and real \(0<a<1\), the globally best stable degree-one rational approximation in the Hardy norm to the finite Blaschke product
\[
B_{N,a}(z)=z^{N-1}\frac{z-a}{1-az}
\]
is unique. Its only pole is real, lies beyond the negative unit-circle point, and is opposite to the displaced zero \(a\). Its exact squared error and a sharp two-term large-delay expansion are given below. For fixed \(N\), moving the displaced zero toward the circle strictly moves the optimal pole toward infinity and strictly improves the approximation.

Let \(r=r_{N,a}\) be the unique solution in \((0,1)\) of
\[
\frac{N-2}{r}-\frac{r}{1-r^2}+\frac{1-a^2}{(r+a)(1+ar)}=0.
\]
Then the unique minimizing rational function is
\[
R_{N,a}(z)=\frac{\lambda_{N,a}z}{1+rz},\qquad
\lambda_{N,a}=(-1)^{N-1}(1-r^2)r^{N-2}\frac{r+a}{1+ar},
\]
and its exact squared distance is
\[
\boxed{E_{N,a}^2=1-(1-r^2)r^{2N-4}\left(\frac{r+a}{1+ar}\right)^2.}
\]
For fixed \(a\in[0,1)\), as \(N\to\infty\),
\[
r_{N,a}=1-\frac1{2N}+\left(\frac{1-a}{2(1+a)}-\frac58\right)\frac1{N^2}+O_a(N^{-3}),
\]
\[
\boxed{1-E_{N,a}^2=\frac{1}{eN}\left(1+\frac{5a+1}{2(1+a)N}+O_a(N^{-2})\right).}
\]
For \(a=0\), the unique-pole assertion is replaced by a full circle of optimal pole parameters, each of modulus \(\sqrt{(N-1)/N}\), and
\[
1-E_{N,0}^2=\frac1N\left(\frac{N-1}{N}\right)^{N-1}.
\]

## Assumptions and scope

The Hardy space \(H^2(\mathbb D)\) has norm \(\|f\|_2^2=\sum_{j\ge0}|\widehat f(j)|^2\). The approximating class consists of all analytic rational functions \((u+vz)/(1-pz)\) with complex \(u,v,p\), \(|p|<1\); polynomial functions of degree at most one are included via \(p=0\). Equivalently, these are rational functions of type at most \((1,1)\) whose reduced denominator has no zero in the closed unit disk. The target \(B_{N,a}\) is an inner function of norm one with \(B_{N,a}(0)=0\). No claim is made for higher rational degree, multiple displaced zeros, or approximation in \(H^\infty\).

## Proof

**Orthogonal reduction.** At a fixed pole parameter \(p\), the rational space is precisely
\[
\operatorname{span}\left\{1,\frac{z}{1-pz}\right\}.
\]
The spanning vectors are orthogonal in \(H^2\), and \(\|z/(1-pz)\|_2^2=(1-|p|^2)^{-1}\). Since \(B_{N,a}(0)=0\), its constant projection vanishes, while reproducing coefficients give
\[
\left\langle B_{N,a},\frac{z}{1-pz}\right\rangle=\frac{B_{N,a}(\overline p)}{\overline p}
\]
(with the continuous value at \(p=0\)). Thus the best squared captured norm at fixed \(p\) equals
\[
\Phi(p)=(1-|p|^2)|p|^{2N-4}\left|\frac{p-a}{1-ap}\right|^2.
\]
This formula is exact; no finite truncation is used.

**The pole has a forced direction.** Put \(p=re^{i\theta}\), \(0<r<1\). The squared automorphism modulus in \(\Phi\) is
\[
\frac{r^2+a^2-2ar\cos\theta}{1+a^2r^2-2ar\cos\theta}.
\]
For \(a,r\in(0,1)\), its derivative with respect to \(\cos\theta\) has the strictly negative sign of \(-(1-a^2)(1-r^2)\). Thus for each radius its unique maximizing angle is \(\theta=\pi\), equivalently \(p=-r\). The radial objective reduces to
\[
\phi_{N,a}(r)=(1-r^2)r^{2N-4}\left(\frac{r+a}{1+ar}\right)^2.
\]
It is positive inside \((0,1)\) and tends to zero at both endpoints for \(N\ge3\); for \(N=2\) and \(a>0\), the derivative at the left endpoint is strictly positive, so the maximum is again interior.

**Uniqueness and the coefficient.** Half the logarithmic derivative of \(\phi_{N,a}\) is
\[
L_{N,a}(r)=\frac{N-2}{r}-\frac{r}{1-r^2}
+\frac{1-a^2}{(r+a)(1+ar)}.
\]
Each nonconstant summand is strictly decreasing in \(r\); the middle summand is strictly decreasing even for \(N=2\). Moreover \(L_{N,a}\) is positive as \(r\downarrow0\) (for \(N=2\), its limit is \((1-a^2)/a>0\)) and negative as \(r\uparrow1\). Hence exactly one stationary radius \(r_{N,a}\) exists and it is the strict global maximum. Projecting at \(p=-r\) gives the displayed \(\lambda_{N,a}\). The target's norm one supplies the exact squared error.

**Parameter monotonicity.** For fixed \(r\in(0,1)\), the positive factor \((r+a)/(1+ar)\) has positive derivative in \(a\), hence the optimal captured energy strictly increases with \(a\). The last term in \(L_{N,a}\) decreases strictly with \(a\), since its numerator decreases and its positive denominator increases. Implicit differentiation of the strictly decreasing equation \(L_{N,a}(r)=0\) gives \(dr_{N,a}/da<0\).

**Sharp asymptotics.** For fixed \(a<1\), the stationarity equation and its strict monotonicity first give \(r=1+O_a(N^{-1})\). Inserting \(r=1-u/N+v/N^2+O_a(N^{-3})\) in \(L_{N,a}(r)=0\) gives \(u=1/2\) and \(v=(1-a)/(2(1+a))-5/8\). This expansion is rigorous by applying the analytic implicit-function theorem after setting \(s=1/N\) and cancelling the removable factor in the stationarity equation near \((s,r)=(0,1)\): in variables \(y=(1-r)/s\), the transformed equation has nonzero \(y\)-derivative at \((s,y)=(0,1/2)\). Substitution into \(\log\phi_{N,a}(r)\) gives
\[
\log\phi_{N,a}(r)=-\log N-1+\frac{5a+1}{2(1+a)N}+O_a(N^{-2}),
\]
whence the stated sharp expansion. When \(a=0\), angular independence follows directly from the objective, and maximizing \((1-r^2)r^{2N-2}\) yields \(r^2=(N-1)/N\), proving the endpoint assertion.

## Verification

The attached standalone standard-library script `CHECK.py` checks the unique positive root numerically for multiple \((N,a)\), compares the exact capture with the direct Hardy coefficient projection and independent complex-parameter random samples, checks monotonicity, and tests the asymptotic formulas at increasing \(N\). These finite tests are supplementary and are not used to prove the all-parameter theorem. The identities and strict monotonicity above constitute the infinite proof.

## Relationship to prior work

Baratchart, Borichev, Chevillard, Coiffard Marre and Zarouf (arXiv:2603.16295, first public March 17, 2026) prove degree-sensitive lower bounds for rational approximation of finite Blaschke products, including \(z^N\), and discuss the difficulty of finding exact optimizers. Their Theorems 2 and 3 give lower bounds, not this exact one-pole optimizer or its unique directional pole law; their section on numerical experiments does not provide a global analytic determination. Wang and Qian (arXiv:2012.06184) prove existence of best rational approximants and give the general Takenaka–Malmquist reproducing-kernel approach. Its general projection principle is used here rather than claimed new; it does not specify the maximizing radius, exact distance or displacement monotonicity for this family. Published work on one-state model reduction includes general interpolation conditions and other transfer functions; the formulas here are for the specified singular Blaschke delay, not a claimed general one-state solution.

## Limitations

A single displaced zero, a single rational pole, scalar \(H^2\), and fixed real \(a\in[0,1)\) are essential to the precise formulation. The expansion is for fixed \(a\) as \(N\to\infty\), not uniform in \(a\) approaching one. The global originality comparison is necessarily literature-dependent: an equivalent elementary-special-case calculation may exist in older system identification or adaptive rational approximation sources that were not fully accessible, and independent priority verification remains open. No claim of a new general projection principle is made.

## References

1. L. Baratchart, A. Borichev, S. Chevillard, C. Coiffard Marre and R. Zarouf, *Lower bounds in \(H^2\)-rational approximation to Blaschke products*, arXiv:2603.16295 (first posted 2026-03-17), https://arxiv.org/abs/2603.16295.
2. Y.-B. Wang and T. Qian, *Pseudo-hyperbolic distance and \(n\)-best rational approximation in \(H^2\) space*, arXiv:2012.06184 (2020), https://arxiv.org/html/2012.06184v1.
3. P. Van Dooren, K. Gallivan, and P.-A. Absil, *\(H_2\)-optimal model reduction with higher-order poles*, SIAM J. Matrix Anal. Appl. 31 (2010), 2738–2753, DOI:10.1137/080731591 (general interpolation conditions; not a claimed identical result).
