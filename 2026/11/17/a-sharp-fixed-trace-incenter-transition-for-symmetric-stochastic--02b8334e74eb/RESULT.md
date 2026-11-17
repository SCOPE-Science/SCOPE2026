# A sharp fixed-trace incenter transition for symmetric stochastic polytopes

## Finding
For every integer \(n\ge4\) and every real \(0<t<n\), consider the convex polytope of reversible, uniform-stationary Markov kernels with prescribed total self-transition mass,
\[
\mathcal S_n(t)=\left\{X\in\mathbb R^{n\times n}:X=X^{\mathsf T},\ X\mathbf1=\mathbf1,\ X_{ij}\ge0,\ \operatorname{tr}X=t\right\}.
\]
Equip its affine hull with the intrinsic Euclidean distance induced by the Frobenius norm. Put
\[
q_n=\sqrt{n^2-n+2},\qquad
\tau_n=\frac{n\sqrt2}{q_n+\sqrt2}.
\]
Its exact largest-inscribed-ball radius is
\[
\boxed{\rho_n(t)=\frac{1}{\sqrt{(n-1)(n-2)}}\min\left\{t,\frac{\sqrt2(n-t)}{q_n}\right\}.}
\]
The threshold \(\tau_n\) lies strictly between zero and \(n\), and \(\tau_n\to\sqrt2\) as \(n\to\infty\). There is a sharp transition in the **complete set** of optimal ball centers.

If \(0<t<\tau_n\), define
\[
\lambda=\frac{tq_n}{\sqrt2\,n(n-1)},\qquad
\beta=1-\frac tn\left(1+\frac{q_n}{\sqrt2}\right)>0,
\]
and let \(\mathcal F_n\) be the fractional perfect matching polytope of the complete graph, represented by symmetric matrices:
\[
\mathcal F_n=\{Y=Y^{\mathsf T}:Y_{ii}=0,\ Y_{ij}\ge0,\ Y\mathbf1=\mathbf1\}.
\]
Then **every** center of a largest intrinsic Euclidean ball, and no other center, has entries
\[
\boxed{X_{ii}=t/n,\qquad X_{ij}=\lambda+\beta Y_{ij}\quad(i\ne j),\quad Y\in\mathcal F_n.}
\]
The incenter locus has affine dimension \(n(n-3)/2\). Its vertices are indexed precisely by partitions of \([n]\) into pairs and undirected odd cycles of lengths at least three: an edge of a paired block receives weight one and each edge of an odd cycle weight one-half. In particular the incenter loci for \(n=4,5,6\) have respectively \(3,22,25\) vertices. Their general vertex count is
\[
\boxed{f_n=n!\,[z^n]\exp\left(\frac{z^2}{2}+\sum_{\substack{\ell\ge3\\\ell\text{ odd}}}\frac{z^\ell}{2\ell}\right).}
\]
In this phase, every optimal ball touches all \(n\) diagonal-coordinate supporting hyperplanes. It additionally touches the off-diagonal hyperplane indexed by \(\{i,j\}\) exactly when the associated \(Y_{ij}\) vanishes. The center corresponding to the all-positive fractional matching touches no off-diagonal supporting hyperplane.

If \(\tau_n\le t<n\), the optimal center is **unique**, with
\[
\boxed{X_{ii}=t/n,\qquad X_{ij}=\frac{n-t}{n(n-1)}\quad(i\ne j).}
\]
For \(t>\tau_n\) its ball touches precisely the \(\binom n2\) off-diagonal-coordinate hyperplanes; at equality \(t=\tau_n\), all \(n+\binom n2\) coordinate hyperplanes touch. Thus the incenter dimension collapses from \(n(n-3)/2\) to zero at one explicit parameter value, even though the polytope has affine dimension \(n(n-1)/2-1\) throughout \(0<t<n\).

## Assumptions and scope
The parameter is real, not necessarily integral. Each \(\mathcal S_n(t)\) has a strictly positive point \(C_t\), whose diagonal entries are \(t/n\) and off-diagonal entries are \((n-t)/(n(n-1))\). Therefore the affine dimension is constant for \(0<t<n\). The asserted inball is intrinsic to this affine space; it is not a ball in the whole \(n^2\)-dimensional matrix space. The two endpoints \(t=0,n\) are omitted because their affine hulls have smaller dimension, and the limiting inradius formula need not equal the endpoint's intrinsic inradius. The matrix convention gives each undirected edge two symmetric off-diagonal entries; all metric projections and radii use this Frobenius convention.

