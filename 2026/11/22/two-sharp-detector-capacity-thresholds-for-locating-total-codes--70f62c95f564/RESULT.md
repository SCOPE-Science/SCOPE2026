# Two sharp detector-capacity thresholds for locating-total codes on \(C_3\square C_6\)

## Finding
Let \(G=C_3\square C_6\) be the labelled Cartesian product with vertices \(V=\mathbb Z_3\times\mathbb Z_6\), and let \(\mathcal L\) be its locating-total dominating vertex sets. A configuration \(S\in\mathcal L\) has a nonempty detector signature \(N(v)\cap S\) at every vertex, and these signatures are distinct for distinct vertices outside \(S\). Define \(\mathcal R_B\) to have vertices \(\{S\in\mathcal L:|S|\le B\}\), with an edge for adding or deleting exactly one selected vertex while retaining a locating-total code.

The minimum size is \(6\), with exactly \(12\) minimum codes. The minimum value is known from the 2014 theorem of Xing and Sohn and is **not a new claim**. The new statement is the exact budget reconfiguration phase diagram. In the following table a component type \((s,m)\times t\) means \(t\) connected components, each containing \(s\) valid states and exactly \(m\) of the twelve minimum codes.

| Maximum selected vertices \(B\) | Total states | Component types \((s,m)\times t\) |
|---:|---:|---|
| 6 | 12 | \((1,1)\times12\) |
| 7 | 372 | \((1,0)\times216\); \((13,1)\times12\) |
| 8 | 5,565 | \((1,0)\times2259\); \((132,0)\times6\); \((1257,6)\times2\) |
| 9 | 22,475 | \((1,0)\times60\); \((22415,12)\times1\) |
| 10 | 48,620 | \((48620,12)\times1\) |

For all integer \(B\) with \(10\le B\le18\), \(\mathcal R_B\) is connected. Therefore **three extra detectors** (capacity nine) are necessary and sufficient to place every optimum in a single connected component, while **four extra detectors** (capacity ten) are necessary and sufficient for connectivity of the full feasible-state graph. At capacity nine there remain exactly sixty isolated inclusion-minimal nonoptimum codes of size nine. This gives two distinct sharp capacity thresholds.

At capacity nine, from *each* optimum the shortest add-delete distances to the twelve optima occur with multiplicities \(1,3,2,6\) at lengths \(0,4,6,12\), respectively. All six opposite-parity optima are at distance twelve. The exact locating-total cardinality polynomial is
\[
\begin{aligned}
L_G(z)=&12z^6+360z^7+5193z^8+16910z^9+26145z^{10}\\
&+25182z^{11}+16908z^{12}+8316z^{13}+3042z^{14}\\
&+816z^{15}+153z^{16}+18z^{17}+z^{18}.
\end{aligned}
\]
The polynomial counts labelled vertex sets, without dividing by graph automorphisms. The enumerator supplements the sharp reconfiguration thresholds, rather than being an independent primary claim.

## Assumptions and scope
The three-cycle is a triangle: row coordinate \(r\in\mathbb Z_3\), column coordinate \(c\in\mathbb Z_6\). Two distinct vertices are adjacent exactly when the row coordinates agree and the columns differ by \(\pm1\pmod6\), or the columns agree and the rows differ by \(\pm1\pmod3\). Thus every vertex has four open neighbors. A locating-total set uses **open**, not closed, neighborhoods and distinguishes only vertices outside the set. A configuration may change by *one vertex addition or deletion*, not token jumping, token sliding, simultaneous replacements, or modifications passing through noncodes. All labels, budget inequalities, and component counts refer solely to this fixed eighteen-vertex graph. No result is asserted for larger triangular tori.

## Proof
**Exact finite characterization.** Label \((r,c)\) by the bit index \(i=3c+r\), with \(0\le r<3\), \(0\le c<6\). For each integer mask \(b\) from \(0\) to \(2^{18}-1\), let \(S_b=\{(r,c):b_i=1\}\), and form four-bit-neighborhood masks \(M_i=\sum_{j\in N(i)}2^j\). Then \(S_b\in\mathcal L\) **if and only if** (i) \(b\mathbin{\&}M_i\ne0\) for every \(i\) and (ii) the nonzero masks \(b\mathbin{\&}M_i\), restricted to \(i\notin S_b\), are pairwise distinct. The two conditions are exactly total domination and location by open-neighborhood signatures; there are no other hidden requirements.

**Exhaustive state enumeration.** Evaluate this predicate for every mask in the complete integer interval \([0,262143]\). The two included independently implemented programs reproduce the cardinality polynomial shown above; in particular no codes have fewer than six vertices, and there are twelve six-vertex codes. These minimum codes are exactly the two choices of alternating three occupied columns, with two selected row vertices per occupied column and their three omitted row indices constituting a permutation of \((0,1,2)\). Directly checking the twelve masks by the predicate confirms this description; the exhaustive sweep proves its converse.

