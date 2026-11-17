# Majority-cluster screening and incenter collapse in two-cluster ultrametric free spaces

## Finding
Let \(2\le p\le q\) be integers, and let \(0<s,t<1\). Partition a finite set \(M=A\sqcup B\), with \(|A|=p\) and \(|B|=q\), and give it distances \(s\) between distinct points of \(A\), \(t\) between distinct points of \(B\), and \(1\) between points in different clusters. Let \(K\) be the unit ball of the real Lipschitz-free space over \(M\), represented in the canonical Euclidean hyperplane of signed masses of total sum zero. Put \(N=p+q\), and define
\[
H_{p,q,t}(j)=\frac{pq}{N}+t\left(t-\frac{2p}{N}\right)j-\frac{t^2}{N}j^2\qquad(0\le j\le q-1).
\]
Then the **globally optimal Euclidean inradius**, in the unrescaled ambient coordinate metric, is
\[
\boxed{r(K)=\left(\max_{0\le j\le q-1}H_{p,q,t}(j)\right)^{-1/2}.}
\]
In particular, the radius is **independent of the entire minority-cluster distance \(s\)**, even though the polytope and its individual facets depend on \(s\).

Define \(\alpha=N/2-p/t\), and let \(J\subseteq\{0,\ldots,q-1\}\) be the one or two integers nearest to \(\alpha\), with clipping to the displayed range. Exactly
\[
\boxed{2\sum_{j\in J}\binom qj}
\]
facets touch the maximal ball centered at the origin. If \(\mathcal C\) denotes the set of centers of **all** Euclidean balls in \(K\) having this maximal radius, then
\[
\boxed{\dim\operatorname{aff}\mathcal C=
\begin{cases}N-2,&J=\{0\},\\ p-1,&J\ne\{0\}.
\end{cases}}
\]
For \(q\ge p+2\), the sharp collapse of optimal-center dimension occurs **at** \(t=2p/(N-1)\). Below that parameter the inball has exactly two tangent facets, squared inverse radius \(pq/N\), and center dimension \(N-2\). At the transition it has \(2(q+1)\) tangent facets and center dimension \(p-1\); above it the center dimension stays \(p-1\), with an explicitly computable binomial contact staircase. If \(q=p\) or \(q=p+1\), the two-contact regime persists throughout \(0<t<1\). The incenter is never unique because \(p\ge2\).

## Assumptions and scope
All scalar spaces are real. The metric inequalities are valid because \(0<s,t<1\) and each cross-cluster distance equals one. Write \(e_z\) for a standard coordinate vector and
\[
E=\{\mu\in\mathbb R^M:\sum_{z\in M}\mu_z=0\},\qquad
K=\operatorname{conv}\left\{\frac{e_x-e_y}{d(x,y)}:x\ne y\in M\right\}\subset E.
\]
Euclidean lengths mean the restriction of the usual coordinate inner product to \(E\), not a Banach--Mazur-optimized or group-rescaled Hilbert norm. Let \(\Pi f=f-N^{-1}\sum_z f(z)\mathbf1\) denote centering. The Euclidean polar of \(K\) in \(E\) is the centered Lipschitz ball
\[
K^\circ=\{\Pi f:\ |f(u)-f(v)|\le d(u,v)\ \forall u,v\in M\}.
\]
Every vertex \(v\) of the polar corresponds to the facet \(\langle v,\mu\rangle=1\) of \(K\), at Euclidean distance \(1/\|v\|_2\) from zero.

## Proof
**1. Exact polar-vertex classification.** For a feasible potential \(f\), join two vertices of \(M\) by an edge whenever \(|f(u)-f(v)|=d(u,v)\). The active incidence normals span \(E\) exactly when this *tight-edge graph* is connected. Thus a centered potential is a polar vertex precisely when its tight-edge graph is connected: disconnected components permit independent small translations, and a connected spanning set of tight equalities fixes all potential differences.

