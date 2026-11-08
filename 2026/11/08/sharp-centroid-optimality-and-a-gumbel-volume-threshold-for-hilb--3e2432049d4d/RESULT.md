# Sharp centroid optimality and a Gumbel volume threshold for Hilbert balls in simplices

## Finding
For each integer \(n\ge2\), equip the interior of an arbitrary nondegenerate Euclidean \((n-1)\)-simplex with the Hilbert cross-ratio metric **without** a factor of \(1/2\). Let \(x=(x_1,\ldots,x_n)\) be its positive barycentric coordinates, and let \(Y\) be a point sampled uniformly by ambient Euclidean volume on the simplex. For \(r>0\) put \(c=e^r-1\). The exact normalized Euclidean mass of the radius-\(r\) ball is
\[
Q_n(x,r):=\Pr\{d_H(x,Y)\le r\}=\frac{1+c}{c}\int_0^\infty e^{-s}\prod_{i=1}^{n}(1-e^{-c x_i s})\,ds.
\]
Equivalently this is the finite rational expression
\[
Q_n(x,r)=\frac{1+c}{c}\sum_{A\subseteq\{1,\ldots,n\}}\frac{(-1)^{|A|}}{1+c\sum_{i\in A}x_i}.
\]
For each fixed radius, the mass is **strictly Schur-concave** in the positive barycentric center. Thus the centroid \(b_n=(1/n,\ldots,1/n)\) is the unique center giving maximal Euclidean-ball volume, and the sharp mass is
\[
\max_{x\in\operatorname{int}S}Q_n(x,r)=Q_n(b_n,r)=\frac{n}{c}\,B\left(\frac{n}{c},n\right).
\]
At any fixed interior center, \(Q_n(x,r)\sim n!\,r^{n-1}\prod_i x_i\) as \(r\downarrow0\). In increasing dimension, the maximal-volume center has the exact fluctuation law
\[
\Pr\{d_H(b_n,Y_n)\le\log n+\log\log n+t\}\longrightarrow\exp(-e^{-t})
\]
for every fixed real \(t\), where \(Y_n\) is uniform in a simplex with \(n\) vertices.

## Assumptions and scope
The simplex is nondegenerate, in any ambient Euclidean embedding of affine dimension \(n-1\), and the probability measure is **normalized Euclidean Lebesgue volume**. This is not the (generally infinite on the whole simplex) Busemann or Holmes–Thompson Hilbert-geometric volume. The center is strictly interior; no Hilbert distances to boundary points are asserted. The Hilbert metric is the logarithm of the cross-ratio, without an additional factor of \(1/2\). Barycentric coordinates sum to one. All assertions hold for every integer \(n\ge2\) and radius \(r>0\); the Gumbel law is an asymptotic statement as the number of vertices tends to infinity.

## Proof
**1. Explicit projective distance.** An affine bijection between the given simplex and the standard probability simplex preserves cross-ratios and normalized Euclidean volume. Write \(x_i>0,y_i>0\), with each coordinate sum one, and set \(q_i=y_i/x_i\). Along the line \(z(\tau)=x+\tau(y-x)\), the boundary intersection parameters are \(\tau_-=1/(1-\max_i q_i)<0\) and \(\tau_+=1/(1-\min_i q_i)>1\), apart from the trivial case \(x=y\). The cross-ratio of \(\tau_-,0,1,\tau_+\) simplifies to \(\max_i q_i/\min_i q_i\). Therefore
\[
d_H(x,y)=\log\frac{\max_i(y_i/x_i)}{\min_i(y_i/x_i)}.
\]

