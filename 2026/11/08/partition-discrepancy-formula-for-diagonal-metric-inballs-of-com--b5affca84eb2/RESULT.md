# Partition-discrepancy formula for diagonal-metric inballs of complete-bipartite symmetric edge polytopes

## Finding

Let \(A\) and \(B\) be nonempty disjoint sets, \(n=|A|+|B|\ge3\), and let
\[
P_{A,B}=\operatorname{conv}\{\pm(e_a-e_b):a\in A,\ b\in B\}
\subset H=\{x\in\mathbb R^n:\sum_i x_i=0\}.
\]
Give \(H\) the positive-definite diagonal metric
\(\|x\|_t^2=\sum_{i=1}^n x_i^2/t_i\), with \(t_i>0\).
Thus this is also the ordinary intrinsic Euclidean metric on the diagonally
scaled polytope \(\operatorname{diag}(t_i^{-1/2})P_{A,B}\).
Write
\[
T_A=\sum_{a\in A}t_a,\quad T_B=\sum_{b\in B}t_b,\quad T=T_A+T_B,
\qquad \delta_S=\min_{\sigma\in\{-1,1\}^{S}}\left|\sum_{i\in S}\sigma_i t_i\right|.
\]
Then the radius of the largest intrinsic metric ball contained in \(P_{A,B}\) is exactly
\[
\boxed{\quad r_t(P_{A,B})^{-2}
=\max\left\{T_A-\frac{\delta_A^2}{T},\;T_B-\frac{\delta_B^2}{T}\right\}.\quad}
\]
An optimal center is the origin. Every facet tangent to its largest ball is
indexed by a sign assignment \(\sigma\in\{-1,1\}^{S}\) on a part \(S\in\{A,B\}\)
for which \(T_S-\delta_S^2/T\) attains the displayed maximum and
\(\left|\sum_{i\in S}\sigma_it_i\right|=\delta_S\).
These, and no other facets, touch the centered ball.

For rational, indeed integer, diagonal metric data the exact-radius threshold problem is already weakly NP-complete on stars: given positive integers \(z_1,\ldots,z_m\) (\(m\ge2\)), equip the symmetric edge polytope of \(K_{m,1}\) with the metric \(\|x\|^2=\sum_{i=1}^m x_i^2/z_i+x_{m+1}^2\) and put \(Z=\sum_i z_i\). Then
\[
\boxed{\quad r^{-2}\ge Z\quad\Longleftrightarrow\quad
\text{the integers }z_1,\ldots,z_m\text{ admit an equal-sum partition}.\quad}
\]
The problem is weakly NP-complete because this is precisely PARTITION and
membership follows from a sign-vector certificate. In particular, the exact
inradius of a diagonal-metric star root polytope captures a natural number-
partitioning discrepancy, despite the simple cross-polytope combinatorics.

In the unweighted case \(t_i=1\), putting \(L=\max(|A|,|B|)\), \(S=\min(|A|,|B|)\),
\(n=L+S\), and \(\varepsilon=L\bmod 2\), the formula becomes
\[
 r^{-2}=L-\frac{\varepsilon}{n}.
\]
The affine dimension of the set of all largest-ball centers is \(S\) if
\(L>S\) and \(L\) is even; \(S-1\) if \(L>S\) and \(L\) is odd;
\(1\) if \(L=S\) is even; and \(0\) if \(L=S\) is odd.

## Assumptions and scope

The metric is restricted from the positive diagonal inner product on ambient
\(\mathbb R^n\) to the intrinsic hyperplane \(H\). All part sizes are at
least one, and \(n\ge3\); no assumption of equal part sizes or of rational
metric weights is needed for the geometric identities. Complexity is assessed
only in the explicitly stated binary-encoded, integer-diagonal family.
Here \(r_t\) is an intrinsic inradius, not an ambient radius in \(\mathbb R^n\).
An affine diagonal deformation of a centrally symmetric polytope remains
centrally symmetric; it need not retain ordinary Euclidean symmetry.

## Proof

**1. Complete facet description.** A linear functional \(f\) supports
\(P_{A,B}\) at height one exactly when
\(\max_{a\in A,b\in B}|f_a-f_b|=1\). Modulo constant vectors, its feasible
set is the polar Lipschitz polytope
\(\{f:|f_a-f_b|\le1\}\). A vertex of this polar is characterized by the
edges satisfying equality spanning a connected graph: equality constraints
are edge differences, whose rank equals \(n\) minus the number of connected
components of the tight-edge graph. If values on \(A\) are nonconstant,
connectedness requires some \(b\in B\) tight with two different \(A\)-values;
those values differ by two, and every \(B\)-value must be their midpoint.
All \(A\)-values must then be exactly the two extremes, since every vertex
must have a tight edge. The same reasoning with \(A,B\) exchanged covers
the other case. If one part is constant, tight connectivity requires each
vertex of the other part to have value one unit above or below it. Thus all
facet functionals, modulo constants, are precisely
\[
 f^{S,\sigma}_i=\begin{cases}\sigma_i&i\in S,\\0&i\notin S,\end{cases}
 \qquad S\in\{A,B\},\quad \sigma_i\in\{-1,1\},
\]
with duplicate descriptions identified. This also follows from the
complete-bipartite facet classification of Higashitani--Jochemko--Michałek,
Proposition 3.4 [1].