A connected tight graph must contain a cross-cluster edge. Orient one such tight edge to have an \(A\)-endpoint at level zero and a \(B\)-endpoint at level one. All other \(A\)-levels lie in \([0,s]\), and all other \(B\)-levels lie in \([1-t,1]\), by within-cluster and cross inequalities. A cross edge can be tight only between levels zero in \(A\) and one in \(B\): any potential cross edge in the opposite orientation has difference at most \(s+t-1<1\). An \(A\)-point that is not at zero can therefore connect to the tight graph only through an intra-\(A\) edge to level zero, forcing its level to be exactly \(s\). Similarly, a \(B\)-point not at level one must be at level \(1-t\). The admissible extreme potentials are therefore, up to simultaneous reversal of signs,
\[
f|_A\in\{0,s\}^{A},\quad f|_B\in\{1-t,1\}^{B},\quad
\#\{a\in A:f(a)=0\}\ge1,\quad
\#\{b\in B:f(b)=1\}\ge1.
\]
Conversely, the zero and one anchors make a connected complete-bipartite tight-edge core; every other point joins its anchor level by a tight internal edge. Hence all of these potentials, and only these, are vertices. Opposite orientations are distinct and yield \(2(2^p-1)(2^q-1)\) facets of \(K\). This total count is auxiliary, not the main geometric invariant.

**2. Euclidean lengths and a strict screening lemma.** Let \(x\in\{0,\ldots,p-1\}\) count the \(A\)-points at level \(s\), and \(y\in\{0,\ldots,q-1\}\) count the \(B\)-points at level \(1-t\). Define \(M_0=q+sx-ty\). Direct subtraction of the squared mean gives
\[
Q(x,y)=\|\Pi f\|_2^2=q+s^2x-(2t-t^2)y-\frac{(q+sx-ty)^2}{N}.
\]
We prove that **every** maximizing pair has \(x=0\). For \(x\ge1\), the decrement in the first index yields
\[
Q(x-1,y)-Q(x,y)=\frac{s}{N}\bigl(2M_0-(N+1)s\bigr)=:G_1.
\]
If \(y=0\), then \(2M_0-(N+1)s\ge2q-(N-1)s>q-p+1>0\). For \(y\ge1\), we may alternatively decrement both indices, obtaining
\[
Q(x-1,y-1)-Q(x,y)=
-s^2+2t-t^2-\frac{2M_0(t-s)+(t-s)^2}{N}=:G_2.
\]
If \(s>t\), then \(M_0\ge q(1-t)+s+t\) and \(2q\ge N\), whence
\[
G_2>(-s^2+2t-t^2)+(s-t)(1-t)=(1-s)(s+t)>0.
\]
If \(t\ge s\), either \(G_1>0\), or else \(2M_0\le(N+1)s\). In the latter case
\[
G_2\ge t\left(2-s-t-\frac{t-s}{N}\right)>0,
\]
because \(0<s\le t<1\). Thus every configuration with \(x\ge1\) admits a *strict* norm-improving reduction. No maximizer can have \(x>0\), proving independence from \(s\).

**3. Exact integer optimization and contact count.** At \(x=0\), the preceding expression simplifies to
\[
Q(0,y)=H_{p,q,t}(y)=\frac{pq}{N}-\frac{t^2}{N}(y-\alpha)^2+\frac{t^2\alpha^2}{N},
\qquad\alpha=\frac N2-\frac pt.
\]
Because the coefficient of the square is strictly negative, exactly the integers nearest \(\alpha\) maximize, including both when \(\alpha\) is half-integral. For each maximizing integer \(y\), choose any \(y\)-subset of \(B\) to carry level \(1-t\); the entire \(A\) cluster has value zero. Every such choice and its negative yield distinct polar vertices, giving the stated contact count.

**4. Global optimality and the complete affine hull of incenters.** Since \(K=-K\), the existence of a ball of radius \(r\) about any center implies, by symmetry and convexity, that the ball of the same radius about zero also lies in \(K\). Hence the minimum facet distance from zero is the global inradius and equals the reciprocal square root of the maximum \(Q\). A ball of that radius centered at \(c\in E\) must satisfy \(\langle v,c\rangle=0\) for every origin-contact normal \(v\), because the facets with normals \(v\) and \(-v\) are both active at zero. Conversely, every noncontact facet has strictly positive slack at zero. By finiteness, a sufficiently small relative neighborhood of zero in the subspace orthogonal to all contact normals still permits a ball of radius \(r\). Therefore
\[
\dim\operatorname{aff}\mathcal C=(N-1)-\operatorname{rank}\operatorname{span}\{v:\|v\|_2^2=\max Q\}.
\]
When \(J=\{0\}\), the two antipodal contact normals are constant on each cluster and their span has rank one. Otherwise, some \(1\le y\le q-1\) is maximizing. Differences between permutations of its \(y\)-subset span the entire \((q-1)\)-dimensional mean-zero subspace supported on \(B\); the average of those contact normals supplies one independent nonzero inter-cluster contrast vector. Their rank is precisely \(q\), so the center dimension is \(p-1\).

