# Two covariance-anisotropy reversals for complete-split stable-set polytopes

## Finding
Let \(p,q\ge2\) be integers, let \(G_{p,q}=K_p\vee\overline{K_q}\) (a clique of size \(p\) completely joined to an independent set of size \(q\)), and let \(P_{p,q}=\operatorname{STAB}(G_{p,q})\subset\mathbb R^{p+q}\) in standard orthonormal indicator coordinates. Let \(C_{\mathrm v}\) be the covariance of a uniformly selected **distinct vertex** of this polytope, and \(C_{\mathrm{vol}}\) the covariance of a Euclidean-volume-uniform point. Both are positive definite. Write \(\kappa_{\mathrm v}\) and \(\kappa_{\mathrm{vol}}\) for their largest-to-smallest eigenvalue ratios.

Define \(t=2^q\), \(N=p+t\), \(D=p+q+1\), and
\[
T=(q+1)p+t+4,\qquad U=(4q+2)p+(q+1)(q+2)+12.
\]
Then the two exact condition numbers are determined without diagonalizing a large matrix by
\[
\kappa_{\mathrm v}+2+\kappa_{\mathrm v}^{-1}=\frac{T^2}{4N},\qquad
\kappa_{\mathrm{vol}}+2+\kappa_{\mathrm{vol}}^{-1}=\frac{U^2}{12(q+2)D}.
\]
For either equation the intended solution has \(\kappa>1\). Put
\[
F_q(p)=3(q+2)(p+q+1)((q+1)p+2^q+4)^2
 -(p+2^q)((4q+2)p+(q+1)(q+2)+12)^2.
\]
For all integer \(p,q\ge2\),
\[
\operatorname{sgn}(\kappa_{\mathrm v}-\kappa_{\mathrm{vol}})
=\operatorname{sgn}F_q(p).
\]
For \(q=2\), the vertex measure is strictly more anisotropic for all \(p\ge2\). For \(q=3\), equality occurs at precisely \(p=2\), and otherwise the vertex measure is more anisotropic. For every \(q\ge4\), the cubic \(F_q\) has exactly two distinct positive real roots \(2<r_1(q)<r_2(q)\), and
\[
\begin{array}{ll}
\kappa_{\mathrm v}<\kappa_{\mathrm{vol}}&\text{for }r_1(q)<p<r_2(q),\\
\kappa_{\mathrm v}>\kappa_{\mathrm{vol}}&\text{for }2\le p<r_1(q)\text{ or }p>r_2(q),
\end{array}
\]
with equality at integer boundary roots, if present. For example, at \(q=4\), the reverse-ordering interval contains exactly \(p=4,5\), and equality holds at \(p=6\). Thus the direction of the sampling-anisotropy comparison reverses twice as the clique size grows.

The transition roots have sharp exponential asymptotics
\[
\lim_{q\to\infty}\frac{q r_1(q)}{2^q}=\frac13,
\qquad \lim_{q\to\infty}\frac{q r_2(q)}{2^q}=3.
\]
More generally, for any integer sequence \(p=p(q)\ge2\) with \(qp/2^q\to c\in(0,\infty)\),
\[
\frac{\kappa_{\mathrm v}}{\kappa_{\mathrm{vol}}}
\longrightarrow\frac{3(1+c)^2}{16c},
\]
which is less than one precisely when \(1/3<c<3\). For fixed \(p\) and growing \(q\), the ratio instead obeys \(\kappa_{\mathrm v}/\kappa_{\mathrm{vol}}\sim3\,2^q/q^2\); for fixed \(q\) and growing \(p\), it tends to \(3(q+1)^2(q+2)/(4(2q+1)^2)>1\).

## Assumptions and scope
The graph is finite and simple, and \(p,q\) are independent integers at least two. All distances, inner products and covariance eigenvalues use the **ambient standard Euclidean metric** on \(\mathbb R^{q+p}\), in which \(P_{p,q}\) is full-dimensional. The vertex law assigns equal mass to all \(2^q+p\) distinct zero–one vertices, including the empty stable set; the volume law is normalized \((p+q)\)-dimensional Lebesgue measure on the polytope. The condition number is the ratio of positive extreme covariance eigenvalues, not a ratio of polytope in- and circumradii.

