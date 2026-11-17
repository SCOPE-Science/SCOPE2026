# The \(S_5\times C_2\) characters of Desargues independence homology

## Finding
Let \(D\) be the Desargues graph, realized as the bipartite inclusion graph between the ten two-element subsets and ten three-element subsets of \(\{1,2,3,4,5\}\). Let \(X=\operatorname{Ind}(D)\) be its ordinary independence complex. The full graph automorphism group is \(G=S_5\times C_2\), with \(S_5\) permuting the five labels and the central involution \(c\) complementing subsets.

The reduced integral homology is free, with \(\widetilde H_4(X;\mathbb Z)\cong\mathbb Z\), \(\widetilde H_5(X;\mathbb Z)\cong\mathbb Z^5\), and all other reduced groups zero. The **new classification** is the rational automorphism representation:
\[
\widetilde H_4(X;\mathbb Q)\cong\operatorname{sgn}_{S_5}\boxtimes\operatorname{sgn}_{C_2},\qquad
\widetilde H_5(X;\mathbb Q)\cong\mathbb Q[\{1,2,3,4,5\}]\boxtimes\operatorname{sgn}_{C_2}.
\]
Here the five-dimensional factor is the ordinary permutation representation of \(S_5\) on its five letters. In particular, for \(p\in S_5\) and \(e\in\{0,1\}\),
\[
\operatorname{tr}(pc^e\mid\widetilde H_4)=(-1)^e\operatorname{sgn}(p),\qquad
\operatorname{tr}(pc^e\mid\widetilde H_5)=(-1)^e\#\operatorname{Fix}(p).
\]
Neither positive-degree homology group has a nonzero \(G\)-invariant rational class. The \(S_5\)-fixed part of degree five, before imposing complementation, is one-dimensional. The known nonequivariant sphere-wedge calculation is not claimed as new.

## Assumptions and scope
Write \(P_2\) and \(P_3\) for the two- and three-element subsets of \(\{1,2,3,4,5\}\). The graph has vertex set \(P_2\sqcup P_3\), with an edge exactly when a two-set is contained in a three-set. All faces of \(X\) are independent vertex sets, including the empty face as the augmentation generator for reduced chains. Orient each nonempty face by the increasing order in the list of all two-subsets followed by all three-subsets, with lexicographic order within either block. This is the graph also denoted \(H(5,2)\) or \(\operatorname{GP}(10,3)\), the bipartite double cover of the Petersen graph.

The asserted representation is **rational** in degree five: a classification of the integral \(\mathbb Z[G]\)-lattice in that degree is not asserted. The integral degree-four action is necessarily the displayed sign character because the underlying group is \(\mathbb Z\).

## Proof
**1. Integral homology and the two possible degrees.** An exact independent-set enumeration gives \(6,211\) nonempty simplices and face vector
\[
(20,160,660,1510,1924,1320,480,115,20,2).
\]
Apply a staged element matching in the displayed vertex order: at stage \(v\), pair every still-unmatched face not containing \(v\) with its one-vertex enlargement when the latter is also unmatched. Include the empty face. Exactly \(3,103\) pairs arise, leaving one critical four-face and five critical five-faces. On all \(30,380\) Hasse covers, orient matched covers upward (from smaller to larger face) and unmatched covers downward. A complete topological sort visits all \(6,212\) augmented faces, proving this matching acyclic. Signed integral gradient-path elimination gives all five differential coefficients from critical dimension five to critical dimension four equal to zero. The reduced Morse complex therefore has one generator in degree four, five in degree five, zero differential and no other critical groups. It follows over \(\mathbb Z\) that the stated homology groups are free with exactly these ranks. This matching is not required to preserve the automorphism action.

