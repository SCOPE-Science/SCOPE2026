# Boundary-orbit aliasing and spectral bulk for polynomial power-map Volterra companions

## Finding

Fix an integer \(k\ge2\), a nonzero polynomial \(g(z)=\sum_{\ell=0}^{d}a_\ell z^\ell\), and \(\alpha>-1\). On the normalized analytic weighted Bergman space \(A^2_\alpha(\mathbb D)\), define the generalized Volterra companion
\[
(\mathcal C_{g,k}f)(z)=\int_0^1 (Rf)((tz)^k)g(tz)\,\frac{dt}{t},\qquad (Rf)(w)=wf'(w).
\]
The endpoint \(\alpha=-1\) means the Hardy space \(H^2\), *not* a degenerate weighted-area measure. Write the unique residue decomposition
\[
g(z)=\sum_{r=0}^{k-1}z^r g_r(z^k),\qquad g_r(w)=\sum_{j\ge0}a_{kj+r}w^j,
\]
and let \(F_k(e^{it})=\sum_{r=0}^{k-1}|g_r(e^{it})|^2\). Equivalently,
\[
F_k(e^{it})=\frac1k\sum_{r=0}^{k-1}\left|g\left(e^{i(t+2\pi r)/k}\right)\right|^2.
\]
Let \(\mathsf T_{F_k}\) denote the Hardy Toeplitz matrix with symbol \(F_k\), transported to \(A_\alpha^2\) through the normalized-monomial coefficient basis. This is explicitly **not** the usual weighted-area Bergman Toeplitz compression. Then
\[
\boxed{\mathcal C_{g,k}^{*}\mathcal C_{g,k}\equiv k^{-(\alpha+3)}\mathsf T_{F_k}\pmod{\mathcal K},}
\]
with the same formula at \(\alpha=-1\), where the scalar is \(k^{-2}\). Consequently
\[
\boxed{\sigma_{\rm ess}(\mathcal C_{g,k}^{*}\mathcal C_{g,k})=k^{-(\alpha+3)}[\min_{\mathbb T}F_k,\max_{\mathbb T}F_k],\quad
\|\mathcal C_{g,k}\|_{\rm e}=k^{-(\alpha+3)/2}\sqrt{\max_{\mathbb T}F_k}.}
\]
The kernel is precisely the constant functions. The range is closed **if and only if** \(\min_{\mathbb T}F_k>0\), or equivalently **no full boundary preimage orbit is a zero set of \(g\)**: there is no \(\omega\in\mathbb T\) such that \(z^k-\omega\) divides \(g(z)\). For every \(k\ge2\), this operator is not Fredholm, including in the closed-range case.

There is also an exact normalized finite-section spectral bulk law. Let \(P_N\) project onto the first \(N\) normalized monomials, and list the \(N\) eigenvalues of \(P_N\mathcal C_{g,k}^{*}\mathcal C_{g,k}P_N\) as \(\lambda_{j,N}\), with multiplicity. For every continuous real function \(\Phi\) on a compact interval containing these spectra,
\[
\boxed{\lim_{N\to\infty}\frac1N\sum_{j=1}^{N}\Phi(\lambda_{j,N})=\frac1{2\pi}\int_0^{2\pi}\Phi(k^{-(\alpha+3)}F_k(e^{it}))\,dt.}
\]
The same holds for complex-valued continuous \(\Phi\), by real and imaginary parts.

## Assumptions and scope

The area normalization is \(dA_\alpha(z)=(\alpha+1)(1-|z|^2)^\alpha\,dA(z)/\pi\) for \(\alpha>-1\). The weight parameter \(\alpha\) is fixed when taking essential spectra or finite-section limits. The polynomial \(g\) may have arbitrary complex coefficients and zeros, including inside and on the unit disk, but is not the zero polynomial. The integer \(k\) is fixed and at least two. The Hardy case uses the standard boundary \(L^2\) norm and the conventional orthonormal monomials.

The spectrum \(\sigma_{\rm ess}\) means spectrum in the Calkin algebra, and the essential norm is distance to compact operators. The interval in the theorem is genuine even when \(F_k\) is constant, in which case it is a singleton. The finite-section limit concerns eigenvalues of the *positive Gram operator*, not eigenvalues of the nonnormal companion itself.

## Proof

