# Polarity traces and an irreducible Heawood Rips symmetry module

## Finding
Let \(\Pi\) be any finite projective plane of order \(q\ge2\), let \(H\) be its bipartite point–line incidence graph, and equip its vertices with shortest-path distance. Set \(X=\operatorname{VR}_{\le2}(H)\), the **inclusive** distance-two Vietoris–Rips simplicial complex. The connected bipartite graph \(H\) has a unique bipartition into points and lines. Write \(G=\operatorname{Aut}(H)\), and let \(\varepsilon:G\to\{+1,-1\}\) record whether an automorphism preserves or exchanges those two parts. There is a canonical (up to the choice of ordering of the two parts) integral \(G\)-module isomorphism
\[
\widetilde H_2(X;\mathbb Z)\cong\varepsilon\otimes_{\mathbb Z} H_1(H;\mathbb Z).
\]
Consequently the character on \(\widetilde H_2(X;\mathbb Q)\), which has rank \(q^3\), is
\[
\chi_X(g)=\begin{cases}
1-f_P(g)-f_L(g)+f_I(g),&\varepsilon(g)=+1,\\
t_I(g)-1,&\varepsilon(g)=-1.
\end{cases}
\]
Here \(f_P,f_L\) count individually fixed points and lines, \(f_I\) counts incidence flags fixed pointwise, and \(t_I\) counts incidence flags fixed as *unordered* edges by a part-exchanging automorphism. In particular, if \(\rho\) is any polarity (an involutory point–line duality), then
\[\boxed{\chi_X(\rho)=a(\rho)-1,}\]
where \(a(\rho)\) is its number of absolute points.

For the Fano plane \(\operatorname{PG}(2,2)\), the full \(336\)-element group \(\operatorname{Aut}(H)\cong\operatorname{PGL}_2(7)\) acts on the eight-dimensional rational group \(\widetilde H_2(X;\mathbb Q)\) **absolutely irreducibly**. Its character on all nine conjugacy classes, in the order displayed below, is
\[
\boxed{(8,0,-1,0,1,2,-1,0,0).}
\]
There are no nonzero globally invariant classes. The absolute-point formula also distinguishes two different polarities of \(\operatorname{PG}(2,4)\): orthogonal and unitary polarities have traces \(4\) and \(8\), respectively, on the same rank-\(64\) integral second homology. The previously established nonequivariant homotopy and Betti numbers are not new results here; the contribution is the integral symmetry module, the polarity character and the explicit irreducibility/class character.

## Assumptions and scope
A finite projective plane of order \(q\) has \(N=q^2+q+1\) points and the same number of lines. Each point lies on \(q+1\) lines, and every two distinct points (respectively, lines) share exactly one incident line (respectively, point). No coordinatization or Desarguesian hypothesis is needed for the integral module theorem. All homology is singular homology of the geometric realization, equivalently integral simplicial homology of the given finite complex. Group actions are induced by graph automorphisms; a graph automorphism may exchange points and lines. The projective plane is assumed to exist; no existence assertion is made for arbitrary \(q\).

For the explicit Fano calculation, points and lines are each indexed by the nonzero vectors \(v\in\mathbb F_2^3\), and \(p_v\) is incident with \(\ell_w\) exactly when \(v\cdot w=0\). The \(168\) point–line-type-preserving automorphisms are induced by \(A\in\operatorname{GL}_3(2)\) as \(v\mapsto Av\) on points and \(w\mapsto A^{-T}w\) on lines. The canonical dot-product duality exchanges \(p_v\) with \(\ell_v\); composing it with these \(168\) collineations produces the entire \(336\)-element graph automorphism group.

## Proof
**1. The natural two-piece cover.** Distances between two distinct points or between two distinct lines are \(2\). A point and line have distance \(1\) if incident and \(3\) otherwise. Thus the scale-two clique complex has all-point and all-line simplices. Every mixed simplex lies in either the simplex \(\{\ell\}\cup P(\ell)\), for one line \(\ell\), or \(\{p\}\cup L(p)\), for one point \(p\): two distinct points have at most one common line, and dually. Let \(U\) be the all-point simplex together with every simplex \(\{\ell\}\cup P(\ell)\), and let \(V\) be the analogous all-line simplex plus all \(\{p\}\cup L(p)\). The complex \(X\) is \(U\cup V\), and \(U\cap V\) is exactly the incidence graph \(H\). Each line vertex is contained in exactly one added maximal simplex of \(U\); these attachments collapse onto the all-point simplex, so \(U\) is contractible. Likewise \(V\) is contractible.

