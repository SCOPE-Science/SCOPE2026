# Kalman-graded Schatten blow-up and sharp rank bounds for inverse Gaussian semigroups

## Finding

Let \(d\ge3\), let \(B\) be a real \(d\times d\) matrix, and let \(Q=-(B+B^{\mathsf T})\) be positive semidefinite. On \(L^2(\mathbb R^d,e^{|x|^2/2}dx)\), take the closed generator \(A=\frac12\operatorname{tr}(Q\nabla^2)-\langle Bx,\nabla\rangle\) specified by Gaussian conjugation (below), and write \(H_t=e^{tA}\). Set \(V_k=\sum_{j=0}^{k}(B^{\mathsf T})^j\operatorname{Ran}Q^{1/2}\), \(V_{-1}=\{0\}\), and \(m_k=\dim V_k-\dim V_{k-1}\). Then \(H_t\) belongs to every Schatten class \(\mathcal S_p\), \(0<p<\infty\), at one (equivalently every) positive time exactly when \(V_{d-1}=\mathbb R^d\). Otherwise no \(H_t\), \(t>0\), is compact.

In the full-rank case, put \(K=\sum_{k\ge0}(2k+1)m_k\). For \(L_k=V_k\ominus V_{k-1}\), choose orthonormal bases, and let \(P_k\) be the orthogonal projection onto \(L_k\). Define \(C_k=\frac1{k!}P_k(B^{\mathsf T})^kQ^{1/2}\), viewed as an \(m_k\)-by-\(d\) matrix, and form the positive definite block matrix \(G\) with blocks \(G_{k\ell}=C_kC_\ell^{\mathsf T}/(k+\ell+1)\). For each fixed \(p>0\),

\[
\boxed{\lim_{t\downarrow0}t^{K}\|H_t\|_{\mathcal S_p}^{p}=\frac{(2/p)^d}{\det G}.}
\]

If \(r=\operatorname{rank}Q\), the exponent satisfies the **sharp rank-dependent bounds**

\[
\boxed{d\le K\le (d-r+1)^2+r-1.}
\]

Both bounds are attained within this class whenever the prescribed rank permits them (for fixed \(r<d\), the lower bound is generally not attainable: its equality requires \(r=d\)). The upper bound is attained for every \(1\le r\le d\) by an explicit dissipative skew-chain model below, with a fully evaluated factorial constant. For that model, the operator trace grows only as \(t^{-d}\), while its trace norm grows as \(t^{-[(d-r+1)^2+r-1]}\); in particular, rank-one diffusion produces a sharp \(t^{-d^2}\) nuclear-norm blow-up despite a \(t^{-d}\) trace.

## Assumptions and scope

All Hilbert spaces are complexified where necessary. The probability Gaussian measure is \(d\gamma(x)=(2\pi)^{-d/2}e^{-|x|^2/2}dx\). Put \(d\nu(x)=e^{|x|^2/2}dx\). The isometry \(Uf=(2\pi)^{-d/4}e^{-|x|^2/2}f\) maps \(L^2(\gamma)\) onto \(L^2(\nu)\). Let \(P_t\) denote the Gaussian Markov Ornstein–Uhlenbeck semigroup with drift \(B\) and covariance \(Q\), preserving \(\gamma\). Define, without any nondegeneracy assumption, \(H_t=e^{t\operatorname{tr}B}U P_t^*U^{-1}\); its generator agrees with \(A\) on smooth compactly supported functions, and this identity specifies its closed realization. \(\mathcal S_p\) means the usual singular-value quasi-ideal when \(0<p<1\).

The appearance of an inverse Gaussian generator here does not require an invariant probability law for the inverse semigroup. The unweighted classical diffusion coefficient may be degenerate. For an arbitrary stationary positive-definite covariance, whitening reduces the operator unitarily to the stated normalization. The theorem concerns the Hilbert-space \(L^2\) realization; no claim is made for other underlying \(L^q\) spaces.

## Proof

**(1) Exact singular-value product and compactness.** On the first Wiener chaos of \(L^2(\gamma)\), \(P_t\) acts by \(e^{tB^{\mathsf T}}\). On the \(j\)-th chaos it acts by its \(j\)-fold symmetric tensor power. Thus \(P_t\) is the bosonic second quantization of \(e^{tB^{\mathsf T}}\). If \(\sigma_1(t),\ldots,\sigma_d(t)\) are the singular values of \(e^{tB}\), the exact known second-quantization formula gives

\[
\|H_t\|_{\mathcal S_p}^{p}
=e^{pt\operatorname{tr}B}\prod_{i=1}^{d}(1-\sigma_i(t)^p)^{-1}
\]

