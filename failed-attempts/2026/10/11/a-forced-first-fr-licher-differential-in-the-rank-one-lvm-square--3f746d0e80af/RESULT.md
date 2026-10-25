# A forced first Frölicher differential in the rank-one LVM square

## Finding

Let
\[
\pi:\mathscr X\longrightarrow\Delta
\]
be the proper holomorphic family of polytopal LVM fourfolds constructed in Theorem 12.7 of the recent source. Its fibres are all diffeomorphic, the central fibre \(X_0\) has curvature rank one, and every fibre \(X_t\) with \(t\ne0\) has full curvature rank two.

On the rank-one central fibre, the first Frölicher differential
\[
d_1^{0,1}:
H_{\bar\partial}^{0,1}(X_0)
\longrightarrow
H_{\bar\partial}^{1,1}(X_0)
\]
has exact rank
\[
\operatorname{rank}d_1^{0,1}=1.
\]
Equivalently,
\[
\dim\ker d_1^{0,1}=1
\]
and
\[
E_2^{0,1}(X_0)=E_\infty^{0,1}(X_0)\cong\mathbb C.
\]

Thus the family exhibits an explicit rank jump of a Frölicher differential:
\[
\operatorname{rank}d_1^{0,1}(X_t)
=
\begin{cases}
1,&t=0,\\
0,&t\ne0.
\end{cases}
\]

This identifies a concrete differential at deficient curvature rank. It does not determine the other first differentials or the complete later-page spectral sequence.

## Assumptions and scope

The family \(X_t\), its Hodge polynomials, and its topological identification are exactly those of arXiv:2609.37936v1.

The Frölicher spectral sequence is indexed by
\[
E_1^{p,q}=H_{\bar\partial}^{p,q}(X)
\]
with differential
\[
d_r:E_r^{p,q}\longrightarrow E_r^{p+r,q-r+1}.
\]

The argument uses only the source Hodge numbers
\[
h^{0,1}(X_0)=2,
\qquad
h^{1,0}(X_0)=1,
\qquad
h^{2,0}(X_0)=0,
\]
the source identity
\[
b_1(X_0)=2,
\]
and standard convergence of the Frölicher spectral sequence to de Rham cohomology.

No assertion is made that the central fibre degenerates at \(E_2\).

## Proof

For the rank-one square, Proposition 12.1 of the source gives the Hodge rows
\[
\begin{array}{c|ccccc}
p\backslash q&0&1&2&3&4\\
\hline
0&1&2&1&0&0\\
1&1&3&3&1&0\\
2&0&2&4&2&0\\
3&0&1&3&3&1\\
4&0&0&1&2&1.
\end{array}
\]
In particular,
\[
\dim E_1^{0,1}=2,
\qquad
\dim E_1^{1,0}=1,
\qquad
E_1^{2,0}=0.
\]

We first show that
\[
E_\infty^{1,0}=E_1^{1,0}.
\]
The only incoming \(d_1\) is
\[
d_1:E_1^{0,0}\longrightarrow E_1^{1,0}.
\]
It is induced by \(\partial\), and therefore annihilates the constant class spanning
\[
H_{\bar\partial}^{0,0}(X_0).
\]
The outgoing first differential
\[
d_1:E_1^{1,0}\longrightarrow E_1^{2,0}
\]
is zero because its target is zero.

For \(r\ge2\), an incoming differential to bidegree \((1,0)\) would originate at a negative holomorphic index, while an outgoing differential would have antiholomorphic index
\[
1-r<0.
\]
Thus no later differential can affect the class. Hence
\[
\dim E_\infty^{1,0}=1.
\]

Lemma 11.12 of the source gives
\[
b_1(X_0)=m=2.
\]
Since the Frölicher spectral sequence converges to de Rham cohomology, the associated graded pieces in total degree one satisfy
\[
b_1(X_0)
=
\dim E_\infty^{1,0}
+
\dim E_\infty^{0,1}.
\]
Therefore
\[
\dim E_\infty^{0,1}=1.
\]

