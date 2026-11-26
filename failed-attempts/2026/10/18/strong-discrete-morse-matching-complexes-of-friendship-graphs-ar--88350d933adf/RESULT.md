# Strong discrete-Morse matching complexes of friendship graphs are uniform sphere wedges

## Finding
For each integer \(n\geq 2\), let \(F_n\) be the friendship graph, also called the triangular Dutch windmill: the one-dimensional simplicial complex formed by identifying one vertex of each of \(n\) copies of the three-cycle \(C_3\). In particular, the triangular regions are *not* filled simplices. Let \(\mathcal{SM}(F_n)\) be the **full** strong discrete-Morse matching complex defined as the downward closure of the vertex-filtration-generated matchings of Knudson and Owens–White. Then

\[
\mathcal{SM}(F_n)\simeq \bigvee^{\,3^n+2n} S^{n-1}.
\]

More precisely, writing \(P_n(t)=\sum_{\sigma\in\mathcal{SM}(F_n)}t^{|\sigma|}\), **including the empty face**, the entire face enumerator is

\[
P_n(t)=(1+4t)^n+2nt(1+2t)^{n-1}.
\]

For the separately handled boundary \(n=1\), the complex consists of six isolated vertices, equivalently a wedge of five zero-spheres, and the face polynomial remains valid. The main decomposition and suspension argument below are stated for \(n\ge2\).

## Assumptions and scope
Vertices of \(F_n\) are \(h,a_1,b_1,\dots,a_n,b_n\). Its edges are exactly \(\{h,a_i\},\{h,b_i\},\{a_i,b_i\}\) for each \(1\le i\le n\). Every graph edge is a one-simplex; no two-simplices are included. A Hasse pair \(u\to v\) denotes the pairing between the vertex \(u\) and the edge \(\{u,v\}\); the arrow points from the newly entered vertex to its unique earlier neighbor. In a vertex filtration, a newly entered vertex is strongly collapsed precisely when its descending link is a cone. For a one-dimensional graph that descending link is a discrete set of previously entered neighbors, hence this happens exactly when there is a **unique** earlier neighbor. The full matching complex includes every subset of every such induced matching, not just maximal-cardinality matchings.

The claim is an integral homotopy classification of the resulting finite abstract simplicial complex for every \(n\ge2\); it makes no claim about the ordinary graph matching complex, the ordinary discrete-Morse complex, or the pure strong-Morse subcomplex when defined by facets of globally maximal dimension.

## Proof
**Step 1: A four-choice join.** In the \(i\)-th petal define the four discrete vertices of the matching complex

\[
D_i=\{a_i\to b_i,\ b_i\to a_i,\ a_i\to h,\ b_i\to h\},\qquad
P_i=\{a_i\to h,\ b_i\to h\}\subset D_i.
\]

These are zero-dimensional simplicial complexes, not simplices on four or two vertices. Any vertex-filtration matching without a hub-headed pair contains at most one matching arrow from each \(D_i\). Indeed, before the hub is entered, only the second outer vertex of a petal can have a unique earlier neighbor, namely the first outer vertex; after the hub has entered, only the first outer vertex of each previously unentered petal can have a unique earlier neighbor, namely the hub. A petal split across hub entry contributes no pair: its later outer vertex sees both the hub and the other outer vertex.

Conversely, any choice of one element from every \(D_i\) occurs simultaneously in some vertex filtration with no hub-headed pair. For internal arrows, place the two outer vertices of the relevant petals before \(h\), in the specified order; place \(h\) next; and for outer-to-hub arrows, place the first chosen outer vertex of each remaining petal after \(h\), followed by its partner. If at least two petal vertices precede \(h\), the hub has at least two earlier neighbors and hence yields no hub-headed arrow; if none precede, the hub has no earlier neighbor. Therefore, the collection of all faces without a hub-headed pair is exactly

\[
A=D_1*D_2*\cdots*D_n.
\]

Each discrete four-point complex has the homotopy type of a wedge of three zero-spheres. Iterating the join formula yields

\[
A\simeq\bigvee^{3^n}S^{n-1}.
\]

**Step 2: All exceptional cones.** If the hub does produce an arrow \(h\to a_i\) or \(h\to b_i\), exactly that one outer vertex has been entered before it. The other outer vertex of petal \(i\) then sees two earlier neighbors and cannot yield a pair. Every other petal is entered after \(h\), and hence contributes at most one of the two arrows from \(P_j\). All such choices are attainable by the order containing the selected old neighbor, then \(h\), then the chosen outer-to-hub vertices of other petals, followed by the remaining vertices. Define

