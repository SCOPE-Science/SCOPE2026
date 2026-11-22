# The full edge-query shattering polynomial of ladder perfect matchings

## Finding
For each integer \(n\ge 1\), let \(L_n=P_2\square P_n\) be the two-row ladder with \(n\) columns. Let \(\mathcal P_n\) contain the edge-incidence vectors of **all graph-theoretic perfect matchings** of \(L_n\). The Boolean query at a physical edge asks whether that edge belongs to an unknown matching. Let \(\Phi_n(z)\) count the sets of **distinct physical edges** shattered by these queries, by support size, with \(\Phi_0(z)=1\) as the empty-board convention.

The complete all-width shattering polynomial is
\[
\boxed{\sum_{n\ge 0}\Phi_n(z)t^n=\frac{1}{1-t-4zt^2+zt^3}.}
\]
Equivalently, for every \(n\ge0\), the coefficient of \(z^k\), for \(0\le k\le\lfloor n/2\rfloor\), is exactly
\[
\boxed{[z^k]\Phi_n(z)=\sum_{r=0}^{k}\binom{k}{r}3^r\binom{n-2k+r}{r},}
\]
and is zero for larger \(k\). Therefore the leading coefficient equals \(4^m\) for \(n=2m\), and \((3m+4)4^{m-1}\) for \(n=2m+1\), \(m\ge1\). The shattered-support complex is not always pure: at \(n=6\) there are maximal shattered supports of cardinalities two and three, including a maximal two-edge support consisting of the rungs at columns three and four. The scalar VC dimension \(\lfloor n/2\rfloor\) was previously known; the claim here is the complete face enumerator, individual-support classification, and nonpurity.

## Assumptions and scope
All graphs are finite and simple. The ladder has vertices \(u_i,w_i\), for \(1\le i\le n\), rung edges \(v_i=u_iw_i\), and separate top and bottom horizontal edges \(a_i=u_iu_{i+1}\), \(b_i=w_iw_{i+1}\), for \(1\le i<n\). Although \(a_i\) and \(b_i\) always have equal outcomes, they are **different physical queries** and count separately in \(\Phi_n\). A support \(S\) is shattered when every function \(S\to\{0,1\}\) is induced by some perfect matching. An empty support is shattered. No duplicate edge queries occur in a support.

For any proposed support \(S\), let \(H\subseteq\{1,\dots,n-1\}\) be the set of positions at which one of the two horizontal edges is queried. The support is shattered **if and only if** all of the following hold:

1. At most one of \(a_i,b_i\) is queried for each cut \(i\); no two positions of \(H\) are consecutive.
2. No queried rung has a column in \(\bigcup_{i\in H}\{i,i+1\}\).
3. Delete the columns in that union from the column path, leaving disjoint intervals. Within each such interval, the queried rung columns admit a matching to **distinct adjacent unqueried columns**. Equivalently, the binary indicator of queried rungs in that interval has **no maximal alternating run of odd length whose first and last symbols are both one**.

These conditions determine every shattered support, including those containing horizontal queries.

## Proof
**Step 1: Perfect matchings are column tilings.** Consider a vertical cut between columns \(i\) and \(i+1\). The prefix of \(2i\) vertices is matched across the cut by an even number of edges. Exactly two physical horizontal edges cross the cut, so both or neither occur. Thus every perfect matching is uniquely a tiling of the column interval with single-column tiles (a rung \(v_i\)) or double-column tiles (both \(a_i,b_i\)). It follows that \(a_i\) and \(b_i\) are equivalent queries. If both lie in a support, the assignments \((0,1)\) and \((1,0)\) are impossible. If selected horizontal positions touch, their all-one assignment is impossible. The rung at a selected horizontal position's endpoint cannot simultaneously be one, establishing necessary conditions 1–2.

**Step 2: Exact rung-only shattering criterion.** Consider a column interval and query only a set \(Q\) of rung positions. A rung is absent precisely if its column is covered by one of the adjacent two-column tiles. We claim that the rung-support \(Q\) is shattered exactly when the path graph on the interval contains a matching saturating \(Q\) with distinct neighbors outside \(Q\).

