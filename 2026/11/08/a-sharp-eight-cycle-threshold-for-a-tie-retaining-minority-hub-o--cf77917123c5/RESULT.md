# A sharp eight-cycle threshold for a tie-retaining minority hub on wheels

## Finding

Let \(W_n=K_1\vee C_n\), for every integer \(n\ge3\). In a synchronous binary update, each rim vertex adopts the strict majority opinion among its three neighbors (its two rim neighbors and the hub). The hub adopts the minority opinion among its \(n\) rim neighbors and retains its own opinion if the rim vote is tied. Then an **initial configuration of least temporal period eight exists if and only if \(n\) is even and \(n\ge12\)**. The first such wheel is \(W_{12}\), on thirteen vertices; exactly \(288\) of its \(8192\) labeled binary configurations have least period eight, forming \(36\) distinct temporal orbits.

For every even \(n\ge12\), one explicit period-eight configuration has hub opinion \(1\) and a single consecutive cyclic block of \(n/2-4\) rim vertices in opinion \(1\), with all other rim opinions \(0\). Its hub's successive opinions are \(1,1,1,1,0,0,0,0\). The property concerns configurations periodic **from time zero**, not merely eventual attractors.

## Assumptions and scope

The wheel is simple and loopless, the vertices are labeled, and the update is simultaneous and deterministic. Write the hub state as \(h\in\{0,1\}\) and the rim states as \(r_i\in\{0,1\}\), with indices \(i\in\mathbb Z/n\mathbb Z\). The simultaneous rule is

\[
r_i'=\begin{cases}r_{i-1}\lor r_{i+1},&h=1,\\r_{i-1}\land r_{i+1},&h=0,\end{cases}
\]

and, writing \(s=\sum_i r_i\),

\[
h'=\begin{cases}1,&2s<n,\\h,&2s=n,\\0,&2s>n.\end{cases}
\]

The hub is the only anti-majoritarian vertex; all rim vertices have odd degree and therefore no ties. The hub's state-dependent tie rule is essential and is not a pure anti-threshold function of its open-neighborhood states when \(n\) is even.

## Proof

**Existence for every even \(n\ge12\).** Put \(a=n/2-4\), so \(a\ge2\). Start with \(h=1\) and a cyclic interval of exactly \(a\) consecutive ones on the rim. For a cyclic interval of \(b\) ones with \(2\le b\le n-4\), an update with \(h=1\) replaces that interval with the interval enlarged by one vertex at each end, increasing its length by two. For an interval of \(b\) ones with \(4\le b\le n-2\), an update with \(h=0\) removes one endpoint from each side, decreasing its length by two. Both facts follow directly from the displayed OR/AND formulas; no other rim sites change. These inequalities hold at every step in the following eight-step construction because \(a\ge2\) and \(a+8=n/2+4\le n-2\).

For each time \(t\) below, write the pair (hub state, consecutive-one-block length). The eight successive pairs, beginning at time zero, are

\[
(1,a),\ (1,a+2),\ (1,a+4),\ (1,a+6),\
(0,a+8),\ (0,a+6),\ (0,a+4),\ (0,a+2),
\]

and the next pair is \((1,a)\) with **exactly the original block position**, because the four endpoint enlargements are undone by the four endpoint removals. To check every hub update, observe that \(a+4=n/2\): the hub retains \(1\) at the first tie and \(0\) at the second tie, changes from \(1\) to \(0\) after the \(a+6\) state, and changes back after the \(a+2\) state. Thus the initial full state returns after eight updates. It does not return after four, since its hub state has changed. As a least period dividing eight can only be \(1,2,4,8\), the least period is exactly eight.

**Odd sizes cannot have period eight.** If \(n\) is odd, the hub never faces a tie. It therefore obeys a pure anti-threshold rule depending only on the open-neighborhood opinions, while the other vertices obey a pure threshold rule. Haslegrave and Cannings, *Majority dynamics with one nonconformist*, arXiv:1606.05496v1, Theorem 10, prove that every recurrent period on a finite loopless graph with exactly this pattern of threshold and anti-threshold updates is one of \(1,2,4,5,6,10\). Hence period eight is impossible at every odd \(n\). This theorem is invoked only for the case satisfying its precise hypotheses.

