# A parity transition in optimal induced-matching exchanges on Möbius ladders

## Finding

For every integer \(n\ge4\), the Möbius ladder \(M_{2n}\) has induced-matching number \(\nu_s(M_{2n})=\lfloor n/2\rfloor\). Its *optimal one-edge-exchange graph* \(\mathcal R_n\) has one vertex for each maximum induced matching, with adjacency when one chosen graph edge can be replaced by another without sacrificing induced matching or cardinality.

The exact classification is

\[
\begin{array}{c|c|c}
\text{rung count}& |V(\mathcal R_n)| & \text{exchange structure}\\\hline
n\equiv0\pmod4&2&2K_1\\
n\equiv2\pmod4&6&6K_1\\
n\text{ odd}&n^2&\text{connected}
\end{array}
\]

For every odd \(n\ge5\), its degree polynomial and edge count are exactly

\[
\sum_{X\in V(\mathcal R_n)}t^{\deg(X)}
=n(n-3)t^4+2nt^5+nt^6,
\qquad |E(\mathcal R_n)|=2n(n+1).
\]

This contrast concerns maximum *induced* matchings and replacing one *edge* at a time. It is not the perfect-matching flip problem, ordinary matching reconfiguration, or token jumping of one endpoint of a matching.

## Assumptions and scope

Graphs are finite, simple and undirected. An induced matching is a set of pairwise vertex-disjoint edges whose combined endpoint set induces exactly those edges (a 1-regular subgraph). For \(n\ge4\), label two vertices in each column \(i\in\mathbb Z/n\mathbb Z\) by \(a_i,b_i\). Put a rung \(R_i=a_ib_i\) in each column. For \(0\le i<n-1\), put horizontal edges \(H_i^a=a_ia_{i+1}\) and \(H_i^b=b_ib_{i+1}\). Across the seam put \(H_{n-1}^a=a_{n-1}b_0\) and \(H_{n-1}^b=b_{n-1}a_0\). This is exactly the graph comprising a cycle of length \(2n\) and the \(n\) antipodal chords. Each rung or horizontal edge has a unique **start column** \(i\).

Only optimum-preserving single-edge replacements are permitted: an edge exchange \(X\mapsto X-\{e\}+\{f\}\) where \(e\in X\), \(f\notin X\), and the resulting edge set is induced and has the same size. The cyclic seam flips rail labels; it is not an ordinary untwisted prism.

## Proof

**1. Column separation and optimum size.** Two edges with the same start column cannot both belong to an induced matching, because their endpoints either coincide or are connected by a rung. Two edges starting in adjacent columns cannot coexist: adjacent rungs are linked by a rail edge, a rung conflicts with a neighboring horizontal edge, and two neighboring horizontals meet or have adjacent endpoints in their shared column. Thus start columns of any induced matching form an independent set of the cycle on \(n\) columns. Its size is at most \(\lfloor n/2\rfloor\). Selecting rungs in every other column gives a matching of this size, hence equality.

**2. The gap-two transition rule.** If successive chosen start columns in cyclic order are separated by two columns, direct inspection of the edges in their three-column window gives precisely these possibilities, taking the seam rail swap into account:

- \(R\to R\): always possible;
- \(R\to H\): either local rail for the new horizontal is possible;
- \(H\to H\): the two horizontals must use opposite local rails;
- \(H\to R\): impossible.

For a gap of three or more start-column steps, those two edges impose no further mutual restriction. For the special even boundary \(n=4\), the same pair of columns is tested in both cyclic directions; applying both transition constraints gives the same classification below.

**3. Maximum configurations.** Put \(m=\lfloor n/2\rfloor\). For even \(n\), an independent set of \(m\) starting columns is necessarily one of the two alternating parity classes, with all successive gaps equal to two. As there is no allowed transition \(H\to R\), the cyclic list consists either entirely of rungs or entirely of horizontals. The two all-rung choices always work. The horizontal choices require alternating rail labels at successive starts; there is one twisted seam in a complete tour, hence consistency holds exactly when \(m\) is odd, that is, \(n\equiv2\pmod4\). In this case each of the two start-column supports admits two choices of horizontal rail phase. Thus there are two or six optima as asserted.

