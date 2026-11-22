# Graph–Bier equators are boundaries of graph handlebodies

## Finding
Let \(G\) be a finite connected simple graph on \(N\ge5\) labeled vertices, viewed **strictly as a one-dimensional simplicial complex**: its simplices are vertices and edges, not filled triangles. Set \(K=G\), let \(K^{\vee}\) be its combinatorial Alexander dual on the same ground set, and form the ordered polytopal deleted product \(M(G)\) from cells \(\sigma\times\tau\) with disjoint nonempty faces \(\sigma\in K\), \(\tau\in K^{\vee}\). Then \(M(G)\) is a connected closed orientable PL manifold and
\[
\dim M(G)=N-3,\qquad
|M(G)|\cong_{\mathrm{PL}}\#^{g}\bigl(S^1\times S^{N-4}\bigr),\quad g=|E(G)|-N+1.
\]
The convention \(\#^0(S^1\times S^{N-4})=S^{N-3}\) applies. In particular, for the complete graph on \(q+4\) vertices and every integer \(q\ge1\),
\[
\operatorname{DConf}(\Delta^{q+3,1},\Delta^{q+3,q})
\cong_{\mathrm{PL}}\#^{\binom{q+3}{2}}(S^1\times S^q).
\]
This is a PL strengthening of the \(p=1\) instances of the mixed-skeleton homotopy-type conjecture in González–González–Pérez-Morales (2026). More generally, the manifold type is insensitive to the graph's degree sequence, triangles as graph cycles, and other structure beyond its vertex count and cycle rank.

## Assumptions and scope
The graph is connected, simple, and finite, with at least five vertices. All graph cycles, including three-cycles, are **unfilled**. Regard the empty face as a member of every simplicial complex, including \(K\), but neither product coordinate is allowed to have an empty face. Precisely,
\[
K^{\vee}=\{B\subseteq[N]:[N]\setminus B\notin K\},\qquad
M(G)=\bigcup_{\substack{\varnothing\ne\sigma\in K,\;\varnothing\ne\tau\in K^{\vee}\\\sigma\cap\tau=\varnothing}} |\sigma|\times|\tau|.
\]
All manifolds, sphere products, handlebodies, and connected sums are understood in the PL category. The integer \(g\) is the first Betti number of the connected graph. For \(N\ge5\), both red and blue vertex sets of the Bier sphere are genuine vertices, and \(K\) is a full subcomplex of its Bier sphere.

## Proof
**1. Bier sphere and color level.** Form the deleted join \(B=K*_{\Delta}K^{\vee}\), with a red copy of each vertex in \(K\) and a blue copy of each vertex in \(K^{\vee}\), and only those joins whose underlying vertex sets are disjoint. The Bier sphere theorem [1,2] identifies \(|B|\) as a combinatorial PL sphere of dimension \(N-2\). Give each red vertex height one and each blue vertex height zero and extend linearly over the simplices. Call the resulting PL function \(h\).

For any mixed simplex \(|\sigma^+*\tau^-|\), a point of height \(1/2\) uniquely decomposes as an equal convex combination of one point in \(|\sigma^+|\) and one point in \(|\tau^-|\). The mutually inverse maps
\[
 (x,y)\longmapsto \tfrac12x^++\tfrac12y^-,\qquad
 z\longmapsto(2z_{\mathrm{red}},2z_{\mathrm{blue}})
\]
identify the level \(h^{-1}(1/2)\), cell by cell and compatibly on faces, with the stated polytopal deleted product \(M(G)\). Each cell has dimension \((|\sigma|-1)+(|\tau|-1)\).

**2. The superlevel is a regular neighborhood of the graph.** In the Bier sphere, the induced full subcomplex on the red vertices is precisely \(K\), because adding an empty blue face imposes no further restriction. The standard *full-subcomplex regular-neighborhood lemma* in PL topology applies: in a triangulated PL manifold equipped with a binary vertex coloring whose red vertices span a full subcomplex, the superlevel \(\{h\ge1/2\}\) is a closed PL regular neighborhood of that red subcomplex, and its frontier is the color level \(h^{-1}(1/2)\). One sees this directly by cutting every mixed edge at its midpoint and triangulating the resulting prisms: the upper pieces form a derived neighborhood of the full red subcomplex, and the midpoint prisms form its frontier. This is an equality of PL polyhedra up to the canonical subdivision and hence respects the PL structure. Let \(W=\{h\ge1/2\}\). Therefore \(M(G)=\partial W\).

**3. Handlebody classification.** A PL regular neighborhood of a connected graph in a PL manifold of dimension \(d=N-2\ge3\) is a \(d\)-dimensional \(0,1\)-handlebody: choose a ball at each vertex and an embedded one-handle for each edge. The ambient PL sphere is orientable, so this regular neighborhood is orientable. Choose a spanning tree of \(G\). Successively amalgamating its \(N-1\) tree handles with the incident vertex balls leaves a single \(d\)-ball; every one of the remaining \(g=|E(G)|-N+1\) edges contributes one orientable one-handle. Any orientable \(d\)-dimensional one-handlebody of genus \(g\) is PL equivalent to the boundary-connected sum of \(g\) copies of \(S^1\times D^{d-1}\) (or a ball if \(g=0\)). Taking boundaries gives
\[
\partial W\cong_{\mathrm{PL}}
\#^g\bigl(S^1\times S^{d-2}\bigr)
=\#^g\bigl(S^1\times S^{N-4}\bigr).
\]
For \(d=3\), the same statement is the classical oriented surface boundary of a three-dimensional handlebody. Thus it applies uniformly to every \(N\ge5\) and proves the general theorem, including connectedness and orientability.

**4. Mixed-skeleton specialization.** For \(K\) the one-skeleton of the simplex on \(N=q+4\) vertices, its Alexander dual consists precisely of all subsets of size at most \(N-3=q+1\), i.e. the \(q\)-skeleton of that simplex. Thus the deleted product in the theorem is exactly \(\operatorname{DConf}(\Delta^{q+3,1},\Delta^{q+3,q})\) under the convention of [3]. The complete graph has \(\binom N2\) edges, so its cycle rank is \(\binom N2-N+1=\binom{N-1}{2}=\binom{q+3}{2}\), yielding the claimed PL type.

## Verification
The included standalone Python program `check_bier_midsection.py` constructs all nonempty graph faces and all nonempty Alexander-dual faces, enumerates the cellular product chains, builds signed integral boundary matrices, and tests that successive boundaries compose to zero. For path graphs, cycle graphs, and complete graphs on five and six vertices it verifies the predicted Betti numbers over the finite fields of characteristic two and 101, in twelve independent examples. In these dimensions the expected Betti numbers are, respectively, \((1,2g,1)\) in dimension two and \((1,g,g,1)\) in dimension three. This confirms the combinatorial normalization and arithmetic on tested examples, but **does not constitute a proof of the universal PL-homeomorphism statement**. The proof is the Bier sphere, regular-neighborhood, and handlebody argument above; no independent verification has been performed.

## Relationship to prior work
Björner–Paffenholz–Sjöstrand–Ziegler [1] prove the deleted-join Bier sphere theorem used as an input, not the PL type of its color-midsection. Choi–Yoon–Yu [2] classify **full induced subcomplexes** of Bier spheres and study toric spaces; those are not the deleted-product equators and do not state the graph-handlebody classification. González–González–Pérez-Morales [3, Theorem 1.3] establish manifoldness of mixed-skeleton deleted products and formulate [3, Conjecture 1.6] for their connected-sum homotopy types. The present theorem establishes a PL type for the entire \(p=1\) column, not the remaining \(p\ge2\) rows, and extends to arbitrary connected graph–Alexander-dual pairs. The classical \(K_5\) genus-six surface case was known [3]. Thus the manifold-recognition and homological inputs from prior papers are distinguished from the new color-regular-neighborhood classification.

## Limitations
The theorem assumes a connected simple graph on at least five vertices, treated as a one-dimensional simplicial complex. No assertion is made for disconnected graphs, general higher-dimensional input complexes, the two-point deleted product of an arbitrary graph with itself, or mixed-skeleton parameters \(p\ge2\). The proof relies on the classical PL regular-neighborhood lemma for full subcomplexes and the Bier PL-sphere theorem, cited as established inputs. Computations cover only \(N\in\{5,6\}\) and two coefficient fields. Novelty is assessed against the literature inspected here, not certified against every possible unpublished or unindexed equivalence. Independent mathematical audit has not occurred.

## References
1. A. Björner, A. Paffenholz, J. Sjöstrand, and G. M. Ziegler, *Bier spheres and posets*, arXiv:math/0311356, first publicly posted 20 November 2003, https://arxiv.org/abs/math/0311356.
2. S. Choi, Y. Yoon, and S. Yu, *On the full subcomplexes of Bier spheres and their applications to real toric spaces*, arXiv:2503.05385v1, first publicly posted 7 March 2025, https://arxiv.org/html/2503.05385v1.
3. E. J. González, J. González, and M. C. Pérez-Morales, *Discrete Configuration Spaces of Simplex Skeleta: a Middle-Dimensional Manifold Phenomenon*, arXiv:2611.12847v1, first publicly posted 9 November 2026, https://arxiv.org/html/2611.12847v1, especially Theorem 1.3, Remark 1.5, and Conjecture 1.6.
