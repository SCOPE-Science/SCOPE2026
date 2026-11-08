# A three-stage two-leader transition on diamond bouquets

## Finding
For every integer \(m\ge 1\), let \(D_m=K_1\vee(mP_3)\) be an unweighted, undirected simple graph. More explicitly, \(D_m\) has a central vertex \(h\) and \(m\) disjoint triples \(a_i,b_i,c_i\), with edges \(ha_i,hb_i,hc_i,a_ib_i,b_ic_i\) for each \(1\le i\le m\), and no other edges. Each subgraph on \(h,a_i,b_i,c_i\) is a diamond (the graph \(K_4\) minus one edge), and the diamonds have only \(h\) in common.

For each two-vertex leader set \(S\), let \(F=V(D_m)\setminus S\), let \(L\) denote the combinatorial Laplacian, and define the *unscaled* noise-free coherence objective
\[
J_m(S)=\operatorname{tr}\!\left((L_{FF})^{-1}\right).
\]
The following is the **complete** optimal two-leader classification, including all ties:

1. If \(m=1\), the unique optimal leader set is \(\{a_1,c_1\}\), and its objective is \(3/4\).
2. If \(m=2\), the unique optimal leader set is \(\{b_1,b_2\}\), and its objective is \(5/2\).
3. If \(m\ge3\), exactly the \(3m\) leader sets \(\{h,v\}\), for arbitrary \(v\ne h\), are optimal, all with objective \((7m-3)/4\). In particular, choosing a degree-two or degree-three vertex as the second leader is equally effective.

The threshold is strict in each integer regime: there are no further optimal placements. For \(m\ge2\), the best hub-free placement always uses the two distinct module centers \(b_i,b_j\). Its objective is \((5m-5)/2\), so the best hub-free minus best hub-containing cost is exactly
\[
\frac{5m-5}{2}-\frac{7m-3}{4}=\frac{3m-7}{4}.
\]
This changes sign between the two- and three-diamond networks.

## Assumptions and scope
All edges have conductance one. Leaders are noise-free and entirely grounded: the follower dynamics use the **principal** Laplacian submatrix with leader rows and columns removed, while the original follower degrees are retained. Exactly two *distinct* vertices are leaders, and \(m\) ranges over all positive integers. Since \(D_m\) is connected and the leader set is nonempty, every \(L_{FF}\) is positive definite. The score \(J_m\) does not include the customary factor \(1/2\) from steady-state variance; multiplying all scores by a common positive constant does not change optimizers. No assertions are made for noisy or finite-gain leaders, heterogeneous edge weights, or other objectives.

## Proof
**One-module matrix data.** After removing the hub from the follower set, a complete ungrounded triple has the block
\[
A=I_3+L(P_3)=\begin{pmatrix}2&-1&0\\-1&3&-1\\0&-1&2\end{pmatrix}.
\]
Its eigenvalues are \(1,2,4\), and hence \(\operatorname{tr}(A^{-1})=7/4\). Moreover \(A^{-1}\mathbf 1=\mathbf 1\), giving \(\mathbf 1^\top A^{-1}\mathbf 1=3\) and \(\mathbf 1^\top A^{-2}\mathbf 1=3\). Let the ordered triple \((t,u,v)\) record these three quantities for any remaining module block. Grounding a single end yields
\[
A_E=\begin{pmatrix}3&-1\\-1&2\end{pmatrix},\qquad
(t_E,u_E,v_E)=(1,7/5,1),
\]
while grounding a middle vertex yields \(A_C=2I_2\) and \((t_C,u_C,v_C)=(1,1,1/2)\). Grounding both ends of one module leaves \(A_{EE}=(3)\), so \((t_{EE},u_{EE},v_{EE})=(1/3,1/3,1/9)\); grounding one end and its center leaves \(A_{EC}=(2)\), so \((t_{EC},u_{EC},v_{EC})=(1/2,1/2,1/4)\). These are direct two-by-two or one-by-one inversions. No module can contain two distinct middle vertices.

**Hub among the leaders.** There are \(m-1\) untouched modules and one with a grounded end or center. The untouched block contributes trace \(7/4\), and the affected block contributes trace \(1\) in either case. Thus
\[
J_{h,E}=J_{h,C}=\frac{7m-3}{4}.
\]

**Hub among followers.** Put the common hub first in \(L_{FF}\), followed by each surviving module block \(A_i\). Its diagonal entry is the original degree \(3m\), and its coupling to every surviving module vertex is \(-1\). The one-by-one Schur complement of \(\operatorname{diag}(A_i)\) is
\[
s=3m-\sum_i\mathbf 1^\top A_i^{-1}\mathbf 1>0.
\]
The block inverse formula gives the **exact** identity
\[
J_m(S)=\sum_i t_i+\frac{1+\sum_i v_i}{s},
\qquad
(t_i,u_i,v_i)=\bigl(\operatorname{tr}A_i^{-1},\mathbf 1^\top A_i^{-1}\mathbf 1,\mathbf 1^\top A_i^{-2}\mathbf 1\bigr).
\]
In every case, the denominator \(s\) is one of \(8/3,5/2,16/5,18/5,4\), respectively, and therefore strictly positive.

