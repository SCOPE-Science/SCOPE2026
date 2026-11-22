# First fractional Hamming-sphere packing gap for single-substitution codes on Dyck words

## Finding

Let \(D_n\) be the set of binary Dyck words of semilength \(n\): each \(w\in D_n\) is a sequence of \(2n\) bits with exactly \(n\) ones and \(n\) zeros, and each initial segment has at least as many ones as zeros. For \(n=1,\ldots,6\), let \(M_n\) be the largest subset \(C\subseteq D_n\) correcting an arbitrary single bit substitution (or no change), where the received word is any binary word. Let \(P_n\) be the fractional packing optimum of the complete radius-one binary Hamming balls centered at \(D_n\), as defined below. Then:

| Semilength \(n\) | \(|D_n|\) | \(M_n\) | \(P_n\) |
|---:|---:|---:|---:|
| 1 | 1 | 1 | 1 |
| 2 | 2 | 1 | 1 |
| 3 | 5 | 2 | 2 |
| 4 | 14 | 4 | 4 |
| 5 | 42 | 10 | 10 |
| 6 | 132 | **22** | **26** |

Thus semilength six is the first strict integrality gap **in this sequence of fractional sphere-packing instances**: \(P_6-M_6=4\) and \(P_6/M_6=13/11\). This result concerns no larger semilengths and does not assert an asymptotic capacity.

## Assumptions and scope

Write \(d_H(u,v)\) for the number of coordinates at which two equal-length binary words differ, and
\[
B_1(w)=\{w\}\cup\{w\oplus e_i:1\le i\le2n\},
\]
where \(e_i\) flips precisely position \(i\). There is no promise that a received word lies in \(D_n\). A code \(C\subseteq D_n\) corrects one substitution exactly when \(B_1(u)\cap B_1(v)=\varnothing\) for distinct \(u,v\in C\).

The natural fractional packing program is
\[
P_n=\max\sum_{w\in D_n}x_w,\qquad
x_w\ge0,\quad\sum_{w\in D_n:\,y\in B_1(w)}x_w\le1
\quad(y\in\{0,1\}^{2n}).
\]
Its covering dual is
\[
P_n=\min\sum_{y\in\{0,1\}^{2n}}z_y,\qquad
z_y\ge0,\quad\sum_{y\in B_1(w)}z_y\ge1
\quad(w\in D_n).
\]
All sums and comparisons in the certificates are exact rational operations; outputs not appearing in any ball may be assigned zero weight.

## Proof

**The distance criterion.** Two radius-one binary Hamming balls intersect if and only if their centers have Hamming distance at most two: a shared output differs from each center in at most one coordinate, and conversely, for centers at distance two the output obtained by changing one of these two coordinates lies in both balls. Every word in \(D_n\) has weight \(n\), hence any pair of its distinct words has even Hamming distance. Therefore a subset \(C\subseteq D_n\) is a correcting code if and only if \(d_H(u,v)\ge4\) for every distinct \(u,v\in C\).

**Finite lower bounds and fractional optimality.** The complete artifact `certificates.json` lists, separately at each \(n\in\{1,2,3,4,5,6\}\), an integer set of distinct Dyck-word bitmasks of cardinality \(1,1,2,4,10,22\). Their pairwise distances are at least four. For each instance the same artifact gives a nonnegative rational primal assignment \(x_w\) and a nonnegative rational dual assignment \(z_y\) whose objectives coincide at \(1,1,2,4,10,26\), respectively. The standalone exact verifier checks every primal inequality over every received word in the union of balls and every dual inequality over every Dyck source word, including signs and objective sums. Weak duality makes the matching primal/dual values the *exact* fractional optima. At semilengths at most five the explicit integer code sizes already equal these fractional upper bounds, proving the stated integer optima.

For \(n=6\), the rational primal certificate has 68 nonzero source weights: forty weights \(1/4\), twenty weights \(1/2\), and eight weights \(3/4\), adding to 26. Its rational dual certificate has 51 nonzero output weights: fifty weights \(1/2\) and one weight 1, also adding to 26. All constraints are checked exhaustively and with exact rational arithmetic in `src/verify_exact.py`.

