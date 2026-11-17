# A universal short odd-period gap and eleven-site traveling waves in Rule 54

## Finding

Let \(F_n:\{0,1\}^n\to\{0,1\}^n\) be the synchronous elementary cellular automaton Rule 54 on an indexed cyclic ring of \(n\ge3\) sites. The local transition is
\[
(F_n(x))_i=x_i\oplus(x_{i-1}\lor x_{i+1}),\qquad i\pmod n.
\]
For every \(n\ge3\),
\[
\#\operatorname{Fix}(F_n^t)=1 \quad(t\in\{1,3,5,7,9\}),\qquad
\#\operatorname{Fix}(F_n^{11})=1+22\mathbf1_{11\mid n}.
\]
Thus no nonzero configuration has a primitive odd temporal period below eleven; the number of primitive temporal eleven-cycle orbits on an indexed ring of length \(n\) is exactly \(2\mathbf1_{11\mid n}\). The two orbits are spatially eleven-periodic traveling waves of opposite directions, interchanged by spatial reflection. This is a universal short-time periodic-point theorem, not a classification of all odd periods or all attracting orbits.

## Assumptions and scope

The symbols \(\oplus\) and \(\lor\) denote Boolean exclusive-or and inclusive-or. Neighbors are distinct because \(n\ge3\). Temporal period is the smallest strictly positive \(t\) with \(F_n^t(x)=x\). Orbits are counted on the fully indexed ring, with no quotient by spatial rotations or reflections. The indicator \(\mathbf1_{11\mid n}\) equals one when eleven divides \(n\), zero otherwise. A configuration fixed by the eleventh iterate has temporal period one or eleven because eleven is prime.

## Proof

**Temporal columns.** Fix a positive integer \(t\). For a time-periodic space–time history, denote the \(t\)-bit time word at one spatial site by \(b=(b_0,\ldots,b_{t-1})\), with time indices modulo \(t\). Let \(a\) and \(c\) denote the adjacent temporal columns. The local transition constraints are, exactly,
\[
 b_{j+1}=b_j\oplus(a_j\lor c_j) \qquad(j\pmod t).
\]
Define a directed graph \(G_t\) on the \(2^{2t}\) ordered pairs \((a,b)\), with an edge \((a,b)\to(b,c)\) precisely when every displayed local constraint holds. Spatially closed walks of length \(n\) in \(G_t\) correspond *bijectively* to configurations on the indexed \(n\)-site ring fixed by \(F_n^t\): the time-zero symbols of the columns give the configuration, and its subsequent time slices are uniquely forced. Repeated vertices and nonprimitive spatial periods are permitted; closed walks are rooted at an indexed site.

