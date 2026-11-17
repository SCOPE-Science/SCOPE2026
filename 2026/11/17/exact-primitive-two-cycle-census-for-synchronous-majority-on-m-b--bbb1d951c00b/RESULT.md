# Exact primitive two-cycle census for synchronous majority on Möbius ladders

## Finding
For the majority map defined below, **the exact number of configurations of least period two** is \(P_n-H_n\); the exact number of *unoriented temporal two-cycles* is \((P_n-H_n)/2\). Set
\[
L_0=2,\quad L_1=1,\quad L_{n}=L_{n-1}+L_{n-2},
\qquad U_0=2,\quad U_1=3,\quad U_n=3U_{n-1}-U_{n-2}.
\]
Let \(B_0=4,B_1=1,B_2=-3,B_3=-8\) and \(B_n=B_{n-1}-2B_{n-2}-B_{n-3}-B_{n-4}\) for \(n\ge4\). Write \(c_n=2\cos(2\pi n/3)\in\{2,-1\}\) and \(d_n=2\cos(\pi n/3)\in\{2,1,-1,-2,-1,1\}\), both integers. Then
\[
\boxed{P_n=\#\{x:F_n^2(x)=x\}=\begin{cases}
U_n+c_n+2,&n\ \mathrm{even},\\
U_n+c_n+2B_n,&n\ \mathrm{odd},
\end{cases}}
\qquad
\boxed{H_n=\#\{x:F_n(x)=x\}=L_n+d_n.}
\]
There are exactly \((P_n-H_n)/2\) distinct primitive two-cycles. This is an exact finite-size count for every \(n\ge3\), not a count of eventual attraction basins. The \(H_n\) count uses a pre-existing cyclic-binary-word enumeration; the contribution is the explicit \(P_n\) census.

## Assumptions and scope
For each integer \(n\ge3\), the simple undirected Möbius ladder \(M_{2n}\) has labelled vertices \(i\in\mathbb Z/(2n)\mathbb Z\) and neighbors \(i-1,i+1,i+n\), all indices modulo \(2n\). A state is \(x\in\{0,1\}^{2n}\), and
\[
F_n(x)_i=\mathbf1\{x_{i-1}+x_{i+1}+x_{i+n}\ge2\}.
\]
Updates are simultaneous; no self-state is included. A primitive temporal orbit has the least positive period of its configurations. The census includes only states already on periodic orbits, not transient predecessors.

## Proof
**1. Fixed configurations.** Suppose \(F_n(x)=x\) and the two ends of a spoke disagree, say \(x_i=0,x_{i+n}=1\). The majority inequalities force the two cycle neighbors of \(i\) to be zero and the two cycle neighbors of \(i+n\) to be one. Repeating this propagation around the cycle forces every clockwise cycle edge from \(i\) to preserve its endpoint value, contradicting the spoke disagreement when the walk reaches \(i+n\). Hence all spoke ends agree: \(x_i=x_{i+n}\). The fixed-point constraint then reduces to a cyclic word of length \(n\) with no isolated zero or one (no substring 010 or 101 with cyclic boundary). The four-state de Bruijn transfer on consecutive bit pairs has characteristic polynomial
\[
(t^2-t-1)(t^2-t+1).
\]
Its \(n\)-th trace is \(L_n+d_n\). The cyclic-word count and an equivalent closed formula were obtained by Agur, Fraenkel and Klein (1988); this is supporting prior work, not a novelty claim.

**2. Exact two-cycle transfer.** Let \(x,y\) be binary configurations with \(y=F_n(x)\) and \(x=F_n(y)\). Group opposite vertices into columns indexed \(0,\ldots,n-1\). Each column has four bits
\[
a_i=(x_i,x_{i+n},y_i,y_{i+n})\in\{0,1\}^4.
\]
Let \(S\) swap the two entries within each temporal layer. The Möbius twist is represented exactly by \(a_{-1}=S(a_{n-1})\) and \(a_n=S(a_0)\). For three four-bit columns \(a,b,c\), declare \(g(a,b,c)=1\) if, for each of the two rows \(r\in\{0,1\}\), both majority identities hold:
\[
 b_{y,r}=\operatorname{maj}(a_{x,r},c_{x,r},b_{x,1-r}),\qquad
 b_{x,r}=\operatorname{maj}(a_{y,r},c_{y,r},b_{y,1-r}).
\]
Construct a \(256\times256\) nonnegative integer matrix \(T\), indexed by ordered pairs of columns, by
\[
T_{(a,b),(b',c)}=\mathbf1\{b=b'\}\,g(a,b,c).
\]
Let \(R\) permute pair states by \((a,b)\mapsto(S(a),S(b))\). Closed walks with this row-swap boundary are in bijection with the \(x,y\) pairs above, so
\[
P_n=\operatorname{tr}(T^nR).
\]
The bijection is at labelled vertices; there is no division by spatial rotations, and \(y\) is uniquely determined by \(x\).

**3. A finite exact transfer calculation.** Enumerating all sixteen possible columns and all triples, the transfer digraph has exactly \(256\) vertices and \(400\) edges. Its cyclic strongly connected components have sizes \(16,8,8,2,1,1\). The row swap \(S\) preserves the components of sizes \(16\) and \(2\) and exchanges the remaining four cyclic components in pairs. A walk from a state to its swapped image must stay within a single strongly connected component: applying the swap supplies a reverse walk, which proves both endpoints belong to the same component. Thus only the sizes \(16\) and \(2\) contribute to \(\operatorname{tr}(T^nR)\).

In the sixteen-state component, \(S\) commutes with the restricted transition matrix; its positive and negative eigenspaces have dimensions \(10\) and \(6\). The exact characteristic polynomials there are
\[
\chi_+(t)=(t-1)(t+1)(t^2-3t+1)(t^2+t+1)(t^4-t^3+2t^2+t+1),
\]
\[
\chi_-(t)=(t-1)(t+1)(t^4+t^3+2t^2-t+1).
\]
These factorizations are verified by independent integer characteristic-polynomial calculations in `verify_transfer.py`, using Newton identities; the program independently builds the graph and its components from the explicit majority rule. The size-two component contributes \(1+(-1)^n\).

Put \(p(t)=t^4-t^3+2t^2+t+1\). Its root power sums are \(B_n\) (Newton identities give the stated initial values and recurrence). Since the remaining quartic is \(p(-t)\), its root power sums equal \((-1)^n B_n\). The quadratic \(t^2-3t+1\) has power sums \(U_n\), while \(t^2+t+1\) has power sums \(c_n\). The common \(t^2-1\) contribution cancels between the \(+\) and \(-\) spaces. Therefore
\[
\operatorname{tr}(T^nR)=U_n+c_n+[1-(-1)^n]B_n+1+(-1)^n,
\]
which gives the two parity cases above. Subtracting the fixed configurations and dividing by two counts distinct primitive temporal two-cycles, completing the proof.

## Verification
Running `python3 verify_transfer.py` builds the full finite transition digraph, computes its exact strongly connected components, exact integer characteristic polynomials, and checks \(P_n\) directly from the twisted trace for \(3\le n\le12\). Running `c++ -O2 -std=c++17 verify_vertex.cpp -o verify_vertex && ./verify_vertex` independently enumerates every labelled state for \(3\le n\le12\), checks \(F_n(x)=x\) and \(F_n^2(x)=x\), and confirms the same counts. Both program outputs are included verbatim. For \(n=8\), the calculations give \(P_8=2208\), \(H_8=46\), and \(1081\) primitive two-cycles.

## Relationship to prior work
Goles and Olivos (1980) established the period-one-or-two restriction for symmetric binary threshold dynamics on all finite graphs; that general theorem does not count periodic states. Benjamini, Chan, O'Donnell, Tamuz and Tan (2014), Section 1, explicitly recount the finite-graph theorem while focusing on unimodular infinite graphs and random graphs. Agur, Fraenkel and Klein (1988), Theorem (1), count cyclic binary strings without isolated symbols for the one-dimensional majority automaton **including its center bit**. That establishes the cyclic-word enumerator used above, and it is not claimed as new; their model is not the Möbius ladder and their one-dimensional orbit statement does not imply the present exponentially large two-cycle census. Searches for Möbius-ladder/chordal-ring majority orbit enumeration did not identify an exact two-cycle count in accessible papers. A manuscript by Flocchini, Geurts and Santoro on dynamic majority in general graphs and chordal rings (cited in a 1999 workshop bibliography) could not be obtained in full and remains a specifically identified priority risk.

## Limitations
This theorem counts periodic states and temporal two-cycles but does not describe transient lengths or attraction-basin sizes. The finite transfer certificate establishes the characteristic-polynomial identities exhaustively on a fixed 256-state graph; direct finite vertex simulations are supporting checks, not the proof of the all-size theorem. The historical-priority assessment is provisional, particularly regarding less-indexed chordal-ring majority literature. No independent scientific review has been performed.

## References
1. E. Goles and J. Olivos, "Periodic behaviour of generalized threshold functions," *Discrete Mathematics* 30 (1980), 187–189. DOI: 10.1016/0012-365X(80)90121-1.
2. Z. Agur, A. S. Fraenkel and S. T. Klein, "The number of fixed points of the majority rule," *Discrete Mathematics* 70 (1988), 295–302. DOI: 10.1016/0012-365X(88)90005-2. Full text: https://u.cs.biu.ac.il/~tomi/Postscripts/majority.pdf.
3. I. Benjamini, S.-O. Chan, R. O'Donnell, O. Tamuz and L.-Y. Tan, "Convergence, unanimity and disagreement in majority dynamics on unimodular graphs and random graphs," arXiv:1405.2486v1, publicly posted 2014-05-11. https://arxiv.org/pdf/1405.2486.
4. P. Flocchini, F. Geurts and N. Santoro, "Dynamic majority in general graphs and chordal rings," referenced as manuscript (1997) and WG 1999 proceedings. Full text not retrieved; see citations in https://carleton.ca/scs/wp-content/uploads/TR-98-05.pdf.