\[
L_i=\bigast_{j\ne i}P_j\cong S^{n-2},\qquad
C_{i,\epsilon}=\{h\to\epsilon_i\}*L_i\quad(\epsilon_i\in\{a_i,b_i\}).
\]

Each \(C_{i,\epsilon}\) is a cone, and the full matching complex is exactly

\[
\mathcal{SM}(F_n)=A\cup\bigcup_{i=1}^{n}(C_{i,a}\cup C_{i,b}).
\]

No two distinct cones have a common face containing a hub-headed matching vertex, since each cone has its own distinct apex. Consequently, when a cone is attached, its intersection with the complex already assembled is precisely its base \(L_i\subset A\).

**Step 3: All attaching maps vanish.** The inclusion \(L_i\hookrightarrow A\) factors through the explicit simplicial cone \(\{d_i\}*L_i\subset A\), where \(d_i\) can be any one vertex of \(D_i\). Thus this inclusion is nullhomotopic even at the level of a chosen simplicial cone, and remains nullhomotopic in every complex subsequently assembled. Attaching \(C_{i,\epsilon}\cong\operatorname{Cone}(L_i)\) along the nullhomotopic inclusion adds a wedge summand \(\Sigma L_i\simeq S^{n-1}\). This applies successively to all \(2n\) exceptional cones. Together with Step 1 it proves the claimed wedge of \(3^n+2n\) copies of \(S^{n-1}\). The reasoning also applies for \(n=2\), when each \(L_i\) is a two-point zero-sphere, because the nullhomotopy explicitly extends over a cone in \(A\).

**Step 4: The exact face enumerator.** The face polynomial of \(A\) is \((1+4t)^n\). Faces in the exceptional cones not already in \(A\) are precisely those containing the unique hub-headed apex. For each of the \(2n\) possible apices their generating function is \(t(1+2t)^{n-1}\). Such sets are pairwise disjoint, giving the stated polynomial without double-counting. At \(n=1\), the hub can pair to either outer vertex and each of the four outer-headed arrows occurs, making six isolated points.

## Verification
The accompanying standalone script `verify_friendship.py` constructs the graph and computes the unique-neighbor rule directly from vertex orders. It compares the **complete downward-closed face sets** against the join-and-cone construction for \(1\le n\le5\). It enumerates all \((2n+1)!\) vertex orders for \(1\le n\le4\), and uses an independent subset dynamic program for \(n=5\). It also computes mod-two simplicial homology exactly on those finite complexes. It confirms reduced Betti ranks \(5,13,33,89,253\) in dimensions \(0,1,2,3,4\), respectively, and zero in other dimensions. Full output is stored in `verification_output.txt`.

This enumeration corroborates the classification for five initial values only. The infinite-family statement is proved by the explicit decomposition and nullhomotopic attachments in Steps 1–3, not extrapolated from experiments.

## Relationship to prior work
Knudson and Owens–White introduce \(\mathcal{SM}(K)\), its defining downward closure, and graph-family calculations for paths, stars and cycles; their disjoint-union join identity does not cover triangles sharing a vertex. The present formula treats the one-vertex amalgam \(F_n\), a different operation from disjoint union. The distinction between full and pure strong-matching complexes is maintained throughout.

Donovan and Scoville study the **ordinary edge-matching complex** of the same Dutch windmill graphs. Their Theorem 5.8 gives a contractible complex for triangular petals. That theorem does not imply the present statement: the ordinary edge-matching complex and the strong vertex-edge gradient-matching complex have different vertices and different faces. The contrast shows that changing the matching construction can alter homotopy even on the identical family of graphs.

Published calculations for ordinary discrete-Morse complexes, single cycles, and star graphs likewise do not provide the vertex-amalgamated strong-matching decomposition used here.

## Limitations
The theorem concerns the one-dimensional friendship graph, not a two-dimensional wedge of filled triangles. Only the **full** strong-matching complex is classified. The natural enumeration and homology checker verifies five small cases; it is not a computer proof of the infinite family. The search of accessible mathematical literature and mathematical-result indexes does not establish absolute worldwide priority; related unindexed work might exist. The result has not undergone an independent mathematical audit.

## References
1. K. P. Knudson and A. Owens–White, *Complexes of strong discrete Morse matchings*, arXiv:2609.06844v1, posted 2026-09-06. https://arxiv.org/html/2609.06844v1. In particular, Sections 3–4 (construction), 7–8 (examples), and 10 (disjoint unions).
2. C. Donovan and N. A. Scoville, *Star clusters in the matching, Morse, and generalized complex of discrete Morse functions*, New York Journal of Mathematics 29 (2023), 1393–1412, Theorem 5.8. https://nyjm.albany.edu/j/2023/29-54p.pdf.