**2. Integral naturality and the sign.** With the ordered cover \((U,V)\), consider the short exact sequence of integral simplicial chains
\[
0\longrightarrow C_*(H)\xrightarrow{(i_U,-i_V)} C_*(U)\oplus C_*(V)
\xrightarrow{\text{sum}}C_*(X)\longrightarrow0.
\]
Its connecting map \(\partial_{\rm MV}:\widetilde H_2(X;\mathbb Z)\to H_1(H;\mathbb Z)\) is an isomorphism because both pieces are contractible and \(H\) is connected. If \(g\) preserves the two parts, it preserves the ordered cover and commutes with \(\partial_{\rm MV}\). If \(g\) exchanges the parts, it interchanges \(U\) and \(V\), which sends the signed injection \((i_U,-i_V)\) to its negative, and hence \(\partial_{\rm MV}g=-g\partial_{\rm MV}\). This proves the displayed integral \(G\)-module isomorphism with the bipartition-sign twist, without assuming an equivariant contraction of either piece. In particular \(H_1(H;\mathbb Z)\) is free of rank \(|E(H)|-|V(H)|+1=(q+1)N-2N+1=q^3\). Every other positive-degree integral reduced homology group of \(X\) vanishes, a nonequivariant fact already established in prior work.

**3. The exact character.** Orient every incidence edge from the point side to the line side. Since \(H\) is connected, the equivariant chain identity in the rational representation ring is
\[
[H_1(H;\mathbb Q)]=[C_1(H;\mathbb Q)]-[C_0(H;\mathbb Q)]+[\mathbf1].
\]
For a part-preserving \(g\), its signed action on graph edges has trace \(f_I(g)\), and the vertex-permutation trace is \(f_P(g)+f_L(g)\). For a part-reversing \(g\), the vertex trace is zero; each fixed *unoriented* incidence edge has orientation sign \(-1\), so the edge trace is \(-t_I(g)\). Multiplying by the bipartition sign yields precisely the two displayed formulas. A polarity reverses type and has order two; a flag \(\{p,\ell\}\) is fixed setwise precisely when \(\ell=\rho(p)\) and \(p\) is incident to \(\rho(p)\). Thus \(t_I(\rho)=a(\rho)\), giving the absolute-point formula.

**4. The Fano-plane full character.** The projective linear description in the assumptions enumerates the full automorphism group. For each conjugacy class the tuple \((\varepsilon,\operatorname{ord},\text{class size},\chi_X)\) is:

| Part sign | Order | Class size | Degree-two trace |
| ---: | ---: | ---: | ---: |
| \(+1\) | 1 | 1 | 8 |
| \(+1\) | 2 | 21 | 0 |
| \(+1\) | 3 | 56 | -1 |
| \(+1\) | 4 | 42 | 0 |
| \(+1\) | 7 | 48 | 1 |
| \(-1\) | 2 | 28 | 2 |
| \(-1\) | 6 | 56 | -1 |
| \(-1\) | 8 | 42 | 0 |
| \(-1\) | 8 | 42 | 0 |

The last two rows are distinct conjugacy classes, although these four recorded invariants coincide. The sum of class sizes is \(336\). The squared-character inner product is
\[
\langle\chi_X,\chi_X\rangle_G=\frac{64+56+48+112+56}{336}=1,
\]
so the complexification is irreducible; the rational representation is therefore absolutely irreducible. Its invariant-space dimension is \((8-56+48+56-56)/336=0\). This conclusion uses the complete character and not merely the known rank eight.

**5. Distinguishing projective polarities.** In \(\operatorname{PG}(2,4)\), the dot-product symmetric form gives an orthogonal polarity, whose absolute points satisfy \(\sum_i x_i^2=0\), equivalently \(\sum_i x_i=0\) in characteristic two: exactly five projective points. The Hermitian form obtained using field conjugation \(x\mapsto x^2\) gives a unitary polarity, whose absolute points satisfy \(\sum_i x_i^3=0\), equivalent to having exactly two nonzero coordinates: exactly nine projective points. The polarity trace formula consequently gives \(4\) and \(8\) on the same \(64\)-dimensional homology space. The statement identifies genuine distinct equivariant information, not a new nonequivariant Betti number.

