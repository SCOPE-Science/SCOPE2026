# Residue-three rigidity and movable maximum-volume simplices in second hypersimplices

## Finding
For every integer \(n\ge 3\), let \(\Delta(2,n)=\{x\in[0,1]^n:\sum_{i=1}^n x_i=2\}\), equipped with its intrinsic Euclidean \((n-1)\)-volume. Call an \((n-1)\)-simplex *maximal* when its volume is largest among **all** simplices whose \(n\) vertices belong to \(\Delta(2,n)\), not necessarily vertices of the ambient polytope.

**Rigidity-versus-mobility theorem.** Every maximal simplex has all its vertices among the hypersimplex vertices \(e_i+e_j\) if and only if \(3\mid n\). If \(n=3k+1\), maximal simplices occur in explicitly attained two-dimensional moving-apex families. If \(n=3k+2\), maximal simplices occur in explicitly attained four-dimensional independent two-apex families. Thus a continuous equality family occurs in exactly two residue classes modulo three; when \(3\mid n\), every maximizer is isolated among all inscribed simplices.

All vertex-supported maximizing simplices correspond precisely to graphs on \(n\) labeled vertices whose connected components are odd-unicyclic and whose number of components is \(k=\lfloor n/3\rfloor\). Their graph component sizes are: \(k\) triangles for \(n=3k\); \(k-1\) triangles plus one triangle with one pendant vertex for \(n=3k+1\); and, for \(n=3k+2\), either \(k-1\) triangles plus one five-vertex odd-unicyclic graph, or (when \(k\ge2\)) \(k-2\) triangles plus two four-vertex odd-unicyclic graphs. Their exact labeled counts are
\[
N_{3k}=\frac{(3k)!}{6^k k!},\qquad
N_{3k+1}=\frac{(3k+1)!}{2\cdot 6^{k-1}(k-1)!},
\]
\[
N_{3k+2}=\frac{27(3k+2)!}{20\cdot6^{k-1}(k-1)!}
+\mathbf 1_{k\ge2}\frac{(3k+2)!}{8\cdot6^{k-2}(k-2)!}.
\]
Under coordinate permutations, the maximizing graphs have respectively one, one, and four or five orbits (four when \(n=5\), five for \(n\ge8\) with \(n\equiv2\pmod 3\)).

For clarity, the maximum-volume **numerical value** is not asserted as an independent discovery: De Loera, Sturmfels, and Thomas's 1995 incidence-determinant lemma yields it by a short additional optimization. With \(k=\lfloor n/3\rfloor\), the value is
\[
\operatorname{Vol}_{n-1}^{\max}=\frac{\sqrt n\,2^{k-1}}{(n-1)!},
\qquad
\frac{\operatorname{Vol}_{n-1}^{\max}}{\operatorname{Vol}_{n-1}(\Delta(2,n))}
=\frac{2^{k-1}}{2^{n-1}-n}.
\]
The contribution assessed here is the exact all-dimension **nonvertex rigidity threshold**, constructed positive-dimensional equality families, and the complete labeled and symmetry-class census of vertex maximizers, not the previously available determinant law.

## Assumptions and scope
All integers satisfy \(n\ge3\), and all simplex points are permitted anywhere in the entire closed hypersimplex. A simplex is specified up to reordering its \(n\) vertices. A *vertex-supported* simplex uses exactly \(n\) distinct extreme points of \(\Delta(2,n)\). The signless vertex-edge incidence matrix of a simple graph on \(n\) labeled nodes has columns \(e_i+e_j\). All statements concern ordinary intrinsic Euclidean volume, not normalized lattice volume; normalized volumes appear only in the cited historical lemma.

