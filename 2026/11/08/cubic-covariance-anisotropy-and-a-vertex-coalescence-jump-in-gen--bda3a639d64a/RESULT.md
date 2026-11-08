# Cubic covariance anisotropy and a vertex-coalescence jump in generalized parking-function polytopes

## Finding

Let \(n\ge 2\), \(a\ge1\), and \(b>0\). For \(0\le j\le n\), let \(v_j\in\mathbb R^n\) be the vector with \(j\) entries equal to \(1\) followed by \(a+jb,a+(j+1)b,\ldots,a+(n-1)b\), and set \(P_n(a,b)=\operatorname{conv}\{\sigma v_j:\sigma\in S_n,0\le j\le n\}\). For positive integral \(a,b\), this is the generalized parking-function polytope of Hanada–Lentfer–Vindas-Meléndez. Here real parameters are allowed by the explicit orbit-hull definition. Let \(X_n\) be uniformly distributed on the **distinct vertices** of \(P_n(a,b)\), not uniformly in its volume.

Put
\[
I_{n,a}=\begin{cases}\{1,\ldots,n\},&a=1,\\ \{0,\ldots,n\},&a>1,\end{cases}\qquad
w_j=\frac{1/j!}{\sum_{h\in I_{n,a}}1/h!}\quad(j\in I_{n,a}),
\]
\[
T_n=na+\frac b2 n(n-1),\qquad
U_n=na^2+abn(n-1)+\frac{b^2}{6}n(n-1)(2n-1),
\]
\[
D_j=j(a-1)+\frac b2 j(j-1),\qquad
A_j=j(a^2-1)+abj(j-1)+\frac{b^2}{6}j(j-1)(2j-1).
\]
Write \(\mathbb E_w\) for expectation under the discrete weights \(w_j\). The **entire Euclidean covariance spectrum** of \(X_n\) consists of
\[
\boxed{\lambda_\parallel=\frac{\mathbb E_w D_j^2-(\mathbb E_w D_j)^2}{n}},\qquad
\boxed{\lambda_\perp=\frac{U_n-\mathbb E_w A_j-n^{-1}\mathbb E_w(T_n-D_j)^2}{n-1}}.
\]
Their eigenspaces are respectively \(\operatorname{span}\{(1,\ldots,1)\}\) (multiplicity one) and its orthogonal complement (multiplicity \(n-1\)); both eigenvalues are strictly positive.

For fixed \(a\ge1\) and \(b>0\), set
\[
V_{a,b}=\begin{cases}
(a-1)^2+2b(a-1)+\tfrac32b^2,&a>1,\\
\dfrac{b^2e(6e-7)}{4(e-1)^2},&a=1.
\end{cases}
\]
Then
\[
\boxed{n\lambda_\parallel\longrightarrow V_{a,b}},\qquad
\boxed{\frac{\lambda_\perp}{n^2}\longrightarrow\frac{b^2}{12}},\qquad
\boxed{\frac{\lambda_\perp/\lambda_\parallel}{n^3}\longrightarrow\frac{b^2}{12V_{a,b}}}.
\]
The total-coordinate-sum deficit \(T_n-\sum_{i=1}^n X_{n,i}\) converges in distribution and in every fixed polynomial moment to \((a-1)J+\frac b2J(J-1)\), with \(J\sim\operatorname{Poisson}(1)\) for \(a>1\), and \(J\sim\operatorname{Poisson}(1)\) conditioned on \(J\ge1\) for \(a=1\). These laws are discrete and non-Gaussian. There is a strict vertex-coalescence discontinuity:
\[
\boxed{\lim_{a\downarrow1,\ a>1}V_{a,b}=\tfrac32b^2
\quad<\quad V_{1,b}=\frac{b^2e(6e-7)}{4(e-1)^2}}.
\]
The polytopes \(P_n(a,b)\) nevertheless converge in Hausdorff distance to \(P_n(1,b)\) for each fixed \(n\) as \(a\downarrow1\).

## Assumptions and scope

