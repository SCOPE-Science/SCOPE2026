# Factorial rigidity of saturated optimal burning schedules on sunlet graphs

## Finding

For every integer \(k\geq3\), set \(n=(k-1)^2+1\) and let \(S_n=C_n\circ K_1\) be the sunlet with cycle vertices \(u_i\) and pendant vertices \(v_i\), for \(i\in\mathbb Z/n\mathbb Z\), and edges \(u_iu_{i+1}\) and \(u_iv_i\). An ordered *strict burning sequence* \((x_1,\ldots,x_k)\) ignites one not-yet-burned vertex at each round, with fire spreading across one graph edge per subsequent round.

**Theorem.** The number of ordered optimal strict \(k\)-round burning sequences of the labelled graph \(S_n\) is precisely

\[
2n(k-1)!.
\]

Every optimum is characterized by an ordered cyclic partition of the \(n\) pendant indices into disjoint labelled intervals of lengths
\[
2k-3,\ 2k-5,\ \ldots,\ 3,\ 1,\ 1,
\]
corresponding respectively to ignition rounds \(1,2,\ldots,k\). In rounds \(1,\ldots,k-2\), ignite the cycle vertex at the center of the respective interval. At round \(k-1\), ignite either its center cycle vertex or its pendant, and at round \(k\), ignite the pendant of its singleton block.

Define the *single-round replacement graph* \(\mathcal B_n\) on these ordered optimal burning sequences by joining two sequences if they differ in exactly one ignition vertex at the same time coordinate. Then
\[
\mathcal B_n\cong n(k-1)!\,K_2.
\]
In particular, the sole permissible one-ignition change is the cycle/pendant switch in round \(k-1\); no other ignition can be moved by a single optimum-preserving replacement. The full dihedral automorphism group acts freely on these schedules, giving exactly \((k-1)!\) symmetry orbits.

## Assumptions and scope

The cycle \(C_n\) has \(n\geq5\) vertices. The usual deterministic burning process is used: vertex \(x_t\) may be selected at time \(t\) only if it is still unburned then; it first burns at time \(t\); prior fires spread one edge per elapsed round. Thus a sequence is legal precisely when \(d(x_s,x_t)\geq t-s\) for all \(s<t\), and successful after \(k\) rounds precisely when
\[
V(S_n)=\bigcup_{t=1}^{k} B_{k-t}(x_t).
\]
Vertices are labelled, ignition order matters, and no identification by graph automorphisms is made in the \(2n(k-1)!\) count. The graph \(\mathcal B_n\) uses replacements at a fixed round, not commuting or reordering round labels. No statement about non-saturated \(n\), other corona graphs, or random ignition processes is part of the new classification.

## Proof

**1. Sharp pendant-coverage capacity.** Let \(r=k-t\). An ignition at \(u_i\) can burn by time \(k\) only the pendants \(v_j\) with cycle distance \(d_{C_n}(i,j)\leq r-1\), so covers at most \(2r-1\) pendants when \(r\geq1\), and none for \(r=0\). An ignition at \(v_i\) with \(r\geq1\) covers at most \(\max\{1,2r-3\}\) pendants, and with \(r=0\) covers exactly its own pendant. Thus any \(k\)-round sequence can cover no more than
\[
\sum_{t=1}^{k-1}(2(k-t)-1)+1=(k-1)^2+1
\]
pendants (the \(r=1\) bound holds for either center or pendant). At \(n=(k-1)^2+1\) each local bound must be attained and no pendant coverage can overlap. Consequently the first \(k-2\) ignitions are cycle vertices, the last is a pendant, the penultimate is the cycle vertex or pendant at one singleton index, and the pendant sets burnt by the respective sources are disjoint consecutive cyclic intervals of the stated lengths. They must cover the full cycle of indices. The longest interval has length \(2k-3<n\), so its center is unique. This also proves no sequence shorter than \(k\) succeeds, since the analogous capacity for \(k-1\) rounds is \((k-2)^2+1<n\).

**2. Every such cyclic tiling actually burns the whole graph.** Fix any partition into the prescribed labelled intervals. For \(t\leq k-2\), let \(h_t=k-t-1\), and ignite its center \(u_{a_t}\). At \(t=k-1\) ignite \(u_{a_{k-1}}\) or \(v_{a_{k-1}}\), and at \(t=k\) ignite \(v_{a_k}\). By construction every pendant burns. Every core \(u_j\) whose pendant lies in any interval other than the final singleton also burns, as the same source reaches that core one round earlier (or, at the penultimate singleton, a pendant source reaches its own parent in one round). The final singleton core \(u_{a_k}\) lies next to at least one *non-singleton* interval, since there are only two singleton intervals and \(k\geq3\). The source of that neighboring non-singleton interval has final core-radius \(h_t+1\), one larger than its pendant-radius \(h_t\), so it burns \(u_{a_k}\), too.

