# Three irreducible affine homology modules in the Clebsch neighborhood complex

## Finding
Let \(C\) be the standard five-regular Clebsch graph, let \(X=\mathcal N(C)\) be its **open** Lovász neighborhood complex, and let \(G=V\rtimes S_5=\operatorname{Aut}(C)\), where \(V\cong(\mathbb Z/2\mathbb Z)^4\) is the translation subgroup. Then the only nonzero reduced rational homology is \(\widetilde H_2(X;\mathbb Q)\cong\mathbb Q^{31}\). Its natural rational \(G\)-representation splits into **three pairwise nonisomorphic absolutely irreducible rational summands** of dimensions
\[
\boxed{\widetilde H_2(X;\mathbb Q)\cong U_6\oplus U_{15}\oplus U_{10}.}
\]
The three summands are uniquely characterized by the support of their \(V\)-characters: \(U_6\) has only the trivial character, \(U_{15}\) has the five characters indexed by singleton subsets of \([5]\), each of multiplicity three, and \(U_{10}\) has the ten characters indexed by two-element subsets, each of multiplicity one. The induced \(S_5\)-module on translation invariants is
\[
\boxed{\widetilde H_2(X;\mathbb Q)^V\cong\bigwedge^2\operatorname{Std}_{S_5},}
\]
where \(\operatorname{Std}_{S_5}\) is the four-dimensional rational standard representation. Consequently the ordinary topological translation quotient has reduced rational second Betti number six and no other reduced rational homology, whereas the full automorphism quotient is rationally acyclic:
\[
\boxed{\widetilde H_2(|X|/V;\mathbb Q)\cong\mathbb Q^6,\qquad \widetilde H_*(|X|/G;\mathbb Q)=0.}
\]

## Assumptions and scope
Use the vertex set \(V=\{x\in\mathbb F_2^5:\sum_i x_i=0\}\), written as even-weight five-bit integers. Vertices \(x,y\) are adjacent exactly when \(x+y=\mathbf1+e_i\) for some \(i\in[5]\); this is the five-regular Clebsch graph, **not** its ten-regular complement. The group acts by \((t,\pi)\cdot x=t+\pi x\) for \(t\in V\), \(\pi\in S_5\). The complex consists of all nonempty subsets of the five-element open neighborhoods, together with the empty simplex. No closed neighborhoods are used. All homology representations and quotient conclusions are over \(\mathbb Q\); this statement neither computes integral torsion nor asserts equivariant homotopy equivalences.

The full automorphism-group assertion follows directly: the displayed transformations yield \(16\cdot5!=1920\) automorphisms. Their action is faithful. Every automorphism fixing the zero vertex permutes its five neighbors. A distance-two vertex is uniquely identified by the pair of zero-neighbors also adjacent to it, because the graph has parameters \((16,5,0,2)\). Thus an automorphism fixing zero is determined by its permutation on those five neighbors, giving at most \(5!\) choices; transitivity gives the upper bound \(16\cdot5!\).

## Proof
**1. Homology concentration.** Exhaustively generating all nonempty faces inside the sixteen five-point neighborhoods gives the face vector \((16,80,160,80,16)\). With the augmented degree-zero boundary, the successive boundary ranks computed over \(\mathbb F_2\) are \((1,15,65,64,16)\). These are also the ranks over \(\mathbb Q\), without assuming that modular ranks alone establish characteristic-zero homology. Indeed, the two initial ranks saturate the upper bounds \(1\) and \(16-1=15\); the chain identity bounds the next rank by \(80-15=65\). The top boundary is injective since its mod-two rank is \(16\), and the chain identity then bounds the preceding boundary rank by \(80-16=64\), attained modulo two. All rational ranks are therefore forced. Subtraction of adjacent boundary ranks gives \(\widetilde H_2(X;\mathbb Q)\cong\mathbb Q^{31}\) with every other reduced rational homology group zero.

**2. Complete affine character.** For any \(g\in G\), let \(f_d(g)\) be the signed number of oriented degree-\(d\) faces stabilized by \(g\). The simplicial Lefschetz identity and the homology concentration imply
\[
\chi(g)=\operatorname{tr}(g\mid\widetilde H_2(X;\mathbb Q))=\sum_{d=0}^4(-1)^d f_d(g)-1.
\]
This formula is evaluated by exact integer enumeration of all \(352\) faces for each of the \(1920\) affine permutations. Independently, every invariant face is a union of cycles of \(g\) on vertices, and the contribution of a nonempty invariant face with \(c\) cycles is \((-1)^{c+1}\), again followed by subtraction of one. Both methods agree on all \(1920\) group elements. The complete character has value-count distribution
\[
\begin{array}{c|rrrrrr}
\chi(g)&-5&-1&1&3&7&31\\\hline
\#\{g\}&80&825&944&60&10&1
\end{array}
\]
so its exact complex-character inner product is
\[
\langle\chi,\chi\rangle_G=\frac1{1920}\sum_{g\in G}\chi(g)^2=3.
\]

