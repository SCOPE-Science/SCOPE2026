# A real-analytic strictly positive definite sphere kernel with one harmonic mode in every degree

## Finding

There is an explicit **real-valued, symmetric, real-analytic, strictly positive definite** kernel on the unit two-sphere whose integral operator has **exactly one positive eigenvalue in each spherical-harmonic degree** and no other positive eigenvalues. In particular, every degree is represented, but its positive coefficient block has rank one rather than full rank \(2n+1\).

Here is a fully specified example. For \(x=(x_1,x_2,x_3)\in S^2\), set \(u(x)=x_1+ix_2\), \(v(x)=x_3\). Assign one real harmonic \(F_n\) in each degree as follows:

\[
F_0(x)=1,\qquad F_1(x)=v(x).
\]

For each integer \(j\ge1\), let \(s_j=2+j(j-1)/2\) and \(I_j=\{s_j,\ldots,s_j+j-1\}\). These intervals partition the integers \(n\ge2\). For \(n\in I_j\), define

\[
F_n(x)=\begin{cases}
\operatorname{Re}(u(x)^n),&j\equiv1\pmod4,\\
\operatorname{Im}(u(x)^n),&j\equiv2\pmod4,\\
v(x)\operatorname{Re}(u(x)^{n-1}),&j\equiv3\pmod4,\\
v(x)\operatorname{Im}(u(x)^{n-1}),&j\equiv0\pmod4.
\end{cases}
\]

Then

\[
\boxed{K(x,y)=\sum_{n=0}^{\infty}2^{-n}F_n(x)F_n(y)}
\]

is strictly positive definite for **every finite collection of distinct sites** on \(S^2\). Furthermore, although the kernel interpolates arbitrary data at every such finite collection, it is not characteristic to probability measures: the distinct measures \((1+\varepsilon x_1)d\sigma\) and \((1-\varepsilon x_1)d\sigma\), for any fixed \(0<\varepsilon<1\) and normalized surface measure \(\sigma\), have identical kernel mean embeddings.

## Assumptions and scope

The space is the real unit sphere \(S^2=\{x\in\mathbb R^3:\|x\|=1\}\), with complex coefficients allowed in finite Gram quadratic forms. A kernel is strictly positive definite if for all integers \(N\ge1\), distinct sites \(x_1,\ldots,x_N\), and nonzero \(c\in\mathbb C^N\), the sum \(\sum_{p,q=1}^N c_p\overline{c_q}K(x_p,x_q)\) is positive. The surface measure \(\sigma\) has total mass one. Real and imaginary parts above are real polynomials in the two real coordinates, and the degree index is the **spherical-harmonic degree**, not a Fourier azimuthal order.

Each of the four residue classes of block indices \(j\bmod4\) contains intervals \(I_j\) of arbitrarily large consecutive length. Every \(F_n\) is nonzero and bounded in absolute value by one on the real sphere.

## Proof

**1. Harmonicity, smoothness, and spectral rank.** The ambient polynomials \(u^n\) are harmonic, since \((\partial_{x_1}^2+\partial_{x_2}^2)u^n=0\), and \(v u^{n-1}\) are harmonic because \(\partial_{x_3}u^{n-1}=0\). Their real and imaginary parts are real homogeneous harmonic polynomials of degree \(n\). Thus \(F_n\) is a spherical harmonic of degree \(n\). As \(|F_n(x)|\le1\), the kernel series converges absolutely and uniformly. Polynomial complexification in a sufficiently small neighborhood of \(S^2\times S^2\) is still dominated by a geometric series with ratio below one (take a coordinate neighborhood in which both \(|x_1\pm ix_2|\) and \(|y_1\pm iy_2|\) are below \(\sqrt2\)); hence \(K\) is real analytic. The sum-of-squares representation proves positive semidefiniteness. Orthogonality of different harmonic degrees shows that the integral operator on \(L^2(S^2,d\sigma)\) has restriction \(2^{-n}|F_n\rangle\langle F_n|\) on degree \(n\). It therefore has exactly one positive eigenvalue \(\lambda_n=2^{-n}\|F_n\|_{L^2(\sigma)}^2\) in each degree, all other \(2n\) eigenvalues in that degree being zero for \(n\ge1\). In fact the positive eigenvalues are explicit: \(\lambda_0=1\), \(\lambda_1=1/6\), and for \(n\ge2\)

