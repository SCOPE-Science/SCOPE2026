# Sharp Laguerre spectral-projection instability for affine Fock composition operators

## Finding

For the normalized Gaussian Fock space \(\mathcal F^2\), fix \(0<a<1\), \(u\in\mathbb C\), and let \(T_{a,u}\) be the unweighted composition operator
\[
(T_{a,u}f)(z)=f(az+(1-a)u).
\]
The nonzero eigenvalues are the simple values \(a^n\), independently of \(u\), and their rank-one Riesz projections \(P_n\) obey, for every integer \(n\geq0\),
\[
P_nf(z)=\frac{f^{(n)}(u)}{n!}(z-u)^n,
\qquad
\boxed{\|P_n\|=e^{|u|^2/2}L_n(-|u|^2)},
\]
where \(L_n(-x)=\sum_{j=0}^n\binom nj x^j/j!\) is a classical Laguerre polynomial evaluated at a nonpositive argument.

For each fixed \(r=|u|>0\) this gives the sharp high-index law
\[
\boxed{\|P_n\|\sim \frac{\exp(2r\sqrt n)}{2\sqrt{\pi r}\,n^{1/4}}}\qquad (n\to\infty).
\]
At the critical displacement scale, if \(u_n\in\mathbb C\) varies with \(\sqrt n|u_n|\to\tau\in[0,\infty)\), with the slope \(a\) fixed, then
\[
\boxed{\|P_n(T_{a,u_n})\|\longrightarrow I_0(2\tau)},
\qquad I_0(2\tau)=\sum_{j=0}^\infty \frac{\tau^{2j}}{(j!)^2}.
\]
For every \(u\ne0\), the eigenfunctions form a complete minimal system but are not a Schauder basis under **any ordering**. Consequently \(T_{a,u}\) is not similar to a normal operator or a scalar-type spectral operator. In contrast, for \(u=0\) the eigenfunctions are an orthonormal basis and all spectral-projection norms equal one.

## Assumptions and scope

The Hilbert space consists of entire functions with
\[
\langle f,g\rangle=\frac1\pi\int_\mathbb C f(z)\overline{g(z)}e^{-|z|^2}\,dA(z),\qquad \|f\|^2=\langle f,f\rangle.
\]
The inner product is linear in its first variable, the monomials \(e_n(z)=z^n/\sqrt{n!}\) are an orthonormal basis, and the reproducing kernel is \(K_w(z)=e^{\overline w z}\). The displacement \(u\) may be complex and is the unique fixed point of the affine symbol. No claim is made for \(a=0\), \(|a|=1\), or nonaffine symbols. Unless varied explicitly for the critical scaling, \(u\) is fixed while \(n\to\infty\).

## Proof

**1. Compact operator and spectral simplicity.** Write \(d=(1-a)u\). From the Gaussian kernel identity, on the monomial basis
\[
T_{a,u}^*e_n(z)=\frac{a^n z^n}{\sqrt{n!}}e^{\overline d z}.
\]
Consequently, Tonelli's theorem and a completed Gaussian square give
\[
\|T_{a,u}\|_{\mathcal S_2}^2
=\frac1\pi\int_\mathbb C e^{-(1-a^2)|z|^2+2\operatorname{Re}(\overline d z)}dA(z)
=\frac{\exp(|d|^2/(1-a^2))}{1-a^2}<\infty.
\]
Thus \(T_{a,u}\) is compact. At the fixed point the Taylor expansion \(f(z)=\sum_{k\ge0}c_k(z-u)^k\) gives \(T_{a,u}f(z)=\sum_{k\ge0}a^kc_k(z-u)^k\). Its nonzero eigenvalues and eigenspaces are therefore exactly \(a^n\) and \(\mathbb C(z-u)^n\). If \((T_{a,u}-a^nI)g=(z-u)^n\), comparison of the \(n\)-th Taylor coefficient gives \(0=1\), so there are no Jordan chains; every nonzero eigenvalue is algebraically simple.

**2. Riesz projection and norms.** The bounded Taylor-jet functional \(f\mapsto f^{(n)}(u)/n!\) picks out precisely the eigenspace for \(a^n\), commutes with \(T_{a,u}\), and vanishes on the other eigenspaces. By the preceding spectral simplicity and compactness it is exactly the Riesz spectral projection. Set
\[
v_n(z)=\frac{(z-u)^n}{\sqrt{n!}},\qquad
w_n(z)=\frac{z^n e^{\overline u z}}{\sqrt{n!}}.
\]
The reproducing-kernel derivative identity \(f^{(n)}(u)=\langle f,z^n e^{\overline u z}\rangle\) gives \(P_nf=\langle f,w_n\rangle v_n\), with \(\langle v_m,w_n\rangle=\delta_{mn}\). In particular \(\|P_n\|=\|v_n\|\|w_n\|\).

Under the normalized complex Gaussian measure, expanding \(|z-u|^{2n}\) and using orthogonality of different monomial degrees yields
\[
\|v_n\|^2=\frac1{n!}\sum_{k=0}^n\binom nk^2k!|u|^{2(n-k)}=L_n(-|u|^2).
\]
For the dual vector, the translated Gaussian identity \(e^{2\operatorname{Re}(\overline uz)-|z|^2}=e^{|u|^2}e^{-|z-u|^2}\) gives \(\|w_n\|^2=e^{|u|^2}L_n(-|u|^2)\). Multiplying square roots proves the exact boxed formula.