## Proof
**1. Vertex determinant and pre-existing input.** Choose any \(n\) pair-sum vertices, and let \(B\) be their \(n\times n\) signless incidence matrix. Since every column sums to two, orthogonal splitting along the normal \((1,\ldots,1)/\sqrt n\) gives
\[
\operatorname{Vol}_{n-1}(\operatorname{conv}\{B_{\cdot1},\ldots,B_{\cdot n}\})
=\frac{\sqrt n}{2(n-1)!}|\det B|.
\]
De Loera--Sturmfels--Thomas, Lemma 2.4 (1995), proves that \(\det B\ne0\) exactly when each connected graph component is odd-unicyclic, and then \(|\det B|=2^c\), where \(c\) is the number of components. Equivalently one may remove pendant vertices by cofactor expansion and compute the determinant \(\pm2\) of each remaining odd cycle. Every component has at least three nodes, so \(c\le\lfloor n/3\rfloor\), with equality attained by the component-size patterns in the Finding. This gives the displayed maximum among vertex tuples. For arbitrary points, each determinant column is a convex combination of vertex columns; determinant multilinearity plus the triangle inequality bounds the absolute determinant by the same maximum. Hence the formula is the unrestricted maximum as well.

**2. Exact vertex configurations and counts.** If \(n=3k\), equality forces all \(k\) components to be triangles. If \(n=3k+1\), their total excess above size three is one, forcing exactly one four-vertex component; its unique odd cycle is a triangle with a fourth pendant node. If \(n=3k+2\), the excess two is distributed as one five-vertex component or two four-vertex components. A five-vertex odd-unicyclic component is a pentagon (\(12\) labeled structures), or a triangle (\(\binom53=10\) choices) with a rooted two-node forest attached to its three core vertices (\(3^2+2\cdot3=15\) forests). Its total count is \(12+150=162\); a labeled four-vertex component has \(4\cdot3=12\) structures. Standard labeled-set multinomial counting, dividing by permutations of components of equal size, yields the three displayed \(N_n\) formulas. At size five, the four distinct component isomorphism types are the pentagon; triangle with both leaves attached to one core vertex; triangle with leaves at distinct core vertices; and triangle with a pendant path of length two. Adding two size-four components at \(n\ge8\) gives one further graph-isomorphism type. This establishes the claimed coordinate-permutation orbit counts, not just the labeled counts.

**3. Rigidity exactly in dimensions divisible by three.** Suppose \(n=3k\), and \(S\) is a maximizing simplex with a nonvertex point \(x\). Write \(x\) as a convex combination of at least two distinct polytope vertices with strictly positive coefficients. Express all remaining simplex points as convex combinations of polytope vertices too. Multilinearity writes the signed determinant of \(S\) as a convex combination of signed determinants of vertex-supported simplices. Every summand lies in the interval \([-2^k,2^k]\); equality of the absolute weighted average with \(2^k\) forces *all* positive-weight summands to equal the same endpoint. Holding the chosen polytope vertices at the other \(n-1\) positions fixed and selecting two different vertices from the support of \(x\), we therefore obtain two distinct maximum-determinant graphs sharing \(n-1\) edges. But every maximum graph at \(n=3k\) is a disjoint union of \(k\) triangles. Deleting one edge from it and adding a **different** edge either fails to restore that original three-node triangle or merges components and decreases their number; the resulting graph cannot again be a partition into \(k\) triangles. Contradiction. Hence every maximizer is vertex-supported, and its finite orbit is isolated.

**4. Explicit continuous families in the other two residue classes.** For \(n=3k+1\), partition the labels into \(k-1\) disjoint triples, one triple \(\{a,b,c\}\), and a remaining label \(d\). Keep all three edges within each triple as fixed simplex vertices. Replace the one last simplex vertex by any point of the Euclidean triangle
\[
T_d=\operatorname{conv}\{e_d+e_a,e_d+e_b,e_d+e_c\}.
\]
Every vertex choice from \(T_d\) produces a spanning graph comprising \(k-1\) triangles plus one triangle-with-leaf, so every vertex determinant has the same absolute value \(2^k\). More strongly, the determinant signs coincide: expanding along the row for the sole leaf \(d\) eliminates the same last column and leaves the same core triangle blocks regardless of the chosen neighbor. Its signed determinant therefore stays exactly \(\pm 2^k\) throughout the entire \(2\)-dimensional triangle \(T_d\). Interior points give maximizers with a nonvertex apex.

