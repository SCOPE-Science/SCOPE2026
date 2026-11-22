# A one-Hankel certificate and Bessel-edge phase law for separated-sign Berger charges

## Finding

A signed moment representation with positive support strictly to the right of its negative support has an exact *one-block test* for every finite order of weighted-shift hyponormality. If the positive measure has infinite support, positivity of the initial moment Hankel block of size \(k+1\) is necessary and sufficient for \(k\)-hyponormality; every later block is automatically positive definite. For one negative atom, the sharp admissible negative mass is the reciprocal of a Christoffel–Darboux diagonal kernel. A uniform positive background on an interval yields explicit strict finite-order levels, an exponential fixed-gap threshold, and a modified-Bessel edge crossover when the atom approaches the interval at inverse-square distance.

More precisely, under the definitions below, the entire family of shifted Hankel matrices obeys the Löwner inequality
\[
H_{n,k}\succeq a^n H_{0,k}\quad(n\ge0),
\]
with strict positive difference for \(n>0\). Thus one initial certificate controls *all* infinitely many moment tests. The shift is nevertheless not subnormal whenever the negative support has genuinely negative mass, because the unique compactly supported representing signed measure is not positive.

## Assumptions and scope

Fix \(0\le s<a<1\). Let \(\nu\) be a probability measure supported on \([a,1]\) whose support is infinite, and let \(\sigma\) be a positive measure of mass \(\eta\in(0,1)\), supported on \([0,s]\). Set
\[
d_n=\int t^n\,d\nu(t)-\int t^n\,d\sigma(t),\quad
\gamma_n=\frac{d_n}{1-\eta},\quad
W e_n=\sqrt{\frac{d_{n+1}}{d_n}}\,e_{n+1}.
\]
All indices \(n,k\) below are nonnegative integers; the hyponormality order \(k\) is positive. Here \(H_{n,k}=(\gamma_{n+i+j})_{i,j=0}^k\). The bounded unilateral weighted shift \(W\) is \(k\)-hyponormal exactly when all \(H_{n,k}\) are positive semidefinite; this is the standard moment criterion (see the first reference).

For the scale family \(\sigma=\eta\sigma_0\), where \(\sigma_0\) is a fixed probability measure supported on \([0,s]\), put
\[
A_k=\left(\int t^{i+j}\,d\nu\right)_{i,j=0}^k,\qquad
B_k=\left(\int t^{i+j}\,d\sigma_0\right)_{i,j=0}^k.
\]
The sharp allowable mass is
\[
\eta_k=\bigl\|A_k^{-1/2}B_k A_k^{-1/2}\bigr\|^{-1}.
\]
For the single-atom case \(\sigma_0=\delta_s\), with \(p_j\) the orthonormal polynomials for \(\nu\), this becomes
\[
\eta_k=\frac{1}{K_k(s,s)},\qquad K_k(s,s)=\sum_{j=0}^{k}|p_j(s)|^2.
\]
This Christoffel identity itself is standard; the asserted operator-level single-block sufficiency and the following sharp phase laws are the conclusions.

In the concrete interval model \(\nu(dt)=dt/(1-a)\) on \([a,1]\), let \(X=(1+a-2s)/(1-a)>1\), \(q=X+\sqrt{X^2-1}\), and let \(P_j\) be the ordinary Legendre polynomial with \(P_j(1)=1\). Then
\[
\eta_k(a,s)=\left[\sum_{j=0}^k (2j+1)P_j(X)^2\right]^{-1},
\]
\[
\eta_k(a,s)\sim \pi\sqrt{X^2-1}\,(1-q^{-2})q^{-(2k+1)}\quad(k\to\infty).
\]
For fixed \(a\in(0,1)\) and \(c\ge0\), write \(s_k=a-c/k^2\), valid for sufficiently large \(k\) (at \(c=0\), the negative point is the nonatomic endpoint and the same conclusion holds). With \(h=2\sqrt{c/(1-a)}\),
\[
\lim_{k\to\infty} k^2\eta_k(a,s_k)
=\bigl[I_0(h)^2-I_1(h)^2\bigr]^{-1}.
\]
Here \(I_0,I_1\) are the modified Bessel functions. The endpoint value \(c=0\) is exactly \(\eta_k(a,a)=1/(k+1)^2\), so its scaled limit is \(1\).

## Proof

