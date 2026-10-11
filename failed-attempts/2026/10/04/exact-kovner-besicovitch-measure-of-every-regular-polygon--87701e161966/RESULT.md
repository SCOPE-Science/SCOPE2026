# Exact Kovner–Besicovitch measure of every regular polygon

## Finding

For a planar convex body \(K\), let its Kovner–Besicovitch measure be
\[
\kappa(K)=\frac{\max\{|C|:C\subseteq K,\ C\text{ centrally symmetric}\}}{|K|},
\]
where \(|\cdot|\) denotes area. Let \(P_n\) be a regular Euclidean \(n\)-gon, \(n\ge3\). Then
\[
\kappa(P_n)=
\begin{cases}
1,&n\text{ even},\\[2mm]
1-\tan^2\!\left(\frac{\pi}{2n}\right),&n\text{ odd}.
\end{cases}
\]

If \(n\) is odd, the unique maximum-area centrally symmetric subset is
\[
P_n\cap(-P_n),
\]
taken with respect to the polygon center. This intersection is a regular \(2n\)-gon with the same inradius as \(P_n\). In particular,
\[
1-\kappa(P_n)=\tan^2\!\left(\frac{\pi}{2n}\right)
=\frac{\pi^2}{4n^2}+O(n^{-4})
\]
along odd \(n\).

For \(n=3\), the formula gives \(\kappa(P_3)=2/3\), recovering the classical sharp triangle value. For \(n=5\), it gives
\[
\kappa(P_5)=\frac{2}{\sqrt5}.
\]

## Assumptions and scope

The optimization is over all centrally symmetric convex subsets of the polygon; the center of symmetry is not prescribed. The polygon is Euclidean and regular. The statement concerns the area-based Kovner–Besicovitch measure, not axial symmetry, Minkowski asymmetry, or the area of a maximum parallelogram.

The literature motivation is twofold. Jin studies maximum-area parallelograms in a convex polygon and explicitly presents them as computable approximations to the maximum-area centrally symmetric body. Goenka, Moore, Sun, and White use the Kovner–Besicovitch measure as the standard central-symmetry benchmark when comparing it with axial symmetry. The classical Fáry–Rédei theorem gives existence and uniqueness of the maximum-area centrally symmetric kernel for every convex body.

## Proof

For a convex body \(K\) and a point \(c\), define
\[
S(c)=K\cap(2c-K).
\]
This is centrally symmetric about \(c\). Conversely, every centrally symmetric subset of \(K\) with center \(c\) lies in \(S(c)\). Therefore the largest centrally symmetric subset with prescribed center \(c\) is exactly \(S(c)\).

We first show that
\[
f(c)=|S(c)|^{1/2}
\]
is concave on the set where \(S(c)\) is nonempty. Let \(c_0,c_1\) be two centers and \(0\le\lambda\le1\), with
\[
c_\lambda=\lambda c_0+(1-\lambda)c_1.
\]
If \(x_i\in S(c_i)\), then \(x_i\in K\) and \(2c_i-x_i\in K\). By convexity,
\[
\lambda x_0+(1-\lambda)x_1\in K
\]
and
\[
2c_\lambda-\bigl(\lambda x_0+(1-\lambda)x_1\bigr)
=
\lambda(2c_0-x_0)+(1-\lambda)(2c_1-x_1)\in K.
\]
Hence
\[
\lambda S(c_0)+(1-\lambda)S(c_1)\subseteq S(c_\lambda).
\]
The planar Brunn–Minkowski inequality now gives
\[
f(c_\lambda)\ge
\lambda f(c_0)+(1-\lambda)f(c_1).
\]

Let \(R\) be rotation by \(2\pi/n\) about the center of \(P_n\), identified with the origin. Rotational invariance gives
\[
f(Rc)=f(c).
\]
The orbit average satisfies
\[
\frac1n\sum_{j=0}^{n-1}R^jc=0.
\]
By concavity,
\[
f(0)\ge \frac1n\sum_{j=0}^{n-1}f(R^jc)=f(c).
\]
Thus the centered intersection
\[
P_n\cap(-P_n)
\]
has maximum possible area among all centrally symmetric subsets. The classical uniqueness theorem for centrally symmetric kernels then identifies it with the unique kernel.

If \(n\) is even, \(P_n=-P_n\), so the kernel is \(P_n\) itself and \(\kappa(P_n)=1\).

