# Sharp spherical deep-hole tails for Johnson hypersimplex codes

## Finding

For integers \(N\ge3\) and \(1\le k\le N-1\), define the zero-sum Euclidean hyperplane
\[
H_N=\{x\in\mathbb R^N:\textstyle\sum_i x_i=0\},\qquad
r_{N,k}=\sqrt{k(N-k)/N},
\]
and the normalized Johnson (hypersimplex-vertex) spherical code
\[
\mathcal J_{N,k}=\left\{u_S=\frac{\mathbf1_S-(k/N)\mathbf1}{r_{N,k}}:\ S\subset\{1,\dots,N\},\ |S|=k\right\}\subset S(H_N).
\]
Let \(X\) be uniform on the unit sphere \(S(H_N)\cong S^{N-2}\), and set
\[
T(X)=\max_{|S|=k}\langle X,u_S\rangle,\qquad R(X)=\arccos T(X).
\]
Put \(s=\min(k,N-k)\), \(m=N-1\), and
\[
c=\frac{s}{\sqrt{(N-1)k(N-k)}},\qquad \rho=\arccos c.
\]
The exact spherical covering radius of \(\mathcal J_{N,k}\) is \(\rho\). All points at that maximal angular distance are the \(N\) vectors
\[
-\frac{e_i-\mathbf1/N}{\sqrt{(N-1)/N}}\ (k<N/2),\qquad
+\frac{e_i-\mathbf1/N}{\sqrt{(N-1)/N}}\ (k>N/2),
\]
for \(1\le i\le N\); at \(2k=N\), *both* displayed orbits occur (\(2N\) points, necessarily distinct).

More strongly, the exact leading small-probability law for a Haar-uniform direction nearly attaining the covering radius is
\[
\Pr\{T(X)\le c+\varepsilon\}
=C_{N,k}\varepsilon^{N-2}+O_{N,k}(\varepsilon^{N-1})\qquad(\varepsilon\downarrow0),
\]
where, with \(h_{N,k}=2N\) at \(2k=N\) and \(h_{N,k}=N\) otherwise,
\[
C_{N,k}=\frac{h_{N,k}\,r_{N,k}^{N-2}}{|S^{N-2}|}
\frac{\sqrt{N-1}(N-1)^{N-2}}{s!\,(N-2-s)!\,(N-1-s)^s\,s^{N-2-s}},
\]
and \(|S^{N-2}|=2\pi^{(N-1)/2}/\Gamma((N-1)/2)\). In angular form,
\[
\Pr\{R(X)\ge\rho-\delta\}
=C_{N,k}(\sin\rho)^{N-2}\delta^{N-2}+O_{N,k}(\delta^{N-1})
\qquad(\delta\downarrow0).
\]
For example, the six-site octahedral code \(\mathcal J_{4,2}\) has \(c=1/\sqrt3\), eight deep holes and \(C_{4,2}=9\sqrt3/\pi\). The ten-site \(\mathcal J_{5,2}\) has \(c=1/\sqrt6\), five deep holes and \(C_{5,2}=20(6/5)^{3/2}/\pi^2\).

## Assumptions and scope

The probability is normalized spherical surface area on the unit sphere of \(H_N\); it is not uniform volume in the hypersimplex. Euclidean inner products and all distances are taken in the induced metric of \(H_N\). The asymptotic parameter is \(\varepsilon\downarrow0\), with \(N,k\) fixed. All ranks, including \(k=1\), \(k=N-1\), and the balanced rank \(2k=N\), are included. The inequality inside the probability may be strict without changing its value for sufficiently small positive \(\varepsilon\), because the distribution has no atoms near \(c\).

## Proof

**1. Facets and covering radius.** The convex hull of the unnormalized code points is the centered hypersimplex
\[
P_{N,k}=\{z\in H_N:-k/N\le z_i\le1-k/N\ \text{for all }i\}.
\]
For \(k=1\) or \(k=N-1\), redundant inequalities may be dropped. The Euclidean distance within \(H_N\) from the origin to the plane \(z_i=a\) is \(|a|\sqrt{N/(N-1)}\). Consequently the minimum support value of the normalized polytope \(P_{N,k}/r_{N,k}\), over unit normal directions, equals its centered inradius
\[
\min_{\|x\|=1}\max_{|S|=k}\langle x,u_S\rangle=c.
\]
Every minimizing support hyperplane is a facet plane at the smallest distance from zero; all such facet planes have precisely the normal vectors listed in the Finding. There are no additional deep holes: a supporting hyperplane at the minimal distance defines a contact plane of the maximal centered ball, and hence must coincide with a nearest facet hyperplane. This also establishes the \(N\)-versus-\(2N\) orbit count.

**2. Tangent model.** Fix an active hole \(a_i\), and write neighboring sphere points uniquely as
\[
x(z)=\frac{a_i+z}{\sqrt{1+\|z\|^2}},\quad z\in H_N,\ z_i=0,\quad\|z\|\text{ small}.
\]
The tangent subspace is canonically \(H_m\) on the remaining \(m=N-1\) coordinates. At a hole corresponding to a lower coordinate facet, exactly those sites with \(i\notin S\) maximize the inner product. At an upper facet, exactly the sites with \(i\in S\) maximize it. All other sites remain strictly submaximal in one neighborhood of the hole. Thus locally
\[
T(x(z))=\frac{c+r_{N,k}^{-1}F(z)}{\sqrt{1+\|z\|^2}},
\]
where \(F(z)\) is either \(\max_{|S|=k}\sum_{j\in S}z_j\) on the remaining \(m\) coordinates or the corresponding maximum over \((k-1)\)-subsets. Since \(\sum_j z_j=0\), complementing and replacing \(z\) by \(-z\) reduces either case to \(F_s(z)=\max_{|S|=s}\sum_{j\in S}z_j\), with \(s=\min(k,N-k)\).

