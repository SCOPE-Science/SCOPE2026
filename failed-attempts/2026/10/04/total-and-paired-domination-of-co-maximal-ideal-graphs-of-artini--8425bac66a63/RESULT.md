# Total and paired domination of co-maximal ideal graphs of Artinian rings

## Finding

Let \(R\) be a finite commutative Artinian ring with identity that is not local, and write its Artinian decomposition as \[R\cong R_1\times\cdots\times R_r,\qquad r\ge2,\] where each \(R_i\) is local. For the co-maximal ideal graph \(\mathbb G(R)\), whose vertices are proper ideals not contained in \(J(R)\) and whose edges satisfy \(I+K=R\), \[\gamma_t(\mathbb G(R))=r\] and \[\gamma_{\mathrm{pr}}(\mathbb G(R))=2\left\lceil\frac r2\right\rceil.\] Thus paired domination equals total domination for even \(r\), while for odd \(r\) it is exactly one larger.

The formula depends only on the number of local factors, not on the sizes or ideal lattices of those factors.

## Assumptions and scope

Let
\[
R\cong R_1\times\cdots\times R_r,
\qquad r\ge2,
\]
be a finite commutative Artinian ring written as a product of local rings, with maximal ideals \(\mathfrak m_i\subset R_i\). Then
\[
J(R)=\mathfrak m_1\times\cdots\times\mathfrak m_r.
\]

A vertex of the co-maximal ideal graph \(\mathbb G(R)\) is a proper ideal
\[
I=I_1\times\cdots\times I_r
\]
that is not contained in \(J(R)\). Since every proper ideal of a local ring is contained in its maximal ideal, this is equivalent to saying that at least one coordinate \(I_i\) equals \(R_i\), while not all coordinates equal their whole rings.

Define the whole-coordinate support
\[
\sigma(I)=\{i:I_i=R_i}.
\]
Every vertex has nonempty proper support.

## Proof

For two vertices \(I,K\), locality gives
\[
I_i+K_i=R_i
\]
if and only if at least one of \(I_i,K_i\) is the whole ring \(R_i\). Therefore
\[
I+K=R
\iff
\sigma(I)\cup\sigma(K)=[r].
\tag{1}
\]

For each \(i\), let \(M_i\) be the maximal ideal of the product ring obtained by putting \(\mathfrak m_i\) in coordinate \(i\) and \(R_j\) in every other coordinate. Then
\[
\sigma(M_i)=[r]\setminus\{i}.
\]

Put
\[
D=\{M_1,\ldots,M_r}.
\]
If \(I\) is any vertex, choose \(i\in\sigma(I)\). Then
\[
\sigma(I)\cup\sigma(M_i)=[r],
\]
so \(I\) is adjacent to \(M_i\). If \(I=M_i\), any distinct \(M_j\) is adjacent to \(M_i\). Hence every vertex, including every vertex of \(D\), has a neighbor in \(D\). Thus \(D\) is a total dominating set and
\[
\gamma_t(\mathbb G(R))\le r.
\tag{2}
\]

For \(r\ge3\), the known ordinary domination number of the co-maximal ideal graph of a finite commutative Artinian ring is \(r\). Since every total dominating set is dominating,
\[
\gamma_t(\mathbb G(R))\ge r.
\]
For \(r=2\), every total dominating set has at least two vertices, while the two maximal ideals form an edge. Therefore
\[
\gamma_t(\mathbb G(R))=r
\]
for every \(r\ge2\).

Now consider paired domination. Every paired dominating set is total dominating and has even cardinality, so
\[
\gamma_{\mathrm{pr}}(\mathbb G(R))
\ge
2\left\lceil\frac r2\right\rceil.
\tag{3}
\]

If \(r\) is even, the set \(D\) induces a clique: for \(i\ne j\),
\[
\sigma(M_i)\cup\sigma(M_j)=[r].
\]
Hence its vertices can be paired arbitrarily into \(r/2\) edges. Therefore \(D\) is paired dominating and equality holds in (3).

