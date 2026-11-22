# Dihedral classification of minimum global Roman functions on cycles

## Finding: exact symmetry classes

Let \(C_n\) be the simple cycle on named vertices \(v_i\), indexed by \(\mathbb Z/n\mathbb Z\), and let \(n\ge3\). A *global Roman dominating function* assigns \(f(v_i)\in\{0,1,2\}\) such that each zero has a neighbor labeled two **both** in \(C_n\) and in its simple complement. Let \(\mathcal M_n\) be the functions of minimum total weight \(w(f)=\sum_i f(v_i)\). Let \(D_n\) act on \(\mathcal M_n\) by rotations and reflections.

**Theorem (complete optimizer shapes and symmetry orbits).** Every optimizer is, up to dihedral symmetry, one of the cyclic gap configurations below. In particular its number of dihedral orbits is

\[
\boxed{|\mathcal M_n/D_n|=\begin{cases}
1,&n=3,\\2,&n=4,\\3,&n=5,\\
1,&n=3m\ (m\ge2),\\
1,&n=3m+1\ (m\ge2),\\
2+\lfloor m/2\rfloor,&n=3m+2\ (m\ge2).
\end{cases}}
\]

For \(n\ge6\), read the twos cyclically and write \(d_1,\dots,d_t\) for the **edge distances** between consecutive twos. The following list is exhaustive and disjoint:

1. \(n=3m\): all \(m\) gaps have length three, with gap word \(2,0,0\).
2. \(n=3m+1\): exactly one gap has length four, word \(2,0,1,0\); all other gaps have length three.
3. \(n=3m+2\): one of (a) \(m+1\) twos, with one length-two gap \(2,0\), all remaining length three; (b) \(m\) twos, with one length-five gap \(2,0,1,1,0\), all remaining length three; (c) \(m\) twos, with exactly two length-four gaps, all remaining length three. In case (c) the smaller cyclic number of gap positions separating the exceptional gaps is \(s\in\{1,\dots,\lfloor m/2\rfloor\}\); these are precisely the distinct dihedral types.

The small cases \(C_3,C_4,C_5\) have respectively the following types: all ones; all ones or a pair of adjacent twos with zeros elsewhere; and all ones, or adjacent twos with one remaining necessary one, or nonadjacent twos with one remaining necessary one. In \(C_4\) and \(C_5\), each nontrivial type is a single dihedral orbit.

**Priority boundary.** The minimum ordinary Roman domination weight \(\lceil2n/3\rceil\), and **all three labelled minimum counts for ordinary cycles**, including \((3m+2)(m+3)/2\), are earlier published results of Deepak G., Alwardi and Indiramma (2021), Theorem 2.4(ii)–(iv). They are not novelty claims here. The theorem above concerns the complete *dihedral classification* and its gap-structure proof, including why ordinary minimizers satisfy the additional complementary constraint at \(n\ge6\).

## Proof

Let \(t,o,z\) respectively denote the numbers of twos, ones and zeros. As every zero has a cyclic two-neighbor and each two has only two cyclic neighbors, \(z\le2t\). Hence \(n=t+o+z\le3t+o\). If \(w=2t+o\), then \(n\le w+t\le3w/2\); so every global Roman function has \(w\ge\lceil2n/3\rceil\). The gap patterns in the statement meet this weight for every \(n\ge6\), as verified below.

Fix \(n\ge6\) and \(w=\lceil2n/3\rceil\). The inequalities \(n-w\le t\le\lfloor w/2\rfloor\) determine the possible defender counts. If \(n=3m\), then \((t,o,z)=(m,0,2m)\). If \(n=3m+1\), then \((t,o,z)=(m,1,2m)\). If \(n=3m+2\), the only possibilities are \((m+1,0,2m)\) and \((m,2,2m)\). These alternatives exhaust all possible label counts at minimum weight.

Whenever \(z=2t\), equality in the neighbor bound means that each two has two distinct zero-neighbors and no zero is adjacent to two different twos. Thus consecutive twos are separated by at least three edges. The first and last internal vertices of each gap are zeros, while any extra internal vertices have no two-neighbor and must be ones. There can therefore be only length-three gaps and, using at most two ones, at most one length-four gap, one length-five gap, or two length-four gaps. Total length distinguishes the cases exactly as above.

For \((t,o,z)=(m+1,0,2m)\), every vertex not labeled two is a zero with a two-neighbor. Every inter-two gap has length at most three. As \(\sum_i d_i=3m+2=3(m+1)-1\), relative to \(m+1\) gaps of length three the total deficit is one; hence precisely one gap has length two and the remainder have length three. In particular, no distance-one gap can occur.

