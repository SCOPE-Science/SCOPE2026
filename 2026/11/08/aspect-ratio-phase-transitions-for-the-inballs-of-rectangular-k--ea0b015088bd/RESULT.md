# Aspect-ratio phase transitions for the inballs of rectangular \(k\)-assignment polytopes

## Finding
For integers \(2\le m<n\) and \(1\le k\le m\), let \(\mathcal A_{m,n,k}\) be the convex hull, in the Frobenius metric on real \(m\)-by-\(n\) matrices, of the zero-one matrices containing exactly \(k\) ones with no two in the same row or column. All inballs are taken **intrinsically in the affine hull**. Set \(p=mn\) and \(J\) equal to the all-ones matrix. The following gives the exact inradius and **every** maximum-ball center, including the rank-changing endpoint \(k=m\).

**Nonmaximal cardinality \(1\le k<m\).** Define
\[
 a=\frac{k}{\sqrt{p(p-1)}},\quad b=\frac{m-k}{\sqrt{p(m-1)}},\quad
 \alpha=\sqrt{\frac{p-1}{p}},\quad
 \gamma=\sqrt{\frac{m(n-1)}{n}}.
\]
Then
\[
 \boxed{\rho(\mathcal A_{m,n,k})=\min\{a,b\}.}
\]
The uniform matrix \(C_0=(k/p)J\) is always an incenter. If \(a\le b\), it is the **unique** incenter. If \(b<a\), the entire incenter locus is
\[
 \boxed{\mathcal I_{m,n,k}=\{C:\sum_{j=1}^n C_{ij}=k/m\ (\forall i),\ C_{ij}\ge b\alpha\ (\forall i,j),\ \sum_{i=1}^m C_{ij}\le1-b\gamma\ (\forall j)\},}
\]
and has affine dimension \(m(n-1)\). The regime \(b<a\) is equivalent to
\[
 \boxed{k>\frac{m\sqrt{mn-1}}{\sqrt{mn-1}+\sqrt{m-1}}.}
\]
At \(C_0\), exactly \(mn\) facet hyperplanes contact the largest ball when \(a<b\), exactly \(m\) when \(b<a\), and exactly \(mn+m\) at equality. In particular, **some** nonmaximal cardinality exhibits a nonunique incenter if and only if
\[
 \boxed{mn-1<(m-1)^3.}
\]
The equality threshold can be realized at integers: \((m,n,k)=(5,13,4)\) gives a unique incenter with simultaneous coordinate and row contacts.

**Maximal cardinality \(k=m<n\).** Define
\[
 a_*=\frac1{\sqrt{n(n-1)}},\qquad b_*=\frac{n-m}{\sqrt{mn(n-1)}},\qquad
 \alpha_*=\sqrt{\frac{n-1}{n}}.
\]
Then, in the different affine hull where every row sum is exactly one,
\[
 \boxed{\rho(\mathcal A_{m,n,m})=\min\{a_*,b_*\}.}
\]
The uniform matrix \(C_0=J/n\) is the unique incenter when \(n-m\ge\sqrt m\). When \(n-m<\sqrt m\), all maximum-ball centers form the translated and scaled rectangular transportation polytope
\[
 \boxed{\mathcal I_{m,n,m}=\ell J+(1-n\ell)\mathcal T_{m,n},\quad
 \ell=b_*\alpha_*,\quad \mathcal T_{m,n}=\{T\ge0:\sum_j T_{ij}=1,\ \sum_i T_{ij}=m/n\}.}
\]
Its affine dimension is \((m-1)(n-1)\). At the uniform center, the number of contacting facets is \(mn\) when \(n-m>\sqrt m\), \(mn+n\) when \(n-m=\sqrt m\), and \(n\) when \(n-m<\sqrt m\). The critical equality occurs, for example, at \((m,n)=(4,6)\).

Thus rectangularity can completely suppress the positive-dimensional incenter phase: for any fixed \(m\), sufficiently large \(n\) makes every \(1\le k\le m\) have a unique incenter. Conversely, \((m,n)=(8,9)\) has incenter dimensions \(64\) at \(k=7\) and \(56\) at \(k=8\).

## Assumptions and scope
The Frobenius metric is \(\|X\|_F^2=\sum_{i,j}X_{ij}^2\). The polytope is the standard fixed-cardinality (rectangular) \(k\)-matching polytope of \(K_{m,n}\); no affine rescaling is made. For \(k<m\) the affine hull is \(H_k=\{X:\sum_{i,j}X_{ij}=k\}\), of dimension \(mn-1\). For \(k=m<n\) it is \(H_m=\{X:\sum_jX_{ij}=1\ (1\le i\le m)\}\), of dimension \(m(n-1)\). The strict inequality \(m<n\) avoids the square Birkhoff endpoint, where **both** row and column sums are affine equalities and the intrinsic metric changes again.

