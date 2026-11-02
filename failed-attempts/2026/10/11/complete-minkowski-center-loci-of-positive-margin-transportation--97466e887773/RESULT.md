# Complete Minkowski-center loci of positive-margin transportation polytopes

## Finding

**Theorem (complete asymmetry and center-locus classification).** Fix integers \(m,n\ge2\) and positive real row and column margins \(r_1,\ldots,r_m>0\), \(c_1,\ldots,c_n>0\), with equal total \(T=\sum_i r_i=\sum_j c_j\). Define the transportation polytope
\[
\mathcal T(r,c)=\{X\in\mathbb R_{\ge0}^{m\times n}:\sum_jX_{ij}=r_i,\ \sum_iX_{ij}=c_j\}.
\]
Put \(U_{ij}=\min\{r_i,c_j\}\), \(u_i=\sum_j U_{ij}\), \(v_j=\sum_i U_{ij}\), and
\[
\beta=\max\left\{\max_i\frac{u_i}{r_i},\max_j\frac{v_j}{c_j}\right\}.
\]
The Minkowski asymmetry \(s(K)=\min\{s\ge1:K-a\subseteq-s(K-a)\text{ for some }a\in K\}\) is exactly
\[
\boxed{s(\mathcal T(r,c))=\beta-1}.
\]
Set \(R_i=r_i-u_i/\beta\), \(C_j=c_j-v_j/\beta\). The **entire** locus of minimizing centers is the affine image of a (possibly degenerate) transportation polytope:
\[
\boxed{\mathcal M(\mathcal T(r,c))=\frac{U}{\beta}+\mathcal T(R,C).}
\]
Here \(\mathcal T(R,C)\) denotes nonnegative tables with the indicated *possibly zero* residual margins. If \(S=\sum_i R_i=\sum_j C_j>0\), set \(I=\{i:R_i>0\}\), \(J=\{j:C_j>0\}\). Then
\[
\dim\operatorname{aff}\mathcal M=(|I|-1)(|J|-1).
\]
If \(S=0\), the locus is a singleton. Thus the minimizing center is unique exactly when \(S=0\) or \(\min\{|I|,|J|\}=1\).

In particular, **every positive-margin square transportation polytope** of size \(n\times n\) satisfies \(s=n-1\), independently of its margins, although its set of optimal centers may have positive dimension. Writing \(r_{\min}=\min_i r_i\), \(c_{\min}=\min_jc_j\), the scalar \(\beta\) can also be computed directly from only the two minimum margins and the opposing margin lists:
\[
\beta=\max\left\{\sum_j\min\left(1,\frac{c_j}{r_{\min}}\right),\sum_i\min\left(1,\frac{r_i}{c_{\min}}\right)\right\}.
\]

## Assumptions and scope

All margins are finite, strictly positive real numbers with equal total. Dimensions \(m,n\ge2\) are arbitrary. The ambient matrix space is restricted to the affine hull specified by the row and column equations. The center locus and dimension statements apply to degenerate residual margins by deleting zero-margin rows and columns. The formula is affine-geometric, not dependent on a Euclidean metric, on integral margins, or on a generic/nondegenerate vertex assumption.

## Proof

**1. Extremal coordinate values.** Every nonnegative table in \(\mathcal T(r,c)\) satisfies \(X_{ij}\le U_{ij}\). Equality is achievable. If \(r_i\le c_j\), put \(X_{ij}=r_i\), fill the other entries of row \(i\) with zero, and fill the remaining row margins against column margins \(c_j-r_i\) for column \(j\) and \(c_k\) for other columns. These lists are nonnegative and have equal total, so the nonnegative outer-product transportation construction works. The case \(r_i\ge c_j\) is symmetric. Consequently \(\max_{X\in\mathcal T}X_{ij}=U_{ij}\).

**2. Inclusion equivalence.** For any \(s\ge1\) and \(A\in\mathcal T(r,c)\), the inclusion \(\mathcal T-A\subseteq-s(\mathcal T-A)\) is equivalent to \(((s+1)A-X)/s\in\mathcal T\) for every \(X\in\mathcal T\). All row and column sums of this transformed table automatically have the correct values. Its nonnegativity, and hence feasibility, is equivalent to \((s+1)A_{ij}\ge U_{ij}\) for every \(i,j\).

