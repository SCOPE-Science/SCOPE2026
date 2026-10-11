# Grounded precision geometry of uniform Cayley-tree edge indicators

## Finding

Let \(T\) be a uniformly random spanning tree of \(K_n\), with \(n\ge6\). For each edge \(e\), define
\[
X_e=\mathbf 1\{e\in T\}.
\]
Let
\[
C=\operatorname{Cov}\bigl((X_e)_{e\in E(K_n)}\bigr).
\]

Write
\[
H=L(K_n)=J(n,2)
\]
for the line graph of \(K_n\). Then
\[
\boxed{
C=\frac1{n^2}L_H.
}
\tag{1}
\]

Equivalently,
\[
\operatorname{Var}(X_e)=\frac{2(n-2)}{n^2},
\]
and for distinct edges
\[
\operatorname{Cov}(X_e,X_f)=
\begin{cases}
-\dfrac1{n^2},&e,f\text{ share one endpoint},\\[1mm]
0,&e,f\text{ are disjoint}.
\end{cases}
\tag{2}
\]

Since every spanning tree has \(n-1\) edges,
\[
\sum_eX_e=n-1
\]
deterministically. Hence
\[
\operatorname{rank}(C)=\binom n2-1,
\qquad
\ker C=\operatorname{span}\{\mathbf 1\}.
\]

Fix any edge \(r\), delete \(X_r\), and let \(C^{(r)}\) be the covariance of the remaining edge indicators. Partition retained edges into
\[
A=\{e:e\cap r\ne\varnothing\},
\qquad
D=\{e:e\cap r=\varnothing\}.
\]
Then \(C^{(r)}\) is positive definite and its precision matrix
\[
P^{(r)}=(C^{(r)})^{-1}
\]
is strictly positive entrywise.

Its diagonal entries are
\[
\boxed{
P^{(r)}_{ee}
=
\frac{n(n+1)}{n-1}
\quad(e\in A),
}
\tag{3}
\]
\[
\boxed{
P^{(r)}_{ee}
=
\frac{n(n+2)}{n-1}
\quad(e\in D).
}
\tag{4}
\]

For distinct retained edges:
\[
\boxed{
P^{(r)}_{ef}
=
\frac{n(n+1)}{2(n-1)}
\quad(e,f\in A,\ e\sim f),
}
\tag{5}
\]
\[
\boxed{
P^{(r)}_{ef}
=
\frac{n^2}{2(n-1)}
\quad(e,f\in A,\ e\cap f=\varnothing),
}
\tag{6}
\]
\[
\boxed{
P^{(r)}_{ef}
=
\frac{n(n+2)}{2(n-1)}
\quad(e\in A,\ f\in D,\ e\sim f),
}
\tag{7}
\]
\[
\boxed{
P^{(r)}_{ef}
=
\frac{n(n+1)}{2(n-1)}
\quad(e\in A,\ f\in D,\ e\cap f=\varnothing),
}
\tag{8}
\]
\[
\boxed{
P^{(r)}_{ef}
=
\frac{n(n+3)}{2(n-1)}
\quad(e,f\in D,\ e\sim f),
}
\tag{9}
\]
\[
\boxed{
P^{(r)}_{ef}
=
\frac{n(n+2)}{2(n-1)}
\quad(e,f\in D,\ e\cap f=\varnothing).
}
\tag{10}
\]

Therefore every off-diagonal precision entry is positive. The full-order linear partial correlations are all strictly negative. In the six cases (5)--(10), respectively, they equal
\[
\boxed{
-\frac12,\quad
-\frac{n}{2(n+1)},\quad
-\frac12\sqrt{\frac{n+2}{n+1}},\quad
-\frac12\sqrt{\frac{n+1}{n+2}},\quad
-\frac{n+3}{2(n+2)},\quad
-\frac12.
}
\tag{11}
\]

Thus two disjoint edge indicators are marginally independent but become strictly negatively correlated after full linear adjustment once the single deterministic edge-count redundancy is removed.

## Assumptions and scope

The tree is uniform over the \(n^{n-2}\) labeled spanning trees of \(K_n\).

The condition \(n\ge6\) ensures that all six off-diagonal orbit types occur. Formula (1) and the existing orbit formulas remain valid for smaller admissible \(n\).

Deleting one edge coordinate removes the deterministic relation \(\sum_eX_e=n-1\). Any edge can be deleted, and every choice is equivalent by symmetry.

“Linear partial correlation” means correlation after least-squares residualization. The indicator vector is not Gaussian, so these are not asserted to be nonlinear conditional correlations.

## Proof

Orient the edges of \(K_n\) arbitrarily and let \(B\) be the oriented incidence matrix. The graph Laplacian is
\[
L_{K_n}=nI-J,
\]
so
\[
L_{K_n}^{+}
=
\frac1n\left(I-\frac1nJ\right).
\]

