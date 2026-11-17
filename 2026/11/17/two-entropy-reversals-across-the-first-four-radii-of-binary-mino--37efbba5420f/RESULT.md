# Two entropy reversals across the first four radii of binary minority dynamics

## Finding
For binary synchronous minority dynamics on a ring, using the distinct open neighbors at distances \(1,\ldots,r\) on both sides and retaining the incumbent bit in an exact tie, let \(M_r(n)\) denote the number of labelled fixed configurations on a ring of \(n>2r\) vertices. The exponential growth constants
\[
\rho_r=\lim_{n\to\infty}M_r(n)^{1/n}
\]
exist for each \(r\in\{1,2,3,4\}\) and obey **two successive reversals**:
\[
\boxed{\rho_1<\rho_2>\rho_3<\rho_4}.\]
In particular, increasing the interaction radius does not change the entropy of fixed minority configurations monotonically, even over the first four ranges. Strict rational enclosures are
\[
\begin{array}{c|c|c}
r&\text{strict lower bound on }\rho_r&\text{strict upper bound on }\rho_r\\\hline
1&1.6180&1.6181\\
2&1.6663&1.6664\\
3&1.6576&1.6577\\
4&1.6593&1.6594
\end{array}
\]
Moreover, each exact finite-ring count is the trace of an explicitly defined binary de Bruijn subgraph adjacency matrix. The dominant eigenvalue has leading coefficient one: \(M_r(n)=\rho_r^n(1+o(1))\) for each fixed radius in this range.

## Assumptions and scope
The ring is the simple cycle on labelled sites \(i\in\mathbb Z/n\mathbb Z\), where \(n>2r\); this ensures all \(2r\) neighboring sites are distinct. The state space is \(\{0,1\}^n\). At each update, a vertex adopts the less frequent binary opinion among its \(2r\) open neighbors; in a tie it retains its own opinion. Thus a configuration is fixed precisely when each site has **at least \(r\)** neighbors whose state differs from its own. The entropy here is the *spatial growth rate of fixed configurations*, not the temporal entropy of the full map, nor a count of two-cycles or attraction basins.

## Proof
Fix \(r\in\{1,2,3,4\}\). Define \(A_r\) with rows and columns indexed by binary words \(u=(u_0,\ldots,u_{2r-1})\). For every appended symbol \(v\in\{0,1\}\), insert the edge
\[
(u_0,\ldots,u_{2r-1})\longrightarrow(u_1,\ldots,u_{2r-1},v)
\]
if the central symbol \(u_r\) in the length-\(2r+1\) window \((u_0,\ldots,u_{2r-1},v)\) disagrees with at least \(r\) of the other \(2r\) symbols. Let the corresponding matrix entry be one, otherwise zero. Because the window is centered at the site being updated, the local edge condition is exactly the fixed-state inequality. Sliding all length-\(2r\) windows around the ring provides a bijection between indexed fixed configurations and rooted closed walks of length \(n\). Hence
\[
M_r(n)=\operatorname{tr}(A_r^n),\qquad n>2r.
\]
The finite directed graphs of \(A_r\) have, respectively, \(4,16,64,256\) vertices and \(6,22,84,326\) edges. Exact exhaustive strongly-connected-component analysis gives one nontrivial component of respective sizes \(4,14,50,184\). All remaining vertices belong to singleton acyclic components without self-loops. In each nontrivial component the gcd of lengths of closed directed walks is one; hence the component is primitive. Consequently \(A_r\) has a unique simple positive spectral-radius eigenvalue \(\rho_r\), all other eigenvalues having smaller modulus. The trace identity proves the existence of the limit and \(M_r(n)=\rho_r^n(1+o(1))\).

For an exact eigenvalue separation, restrict each adjacency matrix to its primitive component \(B_r\), set \(w_r=B_r^{50}\mathbf1\), and observe that every entry of \(w_r\) is a positive integer. Direct integer arithmetic establishes the **strict componentwise inequalities**
\[
L_r w_r<10000 B_rw_r<U_r w_r,
\]
where \((L_1,U_1)=(16180,16181)\), \((L_2,U_2)=(16663,16664)\), \((L_3,U_3)=(16576,16577)\), and \((L_4,U_4)=(16593,16594)\). The Collatz–Wielandt bounds for irreducible nonnegative matrices therefore imply \(L_r/10000<\rho_r<U_r/10000\). Comparing these disjoint intervals yields both reversals, with no reliance on floating-point eigenvalues.

## Verification
The self-contained Python 3 file `verify.py` constructs every transition by the exact local minority inequality, computes strongly connected components and their cycle-length gcd using only integer operations, verifies all strict Perron inequalities using \(B_r^{50}\mathbf1\), and independently compares direct enumeration to transfer-matrix traces for four consecutive allowable ring lengths at each radius. The exact output is recorded in `verification_output.txt`. In particular the direct counts on the smallest four rings are \((6,6,10,20)\), \((20,26,28,62)\), \((70,70,72,122)\), and \((252,272,198,348)\) for radii one through four respectively. These finite checks supplement, rather than replace, the transfer-matrix proof for all ring lengths.

## Relationship to prior work
Wolfram's 1983 survey establishes the classical cellular-automaton setting. Nakar and Ron analyze one-dimensional majority configurations and an associated minority rule, including spatial structure of eventual cycles; their model uses a \(2r+1\)-site neighborhood including the site itself, whereas the current fixed-point count uses \(2r\) distinct open neighbors with tie retention. Their results do not state the spatial fixed-state growth rates compared here. A previously indexed exact spectrum on squared cycles already gives the radius-two minority rate \(1.6663019373\ldots\); that single-radius result is expressly treated as prior art, not reclaimed here. The new comparison requires the independently certified radii three and four and two strict changes of sign.

## Limitations
Only radii \(1\) through \(4\) are classified; no eventual monotonicity or oscillation claim for larger radii follows. The full dynamics, basin sizes, and primitive temporal periods are not counted. The nearby published squared-cycle work was available in indexed summary rather than its full primary text, so a previously unindexed stronger result remains a historical-priority risk. Mathematical verification is internal and is not an independent audit.

## References
1. S. Wolfram, *Statistical mechanics of cellular automata*, Reviews of Modern Physics 55 (1983), 601–644, DOI: https://doi.org/10.1103/RevModPhys.55.601. Published 1983-07-01.
2. Y. Nakar and D. Ron, *The Structure of Configurations in One-Dimensional Majority Cellular Automata: From Cell Stability to Configuration Periodicity*, 2022, https://arxiv.org/abs/2205.08972 (first posted 2022-05-18). See Sections 1.1, 1.5 and 4.
3. *Exact fixed-state spectra and an entropy gap on squared cycles*, publicly indexed research record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-exact-fixed-state-spectra-and-an-entropy-gap-on-squared-cycles--e12f8e4fef4a . Radius-two rate only; full text not accessible during comparison.
