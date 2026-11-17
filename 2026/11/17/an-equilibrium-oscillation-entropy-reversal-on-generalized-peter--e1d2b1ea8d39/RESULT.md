# An equilibrium–oscillation entropy reversal on generalized Petersen graphs

## Finding
For every integer \(n\ge5\), let \(G(n,k)\), for \(k=1,2\), be the labelled cubic generalized Petersen graph with outer vertices \(u_i\), inner vertices \(v_i\), and edges \(u_i u_{i+1}\), \(u_i v_i\), \(v_i v_{i+k}\), with indices modulo \(n\). Let \(M_{n,k}\) update all binary vertex states simultaneously to the strict majority of their three neighbours. Write \(F_k(n)=|\operatorname{Fix}(M_{n,k})|\) and \(C_k(n)\) for the number of *primitive temporal two-cycle orbits* (no spatial quotient).

**Exact step-two census.** There are explicit finite, nonnegative integer matrices \(B\) of size \(778\) and \(C\) of size \(24\), independently defined in the proof, such that
\[
F_2(n)=2+\operatorname{tr}(C^n),\qquad
C_2(n)=\frac{\operatorname{tr}(B^n)-\operatorname{tr}(C^n)}{2}.
\]
Both are adjacency matrices of strongly connected directed graphs containing loops. Their Perron roots \(\beta\) and \(\alpha\) obey the *rigorous rational intervals*
\[
2.64157<\beta<2.64158,\qquad 1.56485<\alpha<1.56486.
\]
Thus \(C_2(n)\sim\beta^n/2\) and \(F_2(n)\sim\alpha^n\).

**Entropy reversal.** For the ordinary prism \(G(n,1)=C_n\square K_2\), let \(\varphi=(1+\sqrt5)/2\). Its fixed configurations and primitive two-cycle orbits have asymptotic counts \(F_1(n)\sim\varphi^n\) and \(C_1(n)\sim\varphi^{2n}/2\). Consequently
\[
\boxed{\frac{F_2(n)}{F_1(n)}\sim\left(\frac{\alpha}{\varphi}\right)^n\longrightarrow0,
\qquad
\frac{C_2(n)}{C_1(n)}\sim\left(\frac{\beta}{\varphi^2}\right)^n\longrightarrow\infty.}
\]
Changing the inner-ring step from one to two therefore **suppresses equilibria but exponentially increases temporal two-cycle populations** at the same vertex count and degree. For \(G(n,2)\), almost every *immediately periodic* configuration belongs to a genuine two-cycle, since \(F_2(n)/|\operatorname{Fix}(M_{n,2}^2)|\to0\). The period-at-most-two result for finite symmetric majority dynamics is classical and not claimed as new.

| \(n\) | Prism fixed | Step-two fixed | Prism primitive two-orbits | Step-two primitive two-orbits |
|---:|---:|---:|---:|---:|
| 5 | 14 | 14 | 55 | 55 |
| 6 | 22 | 14 | 231 | 184 |
| 7 | 32 | 32 | 406 | 427 |
| 8 | 48 | 48 | 1128 | 962 |
| 9 | 76 | 76 | 2853 | 3906 |
| 10 | 124 | 118 | 7626 | 9679 |
| 11 | 202 | 158 | 19701 | 23837 |

## Assumptions and scope
The index range \(n\ge5\) ensures the three neighbors of each vertex of \(G(n,2)\) are distinct. Configurations are labelled binary vectors of length \(2n\); complements and spatial rotations are distinct. The count \(C_k(n)\) identifies two configurations only when they are successive states of the **same temporal orbit**. A state satisfying \(M^2(x)=x\) is either fixed or lies on a primitive two-cycle, so \(C_k(n)=(|\operatorname{Fix}(M^2)|-|\operatorname{Fix}(M)|)/2\).