Suppose \(n\) is odd, and let \(r\) be the inradius of \(P_n\). Write \(P_n\) as the intersection of the half-planes
\[
\langle x,u_j\rangle\le r,\qquad j=0,\ldots,n-1,
\]
where the outward unit normals \(u_j\) are equally spaced by \(2\pi/n\). The reflected polygon \(-P_n\) contributes the normals \(-u_j\). Since \(n\) is odd, the combined set
\[
\{u_j,-u_j:0\le j<n\}
\]
consists of \(2n\) equally spaced unit normals, with angular spacing \(\pi/n\). Hence
\[
P_n\cap(-P_n)
\]
is a regular \(2n\)-gon with inradius \(r\).

A regular \(m\)-gon with inradius \(r\) has area
\[
m r^2\tan\!\left(\frac{\pi}{m}\right).
\]
Therefore
\[
\kappa(P_n)
=
\frac{2n r^2\tan(\pi/(2n))}
{n r^2\tan(\pi/n)}
=
\frac{2\tan(\pi/(2n))}{\tan(\pi/n)}.
\]
Putting \(t=\tan(\pi/(2n))\) and using
\[
\tan(2\arctan t)=\frac{2t}{1-t^2}
\]
gives
\[
\kappa(P_n)=1-t^2
=
1-\tan^2\!\left(\frac{\pi}{2n}\right).
\]
This proves the formula.

## Verification

The proof has two independent layers.

First, the optimization over all possible symmetry centers is not assumed away: the inclusion
\[
\lambda S(c_0)+(1-\lambda)S(c_1)\subseteq S(c_\lambda)
\]
and Brunn–Minkowski show that the square root of overlap area is concave. Averaging any center over the rotational orbit of a regular polygon moves it to the polygon center without decreasing the overlap area.

Second, the centered overlap is computed exactly from supporting half-planes. For odd \(n\), the edge-normal set and its negatives interlace to form the normal set of a regular \(2n\)-gon with the same inradius. The area ratio then reduces to one tangent double-angle identity.

As a numerical sanity check, direct polygon intersection for \(n=3,5,7,9\) gives ratios
\[
0.666666\ldots,\quad
0.894427\ldots,\quad
0.947904\ldots,\quad
0.968908\ldots,
\]
matching
\[
1-\tan^2\!\left(\frac{\pi}{2n}\right)
\]
to floating-point precision. These computations are checks only and are not used in the proof.

## Relationship to prior work

Fáry and Rédei introduced the centrally symmetric kernel and proved that every convex body has a unique maximum-volume centrally symmetric subset. A later paper of Moszyńska and Żukowski explicitly recalls this theorem and develops the associated pseudo-center.

Jin's 2017 paper treats maximum-area parallelograms in convex polygons and explains that such parallelograms provide a \(2/\pi\)-approximation to the maximum-area centrally symmetric body. The paper develops algorithms and structural facts for parallelograms; it does not state the regular-polygon Kovner–Besicovitch formula above.

Goenka, Moore, Sun, and White define the Kovner–Besicovitch measure as the volume ratio of the largest centrally symmetric subset and recall the universal lower bound \(2/3\), with equality for triangles, in their 2023 work on axial symmetry. Their stated results concern axiality and folding symmetry, not an exact regular-polygon profile.

Targeted semantic and web searches for regular polygons, centrally symmetric kernels, pseudo-centers, Kovner–Besicovitch measures, and the tangent formula did not locate an equivalent all-\(n\) statement. The closest indexed results concern other regular-polygon extremal invariants or general algorithms rather than this central-symmetry measure.

## Limitations

The theorem is specific to regular polygons. It does not determine the Kovner–Besicovitch measure of arbitrary cyclic, equiangular, or near-regular polygons, and it does not provide a quantitative stability theorem under perturbation of the vertices.

The originality assessment has a residual historical risk. The central-kernel theory dates to 1950, and the final formula is elementary once rotational averaging and the centered intersection are recognized. A direct copy of the 1950 paper was located, but the available PDF transport could not be fully inspected in this run; a later full-text source confirms the uniqueness theorem. An equivalent regular-polygon computation could therefore exist in older literature under different terminology.

## References

K. Jin, “Finding all Maximal Area Parallelograms in a Convex Polygon,” arXiv:1711.00181, first submitted 2017-11-01.

R. Goenka, K. Moore, W. R. Sun, and E. P. White, “On Axial Symmetry in Convex Bodies,” arXiv:2309.12597, first submitted 2023-09-22.

M. Moszyńska and T. Żukowski, “On G-pseudo-centres of convex bodies,” Glasnik Matematički 33(53) (1998), 251–265.

I. Fáry and L. Rédei, “Der zentralsymmetrische Kern und die zentralsymmetrische Hülle von konvexen Körpern,” Mathematische Annalen 122 (1950), 205–220.
