# Two-defect mobility and degree census of optimal burning schedules on \(C_{k^2-2}\)

## Finding

Let \(k\ge3\), put \(n=k^2-2\), and label the vertices of the simple cycle \(C_n\) by \(\mathbb Z/n\mathbb Z\). An *optimal strict burning schedule* is an ordered \(k\)-tuple \((x_1,\ldots,x_k)\) such that each source is unburned when ignited and every vertex has burned by the end of round \(k\). Let \(\mathcal R_k\) have these schedules as vertices, adjacent when exactly one source \(x_i\) moves to an adjacent vertex of \(C_n\), all other source positions and ignition times remain fixed, and the result is another optimal strict schedule.

**Theorem.** For every integer \(k\ge3\), \(\mathcal R_k\) has exactly \((k-1)!\) connected components, each of cardinality
\[
 n\,\frac{k^2+k-4}{2}.
\]
All components are isomorphic, and the complete degree census is
\[
\begin{aligned}
\#\{s:\deg(s)=2\}&=n(k-1)!(k-1),\\
\#\{s:\deg(s)=3\}&=2n(k-1)!,\\
\#\{s:\deg(s)=4\}&=n(k-1)!\frac{k^2-k-6}{2}.
\end{aligned}
\]
No other degrees occur. In particular,
\[
 |V(\mathcal R_k)|=n(k-1)!\frac{k^2+k-4}{2},\qquad
 |E(\mathcal R_k)|=n(k-1)!(k^2-4).
\]
At \(k=3\), the degree-four term is zero. For \(k\ge4\), three different vertex degrees coexist.

## Assumptions and scope

The burning process starts with every vertex unburned. In round \(i\), a new unburned vertex \(x_i\) is ignited; fire spreads along an edge in each subsequent round, and a vertex stays burned forever. The strict requirement means no source was burned at an earlier round. The closed ball \(B_r(x)\) consists of cycle vertices at distance at most \(r\) from \(x\). Standard burning-sequence equivalence gives
\[
\bigcup_{i=1}^{k}B_{k-i}(x_i)=V(C_n),\qquad
 d(x_i,x_j)\ge j-i\quad(1\le i<j\le k).
\]
A valid schedule is optimal because \((k-1)^2<n\le k^2\); indeed, \(k-1\) closed balls of radii \(k-2,\ldots,0\) cover at most \((k-1)^2\) cycle vertices, whereas explicit \(k\)-source schedules are constructed below. All cycles are labeled, all source times are distinguished, and equality is literal rather than up to rotation or reflection. The theorem asserts no classification for other cycle orders or for unconstrained source jumps.

## Proof

**1. At most two repeated incidences.** Put \(r_i=k-i\); these radii are the distinct integers \(0,1,\ldots,k-1\). Because \(k\ge3\), each ball \(B_{r_i}(x_i)\) is a proper circular interval of exactly \(2r_i+1\) vertices. Their total size is
\[
\sum_{r=0}^{k-1}(2r+1)=k^2=n+2.
\]
For a valid covering, the total incidence excess \(\sum_{v\in C_n}(m(v)-1)\), where \(m(v)\) is the number of balls containing \(v\), is therefore exactly two.

No ignition center can lie strictly inside another source's ball as a circular interval. If a center of positive radius \(r\ge1\) lay in the interior of a different ball, all three consecutive vertices centered there would belong to both balls, already yielding incidence excess at least three. If the center has radius zero, it is \(x_k\); its lying strictly inside the ball of any earlier source \(x_i\) would imply \(d(x_i,x_k)\le r_i-1=k-i-1\), contrary to the strict-source constraint \(d(x_i,x_k)\ge k-i\).

