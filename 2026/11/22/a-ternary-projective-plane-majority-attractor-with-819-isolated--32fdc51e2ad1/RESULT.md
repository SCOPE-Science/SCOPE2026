# A ternary projective-plane majority attractor with 819 isolated geometric phases

## Finding

Let \(G\) be the 26-vertex point--line incidence (Levi) graph of \(\mathrm{PG}(2,3)\). At each synchronous update, a vertex becomes one precisely when **at least three of its four neighbors** are one; otherwise it becomes zero. Thus this is open-neighbor strict majority, with ties resolved in favor of zero. Let \(F\) be the resulting map on all \(2^{26}=67{,}108{,}864\) labelled binary configurations.

The exact temporal identity is
\[
F^6=F^4,\qquad F^5\ne F^3.
\]
Consequently every configuration first reaches a fixed point or a primitive two-cycle after at most four updates, and four is attained. There are exactly **821 fixed configurations** and **336,610 primitive temporal two-cycle orbits**. The basin of an orbit means all initial labelled configurations eventually entering that *particular temporal orbit*, including its recurrent configurations.

| Attractor | Basin size per orbit | Number of orbits |
| --- | ---: | ---: |
| Fixed point | 1 | 819 |
| Fixed point | 24,649 | 1 |
| Fixed point | 52,070,656 | 1 |
| Primitive two-cycle | 2 | 334,971 |
| Primitive two-cycle | 314 | 819 |
| Primitive two-cycle | 14,432 | 819 |
| Primitive two-cycle | 2,265,824 | 1 |

In particular, all 819 nonconstant fixed configurations have **singleton basins**, and all but two of the 821 recurrent phase symbols have unique ancestors. The exact numbers of initial configurations whose *first* periodic entrance occurs at times \(t=0,1,2,3,4\) are respectively
\[
674{,}041,\quad1{,}266{,}408,\quad35{,}098{,}947,\quad15{,}610{,}140,\quad14{,}459{,}328.
\]
These totals add to \(2^{26}\). Global bit-complementation conjugates the stated threshold-three map to the tie-favoring-one threshold-two map, so its temporal and basin census is identical.

## Assumptions and scope

There are thirteen points \(\mathcal P\) and thirteen lines \(\mathcal L\), each line incident with four points and each point on four lines. No vertex has a self-loop; the two graph shores represent distinct point and line vertices. Coordinates in the first verifier are nonzero vectors of \(\mathbb F_3^3\), normalized so the first nonzero coordinate is one, with a line \([a:b:c]\) incident to a point \([x:y:z]\) precisely when \(ax+by+cz=0\) modulo three. The second verifier uses the nine affine points, four points at infinity, twelve affine lines and one line at infinity.

Describe a binary configuration by its **zero sets** \((S,T)\), with \(S\subseteq\mathcal P\), \(T\subseteq\mathcal L\). For \(S\subseteq\mathcal P\) define \(B_{\mathcal P}(S)\) to be all lines meeting \(S\) in at least two points; for \(T\subseteq\mathcal L\) define \(B_{\mathcal L}(T)\) to be all points incident with at least two lines of \(T\). Because each vertex has four neighbors, the strict-majority update in zero-set notation is exactly
\[
F(S,T)=(B_{\mathcal L}(T),B_{\mathcal P}(S)).
\]
Temporal rotation is identified when counting cycles; spatial symmetries and color complementation are not identified. All counts are exact integers, not sampled estimates.

## Proof

**1. Geometric phase classification.** Put \(P=B_{\mathcal L}\circ B_{\mathcal P}\) on point subsets and \(Q=B_{\mathcal P}\circ B_{\mathcal L}\) on line subsets. The finite incidence certificate checks **every** one of the \(2^{13}=8192\) possible subsets, using the explicit thirteen four-point lines. It establishes
\[
P^3=P^2,\qquad Q^3=Q^2,
\]
and identifies the same thirteen-element-geometry class distribution for \(\mathrm{Fix}(P)\) and \(\mathrm{Fix}(Q)\). Their common size is
\[
 r=1+1+234+468+117=821.
\]
The fixed point subsets of \(P\) are precisely (i) the empty set; (ii) all thirteen points; (iii) noncollinear triples; (iv) a collinear triple plus one point off its line; and (v) an entire four-point line plus one point off that line. The counts of these last three classes are
\[
\binom{13}{3}-13\binom{4}{3}=234,\qquad 13\binom{4}{3}\cdot9=468,\qquad13\cdot9=117.
\]
The five classes are pairwise disjoint. They can each be seen to be stable under \(P\) geometrically: three sides of a noncollinear triangle recover its three corners; a three-point line and the three connectors from an external point recover that four-point set; a four-point line and the four connectors recover that five-point set. The claim that **no further subset is stable** is a finite lemma verified exhaustively by the two standalone programs: the first compares every computed stable mask with the five explicitly generated geometric classes, and the second reconstructs the incidence structure in affine coordinates and repeats the classification without using the first incidence matrix. No assertion about an infinite family follows merely from these finite checks.

**2. Exact four-update projection and exceptional fibers.** The same \(8192\)-input finite certificate proves \(\operatorname{im}(P^2)=\mathrm{Fix}(P)\) and the dual statement for \(Q\). For the map \(E=P^2\), its 821 image fibers have sizes
\[
\left\{7216,157,\underbrace{1,\ldots,1}_{819\text{ entries}}\right\}.
\]
Specifically, the all-thirteen-point zero set has fiber size 7216, the empty zero set has fiber size 157, and every other fixed subset has fiber size one. The dual map \(Q^2\) has the identical classification. Because \(F^2=(P,Q)\), it follows exactly, on every 26-bit state, that \(F^6=F^4\). The periodic state space is \(\mathrm{Fix}(P)\times\mathrm{Fix}(Q)\), containing \(821^2=674{,}041\) configurations.

