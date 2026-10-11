# Alternating precision geometry of triangle indicators in an Erdős–Rényi graph

## Finding

Let
\[
G\sim G(n,p),
\qquad
n\ge6,
\qquad
0<p<1.
\]
For each three-vertex set
\[
S\in\binom{[n]}3,
\]
let
\[
Y_S=\mathbf 1\{S\text{ spans a triangle in }G\}.
\]
Write
\[
C=\operatorname{Cov}\bigl((Y_S)_{S\in\binom{[n]}3}\bigr).
\]

Put
\[
\nu=p^3(1-p^3),
\qquad
r=\frac{p^2}{1+p+p^2}.
\tag{1}
\]
For two triangles define the Johnson distance
\[
d(S,T)=3-|S\cap T|.
\]
Thus \(d=1\) means that the triangles share an edge, \(d=2\) means that they share exactly one vertex, and \(d=3\) means that they are disjoint.

The covariance matrix is
\[
\boxed{
C=\nu(I+rA),
}
\tag{2}
\]
where \(A\) is the adjacency matrix of the Johnson graph \(J(n,3)\).

Define
\[
\Delta
=
(1-3r)
(1+(n-7)r)
(1+(2n-9)r)
(1+3(n-3)r),
\tag{3}
\]
\[
Q
=
1+(5n-26)r+3(2n-9)(n-7)r^2,
\tag{4}
\]
and
\[
B
=
\Delta+3(n-3)r^2Q.
\tag{5}
\]
Then
\[
\boxed{
(C^{-1})_{ST}
=
\frac1{\nu}\,b_{d(S,T)},
}
\tag{6}
\]
where
\[
\boxed{
b_0=\frac{B}{\Delta},
\qquad
b_1=-\frac{rQ}{\Delta},
\qquad
b_2=\frac{4r^2(1+3(n-6)r)}{\Delta},
\qquad
b_3=-\frac{36r^3}{\Delta}.
}
\tag{7}
\]

Hence the precision signs alternate with Johnson distance:
\[
b_1<0,
\qquad
b_2>0,
\qquad
b_3<0.
\tag{8}
\]

For distinct triangles, define the full-order linear partial correlation as the correlation of the two least-squares residuals after projecting each indicator onto the linear span of all remaining triangle indicators. Since every diagonal precision entry is \(b_0/\nu\),
\[
\rho^{\mathrm{lin}}_{ST\cdot-\{S,T\}}
=
-\frac{b_{d(S,T)}}{b_0}.
\]
Therefore
\[
\boxed{
\rho^{\mathrm{lin}}_1
=
\frac{rQ}{B}>0,
}
\tag{9}
\]
\[
\boxed{
\rho^{\mathrm{lin}}_2
=
-\frac{4r^2(1+3(n-6)r)}{B}<0,
}
\tag{10}
\]
and
\[
\boxed{
\rho^{\mathrm{lin}}_3
=
\frac{36r^3}{B}>0.
}
\tag{11}
\]

The marginal and linearly adjusted dependence patterns are therefore qualitatively different. Edge-sharing triangles are positively correlated both marginally and after full linear adjustment. Triangles sharing only one vertex are marginally independent but have negative full-order linear partial correlation. Disjoint triangles are marginally independent but have positive full-order linear partial correlation.

## Assumptions and scope

The graph is the homogeneous Erdős–Rényi model with independent edges and fixed \(0<p<1\).

The vector contains indicators of all labeled three-vertex subsets. The theorem is stated for \(n\ge6\), where all four Johnson distances \(0,1,2,3\) occur.

“Linear partial correlation” means residual correlation after least-squares projection. The triangle-indicator vector is not Gaussian, so these quantities are not asserted to equal nonlinear conditional correlations and do not imply conditional independence.

## Proof

For any triangle \(S\),
\[
\mathbb EY_S=p^3
\]
and
\[
\operatorname{Var}(Y_S)
=
p^3(1-p^3)
=
\nu.
\tag{12}
\]

If \(S\) and \(T\) share an edge, their union contains five distinct required edges. Hence
\[
\mathbb E(Y_SY_T)=p^5,
\]
and
\[
\operatorname{Cov}(Y_S,Y_T)
=
p^5-p^6
=
p^5(1-p).
\tag{13}
\]
Using
\[
1-p^3=(1-p)(1+p+p^2),
\]
the ratio of (13) to (12) is exactly the \(r\) in (1).

If \(S\) and \(T\) share at most one vertex, their required edge sets are disjoint. The two indicators are therefore independent. This proves (2).

The covariance is positive definite. Indeed, the independent edge variables have full support on the Boolean edge cube because \(0<p<1\). A zero-variance linear combination of the triangle indicators would therefore be constant on the entire cube. The triangle indicators are distinct square-free monomials in the edge coordinates, so linear independence of multilinear monomials forces every coefficient to vanish.

Set
\[
M=I+rA.
\]
The permutation group on the graph vertices acts transitively on ordered pairs of triangles at each Johnson distance. Since \(M^{-1}\) commutes with this action, there are numbers \(b_0,b_1,b_2,b_3\) such that
\[
(M^{-1})_{ST}=b_{d(S,T)}.
\tag{14}
\]

