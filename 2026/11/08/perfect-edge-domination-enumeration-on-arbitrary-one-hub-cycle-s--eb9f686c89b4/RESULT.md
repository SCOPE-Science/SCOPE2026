# Perfect-edge-domination enumeration on arbitrary one-hub cycle spiders

## Finding

Let \(c\ge3\), \(r\ge2\), and let \(\boldsymbol\ell=(\ell_1,\ldots,\ell_r)\) be positive integers. Form \(U(c;\boldsymbol\ell)\) from a simple cycle \(C_c\) by adjoining \(r\) vertex-disjoint pendant paths of respective edge lengths \(\ell_i\), all at the same cycle vertex, with no other identifications. An edge set \(F\) is **perfect edge dominating** if every edge outside \(F\) shares an endpoint with exactly one edge of \(F\); there is no restriction on edges inside \(F\).

Let \(I_j\) be the number of binary strings of length \(j\ge0\) whose ones have pairwise index distance at least three, with \(I_0=1\), \(I_1=2\), \(I_2=3\), and \(I_j=I_{j-1}+I_{j-3}\) for \(j\ge3\). For boundary formulas set \(I_{-2}=I_{-1}=1\) and \(I_j=0\) when \(j\le-3\). Define
\[
 P_c=I_{c-3},\qquad S_c=I_{c-5},\qquad
 Q_c=\begin{cases}0,&c=3,4,\\ I_{c-7},&c\ge5.\end{cases}
\]
For each integer \(t\ge1\), define integer sequences \(B_0(t),B_1(t),H(t)\) from the initial values
\[
\begin{array}{c|ccc}t&1&2&3\\\hline B_0(t)&1&2&2\\B_1(t)&1&0&1\\H(t)&0&1&2\end{array}
\]
and, independently for each sequence \(X\in\{B_0,B_1,H\}\), the recurrence \(X(t)=X(t-1)+X(t-3)\) for \(t\ge4\).

**Theorem.** The exact number \(N(c;\boldsymbol\ell)\) of perfect edge dominating sets of \(U(c;\boldsymbol\ell)\), including its whole edge set, is
\[
\boxed{\begin{aligned}
N(c;\boldsymbol\ell)={}&P_c\prod_{i=1}^r B_0(\ell_i)
+2S_c\prod_{i=1}^r B_1(\ell_i)\\
&+Q_c\sum_{j=1}^r B_0(\ell_j)\prod_{i\ne j}B_1(\ell_i)
+S_c\prod_{i=1}^r H(\ell_i).
\end{aligned}}
\]
Each of its four terms counts a disjoint structural class, so the formula is also a complete classification by the root and its immediate neighbours. In particular, when all arm lengths equal one,
\[N(c;1,\ldots,1)=P_c+2S_c+rQ_c,\]
whereas for \(r\ge2\) and all arm lengths equal two,
\[N(c;2,\ldots,2)=2^rP_c+S_c.\]
Thus uniformly in \(c\) the former grows at most linearly with the number of arms while the latter grows exponentially, exhibiting a sharp structural change upon subdividing each pendant edge once.

## Assumptions and scope

All graphs are finite, simple and unlabelled as *graph types*, but their distinct edge subsets are counted separately. The cycle has \(c\) distinct vertices, every arm has \(\ell_i\) new vertices and \(\ell_i\) edges, and the root has degree \(r+2\). The formula applies to every \(c\ge3\), every \(r\ge2\), and every positive integral arm-length vector, with repetitions allowed. Changing the order of arms does not change the count. No independence restriction is imposed on the chosen dominating edges themselves.

## Proof

**1. Unique white-set representation.** For a perfect edge dominating set \(F\), let \(W\) be the vertices incident with no edge of \(F\), and put \(R=V\setminus W\). A pair of vertices in \(W\) cannot be adjacent, because their joining edge would be dominated by zero selected edges. Every vertex of \(R\) is incident with a selected edge by its definition. Furthermore, every edge with both endpoints in \(R\) must lie in \(F\): otherwise it would be adjacent to at least one selected edge at each endpoint, hence at least two. Therefore \(F=E(G[R])\). An edge from \(w\in W\) to \(v\in R\) is outside \(F\) and has exactly one adjacent selected edge precisely when \(v\) has degree one in \(G[R]\). Consequently a vertex subset \(W\) corresponds uniquely to a perfect edge dominating set if and only if (i) \(W\) is independent; (ii) every vertex of \(R\) has a neighbour in \(R\); and (iii) every neighbour in \(R\) of a vertex of \(W\) has exactly one neighbour in \(R\).

**2. Forbidden-word representation.** Write the cycle vertices in cyclic order \(v_0,v_1,\ldots,v_{c-1}\), with root \(v_0\). On the remaining path \(v_1,\ldots,v_{c-1}\), record a one at an index exactly when the vertex lies in \(W\). Do the same independently on each pendant path, starting at its vertex adjacent to the root. Since internal vertices have degree two, two ones on any such path cannot be separated by zero or one indices: an adjacent pair violates (i), while a pair at distance two would leave its intervening degree-two vertex without a neighbour in \(R\). Conversely this distance-three spacing ensures conditions (i)--(iii) at all internal degree-two vertices, apart from the boundaries stated next. In every pendant arm of length at least two the penultimate vertex must be in \(R\), as otherwise the terminal leaf would have no neighbour in \(R\). These requirements are also sufficient away from the root.

