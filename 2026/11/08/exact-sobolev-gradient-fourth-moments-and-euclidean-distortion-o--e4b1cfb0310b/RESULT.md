# Exact Sobolev gradient fourth moments and Euclidean distortion of quadratic spherical harmonics

## Finding
For each integer \(n\geq2\), consider the real space \(V_n\) of symmetric traceless \(n\times n\) matrices. For \(A\in V_n\), write \(h_A(\omega)=\omega^{\mathsf T}A\omega\) on \(\mathbb S^{n-1}\), let \(\sigma\) be normalized spherical probability, and equip \(V_n\) with the norm
\[
 N_n(A)=\left(\int_{\mathbb S^{n-1}}|\nabla_{\!S}h_A(\omega)|^4\,d\sigma(\omega)\right)^{1/4}.
\]
For \(A\ne0\), put \(\rho(A)=\operatorname{tr}(A^4)/\operatorname{tr}(A^2)^2\) and
\[
 K_n(A)=\frac{\int|\nabla_{\!S}h_A|^4\,d\sigma}{\bigl(\int|\nabla_{\!S}h_A|^2\,d\sigma\bigr)^2}.
\]
The exact identity is
\[
 \boxed{K_n(A)=\frac{(n+2)[n^2+6n+12+2n(n+2)\rho(A)]}{n(n+4)(n+6)}.}
\]
Its **complete sharp range** is \(K_{n,\min}\leq K_n(A)\leq K_{n,\max}\), where
\[
 \boxed{K_{n,\max}=\frac{3n(n+1)(n+2)}{(n-1)(n+4)(n+6)}}
\]
and
\[
 \boxed{K_{n,\min}=\begin{cases}
 \dfrac{(n+2)(n+4)}{n(n+6)},&n\text{ even},\\[4pt]
 \dfrac{n(n+2)(n+3)(n+5)}{(n-1)(n+1)(n+4)(n+6)},&n\text{ odd}.
 \end{cases}}
\]
Every intermediate value is attained. For \(n=2,3\), both endpoints coincide and every nonzero \(A\) is extremal. For \(n\ge4\), upper equality holds precisely when \(A\) has two eigenvalues of multiplicities \(1\) and \(n-1\). Lower equality holds precisely when its two eigenvalue multiplicities are \(\lfloor n/2\rfloor\) and \(\lceil n/2\rceil\). Values are always counted with multiplicity; orthogonal conjugation and nonzero scalar multiplication preserve equality.

Let \(d_{\mathrm{BM}}\) denote real Banach--Mazur distance and let \(d_n=n(n+1)/2-1\). The **exact Euclidean distortion** of this gradient norm is
\[
 \boxed{d_{\mathrm{BM}}\big((V_n,N_n),\ell_2^{d_n}(\mathbb R)\big)^4
 =\begin{cases}
 \dfrac{3n^2(n+1)}{(n-1)(n+4)^2},&n\text{ even},\\[4pt]
 \dfrac{3(n+1)^2}{(n+3)(n+5)},&n\text{ odd}.
 \end{cases}}
\]
In particular, this nonlinear spherical Sobolev gradient norm is Hilbertian exactly for \(n=2,3\); in dimension four its fourth-power distortion is \(5/4\), and the distortion converges to \(3^{1/4}\) as \(n\to\infty\). The optimal comparison Hilbert norm is the Hilbert--Schmidt norm, up to positive scaling.

The exact endpoint deficits are
\[
 K_{n,\max}-K_n(A)=\frac{2(n+2)^2}{(n+4)(n+6)}\bigl(\rho_{n,\max}-\rho(A)\bigr),\qquad
 K_n(A)-K_{n,\min}=\frac{2(n+2)^2}{(n+4)(n+6)}\bigl(\rho(A)-\rho_{n,\min}\bigr),
\]
where \(\rho_{n,\max}=\frac{n^2-3n+3}{n(n-1)}\), and \(\rho_{n,\min}=1/n\) for even \(n\), respectively \((n^2+3)/[n(n^2-1)]\) for odd \(n\). These nonnegative identities encode spectral rigidity at each endpoint (they are not claimed to be metric-distance stability bounds).