## Proof
**1. Exact space–time encoding.** A column containing the two vertices \(u_i,v_i\) at times zero and one has symbol \(s_i=(a_i,b_i,A_i,B_i)\in\{0,1\}^4\), encoded as \(a_i+2b_i+4A_i+8B_i\). Define \(m(x,y,z)=1\) if \(x+y+z\ge2\), otherwise zero. The pair of time slices forms a two-cycle (possibly a fixed point) exactly when for every \(i\),
\[
\begin{aligned}
 A_i&=m(a_{i-1},a_{i+1},b_i),&a_i&=m(A_{i-1},A_{i+1},B_i),\\
 B_i&=m(b_{i-2},b_{i+2},a_i),&b_i&=m(B_{i-2},B_{i+2},A_i).
\end{aligned}
\]
Construct a directed graph \(H_2\) whose vertices are ordered four-tuples \((p,q,r,s)\in\{0,\ldots,15\}^4\). There is an edge \((p,q,r,s)\to(q,r,s,t)\) for \(t\in\{0,\ldots,15\}\) if and only if the four displayed local conditions hold at the central symbol \(r\) for five consecutive symbols \((p,q,r,s,t)\). This specifies the entire graph with no external tables: it has \(16^4=65536\) vertices and exactly \(102400\) edges. Cyclic spatial configurations satisfying the four local conditions correspond bijectively to closed walks of length \(n\) in \(H_2\); overlapping windows reconstruct the unique labelled word. Therefore \(|\operatorname{Fix}(M_{n,2}^2)|=\operatorname{tr}(A_2^n)\), where \(A_2\) is its adjacency matrix.

Likewise, a single time slice uses symbols \((a_i,b_i)\in\{0,1\}^2\), with only the two time-independent majority conditions. The analogous four-column overlap graph \(H_1\) has \(4^4=256\) vertices and \(320\) edges. Its adjacency matrix satisfies \(F_2(n)=\operatorname{tr}(A_1^n)\). The exact generators for both graphs are included in `verification/transfer.py`.

**2. Exact recurrent decomposition.** The supplied self-contained program enumerates *all* edges of both graphs and finds their strongly connected components by iterative Kosaraju traversal. A directed closed walk lies entirely in one cyclic strongly connected component. For \(H_2\), precisely three components contain a directed cycle: two isolated one-loop vertices and a strongly connected \(778\)-vertex component with \(2202\) internal edges. For \(H_1\), they are two isolated one-loop vertices and a strongly connected \(24\)-vertex component with \(36\) internal edges. Define \(B\) and \(C\) as the adjacency matrices of these respective large components, using the canonical vertex order produced by the source program. It follows *for all \(n\ge5\)* that
\[
|\operatorname{Fix}(M_{n,2}^2)|=2+\operatorname{tr}(B^n),
\quad F_2(n)=2+\operatorname{tr}(C^n),
\]
and subtraction yields the asserted exact orbit formula. The component sizes are outcomes of complete finite algorithms, not inferences from sampled spatial circumferences. Their complete source logic is included.

**3. Certified exponential rates.** Both large components have self-loops, so their strongly connected adjacency matrices are primitive. Hence Perron–Frobenius theory gives \(\operatorname{tr}(B^n)=\beta^n(1+o(1))\) and \(\operatorname{tr}(C^n)=\alpha^n(1+o(1))\). For a component adjacency matrix \(R\), form the strictly positive *integer* vector \(v=R^{80}\mathbf1\) and \(w=Rv\). The accompanying program verifies every coordinate of the integer inequalities
\[
264157v_i<100000w_i<264158v_i\quad(R=B),
\]
\[
156485v_i<100000w_i<156486v_i\quad(R=C).
\]
The Collatz–Wielandt bounds on the spectral radius then establish the claimed **strict rational intervals** exactly. The checks use Python arbitrary-precision integers, not floating-point eigenvalue estimates. Note that \(\varphi^2=(3+\sqrt5)/2<2.61804<2.64157\) and \(\varphi>1.61803>1.56486\).

