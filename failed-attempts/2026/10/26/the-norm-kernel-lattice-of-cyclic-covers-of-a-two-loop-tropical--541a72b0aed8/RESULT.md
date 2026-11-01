# The norm-kernel lattice of cyclic covers of a two-loop tropical rose

## Finding

Let \(R\) be a two-loop metric rose with loop lengths \(a,b>0\). For every integer \(n\ge2\), in the connected cyclic \(n\)-cover \(\widetilde R_n\to R\) whose two loop monodromies are both \(1\in\mathbb Z/n\mathbb Z\), the integral cycle lattice of the connected norm kernel \(\ker(\mathrm{Nm}:J(\widetilde R_n)\to J(R))^0\) is \(A_{n-1}=\{x\in\mathbb Z^n:\sum_{i=0}^{n-1}x_i=0\}\), and the restriction of the ambient Jacobian quadratic form is \((a+b)\sum_{i=0}^{n-1}x_i^2\); consequently its Gram determinant is \(n(a+b)^{n-1}\).

## Assumptions and scope

Let the base metric graph be the rose with one vertex and two oriented loops of positive real lengths \(a\) and \(b\). For each integer \(n\ge2\), the cover considered here is the connected cyclic cover whose two loop generators both map to the generator \(1\in\mathbb Z/n\mathbb Z\). The quadratic form is the unscaled restriction of the ambient tropical-Jacobian quadratic form to the integral lattice of the identity component of the norm kernel. This is not a claim about a separately normalized principal Prym polarization, and it does not cover arbitrary voltage assignments.

## Proof

Write the vertices of the cover as \(v_i\), indexed by \(i\in\mathbb Z/n\mathbb Z\). There are two edges from \(v_i\) to \(v_{i+1}\): an edge \(a_i\) of length \(a\), and an edge \(b_i\) of length \(b\). Give both edge families the forward orientation.

An integral 1-cycle has edge coefficients \(x_i\) on \(a_i\) and \(y_i\) on \(b_i\). The cycle condition at each vertex is

\[
 x_{i-1}+y_{i-1}=x_i+y_i.
\]

Thus \(x_i+y_i=z\) is independent of \(i\). The norm map on cycle lattices sends this cycle to \((\sum_i x_i,\sum_i y_i)\in H_1(R,\mathbb Z)\cong\mathbb Z^2\), because each lifted edge maps to its corresponding oriented loop. Membership in the norm kernel gives \(\sum_i x_i=\sum_i y_i=0\). Since \(\sum_i y_i=nz-\sum_i x_i\), these equations force \(z=0\), hence \(y_i=-x_i\) for every \(i\) and \(\sum_i x_i=0\). Conversely, every integer vector with zero sum gives such a cycle. The norm-kernel lattice is therefore exactly \(A_{n-1}\).

The ambient Jacobian quadratic form on an edge-coordinate cycle is

\[
 Q(x,y)=\sum_{i=0}^{n-1}(a x_i^2+b y_i^2).
\]

On the norm kernel, \(y_i=-x_i\), so

\[
 Q|_{A_{n-1}}(x)=(a+b)\sum_{i=0}^{n-1}x_i^2.
\]

In the basis \(e_0-e_1,e_1-e_2,\ldots,e_{n-2}-e_{n-1}\) of \(A_{n-1}\), the Gram matrix is \((a+b)\) times the Cartan matrix of type \(A_{n-1}\): it has diagonal entries \(2\), entries \(-1\) immediately above and below the diagonal, and zero elsewhere. If \(D_k\) is the determinant of the size-\(k\) tridiagonal matrix with this pattern, expansion along the last row gives \(D_0=1\), \(D_1=2\), and \(D_k=2D_{k-1}-D_{k-2}\). Induction yields \(D_k=k+1\). Taking \(k=n-1\) gives determinant \(n\), and scaling a rank-\((n-1)\) Gram matrix by \(a+b\) multiplies its determinant by \((a+b)^{n-1}\). The claimed determinant follows.

## Verification

The proof is symbolic and applies to every integer \(n\ge2\) and all positive real lengths \(a,b\). The included standard-library script checks the Cartan determinant recurrence for \(n=2,\ldots,32\); those finite checks are a sanity check only, not the proof of the all-parameter statement.

## Relationship to prior work

Mohajer, *tropical covers, tropical abelian varieties and Prym varieties*, arXiv:2604.01574v1 (2 April 2026), develops tropical Jacobians and Prym varieties for cyclic graph covers and gives an explicit volume calculation for free \(\mathbb Z_3\)-covers in Proposition 4.7, including a genus-two example. The present statement identifies the integral norm-kernel cycle lattice and its full restricted quadratic form for the canonical two-loop rose cover in every degree \(n\ge2\), rather than only a volume for degree three. Len and Zakharov's *Kirchhoff's theorem for Prym varieties* is cited as related earlier work on Prym volumes; its full text was not available for direct statement-level comparison in this run, so it remains a priority risk rather than evidence of noncoverage.

## Limitations

The result is restricted to a two-loop rose and to the cyclic cover in which both loop monodromies are the same generator. It concerns the unscaled restriction of the ambient Jacobian quadratic form. It does not compute the normalized principal polarization on a Prym variety, the Abel–Prym map, or the corresponding lattice for arbitrary monodromy assignments. A general graph-homology treatment may make this calculation an elementary special case; the claim is the explicit all-degree lattice identification and metric formula for this canonical family.

## References

1. A. Mohajer, *tropical covers, tropical abelian varieties and Prym varieties*, arXiv:2604.01574v1, 2 April 2026. https://arxiv.org/abs/2604.01574
2. Y. Len and D. Zakharov, *Kirchhoff's theorem for Prym varieties*, *Forum of Mathematics, Sigma* (2022). Identified as related prior work through the reference list of Mohajer; full text not read in this run.
