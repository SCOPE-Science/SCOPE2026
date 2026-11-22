# Three-object acyclic categorical models for all finite two-dimensional CW homotopy types

## Finding

**Theorem.** Let \(X\) be a nonempty, connected, finite CW complex of dimension at most two. Let \(\nu(X)\) denote the least number of objects in a finite acyclic category \(\mathcal C\) for which \(B\mathcal C\simeq X\). Then \(\nu(X)\) is always defined and

\[
\nu(X)=\begin{cases}
1 &\text{if }X\text{ is contractible},\\
2 &\text{if }X\text{ has noncontractible connected-graph homotopy type},\\
3 &\text{otherwise}.
\end{cases}
\]

In particular, every finite connected two-dimensional presentation complex, with arbitrary attaching words, admits a three-object finite acyclic categorical model. The assertion is a homotopy-equivalence classification, not a claim that a given two-dimensional complex has a three-vertex regular triangulation.

## Assumptions and scope

A *finite acyclic category* has finitely many objects and arrows, has only identity endomorphisms, and admits no arrows between objects in opposite directions. Its nerve has a cell for each chain of composable nonidentity arrows. The definition of \(\nu\) uses ordinary homotopy equivalence of classifying spaces.

Collapse a maximal tree of the connected one-skeleton of \(X\). By the cellular approximation and tree-collapse arguments for CW complexes, the result is a presentation two-complex with one vertex, \(k\) oriented loop edges, and \(s\) two-cells attached by finite signed words in these loops; this retains all attaching maps up to homotopy, not merely their relations in fundamental groups. If \(k=0\) but \(s>0\), add a cancelling loop-and-disk pair. If necessary, represent a null-homotopic constant attaching map by the nonempty word \(x_1x_1^{-1}\). These operations preserve the homotopy type. The non-graph cases therefore reduce to \(k\ge1\), \(s\ge1\), and nonempty finite words \(w_r\) (for \(1\le r\le s\)). Write \(L\) for the sum of their lengths.

## Proof

**1. Explicit finite composition table.** Define an acyclic category on the linearly ordered object set \(0<1<2\). There are \(k+1\) arrows \(a_0,\ldots,a_k:0\to1\). For every position \(j\) in each word \(w_r\), put a distinct arrow \(b_{r,j}:1\to2\). Thus there are \(L\) arrows of the second kind.

Include one arrow \(c_*:0\to2\). For each relator \(r\) of length \(\ell_r\), include \(\ell_r-1\) further, distinct arrows \(c_{r,1},\ldots,c_{r,\ell_r-1}:0\to2\), and write \(c_{r,0}=c_{r,\ell_r}=c_*\). For each letter occurrence \((r,j)\) with absolute generator index \(i\), introduce a different arrow \(d_{r,j,t}:0\to2\) for every \(t\in\{1,\ldots,k\}\setminus\{i\}\). There are therefore exactly \(kL-s+1\) arrows from \(0\) to \(2\).

Define every composite of two nonidentity arrows as follows. Suppose the \(j\)-th letter of \(w_r\) is \(x_i\). Set

\[
b_{r,j}\circ a_i=c_{r,j-1},\qquad b_{r,j}\circ a_0=c_{r,j}.
\]

If that letter is \(x_i^{-1}\), reverse these two values:

\[
b_{r,j}\circ a_0=c_{r,j-1},\qquad b_{r,j}\circ a_i=c_{r,j}.
\]

For all other \(t\in\{1,\ldots,k\}\setminus\{i\}\), set \(b_{r,j}\circ a_t=d_{r,j,t}\). There are no three composable nonidentity arrows, so these prescriptions define a unique associative finite acyclic category \(\mathcal C\), with \((k+1)L\) nondegenerate two-simplices in its nerve.

**2. Compute its sink-link graph.** Apply the sink mapping-cone lemma to the object \(2\), in the explicit three-object formulation of Carcacía Campos [1, Section 2.3]. Let \(K\) be the two-vertex graph with the \(k+1\) edges \(a_0,\ldots,a_k\). There is a graph \(\Gamma\) with one vertex for each \(b\)-arrow and each \(c\)- or \(d\)-arrow, and an edge from \(b_{r,j}\) to \(b_{r,j}\circ a_t\) labeled \(a_t\), for each \(t\in\{0,\ldots,k\}\). The projection \(p:\Gamma\to K\) sends this edge to \(a_t\). The lemma gives

\[
B\mathcal C\cong K\cup_p\operatorname{Cone}(\Gamma).
\]

