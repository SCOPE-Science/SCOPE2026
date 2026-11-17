# Euclidean distance shells recover hyperplane-size profiles of paving matroid base polytopes

## Finding
Let \(M\) be a rank-\(k\) paving matroid on \(E=[n]\), where \(2\le k<n\). Give \(\mathbb R^n\) its standard Euclidean norm and set
\[
\Delta_{k,n}=\{x\in[0,1]^n:\sum_{i=1}^n x_i=k\},\qquad
P(M)=\operatorname{conv}\{\mathbf1_B:B\text{ is a basis of }M\}.
\]
For a nonbasis \(k\)-subset \(S\), let \(H(S)=\operatorname{cl}_M(S)\), let \(h=|H(S)|\), and write \(q=n-h\). Then \(H(S)\) is the **unique** hyperplane containing \(S\), and the unique metric projection of \(\mathbf1_S\) onto \(P(M)\) is
\[
\bigl(\Pi_{P(M)}\mathbf1_S\bigr)_i=
\begin{cases}
1-1/k,&i\in S,\\
0,&i\in H(S)\setminus S,\\
1/q,&i\in E\setminus H(S).
\end{cases}
\]
In particular,
\[
\operatorname{dist}_2(\mathbf1_S,P(M))^2=\frac1k+\frac1{n-h}.
\tag{1}
\]
The projection is the barycenter of the \(kq\) bases \((S\setminus\{s\})\cup\{j\}\), with \(s\in S\), \(j\notin H(S)\). These bases span an exposed product-of-simplices face of dimension \(k+q-2\) and intrinsic volume
\[
\frac{\sqrt{kq}}{(k-1)!(q-1)!}.
\tag{2}
\]
For a basis \(S\), its indicator vertex has distance zero.

For each integer \(h\in\{k,\dots,n-1\}\), let \(\lambda_h\) count the hyperplanes of cardinality \(h\). The **complete** multiset of squared distances of the \(\binom nk\) hypersimplex vertices to \(P(M)\) consists of
\[
\lambda_h\binom hk\quad\text{copies of}\quad\frac1k+\frac1{n-h},
\qquad (k\le h<n),
\tag{3}
\]
and \(\binom nk-\sum_{h=k}^{n-1}\lambda_h\binom hk\) zeros. Because these positive values are pairwise distinct, this metric histogram recovers every \(\lambda_h\) with \(h\ge k\), not merely their sum.

If \(M\) is not uniform and \(h_*\) is the largest cardinality of one of its hyperplanes, then the exact Euclidean Hausdorff distance is
\[
\boxed{d_H(\Delta_{k,n},P(M))=\sqrt{\frac1k+\frac1{n-h_*}}.}
\tag{4}
\]
The **only** points of the continuous hypersimplex attaining (4) are the incidence vertices \(\mathbf1_S\) for nonbases \(S\) contained in hyperplanes of cardinality \(h_*\); their number is \(\lambda_{h_*}\binom{h_*}{k}\). If \(M\) is uniform, \(P(M)=\Delta_{k,n}\) and the distance is zero.

## Assumptions and scope
A paving matroid of rank \(k\) has no circuits smaller than \(k\). No representability, connectivity, simplicity beyond the paving condition, or restrictions on hyperplane sizes are assumed. Hyperplanes are proper rank-\(k-1\) flats. The formulas use the fixed standard coordinate embedding (not arbitrary affine-equivalent realizations) and Euclidean distance in \(\mathbb R^n\). The face volume in (2) is its intrinsic Euclidean volume, taking the volume of a zero-dimensional simplex to be one.

## Proof
**Hyperplane ownership.** Every \((k-1)\)-subset is independent. A nonbasis \(k\)-subset \(S\) consequently has rank exactly \(k-1\), and its closure \(H(S)\) is a rank-\(k-1\) flat. If a rank-\(k-1\) flat contains \(S\), it must equal this closure. More generally distinct hyperplanes meet in at most \(k-2\) elements: an independent \((k-1)\)-subset in their intersection would span both. Hence the \(k\)-subsets belonging to distinct hyperplanes of size at least \(k\) are disjoint families.

**Exact projection certificate.** Fix a nonbasis \(S\) with hyperplane \(H=H(S)\), \(|H|=h\), and \(q=n-h\ge1\). For each \(s\in S\), the set \(S\setminus\{s\}\) is an independent set of rank \(k-1\), whose closure is \(H\). Thus every \((S\setminus\{s\})\cup\{j\}\) with \(j\notin H\) is a basis. Their uniform average is the proposed point \(y\in P(M)\).

For any \(z\in P(M)\), the rank inequality for \(H\) gives \(z(H)\le k-1\). Write \(a=\sum_{j\notin H}z_j\ge1\) and \(b=\sum_{i\in H\setminus S}z_i\ge0\). Since \(\sum_i z_i=k\), the sum of deficits on \(S\) is \(\sum_{i\in S}(1-z_i)=a+b\). Cauchy--Schwarz, separately on the \(k\) elements of \(S\) and the \(q\) elements outside \(H\), implies
\[
\|\mathbf1_S-z\|_2^2
\ge\frac{(a+b)^2}{k}+\frac{a^2}{q}
\ge\frac1k+\frac1q.
\]
The exhibited \(y\) attains the bound, proving (1). Equality requires \(a=1\), \(b=0\), constant deficits \(1/k\) on \(S\), and constant coordinates \(1/q\) outside \(H\); hence \(y\) is the **unique** nearest point.