**2. Exponential representation and exact integral.** For independent exponential variables \(E_1,\ldots,E_n\) of unit rate, \(Y_i=E_i/\sum_jE_j\) is uniform on the simplex. The variables \(Z_i=E_i/x_i\) are independent exponentials with respective rates \(x_i\). Their common denominator cancels in the max/min ratio, so the ball event is \(\max_iZ_i\le(1+c)\min_iZ_i\). If the minimum occurs at index \(i\) with value \(s\), its contribution is
\[
\int_0^\infty x_i e^{-s}\prod_{j\ne i}(1-e^{-c x_js})\,ds.
\]
Let \(P(s)=\prod_i(1-e^{-c x_i s})\). The sum of the integrands, with the factor \(e^{-s}\) removed, is \(P(s)+P'(s)/c\), because \(\sum_i x_i=1\). Integration by parts and \(P(0)=0\) yield the asserted \((1+c)/c\) integral. Expanding \(P(s)\) and integrating term by term proves the finite subset-sum formula.

**3. Sharp center by majorization.** For each fixed \(s,c>0\), the function \(u\mapsto\log(1-e^{-csu})\) on \(u>0\) has second derivative
\[
-\frac{(cs)^2 e^{csu}}{(e^{csu}-1)^2}<0.
\]
By strict Karamata, if a barycentric vector \(x\) majorizes another vector \(z\), then \(\prod_i(1-e^{-csx_i})\le\prod_i(1-e^{-csz_i})\), with strict inequality unless the vectors differ only by permutation. Integrating proves strict Schur-concavity. Every probability vector majorizes the uniform vector; equality of its ball mass with the uniform-center mass therefore forces \(x_i=1/n\) for all \(i\). At the centroid substitute \(u=e^{-cs/n}\) into the exact integral, giving
\[
\frac{n(1+c)}{c^2}B(n/c,n+1)=\frac{n}{c}B(n/c,n),
\]
where the last step is the beta recurrence.

**4. Short-radius coefficient.** As \(r\downarrow0\), \(c\sim r\), and \((1-e^{-c x_i s})/(c x_i s)\to1\). Since these ratios lie in \([0,1]\), dominated convergence against \(e^{-s}s^n\) gives \(\int_0^\infty e^{-s}\prod_i(1-e^{-cx_is})ds\sim c^n n!\prod_i x_i\), establishing the coefficient.

**5. Dimensional threshold.** At the centroid, the Hilbert radius is \(D_n=\log(M_n/m_n)\), where \(M_n=\max_i E_i\) and \(m_n=\min_i E_i\) for independent unit-rate exponentials. The elementary identities \(\Pr(M_n\le u)=(1-e^{-u})^n\) for \(u\ge0\) and \(n m_n\overset{d}=\operatorname{Exp}(1)\) give \(M_n/\log n\to1\) in probability and
\[
D_n-\log n-\log\log n=\log(M_n/\log n)-\log(nm_n)\Longrightarrow-\log E,
\]
where \(E\) is unit-rate exponential. Its CDF is \(\Pr(-\log E\le t)=e^{-e^{-t}}\). Joint independence of the minimum and maximum is not assumed.

## Verification
The included executable `check.py` evaluates the exact integral by adaptive quadrature, compares it to independent exponential-sample simulations of uniformly distributed barycentric points, verifies the beta function at the centroid across dimensions \(n=2,\ldots,10\), numerically checks strict balancing and the small-radius coefficient, and compares finite-dimensional central laws with the stated Gumbel limit. The script prints `HILBERT_SIMPLEX_EUCLIDEAN_BALL_MASS_OK` on success. The analytic proof does not depend on these finite computations. Reproduce with `python check.py` after installing `numpy` and `scipy` as specified in `requirements.txt`.

## Relationship to prior work
The classical Hilbert-simplex isometry is due to earlier work cited by Foertsch–Karlsson (2004). Nielsen–Sun (2017) gives the efficient distance formula and depicts simplex Hilbert balls, while Nielsen–Shao (2017) proves their polygonal shape and facet properties. Vernicos (2012, 2014) studies **Hilbert-geometric** Busemann or Holmes–Thompson volume growth, not normalized Euclidean mass of fixed-radius balls. The present result instead supplies an exact Euclidean mass functional for every center, its strict majorization ordering and optimal centroid, and the high-dimensional volume quantile threshold. Standard exponential order statistics supply the last asymptotic step but do not alone imply the positional Euclidean-ball-volume theorem.

## Limitations
The theorem is restricted to simplex domains, normalized Euclidean (not intrinsic Finsler) sampling, and the specified metric normalization. It does not assert a centroid extremum for non-simplex domains, for general sampling densities or for intrinsic Hilbert volume. The asymptotic Gumbel law concerns centroid-anchored distances rather than distances between two independent random points. Historical-priority uncertainty from unindexed geometric probability literature remains possible; independent audit has not been performed.

## References
- T. Foertsch and A. Karlsson, *Hilbert metrics and Minkowski norms*, arXiv:math/0407197, first public version 12 July 2004; especially Theorems 1–2.
- C. Vernicos, *Asymptotic volume in Hilbert Geometries*, arXiv:1207.1142, 4 July 2012; Busemann volume in Theorem 2.
- C. Vernicos, *On the Hilbert Geometry of Convex Polytopes*, arXiv:1406.0733, 3 June 2014; §§5–6.
- F. Nielsen and K. Sun, *Clustering in Hilbert simplex geometry*, arXiv:1704.00454, 3 April 2017; §3, distance and ball descriptions.
- F. Nielsen and L. Shao, *On Balls in a Hilbert Polygonal Geometry*, SoCG 2017 multimedia contribution, DOI:10.4230/LIPIcs.SoCG.2017.67; §§2–3.
