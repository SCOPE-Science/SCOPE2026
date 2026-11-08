# Circle condensation and exact bulk zero counts for two-step Bergman weights

## Finding
Fix any real \(0<a<1\). For each positive integer \(m\), equip the open unit disk \(\mathbb D\) with the radial weight
\[
\omega_{a,m}(z)=1+a^{-m}\mathbf 1_{\{|z|^2<a\}}.
\]
Take area measure \(dA/\pi\). Write \(s=z\overline w\) and denote the scalar weighted Bergman kernel by \(K_{a,m}(s)\). For every fixed \(r\) satisfying \(a<r<1\), there exists an integer \(M(a,r)\) such that for every \(m\ge M(a,r)\), \(K_{a,m}\) has **exactly \(m-1\) zeros, counted with multiplicities, in \(|s|<r\)**, and no zeros on \(|s|=r\).

Moreover, if these \(m-1\) zeros are listed with multiplicity as \(\zeta_{m,1},\ldots,\zeta_{m,m-1}\), then their empirical measures satisfy
\[
\frac1{m-1}\sum_{j=1}^{m-1}\delta_{\zeta_{m,j}}
\;\Longrightarrow\;
\frac{d\theta}{2\pi}\quad\text{on the circle }s=a e^{i\theta}.
\]
Thus one jump-weight family produces an unbounded sequence of exact kernel-zero counts, and its bulk zeros equidistribute around the weight's radial discontinuity in the scalar product coordinate.

## Assumptions and scope
The theorem holds for all fixed real \(0<a<1\) and fixed \(a<r<1\) as \(m\to\infty\). The integer \(M(a,r)\) is existential, not claimed uniform in the two parameters. Each weight is strictly positive and bounded above and below on the disk for its fixed \(m\); the bound is not uniform as \(m\to\infty\). Zeros are those of the scalar function of \(s=z\overline w\), not diagonal points \(z=w\), where positivity prevents vanishing. Every scalar \(|s|<1\) is attained by some pair \(z,w\in\mathbb D\). Zeros arbitrarily close to \(|s|=1\) are not counted or classified here.

## Proof
**1. Exact kernel.** Orthogonality of monomials and the choice of normalized area measure give, for every integer \(n\ge0\),
\[
\|z^n\|_{a,m}^2=\frac{1+a^{n+1-m}}{n+1}.
\]
Consequently, with locally uniform convergence on \(|s|<1\),
\[
K_{a,m}(s)=\sum_{n=0}^\infty\frac{n+1}{1+a^{n+1-m}}s^n.\tag{1}
\]

**2. Inner and outer scaling limits.** For every compact subset of \(|s|<a\), dominated convergence in (1) yields
\[
a^{1-m}K_{a,m}(s)
=\sum_{n=0}^\infty\frac{(n+1)(s/a)^n}{1+a^{m-n-1}}
\longrightarrow (1-s/a)^{-2}.\tag{2}
\]
In particular, no zeros remain in any fixed compact subset of \(|s|<a\) for large \(m\).

For \(a<|s|<1\), put \(j=n-m\) in (1):
\[
\frac{K_{a,m}(s)}{m s^m}
=\sum_{j=-m}^\infty
\frac{1+(j+1)/m}{1+a^{j+1}}s^j
\longrightarrow
\Phi_a(s):=\sum_{j\in\mathbb Z}\frac{s^j}{1+a^{j+1}}.\tag{3}
\]
This convergence is uniform on compact subannuli. For negative \(j\), the summands are dominated by geometric multiples of \((a/|s|)^{|j|}\), and for nonnegative \(j\), by polynomial multiples of \(|s|^j\).

**3. A bilateral-product zero exclusion and its winding.** Write \((v;a)_\infty=\prod_{k\ge0}(1-va^k)\). The classical Ramanujan bilateral summation (also used for annular Szegő kernels) specializes to
\[
\Phi_a(s)=C_a
\frac{(-as;a)_\infty(-1/s;a)_\infty}
{(s;a)_\infty(a/s;a)_\infty},\qquad
C_a=\frac{(a;a)_\infty^2}{(-a;a)_\infty(-1;a)_\infty}>0.\tag{4}
\]
The product converges normally and has no zeros or poles on \(a<|s|<1\): the numerator zeros are at \(s=-a^k\), \(k\ge0\), and \(s=-a^{-k-1}\), \(k\ge0\); the denominator's are at \(s=a^{k+1}\) and \(s=a^{-k}\), respectively. All are on or outside that open annulus.

On the positively oriented circle \(|s|=r\), \(a<r<1\), all factors except the \(k=0\) factor \(1+1/s\) of \((-1/s;a)_\infty\) have winding zero: factors with an inner zero also have a compensating pole at the origin, and factors whose zeros are outside the circle have neither. The factor \(1+1/s=(s+1)/s\) has winding \(-1\). Therefore
\[
\operatorname{wind}_{|s|=r}\Phi_a=-1.\tag{5}
\]
By the zero-free compact-annulus limit (3), \(K_{a,m}(s)/(m s^m)\) has the same winding \(-1\) on \(|s|=r\) for sufficiently large \(m\). Hence the argument principle gives \(N_{a,m}(r)=m-1\), and simultaneously excludes boundary zeros. This proves the exact count.