**Exact edge generator.** Write the words as integers in \([0,2^t-1]\), and let \(S(b)\) be rotation by one toward the least-significant-bit end, so its bit \(j\) is \(b_{j+1}\). If \(a_j=1\), the constraint requires \(S(b)_j=1-b_j\) and leaves \(c_j\) unrestricted. If \(a_j=0\), it forces \(c_j=b_j\oplus S(b)_j\). Thus an edge exists if and only if every set bit of \(a\) is a set bit of \(b\oplus S(b)\), and all permitted successors are enumerated by
\[
 c=((b\oplus S(b))\mathbin{\&}\neg a)\lor s,
 \qquad s\subseteq a,
\]
where complementation is truncated to \(t\) bits and \(s\) runs through all bit submasks of \(a\). There is no sampling or heuristic step. As a cross-check, the exact total edge number satisfies
\[
 |E(G_t)|=\sum_{b\in\{0,1\}^t}3^{\#\{j:b_j\ne b_{j+1}\}}
 =4^t+(-2)^t,
\]
by the eigenvalues \(4,-2\) of the two-state cyclic transfer matrix \(\left(\begin{smallmatrix}1&3\\3&1\end{smallmatrix}\right)\).

**Finite exhaustive lemma.** The included standalone C++17 programs independently enumerate these graphs for \(t=1,3,5,7,9,11\). One constructs the exact adjacency and reverse-adjacency lists from the Boolean formula above and repeatedly deletes any vertex whose current indegree or outdegree is zero. At all six heights every vertex remaining after deletion has exactly one incoming and outgoing edge, and the residual directed-cycle lengths are exactly
\[
\begin{array}{c|rrrrrr}
t&1&3&5&7&9&11\\\hline
\text{surviving cycle lengths}&(1)&(1)&(1)&(1)&(1)&(1,11,11).
\end{array}
\]
The residual vertex counts are \(1,1,1,1,1,23\), respectively. The separate verifier constructs successors by consulting all eight entries of the original local Rule 54 table and computes the recurrent strongly connected components by Kosaraju's algorithm, independently recovering the same lists. The certificate is finite and exhaustive: its largest graph has \(4,194,304\) vertices and \(4,192,256\) edges. Removing zero-degree vertices cannot remove any closed walk; since every surviving vertex has degree one in both directions, *every* closed walk of the original graph is a repetition of precisely one listed simple directed cycle. Therefore the number of rooted closed spatial walks is one at the five smaller odd heights and is \(1+11\mathbf1_{11\mid n}+11\mathbf1_{11\mid n}\) at height eleven. The singleton loop is the all-zero configuration.

**Primitive orbits and wave speed.** On eleven sites the two binary words `00001001111` and `00001111001` each return after eleven Rule 54 updates. The first moves by a cyclic shift of four bit positions at each update, while the second moves by seven, i.e. negative four modulo eleven; neither shift is trivial, so each has least temporal period eleven. Their spatial rotation families are disjoint and related by reflection. The graph classification proves that these are *all* nonzero configurations fixed by the eleventh iterate, at every ring length. Repeating either word spatially gives the two orbits whenever \(11\mid n\); no other ring length admits them.

## Verification

The exact source files are `src/temporal_column_core.cpp` and `src/independent_scc.cpp`; their independently generated outputs are in `certificates/column_core.txt` and `certificates/independent_scc.txt`. Compile each using C++17 and run it without input. The first checks all live-core in/out degrees and enumerates disjoint cycles; the second reads the eight-bit transition rule directly and independently enumerates strongly connected components. The program `src/direct_ring.py` separately enumerates every initial configuration on rings \(3\le n\le11\), including eleven-site witnesses; its recorded output is `certificates/direct_ring.txt`. All recorded outputs were regenerated from the exact included source files. The all-ring statements rest on the complete finite graph certificates, not on the small-ring experiment.

## Relationship to prior work

Martínez, Adamatzky and McIntosh (2008, Section 2.2 and Table 2) already record an eleven-period example on an eleven-site Rule 54 ring and a temporal twenty-seven-cycle on nine sites. Their 2014 extended treatment (Section 4, Table 5) likewise lists the eleven-site example. These examples are explicitly *not* claimed as discoveries here. The distinct statement established here is the complete all-circumference **eleventh-return count**, the classification into exactly two oppositely moving spatial eleven-waves, and the global exclusion of nontrivial odd temporal periods three, five, seven and nine. Redeker (2010) develops the periodic ether/glider formalism, but does not enumerate this complete short-odd sector. A separate published discussion by Guan (2012) concerns Bernoulli shifts on invariant subsystems; its full text could not be inspected, so comparison with that source remains a documented historical-priority limitation.

## Limitations

Nothing here excludes odd temporal periods greater than or equal to thirteen, bounds transients, computes attraction basins, or characterizes arbitrary odd-period orbits. In particular, the nine-site ring has a temporal twenty-seven-cycle (already represented in the 2008 tables): eleven is the earliest *temporal period*, not the smallest *spatial circumference* supporting any odd temporal period. The result is based on transparent exact finite enumeration with two independently implemented checkers; it has not undergone external independent mathematical audit. Prior work may contain an equivalent all-ring classification that was not accessible or indexed.

## References

- G. J. Martínez, A. Adamatzky, H. V. McIntosh, “On the Representation of Gliders in Rule 54 by de Bruijn and Cycle Diagrams,” *Cellular Automata*, LNCS 5191, pp. 83–91 (2008), DOI: https://doi.org/10.1007/978-3-540-79992-4_11. Proceedings eBook public release dated 2008-08-24 by Springer. Public full text: https://www.comunidad.escom.ipn.mx/genaro/Papers/Papers_on_CA_files/acri08R54.pdf
- M. Redeker, “Gliders and Ether in Rule 54,” arXiv:1007.2920v1, first posted 2010-07-17. https://arxiv.org/abs/1007.2920
- G. J. Martínez, A. Adamatzky, H. V. McIntosh, “Complete Characterization of Structure of Rule 54,” arXiv:1410.3096v1, first posted 2014-10-12. https://arxiv.org/html/1410.3096v1
- J. Guan, “Complex Dynamics of the Elementary Cellular Automaton Rule 54,” *Int. J. Mod. Phys. C* 23, 1250052 (2012), DOI: https://doi.org/10.1142/S0129183112500520 (full text inaccessible at review).