If \(r\) is odd, choose any vertex \(X\) with support
\[
\sigma(X)=\{1}.
\]
Such a vertex exists by taking coordinate \(1\) equal to \(R_1\) and choosing proper ideals in all other coordinates. Then \(X\) is adjacent to \(M_1\). Pair \(X\) with \(M_1\), and pair the remaining \(r-1\) vertices
\[
M_2,\ldots,M_r
\]
arbitrarily inside their clique. Thus
\[
D\cup\{X}
\]
is paired dominating of size \(r+1\), again attaining (3).

Consequently
\[
\gamma_{\mathrm{pr}}(\mathbb G(R))
=
2\left\lceil\frac r2\right\rceil.
\]

## Verification

The standalone `verify.py` constructs the co-maximal ideal graph from abstract local ideal counts. A coordinate value is designated as the whole local ring, and adjacency is computed directly from the criterion that in every coordinate at least one summand must be whole.

It exhaustively computes total and paired domination minima for nine product profiles, including mixtures of field factors and nonfield local factors. It also checks the maximal-ideal witness and the odd-parity augmentation at the support level for every \(2\le r\le9\).

Exact output:

```text
VERIFY_OK
ideal_counts=(2, 2): vertices=2 gamma_t=2 gamma_pr=2
ideal_counts=(2, 3): vertices=3 gamma_t=2 gamma_pr=2
ideal_counts=(3, 3): vertices=4 gamma_t=2 gamma_pr=2
ideal_counts=(2, 2, 2): vertices=6 gamma_t=3 gamma_pr=4
ideal_counts=(2, 2, 3): vertices=9 gamma_t=3 gamma_pr=4
ideal_counts=(2, 3, 3): vertices=13 gamma_t=3 gamma_pr=4
ideal_counts=(2, 2, 2, 2): vertices=14 gamma_t=4 gamma_pr=4
ideal_counts=(2, 2, 2, 3): vertices=21 gamma_t=4 gamma_pr=4
ideal_counts=(2, 2, 2, 2, 2): vertices=30 gamma_t=5 gamma_pr=6
support_witness_checks_r=2..9_passed
```

These finite calculations are corroborative only. The general theorem is proved by the support-union argument above.

## Relationship to prior work

Ye and Wu introduced the co-maximal ideal graph and proved its basic connectivity, diameter, clique, and chromatic properties. Their paper identifies the number of maximal ideals as a central graph parameter.

Kavitha and Kala later studied domination for finite commutative Artinian rings. Their theorem gives ordinary domination number equal to the number of local factors when there are at least three factors, together with the complete-bipartite description in the two-factor case.

The present result strengthens that domination picture in two directions. First, the same canonical set of maximal ideals is shown to be total dominating. Second, the paired domination number is determined exactly, with the only additional cost being the unavoidable parity correction when the number of local factors is odd.

Targeted searches using the exact graph name together with “total domination” and “paired domination” did not locate these formulas.

## Limitations

The theorem is stated for finite commutative Artinian nonlocal rings. The proof uses the product decomposition into finitely many local rings and the fact that two proper ideals in a local ring cannot sum to the whole ring.

No claim is made for non-Artinian rings with infinitely many maximal ideals, nor for noncommutative co-maximal ideal graphs.

The ordinary domination theorem used for the lower bound when \(r\ge3\) is published literature; the total and paired formulas are proved independently here from the support structure.

## References

1. M. Ye and T. Wu, “Co-Maximal Ideal Graphs of Commutative Rings,” *Journal of Algebra and Its Applications* 11 (2012), 1250114. DOI: 10.1142/S0219498812501149.
2. S. Akbari, B. Miraftab, and R. Nikandish, “A Note on Co-Maximal Ideal Graph of Commutative Rings,” arXiv:1307.5401.
3. S. Kavitha and R. Kala, “A note on comaximal ideal graph of commutative rings,” *AKCE International Journal of Graphs and Combinatorics* 17 (2020), 453–460. DOI: 10.1016/j.akcej.2019.06.004.
