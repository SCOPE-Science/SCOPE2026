# A primitive integral \(S_5\times C_2\)-orbit basis for Desargues independence homology

## Finding
Let \(L=\{0,1,2,3,4\}\), let \(D=H(5,2)\) be the inclusion graph joining each two-element subset of \(L\) to each containing three-element subset, and set \(X=\operatorname{Ind}(D)\). The group \(S_5\) relabels \(L\); the central involution \(c\) complements subsets. The resulting faithful action is \(G=S_5\times C_2\).

For each \(i\in L\), the six edges of \(D\) of the form \(\{A,A\cup\{i\}\}\), where \(A\in\binom{L\setminus\{i\}}2\), form an induced matching \(M_i\). Order the six edges by the lexicographic order of their two-element lower endpoints, and orient the independence sphere by the ordered join
\[
z_i=\mathop{\ast}_{A\in\binom{L\setminus\{i\}}2}([A]-[A\cup\{i\}])\in \widetilde C_5(X;\mathbb Z).
\]
The specified lexicographic ordering fixes the orientations unambiguously. Reordering the six zero-dimensional join factors by an odd permutation would reverse this orientation, so the order is part of the definition; the group action below takes the resulting signs into account.

The five cycles are an integral basis, and the full action on this basis is
\[
\sigma z_i=z_{\sigma(i)}\quad(\sigma\in S_5),\qquad cz_i=-z_i.
\]
Consequently the complete integral module is
\[
\boxed{\widetilde H_5(X;\mathbb Z)\cong \mathbb Z[L]\boxtimes\varepsilon_{C_2}.}
\]
In particular, a five-cycle on labels acts by the integral regular permutation matrix of the cyclic group of order five; reducing that action modulo five yields one indecomposable Jordan block of size five. This integral conclusion does not follow from a rational character calculation alone.

## Assumptions and scope
The vertex set of \(D\) is \(\binom{L}{2}\sqcup\binom{L}{3}\), with exactly thirty edges given by inclusion. Its independence complex contains vertex sets spanning no inclusion edge, using standard increasing-vertex simplex orientations. The asserted representation is over \(\mathbb Z\), in reduced degree five, for the specified natural faithful group action. All calculations are exact, finite and exhaustive. No assertion is made about integral quotient homology or higher-stage incidence graphs.

## Proof
**1. Induced octahedral spheres.** For fixed \(i\), each two-subset \(A\) of the other four labels has exactly one neighbor \(A\cup\{i\}\) in the selected twelve vertices. Indeed, if \(A\subset B\) for two vertices in this set, \(i\in B\setminus A\) and \(|B\setminus A|=1\), forcing \(B=A\cup\{i\}\). Thus the induced graph is six disjoint edges. Its independence complex is the join of six copies of \(S^0\), hence an embedded \(S^5\). The signed join \(z_i\) has exactly \(2^6=64\) facets and vanishing integral simplicial boundary.

**2. Exact rank upper bound, not an assumption about rational homology.** Enumerate independent subsets by the inclusion rule: the face counts by cardinality, including the empty face, are
\[
(1,20,160,660,1510,1924,1320,480,115,20,2).
\]
On the augmented face poset, stage through vertices in the standard lexicographic order, pairing any still-unmatched face not containing the stage vertex with its still-unmatched union with that vertex. This gives \(3103\) matched pairs and exactly six unmatched faces: one of dimension four and five of dimension five. To certify acyclicity, orient every Hasse edge downward except the matched edges upward. A complete directed topological sort visits all \(6212\) faces along the \(30380\) Hasse incidences. Discrete Morse theory therefore bounds the rank of \(\widetilde H_5(X;\mathbb Z)\) by five. Since the Morse chain group in degree five is free of rank five and has no dimension-six generator, this homology is a subgroup of \(\mathbb Z^5\), hence torsion-free.

**3. Primitive integral detection.** For fixed \(i\), write the other four labels in increasing order as \(a<b<c<d\). Form the independent six-vertex set
\[
F_i=\{\{a,b\},\{b,c\},\{c,d\},\{a,d\},\{a,c,i\},\{b,d,i\}\}.
\]
It is a maximal face of \(X\); this follows directly by testing the remaining fourteen vertices against its six selected vertices, and every check is replayed by the verifier. Consequently its coordinate-cochain \(\phi_i\in C^5(X;\mathbb Z)\) is closed, since the complex has no six-simplex containing \(F_i\). The signed pairings satisfy
\[
\left(\langle\phi_i,z_j\rangle\right)_{i,j\in L}=I_5.
\]
This is verified directly from the sixty-four signed facets of each \(z_j\), including orientations. Pairing a coboundary with a cycle is zero; therefore the \(\phi_i\) induce five independent integral functionals on homology and split off the subgroup spanned by the five \(z_i\) as a primitive direct summand. The rank-five and torsion-free Morse upper bound in step 2 forces this subgroup to be all of \(\widetilde H_5(X;\mathbb Z)\). Thus the five explicit spheres form an integral basis, not merely a rational one.