## Proof
**Step 1: Geometry and exact laws.** Order the independent coordinates first, and call them \(x\in\mathbb R^q\); write the clique coordinates as \(y\in\mathbb R^p\). Stable sets are either arbitrary subsets of the independent class or one clique vertex. Therefore
\[
P_{p,q}=\operatorname{conv}\left(([0,1]^q\times\{0\})\cup\{(0,e_j):1\le j\le p\}\right)
=\{(x,y):y\ge0,\ t_y=\sum_jy_j\le1,\ 0\le x_i\le1-t_y\}.
\]
Every listed binary point is an extreme vertex (its own exposing coordinate functional suffices, or use extremality of every zero–one point in a zero–one hull). For the volume law, the section with \(t_y=t\) has cube factor \((1-t)^q\) and simplex radial factor \(t^{p-1}\). Hence \(T_y:=\sum_jY_j\) has \(\operatorname{Beta}(p,q+1)\) distribution. Conditionally, one may write
\[
X_i=(1-T_y)U_i,\qquad (Y_1,\ldots,Y_p)=T_y V,
\]
where \(U_i\) are independent uniform variables on \([0,1]\), \(V\) is uniform on the probability simplex (Dirichlet with \(p\) unit parameters), and \(T_y,U,V\) are mutually independent. Consequently, writing \(\sigma_T^2=\operatorname{Var}(T_y)=p(q+1)/(D^2(D+1))\), define
\[
a=\frac{(q+1)(q+2)}{12D(D+1)},\qquad b=\frac1{D(D+1)}.
\]
The independent-coordinate contrast eigenspace has eigenvalue \(a\) with multiplicity \(q-1\), and the clique-coordinate contrast eigenspace has eigenvalue \(b\) with multiplicity \(p-1\). On the orthonormal span of the two block-constant vectors, the covariance is
\[
M_{\mathrm{vol}}=\begin{pmatrix}
 a+q\sigma_T^2/4&-\sqrt{q/p}\,\sigma_T^2/2\\
 -\sqrt{q/p}\,\sigma_T^2/2&\sigma_T^2/p
\end{pmatrix}.
\]
Its determinant is \(a\sigma_T^2/p>0\). Its greater eigenvalue is larger than \(a\ge b\), and its smaller eigenvalue is less than \(\sigma_T^2/p<b\). Thus the covariance condition number is the eigenvalue ratio of this matrix. For any positive definite two-by-two matrix with extreme eigenvalue ratio \(\kappa\), one has \((\operatorname{tr}M)^2/\det M=\kappa+2+\kappa^{-1}\); substitution and cancellation give the displayed volume formula.

**Step 2: Vertex law.** Set \(u=2^{q-2}\), so \(N=p+4u\). The independent-coordinate first and off-diagonal second moments are \(2u/N\) and \(u/N\); each clique coordinate has mean and second moment \(1/N\), and two different clique coordinates, or one clique and one independent coordinate, never co-occur. Thus the contrast eigenvalues are \(u/N\) (multiplicity \(q-1\)) and \(1/N\) (multiplicity \(p-1\)). On the orthonormal block-constant span the covariance is
\[
M_{\mathrm v}=\begin{pmatrix}
\dfrac{u((q+1)p+2^q)}{N^2}&-\dfrac{\sqrt{pq}\,2^{q-1}}{N^2}\\
-\dfrac{\sqrt{pq}\,2^{q-1}}{N^2}&\dfrac{2^q}{N^2}
\end{pmatrix}.
\]
The determinant equals \(2^{2q-2}/N^3>0\). Its greater eigenvalue exceeds its upper-left diagonal, which exceeds \(u/N\ge1/N\), and its smaller eigenvalue lies below its lower-right diagonal \(2^q/N^2<1/N\). Hence the full covariance extreme eigenvalues are those of \(M_{\mathrm v}\), and the same two-by-two identity yields \(T^2/(4N)\).

