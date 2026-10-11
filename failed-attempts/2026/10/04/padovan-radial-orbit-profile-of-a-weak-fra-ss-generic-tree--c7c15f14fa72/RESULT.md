# Padovan radial orbit profile of a weak Fraïssé generic tree

## Finding
Let \(M\) be the generic limit of the weak Fraïssé class \(\mathcal G\) of finite acyclic undirected graphs in which no two vertices of degree greater than \(2\) are adjacent. Krawczyk, Kruckman, Kubiś, and Panagiotopoulos describe \(M\) by starting from the unique countable everywhere-infinitely-branching tree \(T\), coloring every edge by \(2\) or \(3\) so that infinitely many edges of each color meet every vertex, and replacing a color-\(j\) edge by a path of length \(j\).

Fix a branch vertex \(o\), equivalently a vertex of infinite degree in \(M\), and let \(q_n\) be the number of \(\operatorname{Aut}(M)_o\)-orbits on the graph-distance sphere \(S_n(o)\). Then
\[
q_0=1,\qquad q_1=q_2=2,\qquad q_n=q_{n-2}+q_{n-3}\quad(n\ge3),
\]
and hence
\[
\sum_{n\ge0}q_nz^n=\frac{(1+z)^2}{1-z^2-z^3}.
\]
Thus the radial orbit profile is
\[
1,2,2,3,4,5,7,9,12,16,21,28,37,49,65,\ldots,
\]
a shift of the Padovan sequence. In particular
\[
\lim_{n\to\infty}q_n^{1/n}=\rho,
\]
where \(\rho=1.324717957\ldots\) is the plastic constant, the real root of \(\rho^3=\rho+1\).

The full automorphism group has exactly three vertex orbits: the infinite-degree branch vertices, the unique internal vertices on length-2 macro-edges, and the two internal positions on length-3 macro-edges (which lie in one orbit).

## Assumptions and scope
Distances are ordinary graph distances in the generic limit \(M\). A “macro-edge” is the path between consecutive infinite-degree vertices; its length is \(2\) or \(3\). The count \(q_n\) is a count of point-stabilizer orbits inside a metric sphere, not the cardinality of those orbits. Except for \(n=0\), the individual orbits are countably infinite.

## Proof
The branch vertices of \(M\) are exactly its infinite-degree vertices, so every graph automorphism preserves their set. Two branch vertices are macro-adjacent when the unique path between them contains no other branch vertex. Such a macro-edge has graph length \(2\) or \(3\), which is therefore preserved by every automorphism. Consequently \(\operatorname{Aut}(M)\) is naturally the automorphism group of the underlying tree \(T\) with its \(\{2,3\}\)-edge coloring; an automorphism of the colored macro-tree extends uniquely along every subdivided edge.

The colored tree is highly homogeneous in the needed sense. Every vertex has countably infinitely many incident edges of each color. Hence any color-preserving isomorphism between two finite connected colored subtrees extends to a global automorphism: after removing the finite subtrees, each boundary vertex has countably many rooted complementary components of each required incoming color, and these components can be paired recursively. In particular, with \(o\) fixed, two vertices are in the same stabilizer orbit exactly when their unique paths from \(o\) have the same macro-edge color word and the same terminal position inside the final macro-edge.

Let \(c_m\) be the number of words in the alphabet \(\{2,3\}\) whose letters sum to \(m\), with the empty word counted for \(m=0\). Then
\[
C(z)=\sum_{m\ge0}c_mz^m=\frac1{1-z^2-z^3}.
\]
A vertex at graph distance \(n\) from \(o\) has one of four terminal states after its completed macro-edge word: it is a branch vertex (offset \(0\)); it is the internal point of a length-2 macro-edge (offset \(1\)); it is the first internal point of a length-3 macro-edge (offset \(1\)); or it is the second internal point of a length-3 macro-edge (offset \(2\)). Therefore
\[
q_n=c_n+2c_{n-1}+c_{n-2},
\]
where \(c_j=0\) for \(j<0\). Multiplying generating functions gives
\[
Q(z)=\sum_{n\ge0}q_nz^n=(1+2z+z^2)C(z)=\frac{(1+z)^2}{1-z^2-z^3}.
\]
The displayed recurrence and initial values follow. Its characteristic equation is \(x^3=x+1\), so the exponential growth rate is the plastic constant.

Finally, branch vertices form one orbit by colored-tree homogeneity. Midpoints of length-2 macro-edges form a second orbit. The internal vertices of length-3 macro-edges form a third: an automorphism may reverse a chosen color-3 macro-edge because the two rooted colored components obtained by deleting it are isomorphic. The three classes cannot mix because their distances to the nearest branch vertices are respectively \(0\), \(\{1,1\}\), and \(\{1,2\}\).

## Verification
The accompanying `verify.py` independently enumerates every finite word in \(\{2,3\}\) up to total weight \(30\), attaches the four possible terminal states, and counts the resulting path codes by graph distance. It checks the closed generating-function recurrence, the first fifteen values, the shift against the standard Padovan recurrence, and numerical convergence toward the plastic constant. The recorded replay ends with `VERIFY_OK`. The finite computation checks the enumerative consequences; the orbit classification itself is proved above.

## Relationship to prior work
Krawczyk–Kruckman–Kubiś–Panagiotopoulos give the weak Fraïssé class, prove WAP and failure of CAP, and explicitly describe its generic limit as the \(2\)-/3-subdivision of an everywhere infinitely branching tree. Their full text contains no occurrence of “orbit,” “Padovan,” or “plastic,” and does not state a point-stabilizer radial profile.

The integer sequence itself is classical: OEIS A000931 records the Padovan recurrence and, beginning at the appropriate shift, the values \(1,2,2,3,4,5,7,9,12,\ldots\). That numerical sequence is not claimed as new. The contribution here is its exact realization as the spherical stabilizer-orbit profile of this canonical weak Fraïssé generic limit, together with the three vertex-orbit classification and plastic-constant orbital growth rate.

Targeted searches for weak-Fraïssé, subdivided-tree, automorphism-orbit, Padovan, plastic-constant, and spherical-orbit formulations did not locate a prior statement of this bridge. The closest indexed results concerned unrelated tree growth or other oligomorphic orbit profiles.

## Limitations
The originality search cannot rule out unindexed folklore, lecture notes, or an equivalent statement phrased purely in permutation-group language. The result concerns the specific generic limit \(M\) and a branch-vertex stabilizer; stabilizers of the two degree-2 vertex orbits have different radial profiles.

## References
1. Adam Krawczyk, Alex Kruckman, Wiesław Kubiś, and Aristotelis Panagiotopoulos, *Examples of weak amalgamation classes*, arXiv:1907.09577; Mathematical Logic Quarterly 68 (2022), 178–188, DOI 10.1002/malq.202100037. First public version: 2019-07-22. MSC 03C07, 03C50.
2. OEIS Foundation, A000931, *Padovan sequence*; recurrence and standard sequence data.
