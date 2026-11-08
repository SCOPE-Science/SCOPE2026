# Exact weighted dice volume and sharp radius-balancing stability

## Finding
Let \(D_{xy}\), \(D_{yz}\), and \(D_{zx}\) denote the unit Euclidean disks centered at the origin in the three coordinate planes of \(\mathbb R^3\). For any \(a,b,c\ge0\), let
\[
K(a,b,c)=aD_{xy}+bD_{yz}+cD_{zx},
\]
where addition means Minkowski sum. Write
\[
C=\sqrt2\,\pi^2\,{}_3F_2\left(\begin{matrix}-\tfrac14,\tfrac14,\tfrac12\\1,1\end{matrix};1\right)
\approx13.3727795244993670.
\]
Then the exact three-dimensional volume, including the boundary cases in which one disk is absent, is
\[
\operatorname{Vol}_3 K(a,b,c)=2\pi(a^2b+a^2c+b^2a+b^2c+c^2a+c^2b)+Cabc. \tag{1}
\]
If \(S=a+b+c>0\), write \(q=(a-S/3)^2+(b-S/3)^2+(c-S/3)^2\) and \(V_*=S^3(12\pi+C)/27\). The **sharp, global radius-balancing stability inequality** is
\[
V_*-\operatorname{Vol}_3 K(a,b,c)\ \ge\ \frac{S(2C-3\pi)}9\,q. \tag{2}
\]
Equality holds precisely at \((a,b,c)=(S/3,S/3,S/3)\) or at permutations of \((S/2,S/2,0)\). In particular, balanced positive radii uniquely maximize volume under fixed total radius. The volume is strictly Schur-concave as a function of the three radii on every fixed positive-sum simplex.

## Assumptions and scope
The disks are **solid** planar Euclidean unit disks, not the three-dimensional convex hull of their union. Each summand is allowed to have zero radius. Volume is ordinary three-dimensional Lebesgue measure in the ambient Euclidean space. The hypergeometric series is defined by
\[
{}_3F_2\left(\begin{matrix}-\tfrac14,\tfrac14,\tfrac12\\1,1\end{matrix};1\right)
=\sum_{j=0}^{\infty}\frac{(-1/4)_j(1/4)_j(1/2)_j}{(j!)^3},
\]
where \((x)_j=x(x+1)\cdots(x+j-1)\) and \((x)_0=1\). This series converges absolutely. There is no claim about differently oriented disks or non-circular cross-sections.

## Proof
**1. Disk decomposition into segments.** If \(v(\theta)=(\cos\theta,\sin\theta,0)\), the centered segment \([-v(\theta),v(\theta)]\) has support function \(|\langle u,v(\theta)\rangle|\). Since \(\int_0^{2\pi}|\langle u,v(\theta)\rangle|\,d\theta=4\sqrt{u_1^2+u_2^2}\), the planar disk is the Minkowski integral \(\frac14\int_0^{2\pi}[-v(\theta),v(\theta)]\,d\theta\). Analogous expressions hold for the other coordinate disks. For finitely many generators \(g_i\), the zonotope volume is exactly \(8\sum_{i<j<k}|\det(g_i,g_j,g_k)|\). Approximating the integrals by Riemann sums, using Hausdorff convergence of convex bodies and continuity of volume, gives the determinant-integral identity
\[
\operatorname{Vol}_3 K=\frac1{48}\sum_{i,j,k\in\{1,2,3\}}r_ir_jr_k
\int_{[0,2\pi]^3}|\det(v_i(\alpha),v_j(\beta),v_k(\gamma))|\,d\alpha\,d\beta\,d\gamma,
\]
where \((r_1,r_2,r_3)=(a,b,c)\) and \(v_i\) parametrizes the unit circle in the corresponding coordinate plane. The factor \(1/48=8/(3!\,4^3)\) accounts for unordered triples and segment normalization.

**2. Repeated-plane terms.** A determinant of three vectors in the same plane vanishes. If two vectors lie in the same plane and the third in a perpendicular coordinate plane, the absolute determinant has the form \(|\sin(\beta-\alpha)\sin\gamma|\), whose integral is \(32\pi\), since \(\int_0^{2\pi}\int_0^{2\pi}|\sin(\beta-\alpha)|\,d\alpha\,d\beta=8\pi\) and \(\int_0^{2\pi}|\sin\gamma|\,d\gamma=4\). The three orderings therefore give coefficient \(3(32\pi)/48=2\pi\) for each monomial \(r_i^2r_j\), \(i\ne j\).

**3. Three distinct planes.** For the choice \(v_1(\alpha)=(\cos\alpha,\sin\alpha,0)\), \(v_2(\beta)=(0,\cos\beta,\sin\beta)\), and \(v_3(\gamma)=(\sin\gamma,0,\cos\gamma)\), the determinant is a sum of two triple trigonometric products (the sign is immaterial after absolute values). Integrating \(\gamma\) first via \(\int_0^{2\pi}|A\cos\gamma+B\sin\gamma|d\gamma=4\sqrt{A^2+B^2}\), the six ordered terms yield
\[
C=\frac12\int_0^{2\pi}\int_0^{2\pi}
\sqrt{\cos^2\alpha\cos^2\beta+\sin^2\alpha\sin^2\beta}\,d\alpha\,d\beta.
\]
The square root equals \(\sqrt{(1+\cos(2\alpha)\cos(2\beta))/2}\). The moments of \(\cos(2\alpha)\), for uniform \(\alpha\), are zero in odd degree and \((1/2)_j/j!\) in degree \(2j\). Expanding the binomial series and integrating termwise gives precisely the hypergeometric expression above. Termwise integration is justified by absolute convergence at the endpoint (or by domination and passage from \(t<1\)). This proves (1).

