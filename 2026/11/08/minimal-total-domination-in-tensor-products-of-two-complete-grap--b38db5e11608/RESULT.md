# Minimal total domination in tensor products of two complete graphs

## Finding

For every pair of integers \(m,n\ge 2\), let \(G_{m,n}=K_m\times K_n\) be the **direct** (categorical, tensor) product: its vertex set is \([m]\times[n]\), and two distinct ordered pairs are adjacent exactly when both coordinates differ. A *total dominating set* \(S\subseteq V(G_{m,n})\) meets the open neighborhood of every vertex, including vertices in \(S\). It is *inclusion-minimal* if no proper subset is total dominating. Write \(\mathcal M_{m,n}(z)=\sum_{S\text{ minimal total dominating}}z^{|S|}\).

**Theorem.** Every inclusion-minimal total dominating set is exactly one of the following, with no other possibilities:

1. Three cells in pairwise distinct rows and pairwise distinct columns.
2. Four cells lying in two distinct rows, with exactly two cells in each row (the chosen columns may overlap).
3. Four cells lying in two distinct columns, with exactly two cells in each column (the chosen rows may overlap).

The two four-cell descriptions overlap precisely on a filled \(2\times2\) rectangle; the three-cell type is disjoint from them. Consequently,
\[
\boxed{\mathcal M_{m,n}(z)=6\binom m3\binom n3 z^3+\binom m2\binom n2\left(\binom m2+\binom n2-1\right)z^4,}
\]
where \(\binom a3=0\) for \(a<3\).

In particular, the upper total domination number is \(\Gamma_t(G_{m,n})=4\) for all \(m,n\ge2\), whereas the minimum total domination number is \(\gamma_t(G_{m,n})=3\) if \(m,n\ge3\) and is \(4\) otherwise. Thus \(G_{m,n}\) is *well-totally-dominated* (all inclusion-minimal total dominating sets have equal cardinality) if and only if \(\min(m,n)=2\). The upper-number conclusion establishes the \(k=1\) case of the cross-product question of Kazemi (2016 preprint; 2017 journal paper), beyond the case with a factor of order two that was proved there.

## Assumptions and scope

Both factors are simple complete graphs of order at least two. They are allowed to have equal or unequal orders. The graph \(G_{2,2}\) is disconnected but has no isolated vertices, and it is covered by the theorem. The direct product is not the Cartesian product or strong product. All graph vertices and rows/columns are labelled; coefficient counts are for distinct labelled vertex subsets, not for orbits under graph automorphisms. Minimality refers to **inclusion**, not minimum cardinality.

## Proof

**Step 1 (cross criterion).** Regard a selected cell \((i,j)\) as an edge between row vertex \(i\) and column vertex \(j\) in an auxiliary bipartite graph \(B_S\) with row class \([m]\), column class \([n]\), and edge set \(S\). For a graph vertex \((i,j)\), its neighbors in \(S\) are exactly the selected cells outside both row \(i\) and column \(j\). Thus \(S\) is total dominating if and only if for no row \(i\) and column \(j\) is \(S\) entirely contained in the union of row \(i\) and column \(j\). We call such a union a *cross*. This equivalence applies whether or not \((i,j)\) itself is selected.

**Step 2 (a matching of three).** If \(B_S\) has a matching of size at least three, take any three edges of it. The corresponding three cells use pairwise distinct rows and columns. A cross can contain at most two such cells, so the three cells already constitute a total dominating set. Inclusion-minimality then forces \(S\) to be exactly that three-edge matching. Conversely, any such triple is total dominating; every two cells fit in some cross (the row of one and column of the other), so the triple is inclusion-minimal.

**Step 3 (matching number at most two).** Otherwise \(B_S\) has matching number at most two. By Koenig's bipartite matching–vertex-cover theorem, its edges have a cover by at most two row/column vertices. Since \(S\) is not contained in a cross, such a cover cannot have a row and a column, nor can it have only one vertex. Hence it consists either of two row vertices or of two column vertices. Suppose it is two rows. The selected cells must include at least two cells in each of those rows: if one row contained at most one cell, the other row together with the column of that single cell (or any column if the row is empty) would be a cross covering \(S\). If one of the two rows contained at least three selected cells, deleting a cell from that row would leave both rows with at least two cells, so the remaining set would still escape every cross, contradicting inclusion-minimality. Therefore each row has exactly two cells. The two-column case is symmetric. Conversely, any set of two cells in each of two rows escapes every cross. Deleting any chosen cell leaves two cells in one row and one in the other, a set contained in a cross. Therefore it is inclusion-minimal. The corresponding statement for two columns is symmetric. Because total domination is monotone in the set \(S\), testing single-cell deletions suffices for inclusion-minimality.

