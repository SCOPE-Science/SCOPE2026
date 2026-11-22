# Dihedral fixed-point and orbit homotopy spectra of prime-divisible partition graphs

## Finding
For every prime \(p\ge5\), the first nontrivial proper-part complex of the \(p\)-divisible partition lattice on \(3p\) cyclically labeled points admits a complete classification of geometric fixed spaces and ordinary quotient homotopy types under **all** dihedral subgroups.

Put \(U=\binom{3p}{p}\), \(B=\binom{2p}{p}\), \(M=U(B-3)/3\), and \(u=\binom{(3p-1)/2}{(p-1)/2}\). These are integers, since \(U B/6\) counts unordered triple partitions. Let \(H\le D_{3p}\) and set \(h=|H\cap C_{3p}|\in\{1,3,p,3p\}\) and \(f=1\) if \(H\) contains a reflection, \(f=0\) otherwise. Thus \(|H|=h(1+f)\).

The geometric fixed space \(X_p^H\) has the following **actual graph** description; the classification is not merely one of Euler characteristics:

| \(h\) | \(f\) | Geometric fixed graph \(X_p^H\) |
|---|---|---|
| \(1\) | \(0\) | Connected graph, homotopy \(\bigvee^{M+1}S^1\) |
| \(1\) | \(1\) | \(u\) disjoint copies of the star \(K_{1,2^{p-1}}\) |
| \(3\) | \(0\) | \(3^{p-1}\) isolated points |
| \(3\) | \(1\) | \(3^{(p-1)/2}\) isolated points |
| \(p\) | \(0\) | The star \(K_{1,3}\) |
| \(p\) | \(1\) | One closed interval |
| \(3p\) | \(0\) | A point |
| \(3p\) | \(1\) | A point |

The ordinary geometric quotient is always a connected graph and, for every such \(H\),
\[
X_p/H\simeq\bigvee^{\beta_p(h,f)}S^1,
\qquad
\beta_p(h,f)=1+\frac{M-(h-1)-2\mathbf 1_{3\mid h}(3^{p-1}-1)-fhu}{h(1+f)}.
\]
The formula is a nonnegative integer because it counts the first Betti number of a connected finite graph. In particular, at \(p=5\), the full rotational quotient has first Betti number \(16606\) and the full dihedral quotient has first Betti number \(8293\).

## Assumptions and scope
The ground set is \(\mathbb Z/(3p)\), and \(p\) is a prime at least five. A \(p\)-divisible partition means every block size is a multiple of \(p\); the lower and upper lattice bounds are removed before forming the order complex. The remaining rank-one vertices are partitions into three blocks of size \(p\); rank-two vertices are partitions into blocks of sizes \(p\) and \(2p\). An edge encodes refinement. The dihedral group \(D_{3p}=\langle r,s\mid r^{3p}=s^2=1,srs=r^{-1}\rangle\) acts by \(r(i)=i+1\) and \(s(i)=-i\) modulo \(3p\). A geometric fixed point is a point fixed by every element of the subgroup, not an orbit class.

## Proof
**Graph counts and connectedness.** Each upper vertex is identified by its unique block of size \(p\); hence there are \(U\) such vertices. Choosing an unordered partition into three blocks of size \(p\) gives \(T=U B/6\) lower vertices. Each lower vertex has degree three, so the edge count is \(E=3T\). Given any two \(p\)-subsets \(A,B\), the complement of their union contains at least \(p\) labels. Choose a \(p\)-set \(C\) there: \(A\) and \(C\) appear together among the three blocks of a lower vertex, as do \(B\) and \(C\). Hence the bipartite graph is connected. Its first Betti number is \(E-(U+T)+1=U(B-3)/3+1=M+1\).

**Fixed graph principle.** Every permutation of labels preserves partition rank. Therefore no graph edge can be reversed by the group. A point in the interior of an edge fixed by a subgroup must have both endpoints fixed. Consequently the geometric fixed space is precisely the graph on fixed partition vertices and fixed incidences, with no extra mid-edge points. Quotients also remain connected finite graphs, because the original graph is connected and rank preservation prevents edge inversions.

**Rotations of order \(p\) and \(3p\).** The order-\(p\) subgroup \(\langle r^3\rangle\) has three point-orbits, each of size \(p\). A fixed \(p\)-subset is exactly one orbit, so there are three fixed upper vertices. A fixed triple partition cannot have its three blocks cyclically permuted by an element of order \(p\ge5\), hence every block must be individually invariant; the unique lower partition comprises the three orbits. Thus the fixed graph is \(K_{1,3}\). A reflection permutes the three leaf blocks by an involution with exactly one fixed block, so the corresponding dihedral subgroup fixes exactly one edge. The full rotation subgroup has no fixed upper vertex, since its unique point-orbit has size \(3p\); its only fixed lower partition has the three residue classes modulo three, which are cyclically permuted by a one-step rotation. This same vertex is fixed under all reflections, and hence all larger subgroups that contain the full rotation subgroup have singleton fixed spaces.

