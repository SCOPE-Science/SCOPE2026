# Link recursion for independent-base types in Sauer’s indivisible hypergraphs

## Finding
For integers \(3\le k<n\), let \(\mathcal A_{k,n}\) be the class of finite \(k\)-uniform hypergraphs having no irreducible induced substructure on \(n\) or more vertices, and let \(U_{k,n}\) be its countable homogeneous limit from Sauer's Theorem 2.5.

Fix a finite independent set \(I\subset U_{k,n}\). For a point \(x\notin I\), define its link on \(I\) by
\[
L_x=\bigl(I,\{S\in\binom{I}{k-1}:S\cup\{x\}\text{ is a hyperedge}\}\bigr).
\]
Then the assignment \(\operatorname{tp}(x/I)\mapsto L_x\) is a bijection between nonalgebraic one-point types over \(I\) and labeled members of \(\mathcal A_{k-1,n-1}\) on the vertex set \(I\).

This gives a one-step recursion in uniformity and boundary size:
\[
S_1^{\mathrm{na}}(I;U_{k,n})\cong \mathcal A_{k-1,n-1}[I].
\]
For \(k=3\), the lower class is simply the class of \(K_{n-1}\)-free graphs. Hence, over an \(m\)-element independent set,
\[
\left|S_1^{\mathrm{na}}(I;U_{3,n})\right|
=\#\{\text{labeled \(K_{n-1}\)-free graphs on \(m\) vertices}\}.
\]
By the Erdős--Kleitman--Rothschild asymptotic for fixed forbidden cliques,
\[
\log_2\left|S_1^{\mathrm{na}}(I;U_{3,n})\right|
=\left(1-\frac1{n-2}+o(1)\right)\frac{m^2}2.
\]

## Assumptions and scope
The language contains one symmetric irreflexive \(k\)-ary relation. "Independent" means that the induced \(k\)-uniform hypergraph on \(I\) has no hyperedges. Irreducibility is in Sauer's sense: the Gaifman graph is complete. Types are orbits of points outside \(I\) under the pointwise stabilizer of \(I\).

The recursion is stated for \(k\ge3\). The \(k=2\) endpoint is graph-theoretic and does not produce another ordinary uniform-hypergraph link class of arity at least two.

## Proof
Let \(L\) be a \((k-1)\)-uniform hypergraph on \(I\), and form its cone \(C_x(L)\) by adjoining a new point \(x\) and taking exactly the \(k\)-edges \(S\cup\{x\}\) for \(S\in E(L)\). Because \(I\) is independent, every irreducible subset of \(C_x(L)\) of size at least \(k\) must contain \(x\).

If \(Y\subseteq I\), then \(Y\cup\{x\}\) is irreducible in the cone exactly when \(Y\) is irreducible in \(L\). Indeed, every pair of vertices of \(Y\) lies together in a cone edge exactly when it lies together in a link edge; and every pair \(x,y\) is covered exactly when \(y\) lies in a link edge. Therefore the cone has an irreducible subset on at least \(n\) vertices exactly when the link has one on at least \(n-1\) vertices. Thus
\[
C_x(L)\in\mathcal A_{k,n}
\quad\Longleftrightarrow\quad
L\in\mathcal A_{k-1,n-1}.
\]

Every legal cone belongs to the age of \(U_{k,n}\), so the Fraïssé extension property realizes it over the already embedded set \(I\). Two realized points have the same link precisely when the induced structures on \(I\) together with the new point are isomorphic by the identity on \(I\); homogeneity then extends that map to an automorphism fixing \(I\) pointwise. Different links give different relation diagrams and hence different types. This proves the bijection.

For \(k=3\), a link is an ordinary graph, and irreducibility is completeness. The legal links are therefore exactly the \(K_{n-1}\)-free graphs. The displayed asymptotic then follows from the classical enumeration of fixed-clique-free labeled graphs.

## Verification
The bundled `verify.py` independently enumerates small link hypergraphs and their cones. It checks the cone/link irreducibility equivalence for \((k,n)=(3,4),(3,5),(4,5),(4,6)\) over all tested labeled links, and for \(k=3\) checks directly that cone legality is equivalent to \(K_{n-1}\)-freeness. It also recovers the labeled triangle-free graph counts
\[
1,1,2,7,41,388,5789
\]
for orders \(0\) through \(6\). The script prints `VERIFY_OK 73123 exact assertions`.

## Relationship to prior work
Sauer proves that these boundary-defined ages are free-amalgamation ages and that their homogeneous limits are rank linear and indivisible. In the proof of Theorem 2.5 he encodes a type over a finite sockel by \((k-1)\)-ary incidence data and derives a rank criterion from the largest irreducible configuration in that data. The lower-uniformity link recursion above is a specialization to independent sockels that packages the legal one-point diagrams as the entire class \(\mathcal A_{k-1,n-1}\); that recursive formulation and the resulting independent-base type enumeration were not located in the checked sources.

A prior finite-parameter calculation for a different generic \(K_4^-\)-free \(3\)-hypergraph also uses link graphs, but its legal links depend on the existing parameter hyperedges through a mixed conflict hypergraph. The present statement concerns Sauer's distinct infinite-boundary family and identifies a full lower-uniformity age on independent parameter sets.

## Limitations
The recursion uses independent parameter sets; arbitrary parameter substructures impose additional compatibility constraints. The result is a short structural corollary of Sauer's type encoding, so an uncatalogued folklore occurrence remains possible. The asymptotic clause for \(k=3\) imports the classical fixed-clique-free graph enumeration theorem and does not sharpen its error term.

## References
Norbert Sauer, “Colouring homogeneous structures,” arXiv:2008.02375, version 1 submitted 5 August 2020. Theorem 2.5 and its proof give the boundary class, free amalgamation, rank linearity, and the type-incidence calculation used here. The paper lists 2000 MSC primary 03E02.

Frank Mousset, Rajko Nenadov, and Angelika Steger, “On the Number of Graphs Without Large Cliques,” *SIAM Journal on Discrete Mathematics* 28 (2014), 1980–1986, DOI 10.1137/130947878. Its abstract recalls the Erdős--Kleitman--Rothschild fixed-clique asymptotic and extends it to slowly growing clique size.