**2. Lefschetz character for every automorphism.** For any \(g\in G\), the reduced signed simplicial Lefschetz sum is
\[
L(g)=\sum_{\substack{\sigma\in X\\\sigma\ne\varnothing,\,g\sigma=\sigma}}(-1)^{|\sigma|-1}\operatorname{sgn}(g|_\sigma)-1.
\]
Every invariant face is a union of vertex orbits. Delete any orbit containing an internal graph edge and form the incompatibility graph on the remaining orbits. If its independence polynomial is \(I_g(t)\), then the preceding sum is exactly \(-I_g(-1)\): an invariant independent face made from \(r\) orbits contributes \((-1)^{r-1}\), including the augmented empty contribution \(-1\). Exhaustive orbit enumeration for each of the 240 distinct automorphisms yields
\[
L(pc^e)=(-1)^e\bigl(\operatorname{sgn}(p)-\#\operatorname{Fix}(p)\bigr).
\]
A completely separate calculation enumerates every fixed oriented simplex and checks its signed contribution; it agrees for every automorphism. The complete fourteen-class table, with group class sizes, appears in `character_table.csv`.

**3. Separate the two homology characters.** The integral Morse complex proves that \(H_4\) is one-dimensional and \(H_5\) five-dimensional over \(\mathbb Q\). Consequently their characters satisfy \(L=\chi_4-\chi_5\). Every one-dimensional rational character of \(S_5\times C_2\) is one of the four products of the trivial or sign characters of the factors. Let \(\eta=\operatorname{sgn}_{S_5}\boxtimes\operatorname{sgn}_{C_2}\). Exact averaging of the fourteen-class Lefschetz values gives \(\langle L,\eta\rangle_G=1\). Since \(\chi_5=\chi_4-L\) is an actual character, its multiplicity of \(\eta\) is nonnegative. Thus \(\langle\chi_4,\eta\rangle_G\ge1\), forcing \(\chi_4=\eta\), as both are one-dimensional. Substitution gives \(\chi_5(pc^e)=(-1)^e\#\operatorname{Fix}(p)\), which is precisely the signed five-point permutation module. Rational characters determine finite-group \(\mathbb Q\)-representations here because these two modules are explicitly defined over \(\mathbb Q\) and the corresponding complex representations are semisimple; equality of their characters gives isomorphism over \(\mathbb Q\).

## Verification
Run `python3 verify.py` (Python 3 standard library only). It independently enumerates all faces; constructs the augmented Morse matching; checks the complete Hasse digraph is acyclic; computes the signed integral Morse differential; builds all 240 natural symmetries; checks by constraint backtracking that there are exactly 240 graph automorphisms; computes the Lefschetz character both from vertex-orbit incompatibility polynomials and from signed fixed simplices; and verifies the character-positivity argument. The included `verification_output.txt` is the output of executing the enclosed program. The computations are finite and exhaustive; the proof does not infer a homotopy theorem from sampling, and no claim is made about general \(H(n,k)\) graphs.

## Relationship to prior work
Engström's 2005 work provides graph-independence-complex methods, and Barmak's 2010 work proves suspension and connectivity results for triangle-free graph independence complexes. These general tools do not calculate the automorphism character for \(H(5,2)\). Mütze and Su's 2015 bipartite-Kneser paper describes the graph family but does not classify its independence-complex homology representations. Tsukuda's incidence-graph/Alexander-dual theorem gives a general homotopy reduction for bipartite graphs (Corollary 5.3); it does not present this fourteen-class calculation or the action of the bipartition-swapping involution on the two homology degrees.

Two later published computations determine the **nonequivariant** homotopy type \(X\simeq S^4\vee\bigvee^5S^5\), and their full result statements, not merely their titles, were compared. Their homotopy classification entails the ranks of the two homology groups but cannot distinguish the signed permutation representation from other modules of the same dimensions. The present result supplies this missing equivariant information, rather than repeating the existing sphere-wedge theorem.

## Limitations
Only the integral homology groups and the rational automorphism characters are determined; the degree-five integral group-ring lattice, equivariant homotopy type, ring structure and a family-level formula for other bipartite Kneser graphs are not. A prior implicit deduction from a stronger, unindexed equivariant theory cannot be categorically excluded. The computation establishes mathematical identities but does not constitute an independent mathematical audit.

## References
1. A. Engström, *Complexes of Directed Trees and Independence Complexes*, arXiv:math/0508148, first public 2005-08-08.
2. J. A. Barmak, *Star clusters in independence complexes of graphs*, arXiv:1007.0418, first public 2010-07-02; Adv. Math. 241 (2013), 33–57.
3. T. Mütze and P. Su, *Bipartite Kneser graphs are Hamiltonian*, arXiv:1503.09175, first public 2015-03-31.
4. S. Tsukuda, *Independence complexes and incidence graphs*, Contributions to Discrete Mathematics 12 (2017), 28–46, DOI:10.55016/ojs/cdm.v12i1.62277.
5. *Independence complex of the Desargues graph is \(S^4\vee\bigvee^5S^5\)*, public research record, 2026-10-04, `https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-independence-complex-of-the-desargues-graph-is-s-4-vee-bigvee-5--f3b1cf10aadb`.
6. *The Desargues independence complex is \(S^4\vee\bigvee^5S^5\)*, public research record, 2026-10-11, `https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-the-desargues-independence-complex-is-s-4-vee-bigvee-5-s-5--e9aae0fc2563`.
