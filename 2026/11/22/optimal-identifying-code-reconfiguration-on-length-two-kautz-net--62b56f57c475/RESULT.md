# Optimal identifying-code reconfiguration on length-two Kautz networks

## Finding
For every integer \(q\ge3\), the directed length-two Kautz graph \(K(q-1,2)\) has exactly
\[
N_q=(q-1)^q-q(q-1)
\]
minimum closed-out-neighborhood identifying codes, each of cardinality \(q(q-2)\). Every minimum code is uniquely of the form
\[
C_f=\{(a,b):a\ne b,\ a\ne f(b)\},
\]
for a fixed-point-free function \(f:[q]\to[q]\) other than the \(q(q-1)\) functions with some center \(t\) satisfying \(f(x)=t\) for all \(x\ne t\).

The one-sensor-exchange graph of minimum codes is exactly the Hamming graph \(\square_{i=1}^q K_{q-1}\) after deleting the \(q(q-1)\) forbidden functions. For \(q\ge4\), those forbidden vertices induce \(q\) disjoint cliques of order \(q-1\); the edge count of the surviving graph is
\[
E_q=\frac{q(q-2)}2\big((q-1)^q-2q(q-1)\big)+q\binom{q-1}{2}.
\]
For \(q\ge5\), exactly \(q(q-1)^2(q-2)\) minimum codes have exchange degree \(q(q-2)-1\), and the other \(N_q-q(q-1)^2(q-2)\) have degree \(q(q-2)\). At \(q=4\), the exact degree spectrum is \(12\) vertices of degree \(6\), \(48\) of degree \(7\), and \(9\) of degree \(8\). At \(q=3\), the two optimal codes are exchange-isolated.

Thus the cardinalities of the full optimum families for \(q=3,4,5,6\) are respectively \(2,69,1004,15595\), and their exchange-edge counts are \(0,240,7410,186840\).

## Assumptions and scope
The alphabet \([q]=\{0,\ldots,q-1\}\) is labeled; all ordered pairs \((a,b)\) with \(a\ne b\) are vertices, and each arc goes from \((a,b)\) to \((b,c)\) with \(c\ne b\). For a code \(C\), the identifying signature of \((a,b)\) is the intersection of \(C\) with its closed *outgoing* radius-one neighborhood \(\{(a,b)\}\cup\{(b,c):c\ne b\}\). Identification means all signatures are nonempty and pairwise unequal. A one-sensor exchange deletes one selected vertex and adds one different vertex, leaving a minimum identifying code. No claim is made about longer Kautz graphs, other observation radii, or fault tolerance. Reversing each two-letter word converts outgoing signatures to incoming signatures in the reversed orientation.

## Proof
**Cardinality and forced representation.** For a fixed second coordinate \(b\), the \(q-1\) vertices \((a,b)\), \(a\ne b\), have the same open outgoing neighborhood. If two of these were outside \(C\), their *closed* outgoing signatures would be identical. Thus a valid code omits at most one vertex in each of the \(q\) second-coordinate columns. Every code has at least \(q(q-2)\) vertices; equality forces precisely one omission \((f(b),b)\) per column and uniquely specifies a function \(f\) with \(f(b)\ne b\).

**Which functions identify.** Define \(B_b=\{(b,c)\in C_f:c\ne b\}\), the selected outgoing-neighbor set of every vertex in column \(b\). The omitted vertex \((f(b),b)\) has signature \(B_b\); the other vertices \((a,b)\) have signatures \(B_b\cup\{(a,b)\}\). Therefore \(B_b\) must be nonempty. It is empty exactly when \(f(c)=b\) for all \(c\ne b\), one of the stated forbidden stars. Assume all \(B_b\ne\varnothing\). Signatures within one column are distinct because each selected self-vertex lies outside \(B_b\). For columns \(b\ne c\), the nonempty sets \(B_b\) and \(B_c\) lie in disjoint first-coordinate classes. Equality of signatures would therefore force \(B_b=\{(b,c)\}\), \(B_c=\{(c,b)\}\), with each selected self-vertex being the other's unique outgoing neighbor. Choose a third letter \(x\notin\{b,c\}\), which exists since \(q\ge3\). Then both \((b,x)\) and \((c,x)\) would be omitted from column \(x\), contrary to precisely one omission. Thus all signatures are distinct. A code attaining the lower bound exists: any fixed-point-free cyclic permutation \(f\) for \(q\ge3\) is not a forbidden star.

**Counting.** There are \((q-1)^q\) fixed-point-free functions. For a chosen center \(b\), a star is determined by the free value \(f(b)\ne b\), giving \(q-1\) stars. Stars with different centers are distinct: their values disagree at any third argument. Hence \(q(q-1)\) stars and the displayed count \(N_q\).