**Existence of the shift.** Since \(\int t^n d\sigma\le\eta s^n\) and \(\int t^n d\nu\ge a^n\), we have \(d_n\ge a^n-\eta s^n>0\). More precisely, with \(u_n=\int t^n d\nu\) and \(v_n=\int t^n d\sigma\), \(v_n\le\eta s^n\le\eta u_n\); hence \(d_n\ge(1-\eta)u_n\) while \(d_{n+1}\le u_{n+1}\le u_n\). Thus \(0<w_n^2\le(1-\eta)^{-1}\) and the shift is bounded. Normalization gives \(\gamma_0=1\).

**One-block domination.** For any complex polynomial \(p(t)=\sum_{j=0}^k z_jt^j\), and every \(n\ge0\),
\[
(1-\eta)\,z^*(H_{n,k}-a^n H_{0,k})z=
\int_{[a,1]}(t^n-a^n)|p(t)|^2 d\nu(t)
+\int_{[0,s]}(a^n-t^n)|p(t)|^2 d\sigma(t)\ge0.
\]
For \(n>0\), the first integrand is strictly positive at every \(t>a\) where \(p(t)\ne0\). An infinite-support probability measure on \([a,1]\) cannot be supported on the finite zero set of a nonzero polynomial together with \(\{a\}\). Consequently the difference is positive definite. Therefore all shifted moment blocks are nonnegative if and only if the initial block is nonnegative; the equivalence to \(k\)-hyponormality now follows from the standard Hankel test.

**Not subnormal.** The signed measure \((\nu-\sigma)/(1-\eta)\) represents the entire sequence \(\gamma_n\) and has negative mass on \([0,s]\), where \(\nu\) vanishes. If a positive representing measure for \(\gamma_n\) existed on \([0,\infty)\), its support would be contained in \([0,1]\): indeed \(0<\gamma_n\le 1/(1-\eta)\) for every \(n\), and positive mass above \(1\) would force unbounded moments. Uniqueness of finite signed measures with the same moments on \([0,1]\), by density of polynomials in continuous functions, would then contradict this negative mass. Thus \(W\) is not subnormal.

**Sharp mass and the one-atom reduction.** For \(\sigma=\eta\sigma_0\), the initial block is \((A_k-\eta B_k)/(1-\eta)\). Since the support of \(\nu\) is infinite, \(A_k\) is positive definite. By conjugation with \(A_k^{-1/2}\), positivity is equivalent to \(\eta\lambda_{\max}(A_k^{-1/2}B_kA_k^{-1/2})\le1\). If \(\sigma_0=\delta_s\), then \(B_k=v_sv_s^*\), \(v_s=(1,s,\ldots,s^k)^T\). Its unique nonzero generalized eigenvalue is \(v_s^*A_k^{-1}v_s=K_k(s,s)\), by the orthonormal-polynomial change of basis. The same finite-rank argument gives the matrix kernel formula when \(\sigma_0\) consists of finitely many atoms.

**Legendre thresholds and strict rungs.** Under \(t=(1+a+(1-a)y)/2\), the measure \(\nu\) becomes \(dy/2\). Hence the orthonormal polynomials are \(\sqrt{2j+1}P_j(y)\); their values at the negative atom are \((-1)^j\sqrt{2j+1}P_j(X)\). All \(P_j(X)>0\) for \(X>1\), so \(K_{k+1}>K_k\), and \(\eta_{k+1}<\eta_k\). Since \(K_k\to\infty\), each interval \((\eta_{k+1},\eta_k]\) is nonempty and gives a non-subnormal shift that is exactly \(k\)-hyponormal but not \((k+1)\)-hyponormal. At the upper endpoint, the initial \((k+1)\)-block is singular but every later one is strictly positive definite.

**Fixed-gap asymptotic.** For fixed \(X>1\), Laplace's method applied to the standard Legendre integral
\[
P_j(X)=\frac1\pi\int_0^\pi \bigl(X+\sqrt{X^2-1}\cos\theta\bigr)^j d\theta
\]
gives
\[
P_j(X)=\frac{q^{j+1/2}}{\sqrt{2\pi j}\,(X^2-1)^{1/4}}\bigl(1+o(1)\bigr).
\]
Therefore \((2j+1)P_j(X)^2\sim q^{2j+1}/[\pi\sqrt{X^2-1}]\). Summing these geometrically growing terms backward from \(j=k\), with ratio tending to \(q^{-2}\) and dominated by a geometric majorant, yields
\[
K_k(s,s)\sim\frac{q^{2k+1}}{\pi\sqrt{X^2-1}(1-q^{-2})}.
\]
Its reciprocal is the fixed-gap expression.

