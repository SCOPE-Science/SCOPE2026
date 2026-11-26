# Integral automorphism modules of Borel–Moore two-point graph configurations

## Finding
Let \(G\) be a finite connected graph, viewed as a compact one-dimensional CW complex \(|G|\), and let
\[
U_2(G)=\{\{x,y\}\subset |G|:x\ne y\},\qquad V=H_1(|G|;\mathbb Z).
\]
For **untwisted integral Borel–Moore homology**, there are canonical isomorphisms, natural under every graph homeomorphism,
\[
H^{\mathrm{BM}}_j(U_2(G);\mathbb Z)\cong
\begin{cases}
\bigwedge^2V,&j=2,\\
V/2V,&j=1,\\
0,&j\ne1,2.
\end{cases}
\]
In particular, if \(g\) is any graph automorphism and \(t(g)=\operatorname{tr}(g_*|V\otimes\mathbb Q)\), then
\[
\operatorname{tr}(g_*|H_2^{\mathrm{BM}}(U_2(G);\mathbb Q))=
\frac{t(g)^2-t(g^2)}2.
\]
The degree-one integral \(2\)-torsion module is exactly the reduction of the graph cycle lattice modulo two. The statement is a classification of **integral automorphism actions**, not a new Betti-number calculation.

## Assumptions and scope
The graph is any nonempty finite connected one-dimensional CW complex; loops, multiple edges, bridges, and leaves are allowed. We use the unordered configuration space of *geometric points* and its ordinary, constant \(\mathbb Z\) coefficient system. We do not use the exchange-sign local system. The term Borel–Moore refers to locally finite homology, not ordinary homology of the open configuration space. Graph homeomorphisms induce proper self-homeomorphisms of the configuration space; arbitrary graph maps may create collisions and are **not** asserted to induce configuration-space maps. The theorem also applies equivariantly to any subgroup of the graph homeomorphism group.

## Proof
**1. Compact relative model.** Set \(S=\operatorname{Sym}^2(|G|)=(|G|\times|G|)/\mathfrak S_2\), and embed the closed diagonal \(\delta:|G|\to S\), \(x\mapsto\{x,x\}\). As \(S\) is a compact triangulable polyhedron, Borel–Moore chains of the open complement are the relative homology chains of its compactification. Thus, functorially under homeomorphisms,
\[
H_j^{\mathrm{BM}}(U_2(G);\mathbb Z)\cong H_j(S,\delta|G|;\mathbb Z).
\]
The pair construction preserves homotopies of graph maps: a homotopy \(F_t\) induces \(\operatorname{Sym}^2(F_t)\), which maps the diagonal to the diagonal for each \(t\). Hence a graph homotopy equivalence induces an equivalence of these compact pairs. It is enough to calculate on a bouquet \(R_b\) of \(b=\operatorname{rank}V\) oriented circles.

**2. The integral complex.** For the bouquet, after collapsing the diagonal, the relative cellular chain groups have \(b\) degree-one generators \(a_i\); in degree two they have triangular same-circle generators \(u_i\) and rectangular mixed-circle generators \(z_{ij}\), for \(1\le i<j\le b\). All relative degree-zero chains vanish. The oriented boundary is
\[
\partial u_i=2a_i,\qquad \partial z_{ij}=0.
\]
In the triangular cell, the two nondiagonal edges contribute equally, and the diagonal edge is zero in relative chains; the rectangular cell is a product of two closed circles. Consequently \(H_1(S,\delta|G|)= (\mathbb Z/2)^b\), \(H_2(S,\delta|G|)=\mathbb Z^{\binom b2}\), and all other groups vanish. These *ranks* and torsion orders agree with the previously published untwisted calculation; the natural identifications below are the refinement.

**3. Integral naturality in degree one.** The map \(j:|G|\to S\), \(x\mapsto\{x,x_0\}\), induces a natural isomorphism \(j_*:V\to H_1(S;\mathbb Z)\) (the map on homology is independent of basepoint). The diagonal satisfies \(\delta_*=2j_*\): both coordinates traverse the same loop, so their class in the symmetric product is twice the single-coordinate class. The relative homology long exact sequence and the injectivity of multiplication by two yield a natural isomorphism
\[
H_1(S,\delta|G|;\mathbb Z)\cong\operatorname{coker}(\delta_*:H_1(G)\to H_1(S))\cong V/2V.
\]
No noncanonical spanning-tree basis is used in this final identification.