**4. Distribution of the counted zeros.** Define the subharmonic functions
\[
u_m(s)=\frac1m\log |K_{a,m}(s)|.
\]
Equations (2) and (3), together with the nonvanishing of their respective limits, imply pointwise convergence away from \(|s|=a\):
\[
u_m(s)\longrightarrow u(s):=\max\{\log a,\log|s|\}.
\]
For every \(R<1\), coefficient positivity and \((n+1)/(1+a^{n+1-m})\le n+1\) give the locally uniform upper bound \(u_m(s)\le -2\log(1-R)/m\) on \(|s|\le R\). Also \(u_m(0)\to\log a\). Compactness for subharmonic functions and uniqueness of the almost-everywhere pointwise limit therefore yield \(u_m\to u\) in \(L^1_{\mathrm{loc}}(\mathbb D)\).

Applying the distributional Laplacian gives
\[
\frac1m\sum_{K_{a,m}(\zeta)=0}\delta_\zeta
=\frac1{2\pi}\Delta u_m
\longrightarrow\frac1{2\pi}\Delta u
=\text{normalized arclength measure on }|s|=a,\tag{6}
\]
where equality of measures is locally on \(\mathbb D\), and zeros are counted with multiplicity. By (2)–(4), for each fixed \(0<\varepsilon<\min(a,1-a)\), all zeros in the disk \(|s|<r\) eventually lie within \(a-\varepsilon<|s|<a+\varepsilon\) (with \(r>a+\varepsilon\) if necessary, then use a smaller \(\varepsilon\)). The exact number \(m-1\) from step 3 converts (6) into the asserted empirical weak convergence for the zeros inside any prescribed \(|s|<r\).

## Verification
The accompanying standalone checker `verify_step_weight.py` evaluates the exact monomial-kernel series and verifies six numerically computed argument-principle windings on three jump radii, as well as three independent bilateral-sum/product identities. Its recorded result is `STEP_BERGMAN_CHECK_PASS argument_windings=6 product_identities=3`. All calculations are approximate checks, not exact certificates of the eventual count or weak convergence; the proofs of those infinite assertions are steps 1–4 above.

To replay, run `python verify_step_weight.py` using standard-library Python. The input parameters, Fourier contour resolution, truncation lengths, and tolerances are specified in that file. No other files or network access are required.

## Relationship to prior work
Zeytuncu (2010) introduced a two-step bounded radial weight with a provable Bergman-kernel zero and observed that suitable changes in the step parameters likewise produce zeros. Della Pella (2014) developed a range of step heights yielding at least one zero and numerical truncated-kernel comparisons. Neither treatment supplies the eventual exact \(m-1\) count or equidistribution for the exponentially growing height specified here.

Perälä (2017) established that a fixed radial disk weight has only finitely many kernel zeros and produced weights with arbitrarily many by a different, iterated construction. There is no conflict: each \(\omega_{a,m}\) is fixed with finitely many zeros, while the parameter \(m\) tends to infinity. The present result identifies an especially simple two-step family and precise bulk zero asymptotics.

The bilateral product (4) is a specialization of Ramanujan's classical sum; Gafai, Murid, and Wahid (2022) use such sums to study weighted Szegő kernels of annuli. This is an analytical ingredient, not a claim of originality for the product identity. The asserted novelty is its application to exact bulk zero counts and angular condensation for these Bergman kernels.

## Limitations
The theorem gives no effective value of \(M(a,r)\), no rate of angular equidistribution, and no classification of possible additional zeros in the boundary layer \(|s|\to1\). It does not assert all zeros of \(K_{a,m}\) are among the \(m-1\) bulk zeros. The parameters \(a\) and \(r\) must remain fixed as \(m\to\infty\), and the result does not classify weights with multiple steps. Historical priority is conditional on the inspected literature; general unpublished or unlocated step-kernel theorems may exist. No independent validation is claimed.

## References
- Y. E. Zeytuncu, *Weighted Bergman Projections and Kernels: Lp Regularity and Zeros* (2010), arXiv:1009.2806, https://arxiv.org/abs/1009.2806.
- A. Della Pella, *Bergman Kernel Zeroes For A Range Of Weights* (dated September 8, 2014), https://dept.math.lsa.umich.edu/~adellape/PDFS/weightedbergmankernelzeros.pdf.
- A. Perälä, *Vanishing Bergman Kernels on the Disk* (first public March 17, 2017), arXiv:1703.05976, https://arxiv.org/abs/1703.05976.
- B. J. Boudreaux, *Equivalent Bergman Spaces with Inequivalent Weights* (2018), arXiv:1802.01099, https://arxiv.org/abs/1802.01099.
- S. Gafai, A. H. M. Murid and A. Wahid, *Infinite Product Representation for the Szegö Kernel for an Annulus* (2022), arXiv:2202.09114, https://arxiv.org/abs/2202.09114.