when all singular values are strictly below one. It also gives \(\operatorname{Tr}H_t=e^{t\operatorname{tr}B}/\det(I-e^{tB})\) in this case. If any singular value equals one, all its tensor powers have norm one on pairwise orthogonal chaos levels, so \(H_t\) is not compact.

Differentiating the first-chaos Gram matrix yields

\[
W_t:=I-e^{tB^{\mathsf T}}e^{tB}=\int_0^t e^{sB^{\mathsf T}}Qe^{sB}\,ds\ge0.
\]

For any vector \(v\), \(v^{\mathsf T}W_tv=\int_0^t\|Q^{1/2}e^{sB}v\|^2ds\). This vanishes iff \(Q^{1/2}B^jv=0\) for every nonnegative integer \(j\), equivalently \(v\perp V_{d-1}\). Thus \(\|e^{tB}\|<1\) for every \(t>0\) exactly when the stated Kalman flag is full; otherwise its largest singular value is one for every \(t>0\). This proves both sides of the compactness/Schatten dichotomy. Full rank also forces \(B\) to be Hurwitz: a nondecaying eigenvector would contradict strict norm contraction at each positive time.

**(2) Graded Gramian determinant.** Work in the orthogonal decomposition \(\mathbb R^d=\bigoplus_{k=0}^{\kappa}L_k\). Terms of order less than \(k\) vanish under projection of \(e^{sB^{\mathsf T}}Q^{1/2}\) to \(L_k\), and its first nonzero coefficient is \(s^k C_k\). Each \(C_k\) has full row rank by the definition of \(V_k\). Let \(D_t\) be block diagonal, equal to \(t^{k+1/2}I\) on \(L_k\). Substituting \(s=tu\) into the Gramian integral gives the entrywise and operator-norm limit

\[
D_t^{-1}W_tD_t^{-1}\longrightarrow G,
\qquad G_{k\ell}=\int_0^1u^{k+\ell}C_kC_\ell^{\mathsf T}du.
\]

The matrix \(G\) is positive definite: if its quadratic form vanishes on \((v_k)\), the vector-valued polynomial \(\sum_k u^k C_k^{\mathsf T}v_k\) vanishes identically, and the full row rank of each \(C_k\) forces every \(v_k=0\). Taking determinants yields

\[
\det W_t=(\det G)t^{\sum_k(2k+1)m_k}(1+o(1)).
\]

As \(t\downarrow0\), every \(\sigma_i(t)\to1\), and \((1-\sigma_i^p)/(1-\sigma_i^2)\to p/2\). Hence \(\prod_i(1-\sigma_i^p)=(p/2)^d\det W_t(1+o(1))\). The second-quantization product and \(e^{pt\operatorname{tr}B}\to1\) prove the boxed limit for every \(p>0\).

**(3) Sharp rank bound.** Put \(r=m_0\). Until the full flag is attained, its dimension strictly increases, and the increments \(m_k\) are nonincreasing, since \(B^{\mathsf T}\) induces surjections \(V_k/V_{k-1}\to V_{k+1}/V_k\). Thus \(K\ge\sum_k m_k=d\), with equality exactly when \(m_0=d\). For fixed \(r\), the latest possible allocation of the \(d-r\) dimensions not already present in \(V_0\) is one new dimension at each of levels \(1,2,\ldots,d-r\). Rearranging the positive weights \(2k+1\) therefore gives

\[
K\le r+\sum_{k=1}^{d-r}(2k+1)=(d-r+1)^2+r-1.
\]

**(4) Attainment and exact factorial coefficient.** For \(m=d-r+1\), set \(J_m=-E_{11}+\sum_{j=1}^{m-1}(E_{j+1,j}-E_{j,j+1})\) and \(B=J_m\oplus(-I_{r-1})\). Then \(Q=-(B+B^{\mathsf T})=2E_{11}\oplus 2I_{r-1}\) has rank \(r\). The chain has one new direction at each level from zero to \(m-1\), and every decoupled scalar adds a level-zero direction; hence \(K=m^2+r-1\). The skew chain is stable because its sole damping coordinate cyclically controls every coordinate; alternatively, the strictly contractive first chaos established in step (1) proves stability. \(\det(-B)=1\), by the tridiagonal determinant recurrence.

For the chain part, choose successive coordinate axes as graded bases. Its first nonzero coefficient at level \(k\) is \(\sqrt2(-1)^k/k!\) in the single noise column. Its graded limit matrix therefore is the signed diagonally rescaled Hilbert matrix with entries \(G_{k\ell}=2(-1)^{k+\ell}/[k!\ell!(k+\ell+1)]\). Cauchy's determinant formula gives