**3. Fourier splitting.** Translations \(t\in V\) of Hamming weight \(0,2,4\) have traces \(31,7,-1\), respectively. The sixteen rational characters of the elementary abelian group \(V\) are \(\lambda_A(t)=(-1)^{|A\cap\operatorname{supp}(t)|}\), with each character uniquely represented by a subset \(A\subseteq[5]\) of size at most two, because complementing \(A\) gives the same character on even-weight vectors. Fourier inversion gives multiplicities
\[
\frac1{16}\sum_{t\in V}\chi(t)\lambda_A(t)=
\begin{cases}6,&|A|=0,\\3,&|A|=1,\\1,&|A|=2.\end{cases}
\]
The \(S_5\) action permutes the five singleton-character spaces transitively and likewise the ten two-subset-character spaces. The direct sum of the respective eigenspaces is a rational \(G\)-subrepresentation of dimensions \(6,15,10\). The three support orbits are disjoint, hence the summands are nonzero and pairwise nonisomorphic. Since the character norm of the complete representation is exactly three, the three summands must each have complex-character norm one; thus all three are absolutely irreducible. Rationality follows because the projectors \(16^{-1}\sum_{t\in V}\lambda_A(t)t\) have rational coefficients.

**4. The six-dimensional module and quotients.** Averaging the full character over translations determines the character of \(\widetilde H_2(X;\mathbb Q)^V\) on the seven cycle types of \(S_5\). For cycle types \((1^5),(2,1^3),(2^2,1),(3,1^2),(3,2),(4,1),(5)\), the respective traces are
\[
(6,0,-2,0,0,0,1).
\]
These agree class-by-class with the exterior-square character \(\big((\#\operatorname{Fix}(\pi)-1)^2-(\#\operatorname{Fix}(\pi^2)-1)\big)/2\) of the standard representation. Its character norm equals one and its average equals zero, so it is nontrivial and absolutely irreducible. For any finite group acting on a finite simplicial complex, barycentric subdivision and rational averaging identify the rational homology of the ordinary quotient with the invariant homology. Applying this to \(V\) and to \(G\), and using the vanishing of all other reduced homology, proves the stated quotient conclusions.

## Verification
Run `python3 verify.py` from the containing directory. It has no third-party dependencies and reconstructs the graph, all simplices, boundary matrices over \(\mathbb F_2\), all \(1920\) symmetry permutations, two independent signed-character formulas, the translation Fourier coefficients, the seven \(S_5\) trace classes, and the character norm. The recorded `verification_output.txt` ends in `CLEBSCH_AFFINE_FOURIER_HOMOLOGY_PASS`. The finite verifier is an exhaustive proof of the finite calculations, not evidence about unexamined graphs.

## Relationship to prior work
Lovász introduced open-neighborhood complexes in connection with graph coloring. Matoušek and Ziegler's publicly posted treatment explains neighborhood and box complexes and their equivariant topology, without calculating the Clebsch affine homology character. Hughes studied representations on neighborhood complexes of Cayley graphs, but his dissertation states that the default complex uses the distance set \(\{0,1\}\), i.e. closed neighborhoods; its concrete examples do not determine this open-neighborhood \(V\rtimes S_5\) module. A published calculation of the open-neighborhood complex of the five-regular Clebsch graph gives the prior nonequivariant homotopy equivalence to a wedge of thirty-one two-spheres, without determining the rational automorphism representation. The homology dimension is prior information, not the present novelty claim. The contribution here is the **three-orbit Fourier multiplicity spectrum, the absolutely irreducible \(6+15+10\) decomposition, the standard exterior-square identification, and the two rational quotient consequences**.

## Limitations
No integral representation lattice, integral quotient homology, equivariant homotopy type, or classification for larger folded cubes is established. No uniqueness in the full mathematical literature is claimed; equivalent results in unindexed material may exist. The reasoning uses a complete but finite exact computation, whose independent mathematical validation is outstanding.

## References
1. J. Matoušek and G. M. Ziegler, *Topological lower bounds for the chromatic number: A hierarchy*, arXiv:math/0208072, first public posting 2002-08-09. https://arxiv.org/abs/math/0208072
2. L. Lovász, *Kneser's conjecture, chromatic number, and homotopy*, J. Combin. Theory Ser. A 25 (1978), 319–324, DOI:10.1016/0097-3165(78)90022-5. [Historical print reference; no first-public day asserted.]
3. J. Hughes, *Group Action on Neighborhood Complexes of Cayley Graphs*, Colorado State University dissertation, 2014. https://mountainscholar.org/bitstreams/ed6738aa-0198-4384-9541-620f793f020b/download
4. *The five-regular Clebsch neighborhood complex is a wedge of thirty-one two-spheres*, public mathematical research record, 2026. https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-the-5-regular-clebsch-neighborhood-complex-is-a-wedge-of-31-2-sp--1dc11cc6574a
5. P. Csorba, *On the simple \(\mathbb Z_2\)-homotopy types of graph complexes and their simple \(\mathbb Z_2\)-universality*, Canad. Math. Bull. 51 (2008), 535–544, DOI:10.4153/CMB-2008-053-9.