**4. Prism comparison.** For \(G(n,1)\), any opposite-coloured rung in a fixed state forces both horizontal neighbors of both endpoints to agree with their own rung endpoint; propagation around the ring forces the two monochromatic opposite layers (two configurations). Otherwise every rung has equal colors, and the cyclic rung word has no isolated bit. The four-state word transfer has characteristic polynomial \((t^2-t-1)(t^2-t+1)\). Thus
\[
F_1(n)=L_n+2+2\cos(n\pi/3),
\]
where \(L_n\) are the Lucas numbers. This prism formula is established prior work and is independently reconstructed here. The canonical bipartite double of any neighbor-only majority network converts an ordered two-cycle pair into a fixed configuration. If \(n\) is even, the prism is bipartite, its double is two disjoint copies, and \(|\operatorname{Fix}(M_{n,1}^2)|=F_1(n)^2\). For odd \(n\), the double is the \(2n\)-rung prism, so \(|\operatorname{Fix}(M_{n,1}^2)|=F_1(2n)\). In either parity class, this is \(\varphi^{2n}(1+o(1))\). Subtracting fixed points and dividing by two establishes \(C_1(n)\sim\varphi^{2n}/2\). The two strict spectral comparisons now imply the entropy reversal.

## Verification
From the directory containing this document, run `python3 verification/transfer.py` and `g++ -std=c++17 -O3 verification/direct.cpp -o /tmp/majority_gp_direct && /tmp/majority_gp_direct`. The Python implementation constructs both full finite graphs, enumerates strongly connected components, checks component and edge cardinalities, checks both spectral-radius intervals by exact-integer inequalities, and traces the recurring adjacency blocks for \(5\le n\le11\). The separately authored C++17 implementation directly evolves all \(4^n\) labelled initial configurations for both \(k=1,2\) and \(5\le n\le11\), computing \(F_k(n)\) and \(|\operatorname{Fix}(M_{n,k}^2)|\) without any transfer graph. Every corresponding count agrees. The actual console outputs are `verification/transfer_output.txt` and `verification/direct_output.txt`. The transfer construction and the finite graph decomposition prove the all-size claim; the small-circumference direct enumeration is an independent check, not the sole proof.

## Relationship to prior work
Goles and Olivos (1980) established the eventual period-at-most-two theorem for symmetric threshold networks; the accessible 2014 treatment of Benjamini et al. restates it and studies random and infinite graphs, not this exact all-size orbit census. A published prism/Möbius ladder study already gives the Lucas-number prism fixed and two-cycle formulas; those facts are explicitly **not** new. A published dodecahedral study counts exactly 118 fixed and 9,679 primitive two-cycle orbits for \(G(10,2)\), also **not** new as an isolated case. An earlier fixed-state classification for the entire \(G(n,2)\) family already establishes the fixed-count ninth-degree structure and the associated equilibrium growth constant. The present result does not claim priority over that fixed-state classification. Its distinctive claim is the **all-circumference primitive two-cycle transfer, the certified \(2.64157\)–\(2.64158\) oscillation growth interval, and the opposing exponential comparisons with the prism**. The finite dodecahedral population is one necessary consistency check, not an independent novelty claim.

## Limitations
These counts concern configurations already on fixed or primitive two-periodic orbits, **not their eventual attraction basins or transient entry times**. The trace matrices provide an exact finite algorithm but no small scalar characteristic polynomial is asserted for the \(778\)-vertex block. Entropy comparisons are asymptotic: the step-two graph does not have more primitive two-cycles at every small circumference. This result does not apply to \(G(n,k)\) for \(k\ge3\), nor does it settle unrelated dynamics on generalized Petersen graphs. Literature searches cannot establish absolute priority against unindexed work. External independent mathematical validation has not been performed.

## References
1. I. Benjamini, S.-O. Chan, R. O'Donnell, O. Tamuz, L.-Y. Tan, *Convergence, Unanimity and Disagreement in Majority Dynamics on Unimodular Graphs and Random Graphs*, arXiv:1405.2486v1, 11 May 2014, https://arxiv.org/pdf/1405.2486.
2. E. Goles and J. Olivos, *Periodic behaviour of generalized threshold functions*, Discrete Mathematics 30 (1980), 187–189, https://doi.org/10.1016/0012-365X(80)90121-1.
3. *A modulo-six twist resonance in synchronous majority dynamics on cubic cyclic ladders*, published mathematical record, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-a-modulo-six-twist-resonance-in-synchronous-majority-dynamics-on--0a383da6731a.
4. *Dodecahedral majority dynamics: an exact recurrent, basin and symmetry census*, published mathematical record, https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-dodecahedral-majority-dynamics-an-exact-recurrent-basin-and-symm--095dfb0decea.