For \(n=3k+2\), choose \(k-1\) disjoint core triples, two remaining labels \(d,f\), and a designated core triple \(\{a,b,c\}\). Keep the edges of all core triangles fixed. Choose one simplex point freely in \(T_d\) as above and an independent second point freely in
\[
T_f=\operatorname{conv}\{e_f+e_a,e_f+e_b,e_f+e_c\}.
\]
For every one of the nine pairs of extreme choices, the edge graph consists of \(k-1\) triangles and one five-vertex odd-unicyclic component. Two successive cofactor expansions along the rows \(d,f\) leave the same signed determinant \(\pm2^k\) independent of both choices. By bilinearity, *every* pair in \(T_d\times T_f\) is maximizing; the parameterized family has dimension four and contains points with both apexes nonvertex. The constructions include the boundary cases \(n=4\) and \(n=5\), respectively. This concludes the all-dimensional rigidity-versus-mobility classification.

## Verification
The accompanying independent arithmetic checker (`second_hypersimplex_checker.py`) enumerates every \(n\)-vertex simplex among \(\binom{n}{2}\) pair-sum vertices for all \(3\le n\le7\), using exact integer Bareiss determinants, checks the old odd-unicyclic determinant certificate and the newly stated maximal counts, and checks absence of one-edge replacements in the divisible-by-three sizes. It covers \(1+15+252+5005+116280=121553\) edge subsets, with maximum counts \(1,12,162,10,420\). It is finite corroboration, not an infinite-dimensional proof. The equality families and rigidity proof are established by the exact multilinear and graph arguments above; no numerical optimizer or floating-point extrapolation is used.

## Relationship to prior work
De Loera, Sturmfels, and Thomas (1995), *Gröbner bases and triangulations of the second hypersimplex*, Lemma 2.4, already gives the exact graph criterion and determinant/normalized-volume formula for every vertex-supported full simplex. That stronger prior result **covers the graph-determinant value and hence the numerical unrestricted maximum once ordinary multilinearity is invoked**; these facts are not claimed original. Its main subject is triangulations, not the equality locus of unrestricted maximum-volume simplices. Parisi, Sherman-Bennett, and Williams (first publicly posted April 16, 2021) develop hypersimplex tilings and comparisons with amplituhedra in a separate geometric setting; their inspected full-text Sections 1, 7, 10, and 11 also do not give the nonvertex rigidity criterion or the family constructions above. Published geometric work on hypersimplex hyperplane sections and vertex convexification studies different invariants, not these optimizing simplex positions. An equivalent earlier classification is possible and would alter historical priority.

## Limitations
The result does **not** claim a classification of every nonvertex maximizing simplex when \(n\not\equiv0\pmod3\), nor does it claim the constructed families attain the largest possible stratum dimension. The count/orbit classification concerns **vertex-supported** maximizers only. The numerical optimum follows a previously published determinant lemma; the new part assessed is the rigidity dichotomy and explicitly dimensioned flexible examples, together with finite optimizer class counts. No independent mathematical audit has been conducted.

## References
1. J. A. De Loera, B. Sturmfels, and R. R. Thomas, *Gröbner bases and triangulations of the second hypersimplex*, Combinatorica 15 (1995), 409–424. Lemma 2.4 and Theorem 2.3. DOI: 10.1007/BF01299745. Lawful author-hosted full text: https://www.math.ucdavis.edu/~deloera/researchsummary/gb%2Bhypersimplex.pdf.
2. M. Parisi, M. Sherman-Bennett, and L. Williams, *The m=2 amplituhedron and the hypersimplex: signs, clusters, triangulations, Eulerian numbers*, initial arXiv posting 2021-04-16, arXiv:2104.08254 (the later complete HTML edition has title wording “tilings”). https://arxiv.org/html/2104.08254v6.
3. B. Braun and L. Solus, *Shellability, Ehrhart Theory, and r-stable Hypersimplices*, initial arXiv posting 2014-08-20, arXiv:1408.4713; supplementary triangulation context. https://arxiv.org/abs/1408.4713.