**Exchange geometry.** Since each minimum code has exactly one omission per column, a one-sensor exchange must replace the missing symbol in precisely one column. Consequently the ambient graph of all fixed-point-free functions is \(\square_{i=1}^q K_{q-1}\), of degree \(\Delta=q(q-2)\), and the exchange graph is its induced subgraph on nonstars. For each center \(b\), the \(q-1\) stars varying \(f(b)\) form a clique; a pair of stars with different centers has Hamming distance at least \(q-2\). For \(q\ge4\), no two different-center stars are adjacent. The ambient edge count is \(\Delta(q-1)^q/2\). The removed edges consist of \(q(q-1)\Delta\) incidences minus the \(q\binom{q-1}{2}\) edges internal to deleted cliques; subtraction gives \(E_q\).

For \(q\ge5\), stars with distinct centers are at Hamming distance at least three. A good function cannot be adjacent to two stars in the same deleted clique, since every common neighbor of two adjacent vertices of a Hamming graph lies in that same coordinate clique and is itself a star. Hence each good function has at most one deleted neighbor. Each deleted star has \(\Delta-(q-2)=(q-1)(q-2)\) good neighbors. Counting these incidences proves the two-value degree spectrum. At \(q=4\), distinct-center stars can lie at distance exactly two: for any unordered pair of centers, exactly one pair of such stars lies at distance two, and its two common neighbors are good. There are \(\binom42=6\) such pairs, yielding \(12\) vertices adjacent to two deleted stars. Each of the \(4\cdot3\) stars has \(6\) good neighbors, so the \(72\) lost-degree incidences yield another \(72-2\cdot12=48\) vertices adjacent to one star and \(69-12-48=9\) adjacent to none. At \(q=3\), direct enumeration gives only two surviving functions, which differ at all three coordinates, hence no exchange edge.

## Verification
Run `python3 standalone/verify_functions.py` and `python3 standalone/verify_subsets.py` using only the Python standard library. The first program independently constructs literal signatures for all fixed-point-free functions for \(3\le q\le6\), verifies the star criterion and exact exchange degrees. The second iterates every unparametrized subset of size \(q(q-2)\) of the graph's \(q(q-1)\) vertices for \(q=3,4,5\), checks all literal closed-neighborhood signatures and independently reconstructs the exchange spectrum at \(q=4\). Both programs finish successfully. Finite enumeration checks only these alphabet sizes; the general statements follow from the proof above.

## Relationship to prior work
Minimum cardinalities on Kautz digraphs were already established by Balbuena, Dalfó and Martínez-Barona's general 2019 line-digraph theorem, including \(q(q-2)\) in this length-two case; that minimum is *not* claimed as new. Their structural criterion implies certain local restrictions on optimum codes, but the explicit arbitrary-alphabet enumeration, removed-Hamming-graph description, exact exchange-edge count and degree distribution here require further specialized deductions. A published enumeration of optimal incoming identifying codes for three-symbol Kautz graphs already covers the \(q=3\) count \(2\); that boundary case is also not claimed as new. The current claim is the combined all-alphabet optimum-family and reconfiguration classification. No inspected source stated this combined invariant; an equivalent earlier specialization remains a priority risk.

## Limitations
The stated reconfiguration graph uses single-sensor exchanges within the class of *minimum* codes, not arbitrary intermediate codes. The degree formula is piecewise with exceptional \(q=3,4\); it does not imply connectivity or a diameter bound. The proof and computer checks are not independent mathematical peer review. A historical formulation of the same optimum-family and exchange graph may exist outside the inspected sources.

## References
1. M. G. Karpovsky, K. Chakrabarty, and L. B. Levitin, *On a New Class of Codes for Identifying Vertices in Graphs*, IEEE Trans. Inform. Theory 44 (1998), 599–611, DOI:10.1109/18.661507.
2. D. Boutin, C. Horan Goliber, and M. Pelto, *Identifying Codes on Directed De Bruijn Graphs*, arXiv:1412.5842 (originally posted 2014-12-18).
3. C. Balbuena, C. Dalfó, and B. Martínez-Barona, *Identifying codes in line digraphs*, arXiv:1905.05083 (2019), especially Theorem 3.4 and Corollary 3.9.
4. *Exact counting and uniform generation of optimal Kautz identifying codes*, published mathematical record https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-exact-counting-and-uniform-generation-of-optimal-kautz-identifyi--728f5ffa301d (ternary alphabet; higher word lengths).