\[
\lambda_n=2^{-n}\begin{cases}
\dfrac{\sqrt\pi\,\Gamma(n+1)}{4\Gamma(n+3/2)},&F_n=\operatorname{Re}(u^n)\text{ or }\operatorname{Im}(u^n),\\
\dfrac{\sqrt\pi\,\Gamma(n)}{8\Gamma(n+3/2)},&F_n=v\operatorname{Re}(u^{n-1})\text{ or }v\operatorname{Im}(u^{n-1}).
\end{cases}
\]

These values follow from uniform longitude averaging of squared sines/cosines and a one-dimensional beta integral in \(v=x_3\).

**2. Consecutive-block moment lemma.** Let \(U\) be a finite subset of \(\mathbb C\setminus\{0\}\), and let \((a_z)_{z\in U}\) be arbitrary complex numbers. Suppose \(\sum_{z\in U}a_z\operatorname{Re}(z^n)=0\) for every exponent in arbitrarily long consecutive blocks belonging to one index set, and \(\sum_{z\in U}a_z\operatorname{Im}(z^n)=0\) for every exponent in arbitrarily long consecutive blocks belonging to another index set. Extend the weights by zero outside \(U\) and write \(W=U\cup\overline U\). The first moment equations are equivalent to

\[
\sum_{w\in W}\frac{a_w+a_{\overline w}}2 w^n=0,
\]

and the second are equivalent to

\[
\sum_{w\in W}\frac{a_w-a_{\overline w}}{2i}w^n=0.
\]

For either equation, choose a single consecutive block of at least \(|W|\) exponents, say \(n_0,\ldots,n_0+|W|-1\). The associated matrix factors as a diagonal matrix with entries \(w^{n_0}\ne0\) times the ordinary Vandermonde matrix on pairwise distinct \(w\in W\). Its determinant is nonzero. Both coefficient families vanish, so \(a_w=0\) for every \(w\in U\). The conclusion is unchanged if all exponents in the second pair of moment systems are shifted by minus one, because consecutive runs remain consecutive and the nodes are nonzero.

**3. Finite-site strict positivity.** Let distinct sites \(x_p\in S^2\) and complex numbers \(c_p\) satisfy \(\sum_p c_p F_n(x_p)=0\) for every \(n\ge0\). Put \(z_p=u(x_p)\). For each distinct projection \(z\), set

\[
A_z=\sum_{p:z_p=z}c_p,\qquad B_z=\sum_{p:z_p=z}c_pv(x_p).
\]

The equations in the arbitrarily long blocks of type \(\operatorname{Re}(u^n)\) and \(\operatorname{Im}(u^n)\), by step 2, imply \(A_z=0\) for every nonzero projected value \(z\). The two types \(v\operatorname{Re}(u^{n-1})\) and \(v\operatorname{Im}(u^{n-1})\) similarly imply \(B_z=0\) for every nonzero \(z\). The degree-zero equation \(F_0=1\) then yields \(A_0=0\), and the degree-one equation \(F_1=v\) yields \(B_0=0\).

A fibre of the projection \(u:S^2\to\overline{\mathbb D}\) has at most two points; if two occur, their distinct vertical coordinates are \(\pm\sqrt{1-|z|^2}\). Therefore the two equations \(A_z=B_z=0\) force each coefficient \(c_p\) on that fibre to vanish (for a one-point fibre, \(A_z=0\) suffices). All \(c_p\) vanish. Finally, the Gram quadratic form equals \(\sum_n2^{-n}|\sum_p c_pF_n(x_p)|^2\), and thus cannot vanish for nonzero \(c\). This proves strict positive definiteness with no bound on the number or arrangement of sites.