## Verification
The standalone standard-library Python program `verify_plane_equiv.py` constructs all \(168\) Fano collineations and their \(168\) type-reversing compositions; checks all \(336\) incidence-preserving permutations; constructs the \(331\) simplices of the Fano scale-two Rips complex; and compares an independently evaluated *signed simplicial Lefschetz trace* with the bipartition-twisted graph-cycle character for **each of the 336 permutations**. It computes conjugacy classes by exact conjugation, checks their nine sizes sum to \(336\), and independently checks the character norm and invariant multiplicity. For \(\operatorname{PG}(2,3)\) it independently builds \(16{,}720\) Rips faces and checks six automorphisms against their signed direct Lefschetz sums, including a polarity. For \(\operatorname{PG}(2,4)\) it enumerates projective coordinates over an explicit four-element field, independently counts the \(105\) flags and the five versus nine absolute points of the two polarities. The recorded reproducible output is `verification_output.txt`. These finite computations corroborate the claims about the small planes; the all-plane integral theorem follows from the structural chain proof rather than finite sampling.

## Relationship to prior work
Adamaszek's 2011 *Clique complexes and graph powers* defines the graph-distance Rips setting and proves topological results for powers of cycles and other graphs. Its original text was inspected, including the introduction and results on graph squares. Larrión, Pizaña, and Villarroel-Flores (2009), *The fundamental group of the clique graph*, prove that clique complexes of squares of connected bipartite graphs and their two bipartition-induced subgraphs have the same fundamental group. Their full openly posted author version was inspected, including Theorem 3.1. Neither source describes the character above.

The published result *Scale-two Vietoris–Rips complexes of finite projective-plane incidence graphs* already determines \(X\simeq\bigvee^{q^3}S^2\), its full nonequivariant barcode, and the same canonical \(U\cup V\) cover. Its complete `RESULT.md` proof was inspected. Those homotopy and Betti conclusions are prior art, and the formal cover-and-Mayer–Vietoris sign mechanism is a natural refinement of that proof. The published result does **not**, however, state the integral automorphism module or determine the Fano nine-class character, its absolute irreducibility, or the two contrasting \(\operatorname{PG}(2,4)\) polarity traces. Different published homology representations of Heawood *matching* and *independence* complexes concern different simplicial objects; they do not imply this scale-two Rips representation. Published graph automorphism descriptions alone do not specify the action on these Rips two-cycles.

## Limitations
The structural formula is an exact integral statement but is directly supported by the known nonequivariant cover; its novelty is in correctly tracking the duality sign and extracting the explicit symmetry invariants. An unindexed group-representation computation or a more general equivariant cover theorem could contain equivalent character consequences; publication priority is not absolute. The 336-element computation and its field-four polarity counterpart are finite reproducibility checks, not independent certification. The homology character does not give the full equivariant homotopy type, cup products, or integral decomposition into indecomposable lattices. Statements apply only to the scale-two graph metric and projective-plane incidence graphs; general connected bipartite incidence geometries do not necessarily have the contractible two-piece cover. No independent mathematical validation has been performed.

## References
1. M. Adamaszek, *Clique complexes and graph powers*, arXiv:1104.0433 (first submitted 2011-04-03), https://arxiv.org/abs/1104.0433.
2. F. Larrión, M. A. Pizaña and R. Villarroel-Flores, *The fundamental group of the clique graph*, European Journal of Combinatorics 30 (2009), 288–294, DOI:10.1016/j.ejc.2007.12.006; author manuscript https://xamanek.izt.uam.mx/map/papers/Fundame06w.pdf.
3. *Scale-two Vietoris–Rips complexes of finite projective-plane incidence graphs*, published public mathematical record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-scale-two-vietoris-rips-complexes-of-finite-projective-plane-inc--c3740b96b3c3.
4. *Topological Symmetry Groups of the Heawood Graph*, Symmetry 12 (2020), 546, https://www.mdpi.com/2073-8994/12/4/546 (automorphism-group context only).