## Assumptions and scope
All matrices, spherical harmonics and norms are real. Ambient dimension is any integer \(n\ge2\); the surface measure \(\sigma\) has total mass one. The gradient is tangential for the standard unit round metric. The coefficient space has precisely dimension \(d_n\), since \(A\mapsto h_A\) is injective on tracefree symmetric matrices. The pointwise gradient is \(2(A\omega-h_A(\omega)\omega)\). The map \(A\mapsto\nabla_{\!S}h_A\) is linear and injective, hence \(N_n\) is indeed a norm. No statement concerns complex matrices or higher-degree harmonic spaces.

## Proof
**Spherical moment reduction.** Abbreviate \(q=\omega^{\mathsf T}A\omega\), \(s=\omega^{\mathsf T}A^2\omega\), \(T_2=\operatorname{tr}(A^2)>0\), and \(T_4=\operatorname{tr}(A^4)\). The tangential projection of the Euclidean gradient gives
\[
 |\nabla_{\!S}h_A|^2=4(s-q^2).
\]
For uniform \(\omega\), Gaussian radial separation or direct coordinate integration gives
\[
 \begin{aligned}
 \mathbb E s^2&=\frac{T_2^2+2T_4}{n(n+2)},\\
 \mathbb E(sq^2)&=\frac{2T_2^2+8T_4}{n(n+2)(n+4)},\\
 \mathbb E q^4&=\frac{12T_2^2+48T_4}{n(n+2)(n+4)(n+6)}.
 \end{aligned}
\]
These follow by evaluating the second and fourth Gaussian quadratic-form moments and dividing by the radial moments \(\mathbb E\|G\|^{2j}=n(n+2)\cdots(n+2j-2)\). Also \(\mathbb E s=T_2/n\) and \(\mathbb E q^2=2T_2/[n(n+2)]\). Therefore
\[
 \boxed{\mathbb E|\nabla_{\!S}h_A|^2=\frac{4T_2}{n+2}},\qquad
 \boxed{\mathbb E|\nabla_{\!S}h_A|^4=\frac{16[(n^2+6n+12)T_2^2+2n(n+2)T_4]}{n(n+2)(n+4)(n+6)}}.
\]
Dividing gives the stated formula for \(K_n(A)\), which is strictly increasing in \(\rho(A)\).

**Complete spectral endpoints, with proof.** Let \(\lambda_1,\ldots,\lambda_n\in\mathbb R\) be the eigenvalues and normalize \(\sum_i\lambda_i=0\), \(\sum_i\lambda_i^2=1\). The ratio \(\rho(A)\) is \(F=\sum_i\lambda_i^4\), a continuous function on a compact smooth sphere. For \(n=2\), the eigenvalues are opposite and \(F=1/2\). For \(n=3\), Newton's identities imply \(\sum_i\lambda_i^4=(\sum_i\lambda_i^2)^2/2\), so \(F=1/2\) identically.

For \(n\ge4\), at any local extremum, independent gradients of the two constraints give multipliers. Multiplying the stationary equations \(4\lambda_i^3=\alpha+2\beta\lambda_i\) by \(\lambda_i\) and summing yields \(\beta=2F\). Thus every eigenvalue is a root of the depressed cubic \(x^3-Fx-\alpha/4=0\). Suppose there are three distinct roots \(a,b,c\); they satisfy \(a+b+c=0\), \(F=a^2+ab+b^2\). As \(n\ge4\), some root, say \(a\), has multiplicity at least two. On four coordinates with eigenvalues \((a,a,b,c)\), consider tangent vectors
\[
 v=(1,-1,0,0),\qquad w=(0,b-c,c-a,a-b).
\]
Both have coordinate sum zero and are orthogonal to the eigenvalue vector. The constrained Lagrangian Hessian divided by four is diagonal with entries \(3\lambda_i^2-F\). Direct expansion gives \(\langle w,Hw\rangle=0\) and \(\langle v,Hw\rangle=-(3a^2-F)(b-c)\ne0\), because the three roots are simple. Hence its restriction to the two-dimensional tangent span is indefinite, contradicting either the minimum or maximum second-order condition. Every extremizer for \(n\ge4\) therefore has at most two distinct eigenvalues.

If the two eigenvalues have multiplicities \(k\) and \(n-k\), the zero-sum and unit-variance constraints give
\[
 F=\frac{n}{k(n-k)}-\frac3n,\qquad1\le k\le n-1.
\]
The largest value has \(k=1\) or \(n-1\); the smallest has \(k\) nearest \(n/2\). Thus the sharp spectral endpoints are exactly the values \(\rho_{n,\max}\) and \(\rho_{n,\min}\) above, with all equality cases. Substitution into \(K_n(A)\) simplifies to the claimed parity-dependent rational constants. The real unit sphere in \(V_n\) is connected, so every intermediate ratio is attained by continuity.