**4. Failure of characteristicness and universality.** The real degree-one harmonic \(g(x)=x_1\) is orthogonal to \(F_1=x_3\), as well as to \(F_n\) for all other degrees, under normalized surface measure. Hence \(\int K(x,y)g(y)d\sigma(y)=0\) for every \(x\). Both probability measures \(d\mu_\pm=(1\pm\varepsilon g)d\sigma\) are positive and distinct when \(0<\varepsilon<1\), yet their kernel embeddings agree. The same orthogonality to the nonzero continuous function \(g\) shows that the kernel's reproducing space is not dense in \(C(S^2)\) under the uniform norm.

## Verification

The included standalone \(\texttt{check.py}\) can be run with Python 3, NumPy and SymPy. It checks ambient harmonicity and degree homogeneity symbolically for 17 initial features, checks 990 exact block assignments, and tests ten configurations (including projected two-point fibres, both poles, regular equatorial polygons, conjugate longitudes and generic sites) against truncated positive Gram spectra. A recorded run passed **1034** finite assertions, with smallest tested Gram eigenvalue approximately \(1.9248516\times10^{-11}\). Those finite diagnostics are **not** a proof of positivity for all finite configurations; that conclusion follows from step 3.

For independent mathematical checking, the critical steps are the identity for \(\operatorname{Re}(z^n)\) and \(\operatorname{Im}(z^n)\), the invertible nonzero-node Vandermonde matrix over a long consecutive block, the treatment of \(z=0\) by degrees zero and one, and the two-point fibre geometry of the sphere. None requires a numerical extrapolation or a probabilistic generic-position hypothesis.

## Relationship to prior work

Jäger's 2020 preprint gives harmonic-coefficient characterizations of positive and strictly positive definite non-isotropic kernels on \(S^2\); these general tests do not by themselves produce the four alternating real feature families or the finite-fibre Vandermonde proof here. Buhmann and Jäger's 2022 Fourier-analysis article gives sufficient conditions for convolutional and axially symmetric kernels, including conditions using positive definite full harmonic blocks; its full-block sufficient condition does not apply to rank-one positive blocks in every nonconstant degree. Guella and Jäger's 2022 preprint (published online in November 2023) gives the general finite-atomic characterization and an asymptotic sufficient condition for positive coefficient supports; its displayed quantitative support condition controls omitted coefficients and does not directly establish this one-active-mode construction.

This example identifies a particularly sparse explicit support satisfying the general finite-atomic criterion, not a new criterion replacing those general theorems. Its one-mode-per-degree real structure is stronger than a two-mode-per-degree complex kernel construction, but neither that comparison nor the searches made here constitute a universal historical priority proof.

## Limitations

The theorem is specific to \(S^2\), gives no uniform lower Gram-eigenvalue bound over clustered configurations, and cannot be truncated at finite degree while retaining arbitrary-size strict positivity. A positive operator rank of one per represented degree is the smallest **nonzero** per-degree rank; this does not claim that every strictly positive definite kernel must represent every degree. It is explicitly non-characteristic and non-universal. Historical novelty relative to all possible older sparse non-isotropic constructions remains provisional pending independent literature assessment.

## References

1. J. Jäger, *Strictly positive definite kernels on the 2-sphere: beyond radial symmetry*, arXiv:2005.02798, first posted 6 May 2020. https://arxiv.org/abs/2005.02798
2. M. Buhmann and J. Jäger, *Strict Positive Definiteness of Convolutional and Axially Symmetric Kernels on d-Dimensional Spheres*, Journal of Fourier Analysis and Applications 28, 40 (2022). https://doi.org/10.1007/s00041-022-09913-x
3. J. C. Guella and J. Jäger, *Strictly positive definite non-isotropic kernels on two-point homogeneous manifolds: the asymptotic approach*, arXiv:2205.07396 (15 May 2022); Positivity 28, 4 (2024). https://arxiv.org/abs/2205.07396
