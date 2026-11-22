# A two-spare optimum-mobility threshold and a three-spare full-connectivity threshold for geodesic transversals of the four-cube

## Finding
Let \(Q_4\) be the graph on four-bit words, with adjacent words differing in one coordinate. A *geodesic transversal* intersects every inclusion-maximal shortest path. For integer \(b\), let \(\mathcal R_b\) be the graph whose vertices are geodesic transversals \(S\subseteq V(Q_4)\) with \(|S|\le b\); two configurations are adjacent if they differ by adding or deleting exactly one vertex. There is no requirement that intermediate configurations be minimum or inclusion-minimal.

The complete cardinality polynomial and inclusion-minimal-set polynomial are, respectively,
\[
\begin{aligned}
T(z)={}&40z^6+560z^7+2910z^8+5920z^9+6376z^{10}\\
&+4176z^{11}+1820z^{12}+560z^{13}+120z^{14}+16z^{15}+z^{16},\\
M(z)={}&40z^6+160z^7+260z^8.
\end{aligned}
\]
Thus the 16-vertex cube has exactly \(22499\) geodesic transversals, of which \(460\) are inclusion-minimal. The known minimum cardinality is six, and the previously classified forty six-vertex configurations are used as starting states, not presented as a new count.

The connected-component size multisets of the four constrained reconfiguration graphs are exactly
\[
\begin{array}{c|c|c}
b&|V(\mathcal R_b)|&\text{component sizes (with multiplicity)}\\\hline
6&40&1\ (40\text{ times})\\
7&600&1\ (160\text{ times}),\quad11\ (40\text{ times})\\
8&3510&1\ (260\text{ times}),\quad3250\ (1\text{ time})\\
9&9430&9430\ (1\text{ time}).
\end{array}
\]
At budget seven the forty nontrivial components are stars \(K_{1,10}\), each centered on a six-vertex minimum transversal. At budget eight **every pair of minimum transversals is reconfigurable**, while 260 inclusion-minimal eight-vertex transversals remain isolated. Thus two spare vertices are necessary and sufficient to connect all optima, but **three spare vertices are necessary and sufficient to connect every feasible state**. Adding budget levels first increases the number of components \(40,200,261\), before the jump to one at budget nine.

Moreover, in \(\mathcal R_8\), shortest addition/deletion distances among the forty distinct minimum transversals have this exact distribution over the \(\binom{40}{2}=780\) unordered pairs:
\[
\#\{\{S,T\}:d_{\mathcal R_8}(S,T)=j\}=
\begin{cases}
60,&j=4,\\160,&j=6,\\480,&j=8,\\80,&j=12,\\0,&\text{otherwise}.
\end{cases}
\]
In particular their maximum mutual relocation distance is twelve moves. These are **TAR** distances under cardinality at most eight, not one-step token-jumping or token-sliding distances.

## Assumptions and scope
All vertices are explicitly labelled by integers \(0,1,\ldots,15\), read as four-bit binary words. Coordinate \(i\in\{0,1,2,3\}\) flips bit \(2^i\). All graph paths and all reconfiguration states are unweighted. An inclusion-minimal transversal contains no strictly smaller transversal; because feasibility is upward closed, checking all single-vertex deletions is necessary and sufficient for minimality. Every reconfiguration move changes the number of selected vertices by exactly one and must preserve geodesic transversality and the specified cardinality budget. No claim is made for \(Q_d\) with \(d\ne4\), nor for other reconfiguration rules.

## Proof
**1. Reduce to a finite hypergraph.** A shortest path in \(Q_4\) flips no coordinate twice. A path shorter than four can be extended at an endpoint by flipping a coordinate not used on it, without losing geodesicity. Consequently the maximal geodesics are precisely the length-four antipodal paths, obtained by choosing a starting four-bit word and an order of its four coordinate changes. There are \(16\cdot 4!/2=192\) undirected maximal geodesics, each with five vertices. Let \(\mathcal P\) consist of their 192 five-vertex masks. For any vertex mask \(s\in\{0,\ldots,2^{16}-1\}\), the exact feasibility predicate is
\[
F(s)\quad\Longleftrightarrow\quad\forall p\in\mathcal P,\quad (s\mathbin{\&}p)\ne0,
\]
where \(\mathbin{\&}\) means bitwise intersection. This is equivalent to the graph-theoretic definition, not a relaxation or a sampled test.

**2. Exact census and minimality.** Exhaust all integers \(s\in[0,65535]\). For each, test the preceding 192 predicates and increment the coefficient indexed by \(|s|\). The coefficients are those of \(T(z)\), including zero coefficients below degree six. To test whether a feasible \(s\) is inclusion-minimal, check that each \(s\setminus\{v\}\) for \(v\in s\) fails the same predicate. Upward closure proves that no larger proper subset could restore feasibility once all these deletions fail. This yields \(M(z)\). The thirty-two lifted-neighborhood and eight middle-sphere six-set families from the earlier extremizer classification are reconstructed as a cross-check against the forty minima; their discovery or characterization is not claimed here.

