# First third homology in circular-ladder general-position complexes

## Finding

For each integer \(3\le n\le8\), let \(L_n=C_n\square K_2\) be the circular-ladder graph, and let \(X_n=\mathrm{GP}(L_n)\) be its geodesic general-position simplicial complex. The complete reduced integral homology of these six complexes is free abelian, with the following ranks. Every reduced homology group not listed is zero.

| \(n\) | \(\operatorname{rank}\widetilde H_1(X_n;\mathbb Z)\) | \(\operatorname{rank}\widetilde H_2(X_n;\mathbb Z)\) | \(\operatorname{rank}\widetilde H_3(X_n;\mathbb Z)\) |
|---:|---:|---:|---:|
| 3 | 3 | 1 | 0 |
| 4 | 15 | 0 | 0 |
| 5 | 5 | 9 | 0 |
| 6 | 24 | 3 | 0 |
| 7 | 7 | 27 | 0 |
| 8 | 32 | 15 | 4 |

In particular, \(n=8\) is the **first** circular ladder, among all integer orders beginning at \(3\), whose general-position complex has nonzero third integral homology:

\[\widetilde H_3(X_n;\mathbb Z)=0\quad(3\le n\le7),\qquad \widetilde H_3(X_8;\mathbb Z)\cong\mathbb Z^4.\]

This is a finite-range calculation. It makes no assertion for \(n\ge9\).

## Assumptions and scope

The graph \(C_n\) is the simple cycle on \(n\) labeled vertices. Graph distances count edges on a shortest path. A subset \(S\subseteq V(L_n)\) is a simplex of \(X_n\) when no three *distinct* vertices in \(S\) lie on any common shortest graph path. In particular, the existence of **one** geodesic containing a selected triple excludes the entire superset. The empty face is implicit; homology is reduced and uses signed integral simplicial boundaries.

Label the vertices by pairs \((i,\varepsilon)\) with \(i\in\{0,\ldots,n-1\}\), \(\varepsilon\in\{0,1\}\), ordered by the integer \(2i+\varepsilon\). Their distances obey

\[d((i,\varepsilon),(j,\delta))=\min(|i-j|,n-|i-j|)+|\varepsilon-\delta|.\]

Consequently a distinct triple \(\{a,b,c\}\) is forbidden if at least one of its three members lies between the others in the metric, i.e. if \(d(a,c)=d(a,b)+d(b,c)\) for some ordering.

## Proof

**Step 1: exhaustive finite face determination.** For each \(n=3,4,5,6,7,8\), first enumerate all unordered triples of distinct graph vertices and mark those satisfying one of the three metric betweenness equalities. Then enumerate **all** nonempty vertex subsets, retaining precisely those containing no forbidden triple. This gives the following face counts \((f_0,f_1,f_2,f_3)\) and numbers \(b_3\) of forbidden triples; no simplex of dimension greater than three survives.

| \(n\) | \(b_3\) | \(f_0\) | \(f_1\) | \(f_2\) | \(f_3\) |
|---:|---:|---:|---:|---:|---:|
| 3 | 12 | 6 | 15 | 8 | 0 |
| 4 | 48 | 8 | 28 | 8 | 2 |
| 5 | 70 | 10 | 45 | 50 | 10 |
| 6 | 168 | 12 | 66 | 52 | 18 |
| 7 | 210 | 14 | 91 | 154 | 56 |
| 8 | 400 | 16 | 120 | 160 | 76 |

**Step 2: exact signed integral boundaries.** Orient every simplex by increasing vertex label, and on a \(k\)-simplex \([v_0,\ldots,v_k]\) use the usual alternating boundary \(\partial_k=\sum_{j=0}^{k}(-1)^j[v_0,\ldots,\widehat v_j,\ldots,v_k]\). Row/column elimination using **only unit pivots** \(+1\) or \(-1\) yields the following integral boundary ranks \((r_1,r_2,r_3)\), with *zero residual matrices* after all pivots.

| \(n\) | \(r_1\) | \(r_2\) | \(r_3\) |
|---:|---:|---:|---:|
| 3 | 5 | 7 | 0 |
| 4 | 7 | 6 | 2 |
| 5 | 9 | 31 | 10 |
| 6 | 11 | 31 | 18 |
| 7 | 13 | 71 | 56 |
| 8 | 15 | 73 | 72 |

Each unit-pivot elimination is a sequence of invertible integer row and column operations. As its residual matrix is zero, every nonzero Smith invariant of every boundary map is \(1\); this is stronger than a rank computation over a field. Thus the cokernel of each boundary is torsion-free, and every integral homology group, which embeds in such a cokernel, is also torsion-free. Since \(r_1=f_0-1\), each complex is connected. Finally,

\[\operatorname{rank}\widetilde H_k(X_n;\mathbb Z)=f_k-r_k-r_{k+1}\qquad (k=1,2,3),\]

with \(r_4=0\), gives exactly the displayed table. For example, at \(n=8\) the third rank is \(76-72=4\), and the second rank is \(160-73-72=15\). No unenumerated higher simplices or homology degrees occur by Step 1. This completes the finite proof.

## Verification

Run the included `verify.py` with a standard Python 3 interpreter. It reconstructs the forbidden triples from the graph metric, enumerates every nonempty subset for all six orders, reconstructs the signed boundary matrices, performs exact integer unit-pivot elimination and asserts the displayed counts and ranks. It fails if a nonzero residual integer entry remains without a unit pivot. An additional separate calculation with Smith normal forms agreed with every rank and invariant factor. These checks are finite, exhaustive for the stated vertex orders, and do not establish a formula for larger orders.

## Relationship to prior work

Klavžar, Patkós, Rus and Yero [1, §3, Theorem 3.2] determined the general-position **number** of the cylinder \(P_r\square C_s\). In particular their formula gives \(\mathrm{gp}(C_3\square K_2)=3\) and \(\mathrm{gp}(C_n\square K_2)=4\) for \(n\ge4\): these complexes can have dimension three from the fourth graph onward. But maximal simplex size alone does not determine integral homology or the sharp *later* onset at \(n=8\). Their §2 face counts concern rectangular path products, not these closed ladders.

Iršič, Klavžar, Rus and Tuite [2] introduced the general-position polynomial and computed it for several graph families, notably rectangular path grids; the inspected article does not provide the integral homology of these circular ladders. The present integral calculation is compatible with, but is not a restatement of, the published cardinality and polynomial results.

## Limitations

Only the six orders \(3\le n\le8\) are covered. The theorem concerns integral homology, **not** homotopy types, cup products, group actions, or persistence. Exhaustive enumeration is a valid finite proof only because the domain is explicitly bounded. This self-review is not independent scholarly validation; an equivalent result outside the inspected literature or search index remains possible.

## References

[1] S. Klavžar, B. Patkós, G. Rus, I. G. Yero, *On general position sets in Cartesian products*, arXiv:1907.04535, originally public 10 July 2019; §3, Theorem 3.2. https://arxiv.org/abs/1907.04535

[2] V. Iršič, S. Klavžar, G. Rus, J. Tuite, *General Position Polynomials*, Results in Mathematics 79 (2024), article 110, published 28 February 2024. https://doi.org/10.1007/s00025-024-02133-3
