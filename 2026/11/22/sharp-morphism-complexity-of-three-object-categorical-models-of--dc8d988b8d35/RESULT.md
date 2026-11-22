# Sharp morphism complexity of three-object categorical models of orientable surfaces

## Finding
For every integer \(g\ge1\), let \(\Sigma_g\) be the closed connected orientable genus-\(g\) surface. Define \(\mu_3(\Sigma_g)\) as the minimum number of **nonidentity morphisms** in a finite acyclic category with **exactly three objects** and classifying space homotopy equivalent to \(\Sigma_g\). Then
\[
\mu_3(\Sigma_g)=(2g+1)(2g+2).
\]
More sharply, every such category has at least \(2g+1\) morphisms between the first and second objects and at least \(2g+1\) between the second and third. Both minima can occur simultaneously. The three objects are themselves minimal because the surface has nonzero integral second homology, whereas a two-object acyclic nerve is at most one-dimensional.

For example the sharp nonidentity-morphism counts for genera \(1,2,3\) are \(12,30,56\), respectively. This optimizes morphism count **conditional on object-minimality**, not across all acyclic categories with arbitrarily many objects.

## Assumptions and scope
A finite acyclic category has only identity endomorphisms and does not admit nonidentity arrows in both directions between distinct objects. Its classifying space is the realization of the nerve, including one one-simplex for every nonidentity arrow and one two-simplex for every composable pair. All spaces, homology groups, and cup products below are integral unless otherwise indicated.

A three-object model with nonzero second homology must contain a composable pair. Relabel its objects \(0<1<2\); write
\[
 a=|\operatorname{Hom}(0,1)|,\quad b=|\operatorname{Hom}(1,2)|,\quad c=|\operatorname{Hom}(0,2)|.
\]
All three numbers are positive. The \(ab\) composable pairs define a composition table into the \(c\) long arrows. Repetitions of composite arrows are allowed.

## Proof
**Lower bound.** The nerve has three zero-simplices, \(a+b+c\) nondegenerate one-simplices, and \(ab\) nondegenerate two-simplices, with no higher cells. Since \(\chi(\Sigma_g)=2-2g\),
\[
 3-(a+b+c)+ab=2-2g,
 \qquad c=ab+1+2g-a-b.
\]
Consequently its number \(m\) of nonidentity morphisms is exactly
\[
 m=a+b+c=ab+1+2g.\tag{1}
\]

Apply the sink decomposition at object \(2\), in the notation of Carcacía-Campos, Section 2.3. The base category on objects \(0,1\) has classifying space a connected graph, \(Y\), with \(a\) parallel edges. The category of arrows into the sink has a bipartite multigraph \(\Gamma\) with \(b+c\) vertices (one for each short arrow from \(1\) or long arrow from \(0\)) and \(ab\) edges (one for each composable pair). The sink lemma identifies
\[
 B\mathcal C\cong Y\cup_{p}\operatorname{Cone}(\Gamma).
\]

The graph \(\Gamma\) must be connected. Indeed, if it has \(q>1\) components, the mapping cone over this disconnected domain contains a **homotopy wedge summand** \(\bigvee^{q-1}S^1\). To see this without an implicit assumption on \(p\), choose one marked vertex in each component of \(\Gamma\), paths in connected \(Y\) joining their images, and maximal trees in all components. Collapsing these trees, and then the chosen connecting tree, gives a cellular model whose \(q-1\) extra one-cells do not occur in any attaching map of a two-cell: every cone two-cell comes from edges of a single component. Hence those one-cells split off as circles. But any nonzero circle-wedge class in the first integral cohomology has zero cup pairing with all first cohomology, contradicting the nondegenerate Poincaré-duality pairing
\[
 H^1(\Sigma_g;\mathbb Z)\times H^1(\Sigma_g;\mathbb Z)
 \longrightarrow H^2(\Sigma_g;\mathbb Z)\cong\mathbb Z
\]
for a closed orientable surface. Thus \(q=1\).

For connected \(\Gamma\), its integral first Betti number is
\[
 \beta_1(\Gamma)=ab-(b+c)+1=a-2g,
\]
using equation (1). The homology long exact sequence of the mapping cone has an injection
\[
 H_2(B\mathcal C;\mathbb Z)\hookrightarrow H_1(\Gamma;\mathbb Z),
\]
because \(H_2(Y;\mathbb Z)=0\). The group on the left is \(\mathbb Z\), so \(a-2g\ge1\), i.e. \(a\ge2g+1\). Reverse all arrows and interchange object order: the opposite category has the same classifying-space homotopy type and exchanges \(a\) and \(b\). The identical argument proves \(b\ge2g+1\). Substitution into equation (1) proves
\[
 m\ge(2g+1)^2+1+2g=(2g+1)(2g+2).\tag{2}
\]