**4. Strict balancing.** Denote the right-hand side of (1) by \(V(a,b,c)\). Its partial derivatives obey
\[
(a-b)(\partial_aV-\partial_bV)=-(a-b)^2[2\pi(a+b)+(C-4\pi)c]. \tag{3}
\]
The same holds cyclically. We establish \(4\pi<C<6\pi\). Every nonconstant hypergeometric summand \(t_j\) is negative, \(|t_1|=1/32\), and for \(j\ge1\),
\[
\frac{|t_{j+1}|}{|t_j|}
=\frac{(j-1/4)(j+1/4)(j+1/2)}{(j+1)^3}
\le\frac{j^2}{(j+1)^2}.
\]
Thus \(|t_j|\le1/(32j^2)\) and \(1-\pi^2/192<\sum_jt_j<1\). The elementary estimates \(\sqrt2>24/17\), \(3<\pi<\sqrt{10}<4\) imply \(4\pi<C<6\pi\). Therefore (3) is strictly negative for unequal coordinates on any simplex with \(S>0\); pairwise averaging strictly increases \(V\) unless the coordinates already coincide. This proves strict Schur-concavity and uniqueness of the balanced volume maximizer.

**5. Sharp global stability.** Put \(u=a-S/3\), \(v=b-S/3\), \(w=c-S/3\). Then \(u+v+w=0\), \(u,v,w\ge-S/3\), and direct expansion of (1) yields the *exact identity*
\[
V_*-V=\frac{CS}{6}(u^2+v^2+w^2)+(6\pi-C)uvw. \tag{4}
\]
We claim \(uvw\ge-S(u^2+v^2+w^2)/18\). This is automatic if the product is nonnegative. Otherwise, up to permutation, \(u,v>0\), \(w=-t\), \(u+v=t\le S/3\). Then \(uv\le t^2/4\) and \(u^2+v^2+w^2=2(t^2-uv)\ge3t^2/2\), so \(tuv/(u^2+v^2+w^2)\le t/6\le S/18\). Equality is possible only when \(u=v=t/2\) and \(t=S/3\). Substitution into (4), using \(6\pi-C>0\), proves (2). Equality occurs exactly at \((u,v,w)=(0,0,0)\) and permutations of \((S/6,S/6,-S/3)\), as claimed. The latter gives equality at the boundary, proving the coefficient in (2) is the largest possible uniform quadratic coefficient.

## Verification
A standalone script, `checks/dice_volume_check.py`, computes partial sums of the absolutely convergent hypergeometric series and independently approximates \(K(a,b,c)\) by Minkowski sums of **inscribed regular polygons**. Their volumes are computed using the *finite* zonotope determinant formula, not by evaluating the derived analytic volume polynomial. Successively finer polygon approximants approach the predicted volume from below, including two- and three-disk cases. The same script checks formula (2) at balanced, nonbalanced interior and sharp boundary configurations. Run with `python3 checks/dice_volume_check.py` using only Python's standard library. The calculations are finite corroboration; the five analytic steps above prove the general statements.

## Relationship to prior work
Mathis and Meroni introduced the three-coordinate-disk **dice** and evaluated the support of a *fiber body* in §5.3 of *Fiber Convex Bodies* (arXiv:2105.12406); their calculation involves a related angular expectation but does not state equation (1) or (2). Gesmundo and Meroni analyzed its algebraic boundary in §7 of *The Geometry of Discotopes* (arXiv:2111.01241), not its three-dimensional volume or extremal radii. Breiding, Bürgisser, Lerario and Mathis, *The zonoid algebra, generalized mixed volumes, and random determinants* (arXiv:2109.14996, Theorem 5.4), provide the **general** determinant/mixed-volume identity, which is a credited ingredient rather than the new result. The contribution is the evaluated triple-plane coefficient and complete sharp stability/equality classification for the natural weighted dice family; the general integral method itself is not new.

A similarly named calculation of the *convex hull* of three equal perpendicular disks concerns a different body. An unindexed equivalent formula or equivalent volume optimization may exist, so historical priority is provisional.

## Limitations
The disks are centered, circular, and in the three pairwise perpendicular coordinate planes. The formula does not extend without new mixed-volume calculations to arbitrary disk-plane orientations, translations or elliptical disks. The proof does not address surface area, volume minimization at fixed sum, or higher-dimensional analogues. Independent verification by another researcher has not occurred; the included review is same-model only.

## References
1. L. Mathis and C. Meroni, *Fiber Convex Bodies*, first public arXiv submission May 26, 2021, arXiv:2105.12406, §5.3, https://arxiv.org/abs/2105.12406 .
2. F. Gesmundo and C. Meroni, *The Geometry of Discotopes*, first public arXiv submission November 1, 2021, arXiv:2111.01241, §7, https://arxiv.org/abs/2111.01241 .
3. P. Breiding, P. Bürgisser, A. Lerario and L. Mathis, *The zonoid algebra, generalized mixed volumes, and random determinants*, first public arXiv submission September 30, 2021, arXiv:2109.14996, Theorem 5.4, https://arxiv.org/abs/2109.14996 .