**Optimality of the Euclidean comparison.** For every orthogonal \(U\), the gradient norm is invariant under \(A\mapsto UAU^{\mathsf T}\). The representation of \(O(n)\) on \(V_n\) is real irreducible: diagonal traceless coordinates carry the standard permutation representation, individual off-diagonal coordinates are separated by sign changes, and plane rotations connect \(\operatorname{diag}(1,-1,0,\ldots)\) to the corresponding symmetric off-diagonal matrix. Consequently every invariant positive quadratic form is a scalar multiple of \(\operatorname{tr}(A^2)\). Given any candidate Euclidean quadratic form \(Q\) and comparison \(Q(A)\le N_n(A)^2\le D^2Q(A)\), average the inequalities and the form over \(O(n)\) to get the same comparison with an invariant form. Therefore the Hilbert--Schmidt comparator is optimal and
\[
 d_{\mathrm{BM}}^4=\frac{\max_{A\ne0}N_n(A)^4/T_2^2}{\min_{A\ne0}N_n(A)^4/T_2^2}
 =\frac{K_{n,\max}}{K_{n,\min}}.
\]
Simplification gives the two asserted formulas, including the low-dimensional Hilbertian cases and the limit.

## Verification
A standalone exact-arithmetic checker is supplied as `VERIFY.py`. It tests the symbolic Gaussian-to-sphere coefficient identity; independently integrates ten diagonal test cases with rational spherical monomial moments in dimensions two through six; checks both spectral endpoint formulas for every integer dimension from two through 100; and verifies the three-root Lagrange Hessian identity. Execute with `python VERIFY.py` (requires SymPy). All indicated checks passed at preparation. The all-dimension conclusions rest on the preceding analytical argument, not on bounded numerical experiments.

## Relationship to prior work
The literature on scalar \(L^4\) spherical harmonics motivates norm and extremizer questions but does not determine this vector-valued **tangential-gradient norm**. Sogge and Zelditch (arXiv:1011.0215v1, October 31, 2010) study \(L^4\) eigenfunction norms and basis averages, not exact gradient-norm distortion. Dai, Feng and Tikhonov (arXiv:1408.1877v1, August 6, 2014) establish sharp *asymptotic orders in harmonic degree* for scalar reverse Hölder ratios, not fixed-degree tangential-gradient moment identities. Stanton and Weinstein (1981) study scalar degree-dependent \(L^4\) extremizers.

A publicly available later theorem titled *Sharp L4/L2 norm and extremizers for degree-two spherical harmonics* computes the scalar fourth moment and the same **upper spectral** ratio \(\rho_{n,\max}\). It thus supplies a relevant ingredient for the upper endpoint, but its scalar conclusion does not assert the mixed gradient moment \(\mathbb E(sq^2)\), the sharp odd/even **lower** gradient endpoint or this norm's optimal Euclidean Banach--Mazur distance. This result does not claim that the upper spectral inequality or the scalar theorem is new. As with any exact finite-dimensional norm invariant, an equivalent unpublished or unindexed formulation may exist.

## Limitations
The measure is normalized Haar surface measure on the round sphere. The matrices are real symmetric and traceless and the degree is exactly two. The theorem concerns tangential-gradient \(L^4/L^2\) and the induced real Banach-space norm, not scalar \(L^4/L^2\) ratios, complex matrix coefficients, arbitrary Riemannian manifolds, higher degrees, higher moments, or metric-distance stability estimates. The finite checker is not an exhaustive proof.

## References
1. C. D. Sogge and S. Zelditch, *Concerning the L4 norms of typical eigenfunctions on compact surfaces*, arXiv:1011.0215v1, publicly posted 2010-10-31. https://arxiv.org/abs/1011.0215
2. F. Dai, H. Feng and S. Tikhonov, *Reverse Hölder's inequality for spherical harmonics*, arXiv:1408.1877v1, publicly posted 2014-08-06. https://arxiv.org/abs/1408.1877
3. R. J. Stanton and A. Weinstein, *On the L4 norm of spherical harmonics*, Math. Proc. Cambridge Philos. Soc. 89 (1981), 343–358. https://doi.org/10.1017/S0305004100058229
4. *Sharp L4/L2 norm and extremizers for degree-two spherical harmonics*, publicly available online theorem (2026), scientific record identifier `d4106097159f`.
