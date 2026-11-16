# Finite positive-type and universality cones for character-polynomial Abel kernels on \(SU(2)\)

## Finding

Fix \(0<r<1\) and an integer \(d\ge1\). Let \(\chi_j\) denote the irreducible \((j+1)\)-dimensional character of \(SU(2)\), with \(\chi_0=1\). Define
\[
 P_r(g)=\sum_{k=0}^{\infty}(k+1)r^k\chi_k(g)
       =\frac{1-r^2}{(1-r\operatorname{tr}(g)+r^2)^2},
 \quad q_b(g)=\sum_{j=0}^d b_j\chi_j(g),
 \quad K_{r,b}(x,y)=P_r(x^{-1}y)q_b(x^{-1}y).
\]
Here \(b=(b_0,\dots,b_d)\in\mathbb R^{d+1}\) is arbitrary, including masks that are not pointwise nonnegative. Define
\[
 C_n(b,r)=\sum_{j=0}^d b_j\sum_{h=0}^{\min(n,j)}
 (|n-j|+2h+1)r^{|n-j|+2h},\qquad
 S(b,r)=\sum_{j=0}^d b_j\sum_{h=0}^j r^{-j+2h}.
\]

**Theorem (all polynomial degrees).** The kernel \(K_{r,b}\) is of positive type on \(SU(2)\) **if and only if** precisely these \(d+1\) finite inequalities hold:
\[
 C_0(b,r)\ge0,\quad\ldots,\quad C_{d-1}(b,r)\ge0,
 \qquad S(b,r)\ge0.
\]
The character coefficient in degree \(n\) is \(C_n(b,r)\), and the entire infinite tail obeys the identity
\[
 \boxed{C_n(b,r)=r^{n-d+1}C_{d-1}(b,r)
              +(n-d+1)r^nS(b,r),\qquad n\ge d-1.}
\]
The coordinate transformation \(b\mapsto(C_0,\ldots,C_{d-1},S)\) is a real linear isomorphism. Consequently, for each fixed \(r\) the admissible mask cone is simplicial, with **exactly \(d+1\) irredundant facets and exactly \(d+1\) extreme rays**, all represented explicitly by the inverse of this finite transformation.

Within the positive-type cone, \(K_{r,b}\) is strictly positive definite on every finite set of distinct elements of \(SU(2)\) exactly when \(C_{d-1}+S>0\). It is \(C\)-universal (its RKHS is uniformly dense in \(C(SU(2))\)) exactly when all \(C_0,\ldots,C_{d-1}\) are **strictly** positive. Thus the asymptotic slope facet \(S=0\) can still contain universal kernels, whereas the other facets obstruct universality.

## Assumptions and scope

These assertions concern continuous, central, real kernels on the full compact group \(SU(2)\), not kernels on a finite subgroup or only on conjugacy classes. Positive type means that \((K_{r,b}(x_i,x_j))_{i,j=1}^m\) is positive semidefinite for arbitrary points and arbitrary \(m\). Strict positive definiteness requires positive definiteness for each collection of pairwise distinct points. For \(C\)-universality the RKHS is dense in the continuous complex-valued functions under the uniform norm. The endpoints \(r=0\) and \(r=1\) are excluded. Degree is *at most* \(d\), so \(b_d=0\) is allowed. The classification does not require \(q_b\) to be pointwise positive.

## Proof

**1. Character expansion.** For \(g\in SU(2)\), write \(\operatorname{tr}(g)=2x\), with \(-1\le x\le1\). The character is \(\chi_j(g)=U_j(x)\), where \(U_j\) is the Chebyshev polynomial of the second kind. Differentiating the classical generating function for the \(U_j\) gives
\[
 \sum_{k\ge0}(k+1)r^kU_k(x)
 =\frac{1-r^2}{(1-2rx+r^2)^2}.
\]
The series converges uniformly on the group since \(|\chi_k(g)|\le k+1\), and its sum is everywhere strictly positive because the denominator is positive for \(0<r<1\).

The Clebsch–Gordan multiplication rule is
\[
 \chi_j\chi_k=\sum_{h=0}^{\min(j,k)}\chi_{j+k-2h}.
\]
For any fixed resulting index \(n\), the values of \(k\) giving a copy of \(\chi_n\) are \(|n-j|, |n-j|+2,\ldots,n+j\). Their Abel coefficients yield \(C_n\) exactly as displayed in the theorem. Orthogonality of irreducible characters shows this is the unique expansion.

**2. The complete affine tail.** For \(n\ge d\), we have \(n\ge j\) for every mask index. Hence
\[
 \frac{C_n}{r^n}
 =\sum_{j=0}^db_j\sum_{h=0}^j
     (n-j+2h+1)r^{-j+2h}
 =(n+1)S+T,
\]
where \(T=\sum_j b_j\sum_{h=0}^j(-j+2h)r^{-j+2h}\) is independent of \(n\). This identity remains true at \(n=d-1\): the only possible formally negative index is \(n-j=-1\), for \(j=d,h=0\), and its coefficient \(n-j+2h+1\) is zero, so adding this zero term is legitimate. Thus \(C_{d-1}=r^{d-1}(dS+T)\). Eliminating \(T\) establishes the boxed identity for every \(n\ge d-1\).

