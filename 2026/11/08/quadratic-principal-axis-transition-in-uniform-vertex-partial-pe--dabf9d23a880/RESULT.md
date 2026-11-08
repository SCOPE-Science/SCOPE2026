# Quadratic principal-axis transition in uniform-vertex partial permutohedra

## Finding
Let \(m\ge2\) and \(n\ge m\) be integers. The standard partial permutohedron is
\[
 \mathcal P(m,n)=\operatorname{conv}\{x\in\{0,1,\ldots,n\}^m:\text{all nonzero coordinates of }x\text{ are distinct}\}.
\]
Let \(X\) be a uniformly chosen **vertex**, with every distinct vertex equally likely; write \(C=\operatorname{Cov}(X)\), \(H=\mathbf1\mathbf1^\mathsf{T}/m\), and
\[
 Z_m=\sum_{d=0}^m\frac1{d!},\qquad p_m=\frac1{m!Z_m}.
\]
Define the following exact rational coefficients (with \(p=p_m\)):
\[
\begin{aligned}
 A_m&=1-(m^2-m+2)p-(m-1)p^2,\\
 B_m&=-m^2+m+3+(m^3-4m^2+3m-6)p+(m^2-4m+3)p^2,\\
 C_m&=-\frac1{12}\bigl[m^4-12m^3+41m^2-34m-27\\
 &\hspace{2em}+(3m^4-20m^3+36m^2-11m+54)p\\
 &\hspace{2em}+(3m^3-21m^2+45m-27)p^2\bigr].
\end{aligned}
\]
**Theorem.** There are positive covariance eigenvalues \(\lambda_\parallel\) on \(\mathbb R\mathbf1\) and \(\lambda_\perp\) on \(\mathbf1^\perp\), the latter with multiplicity \(m-1\), such that
\[
 C=\lambda_\parallel H+\lambda_\perp(I-H),\qquad
 \lambda_\parallel-\lambda_\perp=\frac{A_mn^2+B_mn+C_m}{m(m-1)}.
\]
For every \(m\ge2\), one has \(A_m>0\), and the quadratic has exactly one root \(\tau_m\) with \(\tau_m>m\). The **entire top covariance eigenspace** is \(\mathbf1^\perp\) for \(m\le n<\tau_m\), is all of \(\mathbb R^m\) if \(n=\tau_m\), and is \(\mathbb R\mathbf1\) for \(n>\tau_m\). Moreover,
\[
\boxed{\displaystyle\lim_{m\to\infty}\frac{\tau_m}{m^2}=\frac12+\frac1{\sqrt3}}.
\]
For instance, \(\tau_2=2+\sqrt5\) and \(\tau_3=48/7\); the change occurs between integer heights \(4,5\) for \(m=2\) and \(6,7\) for \(m=3\). This occurs despite the fixed face-lattice type of \(\mathcal P(m,n)\) for fixed \(m\) and all \(n\ge m\).

## Assumptions and scope
The metric is ordinary coordinate Euclidean distance in \(\mathbb R^m\). Covariance uses the **discrete uniform vertex measure**, not the intrinsic volume measure and not a measure supported only on the maximum-support permutation orbit. The height parameter \(n\) is an integer at least \(m\). The real root \(\tau_m\) is a parameter threshold; its appearance does not assert that it is an integer.

Let \(w_k=m!/(m-k)!\), \(W_m=\sum_{k=0}^m w_k\), and
\[
 S_k=\frac{k(2n-k+1)}2,\qquad
 Q_k=\sum_{j=0}^{k-1}(n-j)^2.
\]
For any function \(f\) on \(\{0,\ldots,m\}\), write \(\mathbb E_*f=W_m^{-1}\sum_{k=0}^m w_k f(k)\). Both eigenvalues have the independent explicit evaluations
\[
 \lambda_\parallel=\frac{\mathbb E_* S_k^2-(\mathbb E_* S_k)^2}m,
 \qquad\lambda_\perp=\frac{m\mathbb E_* Q_k-\mathbb E_* S_k^2}{m(m-1)}.
\]
The vertex centroid is \((\mathbb E_* S_k/m)\mathbf1\).

## Proof
**1. Vertex orbits.** The vertex theorem for partial permutohedra (Heuer--Striker, Proposition 5.7, or Behrend et al., Proposition 2.7) states that the vertices consist exactly of all permutations of
\((n,n-1,\ldots,n-k+1,0,\ldots,0)\) for \(0\le k\le m\). The rank-\(k\) orbit has \(w_k\) vertices. Every such vertex has coordinate sum \(S_k\) and squared Euclidean norm \(Q_k\). Averaging over an orbit gives the same coordinate mean in every position. The full vertex distribution is invariant under all coordinate permutations, so its covariance acts by one scalar on \(\mathbf1^\perp\) and one on \(\mathbb R\mathbf1\). Taking variance along \(\mathbf1/\sqrt m\) yields \(\lambda_\parallel=\operatorname{Var}(S_k)/m\); taking the trace and subtracting that eigenvalue yields the stated \(\lambda_\perp\). The finite support affinely spans \(\mathbb R^m\), so both eigenvalues are positive.

**2. Closed polynomial.** Put \(D=m-k\). Its exact distribution is
\[
 \Pr(D=d)=\frac{1/d!}{Z_m},\quad 0\le d\le m.
\]
For the falling factorial \((D)_j\), direct index shifting gives
\[
 \mathbb E(D)_j=\frac{Z_{m-j}}{Z_m}
 =1-p_m\sum_{i=0}^{j-1}(m)_i \quad(j\ge1),
\]
where \(Z_s=0\) for negative indices and \((m)_i=0\) for \(i>m\). In particular these identities evaluate all ordinary moments of \(D\) through order four. Substitute \(k=m-D\), \(S_k=kn-k(k-1)/2\), and \(Q_k=kn^2-nk(k-1)+k(k-1)(2k-1)/6\) into the eigenvalue formulas in the preceding section. Collecting powers of \(n\) gives exactly
\[
 m(m-1)(\lambda_\parallel-\lambda_\perp)=A_mn^2+B_mn+C_m.
\]
This is a polynomial identity derived from the full finite vertex distribution, without fitting data or using an asymptotic approximation.