**Step 1: coefficients and compact approximation.** Set \(e_n(z)=b_{n,\alpha}z^n\), with
\[
b_{n,\alpha}=\left[\frac{\Gamma(n+\alpha+2)}{\Gamma(\alpha+2)\Gamma(n+1)}\right]^{1/2}
\]
for \(\alpha>-1\), and \(b_{n,-1}=1\) for Hardy space. Direct integration gives \(\mathcal C_{g,k}e_0=0\), and for every integer \(n\ge1\),
\[
\mathcal C_{g,k}e_n=\sum_{\ell=0}^{d}a_\ell\frac{n}{kn+\ell}\frac{b_{n,\alpha}}{b_{kn+\ell,\alpha}}\,e_{kn+\ell}.
\]
For any fixed nonnegative \(\ell\), the ratio tends to \(k^{-(\alpha+3)/2}\), by the Gamma-ratio asymptotic and \(n/(kn+\ell)\to 1/k\). The limit is \(1/k\) at the Hardy endpoint. Each fixed monomial channel therefore differs from a constant-weight partial shift by a compact diagonal-weighted shift. If \(S\) is the unilateral shift on \(\ell^2(\mathbb N_0)\), and \(V_ke_n=e_{kn}\), then under the normalized-monomial unitary,
\[
\mathcal C_{g,k}\equiv c\,g(S)V_k\pmod{\mathcal K},\qquad c=k^{-(\alpha+3)/2}.
\]
The constant-input column changes only a finite rank term, so it does not affect this identity. In particular, \(\mathcal C_{g,k}\) is bounded.

**Step 2: exact aliasing Gram identity.** The orthogonal residue ranges of \(S^rV_k\) imply
\[
g(S)V_k=\sum_{r=0}^{k-1}S^rV_k g_r(S),\qquad
(g(S)V_k)^*(g(S)V_k)=\sum_{r=0}^{k-1}g_r(S)^*g_r(S).
\]
For analytic polynomials \(g_r\), multiplication on \(H^2\) gives \(g_r(S)^*g_r(S)=\mathsf T_{|g_r|^2}\) *exactly*, yielding the announced Calkin Gram identity. Expanding the absolute squares and averaging over \(k\)-th roots proves the displayed orbit formula for \(F_k\), since all cross terms with different residues cancel.

**Step 3: essential spectral endpoints and range.** A continuous, real-valued Toeplitz symbol \(F_k\) has Calkin spectrum equal to its boundary range. One direct justification is the product identity modulo compacts, \(\mathsf T_{F}\mathsf T_{H}\equiv\mathsf T_{FH}\), and the asymptotic approximate eigenvectors from the normalized Hardy kernels approaching each boundary point. It follows that the Calkin spectrum of this nonnegative Gram is the interval \(c^2[\min F_k,\max F_k]\), and the essential norm of the companion is the square root of its maximal Gram Calkin spectral value.

Differentiating the defining integral in the radial direction gives \(R(\mathcal C_{g,k}f)(z)=g(z)(Rf)(z^k)\). Since \(g\) is not identically zero, vanishing of \(\mathcal C_{g,k}f\) forces \(Rf\equiv0\), and its kernel is exactly \(\operatorname{span}\{1\}\). An operator with finite-dimensional kernel has closed range exactly when its positive Gram is bounded below on the orthogonal complement of that kernel; this is equivalent to zero being absent from the Gram's essential spectrum when zero is an isolated finite-multiplicity kernel eigenvalue. In the present positive finite-band Toeplitz-plus-compact setting, \(\min F_k>0\) yields a positive Fredholm Gram and hence closed range. Conversely if \(\min F_k=0\), normalized Hardy boundary kernels show a weakly null sequence with vanishing Gram energy; the compact correction vanishes on it, so the range cannot be closed given the finite kernel. Finally, \(F_k(\omega)=0\) holds exactly when every \(g_r(\omega)=0\), equivalent by polynomial division to \(z^k-\omega\mid g(z)\).

For \(k\ge2\), the codimension of the range cannot be finite. Projecting outputs onto the first \(kN\) monomials produces a space of dimension at most \(N+1\), because all inputs of degree at least \(N\) yield outputs of degree at least \(kN\). Its orthogonal complement inside the first \(kN\) monomials therefore has dimension growing at least as \((k-1)N-1\), incompatible with finite-dimensional range cokernel. Thus no such \(\mathcal C_{g,k}\) is Fredholm.

