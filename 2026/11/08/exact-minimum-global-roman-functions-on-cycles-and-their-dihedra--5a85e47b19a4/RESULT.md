# Exact minimum global Roman functions on cycles and their dihedral orbit counts

## Finding

For every labelled simple cycle \(C_n\), \(n\ge3\), the minimum weight and **all** weight-minimum global Roman dominating functions are given by the formulas and cyclic-gap classification below. In particular, for \(m\ge2\), the number of labelled minimum functions at length \(n=3m+2\) is \(n(m+3)/2\); modulo rotation and reflection, there are exactly \(2+\lfloor m/2\rfloor\) classes. These counts refine the classical numerical Roman-domination value and are not counts of all inclusion-minimal functions.

\[
\gamma_{gR}(C_n)=\begin{cases}n,&3\le n\le5,\\\lceil 2n/3\rceil,&n\ge6,\end{cases}
\]
\[
(N_n,O_n)=\begin{cases}
(1,1),&n=3,\\ (5,2),&n=4,\\(11,3),&n=5,\\
(3,1),&n=3m,\ m\ge2,\\
(n,1),&n=3m+1,\ m\ge2,\\
\left(n(m+3)/2,\ 2+\lfloor m/2\rfloor\right),&n=3m+2,\ m\ge2.
\end{cases}
\]

## Assumptions and scope

All graphs are finite simple undirected graphs. The cycle vertices are individually labelled \(v_i\) for \(i\in\mathbb Z/n\mathbb Z\); its edges join consecutive indices. A global Roman dominating function \(f:V\to\{0,1,2\}\) must label each zero vertex so that it sees a label \(2\) both in the graph and its complement. In the cycle this means that each zero vertex sees a label \(2\) at a cyclic neighbour, and **another** label \(2\) at a distinct vertex that is not a cyclic neighbour. The weight is \(\sum_v f(v)\). The integer \(N_n\) counts functions on the named vertex set; \(O_n\) counts the orbits of these functions under all \(2n\) dihedral automorphisms, including reflections. Statements for small cycles use the ordinary complement of the simple cycle, without loops.

## Proof

**Lower bound.** Let \(t,o,z\) count respectively vertices labelled \(2,1,0\). Every zero requires a cyclic neighbour labelled \(2\). Since a vertex of a cycle has only two neighbours, \(z\le2t\), hence \(n=t+o+z\le3t+o\). The weight \(w=2t+o\) therefore satisfies \(n\le w+t\le3w/2\), proving \(w\ge\lceil2n/3\rceil\) for every global Roman function. Equality is attained for all \(n\ge6\) by the explicit gap words constructed below; their global condition is checked at the end.

**Exhaustion by gaps.** Fix \(n\ge6\), set \(w=\lceil2n/3\rceil\), and use both \(n\le w+t\) and \(t\le\lfloor w/2\rfloor\). If \(n=3m\), these inequalities force \(t=m\), \(o=0\), \(z=2m=2t\). If \(n=3m+1\), they force \(t=m\), \(o=1\), \(z=2m=2t\). If \(n=3m+2\), there are only two possibilities: \((t,o,z)=(m+1,0,2m)\) or \((m,2,2m)\).

When \(z=2t\), every labelled \(2\) must have two distinct zero neighbours, and each zero must be adjacent to precisely one labelled \(2\). Thus the cyclic distance between successive twos is at least \(3\), each gap has a zero immediately after its first two and a zero immediately before its second, and every other intervening vertex must be a one. With respectively zero, one, or two ones, the gaps are all of distance \(3\), have one gap of distance \(4\), or have one distance-\(5\) gap or two distance-\(4\) gaps. This proves the three gap types with \(z=2t\).

For the remaining case \((t,o,z)=(m+1,0,2m)\), no one-labelled vertex occurs. Cyclic domination forces each gap between twos to be of distance at most \(3\). There are \(m+1\) gaps and their total distances add to \(3m+2=3(m+1)-1\), so exactly one gap has distance \(2\) and the others distance \(3\) (distance \(1\) would cause a deficit of at least \(2\)). All configurations described above therefore exhaust every function at the lower-bound weight.

**Global feasibility.** For any of these words, each zero is cyclically adjacent to a two. In words containing only two twos (possible only at lengths \(6,7,8\)), each zero is adjacent to at most one two because all relevant gaps have distance at least \(3\); the other two is therefore a distinct non-neighbour. In words with at least three twos, every zero has at most two cyclic neighbours, so at least one two is a non-neighbour. Thus every candidate is globally Roman. In particular, all functions attaining the ordinary Roman lower bound at \(n\ge6\) satisfy the complementary requirement.