For sufficiency, fix such a matching between \(Q\) and unqueried columns. For any binary labeling of \(Q\), place a two-column tile on the partner edge when the queried rung is labeled zero; when it is labeled one, place two single-column rung tiles instead. Fill every other column by a single-column tile. Partner edges are disjoint, so all these decisions coexist.

For necessity, split the zero-one indicator of \(Q\) into its unique maximal alternating runs (successive symbols alternate within a run, while neighboring runs are joined by two equal adjacent symbols). If a run is odd-length and begins and ends in one, it contains \(q+1\) queried columns and only \(q\) unqueried columns. Prescribe value zero for every queried rung in that run and value one for every queried rung elsewhere. The two endpoints have no available unqueried neighbor outside the run: an outside neighbor, if present, is a queried rung prescribed one because the alternating run is maximal. The \(q+1\) zero-rung columns would need disjoint horizontal dimer partners among only \(q\) unqueried columns, a contradiction. Conversely, if there is no such run, each maximal alternating run has at least as many zeros as ones. Matching successive alternating pairs inside each run saturates all its one-positions and uses distinct zero-positions. Joining these independent matchings gives the required external-neighbor matching. This proves both the matching and forbidden-alternating-run criteria.

**Step 3: Supports with horizontal queries.** Assign value one to all selected horizontal queries, forcing their mutually disjoint two-column tiles. Necessity of condition 3 follows by requiring all possible rung labels in the remaining intervals. Conversely, given conditions 1–3, choose independent matching partners for all queried rung columns in the residual intervals by Step 2. For each selected horizontal edge, use the corresponding double-column tile if its requested label is one, or two single-column tiles otherwise. For each queried rung, use its chosen partner tile if its requested label is zero, or two single-column tiles otherwise. The selected patches occupy disjoint pairs of columns; fill uncovered columns with rung tiles. This realizes every labeling, proving the classification.

**Step 4: Enumerate rung-only supports.** Write \(R_n(z)\) for the polynomial of shattered supports using only \(n\) rung positions and \(R_0(z)=1\). Every binary rung-indicator word has a unique decomposition into maximal alternating runs. The allowable run types, indexed by initial and final symbols, have generating functions (\(t\) for columns, \(z\) for selected rungs)
\[
A_{00}=\frac{t}{1-zt^2},\qquad
A_{01}=A_{10}=\frac{zt^2}{1-zt^2},\qquad A_{11}=0.
\]
The prohibited case is precisely an odd alternating run with both endpoints one. Adjacent runs meet at **equal** symbols, so with \(A=(A_{ij})_{i,j\in\{0,1\}}\), the unique run decomposition gives
\[
R(t,z)=\sum_{n\ge0}R_n(z)t^n
=1+\begin{pmatrix}1&1\end{pmatrix}A(I-A)^{-1}\binom11
=\frac{1}{1-t-2zt^2+zt^3}.
\]
This is an ordinary formal-power-series identity: every entry of \(A\) has positive \(t\)-valuation, so \((I-A)^{-1}\) exists formally.

**Step 5: Insert distinct physical horizontal queries.** Each selected horizontal position contributes two columns, one query (weight \(z\)), and an independent choice of top or bottom physical edge (multiplicity two). Between successive selected positions and at both ends there is an unrestricted residual interval, whose rung-support generating series is \(R(t,z)\). By Step 3 this decomposition is bijective. Summing over the number of selected horizontal positions,
\[
\sum_{n\ge0}\Phi_n(z)t^n
=R(t,z)\sum_{h\ge0}\bigl(2zt^2R(t,z)\bigr)^h
=\frac{R(t,z)}{1-2zt^2R(t,z)}
=\frac{1}{1-t-4zt^2+zt^3}.
\]