The transfer-current theorem gives the uniform-spanning-tree determinantal kernel
\[
K=B^\top L_{K_n}^{+}B
=
\frac1nB^\top B.
\tag{12}
\]
Thus
\[
\Pr(e\in T)=K_{ee}=\frac2n.
\tag{13}
\]

For distinct edges,
\[
\Pr(e,f\in T)
=
K_{ee}K_{ff}-K_{ef}^2.
\tag{14}
\]
If \(e,f\) share one endpoint, then \(|B_e^\top B_f|=1\), so
\[
\Pr(e,f\in T)=\frac3{n^2}.
\]
If they are disjoint, then \(B_e^\top B_f=0\), so
\[
\Pr(e,f\in T)=\frac4{n^2}.
\]
Together with (13), this proves (1)--(2).

Now let \(U\) be the unsigned incidence matrix of \(K_n\). Then
\[
U^\top U=2I+A_H,
\]
hence
\[
L_H=2(n-1)I-U^\top U.
\tag{15}
\]
Also
\[
UU^\top=(n-2)I+J.
\tag{16}
\]
Therefore the nonzero eigenvalues of \(L_H\) are \(n\) and \(2(n-1)\). A direct projector calculation yields
\[
C^+
=
\frac{n^2}{2(n-1)}I
+
\frac{n}{2(n-1)}U^\top U
-
\frac{3n-2}{(n-1)^2}J.
\tag{17}
\]

For a connected graph Laplacian, grounding at \(r\) gives
\[
(C^{(r)})^{-1}_{ef}
=
C^+_{ef}-C^+_{er}-C^+_{rf}+C^+_{rr}.
\tag{18}
\]
The \(J\)-term cancels. Put
\[
q_{ef}=(U^\top U)_{ef}.
\]
Then \(q_{ee}=2\), while for distinct edges \(q_{ef}=1\) if they meet and \(q_{ef}=0\) if they are disjoint. Thus
\[
(C^{(r)})^{-1}_{ef}
=
\frac{n^2}{2(n-1)}(1+\mathbf 1_{\{e=f\}})
+
\frac{n}{2(n-1)}
\bigl(q_{ef}-q_{er}-q_{fr}+2\bigr).
\tag{19}
\]
Substitution gives (3)--(10).

For any positive-definite covariance matrix,
\[
\rho^{\mathrm{lin}}_{ef\cdot-(e,f)}
=
-\frac{P^{(r)}_{ef}}
{\sqrt{P^{(r)}_{ee}P^{(r)}_{ff}}}.
\tag{20}
\]
Using (3)--(10) gives (11).

## Verification

The accompanying checker exhaustively generates every labeled tree through \(n=7\) using Prüfer sequences. It recomputes one-edge and two-edge inclusion probabilities and verifies (1)--(2).

For each \(4\le n\le12\), it builds the grounded covariance and the proposed orbitwise precision matrix, then verifies their product is exactly the identity using rational arithmetic.

It also verifies every realized squared partial-correlation formula together with its negative sign.

The replay is supplementary. The universal proof is the transfer-current calculation and grounded line-graph inversion above.

## Relationship to prior work

Burton and Pemantle give the transfer-impedance determinant formula for finite-dimensional marginals of a uniform spanning tree. Their full treatment explicitly places the problem in combinatorial probability and supplies the local probabilities used here. It does not state the complete \(K_n\) edge covariance as a line-graph Laplacian, invert a grounded covariance, or classify full-order linear partial correlations.

Grimmett and Winkler review negative association for uniform spanning trees while studying analogous dependence questions for forests and connected subgraphs. This gives the qualitative negative-dependence context, but negative association alone does not determine the precision matrix.

General grounded-Laplacian theory explains entrywise inverse positivity once (1) is known. The additional content here is the exact Cayley-tree covariance identification and the complete six-class formulas (3)--(11).

Targeted searches for Cayley-tree edge-indicator precision, grounded inverse covariance, line-graph covariance, and spanning-tree edge partial correlations did not locate these formulas.

## Limitations

For a general host graph, uniform-spanning-tree covariance need not collapse to the two-orbit line-graph form in (1).

The full covariance is singular because tree size is fixed. The reported partial correlations therefore refer to a grounded coordinate system after one redundant edge indicator is removed.

Grounded-Laplacian inverse positivity is classical. The originality claim is limited to the exact uniform-Cayley-tree covariance, six precision orbit values, and their statistical interpretation.

Older electrical-network or distance-regular-graph literature may contain an equivalent specialization under different notation.

## References

1. R. Burton and R. Pemantle, “Local Characteristics, Entropy and Limit Theorems for Spanning Trees and Domino Tilings via Transfer-Impedances,” arXiv:math/0404048, first submitted 2004-04-02; *The Annals of Probability* 21 (1993), 1329–1371.
2. G. R. Grimmett and S. N. Winkler, “Negative association in uniform forests and connected graphs,” arXiv:math/0302185, first submitted 2003-02-17; DOI 10.1002/rsa.20012.