**2. The unique cyclic gap encoding.** List the ignition centers clockwise, beginning at the unique radius-zero center, and record their radii in this order as
\[
(r_0,r_1,\ldots,r_{k-1}),\qquad r_0=0,
\]
where the remaining entries are a permutation of \(1,\ldots,k-1\). Let \(d_j\) be the clockwise positive distance between the centers with radii \(r_j\) and \(r_{j+1}\), with subscripts modulo \(k\). No other ball can cover an uncovered point strictly between two consecutive centers without crossing one of those centers, which would put that center in the interior of the other ball. Therefore the centers' own balls must cover each intervening gap, and
\[
 d_j\le r_j+r_{j+1}+1.
\]
Define \(t_j=r_j+r_{j+1}+1-d_j\ge0\). Summing around the cycle gives
\[
\sum_{j=0}^{k-1}t_j
 =\sum_{j=0}^{k-1}(r_j+r_{j+1}+1)-n=k^2-n=2.
\]
Furthermore, \(t_0\le1\) and \(t_{k-1}\le1\): if an interval between the radius-zero center and a positive-radius center had \(t_j=2\), their distance in that direction would be \(r-1\), violating the strict-source separation. All other \(t_j\) may take values \(0,1,2\). Hence allowable gap data consist of two ones in distinct positions or one two at one of the \(k-2\) interior positions. There are
\[
 \binom{k}{2}+(k-2)=\frac{k^2+k-4}{2}
\]
choices.

Conversely, every choice of an anchor position for the radius-zero center, clockwise permutation of the other radii, and such a gap vector \((t_j)\) gives a unique valid schedule. Indeed \(d_j=r_j+r_{j+1}+1-t_j\) is positive, its sum is \(n\), and the two balls at each gap's endpoints cover every vertex in that clockwise segment. Neighboring center pairs satisfy the strict-source distance requirement because \(d_j\ge |r_j-r_{j+1}|\), with the radius-zero restriction handling the only tight case. For nonneighboring centers, either clockwise path between them contains at least two positive gaps; on a path of \(m\ge2\) gap edges the length is
\[
 r_{\mathrm{start}}+r_{\mathrm{end}}+2\sum r_{\mathrm{internal}}+m-\sum t_j
 \ge r_{\mathrm{start}}+r_{\mathrm{end}}
 \ge |r_{\mathrm{start}}-r_{\mathrm{end}}|,
\]
since the total deficit on every path is at most two. Both directions therefore satisfy the separation condition. The same inequality applies to the opposite clockwise route for adjacent pairs whenever that route has at least two gaps. These conditions establish that every generated tuple is a valid strict burning schedule. There are \(n\) anchor positions, \((k-1)!\) radius orders and \((k^2+k-4)/2\) gap vectors.

**3. Moves as a two-particle system.** Sliding the center of radius \(r_j\) one vertex clockwise leaves the radius order unchanged and transfers one unit from \(t_{j-1}\) to \(t_j\). The reverse slide transfers a unit the other way. These are precisely the legal moves on \(t\): transfer one of its two indistinguishable units between neighboring sites of a \(k\)-cycle, with capacity one at sites \(0\) and \(k-1\) and capacity two at all other sites. In particular, no legal slide can exchange the clockwise order of two centers: crossing would force a coincident center at an intermediate position, which is excluded by strictness. Thus each connected component is confined to one clockwise permutation of the nonzero radii.

**4. Connectivity for one fixed radius order.** The gap-vector particle system is connected. To see this, first move one unit away from any doubly occupied interior site into an empty neighbor. Thereafter two units occupy distinct sites on the path \(0,1,\ldots,k-1\), and the ordinary two-particle exclusion graph on a connected path is connected. In particular every gap vector can be brought to \(t=(1,1,0,\ldots,0)\).

It remains to vary the anchor \(x_k\). Starting at this canonical vector, make the legal transfers
\[
 0\to1,\quad1\to2,\quad2\to3,\quad\cdots,\quad (k-2)\to(k-1),\quad(k-1)\to0.
\]
The first transfer uses the capacity-two site \(1\), and no capacity bound is broken thereafter. The gap vector returns to its initial value, while the final transfer is a clockwise slide of the radius-zero center and increments the anchor by exactly one vertex. Repeating this loop reaches all \(n\) anchor positions. Hence all configurations with a fixed clockwise radius order are connected, yielding exactly \((k-1)!\) components, each of the claimed cardinality.

