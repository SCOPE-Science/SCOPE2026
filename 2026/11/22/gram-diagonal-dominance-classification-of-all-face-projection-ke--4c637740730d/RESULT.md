# Gram-diagonal-dominance classification of all-face projection kernels of parallelotopes

## Finding
For every integer \(d\ge 2\), let \(U=(u_1\ \cdots\ u_d)\) be any invertible real \(d\times d\) matrix and let \(P=p_0+U[0,1]^d\). Write its positive-definite Gram matrix \(G=U^{\mathsf T}U=(g_{ij})\), and define
\[
L_i=\sum_{j\ne i}\max\{g_{ij},0\},\qquad
H_i=g_{ii}+\sum_{j\ne i}\min\{g_{ij},0\},\qquad
\delta_i=H_i-L_i=g_{ii}-\sum_{j\ne i}|g_{ij}|.
\]
The *all-face orthogonal kernel* \(K(P)\), consisting of interior points whose orthogonal projection onto the affine span of every nonempty face belongs to that face's relative interior, is exactly
\[
\boxed{K(P)=\big\{p_0+UG^{-1}b:\ L_i<b_i<H_i\ (1\le i\le d)\big\}.}
\]
Thus the entire all-face requirement reduces exactly to checking the relative interiors of the edges. The kernel is nonempty if and only if \(G\) is strictly row-diagonally dominant, \(\delta_i>0\) for every \(i\). When nonempty, it is an open parallelotope with the same center as \(P\), and
\[
\boxed{\frac{\operatorname{vol}_d K(P)}{\operatorname{vol}_d P}
=\frac{\prod_{i=1}^d\delta_i}{\det G}.}
\]
If any \(\delta_i\le0\), the kernel is empty and its volume is zero. The quotient is also the probability that a point sampled uniformly by volume in \(P\) satisfies every face-projection condition.

For the three-dimensional equiangular unit-edge parallelotope with \(g_{ii}=1\), \(g_{ij}=c\) for distinct indices, and \(-1/2<c<1\), the kernel exists precisely when \(-1/2<c<1/2\), and then its volume fraction is
\[
\frac{(1-2|c|)^3}{(1-c)^2(1+2c)}.
\]
In particular the ratios at \(c=1/3\) and \(c=-1/4\) are respectively \(1/20\) and \(4/25\); at \(c=1/2\) the kernel is empty.

## Assumptions and scope
All geometry is Euclidean. The generators \(u_i\) are linearly independent but need not be unit length or orthogonal. Vertices (zero-dimensional faces) impose no restriction because the projection onto a point is that point. The face \(P\) itself imposes that the point is interior. Other faces are indexed by a nonempty set \(I\subseteq\{1,\ldots,d\}\) of free coordinates and fixed values \(\varepsilon_j\in\{0,1\}\) for \(j\notin I\). The strict inequalities in the theorem are essential: boundaries of the kernel fail some required relative-interior condition.

## Proof
**Necessity from edges.** Fix any direction \(u_i\) and any edge with complementary coordinates \(\varepsilon_j\in\{0,1\}\). Write a candidate point as \(B=p_0+UG^{-1}b\), uniquely possible for any \(B\in\mathbb R^d\). Its perpendicular foot on the line of this edge has coordinate
\[
s_i=\frac{b_i-\sum_{j\ne i}g_{ij}\varepsilon_j}{g_{ii}}.
\]
Requiring this coordinate to be strictly between zero and one for *all* edges in direction \(u_i\) is equivalent to requiring
\[
\max_{\varepsilon}\sum_{j\ne i}g_{ij}\varepsilon_j<b_i<g_{ii}+\min_{\varepsilon}\sum_{j\ne i}g_{ij}\varepsilon_j,
\]
which is exactly \(L_i<b_i<H_i\). These inequalities cannot have a solution if any \(\delta_i\le0\).