**2. Intrinsic dual normal norm.** Let
\(M=\operatorname{diag}(t_i^{-1})\), so the squared primal metric is
\(x^{\mathsf T}Mx\). The metric-dual squared norm of \(f|_H\) is the
squared norm of the orthogonal projection, in the \(M\)-metric, of
\(M^{-1}f\) onto \(H\):
\[
\|f|_H\|_{t,*}^{2}
=f^{\mathsf T}\!M^{-1}f-
\frac{(\mathbf1^{\mathsf T}M^{-1}f)^2}{\mathbf1^{\mathsf T}M^{-1}\mathbf1}
=\sum_i t_if_i^2-\frac{(\sum_i t_if_i)^2}{T}.
\]
For \(f=f^{S,\sigma}\) this equals
\(T_S-(\sum_{i\in S}\sigma_it_i)^2/T\).
Therefore the smallest facet distance from zero is the reciprocal square
root of the maximum dual squared norm, giving the stated partition-discrepancy
formula and precisely the tangent-facet description.

**3. Why zero is an optimal center.** Since \(P_{A,B}=-P_{A,B}\), if
\(c+rB_t\subseteq P_{A,B}\), then \(-c+rB_t\subseteq P_{A,B}\).
Convexity implies \(rB_t\subseteq P_{A,B}\), so the origin attains the
largest admissible radius. This argument does not assume uniqueness.

**4. Complexity on stars.** Let \(B\) be the singleton with \(t_b=1\),
and let \(T_A=Z\). The only sign pattern on \(B\) has discrepancy one, and
its dual squared norm is \(1-1/(Z+1)=Z/(Z+1)\).
For \(|A|\ge2\), reversing the sign on any proper nonempty subset gives a
signed sum strictly smaller in absolute value than \(Z\). Hence
\(\delta_A<Z\) and
\[
Z-\frac{\delta_A^2}{Z+1}>\frac Z{Z+1}.
\]
It follows that \(r^{-2}=Z-\delta_A^2/(Z+1)\), which reaches \(Z\)
exactly for a zero-discrepancy partition. The transformation from a
PARTITION instance to \(M=\operatorname{diag}(1/z_1,\ldots,1/z_m,1)\)
is polynomial-time in the binary input length. A sign vector certifies a
yes-instance in polynomial time. The inherited weak NP-completeness is not
a strong NP-hardness statement.

**5. Unweighted center dimension.** For \(t_i=1\), maximize
\(\|f^{S,\sigma}|_H\|^2=|S|-(\sum\sigma_i)^2/n\). The larger part
strictly wins if the part sizes differ, since the possible deficit is at
most \(1/n\); the two parts tie when their sizes coincide. On an even-sized
maximizing part, the balanced signs span precisely the zero-sum subspace of
that part (dimension \(L-1\)). On an odd-sized maximizing part of size at
least three, the minimum-imbalance signs span the entire coordinate space
(dimension \(L\)). Projection to \(H\) is injective on vectors supported
in one proper part. For equal parts, the two spans combine to dimension
\(n-2\) when both are even, and \(n-1\) when both are odd.
Every optimal center must annihilate all tangent-facet normals (their
opposites are also tangent). Conversely, every sufficiently small vector
annihilating those normals is an optimal center because all other facet
inequalities have strictly positive slack at zero. Subtracting these ranks
from \(\dim H=n-1\) gives the four cases.

## Verification

The standalone \`verify.py\` uses exact rational arithmetic. It explicitly
enumerates every bounded integer labeling with one value fixed to zero,
retains those with connected tight-edge graph, and compares their maximal
intrinsic dual squared norm with the discrepancy formula for 42 small
integer-weight profiles. It checks the star-PARTITION equivalence on seven
instances and independently verifies the unweighted incenter dimension by
exact Gaussian elimination on 24 part-size profiles. The observed output is
\`DIAGONAL_BICLIQUE_INBALL_CHECKS_PASSED\`. Finite testing is ancillary;
the proof is the all-dimensional argument above. Run with \`python verify.py\`;
only the Python standard library is needed.

## Relationship to prior work

Higashitani, Jochemko, and Michałek [1] establish the complete
combinatorial classification of biclique symmetric-edge-polytope facets,
including precisely the sign labels used in Step 1. This known classification
is a premise, not a novelty claim. Chen, Davis, and Korchevskaia [2] develop
facet-subgraph correspondences for symmetric edge polytopes, likewise without
specifying the diagonal-metric inradius. Gordon and Petrov [3] study the
combinatorics of Lipschitz polytopes, which provides a related polar language.
The contribution isolated here is the exact metric-dual discrepancy
optimization, its geometric contact consequences, and the resulting
weak NP-completeness on a fixed simple graph family. They are not asserted
to be independent of the pre-existing facet description, and unweighted
star radii are already independently known; those results are not claimed
as new.

## Limitations

No claim is made of a polynomial-time exact algorithm for arbitrary
rational weights, strong NP-hardness, or a complete closed-form enumeration
of all optimizing sign assignments. The formula reduces this task to two
finite weighted partition problems. The complexity theorem concerns an
exact rational-metric decision problem, not floating-point approximation.
The possible existence of an earlier equivalent result phrased as a
weighted Lipschitz-polytope circumradius or a weighted-variance extremum
remains a priority risk. This manuscript has not undergone independent audit.

## References

[1] A. Higashitani, K. Jochemko, M. Michałek, *Arithmetic aspects of
symmetric edge polytopes*, arXiv:1807.07678v1 (first public version
2018-07-20), especially Theorem 3.1 and Proposition 3.4.
https://arxiv.org/abs/1807.07678

[2] T. Chen, R. Davis, E. Korchevskaia, *Facets and facet subgraphs of
symmetric edge polytopes*, arXiv:2107.12315 (first posted 2021).
https://arxiv.org/abs/2107.12315

[3] J. Gordon, F. Petrov, *Combinatorics of the Lipschitz polytope*,
Arnold Math. J. 3 (2017), 205--218; arXiv:1608.06848.
https://arxiv.org/abs/1608.06848