**Step 4: finite-section spectral distribution.** The polynomial \(F_k\) is a trigonometric polynomial, so the Toeplitz matrix \(\mathsf T_{F_k}\) has finite bandwidth. For each fixed positive integer \(m\), all but a uniformly bounded number of the diagonal entries of \((P_N\mathsf T_{F_k}P_N)^m\) equal the zero Fourier coefficient of \(F_k^m\). Hence its trace divided by \(N\) converges to \((2\pi)^{-1}\int F_k^m\). Compact perturbations do not change normalized traces of continuous functions of uniformly bounded selfadjoint finite sections: first establish this for finite-rank perturbations, then uniformly approximate an arbitrary compact perturbation in norm. Polynomial approximation on the common spectral interval extends the moment limit to arbitrary continuous \(\Phi\). Applying this to \(c^2\mathsf T_{F_k}\) proves the claimed bulk law.

## Verification

The independent finite-checking script `check.py` runs using only the Python standard library. It reported `POLYNOMIAL_ALIAS_COMPANION_FINITE_CHECK_OK 2368`. It checks the cyclic root average, high-index Gram coefficients against the Toeplitz symbol for several \(k\) and \(\alpha\), exact rational norms for monomial symbols on unweighted Bergman space, and two contrasting boundary-orbit cases. It tests finite-section moments for one example. These checks are supplementary and do not replace the infinite-dimensional proof above.

For example, at \(k=2,\alpha=0\), choosing \(g(z)=1-z\) gives \(F_2\equiv2\), essential Gram spectrum \(\{1/4\}\), closed range, and essential norm \(1/2\) despite the unit-circle zero of \(g\). In contrast, \(g(z)=1-z^2\) gives \(F_2(e^{it})=|1-e^{it}|^2\), essential Gram spectrum \([0,1/2]\) and nonclosed range. This distinction is precisely the full-fiber zero condition, not merely the presence of an individual boundary zero.

## Relationship to prior work

Dong and Xu's 2026 work gives general Carleson-measure, compactness, essential-norm, and Schatten criteria for generalized Volterra companions on finite-type convex domains. The present specialized calculation concerns an exact Calkin *positive Gram* model, an exhaustive closed-range/root-orbit classification, and a finite-section eigenvalue law for polynomial symbols and monomial composition. Classical Toeplitz symbol calculus, root-of-unity filters, and the Szegő distribution method are used and are not themselves new.

The two-channel antipodal essential-norm formula already known for Bergman slant Toeplitz operators covers a closely related \(k=2\) adjoint-model norm question. Accordingly the \(k=2\) norm calculation alone is **not** claimed as independent novelty. Existing work on slant Toeplitz spectra and commutators addresses different operators or their ordinary (nonnormal) spectra. General weighted-composition essential-norm estimates also provide context, without visibly giving the joint closed-range and spectral-bulk assertions here. Published formulations that implicitly contain this special case remain a residual originality risk.

## Limitations

Only polynomial symbols, integer power composition maps, and fixed weighted Hilbert Bergman/Hardy scales are covered. No uniformity as \(k\), \(\deg g\), or \(\alpha\) varies is asserted. The theorem does not classify the spectrum or point spectrum of the nonnormal operator \(\mathcal C_{g,k}\), and it does not compute singular-value edge fluctuations or finite-section convergence rates. The finite checker cannot certify compactness, essential spectra, the full spectral distribution, or an unbounded-degree limit. No independent validation has been performed. A broader weighted-composition or slant-operator theorem might subsume the combined claim; the literature comparison is made with that explicit risk.

## References

1. Jianxiang Dong and Chunxu Xu, *Generalized Volterra Companion Operators on Bergman Spaces over Convex Domains of Finite Type*, arXiv:2609.27584, first publicly posted 2026-09-23. https://arxiv.org/abs/2609.27584
2. Oinam Nilbir Singh, M. P. Singh, and Thokchom Sonamani Singh, *Algebraic and Spectral Properties of Slant Toeplitz and Slant Little Hankel Operators on Weighted Bergman Space*, arXiv:2507.06546, 2025. https://arxiv.org/html/2507.06546v1
3. Z. Čučković and R. Zhao, *Weighted Composition Operators on the Bergman Space*, J. London Math. Soc. 70 (2004), 499–511. https://doi.org/10.1112/S0024610704005605
4. *Exact antipodal boundary formula for the essential norm of Bergman slant Toeplitz operators*, 2026, available public summary: https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-exact-antipodal-boundary-formula-for-the-essential-norm-of-bergm--f7f6a1e74df8
5. Classical Toeplitz essential-symbol calculus and the first Szegő limit theorem; only their elementary finite-band forms are used in the proof above.