**3. Necessary and sufficient finite constraints.** For a continuous central function on a compact group, the Peter–Weyl/Bochner criterion makes its kernel positive semidefinite exactly when all irreducible character coefficients are nonnegative (the associated Fourier matrices are positive scalar matrices). Therefore every admissible mask has \(C_0,\ldots,C_{d-1}\ge0\). The limit \(\lim_{n\to\infty}C_n/((n+1)r^n)=S\) proves \(S\ge0\) is also necessary. Conversely, if these \(d+1\) inequalities hold, both summands in the tail identity are nonnegative for every \(n\ge d-1\), proving every character coefficient nonnegative.

**4. No hidden facets or degeneracies.** Suppose \(C_0=\cdots=C_{d-1}=S=0\). The tail identity forces all \(C_n=0\), and completeness of the irreducible characters forces \(P_rq_b=0\) everywhere. Since \(P_r>0\) pointwise, \(q_b=0\). Linear independence of \(\chi_0,\ldots,\chi_d\) implies \(b=0\). The square linear map is therefore invertible. It carries the positive-type cone bijectively to the nonnegative orthant in \(\mathbb R^{d+1}\), proving both exact facet count and extreme-ray count.

**5. Strict positivity and universality.** For nonnegative \(C_{d-1},S\), the tail identity has \(C_n>0\) at every \(n\ge d\) whenever \(C_{d-1}+S>0\). Suppose an atomic measure \(\mu=\sum_i v_i\delta_{x_i}\), with distinct \(x_i\), gave zero kernel energy. Positivity of the character Fourier blocks implies the entire matrix Fourier transform of \(\mu\) is zero for every \(n\ge d\). A finite measure with only finitely many nonzero Peter–Weyl blocks coincides with a finite Fourier polynomial times Haar measure; it is absolutely continuous. Since \(\mu\) is also finite atomic and Haar measure has no atoms, \(\mu=0\). This proves strict positive definiteness. Conversely, when \(C_{d-1}=S=0\), only \(C_0,\ldots,C_{d-2}\) may survive, so the associated RKHS has finite dimension and cannot be strictly positive definite on arbitrarily large finite subsets. The standard compact-group Fourier/RKHS density criterion is \(C_n>0\) for every irreducible index \(n\). The tail identity reduces this precisely to strict positivity of \(C_0,\ldots,C_{d-1}\), given the admissibility constraints.

## Verification

The attached standalone `su2_poisson_checker.py` uses only rational arithmetic and the Python standard library. It independently evaluates the full Clebsch–Gordan coefficient formula and the predicted infinite-tail reduction at many separate degrees and rational radii, tests invertibility of the coordinate transformation, and checks two exact boundary examples. Running `python su2_poisson_checker.py` reports `PASS 3200 supplementary exact comparisons`. These finite comparisons support the formulas but do not replace the proof for arbitrary real radii, degrees or group elements.

At \(r=1/2\) and \(d=2\), the mask \((b_0,b_1,b_2)=(1/12,-1/3,1/3)\) has \((C_0,C_1,S)=(0,0,1)\), so its kernel is strictly positive definite but is not \(C\)-universal. The contrasting mask \((11/12,1/3,-1/3)\) has \((C_0,C_1,S)=(1,1,0)\), so its kernel is \(C\)-universal despite lying on a facet of the positivity cone. These two small-degree examples illustrate the general classification; no novelty is asserted for the quadratic subcase itself.

## Relationship to prior work

The character expansion and compact-group positive-type criterion are classical. The compact-kernel universality framework in Said–Da Costa–Steinert–Mostajeran (2026) supplies the universality motivation, while Azangulov–Smolensky–Terenin–Borovitskiy (2024) develops stationary compact Lie-group kernels and explicit \(SU(2)\) harmonic analysis. Neither inspected treatment gives this exact finite positivity certificate and simplicial-cone structure for **arbitrary-degree real character-polynomial masks**. The degree-two specialization is already established elsewhere and is not asserted to be new. The current contribution is the simultaneous \(d\)-parameter theorem, exact all-degree facet structure, and the sharp universal/strict/finite-rank strata.

## Limitations

The theorem is specific to the Abel coefficients \((n+1)r^n\) on \(SU(2)\). It does not assert an analogous finite certificate for heat-semigroup coefficients or for other compact Lie groups. The inverse coordinate map exists but is not expressed here in elementary closed form for general \(d\); it is computable from a finite \((d+1)\)-square matrix. Completeness of literature discovery is not asserted: a possible equivalent identity under Chebyshev-product or central-positive-type terminology remains a priority risk. Independent mathematical validation has not been performed.

## References

1. Salem Said, Nathaël Da Costa, Franziskus Steinert, Cyrus Mostajeran, *Universality of kernels on Riemannian symmetric spaces*, 2026, https://arxiv.org/abs/2608.00010. Public date reported as 2026-06-19.
2. Iskander Azangulov, Aleksandr Smolensky, Andrey Terenin, Viacheslav Borovitskiy, *Stationary Kernels and Gaussian Processes on Lie Groups and their Homogeneous Spaces I: the compact case*, arXiv:2208.14960; https://arxiv.org/abs/2208.14960 (first publicly posted 2022-08-31).
3. Franziskus Steinert, Salem Said, Cyrus Mostajeran, *Universal kernels via harmonic analysis on Riemannian symmetric spaces*, arXiv:2506.19245, publicly posted 2025-06-24; https://arxiv.org/abs/2506.19245.