The number of allowed cycle words with both ends zero is \(P_c\), with ends \((1,0)\) or \((0,1)\) is \(S_c\) for each orientation, and with both ends one is \(Q_c\). These follow by deleting the forced zero prefixes/suffixes and counting a free spaced binary word: the remaining lengths are \(c-3\), \(c-5\), and \(c-7\), respectively. For \(c=3,4\) the two cycle-path endpoints cannot both be one. The boundary conventions for \(I_j\) give the stated formulas exactly, including \(c=3,4,5\).

For a pendant path of \(t\) vertices, \(B_0(t)\), respectively \(B_1(t)\), counts allowed spaced binary words with first bit zero, respectively one, and with penultimate bit zero if \(t\ge2\). The quantity \(H(t)\) counts these words with the first two bits zero; by definition \(H(1)=0\). Their initial values follow by direct inspection at lengths one, two and three. For \(t\ge2\) the counts also equal
\[
B_0(t)=I_{t-3}+I_{t-4},\quad B_1(t)=I_{t-5}+I_{t-6},\quad H(t)=I_{t-4}+I_{t-5}.
\]
These identities arise by splitting on whether the last bit is zero or one, with the penultimate bit forced to zero and the two preceding positions also forced to zero when the last bit is one. Together with the length-one boundary they establish the stated three recurrences, including their first steps at \(t=4,5\).

**3. Root cases.** If the root belongs to \(R\), it has \(r+2\) neighbours. If none is in \(W\), then the cycle word begins and ends in zero and every arm starts with zero: the count is \(P_c\prod B_0\). Otherwise, any neighbour of the root in \(W\) forces the root to have precisely one neighbour in \(R\), hence precisely \(r+1\) neighbours in \(W\). The unique root neighbour outside \(W\) is either one of the two cycle neighbours, yielding \(2S_c\prod B_1\), or the first vertex of exactly one arm \(j\), yielding \(Q_c B_0(\ell_j)\prod_{i\ne j}B_1(\ell_i)\). Summing over \(j\) gives the third term.

If the root belongs to \(W\), all of its neighbours lie in \(R\) and must have exactly one neighbour in \(R\). Hence the first two positions at either end of the cycle path are zero, as are the first two vertices of every arm. In particular no arm can have length one. The permitted cycle word is counted by \(S_c=I_{c-5}\), and arm \(i\) by \(H(\ell_i)\), producing the fourth term. These root cases are exhaustive and pairwise disjoint. The preceding local rules prove sufficiency, so every counted word family determines exactly one admissible \(W\) and thus exactly one \(F\). This proves the formula.

**4. Subdivision contrast.** For \(t=1\), the three arm sequences have values \((B_0,B_1,H)=(1,1,0)\), giving \(P_c+2S_c+rQ_c\). For \(t=2\) they are \((2,0,1)\). With at least two arms the second and third terms vanish, leaving \(2^rP_c+S_c\). As \(P_c\ge1\), the latter grows exponentially in \(r\), while the former is affine in \(r\).

## Verification

Run `python3 artifacts/verify.py` from the package root. The verifier independently enumerates arbitrary edge subsets (rather than deriving them from the word formula) for 468 labelled instances with two to four arms and total order at most 12, checks exact equivalence with the four root classes, and compares their cardinalities with the formula. It also checks the equal-length-two specialization on larger parameters. The unrestricted theorem follows from the proof, not these finite computations.

## Relationship to prior work

Grippo, Lin, Moyano and Vera (arXiv:2607.03894v1, first public 2026-07-04) define this edge-domination notion, develop counting algorithms on generalized series-parallel and chordal graphs, and conjecture that a cycle maximizes the count among connected graphs of given order. Their general algorithm applies to the present graphs but does not state the closed arbitrary-arm product enumerator or the one-subdivision growth transition. Earlier work of Lu, Ko and Tang introduces perfect edge domination and its algorithmic setting. Existing one-tail (lollipop/tadpole) enumerations are recovered by setting \(r=1\), but are a proper one-arm special case: for \(r\ge2\), the root degree and the exactly-\(r+1\)-white-neighbour condition create a new coupling across all arms. The theorem does **not** claim the general conjectured cycle bound for these graphs.

## Limitations

The paths must meet only at a single cycle root; the formula does not apply to multiple attachment vertices, additional chords, arbitrary cactus graphs, or general unicyclic graphs. All counts are exact unweighted cardinalities, not edge-size generating functions. The subdivision contrast changes the order as well as the number of edges. The direct finite enumeration cannot establish the formula for unbounded parameters, and historical-priority comparisons do not constitute an independent mathematical audit.

## References

1. Luciano N. Grippo, Min Chih Lin, Verónica Moyano, Camilo Vera, *Counting perfect edge dominating sets: extremal results and linear-time algorithms*, arXiv:2607.03894v1 (2026-07-04), https://arxiv.org/abs/2607.03894 .
2. Chin Lung Lu, Ming-Tat Ko, Chuan Yi Tang, *Perfect edge domination and efficient edge domination in graphs*, Discrete Applied Mathematics 119 (2002), 227--250, DOI 10.1016/S0166-218X(01)00198-6.
3. Luciano N. Grippo, Min Chih Lin, Camila Vera, *Perfect Edge Domination in P6-free Graphs and in Graphs Without Efficient Edge Dominating Sets*, arXiv:2509.04598v1 (2025-09-04), https://arxiv.org/abs/2509.04598 .