All geometry uses the ambient standard Euclidean metric on \(\mathbb R^n\); these polytopes are full dimensional. The distribution is uniform on distinct **extreme points** of \(P_n(a,b)\). The first parameter is real with \(a\ge1\); the second is real with \(b>0\). All asymptotics send \(n\to\infty\) at **fixed** \(a,b\). No simultaneous limit as \(a\downarrow1\) and \(n\to\infty\) is asserted. The condition number is the ratio of largest to smallest covariance eigenvalues for all sufficiently large \(n\), when the transverse eigenvalue dominates; its asymptotic formula is as stated.

## Proof

**1. Identify all distinct vertices, including at real parameters.** Every displayed orbit point is exposed. Place distinct negative coefficients on the \(j\) coordinates of value \(1\) and distinct positive coefficients on the remaining coordinates, with strictly increasing positive coefficients paired with increasing values. A rearrangement argument uniquely selects a specified permutation within the \(j\)-th orbit. Against any layer with fewer than \(j\) ones, at least one negative-coefficient coordinate must instead receive a value strictly above \(1\); against a layer with more than \(j\) ones, at least one positive-coefficient coordinate must be replaced by \(1\). The other coordinates of the sorted candidate have the same upper values and cannot compensate. These inequalities are strict except that \(v_0=v_1\) at \(a=1\). For \(j=0\), use all positive coefficients; for \(j=n\), all negative coefficients. Thus the only orbit merger is \(v_0=v_1\) at \(a=1\), and the remaining orbits comprise the entire extreme-point set. Every \(j\)-th orbit has \(n!/j!\) distinct members. This agrees with Propositions 3.4–3.5 of Hanada–Lentfer–Vindas-Meléndez for integral parameters.

**2. Obtain the exact mixture.** Let \(J_n\) have weights \(w_j\). Conditional on \(J_n=j\), choose a uniformly random permutation of \(v_j\). This samples every distinct vertex with equal probability. Its coordinate sum \(S_n\) and squared Euclidean norm \(Q_n\) are deterministic conditional on the layer:
\[
S_n=T_n-D_{J_n},\qquad Q_n=U_n-A_{J_n}.
\]
The formulas for \(D_j,A_j\) follow by replacing the first \(j\) terms of \(a,a+b,\ldots,a+(n-1)b\) by \(1\).

**3. Diagonalize exactly.** Permutation invariance implies \(\operatorname{Cov}(X_n)=\alpha I+\beta\mathbf1\mathbf1^{\mathsf T}\). The unit vector \(n^{-1/2}\mathbf1\) has variance \(\operatorname{Var}(S_n)/n\), yielding \(\lambda_\parallel\). The trace is \(\mathbb E Q_n-(\mathbb E S_n)^2/n\). Subtract the parallel eigenvalue and divide by \(n-1\):
\[
(n-1)\lambda_\perp
=\mathbb E Q_n-\frac1n\mathbb E S_n^2,
\]
which is the displayed expression. The law \(J_n\) assigns positive probabilities to at least two distinct coordinate sums, so \(\lambda_\parallel>0\). At least one orbit contains nonconstant coordinates, and therefore has positive transverse variance; hence \(\lambda_\perp>0\).

**4. Take the Poisson limit.** For \(a>1\), the truncated exponential weights \(j!^{-1}\) tend, with all polynomial moments, to the \(\operatorname{Poisson}(1)\) mass \(e^{-1}/j!\). For \(a=1\) the normalization instead tends to \(e-1\), giving the positive-Poisson conditional law. The factorial tail dominates every polynomial in \(j\), so the moment assertion and the sum-deficit limit follow. Writing \(c=a-1\) and \(D=cJ+\frac b2J(J-1)\), the Poisson factorial moments give
\[
\operatorname{Var}(J)=1,\quad
\operatorname{Cov}(J,J(J-1))=2,\quad
\operatorname{Var}(J(J-1))=6.
\]
Consequently \(\operatorname{Var}(D)=c^2+2bc+\frac32b^2\) for \(a>1\). At \(a=1\), the first two nonzero factorial-square moments are \(\mathbb E J(J-1)=1\) and \(\mathbb E[J(J-1)]^2=7\) before conditioning; divide their expectations by \(1-e^{-1}\). This gives \(V_{1,b}=b^2e(6e-7)/(4(e-1)^2)\). Because \(n\lambda_\parallel=\operatorname{Var}(D_{J_n})\), the parallel asymptotic follows.

