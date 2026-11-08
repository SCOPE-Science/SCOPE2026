# Sharp Fibonacci capacity and canonical window set for doubly run-limited de Bruijn cycles

## Finding
For every integer \(n\ge4\), let \(L_n\) be the largest length of a nonempty circular binary word \(c\) satisfying both conditions:

1. No three cyclically consecutive letters of \(c\) are equal (both \(000\) and \(111\) are forbidden, including across the circular boundary).
2. Its \(|c|\) cyclic length-\(n\) windows are pairwise distinct (the starting positions, not just the distinct rotations, are indexed).

With Fibonacci numbers \(F_0=0,F_1=1,F_{j+2}=F_{j+1}+F_j\), the exact extremal length is
\[
L_n=2(F_{n+1}-F_{n-3})=2(F_n+F_{n-2}).
\]
There is a stronger rigidity assertion: *every* length-\(L_n\) maximizer has precisely the same window set
\[
\mathcal R_n=\{w\in\{0,1\}^n:\ w\text{ contains neither }000\text{ nor }111,\ 
\neg[(w_1=w_2)\wedge(w_{n-1}=w_n)]\}.
\]
Conversely, an Euler circuit of the length-\(n\) overlap graph restricted to \(\mathcal R_n\) produces a maximizer, and every maximizer traverses every edge in \(\mathcal R_n\) once.

For \(n=4,5,6,7,8\) the optimum lengths are \(8,14,22,36,58\), respectively.

## Assumptions and scope
Words are indexed binary sequences. A cyclic length-\(n\) window of a circular word \(c=c_0\cdots c_{m-1}\) is \(c_i c_{i+1}\cdots c_{i+n-1}\), with indices reduced modulo \(m\). The no-triple restriction is cyclic and applies even when \(m<n\). The optimum takes the maximum over every positive circular length. Rotation-equivalent maximizers are not counted; only their *common window set* is determined. Both symbols are subject to the run bound; this is not the one-sided zero-run constraint.

## Proof
**1. Window graph and Fibonacci edge count.** Let \(G_n\) have all binary length-\((n-1)\) words avoiding \(000\) and \(111\) as vertices, and all length-\(n\) words avoiding these triples as directed edges, from their length-\((n-1)\) prefix to their corresponding suffix. Every admissible word can be read as its first bit followed by a composition into runs of lengths one or two. Hence its length-\(n\) count is \(2F_{n+1}\).

For an admissible vertex \(v=v_1\cdots v_{n-1}\), the indegree and outdegree are
\[
\deg^-(v)=2-\mathbf 1\{v_1=v_2\},\qquad
\deg^+(v)=2-\mathbf 1\{v_{n-2}=v_{n-1}\}.
\]
Thus \(\deg^+(v)-\deg^-(v)=1\) precisely when the first two bits agree but the last two differ; denote the set of such vertices by \(P\). Starting with one doubled run, ending with a singleton run, and choosing intermediate run lengths corresponds to a composition of \(n-4\) into parts of size one or two. There are \(F_{n-3}\) such compositions (including the empty composition when \(n=4\)), with either choice of starting symbol. Therefore \(|P|=2F_{n-3}\).

**2. Sharp upper bound.** Any candidate circular word with pairwise distinct length-\(n\) windows traces a closed directed trail with no repeated edge in \(G_n\). Its selected edges have equal indegree and outdegree at every vertex. At each \(v\in P\), the full graph has one more outgoing than incoming edge, so at least one outgoing edge must be omitted. Different vertices have disjoint outgoing edge sets. Thus the trail uses no more than
\[
|E(G_n)|-|P|=2(F_{n+1}-F_{n-3})
\]
edges, proving the claimed upper bound.

**3. A uniquely forced balancing deletion.** Let \(D_n\) comprise the admissible length-\(n\) words whose first two and last two bits each agree. Every \(v\in P\) has exactly one outgoing edge in \(D_n\): append to \(v\) a copy of its last bit. That edge arrives at a vertex with negative imbalance (initial bits unequal and terminal bits equal). Every negative-imbalance vertex has exactly one incoming edge from \(D_n\): prepend a copy of its first bit. Consequently deleting all \(D_n\)-edges makes the graph balanced, and \(|D_n|=|P|\). The retained edges are precisely \(\mathcal R_n\).

