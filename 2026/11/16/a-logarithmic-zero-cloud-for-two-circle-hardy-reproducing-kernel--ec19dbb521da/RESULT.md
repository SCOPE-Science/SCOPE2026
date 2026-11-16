# A logarithmic zero cloud for two-circle Hardy reproducing kernels

## Finding
For any fixed \(0<a<1\), put \(\rho=\sqrt a\). For each integer \(N\ge1\), give the analytic Hardy space on \(\mathbb D\) the two-circle norm
\[
\|f\|_N^2=\frac{1}{1+a^{-N}}\int_{|z|=1}|f(z)|^2\,dm(z)
+\frac{a^{-N}}{1+a^{-N}}\int_{|z|=\rho}|f(z)|^2\,dm_\rho(z),
\]
where \(dm\) and \(dm_\rho\) are normalized angular measures on their respective circles. Its reproducing kernel is
\[
K_N(z,w)=(1+a^{-N})F_N(z\overline w),\qquad
F_N(s)=\sum_{n=0}^\infty\frac{s^n}{1+a^{n-N}},\quad |s|<1.
\]
**Zero cloud theorem.** For every \(r\) with \(a<r<1\), there exists \(N_0(a,r)\) such that, for all integers \(N\ge N_0(a,r)\), exactly \(N\) scalar zeros of \(F_N\), counted with multiplicity, lie in \(|s|<r\), and none lies on \(|s|=r\). These \(N\) zeros lie in an annulus whose inner and outer radii both converge to \(a\); equivalently, the count is logarithmic in the inner-to-outer mass ratio because \(N=\log(a^{-N})/\log(1/a)\). Their angular empirical probability measures converge weakly to normalized Lebesgue measure on \(\mathbb T\).

Moreover, **for every** \(N\ge1\), there is an explicit zero-free disk:
\[
F_N(s)\ne0\quad\text{when}\quad
|s|<R_N:=\frac{a^N+a}{a^N+1}>a.
\]
The count refers to the scalar parameter \(s=z\overline w\), not to the cardinality of the two-variable off-diagonal zero set. In particular, the two-circle reproducing kernels have arbitrarily many distinct scalar zero fibres while each Hilbert space consists, as a set, of the usual Hardy functions.

## Assumptions and scope
The parameter \(a\) is fixed strictly between zero and one. The integer \(N\) tends to infinity, and the test radius \(r\) is fixed in \((a,1)\). The weight \(a^{-N}\) is a positive relative mass on the *inner* circle; the associated inner radius is \(\sqrt a\), so scalar kernel products accumulate at the *squared* radius \(a\). All zeros and multiplicities are complex-analytic, and all convergence assertions concern fixed \(a\). The proof does not assume that the zeros are simple.

## Proof
**1. Exact kernel and lower zero exclusion.** Write \(f(z)=\sum_{n\ge0}f_nz^n\). Orthogonality of monomials on both concentric circles gives
\[
\|f\|_N^2=(1+a^{-N})^{-1}\sum_{n\ge0}(1+a^{n-N})|f_n|^2.
\]
The weight is bounded above and below by positive constants for each fixed \(N\), hence the Hilbert space is the standard Hardy space as a set. Reciprocal squared monomial norms give the claimed kernel. Set \(c_n=(1+a^{n-N})^{-1}\). For \(n\ge1\),
\[
\frac{c_{n-1}}{c_n}=\frac{1+a^{n-N}}{1+a^{n-1-N}}.
\]
This ratio is strictly increasing with \(n\), since \(t\mapsto(1+at)/(1+t)\) is strictly decreasing for \(t>0\) and \(a^{n-1-N}\) strictly decreases with \(n\). Its minimum is
\[
\frac{c_0}{c_1}=\frac{a^N+a}{a^N+1}=R_N>a.
\]
The Eneström–Kakeya theorem applied to every nonconstant Taylor polynomial \(\sum_{n=0}^{M}c_ns^n\) excludes zeros in \(|s|<R_N\). The polynomials converge locally uniformly to \(F_N\); Hurwitz's theorem, together with \(F_N(0)>0\), gives the same zero exclusion for \(F_N\).

