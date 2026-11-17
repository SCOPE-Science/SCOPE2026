# Integral homotopy and affine homology character of the eleven-vertex Paley tournament neighborhood complex

## Finding
Let \(T\) be the Paley tournament on \(\mathbb Z/11\mathbb Z\) in which \(u\to v\) exactly when \(v-u\in Q=\{1,3,4,5,9\}\). Let \(X=\overrightarrow{\mathcal N}(T)\) be the out-neighborhood complex, whose simplices are nonempty subsets of common out-neighborhoods. Then
\[
X\simeq\bigvee^{21}S^2.
\]
The affine group \(G=\{x\mapsto ax+b:a\in Q,\ b\in\mathbb F_{11}\}\cong C_{11}\rtimes C_5\) acts simplicially on \(X\). The complete rational homology character \(\chi\) of this action in degree two satisfies
\[
\chi(1)=21,\qquad \chi(x\mapsto x+b)=-1\ (b\ne0),\qquad
\chi(x\mapsto ax+b)=1\ (a\ne1).
\]
Equivalently, \(H_2(X;\mathbb Q)\cong\mathbb Q\oplus W^{\oplus2}\) as \(\mathbb Q[G]\)-modules, where \(W=\mathbb Q(\zeta_{11})\) is the ten-dimensional rational representation on which translations multiply by powers of \(\zeta_{11}\), and multipliers act by the corresponding cyclotomic automorphisms. In particular, \(\dim H_2(X;\mathbb Q)^G=1\).

## Assumptions and scope
All faces are ordinary *unordered* simplices; the arrow direction is used only to determine common out-neighbors. The tournament has no loops. Since \(-1\) is not a square modulo eleven, every pair of distinct vertices has exactly one orientation. The five-element maximal faces are the eleven translates \(v+Q\), for \(v\in\mathbb F_{11}\). The result concerns the specified eleven-vertex tournament and its natural affine subgroup, not all tournaments, not the directed flag complex, and not an integral equivariant splitting.

## Proof
**Face structure.** The quadratic-residue difference set \(Q\) has pairwise translate-intersection size two: \(|(u+Q)\cap(v+Q)|=2\) for distinct \(u,v\). This is also checked directly in the accompanying verifier, for all fifty-five block pairs. Thus the blocks form the symmetric \(2\)-\((11,5,2)\) biplane. Every edge is contained in two blocks; every face of cardinality at least three belongs to at most one block. Consequently, the simplicial face numbers in dimensions zero through four are \((11,55,110,55,11)\).

**A complete acyclic discrete-Morse matching.** Encode each nonempty face by its eleven-bit incidence mask. Initially mark all 242 faces unpaired. Process vertices in the order \(0,1,\ldots,10\); at each vertex \(v\), inspect the currently unpaired faces in increasing order of cardinality and then of bit mask. Pair a face \(A\) not containing \(v\) with \(A\cup\{v\}\) precisely when both remain unpaired, removing both from further consideration. This deterministic rule creates 110 incident pairs. The remaining faces comprise exactly one vertex and 21 triangles. The standalone verifier constructs the complete face Hasse diagram (715 incidences), reverses the oriented arcs corresponding to pairs, and exhaustively checks acyclicity by Kahn elimination (all 242 vertices removed). Running the same method with the vertex order reversed gives the identical critical-cell counts and a second complete acyclicity check. This finite computation is small and exhaustively specified, rather than a sampling argument.

Forman's acyclic matching theorem gives a CW model with exactly one zero-cell, no one-cells, and 21 two-cells (and no higher cells). Every attaching map of a two-cell into the one-point one-skeleton is null, so that CW model is \(\bigvee^{21}S^2\). This proves the integral homotopy equivalence; it does not rely on interpreting finite-field ranks as integral homology. Independent mod-two simplicial boundary ranks \((10,45,44,11)\) are a cross-check.

