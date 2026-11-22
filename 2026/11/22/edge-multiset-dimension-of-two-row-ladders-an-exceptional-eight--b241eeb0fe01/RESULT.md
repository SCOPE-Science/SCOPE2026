# Edge-multiset dimension of two-row ladders: an exceptional eight-column obstruction

## Finding

Let \(L_n=P_n\square K_2\) be the two-row, \(n\)-column ladder, where \(n\ge2\). For an edge \(e=uv\) and a vertex \(x\), let \(d(x,e)=\min\{d(x,u),d(x,v)\}\). For a landmark set \(S\subseteq V(L_n)\), the *edge-multiset signature* of \(e\) is the multiset \(\{d(s,e):s\in S\}\), including multiplicity but not landmark order. A set resolves edges if distinct edges have distinct signatures. Write \(\operatorname{md}_e(G)=\infty\) if no resolving landmark set exists.

**Theorem.** For every integer \(n\ge2\),
\[
\operatorname{md}_e(L_n)=
\begin{cases}
\infty,&2\le n\le4,\\
4,&n\in\{5,6,8\},\\
3,&n=7\text{ or }n\ge9.
\end{cases}
\]
There are exactly \(4\), \(20\), and \(80\) four-vertex bases of \(L_5,L_6,L_8\), respectively. In particular, the graph invariant does **not** vary monotonically with the number of columns: three landmarks suffice at seven columns but not at eight, and suffice again from nine columns onward.

## Assumptions and scope

All graphs are finite, simple, unweighted, and connected. Label vertices \((t,r)\), with columns \(0\le t\le n-1\) and rails \(r\in\{0,1\}\). Adjacent vertices differ by one in exactly one coordinate. Let \(N=n-1\). Three classes of edges are the rungs \(R_t=(t,0)(t,1)\), \(0\le t\le N\), and the two rail edges \(H_t=(t,0)(t+1,0)\) and \(B_t=(t,1)(t+1,1)\), \(0\le t<N\). A basis is a resolving set of minimum size. All bases are counted as unordered subsets of the \(2n\) labelled vertices.

The certificate cases for \(n=2,3,4\) check **all** possible subsets, including larger subsets. Such checks are necessary because edge-multiset resolvability is not assumed to be preserved by adding landmarks.

## Proof

**1. Two landmarks never suffice.** A single vertex cannot resolve the ladder: at least two edges incident to it have signature \(\{0\}\). For two distinct landmarks \(a,b\), let \(d(a,b)=\ell\). If \(\ell\ge2\), the first and last edges of any chosen shortest \(a\)-\(b\) path are distinct, and each has multiset signature \(\{0,\ell-1\}\). If \(\ell=1\), each of \(a,b\) has an incident edge other than \(ab\), because the minimum degree of the ladder is two. Those two edges are distinct and both have signature \(\{0,1\}\). Hence no set of at most two vertices resolves any \(L_n\).

**2. Uniform three-landmark construction for all but the finite exceptional cases.** Suppose first that \(n\ge7\) is odd, so \(N\ge6\) is even. Select the three top-rail landmarks at columns \(\{0,2,N\}\). Suppose alternatively that \(n\ge10\) is even, so \(N\ge9\) is odd. Select those at columns \(\{0,3,N\}\). Write \(j=2\) in the first case and \(j=3\) in the second. For an edge, let its signature be presented as an unordered triple.

Directly from path distances, for \(0\le t<j\), the rung, top edge, and bottom edge signatures are respectively
\[
R_t:\{t,j-t,N-t\},\qquad
H_t:\{t,j-t-1,N-t-1\},\qquad
B_t:\{t+1,j-t,N-t\}.
\]
For \(j\le t\le N\) (with \(H_t,B_t\) only for \(t<N\)), they are
\[
R_t:\{t,t-j,N-t\},\qquad
H_t:\{t,t-j,N-t-1\},\qquad
B_t:\{t+1,t-j+1,N-t\}.
\]
All these formulas specify nonnegative integers; there are \(N+1\) rungs and \(N\) edges in each rail.