**2. Bilateral limit on an annulus.** On \(a<|s|<1\), put
\[
H_N(s)=s^{-N}F_N(s)=\sum_{j=-N}^\infty\frac{s^j}{1+a^j},\qquad
G_a(s)=\sum_{j\in\mathbb Z}\frac{s^j}{1+a^j}.
\]
The positive-index tail converges geometrically whenever \(|s|<1\). For negative \(j=-k\), the summand has modulus \((a/|s|)^k/(1+a^k)\). It follows that \(H_N\to G_a\), together with all derivatives, uniformly on compact subsets of \(a<|s|<1\).

To establish zero-freeness and the exact winding number of \(G_a\), use the standard \(q\)-Pochhammer symbol \((x;a)_\infty=\prod_{k=0}^\infty(1-xa^k)\). The identity \(({-1};a)_j/({-a};a)_j=2/(1+a^j)\), valid for every integer \(j\), identifies \(2G_a\) with Ramanujan's bilateral \({}_1\psi_1\) series at parameters \((-1,-a;a,s)\). The summation formula, valid exactly for \(a<|s|<1\), gives
\[
G_a(s)=\frac{(a;a)_\infty^2}{2(-a;a)_\infty^2}
\frac{(-s;a)_\infty(-a/s;a)_\infty}
{(s;a)_\infty(a/s;a)_\infty}.
\]
No numerator or denominator factor vanishes in that annulus: factors depending on \(s\) only have zeros of modulus at least \(1\); factors depending on \(a/s\) have zeros of modulus at most \(a\). Thus \(G_a\) is holomorphic and nowhere zero in the annulus.

For a fixed circle \(|s|=r\) with \(a<r<1\), each factor \(1\pm a^k s\) has winding zero, since its zero lies outside that circle. Each factor \(1\pm a^{k+1}/s\) has one zero and one pole strictly inside the circle and therefore also has winding zero. The product converges uniformly and is nowhere zero on the circle, so the winding number of \(G_a\) around zero is **zero**. This is stronger than simply knowing it has no zeros in an annulus.

**3. Exact interior count.** Uniform convergence on the fixed circle, with \(G_a\) bounded away from zero there, implies that \(H_N\) is nonvanishing on the circle and has the same winding number, namely zero, for all sufficiently large \(N\). Since \(F_N(s)=s^N H_N(s)\), the winding number of \(F_N\) on that circle is \(N\). The argument principle therefore gives exactly \(N\) zeros in \(|s|<r\), counted with multiplicity, for every sufficiently large \(N\). The count includes every zero inside that circle; no omitted zeros are implicitly added.