**Exact transition enumeration.** For each capacity \(B\), restrict to masks satisfying the predicate and \(\operatorname{popcount}(b)\le B\). Connect two distinct allowed masks if and only if \(b\oplus b'=2^i\) for some bit index \(i\). This is bijective with legal single-addition or single-deletion moves. Breadth-first search over all allowed masks gives the component table. Separately, a second source implementation constructs a disjoint-set union over all legal mask pairs and returns precisely the same component profile for every capacity \(B=6,\ldots,18\). Thus these are full graph decompositions, not Monte Carlo estimates, truncated searches, or selected examples.

**Sharpness and distance claims.** For \(B=8\), two components contain six minima each, so no capacity-eight move sequence can connect all optima. At \(B=9\), one 22,415-state component contains all twelve, proving the first sharp threshold, but sixty single-state components remain, disproving global connectedness. At \(B=10\), all 48,620 allowed configurations lie in one component, proving the second sharp threshold. The two exhaustive programs independently verify connectedness for each of the remaining capacities \(B=11,\ldots,18\). No deletion-monotonicity assumption is used: an arbitrarily chosen detector deletion could invalidate a locating-total code, and therefore connectivity is established by explicit full-state graph traversal. For the capacity-nine minimum-to-minimum metric, breadth-first search from each of the twelve minima computes all finite distances across its entire 22,415-state component, yielding the given multiplicities. The included length-twelve witness supplies an independently inspectable sample path, not the exhaustive proof.

## Verification
The package includes `verify_python.py` and `verify_cpp.cpp`, plus their corresponding recorded exact outputs and `witness_transition.txt`. The first uses a Python set membership predicate, explicit breadth-first components and twelve all-source breadth-first searches. The second creates neighborhood masks independently and uses a C++ disjoint-set data structure, followed by its own shortest-path searches. Both evaluate all \(262144\) possible labelled vertex subsets and all valid one-bit transitions, and agree on each recorded invariant. Reproduce by running `python3 verify_python.py` and compiling `verify_cpp.cpp` with `c++ -O2 -std=c++17 -o verify_cpp verify_cpp.cpp`, then executing `./verify_cpp`. The outputs end in `PASS`. The shortest-path witness masks are hexadecimal under the bit encoding specified above.

## Relationship to prior work
Xing and Sohn's 2014 paper determines \(\gamma_t^L(C_3\square C_n)\), proving that it equals \(n\) if \(6\mid n\) and \(n+1\) otherwise. Its lower bound and periodic constructions are the known source of the six-vertex minimum; the paper does not determine connected components of the capacity-bounded add-delete state graphs on the fixed graph. The earlier conference announcement of the related topic appeared on December 20, 2013. A separate published record concerning the first minimum-code token-slide fragmentation on \(C_3\square C_n\) covers \(n=3,4\), compares slide and jump moves *between minima*, and neither states nor implies the capacity-nine/capacity-ten phase transition on \(C_3\square C_6\). General domination reconfiguration with an add-delete budget does not establish this stronger locating-total predicate. Literature comparisons in the accompanying structured review distinguish objects, moves, and parameter coverage.

## Limitations
The results are exact for one labelled graph, not a general formula in \(n\). The numerical statistics rest on finite exhaustive programs with complete source and independent implementations; they do not constitute a proof of any infinite-family conjecture. The scalar minimum is preexisting. Historical novelty cannot be guaranteed against inaccessible or unindexed work. The classification uses a chosen coordinate labelling, but component sizes and connectivity thresholds are graph isomorphism invariants.

## References
1. Huaming Xing and Moo Young Sohn, *Bounds on locating-total domination number of the Cartesian product of cycles*, Ars Combinatoria 113A (2014), 139–146, https://combinatorialpress.com/article/ars/Volume%20113-A/volume-113-A-paper-12.pdf.
2. Moo Young Sohn, *Bounds on Locating total Domination Number of the Cartesian Product Graphs*, ICNAO2013 programme and conference abstract (December 20, 2013): https://icnao2013-math.nsysu.edu.tw/var/file/190/1190/img/1727/ICNAO2013_Program.pdf and https://icnao2013-math.nsysu.edu.tw/var/file/190/1190/img/1727/Abstracts_ICNAO2013.pdf.
3. Michael A. Henning and Nader Jafari Rad, *Locating-total domination in graphs*, Discrete Applied Mathematics 160 (2012), https://doi.org/10.1016/j.dam.2012.04.004.
4. *First token-slide fragmentation for minimum locating-total codes on \(C_3\square C_n\)*, available public research record, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-first-token-slide-fragmentation-for-minimum-locating-total-codes--078461c289f3.
5. S. M. Haas and K. Seyffarth, *The \(k\)-dominating graph*, Graphs and Combinatorics 30 (2014), https://doi.org/10.1007/s00373-013-1302-3.