Substitution of the one-module data gives every possible symmetry class as follows. Here E means an endpoint of a module path, C means its center, and “different” means two separate modules.

| Leader class | Unscaled objective \(J_m\) | Existence |
|---|---|---|
| Hub + E or C | \((7m-3)/4\) | \(m\ge1\) |
| E + E, same module | \((23m-17)/8\) | \(m\ge1\) |
| E + C, same module | \((59m-39)/20\) | \(m\ge1\) |
| E + E, different modules | \((43m-39)/16\) | \(m\ge2\) |
| E + C, different modules | \((93m-89)/36\) | \(m\ge2\) |
| C + C, different modules | \((5m-5)/2\) | \(m\ge2\) |

**Global comparison.** For every \(m\ge2\), subtracting the distinct-module C+C objective from the other four hub-free objectives, in the order E+E same, E+C same, E+E different, E+C different, yields respectively
\[
\frac{3m+3}{8},\qquad \frac{9m+11}{20},\qquad
\frac{3m+1}{16},\qquad\frac{3m+1}{36}.
\]
Each is strictly positive. Thus the best hub-free pairs for every \(m\ge2\) are precisely the \(\binom m2\) distinct-module C+C pairs. The hub-including cost is \((7m-3)/4\). Their difference \((3m-7)/4\) is negative for \(m=2\) and positive for every integer \(m\ge3\), proving cases 2 and 3. When \(m=1\), the only three orbit types have costs \(1,1,3/4\), with only the two ends of the single module attaining \(3/4\). This proves case 1 and exhausts every leader pair.

## Verification
The attached standalone `verify.py` reconstructs the full graph Laplacian using only the declared five edges per diamond, independently computes exact principal-matrix inverses over rational numbers, and compares them with both the six class formulas and a separate modular Schur-complement calculation. It exhaustively tests every two-vertex leader set for \(1\le m\le7\); it checks class representatives at larger sizes and integer sign inequalities over additional ranges. Execute `python verify.py` from the directory containing the attachment. The verified run returned `VERIFY_OK 2293 exact objective/class and sign checks` using Python's standard library. These finite checks are **not** the proof for arbitrary \(m\); the Schur calculation and signed closed-form differences above supply that proof.

## Relationship to prior work
Lin, Fardad and Jovanović (arXiv:1302.0450, first posted 2013-02-03) formulated unscaled grounded-Laplacian inverse-trace minimization and optimization relaxations for noise-free leaders. Fitch and Leonard (arXiv:1407.1569, first posted 2014-07-07) characterized general leader sets through joint centrality and explicitly analyzed paths and cycles. Patterson, Yi and Zhang (arXiv:1708.06873, first posted 2017-08-23) gave resistance-distance formulas and explicit cycle, path and perfect-tree placements. These general formulas are consistent with the present result but do not themselves evaluate and order the full six symmetry classes of \(K_1\vee(mP_3)\).

An accessible prior treatment of \(K_1\vee(mK_{r-1})\) uses clique petals rather than three-vertex paths; it does not logically imply the diamond-bouquet classification. Similarly, two-hub book graphs and Cartesian products of stars are different graph families. An equivalent graph under a different name or an unindexed specialization of a broader theorem remains possible and would take precedence if discovered. Index searches are not mathematical uniqueness proofs.

## Limitations
Only the exact unweighted, combinatorial, two-noise-free-leader setting is proved. No claim is made about arbitrary petal sizes, weighted diamonds, leader budgets other than two, stability robustness, or independent mathematical validation. One general implication of the algebra is that the complete classification has only two candidate configurations for \(m\ge2\), but this proof does not establish analogous reductions on arbitrary graph bouquets. The result has undergone self-review only, with no independent audit.

## References
1. F. Lin, M. Fardad, M. R. Jovanović, “Algorithms for leader selection in stochastically forced consensus networks,” arXiv:1302.0450, first publicly posted 2013-02-03. https://arxiv.org/abs/1302.0450
2. K. E. Fitch, N. E. Leonard, “Joint Centrality Distinguishes Optimal Leaders in Noisy Networks,” arXiv:1407.1569, first publicly posted 2014-07-07. https://arxiv.org/abs/1407.1569
3. S. Patterson, Y. Yi, Z. Zhang, “A Resistance Distance-Based Approach for Optimal Leader Selection in Noisy Consensus Networks,” arXiv:1708.06873, first publicly posted 2017-08-23. https://arxiv.org/abs/1708.06873