Define the \((m-1)\)-dimensional polar-type polytope
\[
Q_{m,s}=\{y\in H_m:F_s(y)\le1\}.
\]
Since the centered rank-\(s\) hypersimplex contains zero in its interior, \(Q_{m,s}\) is bounded and \(F_s(z)\ge\lambda\|z\|\) for some \(\lambda>0\). Therefore the event \(T(x(z))\le c+\varepsilon\) in a hole neighborhood forces \(\|z\|=O(\varepsilon)\). Substituting \(z=r_{N,k}\varepsilon y\) shows its rescaled domain lies between \((1-O(\varepsilon))Q_{m,s}\) and \((1+O(\varepsilon))Q_{m,s}\). The spherical Jacobian of this central chart is \((1+\|z\|^2)^{-(N-1)/2}\); hence the surface area contributed by one hole is
\[
(r_{N,k}\varepsilon)^{m-1}\operatorname{Vol}_{m-1}(Q_{m,s})+O_{N,k}(\varepsilon^m).
\]
By compactness, all points with \(T\le c+\varepsilon\) lie in disjoint such neighborhoods for sufficiently small \(\varepsilon\). Summing over \(h_{N,k}\) holes and dividing by \(|S^{N-2}|\) proves the probability exponent and reduces its coefficient to the following exact volume.

**3. Exact volume of the tangent polar.** Partition \(H_m\) into \(m!\) congruent coordinate-order chambers. In the chamber \(y_1\ge\cdots\ge y_m\), set \(d_j=y_j-y_{j+1}\ge0\), \(1\le j\le m-1\). Then
\[
\sum_{i=1}^s y_i=\sum_{j=1}^{m-1}a_jd_j,\quad
a_j=\begin{cases}j(m-s)/m&j\le s,\\s(m-j)/m&j\ge s.\end{cases}
\]
The basis vectors for these difference coordinates are the fundamental zero-sum weights \(b_j=\mathbf1_{[j]}-(j/m)\mathbf1\), whose Gram determinant is \(1/m\). Thus the Euclidean Jacobian is \(1/\sqrt m\). The ordered intersection of \(Q_{m,s}\) is the coordinate simplex \(d_j\ge0\), \(\sum a_jd_j\le1\). Its volume is \((\sqrt m(m-1)!\prod a_j)^{-1}\). Multiplication by \(m!\) yields
\[
\operatorname{Vol}_{m-1}(Q_{m,s})=\frac{\sqrt m}{\prod_{j=1}^{m-1}a_j}
=\frac{\sqrt m\,m^{m-1}}{s!\,(m-1-s)!\,(m-s)^s\,s^{m-1-s}}.
\]
This gives the stated coefficient. Finally \(\cos(\rho-\delta)=c+\sin\rho\,\delta+O(\delta^2)\), proving the angular equivalent.

## Verification

The included standalone `verify.py` reconstructs centered hypersimplex vertices and their convex-hull facet distances in orthonormal coordinates for \(3\le N\le7\), checks the support values at all predicted hole orbits, and compares 1,000s of random directions with the theoretical threshold. It also reconstructs the tangent polar polytope by halfspace intersection and independently integrates its convex-hull volume for \(3\le m\le6\), all ranks. It completed 154 structured checks with assertions passing. These finite computations test, but do not replace, the general proof. Run with `OPENBLAS_NUM_THREADS=1 python verify.py` using Python 3, NumPy, and SciPy.

## Relationship to prior work

Hyunjun Yi (2026) establishes the role of regular-simplex edge midpoints \(\mathcal J(N,2)\) in extremal two-distance and isosceles configurations, motivating a new geometric-probability question on these fixed spherical codes. Jevtić, Timotijević, and Živaljević (2025) study hypersimplex deformation cones and normal fans; their facet description is consistent with the first covering-radius step. Neither inspected paper establishes a Haar near-deep-hole probability coefficient. The spherical covering radius alone is an elementary consequence of hypersimplex facets and is not isolated as the purported advance; the all-rank exact factorial tail coefficient and its orbit-sensitive sharp exponent constitute the new claim. Priority over unindexed or alternate formulations has not been independently confirmed.

## Limitations

The result is a near-endpoint asymptotic for a fixed finite code, not the full distribution of \(T\) or a uniform-in-dimension estimate. The \(O_{N,k}\)-constant may depend on \(N,k\). The proof does not assert an improved optimal covering configuration among all spherical codes, nor independent validation of novelty. General near-contact support-function arguments may provide related exponent laws; the factorial coefficient has to be compared with any broader such theorems if identified.

## References

- H. Yi, *Isosceles sets and two-distance sets in Euclidean space*, arXiv:2611.05421, first submitted 2 November 2026, https://arxiv.org/abs/2611.05421 ; inspected v2 full text https://arxiv.org/html/2611.05421v2 .
- F. D. Jevtić, M. Ž. Timotijević and R. T. Živaljević, *Indecomposability of the median hypersimplex and polytopality of the hemi-icosahedral Bier sphere*, arXiv:2504.21345, first submitted 30 April 2025, https://arxiv.org/html/2504.21345v1 .
