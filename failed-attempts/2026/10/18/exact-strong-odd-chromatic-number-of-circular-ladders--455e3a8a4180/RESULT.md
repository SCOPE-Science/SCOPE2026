# Exact strong odd chromatic number of circular ladders

## Finding
For every integer \(n\ge3\), let \(P_n=C_n\square K_2\) be the circular ladder, with two \(n\)-vertex cycles joined by corresponding rungs. Its **strong odd chromatic number** is
\[
\chi_{\mathrm{so}}(P_n)=
\begin{cases}
6,&n=3,\\
2,&n\ge4\text{ even},\\
5,&n\ge5\text{ odd}.
\end{cases}
\]
In particular, every odd circular ladder with at least ten vertices has a five-colour **square colouring** (all vertices within distance at most two receive distinct colours), and no strong odd colouring of it uses four or fewer colours. The triangular prism is the unique order exception to the odd-order five-colour formula.

## Assumptions and scope
All graphs are finite and simple. Write the vertices of \(P_n\) as \(t_i,b_i\), indexed by \(i\in\mathbb Z/n\mathbb Z\). Its edges are \(t_it_{i+1}\), \(b_ib_{i+1}\), and \(t_ib_i\). A strong odd colouring is a proper vertex colouring in which, for each vertex, every colour appearing on its three neighbours appears an odd number of times. Hence the three neighbouring colours are either all equal or pairwise distinct. The number \(n\) denotes cycle order (rung count), not vertex count.

## Proof
**Lower bounds.** Each colour class \(S\) of a strong odd colouring is independent. Moreover, no vertex outside \(S\) has exactly two neighbours in \(S\). Call such an \(S\) *odd independent*.

Suppose that \(n\) is odd. No two consecutive rung columns can both contain a member of \(S\). Otherwise, independence forces (up to exchanging the two rows) \(t_i,b_{i+1}\in S\). Vertex \(b_i\) already has the two \(S\)-neighbours \(t_i,b_{i+1}\), so \(b_{i-1}\in S\) is forced. Vertex \(t_{i-1}\) then has the two \(S\)-neighbours \(t_i,b_{i-1}\), so \(t_{i-2}\in S\) is forced. Iteration forces row-alternating selections \(t_i,b_{i-1},t_{i-2},b_{i-3},\ldots\). Since \(n\) is odd, this eventually forces \(b_i\in S\) as well, contradicting \(t_i\in S\) and independence. Thus the occupied columns of \(S\) form an independent set of \(C_n\), giving \(|S|\le (n-1)/2\). As there are \(2n\) vertices, any strong odd colouring on odd \(n\) needs at least
\[
\left\lceil\frac{2n}{(n-1)/2}\right\rceil
=\left\lceil4+\frac4{n-1}\right\rceil
=\begin{cases}6,&n=3,\\5,&n\ge5\text{ odd}.\end{cases}
\]
(The final case expression is read for odd \(n\) only.) For even \(n\), the presence of edges gives the trivial lower bound two.

**Upper bounds at even \(n\).** The graph \(P_n\) is bipartite exactly when \(n\) is even. Colour the bipartition classes with two colours. Every vertex has three neighbours of the opposite colour, so all neighbourhood multiplicities are odd.

**The triangular prism.** Give its six vertices six distinct colours. The lower bound above shows this is optimal.

**Constructive upper bound for odd \(n\ge5\).** Write each consecutive column as the two-digit word \(ab\), meaning \(t_i\) has colour \(a\), \(b_i\) has colour \(b\), with colours \(0,1,2,3,4\). Define the following column blocks:

| Block | Consecutive columns |
|---|---|
| \(U\), length four | `01 23 10 32` |
| \(V_5\), length five | `01 23 14 30 42` |
| \(V_7\), length seven | `01 23 10 32 04 13 42` |

For \(n\equiv1\pmod4\), take the cyclic concatenation \(U^{(n-5)/4}V_5\). For \(n\equiv3\pmod4\), take \(U^{(n-7)/4}V_7\). Exponents in this block notation mean literal repetition of columns, and are nonnegative in the stated ranges.

