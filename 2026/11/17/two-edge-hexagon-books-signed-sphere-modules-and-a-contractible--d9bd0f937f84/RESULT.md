# Two-edge hexagon books: signed sphere modules and a contractible symmetry quotient

## Finding

For every integer \(h\ge2\), let \(G_h\) consist of the common two-edge path \(a-c-b\) and \(h\) internally disjoint four-edge paths \(a-x_i-y_i-z_i-b\), for \(1\le i\le h\). All edges have length one. Let \(K_h=\operatorname{VR}_{\le2}(V(G_h))\) be the inclusive Vietoris–Rips complex for the **graph-vertex shortest-path metric**. Then
\[
 |K_h|\simeq\bigvee^{h}S^2,\qquad \operatorname{Aut}(G_h)\cong S_h\times C_2.
\]
Moreover, as an integral module for this full automorphism group,
\[
 \widetilde H_2(K_h;\mathbb Z)\cong\mathbb Z[\{1,\ldots,h\}]\boxtimes\varepsilon,
\]
where permutations of the four-edge arms act on the evident integral basis by permutations, and the order-two pole swap (simultaneously reversing every arm) acts by minus the identity. All other reduced integral homology vanishes. The **actual geometric orbit spaces**, not merely their rational homology, satisfy
\[
 |K_h|/S_h\simeq S^2,\qquad |K_h|/(S_h\times C_2)\simeq *.
\]
Thus a nontrivial integral sphere-wedge has a contractible full-symmetry quotient. At integer scales one and two, the first homology of the graph has rank \(h\) and dies entirely at scale two, where \(h\) independent second-homology generators appear.

## Assumptions and scope

The vertices \(a,b,c,x_i,y_i,z_i\) are all distinct except where symbols deliberately repeat. An edge is present exactly when it belongs to one of the specified paths. The poles \(a,b\) are the two vertices of degree \(h+1\), and \(c\) is their unique common neighbor. The full automorphism group permutes the four-edge arms and independently interchanges the poles. The complexes use **vertices only**, not interior points of the metric graph; a face has all pairwise distances at most two. The statements cover every finite \(h\ge2\), with no extrapolation from finite tests.

## Proof

**1. Exact clique decomposition.** Set \(X=\{x_1,\ldots,x_h\}\), \(Z=\{z_1,\ldots,z_h\}\), and put
\[
 L=\Delta[\{a,c\}\cup X]\ \cup\ \Delta[\{b,c\}\cup Z]\ \cup\ \Delta[\{a,b,c\}],
\]
where \(\Delta[T]\) denotes the full simplex on \(T\). For each \(i\), write \(K_i\) for the induced scale-two Rips complex on \(\{a,b,c,x_i,y_i,z_i\}\). The distance-three pairs among those six vertices are exactly \(\{a,z_i\}\), \(\{b,x_i\}\), and \(\{c,y_i\}\). Thus \(K_i\) is the boundary of a three-dimensional cross-polytope, and \(|K_i|\cong S^2\).

Any vertices from two different four-edge arms at distance at most two are either two first vertices \(x_i,x_j\) (meeting through \(a\)) or two last vertices \(z_i,z_j\) (meeting through \(b\)). In particular, no such cross-arm clique contains an intermediate \(y_i\), or mixes first and last vertices. Every cross-arm clique therefore lies in \(L\), and each single-arm clique lies in its \(K_i\). Consequently,
\[
 K_h=L\cup K_1\cup\cdots\cup K_h.
\]
The complex \(L\) is a simplicial cone with apex \(c\). For every \(i\), the intersection of \(K_i\) with \(L\) and all other \(K_j\) is exactly
\[
 I_i=\Delta[\{a,c,x_i\}]\cup\Delta[\{b,c,z_i\}]\cup\Delta[\{a,b,c\}],
\]
which is also a cone with apex \(c\). No pair of the \(K_i\)'s meets beyond the common triangle on \(\{a,b,c\}\). Induction by the CW gluing lemma, applied to the inclusions of the contractible \(I_i\)'s, yields \(|K_h|\simeq\bigvee_i |K_i|\simeq\bigvee^h S^2\). This is an integral homotopy statement.

**2. Exact group and integral action.** For \(h\ge2\), only the poles have degree exceeding two. Every graph automorphism preserves their unordered pair and their unique common neighbor \(c\). The remaining components after removing the poles are the \(h\) internally disjoint length-four arms; they may be permuted freely. Once the poles are chosen, each arm has a unique orientation. Hence the full group is \(S_h\times C_2\).

Since \(L\) is a cone with globally fixed apex \(c\), its straight-line contraction to \(c\) is equivariant. Collapsing \(L\) to a point is therefore a full-group equivariant homotopy equivalence. In fact the resulting pointed space is **exactly** the wedge of \(K_i/I_i\) with the indicated arm permutations. Each quotient \(K_i/I_i\) is homotopy equivalent to \(S^2\), as \(I_i\) is a contractible CW subcomplex of \(K_i\). In the integral relative generators \(H_2(K_i,I_i;\mathbb Z)\cong\mathbb Z\), an arm permutation transports the canonical cross-polytope orientation from one arm to the other without a sign.