**Contact face.** The intersection of \(P(M)\) with its supporting hyperplanes \(x(H)=k-1\) and \(x_i=0\) for every \(i\in H\setminus S\) is exactly
\[
F_S=\operatorname{conv}\{\mathbf1_{(S\setminus\{s\})\cup\{j\}}:s\in S,\ j\notin H\}.
\]
It is an exposed face, affinely and isometrically a Cartesian product of standard simplices \(\Delta_{k-1}\times\Delta_{q-1}\) in disjoint coordinate blocks. The regular simplex \(\operatorname{conv}\{e_1,\dots,e_m\}\) has intrinsic volume \(\sqrt m/(m-1)!\), by a Gram determinant of edge vectors; multiplying the two factors proves (2). The projection \(y\) lies in its relative interior.

**Histogram and farthest-point rigidity.** Unique hyperplane ownership gives exactly \(\lambda_h\binom hk\) nonbases at each \(h\), proving (3). These distances strictly increase with \(h\). Since \(P(M)\subseteq\Delta_{k,n}\), convexity of distance to a convex set places the Hausdorff maximum at a hypersimplex vertex, establishing (4).

To exclude nonvertex maximizers, for each hypersimplex vertex \(v\), write \(p_v=\Pi_{P(M)}v\) and \(r_v=v-p_v\). Every basis vertex has residual zero. Every nonbasis \(\mathbf1_S\) has residual strictly positive exactly on \(S\), strictly negative exactly on \(E\setminus H(S)\), and zero otherwise. Hence distinct hypersimplex vertices have distinct residuals unless both are bases. For any convex combination \(x=\sum_v t_vv\), the point \(\sum_vt_vp_v\) lies in \(P(M)\), and
\[
\operatorname{dist}_2(x,P(M))^2
\le\Big\|\sum_vt_vr_v\Big\|_2^2
=\sum_vt_v\|r_v\|_2^2
-\frac12\sum_{v,w}t_vt_w\|r_v-r_w\|_2^2.
\]
When at least one nonbasis is present, every genuinely nonvertex convex combination either lies in \(P(M)\) (if all its vertices are bases), or has a strictly positive final subtraction. Thus no nonvertex can attain the positive Hausdorff maximum. This also gives the number and type of the deepest vertices. All claims follow.

## Verification
The standalone script `check_paving_metric.py` independently enumerates all rank-\(k\) subsets, removes subsets lying in designated large hyperplanes, checks one-exchange basis witnesses and exact candidate distances, and solves 95 numerical nonnegative least-squares projections over the full remaining vertex hull. Its ten configurations include non-sparse paving matroids, different large-hyperplane sizes in one matroid, rank two, and rank four. Numerical agreement is checked to an absolute tolerance of \(2\times10^{-7}\), with rational arithmetic for the asserted distance values. Computation samples finite examples only; the proof above applies to every finite paving matroid satisfying the assumptions.

For example, take \(n=8\), \(k=3\) and two large hyperplanes \(\{1,2,3,4\}\) and \(\{4,5,6,7,8\}\). Their intersection has one element, so they are compatible with a paving matroid. The 56 hypersimplex vertices split into 42 bases, four nonbases with squared distance \(7/12\), and ten nonbases with squared distance \(2/3\). In particular the sharp Hausdorff distance is \(\sqrt{2/3}\).

## Relationship to prior work
Ferroni's work on sparse-paving matroid polytopes provides Ehrhart formulas for the special circuit-hyperplane regime. Hanely and collaborators develop general paving-matroid polytope dissections using stressed-hyperplane relaxation, and Ferroni and Schröter give corresponding hyperplane-size-based valuative formulas. These supply the natural setting and established rank/facet facts. The sparse-paving projection subcase is not claimed as new. The present metric theorem addresses the genuinely larger **non-sparse paving regime**, where hyperplanes may have different sizes greater than the rank; it determines individual nonbasis projection points, the complete distance histogram, inverse recovery of the hyperplane-size profile and all continuous Hausdorff maximizers. These exact Euclidean statements do not follow by merely evaluating a valuative invariant, since Hausdorff distance and individual projections are not additive polytope valuations.

## Limitations
The conclusions depend on the standard Euclidean coordinate realization, and do not extend as stated to arbitrary norms, non-paving matroids, or affine-distorted base polytopes. The result does not reconstruct the incidence pattern among hyperplanes, only the number in each size class. The existence of equivalent earlier formulas using different language has not been ruled out exhaustively; this analysis is not an independent mathematical audit. Finite numerical checks are corroborative and not substitutes for the unrestricted proof.

## References
1. L. Ferroni, *Matroids are not Ehrhart positive*, arXiv:2105.04465 (initially public May 10, 2021), https://arxiv.org/abs/2105.04465 .
2. D. Hanely, J. L. Martin, D. McGinnis, D. Miyata, G. D. Nasr, A. R. Vindas-Meléndez and M. Yin, *Ehrhart Theory of Paving and Panhandle Matroids*, arXiv:2201.12442 (initially public January 28, 2022), https://arxiv.org/abs/2201.12442 .
3. L. Ferroni and B. Schröter, *Valuative invariants for large classes of matroids*, *Journal of the London Mathematical Society* 110 (2024), e12984, https://doi.org/10.1112/jlms.12984 .
