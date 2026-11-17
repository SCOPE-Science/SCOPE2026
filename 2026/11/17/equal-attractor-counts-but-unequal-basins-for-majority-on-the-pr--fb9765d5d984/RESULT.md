# Equal attractor counts but unequal basins for majority on the prism and Desargues graphs

## Finding

Let \(F_k\) denote synchronous binary open-neighbor majority on \(GP(10,k)\), with \(k\in\{1,3\}\). Both the decagonal prism \(GP(10,1)\) and the Desargues graph \(GP(10,3)\) have exactly \(124\) fixed configurations, \(7{,}626\) primitive temporal two-cycle orbits, and sharp maximum first periodic-entry time \(4\). Nevertheless, the exact populations of initial states eventually reaching **some fixed configuration** are respectively

\[
\boxed{|\mathcal B_{\rm fixed}(GP(10,1))|=36{,}784,\qquad
|\mathcal B_{\rm fixed}(GP(10,3))|=107{,}224.}
\]

Thus exchanging the inner-ring step triples the fixed-attraction population approximately (the exact ratio is \(107224/36784\)) without changing **any** of the total numbers of fixed points or primitive two-cycles. The two-cycle basin populations are \(1{,}011{,}792\) and \(941{,}352\), respectively. The fixed-state population is the same, but its Hamming-weight distribution is not: the prism has fixed configurations of weights \(4,8,12,16\), whereas Desargues has none at those weights.

The full, labelled first periodic-entry census is:

| First entry \(t\) | Prism: period one | Prism: period two | Desargues: period one | Desargues: period two |
|:--:|--:|--:|--:|--:|
| 0 | 124 | 15,252 | 124 | 15,252 |
| 1 | 8,710 | 485,710 | 2,940 | 129,140 |
| 2 | 14,750 | 366,590 | 24,480 | 442,720 |
| 3 | 8,560 | 108,320 | 32,640 | 169,920 |
| 4 | 4,640 | 35,920 | 47,040 | 184,320 |

All counts refer to labelled bit assignments, with temporal phases counted separately in state populations but not in orbit populations.

## Assumptions and scope

For \(k=1\) or \(3\), define the simple undirected cubic generalized Petersen graph \(GP(10,k)\) on \(u_i,v_i\), \(i\in\mathbb Z/10\mathbb Z\), with edges \(u_iu_{i+1}\), \(u_iv_i\), and \(v_iv_{i+k}\) for all \(i\). Index order is part of the label; every configuration is a function from the 20 vertices to \(\{0,1\}\). At each integer time, every vertex takes the majority of its three *distinct graph neighbors* simultaneously; there is no inertia or randomized tie breaking. For an initial assignment \(x\), the first entry time is the smallest \(t\ge0\) such that \(F_k^{t+2}(x)=F_k^t(x)\); at that time its eventual least period is either one or two. The fixed-state basin is the set of all initial assignments for which that least period is one.

## Proof

Both graphs are bipartite because the inner step \(k\) is odd and the horizontal circumference is even. Partition their vertices into two ten-vertex shores

\[
A=\{u_i:i\text{ even}\}\cup\{v_i:i\text{ odd}\},\quad
B=\{u_i:i\text{ odd}\}\cup\{v_i:i\text{ even}\}.
\]

Write \(U:\{0,1\}^B\to\{0,1\}^A\) and \(V:\{0,1\}^A\to\{0,1\}^B\) for the coordinatewise majority maps induced by the explicit neighbor sets. For \(a\in\{0,1\}^A\) and \(b\in\{0,1\}^B\),

\[
F_k(a,b)=(U(b),V(a)),\qquad F_k^2(a,b)=(T_A(a),T_B(b)),
\quad T_A=U\circ V,\;T_B=V\circ U.
\]

Every one of the \(2^{10}=1{,}024\) shore assignments is explicitly enumerated by `verify_reduced_gp.py` from the three-neighbor sets. For **both** \(k\) values, each of the two maps \(T_A,T_B\) has exactly 124 fixed assignments and satisfies the *complete* finite identity \(T_A^3=T_A^2\), \(T_B^3=T_B^2\). It follows for all \(2^{20}\) assignments that \(F_k^6=F_k^4\), hence no periods above two and first periodic entry at most four. The first-entry table above exhibits positive population at time four, proving sharpness.

The fixed configurations of \(F_k\) are in bijection with \(a\in\operatorname{Fix}(T_A)\), via \(a\mapsto(a,V(a))\). Meanwhile the two-step return set is \(\operatorname{Fix}(T_A)\times\operatorname{Fix}(T_B)\). Consequently

