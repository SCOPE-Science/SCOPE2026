# Total and paired domination in left-ideal intersection graphs of \(M_n(\mathbb F_q)\)

## Finding

Let \(q\) be a prime power, \(n\ge2\), and let \(\mathcal G(M_n(\mathbb F_q))\) be the intersection graph whose vertices are the nonzero proper left ideals of \(M_n(\mathbb F_q)\), with distinct vertices adjacent when their intersection is nonzero. If \(n=2\), the graph has no total dominating set and no paired dominating set. If \(n\ge3\), then \[\gamma_t(\mathcal G(M_n(\mathbb F_q)))=q+1,\]and \[\gamma_{\mathrm{pr}}(\mathcal G(M_n(\mathbb F_q)))=\begin{cases}q+1,&q\text{ odd},\\ q+2,&q\text{ even}.\end{cases}\]

This gives the complete total- and paired-domination refinement of the known ordinary domination value for full matrix algebras over finite fields.

## Assumptions and scope

Let
\[
R=M_n(\mathbb F_q),
\qquad n\ge2.
\]
Write \(\mathcal G(R)\) for the simple graph whose vertices are the nonzero proper left ideals of \(R\), with two distinct vertices adjacent exactly when their intersection is nonzero.

A total dominating set \(D\) requires every vertex, including every vertex of \(D\), to have a neighbor in \(D\). A paired dominating set is a dominating set \(D\) for which the induced graph \(\mathcal G(R)[D]\) has a perfect matching.

For a subspace \(U\le \mathbb F_q^n\), define
\[
M_U=\{A\in M_n(\mathbb F_q):Ax=0\text{ for every }x\in U\}.
\]
Every left ideal is of this form, and
\[
M_U\cap M_W=M_{U+W}.
\]
Consequently,
\[
M_U\sim M_W
\iff
U+W\ne\mathbb F_q^n.
\tag{1}
\]

## Proof

We first reconstruct the ordinary domination lower bound because it is the lower bound needed for both strengthened parameters.

Let \(L\) be a two-dimensional subspace of \(\mathbb F_q^n\), and let
\[
U_1,\ldots,U_{q+1}
\]
be its one-dimensional subspaces. The corresponding left ideals
\[
M_{U_1},\ldots,M_{U_{q+1}}
\]
dominate \(\mathcal G(R)\). Indeed, if \(M_W\) is any vertex and \(\dim W\le n-2\), then
\[
\dim(W+U_i)\le n-1
\]
for every \(i\), so \(M_W\) is adjacent to each \(M_{U_i}\). If \(\dim W=n-1\), then
\[
\dim(L\cap W)\ge1,
\]
so some \(U_i\) lies in \(W\), and again \(W+U_i=W\ne\mathbb F_q^n\). Hence
\[
\gamma(\mathcal G(R))\le q+1.
\tag{2}
\]

For the matching lower bound, suppose a dominating set has at most \(q\) vertices. Replacing each \(M_W\) by a maximal left ideal \(M_U\) with \(U\) a one-dimensional subspace of \(W\) cannot decrease its closed neighborhood. Thus one may assume the dominating vertices are indexed by at most \(q\) lines
\[
U_1,\ldots,U_r,
\qquad r\le q.
\]
The number of hyperplanes of \(\mathbb F_q^n\) is
\[
\frac{q^n-1}{q-1},
\]
while a fixed line lies in
\[
\frac{q^{n-1}-1}{q-1}
\]
hyperplanes. Therefore at most
\[
q\frac{q^{n-1}-1}{q-1}
=
\frac{q^n-q}{q-1}
\]
hyperplanes contain one of the selected lines. Since
\[
\frac{q^n-q}{q-1}
<
\frac{q^n-1}{q-1},
\]
there is a hyperplane \(H\) containing none of them. By (1),
\[
H+U_i=\mathbb F_q^n
\]
for every \(i\), so \(M_H\) is adjacent to none of the selected vertices. This contradicts domination. Hence
\[
\gamma(\mathcal G(R))=q+1.
\tag{3}
\]

Now suppose \(n=2\). Every nonzero proper subspace is a line, and two distinct lines span the whole space. Thus (1) shows that \(\mathcal G(R)\) has no edges. It follows immediately that no total dominating set and no paired dominating set exist.