**Rotations of order three.** The subgroup \(\langle r^p\rangle\) has \(p\) point-orbits of size three. No \(p\)-subset is invariant because \(3\nmid p\). An invariant triple partition must have its blocks permuted cyclically by \(r^p\) (none can remain individually invariant). Assigning to each three-point orbit one of the three phase positions in a chosen first block gives \(3^p\) assignments, modulo simultaneous cyclic relabeling of the three blocks. There are precisely \(3^{p-1}\) fixed lower vertices, all isolated. When a reflection is adjoined, its induced action reverses the three phases and pairs the \(p\) rotation-orbits, leaving exactly one rotation-orbit fixed. After the common phase normalization, each of the remaining \((p-1)/2\) pairs contributes one free ternary phase, while the fixed orbit has a uniquely determined compatible phase. Thus the dihedral subgroup fixes exactly \(3^{(p-1)/2}\) isolated vertices.

**Single reflections.** Every reflection of an odd \(3p\)-gon fixes one label and swaps \((3p-1)/2\) pairs. An invariant \(p\)-set contains the fixed label and \((p-1)/2\) swapped pairs, giving \(u\) fixed upper vertices. Any invariant partition into three odd-sized blocks must have one fixed block and a pair of exchanged blocks: three individually fixed odd blocks would require three fixed ground labels, which do not exist. The fixed block must be one of the \(u\) invariant \(p\)-sets. In its complement, the reflection has \(p\) swapped pairs; selecting one element from each pair and identifying the two exchanged blocks leaves exactly \(2^{p-1}\) lower partitions incident to that fixed upper vertex. Each such lower partition has exactly one invariant \(p\)-block, so its vertex has degree one in the fixed graph, giving \(u\) disconnected copies of \(K_{1,2^{p-1}}\).

**Every subgroup and every orbit quotient.** Since \(3p\) has exactly divisors \(1,3,p,3p\), and a dihedral subgroup is its rotation intersection together with no reflection or one reflection coset, the above cases exhaust all subgroups. To count quotient edges and vertices, Burnside applies to each rank and to incidences. Define \(F(g)=E^g-(U^g+T^g)\), using superscripts for fixed-cell counts. The preceding classification gives \(F(1)=M\); \(F(g)=-3^{p-1}\) for the two rotations of order three; \(F(g)=-1\) for every other nonidentity rotation; and \(F(g)=-u\) for every reflection. In any subgroup with rotational part order \(h\), there are \(h-1\) nonidentity rotations, with two of order three precisely when \(3\mid h\), as well as \(fh\) reflections. Therefore \(E_H-V_H=[M-(h-1)-2\mathbf1_{3\mid h}(3^{p-1}-1)-fhu]/[h(1+f)]\). Connectedness yields \(\beta_1(X_p/H)=1+E_H-V_H\), and a connected graph has the specified circle-wedge homotopy type.

## Verification
The accompanying standalone Python program `verify.py` exhaustively enumerates all \(p=5\) partitions and checks fixed vertices and incidences for generators of each of the eight subgroup classes. It verifies \(U=3003\), \(T=126126\), \(E=378378\), \(M=249249\), and \(u=21\). In the order \((h,f)=(1,0),(1,1),(3,0),(3,1),(5,0),(5,1),(15,0),(15,1)\), the verified quotient first Betti numbers are \(249250,124615,83030,41505,49850,24915,16606,8293\). The finite computation is a test of the symbolic all-prime proof, not its substitute.

## Relationship to prior work
Hanlon's 1981 *The fixed-point partition lattices* studies unrestricted partition lattices fixed by permutations; its cycle-and-block description underlies, but does not determine, these size-restricted geometric fixed graphs or all dihedral orbit graphs. Wachs's 1996 *A Basis for the Homology of the d-Divisible Partition Lattice* establishes shellability, top homology, and a full symmetric-group homology action for divisible partition lattices, hence covers important background nonequivariant homology and can recover rational quotient ranks; it does not classify the geometric fixed graphs or integral orbit homotopy types here. Woodroofe's 2009 convex-ear theorem further describes the underlying poset's decomposition. Arone and Brantner study strict fixed points of the **unrestricted** partition complex, not the divisible subposet. Prior orbit-homology information alone cannot recover the disconnected reflection fixed graphs or their exact component structures. The classification is new relative to the inspected claims, with the residual coverage risks stated below.

## Limitations
The theorem concerns only the three-block-level proper parts on exactly \(3p\) labels for primes \(p\ge5\); \(p=3\) is explicitly excluded because rotation stabilizers permit extra fixed three-block partitions, and no claim is made for composite divisibility parameters or larger multiples of \(p\). Individual steps use elementary partition enumeration, and some isolated counts may be obtainable from unrestricted fixed-partition formulas. No claim of publication priority or independent validation is made. A fully unindexed equivalent result, or a specialized unpublished computation for divisible-partition fixed points, remains possible.

## References
1. P. Hanlon, *The fixed-point partition lattices*, Pacific Journal of Mathematics **96** (1981), 319–341. DOI: 10.2140/pjm.1981.96.319. Full text: https://msp.org/pjm/1981/96-2/pjm-v96-n2-p04-s.pdf
2. M. L. Wachs, *A Basis for the Homology of the d-Divisible Partition Lattice*, Advances in Mathematics **117** (1996), 294–318. DOI: 10.1006/aima.1996.0014. Full text: https://www.researchgate.net/publication/248774286_A_Basis_for_the_Homology_of_the_d-Divisible_Partition_Lattice
3. R. Woodroofe, *Cubical Convex Ear Decompositions*, Electronic Journal of Combinatorics **16** (2009), #R17. DOI: 10.37236/83. Public release: 2009-06-10.
4. G. Arone and L. Brantner, *The Action of Young Subgroups on the Partition Complex*, arXiv:1801.01491 (2018). https://arxiv.org/abs/1801.01491