**Step 6: Exact coefficients, extreme counts, and nonpurity.** Expand the denominator as
\[
\frac{1}{1-t-zt^2(4-t)}
=\sum_{k\ge0}z^kt^{2k}\frac{(4-t)^k}{(1-t)^{k+1}}
=\sum_{k\ge0}z^kt^{2k}\sum_{r=0}^{k}\binom{k}{r}3^r(1-t)^{-r-1}.
\]
Since \([t^j](1-t)^{-r-1}=\binom{j+r}{r}\) for nonnegative \(j\), the claimed coefficient sum follows exactly. Its \(k\)-th coefficient is strictly positive iff \(n\ge2k\), so the dimension is \(\lfloor n/2\rfloor\), consistent with prior work. Setting \(n=2m\) leaves only \(r=0,\dots,m\) with each binomial \(\binom r r=1\), giving \(4^m\). At \(n=2m+1\) the binomial is \(r+1\); summing yields \((3m+4)4^{m-1}\) for \(m\ge1\). For \(n=6\), the polynomial is \(1+16z+73z^2+64z^3\). The support \(\{v_3,v_4\}\) satisfies the characterization but cannot be enlarged by any rung or horizontal edge (inspect the three conditions), while there exist shattered three-edge supports; thus the complex is nonpure.

## Verification
The included standalone `full_checker.py` independently constructs the full \(2n\)-vertex ladder as a graph, enumerates graph-theoretic perfect matchings by vertex pairing rather than by the column-tiling recurrence, and compares direct shattering of every physical support with the structural characterization for \(1\le n\le6\). For \(7\le n\le9\), it exhaustively checks every support in the quotient query universe consisting of rungs and one representative per horizontal cut. This checks 246,930 support instances in total. Separately, the checker verifies every closed coefficient from the rational recurrence through \(n=100\), and detects inclusion-maximal faces of sizes two and three at \(n=6\). Run `python3 full_checker.py`; the included `full_checker_output.txt` records actual reproduced output. The proof for arbitrary \(n\) is Steps 1–6, not inference from finite tests.

## Relationship to prior work
Johnson's 2021 work on VC complexity of binary strings studies translate traces of a single infinite string. It motivates binary-string VC analysis, but its objects and theorems do not provide edge-query shattered-support enumerators for families of finite ladder matchings. The prior exact VC-dimension and online-learning result for **the same ladder perfect-matching concepts** establishes \(\lfloor n/2\rfloor\) and an adaptive/static gap, and also uses the column-tile equivalence; those statements are expressly credited. Its theorems do not determine which mixed physical edge supports are shattered, any complete face coefficients, or nonpurity. Tratnik and Ye study resonance graphs, hypercube embeddings and Clar/cube polynomials of perfect matchings; their cube polynomial counts induced cubes in a *different graph* and is not this support enumerator. Related perfect-matching, partition, and regular-language results were compared for stronger implications; none of the inspected statements yielded the present full polynomial. This comparison supports a bounded originality assessment, not proof of exhaustive worldwide priority.

## Limitations
The theorem concerns ordinary **open** two-row ladder graphs and Boolean queries of individual original physical edges, not cyclic ladders, arbitrary grid widths, matching-size distributions or resonance-graph cube counts. The finite checker validates small instances and symbolic consequences, not historical originality or infinite proofs. The coefficient formula does not supply the complete multivariate distribution by edge type, and no closed form for the number of inclusion-maximal supports at every individual size is claimed. Independent mathematical validation and comprehensive historical-priority review have not been performed.

## References
- H. R. Johnson, *Binary strings of finite VC dimension*, arXiv:2101.06490, first public 2021-01-16, MSC 03C45, https://arxiv.org/abs/2101.06490.
- *Exact VC dimension and linear online shattering gap for matching-covered ladders*, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-exact-vc-dimension-and-linear-online-shattering-gap-for-matching--c420d89cdd55 (previously established scalar dimension and tiling structure).
- N. Tratnik and D. Ye, *Resonance Graphs and Perfect Matchings of Graphs on Surfaces*, arXiv:1710.00761, first public 2017-10-02, https://arxiv.org/abs/1710.00761.