**5. Exact first transition.** The first competitor to \(y=0\) is \(y=1\); strict concavity makes all higher \(y\) noncompetitive until that first comparison is reversed. Directly,
\[
H_{p,q,t}(1)-H_{p,q,t}(0)=\frac{t}{N}\bigl((N-1)t-2p\bigr).
\]
For \(q\ge p+2\), the threshold \(2p/(N-1)\) lies strictly inside \((0,1)\). At equality both zero and one maximize; below it only zero maximizes. For \(q\le p+1\), the threshold is at least one, so it is not reached. Subsequent ties occur when \(\alpha\) is half-integral, already exhaustively covered by the nearest-integer rule.

## Verification
`verify_two_cluster.py` uses only Python's standard library and exact rational arithmetic. For selected cases with at most six points it independently enumerates signed tight equations on every labeled spanning tree, retains all feasible Lipschitz potentials, and compares the complete polar-vertex set with the two-level classification. It then checks the global squared norm, number of contacts and contact-normal rank by exact Gaussian elimination. The seven configurations include the first transition on both sides and at equality, balanced sizes, and distinct within-cluster radii. A separate exhaustive finite grid checks the strict screening conclusion for all integer profile pairs \(2\le p\le7\), \(p\le q\le21\) and sixteen rational radius pairs per profile. Run `python3 verify_two_cluster.py`. Every finite check passed; the continuum claims depend on the analytical proof above rather than finite enumeration.

## Relationship to prior work
Aliaga, *Extreme points in Lipschitz-free spaces over compact metric spaces*, arXiv:2102.01219, proves a general characterization of **primal** extreme molecules; it does not compute canonical Euclidean inballs of the present two-cluster metrics. Bredies, Chirinos Rodriguez and Naldi, *On extreme points and representer theorems for the Lipschitz unit ball on finite metric spaces*, arXiv:2304.14039, prove a connected tight-edge characterization and a representer theorem; that criterion is background here, not a novelty claim. Alexander, Fradelizi, García-Lirola and Zvavitch, *Geometry and volume product of finite dimensional Lipschitz-free spaces*, arXiv:1911.10642, study geometric dualities and volume products, rather than the claimed two-cluster radial transition.

The previously obtained exact projection constants for equilateral cluster decompositions determine the least norm of a projection onto within-cluster mass fluctuations, not this Euclidean radius; even the associated sharp projection threshold involves a different invariant. Exact Hilbert distortion for the balanced four-point two-cluster ultrametric optimizes over **all** Euclidean norms, whereas the theorem fixes the canonical coordinate inner product and classifies all inball centers. A facet enumeration for independently shortened disjoint pairs includes the four-point two-pair benchmark but does not give these larger unequal-cluster radial results. The one-cluster-plus-singleton case has its own incenter transition, but its proof does not imply the strict screening of a *nontrivial* minority cluster. Our new claim requires both clusters to contain at least two points.

## Limitations
The conclusion depends on the specified canonical coordinate Euclidean metric and on two internally equilateral clusters with distances strictly below the cross distance. It is not an isometric or Banach--Mazur classification, and it is not asserted for more clusters or nonconstant within-cluster distances. The general existence of other equivalent historical presentations, particularly framed as maximum variance under Lipschitz constraints, has not been excluded. The exact finite computations are corroboration rather than exhaustive verification of real parameters. No independent mathematical audit has been performed.

## References
- R. J. Aliaga, *Extreme points in Lipschitz-free spaces over compact metric spaces*, arXiv:2102.01219, first publicly posted 2021-02-01; https://arxiv.org/abs/2102.01219.
- K. Bredies, J. Chirinos Rodriguez, E. Naldi, *On extreme points and representer theorems for the Lipschitz unit ball on finite metric spaces*, arXiv:2304.14039, first publicly posted 2023-04-27; https://arxiv.org/abs/2304.14039.
- M. Alexander, M. Fradelizi, L. C. García-Lirola, A. Zvavitch, *Geometry and volume product of finite dimensional Lipschitz-free spaces*, arXiv:1911.10642, first publicly posted 2019-11-24; https://arxiv.org/abs/1911.10642.
- S. J. Dilworth, D. Kutzarova, M. I. Ostrovskii, *Lipschitz free spaces on finite metric spaces*, arXiv:1807.03814, first publicly posted 2018-07-10; https://arxiv.org/abs/1807.03814.
