# Unbounded distortion gap for minimum-singular-value row selection on well-conditioned Krylov spaces

## Finding

For every integer \(N\ge 2\), there is a real symmetric positive-definite matrix \(A_N\) of condition number exactly \(3\) and an exact two-column orthonormal Arnoldi basis \(V_N\) for \(\mathcal K_2(A_N,u_N)\), with ambient dimension \(N+3\), for which **every** two-row selection maximizing \(\sigma_{\min}(SV_N)\) has sketched-basis distortion \(\kappa_2(SV_N)=\sqrt N\). Both ordinary DEIM and Q-DEIM select such maximizers. Yet a different two-row selection has \(\kappa_2(SV_N)=1\), the globally minimal possible full-rank distortion, and is the unique two-row minimizer of this distortion.

For the QR whitening \(SV_N=QR\), the distortion metric of Bergermann (2026, equation (3.5)) is \(\kappa_2(V_NR^{-1})=\kappa_2(SV_N)\). Consequently the ratio between the distortion of an *ideal globally E-optimal row selector* and the best possible distortion is exactly \(\sqrt N\), with no dimension-independent bound, even on uniformly well-conditioned SPD Krylov problems.

This is a separation of **selection objectives**, not a claim that the small-amplitude condition-optimal sketch is preferable under finite precision or additive measurement noise.

## Assumptions and scope

All statements are in real exact arithmetic. Fix an integer \(N\ge2\), let \(n=N+3\), and write \(e_j\) for the standard coordinate vectors of \(\mathbb R^n\). Define

\[
\varepsilon=\frac1N,\qquad
\beta=\sqrt{1-\varepsilon^2},\qquad
\gamma=\frac{\beta}{\sqrt N},
\]

\[
u=\beta e_1+\varepsilon e_2,\qquad
v=\varepsilon e_3+\gamma\sum_{j=4}^{N+3}e_j,
\qquad V_N=[u\ \ v],
\]

and

\[
A_N=2I_n+uv^{\mathsf T}+vu^{\mathsf T}.
\]

A row selector \(S\) consists of exactly two distinct unweighted standard coordinate rows. Rank-deficient \(SV_N\) has distortion \(+\infty\). E-optimality means globally maximizing \(\sigma_{\min}(SV_N)\) over all such selectors; condition-optimality means globally minimizing \(\kappa_2(SV_N)\) among full-rank selectors. These objectives must not be conflated. In particular, a single common scalar rescaling of \(S\) changes singular-value magnitudes but not \(\kappa_2(SV_N)\).

DEIM is the sequential residual-maximum pivot algorithm; Q-DEIM is column-pivoted QR applied to \(V_N^{\mathsf T}\), exactly as described by Drmač and Gugercin and used by Bergermann. Ties among the last \(N\) rows are harmless.

## Proof

**1. An exact and uniformly conditioned Krylov basis.** The supports of \(u\) and \(v\) are disjoint and

\[
\|u\|_2^2=\beta^2+\varepsilon^2=1,\qquad
\|v\|_2^2=\varepsilon^2+N\gamma^2=1.
\]

Hence \(V_N^{\mathsf T}V_N=I_2\). On the span of \(u,v\), the matrix \(A_N\) acts as \(\begin{psmallmatrix}2&1\\1&2\end{psmallmatrix}\); on its orthogonal complement it acts as \(2I\). Its spectrum is therefore \(\{1,3\}\) together with \(n-2\) copies of \(2\), and \(\kappa_2(A_N)=3\). Moreover \(A_Nu=2u+v\). A first exact Arnoldi step starting at \(u\) subtracts \(2u\) and normalizes the residual \(v\), producing exactly \(V_N\). The same is true for the first two Lanczos vectors.

**2. A strict ordering of the three row amplitudes.** For \(N\ge2\),

\[
\beta>\gamma>\varepsilon>0,
\qquad
\gamma^2-\varepsilon^2
=\frac{N^2-N-1}{N^3}>0.
\]

A full-rank two-row selection must take one row from \(\{1,2\}\), supported only in the first column, and one from \(\{3,4,\ldots,N+3\}\), supported only in the second. Its nonzero singular values are exactly the two chosen positive row amplitudes. All other row pairs give rank at most one.

**3. Complete two-row classification.** Up to singular-value ordering, the four full-rank selection types and their exact invariants are:

| Selected row indices | \(\sigma_{\min}(SV_N)\) | \(\kappa_2(SV_N)\) |
|---|---|---|
| \(\{1,3\}\) | \(\varepsilon\) | \(\sqrt{N^2-1}\) |
| \(\{1,j\},\ 4\le j\le N+3\) | \(\gamma\) | \(\sqrt N\) |
| \(\{2,3\}\) | \(\varepsilon\) | \(1\) |
| \(\{2,j\},\ 4\le j\le N+3\) | \(\varepsilon\) | \(\sqrt{N-1/N}\) |