**Moving hard edge.** Put \(u=c/[(1-a)k^2]\) and \(X_k=1+2u\). The elementary identity
\[
P_j(1+2u)=\sum_{\ell=0}^j\binom j\ell\binom{j+\ell}{\ell}u^\ell
\]
shows, uniformly when \(j/k\to r\in[0,1]\), convergence to
\[
\sum_{\ell=0}^\infty\frac{[r^2c/(1-a)]^\ell}{(\ell!)^2}
=I_0\bigl(2r\sqrt{c/(1-a)}\bigr).
\]
Termwise domination by \([2c/(1-a)]^\ell/(\ell!)^2\) (for \(j\le k\) and \(k\) sufficiently large) makes the convergence uniform in \(j\). Consequently
\[
\frac{K_k(s_k,s_k)}{k^2}\longrightarrow 2\int_0^1r I_0(hr)^2dr=I_0(h)^2-I_1(h)^2.
\]
The last identity follows by differentiating \(r^2(I_0(hr)^2-I_1(hr)^2)\) and using \(I_0'=I_1\) and \(I_1'=I_0-I_1/z\). The limit is strictly positive since the integral is positive, so reciprocation proves the Bessel formula. If \(c=0\), \(P_j(1)=1\) gives the exact identity \(K_k=(k+1)^2\).

## Verification

For \(a=1/2\), \(s=1/4\), the Legendre argument is \(X=2\), and
\[
K_0=1,\qquad K_1=13,\qquad K_2=657/4,\qquad K_3=8749/4.
\]
For negative mass \(\eta=1/1000\), one has \(4/8749<1/1000<4/657\), giving an explicit non-subnormal shift that is \(2\)-hyponormal but not \(3\)-hyponormal. The standalone Python checker uses exact rational arithmetic to verify these numbers, 45 positive blocks through index 14, the negative order-three initial determinant, the singular order-two boundary block at mass \(4/657\), 12 further boundary checks and 312 direct signed-support inequalities. These finite tests confirm arithmetic but are not substituted for the infinite-dimensional proof. The argument for all \(n\), all fixed \(k\), and the asymptotic limits is analytical.

## Relationship to prior work

Benhida, Curto and Exner (arXiv:2405.15000; first posted 23 May 2024) establish the Berger-type charge setting and analyze countably atomic signs, while explicitly singling out the non-atomic case as worthy of investigation. Their positivity-of-leading-atoms result does not itself imply a one-block sufficiency theorem for continuous positive background supported away from negative mass. Their earlier geometrically regular shifts (arXiv:2309.05888) provide finite-order examples with special atomic supports, not this separated-support theorem. The weighted-shift moment Hankel criterion is existing theory, not claimed as novel. Beckermann, Putinar, Saff and Stylianopoulos (arXiv:1812.06560) develop Christoffel–Darboux perturbation theory; the reciprocal kernel test for a single negative atom in a *single* Gram matrix is a familiar rank-one consequence and is not claimed independently as new. The additional statement here is that support order makes that one matrix sufficient for all shifted moment Hankel matrices, and yields the strict signed-charge hyponormality hierarchy and the specified Legendre/Bessel threshold laws.

## Limitations

The global one-block theorem requires a strict gap \(s<a\), an infinite-support positive measure and \(0<\eta<1\); it makes no assertion for interlaced positive and negative supports or arbitrary unbounded representing charges. At the single endpoint collision \(s=a\), the explicit uniform model still works because \(\nu\) has no atom at \(a\), but the general non-subnormality assertion should not be extended to overlapping atoms. No claim is made that the Christoffel rank-one identity or the standard Legendre/Bessel identities were first discovered here. Historical priority of the complete operator-level statement remains subject to specialized literature not identified in the checked sources, and independent mathematical validation has not been performed.

## References

1. Chafiq Benhida, Raúl E. Curto, George R. Exner, *Signed representing measures (Berger-type charges) in subnormality and related properties of weighted shifts*, arXiv:2405.15000 (first version 23 May 2024), https://arxiv.org/abs/2405.15000 .
2. Chafiq Benhida, Raúl E. Curto, George R. Exner, *Geometrically regular weighted shifts*, arXiv:2309.05888 (2023), https://arxiv.org/abs/2309.05888 .
3. Chafiq Benhida, Raúl E. Curto, George R. Exner, *Conditional positive definiteness as a bridge between k-hyponormality and n-contractivity*, arXiv:2012.10962 (2020), https://arxiv.org/abs/2012.10962 .
4. Bernhard Beckermann, Mihai Putinar, Edward B. Saff, Nikos Stylianopoulos, *Perturbations of Christoffel-Darboux kernels. I: detection of outliers*, arXiv:1812.06560 (2018), https://arxiv.org/abs/1812.06560 .