**3. Construct complete constrained state graphs.** For each budget \(b\), take every feasible mask satisfying \(|s|\le b\). Two such masks are adjacent if and only if \(s\oplus t\) is a singleton, where \(\oplus\) is symmetric difference. Thus scanning all sixteen bit toggles of every feasible mask constructs every allowed edge **exactly once up to orientation**; there are no other legal moves. Exhaustive breadth-first component searches give the four component multisets in the theorem. Independent union-find checks take every inclusion edge \(s\subset s\cup\{v\}\) within the budget, proving the same partition without sharing the traversal algorithm. The number of states at each budget is independently verified from the cardinality polynomial.

At budget seven, every six-set can only add one of its ten missing vertices. No two distinct six-sets share a seven-set superset: the known explicit two-family classification also yields pairwise intersections of size at most four, and the program verifies this directly. Hence the forty minimum-centered components are stars with ten leaves. The remaining 160 seven-sets are inclusion-minimal and therefore isolated. At budget eight, 260 inclusion-minimal eight-sets are likewise isolated because they cannot delete and cannot add within the budget; the component census verifies that **all other 3250 states are connected**, including all forty minima. At budget nine, the union-find census has a single root for all 9430 states. These exact complete enumerations prove both sharp thresholds. They also show why connectivity of the optimum-containing component is distinct from connectivity of the full feasible-state graph.

**4. Shortest relocation metric.** For every minimum mask \(s\), run a standard unit-edge breadth-first shortest-path search in the complete \(\mathcal R_8\) adjacency relation. Each run reaches precisely the 3250 states of its connected component. Read the distance to each other minimum mask; counting each unordered pair once produces \(60,160,480,80\) at respective distances \(4,6,8,12\). Breadth-first exploration on an explicitly exhaustive unweighted finite graph establishes global shortest paths, not merely observed routes. A separate implementation constructs the maximal paths using graph-distance DFS, reconstructs feasibility, constructs components using union-find, and independently reproduces the pair-distance table.

## Verification
Run both Python 3 standard-library programs from a directory containing `artifacts/`:

```
python3 artifacts/verify_primary.py
python3 artifacts/verify_independent.py
```

The first exhausts 65536 masks, 192 maximal paths, four budget graphs, and forty full breadth-first shortest-path searches; it independently checks that the known forty optimum masks equal the two constructive families. The second instead builds the 192 paths from the graph's adjacency matrix using distance-monotone DFS, enumerates vertex combinations by cardinality, computes components by union-find, and repeats every optimum-distance search. Both programs finish with `VERIFY_PRIMARY_OK` and `VERIFY_INDEPENDENT_OK`, respectively. Exact counts and comparison of algorithmically different implementations are evidence for this **finite** theorem only; no infinite extrapolation or external independent audit is asserted.

## Relationship to prior work
Manuel–Brešar–Klavžar [1] introduced geodesic transversals (also called maximal-shortest-path covers), including the network motivation and hitting-set definition. Their network sequel [2] studies other architectures. Hoang–Suzuki–Yagita [3] study reconfiguration of \(k\)-path vertex covers via addition/removal, but that requirement is to hit **every** path on \(k\) vertices, not the maximal shortest paths in this theorem. Chen–Ma–Wu [4] give hypercube bounds and the known scalar minimum of six in dimension four. Prabha–Sandhiya–Manuel [5] also discuss hypercube transversal numbers. The published forty-minimizer result [6] classifies all six-sets into two orbits; it does not compute inclusion-minimal seven- and eight-sets, constrained TAR components, the two-versus-three spare-vertex distinction, or shortest relocation distances. The present theorem expressly takes its minimizer count and structural families as prior knowledge and supplies the additional reconfiguration and inclusion-minimal data.

Searches of published mathematical records under geodesic transversals, maximal shortest-path covers, antipodal-path hitting sets, hypercube reconfiguration, and token addition/removal did not identify a statement implying this full finite classification. This is evidence from a bounded priority check, not a mathematical proof of global novelty.

## Limitations
The result concerns the labelled, unweighted four-cube only and the addition/removal model with a global size cap. It does not claim robustness to simultaneous failure or a formula for all hypercube dimensions. It uses exhaustive finite computation as a mathematical certificate: source code and independent computation methods are included, but external replication, peer review, and exhaustive publication-priority clearance are not claimed. The published minimum-six result and its two-orbit classification are not original contributions here.

## References
[1] P. Manuel, B. Brešar, S. Klavžar, *The geodesic-transversal problem*, arXiv:2101.08042v1, first public 2021-01-20, https://arxiv.org/abs/2101.08042.

[2] P. Manuel, B. Brešar, S. Klavžar, *The geodesic transversal problem on some networks*, arXiv:2109.09372v1, first public 2021-09-20, https://arxiv.org/abs/2109.09372.

[3] D. A. Hoang, A. Suzuki, T. Yagita, *Reconfiguring k-path vertex covers*, arXiv:1911.03026v1, first public 2019-11-08, https://arxiv.org/abs/1911.03026.

[4] S. Chen, X. Ma, T. Wu, *On two problems concerning the geodesic transversal number of graphs*, arXiv:2610.39298v1, first public 2026-10-29, https://arxiv.org/abs/2610.39298.

[5] R. Prabha, B. Sandhiya, P. Manuel, *Geodesic Transversal of Hypercube and Butterfly networks*, arXiv:2611.06107v1, first public 2026-11-04, https://arxiv.org/abs/2611.06107.

[6] *Forty minimum geodesic transversals of the four-dimensional cube*, published 2026-11-08, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-forty-minimum-geodesic-transversals-of-the-four-dimensional-cube--e937d60d04fd.