The pole swap sends \(a\leftrightarrow b\), \(x_i\leftrightarrow z_i\), and fixes \(c,y_i\). In the three octahedral opposite-vertex pairs \((a,z_i)\), \((x_i,b)\), and \((y_i,c)\), it swaps the first two pairs and reverses the endpoints of each; the third pair is fixed. Relative to oriented cross-polytope coordinates, its determinant is \((-1)(-1)^2=-1\). Hence it acts by minus the identity on each \(H_2(K_i,I_i;\mathbb Z)\). This gives the asserted **integral**, not just rational, group module.

**3. The orbit-space distinction.** Because the contraction of \(L\) is equivariant for every subgroup, it descends to a homotopy equivalence on each orbit space. Arm permutations identify the \(h\) summands of \(K_h/L\); therefore \(|K_h|/S_h\simeq |K_1/I_1|\simeq S^2\). Next, the pole-swap is a geometric orientation-reversing reflection of the octahedral two-sphere \(|K_1|\), with fixed great circle. Its quotient \(|K_1|/C_2\) is a closed disk. The image \(|I_1|/C_2\) is a contractible CW subcomplex of that disk: it remains a cone with apex the fixed vertex \(c\). Collapsing a contractible CW subcomplex is a homotopy equivalence, so
\[
 |K_h|/(S_h\times C_2)\simeq (|K_1|/C_2)/(|I_1|/C_2)\simeq *.
\]
These statements concern genuine orbit spaces, not Borel constructions or rationalization.

**4. First two persistence levels.** \(G_h\) has \(3+3h\) vertices and \(2+4h\) edges, so its cycle rank is \(h\). Since \(K_h\) is simply connected, the inclusion \(G_h\hookrightarrow K_h\) kills all first homology; since a graph has no second homology, all \(h\) second-homology generators are born at the second integer threshold. \(\square\)

## Verification

The dependency-free Python program `verify_double_spine.py` constructs the exact graph shortest-path distances and enumerates every clique at scale two for each integer \(1\le h\le6\). It independently reconstructs the union of explicit local octahedra and the common cone, checks the full face equality and every intersection, computes reduced mod-two Betti numbers by complete boundary-matrix elimination, and computes signed fixed-simplex Lefschetz traces under pole reversal and a transposition of two arms. Results agree with ranks \(h\), reversal traces \(-h\), and transposition traces \(h-2\). Run `python3 verify_double_spine.py` from the package directory. These finite tests corroborate, but are not the proof of, the all-parameter topology, integral representation, or quotient contractibility.

## Relationship to prior work

Adamaszek, Adams, Gasparovic and collaborators (arXiv:1712.06224; 2017) give general Rips-gluing criteria. Their Theorem 3.15 requires that a glued path of length \(\alpha\) satisfy the **strict** inequality \(\alpha<\ell/3\), which fails here at the exact boundary \(\alpha=2=6/3\). Their more abstract Theorem 3.13 may be applied by a separate local check and thereby already implies the **nonequivariant wedge decomposition**; the wedge-rank formula alone is not claimed as a novel conceptual theorem. Neither gives the integral full-automorphism module or the actual symmetry orbit-space contraction for this family.

The recent work of Bendersky, Elia and Grbić (arXiv:2605.00705, publicly submitted 1 May 2026) develops topological methods for graph-metric Rips complexes, including cross-polytope homology representatives, on hypercubes. Galetto, Montaño and Wellner (arXiv:2606.20784, publicly submitted 18 June 2026) classify equivariant homology of **hypercube** Rips complexes. Neither covers overlapping hexagon books. The published record *A hexagon-packing classification of scale-two graph Rips complexes* treats girth-six graphs only when **every two six-cycles have disjoint edge sets**; the present common two-edge-spine graphs violate that hypothesis. That paper does not determine the signed symmetry module or the orbit-space homotopy. These are statement-and-implication comparisons, not novelty deductions from different titles.

## Limitations

Only scale two and the change from scale one are classified. The automorphism-module description is integral, but no equivariant homotopy **splitting** of the unquotiented space as a literal wedge action is asserted. The contractibility statement is for the topological orbit space, not the homotopy quotient. The very general gluing theorems may subsume the nonequivariant wedge claim; novelty is restricted to the explicit integral symmetry action and genuine quotient homotopy. An equivalent unindexed equivariant calculation is still a possibility. Independent external review has not been performed.

## References

1. M. Adamaszek, H. Adams, E. Gasparovic, M. Gommel, E. Purvine, R. Sazdanovic, B. Wang, Y. Wang and L. Ziegelmeier, *On Homotopy Types of Vietoris–Rips Complexes of Metric Gluings*, arXiv:1712.06224 (first public 18 December 2017), Theorems 3.13 and 3.15, Proposition 4.1. https://arxiv.org/pdf/1712.06224
2. M. Bendersky, S. Elia and J. Grbić, *Cohomological properties of the Vietoris–Rips Complex of a Hypercube Graph*, arXiv:2605.00705 (first public 1 May 2026). https://arxiv.org/abs/2605.00705
3. F. Galetto, J. Montaño and Z. Wellner, *Homology of Vietoris–Rips complexes of hypercube graphs via group actions*, arXiv:2606.20784 (first public 18 June 2026). https://arxiv.org/abs/2606.20784
4. *A hexagon-packing classification of scale-two graph Rips complexes*, public finding, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-a-hexagon-packing-classification-of-scale-two-graph-rips-complex--70b9bc9b3abb (consulted for the edge-disjointness hypothesis; no authorship ascribed).