For each relator, its \(\ell_r\) vertices of type \(b\) and its consecutive \(c\) vertices form a subdivided circular multigraph: each letter contributes two differently labeled edges between consecutive \(c\) vertices through the corresponding \(b\) vertex. A one-letter word gives a genuine two-edge bigon. All these circles meet precisely at \(c_*\). Every arrow \(d_{r,j,t}\) is a distinct degree-one vertex of \(\Gamma\), so the remaining edges are pendant trees. Hence \(\Gamma\) is connected and deformation retracts to a wedge of exactly \(s\) circles. Its integral first Betti rank is \(s\) (also \((k+1)L-(L+kL-s+1)+1=s\)).

**3. Recover each attaching word.** Contract the edge \(a_0\) of \(K\); this produces the standard rose on generators represented by \(a_i a_0^{-1}\) for \(1\le i\le k\). In \(\Gamma\), traverse the relator circle from \(c_{r,j-1}\) through \(b_{r,j}\) to \(c_{r,j}\). When the letter is positive \(x_i\), its two edges project to \(a_i a_0^{-1}\). When the letter is negative \(x_i^{-1}\), they project to \(a_0 a_i^{-1}\). Thus the based loop of the \(r\)-th circle maps to exactly the word \(w_r\). The pendant edges contribute no loops and may be collapsed. Coning off this connected graph therefore attaches one disk along each of the prescribed \(s\) words, up to homotopy. We obtain \(B\mathcal C\simeq X\).

**4. Sharpness.** An acyclic category with one object is a point. An acyclic category with at most two objects has a classifying space of CW dimension at most one; every *connected* such space is homotopy equivalent to a graph. Conversely a Kronecker category with two objects and \(q+1\) parallel arrows has classifying space a wedge of \(q\) circles, so every connected graph type is modeled using at most two objects. The point uses one. The claimed three-way classification follows, even when \(X\) has nontrivial fundamental group and higher homotopy groups.

## Verification

For the normal form with \(k\) loop generators, \(s\) nonempty relators and total word length \(L\), the category has exactly \(k+1\), \(L\), and \(kL-s+1\) arrows in its three nonidentity hom-sets. Its nerve has \((k+1)L\) nondegenerate two-simplices. The Euler characteristic is therefore

\[
3-\bigl((k+1)+L+(kL-s+1)\bigr)+(k+1)L=1-k+s,
\]

agreeing with the presentation two-complex. The separate, standalone `check_presentation_models.py` enumerates the full composition table, verifies every triangle boundary and \(\partial_1\partial_2=0\), reconstructs the labeled relator loops in the link graph, checks its connectivity and cycle rank, and checks integral Smith invariants for eight small examples: projective plane, Klein bottle, torus, a degree-three Moore space, a sphere, a two-relator torsion space, a circle-sphere wedge, and a three-crosscap surface. It uses Python 3 and SymPy for the optional Smith computations; run `python check_presentation_models.py`.

These examples are finite corroboration only. The general result is proved by the exact construction and mapping-cone argument above.

## Relationship to prior work

Carcacía Campos [1] defines \(\nu\), establishes the sink mapping-cone lemma, and explicitly analyzes the three-object composition-table graph. That work already computes individual families of spheres, Moore spaces, real projective spaces, lens spaces, and bouquets; none of those individual calculations is claimed here as new. The contribution is an explicit **universal realization of every finite connected two-dimensional CW homotopy type by three objects**, including arbitrary attaching words and the resulting complete object-count trichotomy. Its central new step is the composition-table gadget that realizes an arbitrary prescribed finite system of attaching words in one connected sink-link graph.

Ben-Bassat [2] proves finite-monoid realizability for finite simply connected CW complexes, using monoids that permit nontrivial endomorphisms; this does not imply a three-object *acyclic* categorical model. Standard presentation-complex methods are from Hatcher [3]. Known individual surface constructions are special cases of the theorem, not an additional separate contribution.

## Limitations

The theorem applies only to connected finite CW complexes of dimension at most two, up to ordinary homotopy equivalence. It makes no claims for arbitrary higher-dimensional complexes, disconnected spaces, minimal morphism counts, uniqueness of realizing categories, strong or categorical equivalence, or efficiency of the table. The graph/word construction may be combinatorially large; it is finite and explicit. The literature comparison is not an exhaustive historical priority guarantee: equivalent formulations under presentations, collages or low-object nerves could be unindexed. Independent mathematical verification has not been performed.

## References

[1] I. Carcacía Campos, *How many points does it take to see the homotopy of a space? Minimal acyclic categorical models*, arXiv:2611.09718v1 (first publicly posted 2026-11-06), especially Sections 2.1 and 2.3; https://arxiv.org/html/2611.09718v1.

[2] O. Ben-Bassat, *On a Conjecture of Fiedorowicz*, arXiv:2610.38760v1 (first publicly posted 2026-10-28), especially Theorem C; https://arxiv.org/abs/2610.38760.

[3] A. Hatcher, *Algebraic Topology*, Cambridge University Press (2002), Sections 0 and 1.2; https://pi.math.cornell.edu/~hatcher/AT/AT.pdf.