All the displayed words are globally feasible. They are Roman on the cycle by the local gap description. If there are at least three twos, a zero has at most two cyclic neighbors, so at least one two is a non-neighbor and supplies complement defense. If there are exactly two twos, the only such cases here are \(n=6,7,8\), and their gaps have distance at least three; each zero sees at most one two cyclically, so its other two-defender is a non-neighbor. Therefore ordinary cycle minima of length \(n\ge6\) **coincide as a set** with global cycle minima, because every ordinary minimum must satisfy the same inequalities and exhaustive gaps, and every listed word is globally feasible.

The dihedral group acts on the cyclic list of gap lengths by cyclic permutation and reversal. The all-three list and each unique-exception list form one orbit. In the two-length-four family, the two identical exceptional positions lie in a cyclic list of \(m\) gaps. Two such choices are dihedrally equivalent if and only if their shorter cyclic separation is equal. Thus \(s=1,2,\ldots,\lfloor m/2\rfloor\) labels all orbits, with no identifications between the three different defender/gap families. This proves the formula for \(n\ge6\).

For the remaining small cycles, the complement of \(C_3\) has no edges, so zeros are impossible and all ones gives the unique minimum of weight three. For \(C_4\), a zero must see separate twos across the cycle and complement neighborhoods. No weight below four is feasible; all ones and the four placements of adjacent twos with two zeros are the five weight-four functions, in two orbits. For \(C_5\), any configuration of weight at most four would need exactly two twos and no ones. If the twos are adjacent, the opposite vertex has no cyclic two-neighbor; if nonadjacent, their common neighbor has no complementary two-neighbor. Thus the minimum is five. It is achieved by all ones and by the five rotations of each of two two-defender types, with the necessary single one at the unique vertex not otherwise defended. These form three dihedral orbits. The theorem follows.

## Previously known labelled counts (not a new result)

For context, the ordinary-cycle result of Deepak G., Alwardi and Indiramma (2021), Theorem 2.4(ii)–(iv), combined with the equality of ordinary and global minimum sets proved above, yields for \(n\ge6\)

\[
|\mathcal M_n|=\begin{cases}
3,&n=3m,\\n,&n=3m+1,\\n(m+3)/2,&n=3m+2.
\end{cases}
\]

The small global cases have \(|\mathcal M_3|=1\), \(|\mathcal M_4|=5\), and \(|\mathcal M_5|=11\). These formulas are included to distinguish labelled counts from the symmetry quotient, not to reassert priority for the earlier numbers.

## Verification and limitations

Fresh direct enumeration of every ternary labeling for \(3\le n\le12\) checks both the cycle and complement requirements, optimizes weight, and computes the dihedral orbits from all rotations and reflections. The resulting triples \((\gamma_{gR},|\mathcal M_n|,|\mathcal M_n/D_n|)\) match the theorem in every tested case. At \(n\ge6\), the independently enumerated ordinary and global minimum sets coincide. These finite calculations test small orders; the all-length assertions are proved by the inequalities and gap argument above.

The contribution is limited to simple cycles, their minimum-weight configurations, and the natural dihedral action. Neither the ordinary Roman domination number, the 2021 labelled counts, nor the general idea of counting Roman labelings is claimed as new. Standard orbit-counting on two exceptional gap positions is elementary, but gives a complete exact symmetry classification for this natural extremal configuration family. Unindexed equivalent dihedral classifications may exist; bibliographic searches cannot certify absolute priority. No assertion is made about higher weights or other graph families.

## References

1. Deepak G., A. Alwardi and M. H. Indiramma, *Roman Domination Polynomial of Cycles*, International Journal of Mathematics and Combinatorics 2021(3), 86–97, Theorem 2.4(ii)–(iv). https://fs.unm.edu/IJMC/Roman_Domination_Polynomial_of_Cycles.pdf
2. S. B. Reddy, A. K. Das, A. S. Kare and I. V. Reddy, *On the complexity of global Roman domination problem in graphs* (2026), arXiv:2601.09167. https://arxiv.org/abs/2601.09167
3. F. N. Abu-Khzam, H. Fernau and K. Mann, *Roman Census: Enumerating and Counting Roman Dominating Functions on Graph Classes* (2022), arXiv:2208.05261. https://arxiv.org/abs/2208.05261
4. Z. Shi and K. M. Koh, *Counting the Number of Minimum Roman Dominating Functions of a Graph* (2014), arXiv:1403.1019. https://arxiv.org/abs/1403.1019
5. S. Panda and A. Goyal, *Hardness results of global roman domination in graphs* (2023), Discrete Applied Mathematics, DOI:10.1016/j.dam.2023.08.020. Access to the complete article was unavailable during this comparison; no negative conclusion is drawn from its absence.
