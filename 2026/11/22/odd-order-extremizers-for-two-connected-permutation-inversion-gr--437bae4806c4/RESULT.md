# Odd-order extremizers for two-connected permutation inversion graphs

## Finding
Let \(m\ge 1\) be an integer, let \(n=2m+1\), and let \(G_\pi\) be the inversion graph of \(\pi\in S_n\). Among permutations whose inversion graph is two-vertex-connected, the **minimum inversion count** is \(3m\), and the **number attaining it** is exactly \(3m-2\). Of these, exactly \(m\) permutations contain a single occurrence of the pattern \(321\); the other \(2m-2\) avoid \(321\).

There is also a complete constructive classification. For \(m\ge2\), all minimizers, without repetitions, are obtained by inserting one point of inversion-graph degree exactly two into the unique even-order extremizer \(L_{2m}\). The even extremizers are defined by \(L_4=3412\) and \(L_{r+2}=F(L_r)\) for even \(r\ge4\), where \(F\) increments the largest entry of a permutation of length \(r\), inserts the new largest entry \(r+2\) immediately before its final entry, and appends \(r\). In particular, \(L_6=351624\), \(L_8=35172846\). At \(m=1\), the sole minimizer is \(321\).

## Assumptions and scope
We use position-labelled inversion graphs: \(i,j\) are joined when \(i<j\) and \(\pi_i>\pi_j\). Two-vertex-connected means at least three vertices, connected after deletion of any one vertex. A triangle in this graph is exactly an occurrence of the decreasing pattern \(321\).

For a permutation \(a\) of length \(r\), write \(I_{p,v}(a)\) for the permutation of length \(r+1\) obtained by adding a new entry of rank \(v\) after precisely \(p\) old entries, where \(0\le p\le r\) and \(1\le v\le r+1\), increasing each old entry at least \(v\) by one. Its new vertex has degree
\[
\delta_a(p,v)=\#\{i\le p:a_i\ge v\}+\#\{i>p:a_i<v\}.
\]
No claims are made about two-connectivity of permutations other than the stated extremal layer.

## Proof
**Lower bound and constructions.** Inversion graphs are \(4\)-chordal, and the published two-connected \(4\)-chordal bound is \(|E(G)|\ge 3|V(G)|/2-2\) [1, Proposition 2.8]. For \(n=2m+1\), integrality gives at least \(3m\) inversions. The same paper [1, Remark 3.6] characterizes the unique even extremizer \(L_{2m}\) for \(m\ge2\), with \(3m-2\) edges. Inserting a vertex with two distinct neighbors into a two-connected graph preserves two-connectivity (after deleting the inserted vertex the original is connected; after deleting an old vertex the inserted vertex still attaches to a surviving old neighbor). Thus every \(I_{p,v}(L_{2m})\) satisfying \(\delta_{L_{2m}}(p,v)=2\) is an odd extremizer with \(3m\) edges.

**Converse by extremal ear decompositions.** By [1, Lemmas 2.3, 3.3], any two-connected inversion graph has an anchored induced ear decomposition starting with a triangle or induced square. Each later step adds either one vertex and at least two edges, or two vertices and at least three edges. If the initial cycle is a triangle, let \(a,b\) count the two-vertex and one-vertex steps. Then \(2a+b=2m-2\), and the edge count is at least \(3+3a+2b=3m+b/2\). Equality forces \(b=0\). If the initial cycle is a square, \(2a+b=2m-3\) and the edge count is at least \(4+3a+2b=3m+(b-1)/2\); since \(b\) is positive and odd, equality forces \(b=1\). In either case every step has its minimum possible edge increment.

The final step is therefore either a one-vertex addition to a minimum even-order graph, necessarily \(L_{2m}\), or a two-vertex induced ear on a minimum odd-order graph of length \(2m-1\). The anchored two-vertex ear has a **unique** permutation insertion position: one new vertex becomes topmost and third from the right, the other becomes rightmost and third from the top [1, Lemma 3.5]. This is exactly the operation \(F\). At order five, the triangle-start possibility is \(F(321)=42513=I_{1,2}(L_4)\), while the square-start possibility is already a degree-two insertion into \(L_4\).