To check the entire infinite construction, a local property suffices. For each centre column \(x=(a,b)\) with predecessor \(p=(c,d)\) and successor \(z=(e,f)\), properness and a square colouring follow whenever \(c,e,b\) are three pairwise distinct colours, \(d,f,a\) are three pairwise distinct colours, and the centre is different from both corresponding horizontal neighbour colours. In fact the displayed triple conditions together with every block's vertical inequality give all of these requirements.

The possible cyclic three-column windows for **all** displayed constructions, written `(previous,center,next)`, are exactly the following 13 triples:

`(01,23,10) (01,23,14) (04,13,42) (10,32,01) (10,32,04) (13,42,01) (14,30,42) (23,10,32) (23,14,30) (30,42,01) (32,01,23) (32,04,13) (42,01,23)`.

For every listed triple the three neighbours of the top centre vertex have mutually distinct colours, as do the three neighbours of the bottom centre vertex; all horizontally and vertically adjacent vertices also differ. This is a direct finite inspection of digit values. It suffices to inspect \(U^kV_5\) and \(U^kV_7\) for \(k=0,1,2\): additional copies of the period-four word \(U\) only repeat interior windows already present at \(k=2\); the cyclic seams are determined by the unchanged first and last columns. Consequently every construction is a proper square colouring, hence a strong odd five-colouring. This establishes the upper bound and completes the proof.

## Verification
The standalone standard-library script `verify.py` reconstructs all three-neighbour sets directly from the graph, validates both block families through 499 rungs, establishes the complete 13-window census and its stabilization, and independently checks odd independent set maxima by exhaustive subset enumeration for \(3\le n\le9\). A separate finite-state search across all permissible two-colour column states checks existence or impossibility of strong odd colourings for every palette size \(2\le q\le5\) and \(3\le n\le12\). The recorded result is `VERIFICATION_OK` in `verify_output.txt`. The infinite proof is the propagation argument and the period-four local-window verification, not any extrapolation from sampled instances.

## Relationship to prior work
Kwon and Park initiated strong odd colouring. Caro, Petruševski, Škrekovski and Tuza, *On strong odd colorings of graphs* (arXiv:2410.02336, Section 4, Theorem 4.2), prove a general submultiplicative bound for Cartesian products; that bound does not yield the three-case exact formula above. The same authors' *The odd independence number of graphs, I* (arXiv:2509.20763, Proposition 1) establishes the general inequality between odd independent sets and strong odd chromatic number, without this prism colouring. Their companion *Part II* (arXiv:2510.01897) studies finite and infinite grids and chessboard graphs, not this complete rung-by-rung classification. Pradhan, Sharma and Verma, *On the Classical and Parameterized Complexity of Strong Odd Coloring* (arXiv:2610.01441, first public October 1, 2026), investigate hardness and algorithms on specified graph classes; available publication metadata do not state the prism result. Ordinary distance-two/square colouring is a stronger property than strong odd colouring; here its explicit five-colour construction supplies the sharp odd-case upper bound only when combined with the independent lower argument.

## Limitations
The classification is restricted to ordinary circular ladders \(C_n\square K_2\), not twisted Möbius ladders or arbitrary Cartesian graph products. Independent mathematical auditing has not been performed. Earlier equivalent formulas under square colouring, generalized Petersen graph, or odd-independent colouring terminology cannot be categorically excluded. The October 2026 complexity preprint's full text was not accessible during this assessment, so comparisons with that source are limited to its complete publicly available abstract and publication metadata; this is an explicit residual bibliographic-priority risk.

## References
1. H. Kwon and B. Park, *Strong odd coloring of sparse graphs*, arXiv:2401.11653 (2024).
2. Y. Caro, M. Petruševski, R. Škrekovski and Z. Tuza, *On strong odd colorings of graphs*, arXiv:2410.02336, Section 4, Theorem 4.2 (first public 2024-10-03).
3. Y. Caro, M. Petruševski, R. Škrekovski and Z. Tuza, *The odd independence number of graphs, I: Foundations and classical classes*, arXiv:2509.20763 (2025).
4. Y. Caro, M. Petruševski, R. Škrekovski and Z. Tuza, *The odd independence number of graphs, II: Finite and infinite grids and chessboard graphs*, arXiv:2510.01897 (2025).
5. D. Pradhan, V. Sharma and S. Verma, *On the Classical and Parameterized Complexity of Strong Odd Coloring*, arXiv:2610.01441 (first publicly posted 2026-10-01).