**Sufficiency for every face.** Assume all \(\delta_i>0\) and \(L_i<b_i<H_i\) for every \(i\). Consider any nonempty face with free-coordinate index set \(I\) and fixed complementary coordinates \(\varepsilon_j\). Write the orthogonal foot as the point on its affine span whose free coordinates are the vector \(s\). The normal equations are
\[
G_{II}s=b_I-G_{I,I^c}\varepsilon.
\]
The matrix \(G_{II}\) is positive definite, so there is a unique foot. Suppose that some \(s_i\) is not in the open unit interval, and let
\[
m=\max\left(0,\max_{i\in I}(-s_i),\max_{i\in I}(s_i-1)\right).
\]
Then all \(s_k\in[-m,1+m]\), and some coordinate equals \(-m\) or \(1+m\) (including the endpoint case \(m=0\)). If \(s_i=1+m\), the normal equation gives, after bounding all other coordinates and all fixed \(\varepsilon_j\in[0,1]\),
\[
b_i\ge H_i+m\left(g_{ii}-\sum_{k\in I\setminus\{i\}}|g_{ik}|\right)\ge H_i,
\]
contradicting \(b_i<H_i\). If \(s_i=-m\), the same bounds give
\[
b_i\le L_i-m\left(g_{ii}-\sum_{k\in I\setminus\{i\}}|g_{ik}|\right)\le L_i,
\]
contradicting \(b_i>L_i\). The coefficients of \(m\) are positive because of strict diagonal dominance. Thus every face foot is in the face's relative interior. Taking \(I=\{1,\ldots,d\}\) also proves that the original point lies in \(\operatorname{int}P\), so no assumption of interiority was overlooked.

**Center and volume.** Since \(L_i+H_i=\sum_jg_{ij}\), the center of the open \(b\)-box is \(G\mathbf1/2\), mapping to \(p_0+U\mathbf1/2\), the center of \(P\). The map \(b\mapsto p_0+UG^{-1}b\) has absolute determinant \(|\det U|/(\det G)=1/|\det U|\). Its image of the open box has volume \((\prod_i\delta_i)/|\det U|\), whereas \(\operatorname{vol}_d P=|\det U|\). Their ratio is the claimed product divided by \(\det G\).

**Equiangular specialization.** The three eigenvalues of the stated Gram matrix are \(1-c\) twice and \(1+2c\) once, so positive definiteness is equivalent to \(-1/2<c<1\). Each diagonal-dominance gap is \(1-2|c|\); substitution into the determinant formula gives the asserted threshold and fraction. The rational examples follow by direct arithmetic.

## Verification
The accompanying `verify.py` uses exact rational SymPy linear algebra to check 60 rational positive-definite Gram matrices generated from invertible integer bases in dimensions two through five, 420 center points and 31,500 projections to faces, as well as two exact volume ratios and two empty-kernel cases. Execute `python verify.py` with SymPy installed. Its expected output starts with `PASS:`. These finite checks corroborate the analytic proof and do not prove the quantified infinite-dimensional-family statement.

## Relationship to prior work
Jan Pavlík's *Thales's theorem in higher dimensions* (arXiv:2611.14277, Definition 6.1) defines the orthogonal kernel for every polytope as an intersection of open sets and notes it can be empty. Its Lemma 6.2 groups the same constraints by vertex; Theorem 6.6 characterizes orthogonal tilings in dimension three, not higher dimensions. The companion *Face lattices of polytopes and bipolar polytopes* (arXiv:2611.13896, Section 5.3) discusses regular cutout configurations and orthogonal face projections. The present result specializes the face-projection question to all Euclidean parallelotopes and gives a strict Gram-matrix nonemptiness criterion, an exact \(2d\)-slab reduction and exact volume that are not stated in those inspected materials. In three dimensions, the kernel criterion may be combined with Pavlík's published tiling theorem; no higher-dimensional tiling claim is made here.

## Limitations
The shape formula relies on an invertible parallelotope generator matrix. The argument does not give a criterion for arbitrary combinatorial cubes or general polytopes. This is not a solution to the higher-dimensional tiling conjecture in the motivating paper. The published-priority search is bounded; unindexed historical treatments of edge-projection inequalities may exist. The result has undergone no independent mathematical audit.

## References
1. Jan Pavlík, *Thales's theorem in higher dimensions*, arXiv:2611.14277v1 (first submitted 10 November 2026), Definition 6.1, Lemma 6.2, Theorem 6.6. https://arxiv.org/abs/2611.14277
2. Jan Pavlík, *Face lattices of polytopes and bipolar polytopes*, arXiv:2611.13896v1 (first submitted 10 November 2026), Section 5.3 and Remark 5.19. https://arxiv.org/abs/2611.13896