To complete induction, let \(r\ge4\) be even and suppose \(\delta_{L_r}(p,v)=2\). Directly from the definitions of insertion and \(F\), the following exhaustive commutation identities hold:
\[
F(I_{p,v}(L_r))=
\begin{cases}
 I_{p,v}(L_{r+2}),&p<r,\ v\le r,\\
 I_{r-3,r}(L_{r+2}),&(p,v)=(r-2,r+1),\\
 I_{r-1,r-2}(L_{r+2}),&(p,v)=(r,r-1).
\end{cases}
\]
The only degree-two cells outside the first case are the two displayed exceptional cells. The identities can be checked by replacing \(L_{r+2}\) with the recursive definition, tracking the old maximum and final entry in the last two cases. Consequently every two-vertex-ear extension of a previously classified odd extremizer is also a degree-two insertion into the next even ladder. This proves the constructive classification for every \(m\ge2\).

**Exact census.** Let \(r=2m\ge6\). A direct calculation from the recursive even-ladder word gives exactly the following cells with \(\delta_{L_r}(p,v)=2\):
\[
\begin{gathered}
(0,3),(1,2),(1,4),(2,1),\\
(2j+1,2j),(2j+1,2j+2),(2j+1,2j+4)
\quad(1\le j\le m-2),\\
(r-2,r+1),(r-1,r-2),(r-1,r),(r,r-1).
\end{gathered}
\]
The table follows by counting entries larger than \(v-1\) to the left and entries smaller than \(v\) to the right; the recursive ladder has initial word \(3,5,1\), alternating internal entries \(7,2,9,4,11,6,\ldots\), and terminal entries \(r,r-4,r-2\). There are \(3m+2\) cells. Distinct cells give the same inserted permutation only when the inserted point and a pre-existing point lie in a common adjacent consecutive-value run, allowing either to be deleted to recover \(L_r\). Since \(L_r\) has no adjacent consecutive-value pair for \(r\ge6\), the only duplicate pairs are
\[
\begin{aligned}
(0,3)&\sim(1,4),& (1,2)&\sim(2,1),\\
(r-3,r)&\sim(r-2,r+1),& (r-1,r-2)&\sim(r,r-1).
\end{aligned}
\]
Therefore the number of distinct permutations is \(3m+2-4=3m-2\). At \(r=4\), direct evaluation gives eight cells and exactly four distinct insertions: two groups of three equivalent cells and two singleton cells. The same total follows.

The ladder graph is triangle-free. A new vertex with exactly two neighbors creates one triangle if and only if those neighbors are adjacent, and never more than one. Among the displayed cells this happens exactly at \((p,v)=(2j-1,2j)\) for \(1\le j\le m\), which are distinct after duplicate-cell identifications. This yields exactly \(m\) permutations containing one \(321\), and \((3m-2)-m=2m-2\) avoiding \(321\). At \(m=1\), \(321\) has three inversions and is the unique two-connected permutation of length three.

## Verification
Run \(\texttt{python3 verify.py}\) using Python 3.10 or later. It enumerates all permutations at odd lengths three, five, seven, and nine and checks the exact extremal family and triangle counts. It separately checks even uniqueness through length eight, the complete degree-two insertion-cell table through length fifty, and both exceptional commutation identities at each tested length. Its expected terminal marker is \(\texttt{VERIFY_OK}\). The full unbounded theorem follows from the proof above, not from finite enumeration.

## Relationship to prior work
Verkama [1] establishes the sharp two-connected \(4\)-chordal edge bound, anchored ear lemmas, and uniqueness of the even-order extremal inversion permutation (Remark 3.6). Its Table 1 counts all permutations by vertex connectivity for orders up to seven, not the minimum-inversion stratum at every odd order. The result here supplies the odd-order insertion classification and its all-order enumeration. Tenner and Vatter [2] study a different inversion-graph statistic (cyclomatic number and reduced words); no covering odd-extremizer census was identified from its accessible abstract.

## Limitations
Historical priority has not been independently established; equivalent results may be unindexed or expressed in different terminology. The derivation uses the published chordality and anchored-ear results from [1], rather than reproving their general forms. Only small orders are checked exhaustively by code. No claim is made about extremizers for higher vertex-connectivity, other inversion counts, or optimization under pattern avoidance.

## References
[1] E. Verkama, *Permutation patterns and higher connectivity in inversion graphs*, arXiv:2611.17237v1, first posted November 12, 2026, https://arxiv.org/abs/2611.17237 . In particular Proposition 2.8, Lemmas 3.3 and 3.5, and Remark 3.6.

[2] B. E. Tenner and V. Vatter, *Cyclomatic numbers and permutations*, arXiv:2607.06198, first posted July 7, 2026, https://arxiv.org/abs/2607.06198 .