**3. The recurrent swap and all basins.** The map \(B_{\mathcal P}\) restricts to a bijection from \(\mathrm{Fix}(P)\) to \(\mathrm{Fix}(Q)\), inverse to \(B_{\mathcal L}\), by the equations defining these fixed sets. Hence recurrent states may be written uniquely \((S,B_{\mathcal P}(U))\), where \(S,U\in\mathrm{Fix}(P)\). Under this coordinate system,
\[
F(S,B_{\mathcal P}(U))=(U,B_{\mathcal P}(S)),
\]
so \(F\) **interchanges two 821-valued symbols**. There are therefore \(821\) fixed points and \(\binom{821}{2}=336{,}610\) two-cycle orbits. Put \(w(S)=|E^{-1}(S)|\). The single-orbit basin of fixed symbol \(S\) has size \(w(S)^2\), and the two-cycle of distinct symbols \(S,U\) has basin size \(2w(S)w(U)\). The incidence verification checks that fiber sizes are preserved under the point-to-line phase bijection. Inserting 819 unit fibers and exceptional fibers 157 and 7216 gives every row of the stated basin table. As a checksum, the weighted sum of all rows equals \(67{,}108{,}864\).

**4. Sharp periodic-entry cutoff.** For each shore, the number of thirteen-bit subsets first entering its recurrent phase set after \(t=0,1,2,3,4\) successive alternating incidence updates is, respectively,
\[
821,\quad572,\quad4693,\quad1170,\quad936.
\]
Both checkers verify these **exhaustive** counts. The entry time of a pair is the maximum of its two shore entry times, since the shore transformations alternate with each update and the recurrent sets are invariant under these maps. Squaring cumulative shore counts and taking successive differences proves the five 26-bit first-entrance totals. Since 936 shore inputs need four updates, the global bound four is attained, which also establishes \(F^5\ne F^3\).

## Verification

Run `python3 verify_primary.py` and `python3 verify_independent.py` using the two embedded Python source files. Neither uses external packages. The primary program constructs a symmetric 13-by-13 incidence matrix from normalized homogeneous \(\mathbb F_3\) coordinates, iterates all 8192 shore masks, checks the full geometric pattern classification, the six-versus-four iterate identity, phase fibers, orbit-basin classes, and first-entry counts. The independent program constructs the plane from affine lines and points at infinity, uses separate point-to-line and line-to-point maps, verifies all pairwise projective incidence axioms, and independently computes the complete phase, basin and entry-time census. Both scripts terminate with assertions unless every claimed count agrees. The dynamic factorization proves completeness for all \(2^{26}\) states without claiming a 67-million-state brute-force replay.

## Relationship to prior work

Goles and Olivos established the general eventual-period-two theorem for symmetric Boolean threshold networks in 1980. Kuhlman, Mortveit, Murrugarra and Kumar's *Bifurcations in Boolean Networks*, first publicly posted on 2011-08-15, treats general synchronous threshold and bi-threshold attractors, with tree and cycle constructions; its inspected main results and graph-family sections do not enumerate this projective-plane incidence graph. The previously published *A two-step majority projection and exact attraction basins on the Heawood graph* gives a **different** 14-vertex Fano-plane result, with 58 phases and a two-update cutoff. It provides a closely related method but neither implies the 821 geometric classes nor the exceptional 157/7216 fibers, four-update cutoff, or basin table of the ternary plane. *Complete stopping configurations and erasure-failure spectrum of the order-three projective plane* classifies stopping sets for a binary incidence parity-check matrix, not this twofold secant threshold map, temporal orbits or attraction fibers. Nagy's *Partitioning the projective plane to two incidence-rich parts* proves existence and structural bounds for internal partitions; it does not enumerate threshold dynamics or their basins. The standard geometry and general threshold period theorem are not claimed as new.

## Limitations

This is an exact result only for the labelled incidence graph of \(\mathrm{PG}(2,3)\) and the stated threshold-three rule (or its globally complemented threshold-two conjugate). It is not a formula for arbitrary projective planes, tie-retaining majority or asynchronous updates. The finite phase-classification lemma depends on the supplied exhaustive 8192-subset certificate; the factorization, not a direct full-state enumeration, converts that lemma into all 26-vertex counts. Distinct formulations or unindexed prior computations may exist. No independent external mathematical audit has been performed.

## References

1. E. Goles and J. Olivos, *Periodic behaviour of generalized threshold functions*, Discrete Mathematics 30 (1980), 187--189, https://doi.org/10.1016/0012-365X(80)90121-1 .
2. C. J. Kuhlman, H. S. Mortveit, D. Murrugarra and V. S. A. Kumar, *Bifurcations in Boolean Networks*, arXiv:1108.2974, first posted 2011-08-15, https://arxiv.org/abs/1108.2974 .
3. *A two-step majority projection and exact attraction basins on the Heawood graph*, published full text, https://github.com/published-finding corpus/2026/blob/main/2026/11/2/SCOPE-a-two-step-majority-projection-and-exact-attraction-basins-on-th--8cd2964a9d93/RESULT.md .
4. *Complete stopping configurations and erasure-failure spectrum of the order-three projective plane*, published full text, https://github.com/published-finding corpus/2026/blob/main/2026/10/12/SCOPE-complete-stopping-configurations-and-erasure-failure-spectrum-of--fc9b95f1c3c6/RESULT.md .
5. Z. L. Nagy, *Partitioning the projective plane to two incidence-rich parts*, arXiv:2403.13734, first posted 2024-03-20, https://arxiv.org/abs/2403.13734 .