**4. Radial collapse and uniform angles.** The zero-free bound in step 1 shows that every counted zero has modulus at least \(R_N>a\). Apply step 3 to any other fixed radius \(r'\in(a,r)\): for sufficiently large \(N\), exactly the same number \(N\) of zeros lies in \(|s|<r'\), so all the original zeros do. Because \(r'\) can be chosen arbitrarily close to \(a\), the largest and smallest moduli among these \(N\) zeros converge to \(a\).

Write these zeros with multiplicity as \(s_{N,1},\ldots,s_{N,N}\). For each integer \(k\ge1\), the residue theorem and logarithmic differentiation give
\[
\sum_{j=1}^N s_{N,j}^{k}
=\frac{1}{2\pi i}\oint_{|s|=r}
 s^k\frac{F_N'(s)}{F_N(s)}\,ds
=\frac{1}{2\pi i}\oint_{|s|=r}
 s^k\frac{H_N'(s)}{H_N(s)}\,ds.
\]
Here the discarded integrand \(Ns^{k-1}\) has zero contour integral because \(k\ge1\). The last integral is bounded independently of \(N\), by uniform convergence of \(H_N\) and \(H_N'\) and the nonvanishing of \(G_a\) on the circle. Thus \(N^{-1}\sum_j s_{N,j}^{k}\to0\). Uniform radial convergence to \(a>0\) implies
\[
\frac1N\sum_{j=1}^N\left(\frac{s_{N,j}}{|s_{N,j}|}\right)^k\longrightarrow0
\quad(k=1,2,\ldots).
\]
The negative moments converge to zero by conjugation. Trigonometric polynomial approximation now proves weak convergence of the angular empirical measures to Haar probability on \(\mathbb T\). This completes the proof.

## Verification
A standalone standard-library Python script, `CHECK.py`, evaluates the bilateral series and Ramanujan product at representative parameters, confirms coefficient-ratio identities, and computes numerical phase winding for selected \(N\) and \(a\). It returns 23 successful finite tests. It is a consistency check, not a replacement for the infinite-product identity, Hurwitz theorem, argument principle, or equidistribution proof. The claim holds for all fixed \(0<a<1\), not just the sampled values.

## Relationship to prior work
The 2026 public report and subsequent preprint by Pennanen, Rättyä, Wang and Wu concern *off-diagonal estimates* for radial Bergman kernels; these motivate looking at what radial moment sequences can say about kernels, but provide no zero-count theorem for the present two-circle Hardy norm. The annular Szegő kernel work of Gafai, Murid and Wahid establishes an infinite product for an entire *bilateral* Laurent kernel, including nonvanishing criteria for its weighted variants. The bilateral limit in step 2 is closely related, and its nonvanishing is therefore not new in isolation; the claimed increment is the exact zero cloud, radial localization and angular law for the one-sided, \(N\)-dependent disk kernels. Katori and Shirai analyze a *random Gaussian Laurent series* with weighted Szegő covariance and its random zeros, not these deterministic kernel zeros. Ameur, Charlier and Cronvall study hard-wall random-matrix correlation asymptotics involving related weighted kernels rather than this exact one-sided truncation geometry. The Ramanujan identity is classical and expressly credited, not asserted as a new lemma.

## Limitations
The theorem does not classify zeros in a boundary layer approaching \(|s|=1\), nor does it provide a rate of angular equidistribution, simplicity of all counted zeros, or uniformity as \(a\) tends to either endpoint. An asymptotic scalar zero count in each fixed disk is not a global enumeration of every kernel zero in \(\mathbb D\). The two-circle Hilbert norm is singular as a radial *area* weight, so any conclusions about absolutely continuous weighted Bergman spaces would require a separate argument. Possible equivalent results under theta-function or finite-section terminology remain a literature-priority risk.

## References
1. A. Pennanen, J. Rättyä, S. Wang and F. Wu, *Optimal off-diagonal upper estimates for Bergman reproducing kernels*, public seminar announcement dated 2026-05-25, https://www.stu.edu.cn/cmac/info/1531/38351.htm ; preprint https://arxiv.org/abs/2607.19959 (v1 posted 2026-07-22).
2. N. S. Gafai, A. H. M. Murid and N. H. A. A. Wahid, *Infinite Product Representation for the Szegö Kernel for an Annulus*, Journal of Function Spaces (2022), https://doi.org/10.1155/2022/3763450 ; preprint https://arxiv.org/abs/2202.09114 .
3. M. Katori and T. Shirai, *Zeros of the i.i.d. Gaussian Laurent Series on an Annulus: Weighted Szegő Kernels and Permanental–Determinantal Point Processes*, Communications in Mathematical Physics 392 (2022), https://doi.org/10.1007/s00220-022-04365-2 .
4. Y. Ameur, C. Charlier and J. Cronvall, *Random Normal Matrices: Eigenvalue Correlations Near a Hard Wall*, Journal of Statistical Physics 191 (2024), https://doi.org/10.1007/s10955-024-03314-8 .
5. NIST Digital Library of Mathematical Functions, §17.8.2, Ramanujan's \({}_1\psi_1\) summation, https://dlmf.nist.gov/17.8.E2 .
6. Eneström–Kakeya zero annulus theorem, Hurwitz's theorem, the argument principle, and the trigonometric-polynomial approximation theorem (classical standard results).