**3. Sharp fixed-displacement growth.** Put \(x=|u|^2>0\), \(\lambda=\sqrt{nx}\), and define the Bessel-series weights
\[
b_j=\frac{\lambda^{2j}}{(j!)^2},\qquad Z=\sum_{j=0}^\infty b_j=I_0(2\lambda).
\]
The Laguerre sum is \(L_n(-x)=\sum_{j=0}^n b_j q_{n,j}\), with \(q_{n,j}=\prod_{k=0}^{j-1}(1-k/n)\) for \(j\le n\) and zero otherwise. The ratios \(b_{j+1}/b_j=\lambda^2/(j+1)^2\) imply, by geometric-tail comparison around its mode, that the probability weights \(b_j/Z\) concentrate at \(j/\lambda\to1\) as \(\lambda\to\infty\). On any fixed shrinking-relative neighbourhood of that mode,
\[
\log q_{n,j}=-\frac{j(j-1)}{2n}+O\left(\frac{j^3}{n^2}\right)\longrightarrow -\frac x2.
\]
Because \(0\le q_{n,j}\le1\), the concentration and bounded convergence yield \(L_n(-x)/I_0(2\sqrt{nx})\to e^{-x/2}\). Finally, the elementary integral
\[
I_0(2\lambda)=\frac1\pi\int_0^\pi e^{2\lambda\cos\theta}\,d\theta
\sim\frac{e^{2\lambda}}{2\sqrt{\pi\lambda}}
\]
by Laplace's method. Multiplication by \(e^{x/2}\) gives the stated sharp prefactor with no unproved spectral asymptotic assumption.

**4. Critical scaling.** Write \(x_n=|u_n|^2\) and assume \(nx_n\to\tau^2\). For each fixed \(j\),
\[
\binom nj\frac{x_n^j}{j!}\to\frac{\tau^{2j}}{(j!)^2}.
\]
For all sufficiently large \(n\), the terms are bounded by \(C^j/(j!)^2\) for a fixed \(C>\tau^2\); therefore dominated convergence for series and \(e^{x_n/2}\to1\) give the Bessel crossover, including \(\tau=0\).

**5. Basis and similarity obstruction.** The finite span of \((z-u)^n\) is exactly the polynomial space, dense in \(\mathcal F^2\). The nonzero bounded biorthogonal functionals \(f\mapsto f^{(n)}(u)/n!\) prove minimality. Were these eigenfunctions a Schauder basis in any enumeration, the uniform boundedness principle applied to its partial-sum projections would bound all coordinate rank-one projections, which are exactly \(P_n\). This contradicts the sharp growth whenever \(u\ne0\). Finally, a bounded invertible similarity to a normal or scalar-type spectral operator gives uniformly bounded isolated spectral projections, another contradiction. At \(u=0\) the normalized eigenfunctions are the monomials \(e_n\), furnishing the contrasting orthonormal case.

## Verification

The standalone script `check.py` uses only Python's standard library. Run `python3 check.py` in the directory containing this file; the successful run prints `VERIFICATION_OK 993`. It checks exactly (with rational arithmetic) polynomial Laguerre norms, biorthogonality, and finite polynomial-matrix intertwining identities, and numerically checks dual-vector norms, the fixed-displacement asymptotic, and the Bessel crossover. Finite tests do **not** certify the infinite spectral or asymptotic statements; those follow from the steps above.

## Relationship to prior work

Mengestie–Seyoum (2019) investigate Fock-type composition spectra; Chalendar–Partington (2021) analyze Fock affine-composition iteration, including its limiting evaluation projection. Seyoum–Mengestie (2021) determine Fock weighted-composition spectra, and Mengestie (2022), Lemma 2.1, identifies the shifted polynomial eigenvectors. The present calculation uses these spectral objects and adds exact **all-index** rank-one Riesz-projection norms, a sharp high-index growth coefficient, the displacement-scale Bessel transition, and the basis/similarity obstruction. The previously known fixed-point evaluation projection is exactly the \(n=0\) instance and is not asserted to be new.

## Limitations

The growth law assumes fixed nonzero displacement; the crossover covers bounded scaled displacement only. The slope is strictly real and between zero and one; general complex slopes are outside the stated domain even though related statements may be possible. The argument does not estimate resolvent norms between eigenvalues or classify nonaffine composition symbols. The literature comparison is based on the identified full-text sources and searchable records; exact priority against unindexed literature is not proved.

## References

1. T. Mengestie and W. Seyoum, *Spectra of composition operators on Fock-type spaces*, Quaestiones Mathematicae (online 28 November 2019), DOI: https://doi.org/10.2989/16073606.2019.1692092.
2. I. Chalendar and J. R. Partington, *Weighted composition operators on the Fock space: iteration and semigroups*, first public 1 June 2021, https://arxiv.org/abs/2106.00427.
3. W. Seyoum and T. Mengestie, *Spectrums and Uniform Mean Ergodicity of Weighted Composition Operators on Fock Spaces*, published online 7 October 2021, DOI: https://doi.org/10.1007/s40840-021-01203-x.
4. T. Mengestie, *Dynamics of Weighted Composition Operators and Their Adjoints on the Fock Space*, published 24 February 2022, DOI: https://doi.org/10.1007/s11785-022-01204-z.