**Step 4 (count).** There are \(\binom m3\binom n3 3!\) disjoint-coordinate triples. For row-type four-sets, choose the two rows and independently two columns within each: \(\binom m2\binom n2^2\). Column-type four-sets number \(\binom n2\binom m2^2\). A set appears in both classes exactly when it is the four corners of one \(2\times2\) rectangle, of which there are \(\binom m2\binom n2\). Inclusion-exclusion gives the displayed polynomial. The four-cell coefficient is strictly positive for all \(m,n\ge2\), while the three-cell coefficient is positive exactly when both factor orders are at least three. These observations yield all extremal and well-totally-dominated claims.

## Verification

The accompanying `verify.py` constructs the product graph from its adjacency rule, tests the total domination condition on every nonempty subset, tests each present vertex for a deletion preserving total domination, and compares the resulting complete family of minimal sets with an independently generated family from the theorem. Exhaustive tested parameters are \((m,n)=(2,2),(2,3),(2,4),(2,5),(3,3),(3,4),(3,5),(4,4),(4,5)\). There are 1,152,839 nonempty candidate subsets across these nine instances and 2,417 minimal total dominating sets; every family and coefficient matches. The verification is finite evidence, not a substitute for the unrestricted proof.

Run with Python 3 using `python verify.py`; it requires only the standard library.

## Relationship to prior work

Burcroff and O'Brien (first publicly posted 2021-10-02) established unimodality of **ordinary** domination polynomials for connected direct products of complete graphs and treated graph-product domination enumeration in their Section 5.1. Ordinary domination does not require selected vertices to be adjacent to selected vertices; their polynomial result does not imply this inclusion-minimal **total**-domination classification.

Kazemi's work on upper \(k\)-tuple total domination (arXiv 2016-03-08; journal 2017) states in Proposition 7 that the upper \(k\)-tuple total domination number of \(K_n\times K_2\) is \(2k+2\), and asks in Question 1 whether the same holds for arbitrary two complete factors (under the stated degree conditions). At \(k=1\), the present theorem proves the proposed equality for all factor orders and counts every minimal set; it does **not** resolve that question for any \(k>1\). In particular the known \(K_n\times K_2\) upper-number case is not presented as new.

Bahadır, Ekim and Gözüpek (first publicly posted 2020-10-05) studied well-totally-dominated graphs generally, including structural restrictions, rather than this exact direct-product minimal-set enumerator. Standard Koenig matching–cover duality is invoked as an established theorem, not claimed as a new lemma.

## Limitations

This treats only two complete factors, not arbitrary graph products, not three or more complete factors, and not \(k\)-tuple total domination for \(k>1\). The argument gives an exact family classification for all stated sizes, but its publication priority remains provisional: a differently indexed equivalent formula or table may exist. It has not undergone independent mathematical audit. The finite verification is limited to the listed nine parameter pairs.

## References

1. A. Burcroff and G. O'Brien, *Unimodality and monotonic portions of certain domination polynomials*, arXiv:2110.00709 (v1 publicly submitted 2021-10-02), especially Section 5.1. https://arxiv.org/abs/2110.00709
2. A. P. Kazemi, *Upper k-tuple total domination in graphs*, arXiv:1603.02428 (v1 publicly submitted 2016-03-08), Pure and Applied Mathematics Quarterly 13 (2017), 563–579, especially Proposition 7 and Question 1. https://arxiv.org/abs/1603.02428
3. S. Bahadır, T. Ekim and D. Gözüpek, *Well-totally-dominated graphs*, arXiv:2010.02341 (v1 publicly submitted 2020-10-05); Ars Mathematica Contemporanea 20 (2021), 209–222. https://arxiv.org/abs/2010.02341
4. D. Kőnig's bipartite matching–vertex-cover theorem (standard form: maximum matching size equals minimum vertex-cover size).
