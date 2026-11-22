# Infinite signed spectra in symmetric ratio-type copula chains

## Finding

Consider the symmetric ratio-type copula
\[
C_\theta(u,v)=\frac{uv}{1-\theta f(u)f(v)},\qquad 0\le u,v\le1.
\]
Let \(f\in C^1([0,1])\) be strictly monotone, with \(f(1)=0\) and \(f(0)\ne0\). Assume that \(C_\theta\) is a copula and its denominator is strictly positive on the closed unit square. Let \(P_\theta\) be the stationary one-step Markov operator on the centered real space \(L_0^2([0,1])\), induced by the density \(c_\theta=\partial_u\partial_v C_\theta\).

**Spectral signature theorem.** All three regimes are exact:

1. For \(\theta>0\), \(P_\theta\) is positive semidefinite, trace-class, and has infinitely many strictly positive eigenvalues and no negative eigenvalues. For every centered \(h\in L^2\), the lag covariance \(\gamma_n(h)=\operatorname{Cov}(h(X_0),h(X_n))\) is a completely monotone sequence:
   \[
   (-1)^k\Delta^k\gamma_n(h)\ge0\qquad(n,k\in\mathbb N_0),
   \]
   with \(\Delta\gamma_n=\gamma_{n+1}-\gamma_n\).
2. At \(\theta=0\), \(P_0=0\) on \(L_0^2\): consecutive states are independent.
3. For \(\theta<0\), \(P_\theta\) is compact and has **infinitely many strictly positive and infinitely many strictly negative eigenvalues**, although \(C_\theta\) is negatively quadrant dependent. More precisely, for every integer \(m\ge1\) and every set of distinct \(u_1,\ldots,u_m\in(0,1)\), the symmetric matrix
   \[
   H_m=\big[C_\theta(u_i,u_j)-u_i u_j\big]_{i,j=1}^m
   \]
   has exactly \(\lfloor m/2\rfloor\) positive eigenvalues, \(\lceil m/2\rceil\) negative eigenvalues and no zero eigenvalues. Consequently there are centered square-integrable observables with strictly positive lag-one covariance and others whose nonzero-lag covariances have signs \((-1)^n\) for every integer \(n\ge1\).

**Concrete 2024 instance.** El Ktaibi, Bentoumi and Mesfioui introduced \(f(u)=(1-u)e^{-u}\) as copula \(D^{(7)}\), with admissible \(-e^2\le\theta\le1\). The theorem covers its full negative interval \([-e^2,0)\) and its positive interval \((0,1)\). The singular-denominator endpoint \(\theta=1\) is excluded from the present spectral assertions.

## Assumptions and scope

The denominator hypothesis means \(1-\theta f(u)f(v)>0\) for every \((u,v)\in[0,1]^2\). This is automatic for negative \(\theta\), because strict monotonicity and \(f(1)=0\) imply that \(f\) has one sign on \([0,1)\). For positive \(\theta\), it is equivalent to \(\theta f(0)^2<1\). The copula admissibility requirement is separate; no claim is made that arbitrary values of \(\theta\) define copulas.

The Markov chain \((X_n)_{n\ge0}\) has stationary uniform marginal, and \(\Pr(X_{n+1}\in dv\mid X_n=u)=c_\theta(u,v)\,dv\). The density is continuous and symmetric under the stated hypotheses; therefore its Markov operator is a compact self-adjoint contraction on \(L^2\), preserving \(L_0^2\). Inertia counts above use the order (positive, negative, zero). No assertion of exact eigenvalue magnitudes, eigenfunction formulas, or optimal mixing rates is part of the finding.

## Proof

**1. The covariance bridge.** Put \(K_\theta(u,v)=C_\theta(u,v)-uv\). Algebra gives
\[
K_\theta(u,v)=\frac{\theta\,u f(u)\,v f(v)}{1-\theta f(u)f(v)}.
\tag{1}
\]
For any real \(h\in C^1([0,1])\), integration by parts twice (using uniform marginals and \(K_\theta=0\) on all four boundary edges) yields Hoeffding's covariance identity
\[
\langle h-\bar h,P_\theta(h-\bar h)\rangle
=\int_0^1\!\int_0^1 h'(u)h'(v)K_\theta(u,v)\,du\,dv,
\tag{2}
\]
where \(\bar h=\int_0^1 h(u)\,du\). Every smooth derivative profile is realizable by a centered \(h\), by integrating it and subtracting its mean.