**Sharp construction.** Set \(r=2g+1\), an odd integer at least three. Take three objects \(0<1<2\), with short morphisms \(f_i:0\to1\) and \(g_j:1\to2\), for all \(i,j\in\mathbb Z/r\mathbb Z\). Introduce long arrows \(h_k:0\to2\) for all \(k\in\mathbb Z/r\mathbb Z\), and an additional distinct long arrow \(\ell_{ij}:0\to2\) for each ordered pair with \(i\notin\{j,j+1\}\). Declare the composite for every pair to be
\[
 g_j\circ f_i=\begin{cases}
 h_j,&i=j,\\
 h_{j-1},&i=j+1,\\
 \ell_{ij},&\text{otherwise},
 \end{cases}
\]
with indices modulo \(r\). No triple of nonidentity arrows is composable; identities and this table therefore define an associative acyclic category. The three nonidentity Hom-set cardinalities are
\[
 a=b=r,\qquad c=r+r(r-2)=r(r-1),
\]
so its nonidentity-morphism count is exactly \(r(r+1)=(2g+1)(2g+2)\).

Each \(\ell_{ij}\) occurs in exactly one two-simplex of the nerve. Its one-simplex is therefore a free face, and collapsing this edge together with its unique triangle, for all \(r(r-2)\) such pairs, preserves the homotopy type. The remaining two-dimensional \(\Delta\)-complex has three vertices; three sets of \(r\) edges, labelled \(f_i,g_j,h_k\); and the \(2r\) oriented triangles
\[
 A_j=(f_j,g_j,h_j),\qquad B_j=(f_{j+1},g_j,h_{j-1}).
\]
Every remaining edge lies in exactly two triangles. Each vertex link is a connected two-regular graph on \(2r\) vertices, hence a circle: at object \(1\) its link follows consecutive \(f\)-indices, at object \(2\) consecutive \(h\)-indices, and at object \(0\) the successive \(h\)-indices differ by two; the last link is connected precisely because \(r\) is odd. Thus the remaining complex is a closed connected surface. The integral two-chain
\[
 \sum_{j\in\mathbb Z/r\mathbb Z}(A_j-B_j)
\]
has zero boundary, pairing all incident triangles with opposite signs, so the surface is orientable. Its Euler characteristic is
\[
 3-3r+2r=3-r=2-2g.
\]
The classification of closed orientable surfaces now identifies it with \(\Sigma_g\), proving that (2) is attained.

## Verification
The enclosed standalone Python checker deterministically constructs the composition tables for each genus from \(1\) through \(12\), tests all \(r(r-2)\) prescribed free-face collapses, checks that every surviving edge has exactly two incident triangles, checks connectivity and degree two of all three vertex links, verifies the signed integral fundamental two-cycle, and verifies the precise face and morphism counts. It reports `ALL_12_PARAMETER_TESTS_PASSED`. These are reproducibility tests for the **upper construction**, not an exhaustive search over all categories or a substitute for the uniform lower-bound proof.

Run from the folder containing the embedded checker:

```bash
python3 surface_morphism_optimality_checker.py
```

## Relationship to prior work
Carcacía-Campos, *How many points does it take to see the homotopy of a space? Minimal acyclic categorical models* (first publicly posted November 6, 2026), establishes the relevant three-object composition-table and sink-cone framework and emphasizes object count as its complexity measure. Its general machinery, in particular the sink lemma and Section 2.3, does not state the sharp nonidentity-morphism minimum for the closed orientable surface of every genus. The new contribution is the uniform sharp **morphism budget** for object-minimal surface models, requiring a Poincaré-duality connectedness argument and the matching construction. General models of two-complexes and known explicit surface models do not by themselves imply a lower bound for every competing composition table.

The finite acyclic category model is the **ordinary nerve**, not a poset model, regular simplicial triangulation, or stable homotopy object. The count includes every nonidentity morphism, including direct arrows from \(0\) to \(2\), irrespective of whether each such arrow is a composite.

## Limitations
The restriction to exactly three objects is essential to the meaning of the optimality theorem. No claim is made about unrestricted minimum morphism count across categories with four or more objects. The result does not classify all equality cases or nonorientable surfaces. Finite tests cover only genera \(1\) through \(12\); correctness for all positive genera rests on the explicit proof, and no independent mathematical validation is claimed.

## References
- Isaac Carcacía-Campos, *How many points does it take to see the homotopy of a space? Minimal acyclic categorical models*, arXiv:2611.09718v1 (November 6, 2026), especially Lemma 2.1 and Section 2.3, https://arxiv.org/abs/2611.09718.
- Isaac Carcacía-Campos, *From old categorical models to new ones through open covers*, arXiv:2609.37843v1 (September 29, 2026), https://arxiv.org/abs/2609.37843.
- Allen Hatcher, *Algebraic Topology*, Cambridge University Press (2002), for mapping cones, Poincaré duality and the fundamental group of a wedge.
