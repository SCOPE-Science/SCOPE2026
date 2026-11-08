# Uniform scale-three Vietoris–Rips homotopy and persistence of generalized quadrangles

## Finding
For every **existing finite thick generalized quadrangle** \(\mathcal Q\) of order \((s,t)\), with integers \(s,t\ge2\), let \(G\) be its point–line incidence graph, assign length one to every incidence edge, and let \(K_r=\operatorname{VR}_{\le r}(V(G))\) be the inclusive Vietoris–Rips complex for the shortest-path metric. Then
\[
K_r\simeq
\begin{cases}
\text{a discrete set of }(s+t+2)(st+1)\text{ points},&0\le r<1,\\
\bigvee^{s^2t^2}S^1,&1\le r<3,\\
\bigvee^{s^4t^4}S^3,&3\le r<4,\\
\text{a point},&r\ge4.
\end{cases}
\]
At the middle transition the equality \(K_3=K_{\rm point}*K_{\rm line}\) holds as an abstract simplicial complex, with the two factors the clique complexes of the point-collinearity and line-intersection graphs. Both factors simplicially collapse onto connected graphs with \(s^2t^2\) independent cycles. The inclusion \(K_1\hookrightarrow K_2\) is a simplicial-collapse equivalence. In particular the **complete reduced integral persistence barcode** is
\[
\left((s+t+2)(st+1)-1\right)[0,1)\ \text{in degree }0,\qquad
s^2t^2[1,3)\ \text{in degree }1,\qquad
s^4t^4[3,4)\ \text{in degree }3,
\]
with no other intervals. Here a coefficient before an interval means that many copies of the interval module.

## Assumptions and scope
A finite thick generalized quadrangle of order \((s,t)\) consists of point set \(P\), line set \(L\) and incidence relation such that every line contains exactly \(s+1\) points, every point lies on exactly \(t+1\) lines, two distinct points determine at most one line, and for each point \(p\) not on a line \(\ell\) there is exactly one point \(q\) on \(\ell\) collinear with \(p\) (equivalently a unique incident line through \(p\) meeting \(\ell\)). We assume that such a geometry exists; not every integer parameter pair is realizable. These axioms imply that the bipartite incidence graph \(G\) is connected, has diameter four and girth eight, and
\[
|P|=(s+1)(st+1),\qquad |L|=(t+1)(st+1),\qquad
|E(G)|=(s+1)(t+1)(st+1).
\]
All intervals use inclusive graph-distance thresholds; there is no rescaling by two or use of a Euclidean ambient metric. Homotopy claims are ordinary, not equivariant, and the barcode uses integral homology with reduced degree zero.