**2. Positive parameter.** If \(0<\theta f(0)^2<1\), the geometric expansion of (1) is uniformly convergent on the square:
\[
K_\theta(u,v)=\sum_{j=1}^{\infty}\theta^j a_j(u)a_j(v),
\qquad a_j(u)=u f(u)^j.
\tag{3}
\]
Since \(f\in C^1\), termwise mixed differentiation is justified by the summable bound
\[
\|a'_j\|_\infty\le M^j+jM^{j-1}\|f'\|_\infty,
\qquad M=|f(0)|,
\]
and the condition \(\theta M^2<1\). Thus
\[
c_\theta(u,v)=1+\sum_{j=1}^{\infty}\theta^j a'_j(u)a'_j(v).
\tag{4}
\]
The centered operator is a norm-convergent sum of positive rank-one operators with summable traces \(\sum_{j\ge1}\theta^j\|a'_j\|_2^2\), proving positivity and trace class. For any distinct interior points \(u_i\), the matrix \([K_\theta(u_i,u_j)]\) is strictly positive definite: it is a Gram matrix of vectors \((\sqrt{\theta^j}\,u_i f(u_i)^j)_{j\ge1}\). Their first \(m\) coordinates are independent because \(f(u_i)\ne0\) are distinct, by the Vandermonde determinant. Equation (2), approximation by smooth derivative bumps at arbitrary distinct points, and the min-max principle therefore give arbitrarily large strictly positive subspaces of \(P_\theta\), hence infinitely many positive eigenvalues.

A self-adjoint Markov contraction has spectrum in \([-1,1]\). Positivity confines the spectral measure \(\mu_h\) of any centered \(h\in L^2\) to \([0,1]\); by the spectral theorem
\[
\gamma_n(h)=\langle h,P_\theta^n h\rangle
=\int_{[0,1]}t^n\,\mu_h(dt).
\tag{5}
\]
Taking arbitrary forward differences proves the displayed complete monotonicity. At \(\theta=0\), \(C_0(u,v)=uv\) and the centered operator vanishes.

**3. Negative parameter and exact finite inertia.** Write \(a=-\theta>0\), and, for the selected points, \(t_i=f(u_i)\) and \(w_i=u_i t_i\). By (1),
\[
(H_m)_{ij}=-a\frac{w_iw_j}{1+a t_it_j}.
\]
All \(w_i\ne0\), all \(t_i\) are distinct, and the denominators are positive. The classical Cauchy double-alternant determinant identity gives the *exact* nonzero determinant
\[
\boxed{\displaystyle
\det H_m=(-1)^{m(m+1)/2}a^{m(m+1)/2}
\frac{\big(\prod_{i=1}^m w_i^2\big)
\big(\prod_{1\le i<j\le m}(t_i-t_j)^2\big)}
{\prod_{i,j=1}^m(1+a t_it_j)}.}
\tag{6}
\]
This applies to each leading principal submatrix too. With \(\det H_0=1\), the successive Gaussian-elimination pivots have signs
\[
\operatorname{sgn}\frac{\det H_j}{\det H_{j-1}}=(-1)^j,
\qquad j=1,\ldots,m.
\tag{7}
\]
The inertia theorem for symmetric \(LDL^\mathsf{T}\) congruence now yields precisely \(\lfloor m/2\rfloor\) positive and \(\lceil m/2\rceil\) negative eigenvalues. In particular, already \(m=2\) gives a negative determinant, so the kernel is *not* negative semidefinite despite being pointwise nonpositive.

Take distinct interior points and smooth nonnegative disjoint bump functions \(\phi_i\), each of integral one, supported in shrinking neighborhoods of \(u_i\). The covariance matrix of the centered observables obtained by integrating the \(\phi_i\)'s converges entrywise to \(H_m\), by (2) and continuity of \(K_\theta\). For sufficiently narrow bumps it has the same inertia, as each eigenvalue of \(H_m\) is nonzero. Thus the centered Markov operator has positive subspaces of unbounded dimension and negative subspaces of unbounded dimension. Its continuity-kernel Hilbert–Schmidt compactness implies infinitely many positive and negative nonzero eigenvalues.

For a centered eigenfunction \(h_-\) associated with any negative eigenvalue \(\lambda_-<0\), stationarity gives
\[
\gamma_n(h_-)=\lambda_-^n\|h_-\|_2^2,
\qquad n\ge0,
\tag{8}
\]
with strict alternating signs at positive lags. A positive eigenfunction yields strictly positive covariance at every lag. Meanwhile (1) has \(K_\theta\le0\) everywhere when \(\theta<0\), the known negative quadrant dependence property. This proves the stated distinction.

## Verification

Run the included standard-library script with `python3 CHECKER.py`. It exactly checks identity (6) by rational Gaussian elimination and the alternating \(LDL^\mathsf{T}\) pivot signs for \(m=1,\ldots,6\), and checks positive definiteness for positive parameters for the same sizes. For the 2024 exponential-ratio model at \(\theta=-1\), the two-node kernel at \(u=1/4\), \(v=3/4\) has eigenvalues approximately \(-0.0245863162\) and \(+0.000950767876\). These are finite reproductions of the formulas, **not** the proof of the infinite-rank result; (3), (6), bump approximation and compact spectral theory provide that proof for every admissible parameter and every matrix size.

## Relationship to prior work

El Ktaibi, Bentoumi and Mesfioui (2024) introduce the separable ratio-type family and its exponential-generator example, and study admissibility, quadrant dependence, tail measures and rank association. Those definitions and parameter intervals are prior work. The present theorem treats stationary copula-based Markov operators, exact signed inertia of every sampled covariance kernel, and lag-covariance moment sequences.

Longla (2024) gives a general Hilbert–Schmidt eigenfunction representation and studies mixing for other copula constructions. That general spectral representation is used here as background and does not by itself supply the sign counts in (6) for the separable ratio-type family. Longla, Mous-Abou and Ngongo (2022) study mixing for the classical Ali–Mikhail–Haq subfamily; their statements about mixing do not imply the alternating finite-matrix inertia or infinitely many eigenvalues of both signs. Chesneau (2023) provides other ratio-type copulas; its construction and dependence calculations do not make this spectral classification. The Cauchy determinant identity and the spectral theorem are classical and are not presented as new.

## Limitations

The theorem is conditional on actual copula admissibility and a strictly positive denominator; it does not characterize the admissible parameter range for arbitrary \(f\). The singular-denominator positive endpoint is excluded, including \(\theta=1\) in the exponential example. No exact spectrum, spectral gap or mixing constant is computed. Priority has been compared with the cited primary full texts and indexed searches but cannot be declared exhaustive; related classical sign-regular kernel literature remains a possible source of overlapping formulations. This is not independently audited.

## References

1. F. El Ktaibi, R. Bentoumi and M. Mesfioui, *On the Ratio-Type Family of Copulas*, Mathematics **12** (2024), 1743; first public date 3 June 2024. https://doi.org/10.3390/math12111743
2. M. Longla, *New copula families and mixing properties*, Statistical Papers **65** (2024), 4331–4363. https://doi.org/10.1007/s00362-024-01559-9
3. M. Longla, H. Mous-Abou and I. S. Ngongo, *On Some Mixing Properties of Copula-Based Markov Chains*, Journal of Statistical Theory and Applications **21** (2022), 131–154. https://doi.org/10.1007/s44199-022-00045-1
4. C. Chesneau, *A Collection of Two-Dimensional Copulas Based on an Original Parametric Ratio Scheme*, Symmetry **15** (2023), 977. https://doi.org/10.3390/sym15050977