For odd \(n=2m+1\), \(m\ge2\), a maximum independent set of starting columns has precisely one cyclic gap of three, all other gaps being two. There are exactly \(n\) such supports. Begin the chosen-edge list just after the unique long gap and read it until just before that gap. The forbidden \(H\to R\) transition means that the edge types form a block \(R^{m-h}H^h\), for some \(0\le h\le m\). When \(h=0\) there is one realization; when \(h\ge1\), choose one of two rails for the first horizontal and all following horizontal rails are forced by alternation. The long gap disconnects these constraints, so the twisted seam causes no extra identification. Every listed choice is valid and distinct. Each start support therefore yields \(1+2m=n\) optima, giving \(n^2\) overall.

**4. Even cases are frozen.** The two maximum start supports for even \(n\) differ in all \(m\ge2\) positions. Thus a one-edge replacement cannot change the start support. On one fixed support, the optimum horizontal realizations (when they exist) and the all-rung realization differ in at least \(m\ge3\) selected edges, and the two horizontal rail phases also differ in all \(m\) positions. Consequently no two distinct optima differ by one edge; \(\mathcal R_n\) has no edges. At \(n=4\), only the two all-rung optima exist and are likewise disjoint.

**5. Odd cases are connected.** Given an odd-order optimum containing a horizontal edge, consider its first horizontal edge in the list after the unique gap of three. Replacing that edge by the rung at the same start position preserves all the gap-two rules: its predecessor is either a rung or is across the long gap, and its successor is a horizontal, for which \(R\to H\) is permitted. Repeating removes every horizontal without leaving the optimum family. The resulting all-rung optimum is supported on

\[
A_a=\{a,a+2,\dots,a+2m-2\}\pmod n.
\]

For any \(a\), the support \(A_{a+2}\) is obtained from \(A_a\) by replacing the rung at \(a\) with the rung at \(a-1\); the two supports have \(m-1\) common columns. As \(\gcd(n,2)=1\) for odd \(n\), these replacements connect all \(n\) all-rung optima. Consequently every optimum is in one connected component.

**6. Exact odd degrees.** Retain the parameter \(h\) counting horizontals, with \(m=(n-1)/2\). First consider exchanges that preserve the chosen start support. The only legal changes occur at the \(R/H\) boundary or at an endpoint of the horizontal block, and the gap-two rules give counts \(2,3,2,1\) respectively for \(h=0\), \(h=1\), \(2\le h<m\), and \(h=m\). For example, with \(h=1\) one can convert the sole horizontal into a rung, flip its rail, or convert the immediately preceding rung into the uniquely compatible horizontal.

Next, a one-edge change of a maximum start support can only move its first chosen column backward one step or its last chosen column forward one step (the unique gap of three shifts by two). Moving the first column leaves a new gap of three to its successor and a gap of two from the previously last edge. It permits three new edge types when that last edge is a rung (the \(h=0\) case), and one type when it is horizontal (\(h>0\)). Moving the last column leaves a gap of two to the original first edge and permits one new edge if that first edge is a rung (\(h<m\)), or two if it is horizontal (\(h=m\)). The two moves are distinct. Summing gives the exact degree table:

\[
\begin{array}{c|c|c|c}
h&\text{same support}&\text{changed support}&\deg\\\hline
0&2&4&6\\
1&3&2&5\\
2\le h<m&2&2&4\\
m&1&3&4
\end{array}
\]

Per start support, there is one \(h=0\) optimum and two optima for each \(1\le h\le m\). Across \(n\) supports this gives \(n\) degree-six, \(2n\) degree-five, and \(2n(m-1)=n(n-3)\) degree-four configurations. Their degree sum is \(4n(n+1)\); the handshake lemma gives \(2n(n+1)\) edges.