**Step 3: Exact comparison and root count.** For \(z>1\), the map \(z\mapsto z+2+z^{-1}\) is strictly increasing. Cross-multiplying the two positive expressions in Step 2 and Step 1 proves that the condition-number difference has the sign of \(F_q(p)\). Direct algebra gives
\[
F_2(p)=4p^2(2p+5),\qquad F_3(p)=4(p-2)^2(11p+28).
\]
For \(q\ge4\), write \(t=2^q\ge q^2\). The leading coefficient of \(F_q\), considered as a cubic in real \(p\), is \((q-1)^2(3q+2)>0\). It obeys
\[
F_q(0)=(3t-(q+1)(q+2))\bigl((q+1)(q+2)t-48\bigr)>0,
\]
\[
F_q(2)=-(q+2)(q^2+5q-3t)\bigl((q+3)t-10q-18\bigr)>0.
\]
To check the crucial negative evaluation, put
\[
A=q(q+1)(q+2)-(2q+1)t,
\]
\[
B=-(2q+1)(q-2)t^2+(q^4+4q^3-19q^2+2q)t-48q^2.
\]
One obtains \(F_q(t/q)=-AB/q^3\). From \(t\ge q^2\) and \(q\ge4\), we have \(A<0\), while
\[
B\le -t\,[q^4-7q^3+17q^2-2q]-48q^2<0.
\]
The last inequality uses \(q^3-7q^2+17q-2>0\) for \(q\ge4\) (its derivative is everywhere positive and its value at four is positive). Hence \(F_q(t/q)<0\), and \(2<t/q\). By continuity, the sign of a cubic at negative infinity, zero, two, \(t/q\), and positive infinity forces exactly one negative real root and two distinct roots \(2<r_1(q)<t/q<r_2(q)\). Their sign intervals are as claimed. For \(q=4\), factorization is \(F_4(p)=18(p-6)(7p^2-5p-72)\), giving the example.

**Step 4: Asymptotic thresholds.** Fix \(c>0\) and put \(p=c2^q/q+o(2^q/q)\). With \(t=2^q\), one has
\[
\frac1t\frac{T^2}{4N}\longrightarrow\frac{(1+c)^2}{4},\qquad
\frac1t\frac{U^2}{12(q+2)D}\longrightarrow\frac{4c}{3}.
\]
Both limits are positive, so both condition numbers tend to infinity and are asymptotic to their corresponding displayed trace-determinant expressions. Their ratio converges to \(3(1+c)^2/(16c)\), with strict sign change at \(c=1/3,3\). The root count in Step 3 plus continuity of these limiting signs on compact \(c\)-intervals proves the two sharp root limits. If \(p\) is fixed and \(q\) grows, the two condition numbers are asymptotic to \(2^q/4\) and \(q^2/12\). If \(q\) is fixed and \(p\) grows, they are asymptotic to \((q+1)^2p/4\) and \((2q+1)^2p/[3(q+2)]\), respectively. The latter ratio is strictly greater than one since \(3(q+1)^2(q+2)-4(2q+1)^2=(q-1)^2(3q+2)>0\).

## Verification
The dependency-free program `artifacts/verify.py` independently enumerates all distinct vertices for the small parameter grid, uses exact rational arithmetic to check every covariance entry, verifies trace/determinant and comparison identities over a broad additional parameter grid, and tests integer boundary identities. It reports `SPLIT_VERTEX_VOLUME_COVARIANCE_CHECKS_PASSED`. The optional `artifacts/verify_triangulation.py` constructs simplicial triangulations of four low-dimensional examples and integrates polynomial moments exactly over each simplex, independently reproducing the volume-covariance matrices. The full infinite-family claim and both root limits follow from the analytical argument; finite programs do not substitute for it.

## Relationship to prior work
Stable-set polytopes and their edge structure are studied by Aliniaeifard, Benedetti, Bergeron, Li, and Saliola (first released 2018), and perfect-graph stable-set polytope descriptions and extension complexity by Hu and Laurent (first released 2017). These establish the relevant polytope framework and vertices/facets, not a comparison of covariance condition numbers for two sampling laws. General results on minimum enclosing spheres, inballs, or John ellipsoids concern different extremal geometry; their conclusions do not imply covariance of a uniformly sampled *vertex* and of a uniformly sampled *volume point*. The precise two-reversal phase and the constants \(1/3\) and \(3\) are the specific contribution claimed here.

## Limitations
The comparison is for Euclidean covariance condition number only and for the canonical coordinate realization; arbitrary affine changes of coordinates do not preserve it. The two real boundary roots need not be integers, so finite integer equality cases are not classified beyond those explicitly given. No claim is made that all volume/vertex moment formulas for iterated pyramids are previously unknown, and historical priority of equivalent formulations remains open to external review. No independent mathematical audit has been performed.

## References
1. H. Hu and M. Laurent, *On the Linear Extension Complexity of Stable Set Polytopes for Perfect Graphs*, arXiv:1706.05496, first publicly submitted 2017-06-17; https://arxiv.org/abs/1706.05496 .
2. F. Aliniaeifard, C. Benedetti, N. Bergeron, S. X. Li and F. Saliola, *Stable set polytopes and their 1-skeleta*, arXiv:1804.00360, first publicly submitted 2018-04-02; https://arxiv.org/abs/1804.00360 .