**4. Integral naturality in degree two.** The second homology of \(S\) is canonically \(\bigwedge^2V\). Explicitly, the unordered quotient map \(q:|G|\times|G|\to S\) sends the homology cross product of cycles \(\alpha,\beta\in V\) to a class \(q_*(\alpha\times\beta)\); exchanging the factors reverses the sign in degree two, and the class for repeated cycles is zero. This descends to an alternating homomorphism \(\bigwedge^2V\to H_2(S;\mathbb Z)\). On the bouquet \(R_b\), its images for \(i<j\) are precisely the oriented mixed-circle rectangles \(z_{ij}\), giving an **integral basis**. Pair homotopy invariance extends the isomorphism naturally to all finite connected graphs. Since the map \(H_1(\delta|G|)\to H_1(S)\) is multiplication by two and thus injective, the relative long exact sequence gives a natural integral isomorphism \(H_2(S)\to H_2(S,\delta|G|)\). Composing proves the desired natural exterior-square identification.

**5. Symmetry character.** Naturality transports any automorphism action in degree two to \(\bigwedge^2(g_*|V)\). For every endomorphism of a finite-dimensional vector space over \(\mathbb Q\), the trace of the second exterior power is one half the square of the ordinary trace minus the trace of its square. Degree one is the action on \(V/2V\), as claimed. This completes the proof for all finite connected graphs.

## Verification
The accompanying `verify_bm.py` independently builds the relative cellular chain groups and integral boundary matrices from graph vertices and edges. It checks \(\partial^2=0\), rational second Betti ranks and mod-two first Betti ranks for paths, cycles, a bouquet of two triangles, and complete graphs through five vertices. Exact Smith normal forms verify that all nonunit elementary divisors are precisely one \(2\) for each independent graph cycle in four examples. Signed cellular Lefschetz traces for a pentagon, a petal-swapping involution, and permutations of four complete-graph vertices agree with the proposed exterior-square character. Run `python3 verify_bm.py` with Python 3 and SymPy. These finite computations are checks; the all-graph theorem follows from the preceding homotopy-invariant pair proof, not enumeration.

## Relationship to prior work
Khan's 7 August 2026 paper, Theorem 3.4, computes the untwisted integral Borel–Moore homology *groups* for two unordered graph particles, including \((\mathbb Z/2)^b\) and \(\mathbb Z^{\binom b2}\); those group computations are not new here. The publicly available *Exchange-sign Borel–Moore homology of two-point graph configurations* instead gives a graph-automorphism-natural **divided-square** integral representation for the different exchange-sign coefficient system; its proof explicitly notes the untwisted group calculation but does not state the untwisted integral automorphism modules or the alternating character. Classical symmetric-product constructions underpin the proof here: the exterior-square identification itself is elementary for one-dimensional CW complexes. The additional assertion identifies the **specific ordinary Borel–Moore pair and both integral symmetry modules**, not simply the graded homology groups or the sign-twisted module. Relevant symmetric-product literature can imply individual intermediate lemmas, so overlap beyond inspected statements remains a priority risk.

## Limitations
No assertion is made about ordinary singular homology of the noncompact configuration space, the sign local system, configurations of more than two particles, or arbitrary non-homeomorphic graph maps. The theorem concerns integral homology representations and does not classify quotient-space homology integrally. The naturality claim requires proper configuration-space self-maps furnished by graph homeomorphisms. Publication coverage beyond the inspected works and general symmetric-product literature remains a residual risk. Independent mathematical audit has not been performed.

## References
1. Munawar Khan, *Borel–Moore Homology of 2-Particle Unordered Configuration Spaces of Graphs via Discrete Morse Theory*, arXiv:2608.18143v1, first public 2026-08-07, especially Theorem 3.4 and §§2–3. https://arxiv.org/abs/2608.18143
2. *Exchange-sign Borel–Moore homology of two-point graph configurations*, public research note, October 2026, especially its Finding, Proof §§2–4 and Relationship to prior work. https://github.com/published-finding corpus/2026/blob/main/2026/10/11/SCOPE-exchange-sign-borel-moore-homology-of-two-point-graph-configurat--68e49e70a285/RESULT.md
3. Dmitry V. Gugnin, *On Integral Cohomology Ring of Symmetric Products*, arXiv:1502.01862 (2015), general symmetric-product homology functoriality. https://arxiv.org/abs/1502.01862