## Proof
**1. Tangent space and the two exact coordinate-normal lengths.** Write \(J=\mathbf1\mathbf1^{\mathsf T}\) and \(P=I-J/n\). The linear translation space is
\[
L=\{H=H^{\mathsf T}:H\mathbf1=0,\ \operatorname{tr}H=0\}.
\]
For a symmetric ambient matrix \(A\), its Frobenius-orthogonal projection onto \(L\) is
\[
\Pi_L(A)=PAP-\frac{\operatorname{tr}(PAP)}{n-1}P.
\]
Indeed \(A\mapsto PAP\) projects onto symmetric row-zero matrices, and \(P\) spans the trace direction inside that space; \(\|P\|_F^2=\operatorname{tr}P=n-1\). The coordinate functional \(H\mapsto H_{ii}\) has ambient symmetric gradient \(D_i=e_ie_i^{\mathsf T}\), while \(H\mapsto H_{ij}\), for \(i\ne j\), has gradient \(F_{ij}=(e_ie_j^{\mathsf T}+e_je_i^{\mathsf T})/2\). A direct evaluation gives
\[
\boxed{d_n^2:=\|\Pi_L(D_i)\|_F^2=\frac{(n-1)(n-2)}{n^2}},\qquad
\boxed{o_n^2:=\|\Pi_L(F_{ij})\|_F^2=\frac{(n-2)(n^2-n+2)}{2n^2(n-1)}}.
\]
For example, \(\|Pe_i\|^2=(n-1)/n\), \((Pe_i)\cdot(Pe_j)=-1/n\) for distinct indices, and the trace-direction subtractions are respectively \((n-1)/n^2\) and \(1/(n^2(n-1))\). The exact squared lengths follow. Both numbers are positive for \(n\ge4\).

**2. A ball test that does not presuppose facets.** For any \(X\) in the affine space, the radius-\(r\) Frobenius ball centered at \(X\), restricted to the affine space, lies in \(\mathcal S_n(t)\) if and only if
\[
X_{ii}\ge r d_n\ (1\le i\le n),\qquad
X_{ij}\ge r o_n\ (1\le i<j\le n).
\]
This follows by minimizing each coordinate functional over the ball using its projected gradient, and intersecting the resulting coordinate halfspaces; the other affine constraints are automatic. No assertion that the orthogonal foot lies in the relative interior of a facet is needed.

**3. Sharpness.** Summing the diagonal inequalities and using \(\sum_iX_{ii}=t\) gives \(r\le t/(nd_n)\). Summing the off-diagonal inequalities, counting both symmetric entries in the full row sum \(\sum_{ij}X_{ij}=n\), gives \(r\le(n-t)/(n(n-1)o_n)\). At the permutation-invariant feasible matrix \(C_t\), every diagonal inequality has clearance \(t/(nd_n)\), and every off-diagonal inequality has clearance \((n-t)/(n(n-1)o_n)\). Thus their minimum is achieved globally. Substituting the exact normal lengths yields the displayed radius. Equating the two clearances gives exactly \(t=\tau_n\).

**4. Every optimizer.** In the low-trace case, equality in the sharp diagonal sum forces \(X_{ii}=r d_n=t/n\) for every \(i\). For all off-diagonal positions, the sharp ball condition becomes \(X_{ij}\ge\lambda=r o_n\). Subtract \(\lambda\) from each off-diagonal and note that every residual row sum equals
\[
\frac{n-t}{n}-(n-1)\lambda=\beta.
\]
Since \(\beta>0\), dividing these residual entries by \(\beta\) establishes the exact bijection with \(\mathcal F_n\). The uniform strictly positive \(Y_{ij}=1/(n-1)\) shows that the incenter locus has the full affine dimension of \(\mathcal F_n\). The off-diagonal edge-incidence matrix of \(K_n\) has rank \(n\): any row dependence has \(a_i+a_j=0\) on every edge, hence \(a_i=0\) by considering a triangle. Therefore \(\dim\mathcal F_n=\binom n2-n=n(n-3)/2\).

In the high-trace case, equality in the off-diagonal sum forces **every** \(X_{ij}\) for \(i\ne j\) to equal \((n-t)/(n(n-1))\); the row equations then force every diagonal entry to be \(t/n\). At the threshold, both families of inequalities are equalities and the same unique matrix follows. The ball test immediately proves all contact classifications. The threshold tends to \(\sqrt2\) by division of numerator and denominator by \(n\).