**5. Transverse limit and jump.** The expressions \(D_{J_n}\) and \(A_{J_n}\) have moments bounded uniformly in \(n\), since they are fixed-degree polynomials in factorial-tail indices. Thus \(\mathbb E_w A_j=O_{a,b}(1)\), while \(\mathbb E_w (T_n-D_j)^2=T_n^2+O_{a,b}(n^2)\). Since \(U_n=b^2n^3/3+O_{a,b}(n^2)\) and \(T_n=b n^2/2+O_{a,b}(n)\), it follows that \(\lambda_\perp=b^2n^2/12+O_{a,b}(n)\). Dividing by the parallel limit yields the cubic condition-number scale. Finally, the two formulas for \(V_{a,b}\) have different one-sided values at \(a=1\), because two distinct positive-weight vertex orbits coalesce there. All generating vertices depend continuously on \(a\), so the convex hull converges in Hausdorff metric for every fixed \(n\). This proves the stated geometric discontinuity.

## Verification

Execute `python3 check_parking_covariance.py` with Python 3 (no third-party dependencies). The script constructs all distinct vertices and full covariance matrices using exact rational arithmetic for sizes \(2\le n\le6\) and parameter pairs \((a,b)\in\{(1,1),(2,1),(3,2)\}\). It verifies both invariant eigenspaces and the exact formula. Separate numerical calculations at sizes 100, 500, and 2000 compare the three asymptotic quantities with their proved constants. Its final success marker is `PARKING_VERTEX_SPECTRUM_CHECKS_PASSED`.

These finite checks are not a proof of the general statements; the complete proof is the orbit decomposition and moment calculation above.

## Relationship to prior work

Hanada, Lentfer and Vindas-Meléndez (2022/2024) determine the two-parameter parking-function polytopes, their vertex orbits, face structure and volume; their Propositions 3.4–3.5 give the exact source orbit descriptions and the orbit merger when \(a=1\). Bayer and collaborators (2024/2025) treat generalized versions via facets, building sets, polymatroids and combinatorial invariants. Neither inspected work provides the covariance eigenspectrum, the cubic vertex-cloud anisotropy, or the covariance discontinuity. Other known results about inballs, circumballs or minimal enclosing ellipsoids optimize *extremal shape*, not the covariance of the **uniform vertex measure**, so they do not imply this claim. A different combinatorial family may have a similar two-eigenspace representation without implying the exact weighted moments here.

## Limitations

This concerns the vertex measure only. Uniform volume measure, weighted vertex sampling, other parameter vectors, and coupled dimension/parameter limits are not addressed. For real nonintegral parameters the object is defined by the stated orbit hull, not by integer parking functions. The exact finite-size formula uses finite factorial sums rather than a claimed simpler closed form. Historical priority is provisional: equivalent formulations in random-permutation or random-vertex covariance literature may exist. Independent audit has not been performed.

## References

- M. Hanada, J. Lentfer and A. R. Vindas-Meléndez, *Generalized parking function polytopes*, arXiv:2212.06885 (first public 2022-12-13); *Annals of Combinatorics*, DOI:10.1007/s00026-023-00671-1, especially Propositions 3.4–3.5.
- M. M. Bayer et al., *Combinatorics of generalized parking-function polytopes*, arXiv:2403.07387 (first public 2024-03-12); *Discrete & Computational Geometry*, DOI:10.1007/s00454-025-00770-1.
- Z. Amanbayeva and T. Wang, *The convex hull of parking functions of length n*, arXiv:2104.08454 (2021), for the classical polytope's enumerative geometry.
