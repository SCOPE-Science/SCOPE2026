# All dihedral-subgroup orbit spaces of the pentagonal wheel forest complex are four-sphere wedges

## Finding
Let \(W=K_1*C_5\) be the six-vertex graph formed by joining a central hub to all five vertices of a pentagon. Let \(K=\mathcal F(W)\) be the independence complex of its cycle matroid: its vertices are the ten graph edges and its simplices are the nonempty acyclic edge subsets, together with the empty face. The natural dihedral action permutes pentagon vertices and fixes the hub.

**Theorem.** For every subgroup \(H\le D_5\), the *ordinary geometric* quotient (not a homotopy quotient) satisfies
\[
|K|/H\simeq\bigvee^{30/|H|}S^4.
\]
All eight subgroup quotients are simply connected, have torsion-free integral homology, and have no positive-degree homology outside degree four. The complete conjugacy-type classification is:

| \(H\) | Number of subgroups | Homotopy type |
|---|---:|---|
| \(1\) | 1 | \(\bigvee^{30}S^4\) |
| Reflection \(C_2\) | 5 | \(\bigvee^{15}S^4\) |
| Rotation \(C_5\) | 1 | \(\bigvee^{6}S^4\) |
| Full \(D_5\) | 1 | \(\bigvee^{3}S^4\) |

The labeled-complex homotopy and integral symmetry representation were known previously; the conclusion being established here is the **ordinary quotient homotopy** for the nontrivial subgroup actions.

## Assumptions and scope
Use graph vertices \(0,1,2,3,4,\infty\), with indices modulo five. The ten edges are the five rim edges \(e_i=\{i,i+1\}\) and the five spokes \(s_i=\{i,\infty\}\). Thus the vertex set of \(K\) is \(\{e_i,s_i:0\le i<5\}\), and \(K\) is pure four-dimensional, since a spanning tree of \(W\) has five edges. The group \(D_5=\langle r,s\mid r^5=s^2=1,\ srs=r^{-1}\rangle\) permutes these edges by induced graph automorphisms. Throughout, a quotient means the topological quotient of the realization by the specified finite action. The assertion covers exactly subgroups of this \(D_5\), not arbitrary automorphisms or different wheel sizes.

## Proof
**1. Labeled complex.** The independence complex of a matroid is shellable, hence a wedge of top-dimensional spheres. In particular, Kook's coned-graph theorem and its edge-rooted forest count give \(|K|\simeq\bigvee^{30}S^4\); this labeled statement is prior work. It implies \(\pi_1(|K|)=1\).

**2. Fundamental groups of quotients.** The five spokes together are a spanning tree, hence a four-simplex of \(K\). Every element of \(D_5\) fixes its barycenter, and so each subgroup element has a fixed point in \(|K|\). The orbit-space fundamental-group theorem of Armstrong, applied to the simply connected simplicial complex and finite group \(H\), identifies \(\pi_1(|K|/H)\) with \(H\) modulo the normal closure of elements having fixed points. Consequently
\[\pi_1(|K|/H)=1\quad\text{for every }H\le D_5.\]

**3. Integral orbit cellular chains.** Pass to barycentric subdivision, indexed by strict flags \(\sigma_0\subsetneq\dots\subsetneq\sigma_d\) of nonempty forest faces. Every group element preserving a flag must preserve every face individually, because their cardinalities differ. Thus the action is without cell inversions, and its flag-orbit cells form an integral cellular chain model of the *ordinary* quotient. For a canonical orbit of an oriented flag, its boundary is the alternating sum of canonical face-orbit flags. This description also accounts for any identifications between distinct boundary faces; it is not the homotopy-orbit chain complex. The supplied standard-library verifier enumerates all \(461\) nonempty forest faces (counts by size \(10,45,115,170,121\)), all strictly increasing flags and their \(H\)-orbits; it checks the induced edge permutations preserve forests and are closed under composition, and verifies all consecutive integer boundaries compose to zero.