**5. Extreme optimal centers and their counts.** For \(Y\in\mathcal F_n\), a positive-support graph with an even cycle admits a nonzero alternating-edge perturbation preserving every row sum, and so cannot be an extreme point. More generally, the unsigned incidence columns of its positive-support edges must be linearly independent; if not, a sufficiently small signed kernel perturbation remains nonnegative and splits \(Y\). On a connected bipartite support component, independent incidence columns force a tree, and a leaf forces an adjacent weight one, excluding any other positive adjacent edge. Thus the component is a single edge of weight one. On a nonbipartite component, independent columns allow exactly one cycle, necessarily odd. No tree branch can attach because a leaf again forces a weight one and contradicts positivity of the path toward the odd cycle. Consequently the component is an odd cycle with unique weights one-half. Conversely, isolated edges and disjoint odd cycles have independent incidence columns, making their feasible weight assignments extreme. This classical half-integral characterization appears in general form in Behrend's study of fractional perfect matching polytopes; it is used here to classify the new incenter locus, not claimed as a new matching-polytope theorem.

The exponential formula for labeled assemblies counts a paired block on two labels in exactly one way and an undirected odd cycle on \(\ell\) labels in \((\ell-1)!/2\) ways. Its exponential generating function is the one displayed, and its first relevant coefficients give \(f_4=3\), \(f_5=22\), \(f_6=25\). This completes the classification.

## Verification
The included `check_trace_symmetric_stochastic.py` constructs an independent symmetric-matrix orthonormal basis and computes the projected coordinate-functional norms by SVD rather than by the projection formula in the proof. For each integer \(4\le n\le10\), it then solves seven unrestricted linear programs whose variables are all independent symmetric matrix entries and a candidate radius, with row sums, prescribed trace, and every projected coordinate-normal inequality. All 49 resulting radii agree with the closed formula. It also checks the explicit low-trace affine incenter construction. These finite computations independently corroborate algebraic identities and boundary cases; the proof above establishes the entire real-parameter, all-dimension statement.

## Relationship to prior work
Brualdi and Cao (arXiv:1712.03129, first public 2017-12-08) characterize vertices and related combinatorics of symmetric doubly stochastic polytopes; their paper does not impose a trace slice or determine intrinsic Euclidean inscribed balls. Bouthat, Mashreghi, and Morneau-Guérin (arXiv:2310.14043, first public 2023-10-21) study Schatten-metric **minimum enclosing** balls for the ordinary Birkhoff polytope, a different containment direction and affine space. Behrend (arXiv:1301.7356) gives a general theory of fractional perfect matching polytopes and the already-known odd-cycle vertex structure; identifying such a polytope as an entire family of inball centers in a trace-sliced symmetric stochastic polytope is separate. Existing exact inradius formulas for unconstrained transportation polytopes concern independently variable matrix entries with fixed row and column sums, and do not imply the trace-constrained symmetric tangent-space metric formula. A different family of partial assignment polytopes also has incenter loci isomorphic to a Birkhoff polytope, but differs in constraints, normal orbits, threshold, and optimizer geometry.

## Limitations
All inball claims are for \(n\ge4\) and \(0<t<n\), with real entries and the intrinsic Frobenius metric. No assertion is made at the dimension-changing endpoint slices. The matching-polytope vertex characterization is credited prior work. The literature searches and examined sources are finite; differently formulated metric results in older matrix geometry could still exist. Independent mathematical review has not been performed.

## References
1. Richard A. Brualdi and Lei Cao, *Symmetric, Hankel-symmetric, and Centrosymmetric Doubly Stochastic Matrices*, arXiv:1712.03129, first version 2017-12-08; Acta Mathematica Vietnamica 43 (2018), 675–700. https://arxiv.org/abs/1712.03129
2. Ludovick Bouthat, Javad Mashreghi, and Frédéric Morneau-Guérin, *On the Geometry of the Birkhoff Polytope II: The Schatten \(p\)-norms*, arXiv:2310.14043, first version 2023-10-21. https://arxiv.org/abs/2310.14043
3. Roger E. Behrend, *Fractional Perfect \(b\)-Matching Polytopes. I: General Theory*, arXiv:1301.7356, first version 2013-01-30. https://arxiv.org/abs/1301.7356