## Verification

Two standalone checkers included in the package independently reconstruct the graph and enumerate optima. `verify_rim.py` constructs the \(2n\)-cycle and antipodal chords, runs a complete edge-conflict branch-and-bound search (enumerating all optimal solutions), and checks adjacency and connected components. `check_twisted.py` builds the twisted two-rail coordinates instead, enumerates all \(\binom{3n}{\lfloor n/2\rfloor}\) candidate sets for small instances, tests inducedness directly from vertex neighborhoods, then checks exchange adjacency and degrees. Both were executed through \(4\le n\le12\), and exactly matched the formulas. The proof above, not a finite search, establishes the result for all \(n\ge4\).

Examples: at \(n=5\), the connected 25-vertex exchange graph has ten degree-four, ten degree-five and five degree-six vertices and 60 edges; at \(n=6\) there are six isolated optima; at \(n=9\) there are 81 connected optima and 180 exchange edges; at \(n=12\) there are two isolated optima.

## Relationship to prior work

Induced matchings are also known as strong matchings or independent sets in the square of a line graph. Basavaraju et al. (2013) develop bounds for the number of inclusion-maximal induced matchings in triangle-free graphs and give the corresponding general definitions; their bound does not imply an optimum-by-optimum exchange classification for Möbius ladders. Rautenbach (2015) provides greedy algorithmic bounds for induced matchings, not this specific classification. McSorley (1998) studies enumerative structures of Möbius ladders: its openly indexed abstract was inspected, but the available university repository returned HTTP 403 for the full document. Its potential overlap with the pure enumeration formula is therefore explicitly unresolved. The main claim is the all-order optimum-preserving *one-edge* reconfiguration dichotomy and exact degree profile, not a claim that all Möbius-ladder enumeration is new.

Eto et al. (2021) study general reconfiguration of induced \(d\)-regular vertex subsets. Their \(d=1\) rule moves one *vertex* and thus is not the one-whole-edge replacement rule here; their results concern algorithmic complexity on graph classes, not this exact family. Published Möbius-ladder results on ordinary matchings, perfect-matching square flips, vertex independent sets, and edge-open packings use different feasible sets or moves, hence their quantitative statements do not logically entail this theorem.

## Limitations

The theorem is restricted to the labelled Möbius ladders with \(n\ge4\); the exceptional three-rung graph \(M_6\cong K_{3,3}\) is not included. It treats only maximum-cardinality induced matchings and one-whole-edge replacements, not all maximal induced matchings, other graph families, shortest exchange-path lengths, or alternate reconfiguration rules. Enumerations through order twelve are checks rather than a proof for arbitrary order. A historic same-object enumerative paper remained inaccessible in full despite an open-repository attempt; the exact priority of the pure counting formula and any unindexed exchange characterization remains a residual risk.

## References

1. M. Basavaraju, P. Heggernes, P. van 't Hof, R. Saei, Y. Villanger, *Maximal induced matchings in triangle-free graphs*, arXiv:1312.5180v1 (first public 18 December 2013), https://arxiv.org/pdf/1312.5180.
2. D. Rautenbach, *Two Greedy Consequences for Maximum Induced Matchings*, arXiv:1507.04145v1 (15 July 2015), https://arxiv.org/pdf/1507.04145.
3. J. P. McSorley, *Counting Structures in the Möbius Ladder*, Discrete Mathematics 184 (1998), 137–164, https://doi.org/10.1016/S0012-365X(97)00086-1; abstract at https://opensiuc.lib.siu.edu/math_articles/93/ (full text inaccessible on inspection).
4. H. Eto, T. Ito, Y. Kobayashi, Y. Otachi, K. Wasa, *Reconfiguration of Regular Induced Subgraphs*, arXiv:2111.13476 (2021), https://arxiv.org/pdf/2111.13476.