The known exact inequality representation of these polytopes is
\[
 X_{ij}\ge0,\qquad \sum_jX_{ij}\le1,\qquad \sum_iX_{ij}\le1,\qquad \sum_{i,j}X_{ij}=k.
\]
For \(1<k<m<n\) every listed inequality defines a facet. For \(k=1\), only the coordinate constraints define facets. For \(k=m<n\), row sums are affine equalities and the coordinate and column-sum constraints define facets. These facts are established in the cited complete-bipartite \(k\)-assignment polytope literature; they are not asserted as new.

## Proof
For a full-dimensional polytope inside an affine space \(H\) with tangent subspace \(L\), a ball of radius \(r\) about \(C\in H\) lies in a halfspace \(\langle A,X\rangle\le\beta\) precisely when
\[
 \langle A,C\rangle+r\|\operatorname{proj}_L A\|_F\le\beta.
\]
This follows by maximizing the linear functional on the Euclidean ball in \(H\). Imposing these inequalities for a complete halfspace representation is necessary and sufficient for ball containment, including when an inequality is redundant.

For \(k<m\), put \(p=mn\). The tangent space is \(L=\{X:\sum_{i,j}X_{ij}=0\}\). If \(E_{ij}\) is a matrix unit, \(R_i\) a row indicator, and \(Q_j\) a column indicator, their orthogonal projections are obtained by subtracting the mean matrix. Their squared projected norms are respectively
\[
 \|\operatorname{proj}_L E_{ij}\|_F^2=1-1/p,
 \quad \|\operatorname{proj}_L R_i\|_F^2=n(m-1)/m,
 \quad \|\operatorname{proj}_L Q_j\|_F^2=m(n-1)/n.
\]
Summing the \(mn\) coordinate lower bounds for a feasible radius \(r\) gives \(k\ge rp\alpha\), hence \(r\le a\). Summing the \(m\) row upper bounds gives \(k\le m-rm\sqrt{n(m-1)/m}\), hence \(r\le b\). Columns similarly give \(r\le c=(n-k)/\sqrt{p(n-1)}\). Since the function \(f(z)=(z-k)/\sqrt{z-1}\) increases for \(z\ge m\ge k\) (its derivative has numerator \(z+k-2\)), and \(m<n\), we have \(b<c\) for \(k\ge1\). Therefore every feasible radius is bounded by \(\min\{a,b\}\). At \(C_0=(k/p)J\), all three families of clearances are exactly \(a,b,c\), so this bound is attained.

If \(a\le b\), every feasible center of an optimal ball satisfies \(C_{ij}\ge a\alpha=k/p\) at all \(mn\) coordinates. Their fixed total sum is \(k\), so every inequality is an equality and \(C=C_0\). If \(b<a\), each row obeys \(\sum_jC_{ij}\le1-b\sqrt{n(m-1)/m}=k/m\); since the total is \(k\), all \(m\) row inequalities become equalities. The remaining ball-containment conditions are exactly the displayed coordinate lower bounds and column upper bounds. Conversely, every displayed matrix satisfies all projected halfspace constraints at radius \(b\), proving sufficiency. At \(C_0\), coordinates and columns have strictly more clearance than \(b\), so the incenter locus contains a relative neighborhood of \(C_0\) in the affine subspace of matrices with fixed row sums \(k/m\). This subspace has dimension \(mn-m=m(n-1)\); no higher dimension is possible. Direct comparison of the three clearances gives the claimed contact counts. Solving \(b<a\) yields the square-root threshold; because this threshold is independent of \(k\), a qualifying integer \(k<m\) exists precisely when \(k=m-1\) qualifies, equivalent to \(mn-1<(m-1)^3\).

For \(k=m<n\), every row sum is one and the tangent space is \(L=\{X:\sum_jX_{ij}=0\ \forall i\}\). Projection within each row subtracts that row's mean. Therefore
\[
 \|\operatorname{proj}_L E_{ij}\|_F^2=(n-1)/n,
 \qquad \|\operatorname{proj}_L Q_j\|_F^2=m(n-1)/n.
\]
The coordinate lower bounds summed over any row give \(1\ge rn\alpha_*\), hence \(r\le a_*\). The \(n\) column upper bounds sum to \(m\le n-rn\sqrt{m(n-1)/n}\), hence \(r\le b_*\). Both are attained at \(C_0=J/n\), proving the endpoint formula.