## Proof
**Step 1 (distances and graph powers).** Points \(p,p'\) have distance two exactly when they are distinct and collinear; otherwise their distance is four. Dually, distinct lines have distance two exactly when they intersect, otherwise four. A point and line have distance one when incident and distance three when not incident: for a nonincident pair, the quadrangle axiom supplies a length-three path through the unique point on the line collinear with the chosen point. These are all possibilities, so \(\operatorname{diam}(G)=4\). The incidence graph has no cycle of length four by uniqueness of the joining line and no length-six cycle by the quadrangle axiom (three pairwise collinear points cannot determine three different lines); thickness ensures an eight-cycle exists.

**Step 2 (scale two).** At threshold one the complex is \(G\), since \(G\) is bipartite and triangle-free. Proposition 2.2 of Adamaszek, *Clique complexes and graph powers* (2011), states that the clique complex of the square of a graph of girth at least seven simplicially collapses onto the original clique complex. Since \(G\) has girth eight, \(K_2\searrow K_1=G\), by a collapse relative to \(G\). (Equivalently, one can pair each subset of at least two neighbors of a vertex with the face obtained by adjoining that vertex: no four- or six-cycles makes the matching well-defined and acyclic.) Its cycle rank equals
\[
|E(G)|-|V(G)|+1
=(s+1)(t+1)(st+1)-(s+t+2)(st+1)+1=s^2t^2.
\]
Thus both \(K_1\) and \(K_2\) have the homotopy type of a wedge of \(s^2t^2\) circles, and the inclusion at scale two is an integral homology isomorphism.

**Step 3 (the scale-three join).** Every point is at distance at most three from every line, while same-type pairs are at distance at most three precisely when collinear/intersecting. Hence the threshold graph at scale three is the graph-theoretic join of the point-collinearity graph and the line-intersection graph. Passing to clique complexes gives the exact identity
\[
K_3=K_P*K_L.
\]
A clique with three or more vertices of \(K_P\) lies on one line: three mutually collinear points on three distinct lines would create an incidence six-cycle. Thus the maximal simplices of \(K_P\) are precisely \(\Delta(P\cap\ell)\), one \(s\)-simplex for each line \(\ell\). Different maximal simplices meet in at most one vertex. For each such simplex choose a fixed root vertex; pair every face consisting of at least two other vertices with its extension by the root. These are elementary collapses, internal to that maximal simplex, deleting all its higher-dimensional faces and leaving exactly the star-tree from the root to its \(s\) other vertices. A face of dimension at least one belongs to a unique such maximal simplex, so the collapses on different line-simplices do not interfere. Their union is acyclic (a gradient cycle cannot cross between maximal simplices through their shared, unmatched vertices). We get a simplicial collapse to a connected graph with \(|P|\) vertices and \(s|L|\) edges. Its cycle rank is
\[
s|L|-|P|+1
=s(t+1)(st+1)-(s+1)(st+1)+1=s^2t^2.
\]
The point-collinearity graph is connected because any two points are linked by a chain of collinearities, as follows from diameter four. Consequently \(K_P\simeq\bigvee^{s^2t^2}S^1\). Interchanging points and lines gives, using the same no-six-cycle argument and collapses on each \(t\)-simplex of lines through a fixed point,
\[
K_L\simeq\bigvee^{s^2t^2}S^1.
\]
Each complex is connected. For connected based finite CW complexes, \(X*Y\simeq\Sigma(X\wedge Y)\), so
\[
K_3\simeq\left(\bigvee^{s^2t^2}S^1\right)*\left(\bigvee^{s^2t^2}S^1\right)
\simeq\bigvee^{s^4t^4}S^3.
\]
This is an integral **homotopy** equivalence, not an inference from finite-field Betti numbers.

**Step 4 (death and persistence).** All graph distances are integers, and the diameter is four, so \(K_r\) is constant on each interval between successive integers and \(K_4\) is the full simplex. Before scale one the vertices are isolated. Scale one connects them; degree-zero bars then die. Step 2 implies that the \(s^2t^2\) circle generators survive the inclusion at scale two; Step 3 shows they all die at scale three while exactly \(s^4t^4\) independent degree-three generators first appear. These die at scale four. No other reduced homology groups occur at any stage. Because each degree is supported at consecutive parameter stages with identity maps on the only nonzero two-stage persistence component, these statements determine the asserted complete integral interval decomposition.

## Verification
The standalone `verify.py` constructs the symplectic generalized quadrangles \(W(3,2)\) and \(W(3,3)\) over finite fields, without external packages. It enumerates their points and isotropic projective lines, checks the incidence metric and diameter, enumerates all faces in each scale-three join factor and in the scale-two complex, and independently checks explicit acyclic face-pairings by topological sorting the **entire** oriented face-poset covering graph. It also computes mod-two homology of the factors and scale-two complexes. The resulting cycle ranks are \(16\) and \(81\) respectively, while the proven scale-three join formula yields \(256\) and \(6561\) three-spheres.

Running `python verify.py` yields the deterministic transcript in `verification_output.txt`, concluding `GENERALIZED_QUADRANGLE_RIPS_FINITE_CHECK_PASS`. The checker does **not** directly enumerate the full scale-three join for the larger example or prove the uniform theorem by sampling; that theorem is proved by the combinatorial argument above.

## Relationship to prior work
Adamaszek's graph-power theorem proves the scale-one-to-two collapse under the girth condition, but does not determine the scale-three behavior of generalized quadrangles. The archived work of Abreu, Araujo-Pardo, Balbuena, Labbate and Salas constructs girth-eight generalized-quadrangle incidence graphs and supplies the geometric context, but does not study their Rips homotopy or persistence.

A 2026 public result, *The scale-three Rips complex of the Tutte–Coxeter graph is a wedge of 256 three-spheres*, proves the special case \(s=t=2\) using a duad–syntheme model. Its proof does not state or establish a uniform formula for higher-order, nonclassical, or unequal-parameter generalized quadrangles. The present theorem includes that known case and extends the exact join-and-collapse mechanism to arbitrary line sizes and dual line pencils; the corresponding full family formula and complete integral persistence do not follow as a stated theorem from the previously inspected sources. The earlier special case is not presented as new here.

McCabe's 2026 approximation-lower-bound paper uses incidence graphs of generalized polygons and the same small-scale girth stability, but its stated quantitative conclusions concern sizes of approximations and persistent first-homology at stabilized lower scales, not the scale-three integral sphere-wedge classification. Projective-plane and affine-plane incidence Rips results concern distinct incidence geometries and thresholds; they do not subsume this generalized-quadrangle theorem. Full-result, alias, graph-power, and implication searches did not identify a broader published theorem containing the uniform claim. This is a bounded originality assessment, not proof of publication priority.

## Limitations
The theorem applies only to finite existing thick generalized quadrangles; it does not assert existence at arbitrary integer pairs, extend to degenerate orders, classify equivariant representations or provide canonical generators. The integral interval decomposition is made for the discrete shortest-path metric with inclusive thresholds. Finite checks at orders two and three are corroboration, not an infinite proof. There is a directly related published order-two case, and equivalent unindexed or inaccessible generalizations may exist; independent literature and mathematical audits have not been performed.

## References
1. M. Adamaszek, *Clique complexes and graph powers*, arXiv:1104.0433, first public version 2011-04-03, especially Proposition 2.2 and Sections 2–3.
2. M. Abreu, G. Araujo-Pardo, C. Balbuena, D. Labbate, and J. Salas, *Families of small regular graphs of girth 7*, arXiv:1211.2672, first public version 2012-11-12, introduction and generalized-quadrangle preliminaries.
3. *The scale-three Rips complex of the Tutte–Coxeter graph is a wedge of 256 three-spheres*, public mathematical record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-the-scale-3-rips-complex-of-the-tutte-coxeter-graph-is-a-wedge-o--9454ecd0bd54 .
4. K. McCabe, *Lower Bounds for Approximating the Vietoris–Rips Filtration*, arXiv:2607.06524, first public version 2026-07-07, especially Section 3.
5. N. Saleh, T. Titz Mite, and S. Witzel, *Vietoris–Rips complexes of Platonic solids*, arXiv:2302.14388, first public version 2023-02-28.