**4. Strong connectivity of the balanced graph.** From any vertex, repeatedly append the complement of its current last bit. The resulting edges always finish with two unequal symbols, so none belongs to \(D_n\). After \(n-1\) steps this reaches one of the two alternating length-\((n-1)\) vertices. Those two vertices communicate via the same alternating extensions. From an alternating vertex whose final symbol differs from the first bit of any desired admissible vertex \(v\), append the \(n-1\) bits of \(v\), in order. All traversed edges start with two unequal symbols: until the initial alternating symbols have been shifted out this is immediate, and at the last step it uses the chosen difference at the junction. Thus none is deleted; neither does any step introduce a triple, since the junction has unequal symbols and \(v\) itself is admissible. The final vertex is \(v\). Therefore all vertices are mutually reachable via retained edges. The finite balanced strongly connected directed graph has an Euler circuit, giving a circular word with exactly \(|\mathcal R_n|\) distinct windows and no cyclic triple.

**5. Rigidity of the entire maximum window set.** Equality in Step 2 permits exactly \(|P|\) deleted edges. Every positive-imbalance vertex must delete one outgoing edge, leaving no deletions from any other vertex. The two outgoing edges of a positive vertex append either its last symbol or its opposite. The opposite-symbol edge reaches a zero-imbalance vertex: its initial and terminal adjacent pairs both differ. Deleting an incoming edge there, with no outgoing edge deleted there, contradicts balanced selected degrees. Thus every positive vertex must delete its same-symbol edge, exactly the unique edge of \(D_n\). No other edge is omitted, establishing the canonical window-set theorem.

## Verification
The accompanying `verify.py` uses only Python 3 standard-library modules. It regenerates all admissible length-\(n\) windows, independently calculates their imbalance, checks the retained subgraph's balance and strong connectivity, produces an Euler tour, and verifies its actual cyclic length-\(n\) windows for every \(3\le n\le16\). For \(n=4,5\), it also exhaustively checks all circular binary strings up to the total number of admissible length-\(n\) edges, both for optimality and for the asserted uniqueness of the window set. Run `python3 verify.py` in a directory containing the file. The infinite theorem is established by Steps 1–5, not inferred from finite experiments.

## Relationship to prior work
Sawada, Williams and Wong (2016) construct universal cycles for specified rotation-closed languages using generalized greedy and necklace approaches. The canonical edge set \(\mathcal R_n\) in this result need not be rotation-closed: for example, with \(n=4\), the permitted window \(0010\) has a rotation \(1000\) violating the no-triple constraint. Thus their rotation-closed universal-cycle theorem does not imply this exact maximum and rigidity statement.

Chee and coauthors (2024) study maximum-length run-length-limited sequences in de Bruijn graphs with a one-sided bound on consecutive zeros. The present two-sided constraint excludes both \(000\) and \(111\) and requires an explicitly balanced proper subset of the linearly admissible edges. The all-length exact two-sided capacity and uniqueness assertion are not statements of the inspected source. The general cut-down de Bruijn framework concerns repetition-free windows without this double run constraint, and therefore does not itself compute this constrained optimum.

## Limitations
The theorem is restricted to a binary alphabet, the run-length cap two for both symbols, and all orders \(n\ge4\). It does not enumerate distinct Euler tours/maximizers, obtain a shortest universal cycle for a rotation-closed prescribed language, or solve asymmetric higher run caps. Exhaustive computations cover only finite lengths; the proof supplies the infinite result. An unindexed equivalent historical treatment may exist; no claim of independent external validation is made.

## References
- J. Sawada, A. Williams, D. Wong, *Generalizing the Classic Greedy and Necklace Constructions of de Bruijn Sequences and Universal Cycles*, Electronic Journal of Combinatorics 23(1), P1.24 (publicly available 2016-02-05). https://doi.org/10.37236/5517
- Y. M. Chee, T. Etzion, T. L. Nguyen, D. H. Ta, V. D. Tran, V. K. Vu, *Maximum Length RLL Sequences in de Bruijn Graph* (first public arXiv version 2024-03-03). https://arxiv.org/abs/2403.01454
- *Cut-down de Bruijn sequences*, De Bruijn Sequences and Universal Cycles reference, https://debruijnsequence.org/db/cutdown (background on repetition-free cyclic window sequences).