Because \(\gamma>\varepsilon\), the global maximum of the smallest singular value is \(\gamma\), and **all** E-optimal pairs are precisely \(\{1,j\}\) with \(4\le j\le N+3\). Their condition numbers equal \(\sqrt N\). The row pair \(\{2,3\}\) has two equal positive singular values, hence condition number \(1\). All other full-rank types have strictly larger condition number for \(N\ge2\), and rank-deficient pairs have infinite condition number. Thus \(\{2,3\}\) is the unique distortion minimizer.

**4. Actual DEIM and Q-DEIM pivots.** In DEIM, the unique largest absolute first-column entry is \(\beta\) at row \(1\), so that is the first pivot. The second-column entry at that pivot is zero; therefore the second-column interpolation residual is exactly \(v\). Its largest entry magnitude is \(\gamma\), attained precisely at rows \(4,\ldots,N+3\). In Q-DEIM, the columns of \(V_N^{\mathsf T}\) have norms \(\beta,\varepsilon,\varepsilon,\gamma,\ldots,\gamma\). The first pivot is uniquely row \(1\). After projecting it out, the remaining first-coordinate columns vanish and the largest residual column norm is \(\gamma\), again at a row in \(\{4,\ldots,N+3\}\). Thus both procedures produce an E-optimal but distortion-suboptimal selector.

**5. The published whitening distortion.** For any full-rank selected \(SV_N\), perform thin QR factorization \(SV_N=QR\), where \(Q^{\mathsf T}Q=I\). Since \(V_N\) has orthonormal columns, the nonzero singular values of \(V_NR^{-1}\) are those of \(R^{-1}\). Therefore

\[
\kappa_2(V_NR^{-1})=\kappa_2(R^{-1})
=\kappa_2(R)=\kappa_2(SV_N).
\]

The distortion ratio is exactly \(\sqrt N/1=\sqrt N\), which diverges as \(N\to\infty\). This completes the proof.

## Verification

The standalone `verify_krylov.py` checker uses exact rational arithmetic on squared row amplitudes and enumerates every two-row subset for each \(N=2,\ldots,80\), totaling \(95{,}274\) pairs. It checks the complete maxima/minima classification and the exact squared distortion ratios. It also independently constructs the floating-point matrices for ten sizes, runs DEIM and actual SciPy pivoted QR for Q-DEIM, checks the whitening identity, and for six sizes verifies the spectrum and second Arnoldi vector of the explicit SPD matrix. The recorded output is `CHECKS_OK`. The exact proof above, not the finite computations, establishes all-integer quantifiers.

Reproduction: `python verify_krylov.py` with Python 3, NumPy, and SciPy. No external input files or network access are needed.

## Relationship to prior work

Bergermann (2026, sections 3–5) derives the whitening condition-number distortion and chooses maximization of the smallest sketched-basis singular value as a useful selection objective, using DEIM and Q-DEIM. That paper does not claim a universal approximation ratio comparing its E-optimal objective with globally optimal condition-number distortion. The present exact construction shows that no dimension-independent ratio exists and that the stated algorithms attain the poorly distorted selection on a genuine SPD Krylov basis.

Drmač and Gugercin (2015/2016) develop Q-DEIM and analyze its inverse-selected-submatrix norm; their conditioning and interpolation bounds do not by themselves compare the E-optimal selection to the distinct minimum-condition-number selector. Ipsen and Saibaba (2025/2026) study complexity of distinct subset criteria, including pseudo-inverse norm and condition number, but do not furnish this SPD Krylov construction or its exact simultaneous DEIM/Q-DEIM behavior. These established tools and distinctions are credited, not claimed as new.

## Limitations

The result concerns exactly two selected rows, a two-dimensional Krylov space, and the particular explicit family. It is not a lower bound on approximation errors, floating-point stability, solver convergence or the runtime of the complete Krylov algorithms. The condition-optimal row pair selects entries of size \(1/N\); thus its inverse sketch may be highly sensitive to **additive data noise or finite precision**, despite its ideal scale-invariant condition number. The theorem does not recommend that row pair for noisy computation. It instead isolates a sharp objective mismatch in the stated distortion metric. Weighted row sampling and other objectives are not analyzed, and broader pre-existing subset-selection theorems may subsume parts of the observation.

## References

1. K. Bergermann, *Deterministic sketching for Krylov subspace methods*, arXiv:2604.07158v1 (April 8, 2026), especially equations (3.5)–(3.6), Algorithms 4.1–4.2, and sections 4–5. https://arxiv.org/abs/2604.07158
2. Z. Drmač and S. Gugercin, *A new selection operator for the discrete empirical interpolation method — improved a priori error bound and extensions*, arXiv:1505.00370v1 (May 2, 2015), SIAM J. Sci. Comput. 38 (2016). https://arxiv.org/abs/1505.00370
3. I. C. F. Ipsen and A. K. Saibaba, *Many (most?) column subset selection criteria are NP hard for a few columns*, arXiv:2511.02740v2 (April 10, 2026), especially criterion table and sections 5–6. https://arxiv.org/abs/2511.02740