**Labelled enumeration.** The all-distance-\(3\) word has exactly three rotations. For \(n=3m+1\), the sole distance-\(4\) gap determines one of the \(n\) possible initial positions. For \(n=3m+2\), the distance-\(2\) family and the distance-\(5\) family contribute \(n\) functions each. The two-distance-\(4\) family has \(\binom m2\) choices of two special positions among \(m\) cyclic gaps; marking an initial two yields \(n\binom m2\) descriptions, and each resulting labelled word is described exactly \(m\) times, giving \(n(m-1)/2\). Hence \(N_n=n+n+n(m-1)/2=n(m+3)/2\) in this residue class.

**Dihedral orbits.** Cyclic shifts and reversal act on the cyclic list of inter-two gap lengths. A unique exceptional gap is one orbit for each family with one such gap. The two-distance-\(4\) family is classified under these actions by the smaller circular separation \(s\) between its two special gaps, with \(1\le s\le\lfloor m/2\rfloor\). Each \(s\) occurs and two different \(s\) cannot be dihedrally equivalent. This gives exactly \(\lfloor m/2\rfloor\) additional orbits and proves \(O_n=2+\lfloor m/2\rfloor\).

**Small cycles.** For \(C_3\), the complement has no edges, so no zero is permitted; all ones is the unique optimum. For \(C_4\), the complement consists of two edges. An admissible zero requires two distinct twos, one at each of its two corresponding neighbourhoods. Consequently no weight below \(4\) is possible; at weight \(4\), all ones and the four configurations with an adjacent two-pair and two zeros are exactly the possibilities, yielding two dihedral orbits. For \(C_5\), the complement is again a five-cycle. A function of weight at most \(4\) would have two twos and no ones (a single two cannot satisfy both global conditions for a zero). If the two twos are adjacent, the unique vertex not adjacent to either is undominated; if they are nonadjacent, the vertex adjacent to both has no two in the complement. Thus weight \(5\) is necessary. At weight \(5\), the all-one function is feasible, as are precisely the five adjacent-two-pair placements with a one at the sole other undominated vertex and the five nonadjacent-two-pair placements with a one at their shared cyclic neighbour. Every other placement fails at least one required zero condition. The two ten-function types are separate five-element dihedral orbits, and all ones is a third orbit.

## Verification

The standalone `artifacts/verify.py` checks the global predicate directly on every ternary word for each length \(3\le n\le12\), determines the actual minimum, counts labelled minimizers and dihedral orbits, then compares with the closed formulas. It also constructs all cyclic-gap patterns for \(6\le n\le80\), checks each is globally admissible with the predicted weight, and verifies the exact labelled and dihedral counts. Run with `python3 artifacts/verify.py` after extracting this file. The script has no nonstandard Python dependencies. The unrestricted statements follow from the proof, not from finite enumeration.

## Relationship to prior work

Reddy, Das, Kare and Reddy (2026) formulate global Roman domination and establish algorithms and complexity classifications for several graph classes, not the present cycle minimizer enumeration. The ordinary Roman domination value on cycles is classical; the numerical lower bound is not presented here as novel. Abu-Khzam, Fernau and Mann study pointwise-minimal Roman functions and give counts for paths, which differ both in the type of minimality and in the global complement condition. Shi and Koh give graph-general counting algorithms for minimum ordinary Roman functions; an algorithm for arbitrary graphs does not state the present cyclic structural and dihedral classification. Related older algorithmic treatments may contain equivalent specializations; historical priority is provisional.

## Limitations

This classification concerns only simple labelled cycles, minimum *weight* global Roman functions, and the natural dihedral action. It does not enumerate higher-weight functions, general unicyclic graphs, or generic global Roman solutions on arbitrary graphs. The proof and computation provide same-author verification; independent mathematical validation and exhaustive bibliographic priority review have not been performed.

## References

- S. B. Reddy, A. K. Das, A. S. Kare and I. V. Reddy, *On the complexity of global Roman domination problem in graphs* (first public preprint January 14, 2026), arXiv:2601.09167, https://arxiv.org/abs/2601.09167 .
- F. N. Abu-Khzam, H. Fernau and K. Mann, *Roman Census: Enumerating and Counting Roman Dominating Functions on Graph Classes* (first public preprint August 10, 2022), arXiv:2208.05261, https://arxiv.org/abs/2208.05261 .
- Z. Shi and K. M. Koh, *Counting the Number of Minimum Roman Dominating Functions of a Graph* (2014), arXiv:1403.1019, https://arxiv.org/abs/1403.1019 .
- S. Panda and A. Goyal, *Hardness results of global roman domination in graphs* (2023), Discrete Applied Mathematics, DOI:10.1016/j.dam.2023.08.020 .