If \(a_*\le b_*\), each coordinate of an optimal center is at least \(a_*\alpha_*=1/n\); every row sums to one, forcing \(C_0\). If \(b_*<a_*\), summing the optimal column upper bounds forces every column sum to equal \(m/n\). The remaining necessary and sufficient constraints are \(C_{ij}\ge\ell=b_*\alpha_*\) and the already fixed row sums one. Since \(b_*<a_*\), \(0<n\ell<1\). Substitution \(T=(C-\ell J)/(1-n\ell)\) is a bijection onto the displayed nonnegative rectangular transportation polytope. The strictly positive uniform transportation matrix is in its relative interior, so its dimension is \(mn-(m+n-1)=(m-1)(n-1)\). Comparing \(b_*/a_*=(n-m)/\sqrt m\) proves the phase criterion and contact counts.

At \((5,13,4)\), \(mn-1=(m-1)^3=64\), giving the stated nonterminal tie. At \((4,6,4)\), \(n-m=\sqrt m=2\). At \((8,9,7)\), \(mn-1=71<(m-1)^3=343\) and the threshold is below seven, so the incenter locus has dimension \(8(9-1)=64\). At \((8,9,8)\), the endpoint column phase has dimension \(7(9-1)=56\). All claimed phase and dimension statements follow.

## Verification
The proof is algebraic and covers **all** integer parameters \(2\le m<n\), \(1\le k\le m\); finite computations are not substituted for any infinite argument. The accompanying `verify.py` reconstructs the affine tangent space by orthonormal nullspaces, independently formulates the Euclidean Chebyshev linear program from all defining inequalities, and checks the predicted optimal radius and dimension of the locus of active constraints at the uniform center. It tests 175 cases: \(2\le m\le8\), \(m+1\le n\le m+5\), \(1\le k\le m\). A separate exact-arithmetic portion verifies the two critical integer examples and the aspect-ratio threshold inequalities. Requirements are Python 3 with NumPy and SciPy. Computations validate finite test instances to numerical tolerance; the proof above is what establishes the universal result.

## Relationship to prior work
Gill and Linusson's *The \(k\)-assignment polytope* (2009) proves the matrix inequality representation and gives the facet/affine-dimension cases, one-skeleton diameter, face poset, and combinatorial structure. Torres's 2023 paper establishes the same representation for fixed-size matchings of arbitrary bipartite graphs and studies normality. Their one-skeleton diameter is not an inscribed Euclidean radius. Heuer and Striker (2020/2022) study the **all-cardinalities** partial permutation polytope, which has different affine dimension; taking a fixed-total slice does not preserve its ambient inball. These publications provide the known starting geometry, not the formulas above.

An earlier square-case geometric result, *A Birkhoff-polytope family of incenters for partial assignment polytopes* (2026), gives an inball phase transition for \(N\)-by-\(N\) fixed-size assignments with \(2\le k<N\). It explicitly does not treat rectangular sizes or full-rank endpoints. At square sizes, row and column inequalities have equal intrinsic norms and their simultaneous saturation produces a Birkhoff locus. For \(m<n\), row and column norms separate and the nonterminal high-rank locus has dimension \(m(n-1)\), not \((m-1)^2\). At \(k=m<n\), the tangent space changes and an independent column-controlled transportation phase appears. These are not specializations of the square theorem. Standard formulas for full equality-margin transportation polytopes also do not imply the radius in the different affine hulls used here.

## Limitations
The claims require standard Frobenius geometry; they do not assert invariance under arbitrary affine projections. Square parameter pairs are excluded because their known metric geometry follows a different row/column symmetry, and the square perfect-matching endpoint is the Birkhoff polytope. The explicit incenter inequalities characterize entire loci but do not enumerate all vertices or faces of the nonterminal high-rank center polytopes. The checked literature does not rule out an unindexed equivalent result under the terminology of Chebyshev centers, fixed-rank doubly substochastic slices, or transportation-polytope sections. The companion computations are finite corroborations, not historical-priority proofs or independent mathematical auditing.

## References
1. Juan Camilo Torres, *Normality of \(k\)-Matching Polytopes of Bipartite Graphs*, arXiv:2306.11910v1, first public 2023-06-20, especially Theorem 3.1 and the matrix specialization, https://arxiv.org/abs/2306.11910.
2. Jonna Gill and Svante Linusson, *The \(k\)-assignment polytope*, *Discrete Optimization* 6 (2009), 148--161, DOI 10.1016/j.disopt.2008.10.003, especially Section 2 and its facet/dimension table; author postprint https://liu.diva-portal.org/smash/get/diva2:210918/FULLTEXT01.pdf.
3. Dylan Heuer and Jessica Striker, *Partial Permutation and Alternating Sign Matrix Polytopes*, arXiv:2012.09901v1, first public 2020-12-17, especially Section 3, https://arxiv.org/abs/2012.09901.
4. *A Birkhoff-polytope family of incenters for partial assignment polytopes*, earlier square-case research record (2026), public record identifier 6c3de65c0b12; square and non-endpoint scope only.