Assume from now on that \(n\ge3\). For distinct lines \(U_i,U_j\le L\),
\[
U_i+U_j=L\ne\mathbb F_q^n.
\]
Hence the \(q+1\) vertices
\[
M_{U_1},\ldots,M_{U_{q+1}}
\]
form a clique. Since they already dominate, they are also a total dominating set. Combining this with (3) gives
\[
\gamma_t(\mathcal G(R))=q+1.
\]

For paired domination, first let \(q\) be odd. Then \(q+1\) is even, and the dominating clique on
\[
M_{U_1},\ldots,M_{U_{q+1}}
\]
has a perfect matching. Thus
\[
\gamma_{\mathrm{pr}}(\mathcal G(R))=q+1.
\]

Finally let \(q\) be even. Every paired dominating set has even cardinality, while (3) gives the lower bound \(q+1\), which is odd. Therefore
\[
\gamma_{\mathrm{pr}}(\mathcal G(R))\ge q+2.
\]
Choose a line \(T\) not contained in \(L\). Since \(n\ge3\), every two distinct lines span a two-dimensional proper subspace, so \(M_T\) is adjacent to every \(M_{U_i}\). Hence
\[
\{M_T,M_{U_1},\ldots,M_{U_{q+1}}\}
\]
is a dominating clique of even order \(q+2\), and therefore has a perfect matching. Thus
\[
\gamma_{\mathrm{pr}}(\mathcal G(R))=q+2.
\]

## Verification

The symbolic argument above proves the theorem for every prime power \(q\) and every \(n\ge2\). The accompanying `verify.py` independently constructs the subspace model of the left-ideal graph for the prime-field cases
\[
(n,q)\in\{(2,2),(2,3),(3,2),(3,3)\},
\]
then exhaustively searches for ordinary, total, and paired dominating sets through the claimed optimum.

Exact output:

```text
VERIFY_OK
n=2 q=2 vertices=3 gamma=3 gamma_t=None gamma_pr=None
n=2 q=3 vertices=4 gamma=4 gamma_t=None gamma_pr=None
n=3 q=2 vertices=14 gamma=3 gamma_t=3 gamma_pr=4
n=3 q=3 vertices=26 gamma=4 gamma_t=4 gamma_pr=4
```

The finite computations are corroborative only; they are not used to extend the theorem beyond the tested cases.

## Relationship to prior work

Jafari and Jafari Rad studied domination in intersection graphs of rings and modules. Their paper is algebraically classified first under associative-ring and module sections and treats ordinary domination, not total or paired domination.

Akbari and Nikandish then analyzed the left-ideal intersection graph of matrix algebras over finite fields in detail. They prove that every left ideal of \(M_n(\mathbb F_q)\) has the form \(M_U\), with
\[
M_U\cap M_W=M_{U+W},
\]
and establish the ordinary domination formula
\[
\gamma(\mathcal G(M_n(\mathbb F_q)))=q+1.
\]
Their full matrix-algebra section was inspected around the structural lemma and domination theorem; searches of the full text for “total domination,” “paired,” and “perfect matching” returned no occurrences.

The present result strengthens that ordinary value in two independent directions. For \(n=2\), ordinary domination is finite but total and paired domination do not exist because the graph is edgeless. For \(n\ge3\), total domination retains the value \(q+1\), while paired domination detects the parity of the field order:
\[
q+1\quad\text{for odd }q,
\qquad
q+2\quad\text{for even }q.
\]
Targeted literature searches under the exact matrix-algebra, left-ideal-intersection, total-domination, paired-domination, and perfect-matching formulations did not locate a covering result.

## Limitations

The theorem concerns full matrix algebras over finite fields. It does not claim the same formulas for matrix rings over general finite rings or division rings, products of simple Artinian rings, or arbitrary semisimple rings.

The proof uses only the left-ideal graph. No statement is made for right-ideal, two-sided-ideal, or zero-divisor graphs.

The originality comparison is strongest against the fully inspected matrix-algebra paper and targeted exact-invariant searches. A poorly indexed source using different terminology for paired domination remains a residual risk.

## References

1. S. H. Jafari and N. Jafari Rad, “Domination in the intersection graphs of rings and modules,” *Italian Journal of Pure and Applied Mathematics* 28 (2011), 17–20. Public issue date: 19 July 2011.
2. S. Akbari and R. Nikandish, “Some results on the intersection graph of ideals of matrix algebras,” *Linear and Multilinear Algebra* 62 (2014), 195–206. DOI: 10.1080/03081087.2013.769101. Published online 11 March 2013.
3. T. W. Haynes and P. J. Slater, “Paired-domination in graphs,” *Networks* 32 (1998), 199–206.