\[
\det G=\frac{2^{m}}{\prod_{k=0}^{m-1}(k!)^2}\prod_{k=0}^{m-1}\frac{(k!)^4}{(2k)!(2k+1)!}.
\]

Each of the \(r-1\) independent scalar directions contributes \((pt)^{-1}(1+o(1))\). Consequently, for **every** \(1\le r\le d\) and \(p>0\), this explicit rank-\(r\) example obeys

\[
\boxed{\lim_{t\downarrow0}t^{m^2+r-1}\|H_t\|_{\mathcal S_p}^{p}
=p^{-d}\prod_{k=0}^{m-1}\frac{(2k)!(2k+1)!}{(k!)^2},\quad m=d-r+1.}
\]

Its operator trace has \(\operatorname{Tr}H_t=e^{t\operatorname{tr}B}/\det(I-e^{tB})\sim t^{-d}\), because \(\det(-B)=1\). For rank one in dimension three this supplies the explicit contrast \(\|H_t\|_{\mathcal S_1}\sim8640\,t^{-9}\) and \(\operatorname{Tr}H_t\sim t^{-3}\).

## Verification

The general proof is analytic and applies to all dimensions and all positive Schatten exponents. As independent finite checks, the standalone `CHECK.py` performs exact-rational determinant comparisons through chain length eight. The degree-three rank-one chain \(B=\begin{psmallmatrix}-1&-1&0\\1&0&-1\\0&1&0\end{psmallmatrix}\) has \(Q=\operatorname{diag}(2,0,0)\), graded matrix \(G=\begin{psmallmatrix}2&-1&1/3\\-1&2/3&-1/4\\1/3&-1/4&1/10\end{psmallmatrix}\), and exact determinant \(1/1080\). Hence the \(p=1\) coefficient is \(8\cdot1080=8640\). High-precision independent numerical evaluation of the covariance integral and Gaussian singular values at \(t=0.2,0.08,0.03\) converges toward the predicted limits. Those checks do not substitute for the determinant and chaos proofs.

## Relationship to prior work

Bruno, Casarino, Ciatti and Sjögren (2026) establish inverse-Gaussian operator conjugation and the spectral structure, assuming a strictly positive diffusion matrix; their first-public preprint date is 4 November 2026, and primary MSC is 47A10. Araki, Sinha and Sunder (1995) prove the general second-quantization Schatten ideal criteria and product formulas used as inputs here. Classical Kalman controllability gives positive finite-time Gramians, and standard controllability-index arguments identify the filtration. None of those ingredients is claimed as new.

The contribution assessed here is the **dimension-at-least-three graded Schatten exponent and positive exact coefficient**, the sharp bound at fixed diffusion rank, and an all-dimension extremal chain with explicit factorial coefficient and growing trace/nuclear-norm separation. Earlier planar inverse-Gaussian calculations already provide nonnormal Schatten formulas and two-dimensional ellipticity-edge behavior; neither the planar formula nor its crossover is asserted as new here. Searches and material comparisons did not establish a covering result for the full graded rank-bound theorem, but an unlocated equivalent in older control/second-quantization literature remains possible.

## Limitations

The conclusions are for quadratic Ornstein–Uhlenbeck generators with standard invariant Gaussian covariance and the specified inverse Gaussian \(L^2\) realization, including degenerate diffusion. Only leading small-time Schatten coefficients are determined, not full higher-order expansions or resolvent Schatten norms. Positive-time all-Schatten membership requires full Kalman rank. No claim is made about endpoint \(p=\infty\), infinite-dimensional state spaces, or non-Gaussian perturbations. The model proof uses known general Fock-space formulas and known control-system machinery; independent literature auditing has not occurred.

## References

- T. Bruno, V. Casarino, P. Ciatti, P. Sjögren, *Spectral and mapping properties of the inverse Ornstein–Uhlenbeck operator*, arXiv:2611.06826v1, first submitted 2026-11-04, Sections 2–4.
- H. Araki, K. B. Sinha, V. S. Sunder, *On Boundedness and \(\|\cdot\|_p\) Continuity of Second Quantisation*, Publ. Res. Inst. Math. Sci. **31** (1995), 941–952, doi:10.2977/PRIMS/1195163724.
- M. Hitrik, K. Pravda-Starov, J. Viola, *Short-time asymptotics of the regularizing effect for semigroups generated by quadratic operators*, arXiv:1510.01992 (2015).
- P. Alphonse and J. Martin, *Approximate null-controllability with uniform cost for the hypoelliptic Ornstein–Uhlenbeck equations*, SIAM J. Control Optim. **61** (2023), 1679–1711, doi:10.1137/22M1487412.
