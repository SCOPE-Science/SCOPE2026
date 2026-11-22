# A seven-cycle collapse of the conjugation quotient of the proper-subgroup complex of \(S_4\)

## Finding
Let \(G=S_4\) and \(L(G)=\{H:1<H<G\}\) be the poset of proper nontrivial subgroups under inclusion. The group \(G\) acts on the geometric realization of the strict-chain order complex by simultaneous conjugation. Then
\[|\Delta L(S_4)|/S_4\simeq S^1.\]
More precisely, the quotient has a finite regular CW decomposition with nine vertices, fifteen edges and six two-cells, and eight explicit elementary cellular collapses leave one seven-edge cycle. The homotopy equivalence is not a claim of homeomorphism.

## Assumptions and scope
A simplex is a strictly increasing chain \(H_0<\cdots<H_d\) of nonidentity proper subgroups. Two chains are identified only if one *single* permutation conjugates every member of the first chain to the corresponding member of the second. In particular, separate conjugacy of each subgroup does not define the quotient. As subgroup orders strictly increase along each chain, a chain stabilizer cannot permute its vertices: the resulting quotient is a regular CW complex with one cell per chain orbit and face maps obtained by deleting one chain member. Multiple cells can have the same endpoint orbit classes. Quotient here means the ordinary orbit space, not a homotopy or Borel quotient.

## Proof
Enumerate the 24 permutations of four letters, build their multiplication and inversion tables, and construct the entire subgroup set by repeatedly adjoining each group element to each previously known subgroup and closing under multiplication. This is exhaustive: every finite subgroup has a finite generating set, and induction over its generators reaches that subgroup. There are exactly 30 subgroups, including the trivial and whole groups, hence 28 elements of \(L(G)\). Its strict chains number 28 vertices, 63 edges, and 24 two-simplices; there are no longer chains.

Each group element induces a permutation of the 28 proper nontrivial subgroups. Choosing the lexicographically first simultaneously conjugate chain gives canonical orbit representatives. There are exactly nine vertex, fifteen edge, and six triangle orbits. The source code reconstructs the face maps from actual chain orbits; the signed boundaries satisfy \(\partial_1\partial_2=0\). The six two-cell boundary edge-index lists, in the reproducible lexicographic enumeration, are \((11,2,0),(11,6,3),(12,6,4),(12,7,4),(13,8,4),(14,6,5)\). Distinct edges with identical endpoint-orbit pairs remain distinguished.

The attached certificate gives the elementary collapse pairs as \((d,u,v)\), with \(d\) the dimension of the upper cell, \(u\) its index and \(v\) the lower face index. Six triangle–edge pairs are removed first, followed by two edge–vertex pairs. The verifier checks at *each* deletion that the lower face belongs to exactly one surviving upper cell, and that no higher-dimensional cell contains the upper cell. The remaining seven vertices each have valence two, and the residual one-skeleton is connected. Hence the residual CW complex is a seven-edge circle, proving the stated homotopy equivalence by elementary collapse.

## Verification
Place `verify.py` and `certificate.json` in the same directory and execute `python3 verify.py certificate.json` using Python 3 (standard library only). The verifier independently regenerates all permutation tables, subgroup closures, strict subgroup flags, simultaneous conjugacy orbits and face maps; checks the cellular boundary composition, all eight free-face conditions and the connected seven-cycle remainder. The observed terminal output is `S4_SUBGROUP_CONJUGACY_QUOTIENT_SEVEN_CYCLE_OK 30 [9, 15, 6]`. The algorithm enumerates **all** relevant finite objects; no extrapolation from samples or floating-point computation is involved.

## Relationship to prior work
Ramras, *Connectivity of the coset poset and the subgroup poset of a group* (2002), analyzes the proper subgroup poset **before** conjugation, including connectivity criteria; neither its subgroup-poset section nor its coset-poset results identify this geometric conjugation quotient. A later published calculation, *Conjugation quotients of the proper-subgroup complexes of \(A_5\) and \(S_5\)* (2026), derives an orbit circle for \(A_5\) and an orbit two-sphere for \(S_5\), but its methods and reported finite data concern those two other groups, not the \(S_4\) quotient or the eight-pair collapse here. The smaller \(S_3\) proper-subgroup orbit complex consists of two isolated conjugacy classes; the \(S_4\) case is the first of these natural symmetric-group examples with a nontrivial orbit loop and genuine two-cell orbit attachments. No general formula for all \(S_n\) is asserted.

## Limitations
This is one natural finite-group homotopy classification, not a family theorem. It does not determine the complete equivariant homotopy type, the nonequivariant homology representation, or all subgroup quotients. A previously unindexed equivalent calculation could exist. The reproducible certificate verifies the finite topology but does not by itself establish publication priority. No independent mathematical audit has been performed.

## References
1. Daniel A. Ramras, *Connectivity of the coset poset and the subgroup poset of a group*, arXiv:math/0210001 (first public October 1, 2002); https://arxiv.org/abs/math/0210001 ; full text https://pi.math.cornell.edu/~kbrown/ramras.pdf .
2. *Conjugation quotients of the proper-subgroup complexes of \(A_5\) and \(S_5\)* (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/17/SCOPE-conjugation-quotients-of-the-proper-subgroup-complexes-of-a-5-an--5700bda30292 .
