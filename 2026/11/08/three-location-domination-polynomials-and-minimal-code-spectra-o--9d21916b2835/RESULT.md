# Self-locating-dominating codes of complete prisms and their crown complements

## Finding

Let \(n\ge4\) and \(G=K_2\square K_n\), consisting of two labelled cliques \(A=\{a_i:1\le i\le n\}\), \(B=\{b_i:1\le i\le n\}\) with matching edges \(a_ib_i\). Let \(H=\overline G\), the crown graph \(K_{n,n}\) minus this matching. A set \(C\) is self-locating-dominating in \(G\) exactly when every column \(\{a_i,b_i\}\) contains a selected vertex and \(|C\cap A|,|C\cap B|\ge2\). The full and inclusion-minimal cardinality enumerators for this family are respectively
\[
S_G(z)=(2z+z^2)^n-2(n+1)z^n-2nz^{n+1},\qquad
M_G(z)=(2^n-2n-2)z^n.
\]
In particular, the inclusion-minimal sets are precisely the one-per-column choices using at least two vertices from each clique.

In contrast to the solid-locating-dominating families, which coincide for \(G\) and \(H\), their self-locating-dominating families differ. The cardinality enumerator of sets self-locating-dominating in **both** graphs is
\[
S_{G,H}(z)=2z^n\bigl((1+z)^n-1-nz\bigr)-z^{2n}.
\]

## Assumptions and scope

Graphs are finite, simple, undirected and labelled; polynomials count vertex subsets, not automorphism orbits. Put \(I_C(u)=N[u]\cap C\) for the closed neighborhood \(N[u]\) in the graph under consideration. Every vertex outside a dominating code has a nonempty identifying set. In addition, self-location requires \(\bigcap_{c\in I_C(u)}N[c]=\{u\}\) for each \(u\notin C\). Solid location instead requires that the identifying sets of distinct outsiders be incomparable under inclusion. Inclusion-minimal refers to containment, not minimum cardinality.

## Proof

**Self-location in the prism.** An outsider \(a_i\) has signature \(A_C\cup(\{b_i\}\cap C)\), with \(A_C=C\cap A\); symmetrically the signature at \(b_i\) uses \(B_C=C\cap B\). In an empty column any nonempty signature at \(a_i\) uses only codewords from \(A\); the intersection of their closed neighborhoods contains the entire clique \(A\), so an empty column is impossible. With all columns occupied, any missing \(a_i\) has its mate \(b_i\) in \(C\). If \(A_C\) is empty, \(N[b_i]\) is not a singleton. If \(A_C=\{a_j\}\), the neighborhood intersection contains both \(a_i\) and \(b_j\). If \(|A_C|\ge2\), intersecting the neighborhoods of two distinct members of \(A_C\) eliminates all of \(B\); intersecting further with \(N[b_i]\) leaves exactly \(a_i\). The symmetric test holds for missing \(b_i\); a fully selected clique already satisfies its count requirement. This proves the characterization.

Nonempty columns contribute \((2z+z^2)^n\). The sets with at most one selected vertex in \(A\) have three forms: the whole \(B\) alone; one \(A\)-only column and all other columns \(B\)-only; or one double column and all others \(B\)-only. They contribute \((n+1)z^n+nz^{n+1}\). The excluded family for \(B\) is disjoint from this one, since every set still under consideration has at least \(n\ge4\) vertices. This gives \(S_G\). If a self-locating code has a double column, its size is at least \(n+1\ge5\); the clique with at least three selected vertices can lose its vertex from any double column, preserving both requirements. A one-per-column code satisfying the clique counts is minimal because every deletion empties a column. Of the \(2^n\) one-per-column choices, exactly \(2+2n\) have a clique with at most one choice. This gives \(M_G\).

**Comparison with the crown.** For every outsider, the two closed traces in complementary graphs are complementary subsets of \(C\). When there are at least two outsiders, pairwise incomparability rules out both an empty and a full trace and is invariant under taking complements. For at most one outsider domination is automatic in both graphs, since no vertex is isolated. Thus the solid families coincide. The crown solid polynomial and its full code classification were previously given in the crown-graph result cited below; they transfer to the prism without a separate enumeration.

For self-location in the crown, the same earlier result gives the allowable patterns: a full side, or exactly one omitted matched pair with all other vertices selected. To see the restriction when neither side is full, let \(P=\{i:a_i\notin C\}\), \(Q=\{i:b_i\notin C\}\). If \(i\in P\), the identifying set of \(a_i\) in the crown is \(B_C\setminus\{b_i\}\). For \(j\notin P\) with \(j\in Q\), the selected vertex \(a_j\) would be adjacent in the crown to every member of that signature, contradicting self-location (or domination if empty). Hence \(Q\subseteq P\), and similarly \(P\subseteq Q\). If \(P=Q\) has at least two members, the two corresponding omitted vertices of \(A\) have equal signatures. A single matched omission is indeed feasible in the crown: the \(n-1\) signature vertices on one side have distinct indices, and the only vertex adjacent to all of them is the omitted mate-side vertex; on their own side their closed neighborhoods intersect trivially. A full side is also feasible in the crown: for an omitted vertex on the other side, the \(n-1\) signature vertices exclude exactly its matched index, and their common closed neighborhood consists of the omitted vertex. These checks use \(n-1\ge2\).

The matched omission is never feasible in the prism, which cannot have an empty column. A set self-locating in both graphs must therefore contain an entire side and at least two vertices of the other side. Counting this for each full side gives \(2z^n((1+z)^n-1-nz)\), with \(z^{2n}\) subtracted for double counting the full vertex set. For example, one entire side alone works in the crown but not in the prism, while any one-per-column choice with at least two from each clique works in the prism but does not contain a full side.

## Relationship to prior work

Junnila, Laihonen and Lehtilä give the minimum cardinalities for rook graphs; the self-location minimum \(n\) is not the contribution here. The earlier crown-graph work gives both all-code classifications in the complement and, through trace complementation, the prism's solid family. Locating-total domination of the prism retains an open-neighborhood test for selection and distinguishes only outsiders; its complete classification permits empty columns and includes whole-side choices. The self-location condition instead tests identifying intersections against all vertices. The results here concern the full and inclusion-minimal self-location enumerators in the prism and the exact shared subfamily with the crown. No exhaustive historical priority is claimed.

## Verification

Execute `python3 verify.py` with the standard library. Direct neighborhood enumeration in the prism and crown for \(4\le n\le6\) tests all 5,376 labelled subsets in each graph. This checks the prism self-location polynomial, its inclusion-minimal spectrum, the shared self-location polynomial, and equality of the two solid families in this range. The unrestricted result is the structural proof above.

## References

- V. Junnila, T. Laihonen and T. Lehtilä, *On Regular and New Types of Codes for Location-Domination*, Discrete Applied Mathematics 247 (2018), 225–241, DOI 10.1016/j.dam.2018.03.050.
- *Self- and solid-locating-dominating code polynomials of crown graphs*, [Resultary, 2026-10-13](https://github.com/Resultary/2026/tree/main/2026/10/13/SCOPE-self-and-solid-locating-dominating-code-polynomials-of-crown-gra--60cce5e52da9).
- *Full locating-total domination polynomial of complete prisms*, [Resultary, 2026-11-02](https://github.com/Resultary/2026/tree/main/2026/11/2/SCOPE-full-locating-total-domination-polynomial-of-complete-prisms--7f2244f74bb9).