**The six-pair integer upper bound.** Generate all 132 Dyck sources by the explicit up/down recursion in `src/max_clique.cpp`, and form their compatibility graph \(G\) whose distinct vertices are adjacent exactly when their Hamming distance is at least four. By the distance criterion, \(M_6\) is the clique number of \(G\). The standalone C++17 branch-and-bound implementation visits exactly 3,250,007 recursive search nodes and establishes that its largest clique has size 22. The algorithm enumerates every remaining candidate as a possible next clique vertex; at each node, it greedily colors the candidate graph. Since every clique uses at most one vertex per proper color class, the number of colors gives a rigorous upper bound on any clique extension. Descending-color traversal permits the bound \(\text{current depth}+\text{candidate color}\le\text{incumbent}\) to prune only branches that cannot improve the incumbent. Each branch removes already processed vertices, hence no clique is omitted. The reported maximum is attained by the explicit 22-source witness in `certificates.json`. No random sampling or timeout inference is used in this exhaustive argument.

Consequently \(M_6=22<P_6=26\). At smaller semilengths equality \(M_n=P_n\) has already been proved, giving the first-gap assertion.

## Verification

The bitmask convention is bit zero = first step; a one bit denotes an upward step. The package contains:

- `certificates.json`: complete six-instance source counts, explicit optimal integer codebooks, all rational primal and dual supports, and exact objective values.
- `src/verify_exact.py`: Python standard-library checker of the Dyck enumeration, code witnesses, every rational packing and covering inequality, and exact equality of the primal and dual objectives.
- `src/max_clique.cpp`: stand-alone exhaustive GNU C++17 maximum-clique search giving \(M_6=22\).
- `src/milp_crosscheck.py`: separate source enumeration and integer-programming cross-check using NumPy and SciPy/HiGHS. The latter is corroborative, not the proof of exhaustive optimality.

Reproduce from the artifact directory with `python3 src/verify_exact.py`, `g++ -O3 -std=gnu++17 src/max_clique.cpp -o max_clique && ./max_clique 6`, and, with NumPy and SciPy available, `python3 src/milp_crosscheck.py`. Required results include `EXACT_ALL_OK`, `MAX 22` with `NODES 3250007`, and `MILP_ALL_OK`. The exact certificate checker and the full exhaustive search are the mathematical dependencies; the separate MILP computation is an additional numerical consistency check.

## Relationship to prior work

Ardila's *The Catalan matroid* establishes that the up-step position sets of Dyck paths are the bases of a matroid. Hence our confusability graph can also be described as the one-element basis-exchange graph (the induced Johnson adjacency graph) on these bases. This known equivalence supplies a natural interpretation, not the computed Hamming-code optimum or fractional gap. Cohen, Tetali and Yeliussizov examine random walks and fast mixing on lattice-path-matroid bases, not maximum error-correcting independent sets or fractional sphere packing. Mütze, Standke and Wiechert consider Gray-order generation via local changes, not maximally separated selections. Yazdi, Kiah and Milenkovic use Dyck paths as ingredients of balanced weakly mutually uncorrelated codes, but their inspected construction does not supply the present full-source finite optimum/dual-gap pair. Searches for Dyck single-substitution codes, Catalan-matroid independence packing, and equivalent Johnson-graph formulations did not uncover a covering result. The standard unrestricted constant-weight-code tables concern all balanced 12-bit words and list at least 132 words at distance four for the corresponding parameters; this does not bound an optimal code contained in the much smaller Dyck subset. Absence from searches is not a proof of historical priority.

## Limitations

The exact integer and rational bounds are proved only for semilengths one through six, and the 22-codeword optimum refers to the **entire** Dyck-word source alphabet at semilength six with a **full binary one-substitution received alphabet**. No all-length recurrence, asymptotic statement, maximum-codebook census, or stream-synchronization property is proved. Historical priority can be affected by unindexed calculations or inaccessible related texts. Independent mathematical audit has not been performed.

## References

1. Federico Ardila, *The Catalan matroid*, first public arXiv version 2002-09-25, https://arxiv.org/abs/math/0209354 .
2. Emma Cohen, Prasad Tetali, Damir Yeliussizov, *Lattice Path Matroids: Negative Correlation and Fast Mixing*, first public arXiv version 2015-05-25, https://arxiv.org/abs/1505.06710 .
3. Torsten Mütze, Christoph Standke, Veit Wiechert, *A minimum-change version of the Chung-Feller theorem for Dyck paths*, first public arXiv version 2016-03-08, https://arxiv.org/abs/1603.02525 .
4. S. M. Hossein Tabatabaei Yazdi, Han Mao Kiah, Olgica Milenkovic, *Weakly Mutually Uncorrelated Codes*, first public arXiv version 2016-01-29, https://arxiv.org/abs/1601.08176 .
5. Andries Brouwer, *Bounds for constant weight codes*, online table for \(A(12,4,6)\), https://aeb.win.tue.nl/codes/Andw.html .