**4. Exact symmetry, with signs.** The relabeling action sends \(M_i\) to \(M_{\sigma(i)}\). The stabilizer \(S_4\) permutes the six two-subsets of the complementary four-element set by an even permutation: a transposition of two labels swaps exactly two pairs of two-subsets. Hence the signed ordered join orientation is preserved, so \(\sigma z_i=z_{\sigma(i)}\). Complementation swaps endpoints on all six edges (six minus signs, net plus one) and acts on the six edge factors by three disjoint swaps (minus sign). Consequently \(c z_i=-z_i\). The verifier checks the stronger equality of integral simplicial chains for all \(120\) relabelings and all five cycles, as well as complementation. The displayed \(G\)-lattice follows.

## Verification
Run `python3 check_desargues_integral.py` using standard Python 3. The program reconstructs every graph vertex, inclusion edge, and independent face, replays the complete augmented matching, checks every directed Hasse incidence for acyclicity, verifies all sixty-four signed terms and integral boundaries of the five octahedral cycles, checks maximality of each detecting facet and the unimodular identity pairing matrix, and replays every chain-level symmetry identity. Its full deterministic output is recorded in `verification_output.txt`. The final line is `conclusion_H5_integral_S5_perm_5_times_C2_sign=True`.

## Relationship to prior work
Randić established the full 240-element automorphism group of the Desargues–Levi graph; that graph-symmetry determination does not compute any independence-complex homology. Freij developed general equivariant discrete Morse theory; that theory does not identify this graph's integral module. Tsukuda's general incidence-graph/Alexander-duality theorem produces a nonequivariant homotopy reduction, not the present primitive integral five-sphere basis. Kumar–Singh–Verma study the same bipartite Kneser graph in their edge-ideal graded-Betti-number setting, not the natural integral equivariant homology of its independence complex. Previously recorded exact homotopy results give \(X\simeq S^4\vee\bigvee^5S^5\). A separate earlier rational character classification identifies the five-point permutation character, twisted by the complement sign; the new result strengthens this to an explicit, **primitive integral** permutation lattice and geometric basis. Rationally isomorphic but integrally inequivalent lattices can have distinct reductions in characteristic five, so the earlier rational statement does not imply this result.

## Limitations
This theorem concerns only degree-five integral homology for the specified graph and natural group. It does not identify the degree-four integral representation, an integral equivariant homotopy splitting, or the quotient's integral cohomology. The finite matching and pairing are exhaustively checked in ordinary Python rather than deduced from a family-wide closed formula. Published-source searches and the inspected works did not reveal an equivalent integral basis, but this does not certify global publication priority. The historical first-public month of the 1979 graph-symmetry article is reported only as a month; no day is inferred from it.

## References
1. M. Randić, *Symmetry properties of graphs of interest in chemistry. II. Desargues–Levi graph*, International Journal of Quantum Chemistry 15 (1979), 663–682. DOI: 10.1002/qua.560150610 (first published June 1979; exact day not supplied; public online version dated 2004-10-19).
2. R. Freij, *Equivariant discrete Morse theory*, Discrete Mathematics 309 (2009), 3821–3829. DOI: 10.1016/j.disc.2008.10.029 (dated 2009-06-28).
3. S. Tsukuda, *Independence complexes and incidence graphs*, Contributions to Discrete Mathematics 12 (2017), 28–46. DOI: 10.55016/ojs/cdm.v12i1.62277.
4. A. Kumar, P. Singh and R. Verma, *Certain homological invariants of bipartite Kneser graphs*, arXiv:2105.06144v1 (2021).
5. *The Desargues independence complex is \(S^4\vee\bigvee^5S^5\)*, published mathematical research record (2026-10-11), identifier `published-finding corpus:2026/10/11/SCOPE-the-desargues-independence-complex-is-s-4-vee-bigvee-5-s-5--e9aae0fc2563`.