The resulting quotient-cell counts from degrees zero through four are
\[
\begin{array}{c|rrrrr}
 H&C_0&C_1&C_2&C_3&C_4\\\hline
 C_5&93&1358&4992&6624&2904\\
 C_2&244&3432&12504&16560&7260\\
 D_5&60&716&2520&3312&1452
\end{array}
\]
where \(C_d\) denotes the **rank** of a free cellular chain group, not its homology. The integer elimination uses only pivots of unit value \(\pm1\), performs elementary chain cancellations, and ends with zero differentials and free generators of ranks
\[
\begin{array}{c|rrrrr}
H&H_0&H_1&H_2&H_3&H_4\\\hline
C_5&1&0&0&0&6\\
C_2&1&0&0&0&15\\
D_5&1&0&0&0&3.
\end{array}
\]
These are exact *integral* results: a unit cancellation is unimodular and cannot lose torsion. In the order of boundary degrees one to four, the independent verified cancellation totals are \((92,1266,3726,2898)\), \((243,3189,9315,7245)\), and \((59,657,1863,1449)\), respectively. The full quotient-chain calculation is finite and exhausts the specified complexes, rather than extrapolating from sampled instances.

**4. Homotopy conclusion.** Each quotient is a connected four-dimensional CW complex with trivial \(\pi_1\), with \(H_2=H_3=0\) and \(H_4\) free of the stated rank. Applying the Hurewicz theorem successively, each quotient is three-connected and its fourth Hurewicz map is an isomorphism. A wedge of four-spheres representing a basis of \(H_4\) induces an isomorphism in integral homology; the simply connected homology form of Whitehead's theorem makes this map a homotopy equivalence. The identity subgroup has the already known labeled type and completes the classification.

## Verification
Run \(\texttt{python3 verify_wheel_quotients.py}\) with Python 3.9 or newer; it uses only the standard library. The exact program regenerates the graph and all faces; checks the subgroup permutations and invariance of the simplicial complex; enumerates barycentric flag-orbits; builds signed integer boundaries and checks \(\partial^2=0\) at every applicable degree; applies only unimodular unit-pivot cancellations; asserts the surviving ranks and Euler characteristics; and prints \(\texttt{VERIFY_OK}\). In a distinct consistency calculation, it enumerates the thirty edge-rooted forests indexing the known integral top-homology basis and checks that all nonidentity dihedral elements have zero fixed basis vectors and that the group has exactly three orbits on this index set. This recovers the known rational invariant ranks \(30/|H|\), but is **not** substituted for the integral quotient-chain computation.

## Relationship to prior work
Kook's coned-graph theorem explicitly supplies the prior labeled wedge of thirty four-spheres and the automorphism action (up to the relevant orientation sign) on edge-rooted forests. The reflection and rotation permutations of the five rim vertices are even, and the thirty rooted forests form three free \(D_5\)-orbits. Thus an integral regular-module character and its subgroup-invariant ranks were already accessible from Kook. They do *not* automatically determine integral homology or attaching maps of an ordinary geometric orbit space with fixed points. The classification here supplies the separate quotient computation, with simple connectivity and complete homotopy types for every subgroup.

The matroid shellability account by Ardila, Castillo and Samper supplies general independence-complex context, while Moci and Pezzoli address homology representations under automorphism groups rather than these geometric orbit spaces. The orbit fundamental-group step uses Armstrong. Comparison against these texts and targeted research records did not identify a stronger theorem explicitly classifying these quotients; that negative search is not proof of publication priority.

## Limitations
The calculation is restricted to the pentagonal wheel and its particular dihedral action, and makes no assertion for larger wheels or other automorphism groups. The chain computation is an exhaustive certificate for the finite objects specified; it does not generalize them by numerical interpolation. The relationship-to-prior assessment depends on inspected literature and searchable records; an equivalent unindexed quotient theorem could exist. The general supporting results of Kook, matroid shellability, and Armstrong are prerequisites, not independent discoveries here. Independent mathematical audit is not asserted.

## References
- W. Kook, “The homology of the cycle matroid of a coned graph,” *European Journal of Combinatorics* 28 (2007), 734–741. DOI: https://doi.org/10.1016/j.ejc.2006.01.001. First available online March 9, 2006. The original full-text paper was inspected, especially its coned-cycle examples and equivariant edge-rooted-forest theorem.
- M. A. Armstrong, “On the fundamental group of an orbit space,” *Proceedings of the Cambridge Philosophical Society* 61 (1965), 639–646. DOI: https://doi.org/10.1017/S0305004100038974.
- F. Ardila, F. Castillo and J. A. Samper, “The topology of the external activity complex of a matroid,” *Electronic Journal of Combinatorics* 23(3) (2016), P3.8. https://www.combinatorics.org/ojs/index.php/eljc/article/download/v23i3p8/pdf/.
- L. Moci and P. Pezzoli, “Representations of automorphism groups on the homology of matroids,” arXiv:2001.03760 (2020). https://arxiv.org/pdf/2001.03760.