**The remaining even sizes.** The only unresolved possible sizes are \(n=4,6,8,10\). Exhaustive finite evaluation of the explicitly displayed update map checks every one of the \(2^{n+1}\) labeled configurations at each size, without sampling. It counts a configuration as having least period eight precisely when the eighth iterate equals the initial configuration and the fourth iterate differs. The full finite computations, presented as an independently checkable finite proof in `check_bitwise.py` and `check_graph.py`, return zero at all four sizes. The same complete evaluation at \(n=12\) returns precisely \(288\) primitive-eight configurations, as asserted. Both programs independently implement the update: one with bit operations, the other from the explicit graph adjacency. Their complete loop bounds and results appear in the verification section. This completes the characterization.

## Verification

Execute `python3 check_bitwise.py` and `python3 check_graph.py` using Python 3.8 or later. The first exhausts all \(2^{n+1}\) states for every \(3\le n\le16\), checks eighth versus fourth iterates, and prints the counts. The second independently constructs the actual adjacency lists and exhausts \(3\le n\le12\). Both return zero for \(3\le n\le11\) and \(288\) at \(n=12\). Additional bitwise counts at \(n=14\) and \(n=16\) are \(784\) and \(1536\), respectively; these are checks, not claimed formulas at all lengths. The first program also tests the symbolic block witness at every even length from \(12\) to \(100\). Its exact \(n=12\) trajectory has hub/count pairs \((1,2),(1,4),(1,6),(1,8),(0,10),(0,8),(0,6),(0,4)\).

The infinite-family assertion rests on the endpoint-expansion proof and the cited odd-case theorem, not on finite experiments. The finite exclusion \(n\in\{4,6,8,10\}\) and the \(288\) count use the complete, reproducible finite enumeration.

## Relationship to prior work

Haslegrave and Cannings, arXiv:1606.05496v1 (first public version June 17, 2016), provide the critical broader period restriction for a **pure anti-threshold** nonconformist (Theorem 10), and describe period-eight behavior requiring loops under that assumption. Here the graph is loopless but the hub's inertial tie rule explicitly falls outside their pure neighbor-dependent anti-threshold hypothesis. The claim does **not** contradict the theorem; rather, it locates a sharp, natural boundary of its applicability and gives an infinite explicit wheel family and a first-size census not stated there. Their Section 5 constructs other possible periods on other graphs using more general hub rules and does not imply this wheel-specific existence criterion.

Goles and Olivos' 1980 symmetric threshold-network results address homogeneous-sign threshold period restrictions; Cannings' 2009 majority/minority network study discusses other network classes. Neither an abstract-level description nor generic period realizability implies the displayed wheel threshold. The exact existence statement and the finite size-12 population were compared against published searches for wheel dynamics, one contrarian, inertial anti-majority ties, and period-eight networks. Unindexed alternatives remain a historical-priority risk.

## Limitations

No formula is claimed for the total primitive-eight population at general even lengths above \(12\), nor for other primitive periods, basins of attraction or first-entry times. The absence of period eight on odd wheels relies on a published general theorem, with its pure anti-threshold assumption explicitly checked; the current argument does not reprove that theorem. The exact count \(288\) rests on an exhaustive finite checker with inspectable source, not a symbolic closed-form classification. The historical comparison includes one accessible full preprint and abstracts of older works; it cannot exclude all unpublished or unindexed prior equivalent results. Independent external audit has not been performed.

## References

1. J. Haslegrave and C. Cannings, *Majority dynamics with one nonconformist*, arXiv:1606.05496v1 (2016-06-17), especially Sections 1, 4 (Theorem 10), and 5. https://arxiv.org/html/1606.05496v1
2. C. Cannings, *The majority and minority models on regular and random graphs*, GameNets (2009-06-26), DOI 10.1109/GAMENETS.2009.5137464. https://eudl.eu/doi/10.1109/gamenets.2009.5137464
3. E. Goles and J. Olivos, *Periodic behaviour of generalized threshold functions*, Discrete Mathematics 30 (1980), 187–189, DOI 10.1016/0012-365X(80)90121-1. https://pure.uai.cl/en/publications/periodic-behaviour-of-generalized-threshold-functions/