**Homology character.** The affine transformations preserve the out-neighborhood blocks because \(aQ=Q\) for \(a\in Q\). The reduced Lefschetz formula applies to the action on \(X\). A nontrivial translation has a single orbit of length eleven on vertices and hence fixes no nonempty face (all faces contain at most five vertices). Its reduced Lefschetz number is \(-1\). Each affine element with \(a\ne1\) is conjugate by translation to multiplication by \(a\), has one fixed vertex and two orbits of length five. Exactly one of the two five-element orbits is a facet (the out-neighborhood of the fixed vertex). Thus the signed chain traces occur only in degrees zero and four, with contributions \(+1\) and \(+1\); the reduced Lefschetz number is \(1+1-1=1\). The identity has reduced Euler characteristic \(21\). Because reduced homology is concentrated in even degree two, these Lefschetz numbers are exactly the homology character values.

To identify the rational representation, let \(W=\mathbb Q(\zeta_{11})\) with translations acting by cyclotomic multiplication and the complement \(C_5\) acting by Galois automorphisms. Its character is ten at the identity, minus one on nonidentity translations, and zero on elements outside the translation subgroup. Hence \(\mathbf1\oplus2W\) has exactly the character calculated above. Maschke's theorem and rational character theory identify the representations. Averaging the character over the 55 group elements yields one invariant dimension.

## Verification
Run `python3 verify.py` using Python 3's standard library. The program reconstructs all 2048 subsets in two independent ways, verifies all design-block intersections, constructs and checks two complete Morse matchings, calculates independent mod-two boundary ranks, and evaluates signed fixed-simplex Lefschetz traces for all 55 affine symmetries. The unedited output is included as `verification_output.txt`. The final line is `ALL_CHECKS_PASS`. The executable program, not the output log alone, is the finite certificate.

## Relationship to prior work
Dochtermann and Singh (first publicly available August 24, 2021) define the directed out-neighborhood complex in Definition 4.1, relate it to the directed edge Hom complex in Theorem 4.3, and give general vanishing and construction results (Theorem 4.12 and Proposition 5.1). Their Section 5 tabulates five-vertex tournament neighborhood homology; it does not give this eleven-vertex integral homotopy type or affine homology representation. The group-based block configuration is the classical \(2\)-\((11,5,2)\) symmetric biplane and is not itself new. The tournaplex and directed flag-complex constructions of Govc, Levi and Smith are different face rules. Related published neighborhood-complex results for Steiner \(2\)-design incidence graphs assume the pair-incidence parameter one, whereas this biplane has parameter two. Graph-like neighborhood results requiring edge-disjoint four-cycles do not apply because each incidence edge belongs to multiple four-cycles. These reductions and stronger-covering comparisons distinguish the present claim from superficially similar results.

## Limitations
The result is for the fixed Paley tournament of order eleven and the natural order-55 affine group. It does not assert equivariant homotopy equivalence to an action on a wedge of spheres or classify the integral \(\mathbb Z[G]\)-module. The novelty comparison is based on the inspected primary text and relevant indexed research, not a proof of universal absence of an equivalent computation. Related biplane surface-model literature was accessible only at the abstract level and is a residual literature risk.

## References
1. A. Dochtermann and A. Singh, *Homomorphism complexes, reconfiguration, and homotopy for directed graphs*, arXiv:2108.10948 (v1 posted 2021-08-24), especially Definitions 4.1, Theorem 4.3, Theorem 4.12 and Section 5. https://arxiv.org/abs/2108.10948
2. D. Govc, R. Levi and J. P. Smith, *Complexes of tournaments, directionality filtrations and persistent homology*, Journal of Applied and Computational Topology **5** (2021), 313–337, doi:10.1007/s41468-021-00068-0. https://link.springer.com/article/10.1007/s41468-021-00068-0
3. *Modelling biplanes on surfaces*, European Journal of Combinatorics **25** (2004), 899–909, doi:10.1016/j.ejc.2003.05.004 (abstract consulted only; no claim of comprehensive full-text exclusion).