There is no incoming differential to any
\[
E_r^{0,1}.
\]
At the first page the only possible outgoing map is
\[
d_1^{0,1}:E_1^{0,1}\longrightarrow E_1^{1,1}.
\]
If a class survives it, the next possible outgoing map is
\[
d_2:E_2^{0,1}\longrightarrow E_2^{2,0}.
\]
But
\[
E_2^{2,0}=0
\]
because already
\[
E_1^{2,0}=0.
\]
For \(r\ge3\), the target has negative antiholomorphic index. Consequently
\[
E_\infty^{0,1}
=
E_2^{0,1}
=
\ker d_1^{0,1}.
\]

The domain has dimension \(2\) and the kernel has dimension \(1\), so
\[
\operatorname{rank}d_1^{0,1}=1.
\]

For \(t\ne0\), Theorem 12.7 states that the Frölicher spectral sequence of \(X_t\) degenerates at \(E_1\). Hence every first differential vanishes, in particular
\[
d_1^{0,1}(X_t)=0.
\]
This proves the claimed rank jump.

## Verification

The primary source was inspected at the rank-one square Hodge diamond, the first-Betti-number lemma, the general deficient-rank Frölicher obstruction, and the proper holomorphic square family. The source explicitly states that the central rank-one fibre does not degenerate at \(E_1\), while the punctured fibres do.

The bidegree argument was checked page by page. The group
\[
E_1^{2,0}
\]
vanishes, so neither the holomorphic one-form in bidegree \((1,0)\) nor a class in
\[
E_2^{0,1}
\]
can be killed by the only potentially relevant outgoing maps. Total-degree-one convergence then fixes the kernel dimension uniquely.

Earlier moment-angle work was also inspected. In a rational moment-angle setting it identifies
\[
d_1:E_1^{0,1}\to E_1^{1,1}
\]
as the relevant first differential and proves \(E_2\)-degeneration there. The recent source treats the deficient-curvature LVM setting separately and explicitly lists computation of its Frölicher differentials as a remaining problem.

No numerical experiment or finite enumeration is used.

## Relationship to prior work

The recent Dolbeault--Hochster paper computes the entire Hodge diamond of the rank-one square and proves nondegeneration at \(E_1\) from a dimension excess in total degree one. It does not identify which Frölicher differential has nonzero rank. Its introduction explicitly says that computing Frölicher differentials at deficient curvature rank requires a model retaining both
\[
\partial
\quad\text{and}\quad
\bar\partial.
\]

The present result extracts the first forced differential without requiring such a full model. The vanishing
\[
h^{2,0}=0
\]
removes every alternative route by which the excess
\[
h^{1,0}+h^{0,1}-b_1=1
\]
could disappear, so the rank of
\[
d_1^{0,1}
\]
is determined purely by convergence and bidegrees.

Panov--Ustinovsky previously proved \(E_2\)-degeneration for a rational moment-angle class and identified a first differential from \((0,1)\) to \((1,1)\) in that setting. Krutowski--Panov later provided a broad Dolbeault DGA model for complex moment-angle manifolds. These works supply the closest general mechanism, but the new source explicitly separates the deficient-curvature square from the settings where those models compute the required differential.

Targeted searches for the rank-one square, deficient curvature, and the exact
\[
d_1^{0,1}
\]
rank did not locate a statement of the result.

## Limitations

Only one differential rank is determined:
\[
d_1^{0,1}.
\]
The image class inside
\[
H_{\bar\partial}^{1,1}(X_0)
\]
is not identified.

No claim is made about the ranks of the other \(d_1\) maps, higher differentials in other bidegrees, or \(E_2\)-degeneration of the central fibre.

The proof is specific to the rank-one square Hodge diamond and its vanishing
\[
h^{2,0}=0.
\]

## References

1. L. Katzarkov, K.-S. Lee, E. Lupercio, and L. Meersseman, *Dolbeault--Hochster Theory of Polytopal LVM Manifolds*, arXiv:2609.37936v1, 2026.
2. T. Panov and Y. Ustinovsky, *Complex-analytic structures on moment-angle manifolds*, Moscow Mathematical Journal 12 (2012), 149--172; arXiv:1008.4764.
3. R. Krutowski and T. Panov, *Dolbeault cohomology of complex manifolds with torus action*, Contemporary Mathematics 772 (2021), 173--187; arXiv:1908.06356v4.
