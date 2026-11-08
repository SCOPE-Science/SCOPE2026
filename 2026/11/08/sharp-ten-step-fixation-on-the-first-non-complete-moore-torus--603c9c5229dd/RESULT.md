# Sharp ten-step fixation on the first non-complete Moore torus

## Finding
At contact threshold \(\theta=4\), every configuration of the three-color cyclic successor cellular automaton on the periodic \(4\times4\) square lattice reaches a fixed configuration in at most ten updates. Exactly \(99,819\) of the \(3^{16}=43,046,721\) configurations are fixed, and the bound of ten is sharp.

## Assumptions and scope
Let the sites be \(V=(\mathbb Z/4\mathbb Z)^2\). A configuration is any function \(x:V\to\{0,1,2\}\). Its Moore neighborhood at \((r,c)\) comprises the eight distinct sites \((r+\delta_r,c+\delta_c)\), with \(\delta_r,\delta_c\in\{-1,0,1\}\) and \((\delta_r,\delta_c)\ne(0,0)\); all positions are reduced modulo four. In one synchronous step a site of color \(a\) becomes \(a+1\pmod3\) if at least four of its eight neighbors have color \(a+1\pmod3\); otherwise it retains \(a\). Write \(F\) for this deterministic finite map and \(\tau(x)=\min\{t\ge0:F^{t+1}(x)=F^t(x)\}\) when this set is nonempty. Then the claim is
\[
\#\operatorname{Fix}(F)=99,819,\qquad \max_{x\in\{0,1,2\}^{16}}\tau(x)=10.
\]
The \(4\times4\) square is the first square periodic Moore lattice with eight distinct neighbors in which the neighbor graph is not complete: the \(3\times3\) neighborhood graph is the complete graph on nine vertices.

## Proof
This is an exact finite enumeration proof, not an extrapolation from a sample. Encode a configuration by the integer \(s=\sum_{i=0}^{15} x_i3^i\), where \(i=4r+c\). The attached standalone C++17 program `verify.cpp` defines the transition \(\operatorname{next}(s)\) by decoding all sixteen ternary digits, counting the eight successor-color neighbors at each site, and re-encoding the simultaneously updated digits. The program iterates *all* consecutive integers from zero through \(3^{16}-1\), without exclusions or random sampling. The modular row/column address calculation makes the eight-neighbor list exact.

It computes the functional digraph's directed distance to a fixed vertex by deterministic path traversal. Each vertex is marked unseen, on the current path, or resolved with its distance to a fixed vertex. A self-loop is labeled distance zero. If an on-path vertex is revisited, the program exits with a failure (a nontrivial periodic orbit). Otherwise, on reaching a previously resolved distance, it assigns the successive distances to the path in reverse. Since a finite function has a unique outgoing edge at each vertex, these rules are exhaustive: every component is either a directed cycle with rooted in-trees, or a fixed-point tree. The completed scan encounters no nontrivial directed cycle, and the largest assigned distance is exactly ten. The program separately checks every distance is resolved and reports \(3^{16}\) states, \(99,819\) fixed vertices, maximal transient ten, and exact depth sum \(110,746,398\). The source is fully self-contained and uses only standard C++17.

The independent `check_fixed.cpp` uses a distinct row-triple calculation: it enumerates all \(3^4=81\) possible row words, marks a triple of consecutive rows admissible if none of the four sites of its middle row has four or more successor neighbors, and counts four-row cyclic words for which all four row triples are admissible. This second finite calculation independently yields exactly \(99,819\) fixed configurations.

For sharpness, the initial rows
\[
(2,1,2,1),\quad(2,1,0,2),\quad(1,2,1,0),\quad(0,0,0,0)
\]
undergo exactly ten nontrivial updates before becoming the all-one fixed state. The full step-by-step state and changing-site counts are provided in `witness_trace.txt`, and are reproduced from the update rule.

## Verification
Compile `verify.cpp` and `check_fixed.cpp` separately using `g++ -O3 -std=c++17` and run both binaries. The expected final lines are `VERIFY_OK states=43046721 fixed=99819 max_transient=10 maximizing_state=109805 sum_transient=110746398` and `CHECK_FIXED_OK fixed=99819`. The principal verifier uses two bytes per encoded state for distances and detects a cycle explicitly; it does not assume stabilization. The second checker independently evaluates the fixed-state criterion using the row structure. Both checks executed successfully on the included source. The programs are exact integer computations, not floating-point simulations.

## Relationship to prior work
Muñoz and Nuño, *Symmetry-resolved periods in a cyclic-dominance automaton* (arXiv:2610.37990v1, 27 October 2026), define this precise update law (Section II) and report that more than \(99.5\%\) of sampled runs freeze at \(\theta\ge4\), with no observed oscillating attractor (Section V.13 and Supplement S3). That is empirical, and does not imply uniform fixation of all configurations or a sharp ten-step transient on this torus. Fisch, Gravner and Griffeath's foundational study supplies the cyclic-automaton context and bootstrap threshold; it does not supply the stated exhaustive finite-state census. A general strict-majority finite-graph Lyapunov argument applies for eight neighbors only when \(\theta\ge5\); the present critical case \(\theta=4\) lies outside that hypothesis.

## Limitations
Only the exact finite \(4\times4\), three-color, radius-one, synchronous, periodic system with threshold four is classified. There is no claim that larger tori fixate or that their convergence time is uniformly bounded. Exhaustive finite checking is an exact proof for this finite set because the code visits every state and checks cycles; it is not an infinite-lattice proof. Historical priority is provisional, especially against specialized studies of finite cyclic-automaton functional digraphs.

## References
1. F. J. Muñoz and J. C. Nuño, *Symmetry-resolved periods in a cyclic-dominance automaton: separating intrinsic from lattice-induced periodicity*, arXiv:2610.37990v1 (first public 2026-10-27), Sections II and V.13, https://arxiv.org/html/2610.37990v1.
2. R. Fisch, J. Gravner, and D. Griffeath, *Threshold-range scaling of excitable cellular automata* (1991), cited in reference 1, Sections I and II.
3. H. Matamala and E. Goles, *Dynamic Behavior of Cyclic Automata Networks* (1997), cited in reference 1, Section I; relevant historical context, complete text not available during comparison.