Fix triangles \(S,T\) at distance \(e\). Count neighbors \(Z\) of \(S\) according to their distance from \(T\). The four rows of counts are
\[
e=0:
\qquad
(0,\;3(n-3),\;0,\;0),
\]
\[
e=1:
\qquad
(1,\;n-2,\;2(n-4),\;0),
\]
\[
e=2:
\qquad
(0,\;4,\;2(n-4),\;n-5),
\]
and
\[
e=3:
\qquad
(0,\;0,\;9,\;3(n-6)).
\tag{15}
\]
Each row sums to the Johnson degree
\[
3(n-3).
\]

The identity
\[
MM^{-1}=I
\]
therefore reduces exactly to
\[
b_0+3(n-3)rb_1=1,
\tag{16}
\]
\[
rb_0+(1+(n-2)r)b_1+2(n-4)rb_2=0,
\tag{17}
\]
\[
4rb_1+(1+2(n-4)r)b_2+(n-5)rb_3=0,
\tag{18}
\]
and
\[
9rb_2+(1+3(n-6)r)b_3=0.
\tag{19}
\]

Solving (16)--(19) gives (7). This is a direct four-variable calculation; no spectral decomposition is needed.

It remains to verify the signs. First,
\[
0<r<\frac13,
\]
because
\[
3p^2<1+p+p^2
\]
is equivalent to
\[
(2p+1)(p-1)<0.
\]
Thus every factor in \(\Delta\) is positive when \(n\ge6\): in the only potentially decreasing factor,
\[
1+(n-7)r\ge1-r>0.
\]

For \(n\ge7\), every coefficient in
\[
Q
=
1+(5n-26)r+3(2n-9)(n-7)r^2
\]
is nonnegative and the constant term is positive. For \(n=6\),
\[
Q=1+4r-9r^2>1+r>0,
\]
because \(r<1/3\). Therefore
\[
\Delta>0,
\qquad
Q>0,
\qquad
B>0.
\]
The signs in (8) follow immediately from (7).

Finally, the standard precision identity for least-squares partial correlations gives
\[
\rho^{\mathrm{lin}}_{ST\cdot-\{S,T\}}
=
-\frac{(C^{-1})_{ST}}
{\sqrt{(C^{-1})_{SS}(C^{-1})_{TT}}}.
\]
All diagonal entries are equal, so substituting (7) yields (9)--(11).

## Verification

The accompanying exact-rational checker reconstructs the Johnson neighbor-distance counts directly from three-subsets and verifies all four rows in (15) for a range of \(n\).

For rational values of \(p\), it then checks (16)--(19), the positivity of \(\Delta,Q,B\), the alternating precision signs, and the exact partial-correlation formulas using rational arithmetic.

Finally, it materializes the complete matrix \(M\) and the distance-class matrix defined by (7) for several graph sizes and verifies the matrix product exactly entry by entry.

The finite replay is supplementary. The all-\(n\), all-\(p\) theorem follows from the covariance calculation, the orbit reduction, the exact neighbor counts, and the solved linear system.

## Relationship to prior work

Reinert and Röllin study edge, two-star, and triangle counts jointly in Bernoulli random graphs. Their random-graph section computes covariance formulas for those aggregate counts and develops a multivariate normal approximation. Their object is the low-dimensional count vector, not the covariance matrix of all individual triangle indicators.

Chatterjee's triangle-count work also treats the local dependence created by overlap of triangle vertex sets. In its localization argument, triples are partitioned according to whether they share zero, one, or at least two vertices with a fixed triple. That overlap structure is consistent with the covariance sparsity used here, but the paper addresses upper-tail probabilities for the total triangle count rather than precision or partial correlations of the indicator vector.

The matrix \(A\) in (2) is the Johnson graph \(J(n,3)\) adjacency matrix. Johnson-scheme spectral theory is classical, so no novelty is claimed for recognizing that symmetry class. The contribution is the exact specialization of the random-graph covariance inverse, including the closed distance-class coefficients and the resulting alternating partial-correlation law.

Targeted searches for triangle-indicator inverse covariance, precision matrices, Johnson-graph resolvents in this probabilistic role, and triangle-indicator partial correlations did not locate the statement (6)--(11).

## Limitations

The theorem concerns only second-order linear adjustment. It does not classify nonlinear conditional dependence among triangle indicators.

The homogeneous independent-edge model is essential to the simple Johnson form. Inhomogeneous edge probabilities generally destroy the four-orbit reduction.

The inverse calculation is elementary association-scheme algebra once the covariance is recognized as \(I+rA\). Older algebraic-combinatorics literature may contain an equivalent resolvent formula for \(J(n,3)\); the principal originality claim is the probabilistic precision interpretation and sign classification.

## References

1. G. Reinert and A. Röllin, “U-statistics and random subgraph counts: Multivariate normal approximation via exchangeable pairs and embedding,” arXiv:0912.3425, first submitted 2009-12-17; *Journal of Applied Probability* 47 (2010), 378–393.
2. S. Chatterjee, “The missing log in large deviations for triangle counts,” arXiv:1003.3498, first submitted 2010-03-18.