First compare edges at columns \(t\ge j\). Each signature has the form
\[
\{q-j,q,N-q+c\},
\]
where \((q,c)=(t,0)\) for a rung, \((t,-1)\) for a top edge, and \((t+1,1)\) for a bottom edge. The map from edge to \((q,c)\) is injective. If two equal signatures have the same distinguished pair \(\{q-j,q\}\), their \(q\) and \(c\) are equal. Otherwise, their common triple must have two distinct pairs of entries with difference \(j\), and thus must be an arithmetic progression of step \(j\). Relabel the two edges to make their distinguished upper pair members \(q\) and \(q+j\). The third entry of the first signature must be \(q+j\), and the third entry of the second must be \(q-j\). These equations are
\[
N-q+c=q+j,\qquad N-(q+j)+c'=q-j,
\]
which imply \(c'=c-j\) and \(2q=N+c-j\). Since \(c,c'\in\{-1,0,1\}\), for \(j=3\) the first equation is impossible. For \(j=2\), it requires \((c,c')=(1,-1)\), and then \(2q=N-1\), impossible because \(N\) is even. Thus all signatures in this right-hand region are distinct.

There are only \(3j\) signatures in the initial region \(t<j\). When \(j=2\) and even \(N\ge6\), they are
\[
\begin{array}{c|cccccc}
 &R_0&R_1&H_0&H_1&B_0&B_1\\\hline
\text{signature}
&\{0,2,N\}&\{1,1,N-1\}&\{0,1,N-1\}
&\{0,1,N-2\}&\{1,2,N\}&\{1,2,N-1\}.
\end{array}
\]
They are pairwise distinct, and only \(R_0\) contains two entries differing by \(2\). Every right-hand signature contains such a pair, so any collision with the left-hand region would require the right-hand signature to equal \(\{0,2,N\}\). That signature has only one pair differing by two, namely \(\{0,2\}\); the right-hand distinguished pair would force \(q=2\), where its third entry is at most \(N-2\), a contradiction.

When \(j=3\) and odd \(N\ge9\), the initial signatures are
\[
\begin{array}{c|ccc}
 t&R_t&H_t&B_t\\\hline
 0&\{0,3,N\}&\{0,2,N-1\}&\{1,3,N\}\\
 1&\{1,2,N-1\}&\{1,1,N-2\}&\{2,2,N-1\}\\
 2&\{1,2,N-2\}&\{0,2,N-3\}&\{1,3,N-2\}.
\end{array}
\]
Again they are pairwise distinct and only \(R_0\) contains a pair of entries at distance \(3\). Its only such pair is \(\{0,3\}\); a matching right-hand signature would have \(q=3\) and third entry at most \(N-3\), not \(N\). This proves that the three selected vertices resolve every edge. The all-order upper bound is therefore \(3\) for odd \(n\ge7\) and even \(n\ge10\), and Step 1 makes it sharp.

**3. Finite exceptions and minimum-basis multiplicities.** The remaining orders are \(2,3,4,5,6,8\). The exhaustive certificate `finite_obstructions.json`, verified independently by `verify_certificate.py`, contains a pair of distinct edges with identical signatures for every one of the \(2^{2n}\) vertex subsets when \(n=2,3,4\), and for every three-vertex subset when \(n=5,6,8\). Its records cover \(336\) subsets in the first three cases and \(900\) three-vertex subsets in the latter three cases. The checker derives edge distances from coordinates and confirms both equality of each indicated pair and complete lexicographic coverage. Therefore the first three orders admit no resolving set, and the latter three require at least four vertices.

For each of \(n=5,6,8\), the explicit set \(\{(0,0),(0,1),(2,0),(4,0)\}\) resolves every edge. Exhaustive enumeration of all \(\binom{2n}{4}\) four-vertex subsets gives exactly \(4,20,80\) successful subsets, respectively. A breadth-first-search implementation (`verify_bfs.py`) and a separately implemented coordinate-distance C++17 program (`verify_coords.cpp`) independently reconstruct these counts and all finite lower bounds. This finishes the theorem.

## Verification

Run from the directory containing the files:

```sh
python3 verify_bfs.py
python3 verify_certificate.py finite_obstructions.json
g++ -O2 -std=c++17 verify_coords.cpp -o verify_coords
./verify_coords
```

The BFS program enumerates all landmark subsets for orders \(2,3,4\), and subsets up to size four (up to size three for \(n=7\)) for orders \(5,6,7,8\), then checks the three-landmark constructions for orders \(7\) through \(150\), excluding \(8\). The C++17 program independently enumerates the same finite cases using direct Manhattan graph distances, and checks constructions through order \(256\). The certificate checker is separate from the generator and checks every explicit obstruction pair and the required full coverage. `verification_output.txt` contains the observed outputs. The infinite part is established by Step 2's symbolic argument, not by these finite tests.

## Relationship to prior work

Ikhlaq, Ismail, Siddiqui, and Nadeem introduced edge-multiset dimension and established a general lower bound of three for non-path connected graphs, as well as dimension-three results for long cycles, kayak paddle graphs, dragon graphs, and comb products of two paths. The complete source text does not state a result for the Cartesian *ladder* \(P_n\square K_2\), which is different from the rooted/comb product of paths. The present theorem identifies the exact finite-infinite transition and the nonmonotone small-order exception of that family. Ordinary **ordered** edge-metric dimension, vertex multiset dimension, and multiset partition dimension are different invariants; results about them do not by themselves imply this theorem.

## Limitations

The theorem applies only to width-two open path grids. It does not classify every optimal three-landmark configuration for large \(n\), determine the complete polynomial of nonminimum resolving sets, or extend to arbitrary rectangular grids. The finite minimum-basis multiplicities rest on fully exhaustive finite enumeration, not a separate symbolic counting formula. The literature comparison does not establish absolute priority over unindexed research or inaccessible versions of relevant surveys. Independent validation has not been performed.

## References

1. H. M. Ikhlaq, R. Ismail, H. M. A. Siddiqui, M. F. Nadeem, “A New Technique to Uniquely Identify the Edges of a Graph,” *Symmetry* **15** (2023), article 762, first published 20 March 2023. https://doi.org/10.3390/sym15030762 . Full text: https://www.mdpi.com/2073-8994/15/3/762
2. M. Farhan, S. Klavžar, D. Kuziak, I. G. Yero, “Multiset resolvability parameters in graphs: A survey with new results and open problems,” arXiv:2607.10311 (2026). https://arxiv.org/abs/2607.10311 . Only abstract-level material was accessible in this comparison.
3. A. Albejani, Y. Lin, J. Ryan, K. A. Sugeng, “Multiset Partition Dimension of Graphs,” arXiv:2607.07407 (2026). https://arxiv.org/abs/2607.07407 . It uses partition-to-vertex signatures, not edge-to-landmark signatures.