**3. Exactly one crossing above the combinatorial threshold.** Since \(Z_m\ge2\) for \(m\ge1\), \(0<p_m\le1/(2m!)\). Thus for \(m\ge4\),
\[
 A_m\ge1-\frac{m^2}{2m!}-\frac{m-1}{4(m!)^2}>0.
\]
The last bound is positive at \(m=4\) and strengthens with increasing \(m\). Direct substitution gives \(A_2=4/25>0\) and \(A_3=63/128>0\). At \(n=m\), exact collection yields
\[
\begin{aligned}
-12(A_mm^2+B_mm+C_m)={}&m^4+17m^2-70m-27\\
&+(3m^4+16m^3+24m^2+61m+54)p_m\\
&+(3m^3+15m^2+9m-27)p_m^2.
\end{aligned}
\]
For \(m\ge4\), the first summand is positive (its value at \(4\) is \(221\) and its derivative is positive thereafter); both other summands are positive. For \(m=2,3\) one computes \(A_mm^2+B_mm+C_m=-4/5,-729/128\), respectively. Hence the quadratic is negative at \(n=m\) but tends to \(+\infty\) as \(n\to+\infty\). An upward-opening quadratic negative at one point has exactly one zero to its right, and its sign changes there. The eigenspace classification follows.

**4. Quadratic-scale limit.** Since \(p_m=O(1/m!)\), the coefficient formulas imply
\[
 A_m\longrightarrow1,\qquad \frac{B_m}{m^2}\longrightarrow-1,
 \qquad\frac{C_m}{m^4}\longrightarrow-\frac1{12}.
\]
After setting \(n=m^2z\) and dividing the quadratic by \(m^4\), the positive root converges to the positive zero of \(z^2-z-1/12\), namely \(1/2+1/\sqrt3\). Since the unique relevant root is positive and lies above \(m\), no root selection ambiguity occurs.

## Verification
The standalone standard-library script `verify.py` reconstructs all actual vertices for \(2\le m\le6\), \(m\le n\le m+6\), evaluates every entry of their rational covariance matrices, and independently compares both predicted eigenspaces and the exact quadratic. This is \(35\) parameter instances involving \(16,583\) enumerated vertex vectors. It also checks positivity and the sign change around the unique real threshold for \(2\le m\le200\). Run `python3 verify.py` in the directory containing that file. All finite checks returned `PARTIAL_PERMUTOHEDRON_VERTEX_COVARIANCE_CHECKS_PASSED`. These computations corroborate the identities; the infinite-parameter proof is the orbit moment calculation and polynomial sign argument above.

## Relationship to prior work
Heuer and Striker established the original polytope and the exact vertex-orbit description in their 2020 public preprint. Behrend and collaborators investigated its face lattice, volume, and Ehrhart invariants. The 2024 article by Behrend focuses on Ehrhart enumeration. These references provide the vertex counts and reveal that for fixed \(m\) the combinatorial type is constant across \(n\ge m\), but they do not state the covariance spectrum or its principal-axis transition.

Related analyses of *enclosing spheres* and *Löwner ellipsoids* for partial permutohedra make use of rank-orbit sums or specially weighted two-orbit contact distributions. A minimum enclosing ball depends on the maximum radial distance; a Löwner ellipsoid optimizes a determinant with chosen contact weights. Neither quantity determines the covariance under the uniform distribution on **all** vertices; the vertex measure and the sharp spectral crossing here are different objects. In particular, no claim is made about an optimal ellipsoid or an interior-volume covariance tensor. The published research comparisons listed in the review identify these distinctions at the statement level.

## Limitations
The theorem concerns the standard coordinate realization and the discrete uniform vertex measure only. It does not describe the covariance of a uniform random interior point, other vertex weightings, or nonorthogonal affine images. The exact real threshold is defined through explicit coefficients rather than a simpler radical simplification. Exhaustive finite checks do not replace the infinite proof, and independent priority verification remains open.

## References
1. Dylan Heuer and Jessica Striker, *Partial permutation and alternating sign matrix polytopes*, arXiv:2012.09901, first public preprint 2020-12-17, Section 5.1, Proposition 5.7. https://arxiv.org/abs/2012.09901
2. Roger E. Behrend, Federico Castillo, Anastasia Chavez, Alexander Diaz-Lopez, Laura Escobar, Pamela E. Harris, and Erik Insko, *Partial permutohedra*, arXiv:2207.14253, first public preprint 2022-07-28, Proposition 2.7 and Sections 3--6. https://arxiv.org/abs/2207.14253
3. Roger E. Behrend, *Ehrhart polynomials of partial permutohedra*, arXiv:2403.06975, first public preprint 2024-03-11, Sections 1--3. https://arxiv.org/abs/2403.06975
4. *A quadratic contact threshold for the Löwner ellipsoid of partial permutohedra*, publicly available mathematical result (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-a-quadratic-contact-threshold-for-the-l-wner-ellipsoid-of-partia--e37a5d64aafd.
5. *Exact circumball and contact-rank transitions of partial permutohedra*, publicly available mathematical result (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-circumball-and-contact-rank-transitions-of-partial-permuto--5aee45e4fbff.