**3. Ignitions are legal when scheduled.** Two distinct cyclic intervals are disjoint, hence their centers at rounds \(s<t\leq k-1\) are at cycle distance at least \(h_s+h_t+1\), where \(h_{k-1}=0\). This is strictly greater than \(t-s\) (for \(t\leq k-2\), the difference is at least \(2(k-t)-1\); for \(t=k-1\), it is one). Replacing the penultimate core source by its pendant only increases distances to preceding core sources. For the last pendant source, its pendant index is outside all preceding pendant intervals, so for any preceding core source \(s\) its distance is at least \(h_s+2=k-s+1>k-s\); the penultimate source is at least two edges away from the final pendant. Thus \(d(x_s,x_t)>t-s\) for every \(s<t\), and the sequence is strict.

**4. Counting.** The \(k\) intervals have distinct time labels, even though the last two happen to have equal length one. Fix the starting index of the first interval (\(n\) choices) and cyclically order the other \(k-1\) labelled intervals (\((k-1)!\) choices). The tiling then uniquely fixes each center and the final pendant; the penultimate ignition admits the two independent cycle/pendant choices. This gives \(2n(k-1)!\) and no duplicates.

**5. Replacement graph.** In any optimum, the sets of pendant indices reached by the \(k\) sources are a disjoint partition, and each source attains its maximum. If all but the round-\(t\) ignition are fixed, their leaf coverage leaves exactly the same interval of labels for round \(t\). For \(t\leq k-2\), only its original cycle center produces this full interval; at \(t=k\), the source must remain the same pendant; and at \(t=k-1\), the two choices are its cycle center and pendant. Thus each schedule has exactly one replacement neighbor, its penultimate switch, so \(\mathcal B_n\) is the stated disjoint matching.

**6. Dihedral symmetry.** All \(k\geq3\) pendant-index interval centers are distinct. A nonidentity rotation fixes no cycle index and a reflection fixes at most two; therefore no nonidentity dihedral automorphism fixes a labelled ordered schedule. Each orbit has size \(2n\), giving \(2n(k-1)!/(2n)=(k-1)!\) orbits.

## Verification

The standalone program `verify_burning.cpp` reconstructs distances by independent graph breadth-first searches and enumerates **all** legal ordered \(k\)-tuples, including alternatives outside the classified type, for the saturated cases \((n,k)=(5,3),(10,4),(17,5)\). It obtains respectively \(20,120,816\) successful ordered sequences, agreeing with the theorem. The independent `verify_tiling.py` generates the canonical interval tilings and verifies full graph burning, strict ignition legality and uniqueness for \(k=3,4,5,6,7\), giving counts \(20,120,816,6240,53280\); it explicitly reconstructs the single-round replacement graph for \(k=3,4,5\), obtaining \(10,60,408\) disjoint edges.

Run in a directory containing both files:

```
g++ -std=c++17 -O3 -Wall -Wextra verify_burning.cpp -o verify_burning
./verify_burning
python3 verify_tiling.py
```

The all-\(k\) proof is the capacity-and-tiling argument, not an inference from finite tests.

## Relationship to prior work

Bonato, Janssen and Roshanbin introduce the standard ordered burning model in their publicly available 2015 preprint [1]. Jenifer and Shanthi [2], Theorem 3.4, state the **scalar** sunlet burning number (with their two cases equivalent to \(1+\lceil\sqrt{n-1}\rceil\) for \(n\geq3\)). That scalar result is not claimed here as original. Their fully inspected sunlet treatment does not enumerate optimal ordered ignition sequences, classify their interval tilings, or establish exchange components. Previously reported exact reconfiguration results for bare cycles involve different vertex sets and cannot imply the pendant-constrained placement and single-source replacement structure above.

## Limitations

The theorem is about saturation lengths \(n=(k-1)^2+1\) and precisely ordered, strict, minimum-length schedules. It gives no enumeration for other sunlet lengths and no claim that every distinct future paper/database has been exhaustively checked. A possible unindexed earlier enumeration or unpublished computation remains a priority risk. Independent scholarly verification has not been performed.

## References

1. A. Bonato, J. Janssen and E. Roshanbin, *How to burn a graph*, original arXiv submission 23 July 2015, arXiv:1507.06524, https://arxiv.org/abs/1507.06524 .
2. M. S. Mary Jenifer and A. S. Shanthi, *Burning number of path and cycle related graphs*, Journal of Discrete Mathematical Sciences and Cryptography 29 (2026), 1347–1354, DOI:10.47974/JDMSC-2582, https://tarupublications.com/journals/jdmsc/volume/29/issue/3/burning-number-of-path-and-cycle-related-graphs .