**5. Degrees.** A vector with two units at a single interior site has two legal moves. There are \(k-2\) such vectors. Two units at different sites have degree four except when the sites are adjacent and a unit would be moved into a capacity-one site. The adjacent pair \(\{0,k-1\}\) has degree two; the pairs \(\{0,1\}\) and \(\{k-2,k-1\}\) have degree three; all remaining pairs have degree four. Thus, per anchor and clockwise radius order, there are \(k-1\) vectors of degree two, two of degree three, and \(\binom{k}{2}-3=(k^2-k-6)/2\) of degree four. Multiplication by \(n(k-1)!\) gives the formulas above. The handshaking lemma gives the exact number of edges.

## Verification

Two standalone programs accompany this document. `construct_check.py` enumerates the cyclic-gap encodings, checks the strict distance constraints and ball coverings directly, verifies the predicted counts for \(k=3,\ldots,7\), and independently compares the complete generated set against brute-force tuples for \(k=3,4\). Run with `python3 construct_check.py`; the exact expected result appears in `construct_check.out`.

`direct_exhaustive.cpp` constructs the burning ball bitsets directly from shortest-path distances, enumerates all ordered tuples subject only to strict ignition constraints and coverage, and then builds the source-slide graph and performs exhaustive breadth-first component enumeration for \(k=3,4,5\). Compile with `g++ -std=c++17 -O3 direct_exhaustive.cpp -o direct_exhaustive` and run `./direct_exhaustive`; see `direct_exhaustive.out`. At \(k=3\), it confirms 56 schedules in two 28-state components, degree distribution \((28,28,0)\), and 70 edges. At \(k=4\), it confirms 672 schedules in six 112-state components, degree distribution \((252,168,252)\), and 1008 edges. At \(k=5\), it confirms 7176 schedules in 24 components of 299 states, degree distribution \((2208,1104,3864)\), and 11592 edges. Finite checks corroborate but are not the proof for unbounded \(k\).

## Relationship to prior work

Bonato, Janssen and Roshanbin developed the graph-burning process, its ball-cover/separation characterization, and the minimum burning time of paths and cycles. Their graph-burning number and definitions are used here, not claimed as new. The result concerns a different exact invariant: the entire source-slide reconfiguration graph for strictly valid schedules on the **two-below-square** cycle family. Earlier single-deficit and perfect-square classifications do not logically determine the two-particle state graph, its connectivity, or its degree distribution; no such classification is claimed for them here. Bonato's survey and the algorithmic treatment of optimal burning sequences by Pereira et al. provide closely related background but do not state this exact mobility theorem in inspected material. Relevant indexed records yielded no equivalent covering statement; this is evidence of noncoverage in the checked sources, not a proof of universal priority.

## Limitations

This theorem applies only to ordinary labeled simple cycles \(C_{k^2-2}\), \(k\ge3\), strict time-labelled optimum burning schedules, and slides of one source by one edge while other ignition times and locations remain fixed. It does not address arbitrary optimal schedules with a different timing convention, source swaps, larger deficits, nor the diameters or isomorphism types of the individual components beyond their stated size and connectivity. Historical priority cannot be guaranteed by a finite literature search. No independent scholarly audit has been performed.

## References

1. A. Bonato, J. Janssen, E. Roshanbin, *How to burn a graph*, arXiv:1507.06524v1, first posted 2015-07-23, especially Section 2, formula (1), Theorem 10 and Corollary 11. https://arxiv.org/abs/1507.06524
2. A. Bonato, *A survey of graph burning*, Contributions to Discrete Mathematics 16 (2021), 185–197, DOI:10.55016/ojs/cdm.v16i1.71194, especially Section 2.
3. F. de Carvalho Pereira, P. J. de Rezende, T. Yunes, L. F. B. Morato, *A Row Generation Algorithm for Finding Optimal Burning Sequences of Large Graphs*, ESA 2024, DOI:10.4230/LIPIcs.ESA.2024.94, Sections 1–3.