**3. Threshold and full locus.** Set \(b=s+1\). A feasible \(A\ge U/b\) exists if and only if \(br_i\ge u_i\) for every row and \(bc_j\ge v_j\) for every column. Necessity follows by summing. For sufficiency set \(R_i(b)=r_i-u_i/b\), \(C_j(b)=c_j-v_j/b\). Their totals coincide because \(\sum_i u_i=\sum_j v_j\). If their common total \(S(b)>0\), the nonnegative rank-one matrix \(Y_{ij}=R_i(b)C_j(b)/S(b)\) has these margins; if it is zero, choose \(Y=0\). Then \(A=U/b+Y\) is feasible. Thus the least \(b\) is exactly \(\beta\), and the complete set of solutions at equality is \(U/\beta+\mathcal T(R,C)\). The bound \(\beta\ge2\) follows directly because for \(r_{\min}\le c_{\min}\), \(u_{i_*}/r_{i_*}=n\ge2\), while otherwise \(v_{j_*}/c_{j_*}=m\ge2\). This also proves \(s=\beta-1\ge1\).

**4. Dimension and uniqueness.** Every residual table has zero entries outside \(I\times J\). If \(S>0\), the matrix \(Y_{ij}=R_iC_j/S\) is strictly positive on \(I\times J\), hence is relatively interior to the transportation polytope on this support. Its affine hull has \(|I|+|J|-1\) independent row-column equations in \(|I||J|\) variables, giving dimension \((|I|-1)(|J|-1)\). For \(S=0\), all residual entries vanish. The criterion for a singleton follows.

**5. Minimum-margin and square invariance.** The function \(x\mapsto\sum_j\min(1,c_j/x)\) is nonincreasing on \(x>0\); its maximum over row margins occurs at \(r_{\min}\). Apply the column analogue to obtain the displayed alternative formula. When \(m=n\), every row and column ratio is at most \(n\). If \(r_{\min}\le c_{\min}\), the smallest row has every \(U_{ij}=r_{\min}\), yielding ratio \(n\); otherwise the smallest column has every \(U_{ij}=c_{\min}\), also yielding \(n\). Therefore \(\beta=n\) and \(s=n-1\).

## Verification

The standalone program `verify.py` performs exact rational checks on 648 automatically generated positive-margin instances, including the residual transportation construction, minimizer inclusion inequalities, minimum-margin threshold, and affine-dimension formula; it independently solves 45 small optimization instances by linear programming, including independent linear programs for each coordinate maximum. It also checks eight square Birkhoff instances. It does **not** prove statements for arbitrary real margins; the proof above does. Run `python3 verify.py`; SciPy is required only for the optional independent LP comparison.

For an illustrative \(3\times3\) case with \(r=c=(1,2,3)\), \(s=2\) and both sets \(I,J\) equal \(\{2,3\}\), giving a one-dimensional center locus. For \(r=c=(1,1,1)\), \(s=2\) but all residual margins vanish and the center is unique.

## Relationship to prior work

General formulations for Minkowski symmetry of a point in a polyhedron and linear-programming computation of Minkowski centers were established before this statement, especially by Belloni and Freund and by den Hertog, Pauphilet, and Soali. **Neither the general LP reduction nor the Minkowski-asymmetry definition is claimed as new.** Transportation polytopes, their vertex geometry, and monotone paths are also classical; Blanchard, De Loera, and Louveaux provide a geometry-focused primary source. The assertion assessed here is the closed-form margin formula for all transportation polytopes, the complete translated-residual transportation-polytope description of *all* minimizing centers, their exact dimension and uniqueness criterion, and the universal square-margins invariance. The generic LP schemes apply to these objects but do not themselves state these specialized identities.

## Limitations

The formula assumes a **complete** bipartite support and strictly positive prescribed margins. Structural zero constraints, upper bounds on individual cells, unequal total margins, or absent cells require separate analysis. Originality is not independently certified; equivalent or overlooked formulations in optimization or matrix-scaling literature remain possible. Finite experiments are illustrative checks only, not a universal proof. The complete theoretical proof concerns the stated unrestricted nonnegative real transportation polytope.

## References

- M. Blanchard, J. A. De Loera, and Q. Louveaux, *On the Length of Monotone Paths in Polyhedra*, arXiv:2001.09575 (first posted 27 January 2020), especially the transportation-polytope discussion. https://arxiv.org/abs/2001.09575
- D. den Hertog, J. Pauphilet, and M. Y. Soali, *Minkowski Centers via Robust Optimization: Computation and Applications*, 2023, especially Proposition 4 and the polyhedral linear-programming formulation. https://optimization-online.org/wp-content/uploads/2022/01/Minkowski_Final-1.pdf
- A. Belloni and R. M. Freund, *On the Symmetry Function of a Convex Set*, Mathematical Programming 111 (2008), 57–93, DOI 10.1007/s10107-006-0074-4.
- J. A. De Loera and E. D. Kim, *Combinatorics and Geometry of Transportation Polytopes: An Update*, arXiv:1307.0124. https://arxiv.org/abs/1307.0124
- P. Koehl, *Extreme points of general transportation polytopes*, arXiv:2404.16791 (first posted 25 April 2024). https://arxiv.org/abs/2404.16791
