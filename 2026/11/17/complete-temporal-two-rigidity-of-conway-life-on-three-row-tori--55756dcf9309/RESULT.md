# Complete temporal-two rigidity of Conway Life on three-row tori

## Finding

Consider synchronous Conway Life (B3/S23) on the fully periodic, labelled Moore lattice \(\mathbb Z/3\mathbb Z\times\mathbb Z/n\mathbb Z\), with \(n\ge3\). Let \(F_n\) denote one simultaneous update. For **every** integer \(n\ge3\),

\[
\operatorname{Fix}(F_n^2)\setminus\operatorname{Fix}(F_n)=
\begin{cases}
\{X^{(0)},X^{(1)},X^{(2)},X^{(3)}\},&4\mid n,\\
\varnothing,&4\nmid n,
\end{cases}
\]

where \(X^{(s)}\) has three identical rows, each equal to the binary cyclic word obtained by repeating `1100` and shifting the columns by \(s\) positions. In particular,

\[
\#\operatorname{Fix}(F_n^2)-\#\operatorname{Fix}(F_n)
=4\mathbf 1_{4\mid n},\qquad
\#\{\text{primitive temporal two-orbits}\}=2\mathbf 1_{4\mid n}.
\]

Both two-orbits, when present, belong to one orbit under cyclic spatial translation. No temporally primitive two-cycle on this torus contains a partially occupied column or a spatially localized oscillating motif.

## Assumptions and scope

The lattice has exactly three indexed rows and \(n\) indexed columns, both cyclic. Its eight Moore neighbors at each cell consist of the two other rows in its column and all three cells in each adjacent column. For \(n\ge3\), these eight sites are distinct. The live-neighbor count \(h\) determines the next bit \(b'\): \(b'=1\) exactly when \(h=3\), or when \(b=1\) and \(h=2\). Period is least temporal period under the **unshifted** map \(F_n\); spatial translations are not identified when counting labelled configurations or temporal orbits.

## Proof

Write a column at time zero as a three-bit integer \(x\in\{0,\ldots,7\}\), and at time one as \(y\in\{0,\ldots,7\}\). Encode a two-time column by \(c=x+8y\in\{0,\ldots,63\}\). For three consecutive columns \(a,b,c\), define \(L(a,b,c)\) to hold if, for each row, the B3/S23 local rule applied to the time-zero fields of those columns produces the time-one bit in the central column, **and** the same rule applied to their time-one fields produces the time-zero bit there. Explicitly, writing \(b_{r,t}\in\{0,1\}\) for the row-\(r\), time-\(t\) bit of \(b\), set

\[
H_{r,t}(a,b,c)=b_{r+1,t}+b_{r+2,t}
+\sum_{j=0}^{2}(a_{j,t}+c_{j,t}),
\]

where row indices are modulo three. Require, for both \(t\in\{0,1\}\),

\[
b_{r,1-t}=\mathbf1_{H_{r,t}=3}
+\mathbf1_{\{H_{r,t}=2\}}b_{r,t}.
\]

The two summands cannot both be one. Define a directed graph \(G\) on all \(64^2=4096\) ordered pairs \((a,b)\), putting \((a,b)\to(b,c)\) exactly when \(L(a,b,c)\) holds. Each closed walk of length \(n\) uniquely encodes a labelled pair \((X,Y)\) satisfying \(F_n(X)=Y\) and \(F_n(Y)=X\); conversely each such pair uniquely yields a closed walk. This correspondence is exact even at \(n=3\), because the three neighboring columns in each constraint correspond to three distinct cyclic columns.

The **finite graph lemma** is: \(G\) has \(6140\) edges and exactly three cyclic strongly connected components. Their respective numbers of vertices and internal edges are \((30,75)\), \((27,81)\), and \((4,4)\). In both larger components, every vertex \((a,b)\) has both columns *phase-diagonal*: its time-zero and time-one three-bit fields agree. The four vertices of the remaining component, represented by integers \(64a+b\), are

\[
455\longrightarrow504\longrightarrow3640\longrightarrow3591\longrightarrow455.
\]

This is the entire internal edge set of that component, and it is not phase-diagonal. The lemma is proved by explicit exhaustive construction of all \(4096\) vertices and all \(64^3\) possible column triples, followed by strongly connected component decomposition. The standalone `transfer_certificate.py` reproduces the complete finite check using only the displayed local rule and standard-library graph traversal, and independently asserts every integer and vertex above; it is a **finite proof certificate**, not an extrapolation from sampling ring sizes. Directly inspecting its loops verifies the local rule, the edge enumeration, and the SCC assertions.

Any closed walk lies completely inside one cyclic strongly connected component. The phase-diagonal components encode only \(X=Y\), hence fixed configurations. The sole non-phase-diagonal component is a directed four-cycle. It contributes exactly four closed walks if \(4\mid n\) and none otherwise. Its time-zero columns cycle through \(7,7,0,0\), giving precisely the four spatial phases of three identical rows with horizontal word `1100` repeated. The time-one columns are their complements, so two updates return the original phase, while one update moves it by two columns and changes it. The four configurations form two temporal orbits, exchanged by a one-column spatial shift. This proves all assertions for every \(n\ge3\).

## Verification

Run `python3 transfer_certificate.py` under Python 3, without third-party packages. The certificate reconstructs \(4096\) graph vertices, all \(6140\) legal edges, all \(4038\) strongly connected components, and exactly the three cyclic components described in the proof. Its recorded output is `transfer_output.txt`.

Independently, compile `direct_enumeration.cpp` with `g++ -O3 -std=c++17 direct_enumeration.cpp -o verify_direct` and run `./verify_direct`. This program constructs the original eight-neighbor dynamics using cell masks, independently tests every one of the \(2^{3n}\) configurations for each \(n\in\{3,4,5,6,7\}\), and checks the fixed- and two-period populations. Its recorded output is `direct_output.txt`. The brute-force test corroborates the small cases; the universal result rests on the exhaustive finite graph lemma.

## Relationship to prior work

Harold V. McIntosh's chapter *Life's Still Lifes* in *Game of Life Cellular Automata* develops de Bruijn methods for narrow strips, explicitly identifies the \(30\)- and \(27\)-state fixed-point components at width three, and treats the difficulty of general period-two enumeration (Chapter 4, especially pp. 46–49). Those two components are **already established**, and neither their decomposition nor the period-one enumeration is claimed as new. The contribution here is the complete two-time graph reduction: all nonfixed period-dividing-two configurations lie in one additional isolated directed four-cycle, yielding an exact all-circumference oscillation classification. Reia and Kinouchi study mean-field and bulk-density behavior for Life and related outer-totalistic rules, rather than this finite-width exact-period problem.

## Limitations

No statement is made about least periods greater than two, attraction basins or transient lengths, other torus heights, or vertically open strips. The finite graph lemma can be independently reimplemented or manually audited; the included full-enumeration test is bounded and is not by itself an infinite proof. Historical-priority searches did not locate a stronger equivalent exact classification, but an unindexed enumeration remains possible; this is not independent external validation.

## References

1. H. V. McIntosh, “Life's Still Lifes,” Chapter 4 of *Game of Life Cellular Automata*, A. Adamatzky (ed.), Springer, 2010, DOI `10.1007/978-1-84996-217-9` (eBook first released 2010-06-14). The width-three fixed-state analysis is on pp. 46–49.
2. S. M. Reia and O. Kinouchi, “Conway's game of life is a near-critical metastable state in the multiverse of cellular automata,” arXiv:`1407.1006` (first posted 2014-07-03), *Physical Review E* **89**, 052123 (2014).