\[
\#\operatorname{Fix}(F_k)=124,\quad
\#\operatorname{Fix}(F_k^2)=124^2=15{,}376,\quad
\#\text{primitive two-orbits}=\frac{15{,}376-124}{2}=7{,}626.
\]

For each shore, the maps \(T_A,T_B\) attain a fixed point within at most two iterations. Let \(s_A(a)=T_A^2(a)\), \(s_B(b)=T_B^2(b)\) be their terminal projections, and set

\[
p_A(z)=\#\{a:s_A(a)=z\},\qquad
p_B(w)=\#\{b:s_B(b)=w\}.
\]

The initial full state \((a,b)\) eventually reaches a fixed configuration of \(F_k\) **if and only if** \(s_A(a)=U(s_B(b))\). Thus the basin population is exactly the *finite and reproducible* integer sum

\[
\sum_{w\in\operatorname{Fix}(T_B)}p_B(w)\,p_A(U(w)).
\]

Evaluating these \(1{,}024\)-element terminal maps yields \(36{,}784\) for \(k=1\) and \(107{,}224\) for \(k=3\). These exact calculations are independently confirmed by the direct enumeration of all \(1{,}048{,}576\) full assignments per graph in `verify_full_gp.cpp`. That independent program constructs the original twenty neighbor masks and iterates the uncompressed update map; no bipartite factorization is used. Both methods independently reproduce all table entries and the Hamming-weight profile.

For clarity, the numbers of fixed configurations at each occupied-vertex weight are:

| Weight | Prism | Desargues |
|--:|--:|--:|
| 0 | 1 | 1 |
| 4 | 10 | 0 |
| 6 | 10 | 20 |
| 8 | 25 | 0 |
| 10 | 32 | 82 |
| 12 | 25 | 0 |
| 14 | 10 | 20 |
| 16 | 10 | 0 |
| 20 | 1 | 1 |

The complete raw orbit-flip and first-entry histograms are reproduced by both included programs.

## Verification

Run `python3 verify_reduced_gp.py` and `g++ -O3 -std=c++17 verify_full_gp.cpp -o verify_full_gp && ./verify_full_gp`. Compare standard output with the separately embedded `verification_reduced_output.txt` and `verification_full_output.txt`. Both programs enumerate finite sets exhaustively, assert intermediate cardinalities, and report exact integers; no sampling, floating-point inference, or unsupported finite-to-infinite extrapolation is used. The complete execution is limited to the two explicitly defined 20-vertex graphs.

## Relationship to prior work

The finite-graph period-at-most-two property is classical (Goles–Olivos); recent general analyses study convergence times, influence and random-graph behavior [1,2]. The classical graphs and their identification are documented in [3]. A prior exact all-circumference prism majority recurrence census already implies the prism's \(124\) fixed states and \(7{,}626\) two-cycle orbits and is *not* presented here as a new count. The new comparison is the **coincidence** of the two recurrent-state totals with the Desargues graph, together with a highly unequal fixed-attraction basin, the contrasting fixed-state weight spectra and the complete paired entry-time tables. General convergence-to-period-two theorems, a prism recurrent count by itself and the separate dodecahedral-graph majority census do not imply these graph-specific joint numbers.

## Limitations

This is an exact classification of two finite labelled graphs only. It makes no all-circumference claim about \(GP(n,3)\), other generalized Petersen graphs, or any stochastic voting rule. It neither identifies all graph-automorphism classes nor claims a general relation between graph girth and basin size. Novelty remains subject to unindexed historic enumerations and inaccessible individual public research files; mathematical verification described here is reproducible but not independent external certification.

## References

1. Itai Benjamini, Siu-On Chan, Ryan O’Donnell, Omer Tamuz and Li-Yang Tan, “Convergence, unanimity and disagreement in majority dynamics on unimodular graphs and random graphs,” arXiv:1405.2486, first posted 2014-05-11. https://arxiv.org/abs/1405.2486
2. Dominik Kaaser, Frederik Mallmann-Trenn and Emanuele Natale, “On the Voting Time of the Deterministic Majority Process,” arXiv:1508.03519, first posted 2015-08-14. https://arxiv.org/abs/1508.03519
3. Eric W. Weisstein, “Desargues Graph,” MathWorld, https://mathworld.wolfram.com/DesarguesGraph.html (the graph identification, not the dynamics).
4. E. Goles and J. Olivos, “Periodic behaviour of generalized threshold functions,” Discrete Mathematics 30 (1980), 187–189. https://doi.org/10.1016/0012-365X(80)90121-1 (general period-at-most-two antecedent).
