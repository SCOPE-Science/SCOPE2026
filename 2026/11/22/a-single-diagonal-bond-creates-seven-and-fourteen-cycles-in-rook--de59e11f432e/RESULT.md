# A single diagonal bond creates seven- and fourteen-cycles in rook parity dynamics

## Finding
Let \(m,n\ge2\), \(q=2^h\) with \(h\ge1\), and consider the labelled \(m\times n\) rook graph \(K_m\square K_n\). Add the single previously absent undirected edge joining cells \((0,0)\) and \((1,1)\). Let \(F\) be the synchronous open-neighbor sum on \(\mathbb F_q^{mn}\) (no self-feedback). Let \(J_s(\lambda)\) denote a Jordan block, and let \(C_2(p)\) denote the six-dimensional primary companion block of \(p(z)^2\), with \(p(z)=z^3+z+1\) (equivalently, the \(\mathbb F_2[z]\)-module \(\mathbb F_2[z]/(p^2)\), extended to \(\mathbb F_q\)). The complete rational Jordan classification is:

- **Even–even, except \((m,n)=(2,2)\):** one \(J_2(1)\), two \(J_3(0)\), \(m+n-6\) copies of \(J_2(0)\), and \((m-2)(n-2)\) copies of \(J_1(0)\). At \((2,2)\), there is one \(J_2(1)\) and two \(J_1(0)\).
- **Odd–odd:** one \(J_4(1)\), one \(J_2(1)\), \(m+n-6\) copies of \(J_1(1)\), and \(mn-m-n\) copies of \(J_1(0)\).
- **Mixed parity:** write \(e\ge2\) for the even side length and \(o\ge3\) for the odd one. There is one \(C_2(p)\), \(o-3\) copies of \(J_2(0)\), and \((e-2)(o-1)\) copies of \(J_1(0)\). When \(e\ge4\), there is additionally one \(J_2(1)\) and \(e-4\) copies of \(J_1(1)\); when \(e=2\), neither extra block is present.

In particular, a **single new diagonal bond** induces genuine primitive seven- and fourteen-cycles for *every* mixed-parity board, whereas the intact rook network has no primitive period greater than two. Both-odd boards have primitive period four, and both-even boards acquire a nonzero two-cycle component despite the intact even–even rook map being nilpotent.

Put \(N=mn\), \(r_k=\operatorname{rank}F^k\), and \(r=\dim\operatorname{Per}(F)\). All first-entry counts are determined by the following ranks:

\[
\begin{array}{c|cccc|c}
 &r_0&r_1&r_2&r_3&r\\\hline
\text{even--even, not }(2,2)&N&m+n&4&2&2\\
(2,2)&4&2&2&2&2\\
\text{odd--odd}&N&m+n&m+n&m+n&m+n\\
\text{mixed, sides }e,o&N&e+o+1&e+4&e+4&e+4
\end{array}
\]

For any \(k\ge0\), the number of states first reaching recurrence *by* update \(k\) is
\[
B_k=q^{r+N-r_k}.
\]
Consequently the number first reaching recurrence *at* update zero is \(B_0=q^r\), and at update \(k\ge1\) it is \(B_k-B_{k-1}\). The maximum first-entry time is three for even–even boards other than \((2,2)\), one for \((2,2)\) and odd–odd boards, and at most two for mixed boards (sharp two when \(o\ge5\), sharp one when \(o=3,e\ge4\), and zero when \((e,o)=(2,3)\)).

The numbers \(P_d\) of *recurrent configurations* with periods dividing \(d\) are:

- Even–even: \(P_1=q\), \(P_2=q^2\).
- Odd–odd: \(P_1=q^{m+n-4}\), \(P_2=q^{m+n-2}\), \(P_4=q^{m+n}\).
- Mixed, \(e=2\): \(P_1=P_2=1\), \(P_7=q^3\), \(P_{14}=q^6\).
- Mixed, \(e\ge4\): \(P_1=q^{e-3}\), \(P_2=q^{e-2}\), \(P_7=q^e\), \(P_{14}=q^{e+4}\).

All unlisted possible periods are absent. Exact primitive orbit counts follow from \(\frac1d\sum_{j\mid d}\mu(d/j)P_j\), where \(\mu\) is the Möbius function and \(P_j\) is the number of configurations with period dividing \(j\). For each periodic orbit of length \(d\), its attraction basin contains exactly \(d q^{N-r}\) initial configurations. For the smallest mixed board \((2,3)\) over \(\mathbb F_2\), there is precisely one fixed state, one primitive seven-cycle, and four primitive fourteen-cycles, with no transient states.

## Assumptions and scope
The vertex set consists of ordered coordinates \((i,j)\), with \(0\le i<m\), \(0\le j<n\); distinct cells are adjacent when their row or column agrees. Precisely the edge between \((0,0)\) and \((1,1)\) is added, with no other changes. Any missing rook edge is conjugate to this one under row and column permutations. The dynamics is the adjacency action over a field of characteristic two, not Boolean OR, and not an oriented or self-feedback rule. Counts are for labelled configurations; an orbit count divides the number of configurations of exact period by its period. A state is recurrent if it is periodic at time zero. The primary classification is \(37B15\).

## Proof
**1. Tensor equation.** Identify the state space with \(U\otimes V\), where \(U=\mathbb F_q^m\) and \(V=\mathbb F_q^n\). Write \(J_s\) for the all-ones matrix of order \(s\), and \(E\) for the two-corner swap \(E(e_0\otimes f_0)=e_1\otimes f_1\), \(E(e_1\otimes f_1)=e_0\otimes f_0\), annihilating all other coordinate basis vectors. Characteristic two cancels the two diagonal terms of the rook adjacency, so
\[
F=J_m\otimes I_n+I_m\otimes J_n+E.
\]
Equivalently, if \(r_i\) and \(c_j\) are the row and column sums of a configuration, then
\[
(Fx)_{ij}=r_i+c_j+\mathbf1_{(i,j)=(0,0)}x_{11}+\mathbf1_{(i,j)=(1,1)}x_{00}.
\]

**2. An exact invariant decomposition valid for every size.** On either coordinate space \(\mathbb F_q^s\), split off two distinguished basis vectors \(e_0,e_1\), and write \(T_s\) for the subspace supported on the \(s-2\) other coordinates, with coordinate-sum functional \(\sigma\) and all-ones tail vector \(w\). Define an invariant *core* \(U_s\) and a complementary subspace \(R_s\) as follows.

If \(s=2\), let \(U_s=\mathbb F_q^2\) and \(R_s=0\). If \(s\ge3\) is odd, then \(\sigma(w)=1\), and set \(U_s=\langle e_0,e_1,w\rangle\), \(R_s=\ker(\sigma|_{T_s})\); hence \(\dim R_s=s-3\). If \(s\ge4\) is even, then \(\sigma(w)=0\). Choose \(R_s\subseteq\ker\sigma\) complementary to \(\langle w\rangle\) within \(\ker\sigma\), and set \(U_s=\langle e_0,e_1,e_2,w\rangle\); hence \(\dim R_s=s-4\). These spaces give a direct sum \(\mathbb F_q^s=U_s\oplus R_s\). In every case \(J_s R_s=0\), \(J_sU_s\subseteq U_s\), and the coordinate evaluations at \(e_0,e_1\) vanish on \(R_s\).

Therefore \(F\) respects the **direct sum of four invariant tensor sectors**
\[
(U_m\otimes U_n)\oplus(R_m\otimes U_n)\oplus(U_m\otimes R_n)\oplus(R_m\otimes R_n).
\]
On the first sector it is the same diagonally edited rook operator as at the representative sizes \(m_0\in\{2,3,4\}\), \(n_0\in\{2,3,4\}\) of equal parity and tail type. On the remaining three sectors it acts respectively as \(I\otimes J_{n_0}\), \(J_{m_0}\otimes I\), and zero. This gives an infinite family reduction by an explicit invariant basis, **not** an extrapolation from finitely many sampled graph sizes.

**3. Exact six core calculations.** Since the two side lengths can be interchanged, only six core pairs are needed. Their elementary-divisor blocks are obtained by integer bit-matrix multiplication and rank-nullity, with full reproducible calculations in `verify_core.py`:

\[
\begin{array}{c|l}
(m_0,n_0)&\text{core blocks}\\\hline
(2,2)&J_1(0)^2,\ J_2(1)\\
(2,3)&C_2(p)\\
(2,4)&J_3(0)^2,\ J_2(1)\\
(3,3)&J_1(0)^3,\ J_4(1),\ J_2(1)\\
(3,4)&J_1(0)^4,\ J_2(1),\ C_2(p)\\
(4,4)&J_1(0)^4,\ J_2(0)^2,\ J_3(0)^2,\ J_2(1)
\end{array}
\]

For each core, the checker constructs the adjacency matrix directly, computes the nullities of the first four powers of \(F\), \(F+I\), and \(p(F)=F^3+F+I\), and compares all of them with the displayed blocks. These three polynomials are pairwise coprime; the nullities of their successive powers determine every displayed primary block multiplicity. In particular, the six-dimensional \(C_2(p)\) is **not** just a seven-periodic block: \(p(F)\ne0\) but \(p(F)^2=0\) there, so its order is fourteen. The degree-three irreducible \(p\) has roots of multiplicative order seven over characteristic two.

**4. Assemble the complete blocks.** Over characteristic two, \(J_s\) is a rank-one idempotent when \(s\) is odd, with blocks \(J_1(1)\oplus J_1(0)^{s-1}\), and a rank-one square-zero matrix when \(s\) is even, with blocks \(J_2(0)\oplus J_1(0)^{s-2}\). Apply these formulas to the three noncore sectors in step 2 and add the applicable core blocks from step 3. Counting the sector dimensions produces exactly the parity-dependent blocks in the Finding, including all small-side exceptions. For example, the mixed-parity recurrent component is always \(C_2(p)\), with the additional unipotent blocks only when the even side has length at least four.

**5. Temporal counts.** On the nilpotent primary component, successive kernels of \(F^k\) count precisely the initial conditions entering recurrence by update \(k\); the recurrent primary component is invertible. Thus the number is \(q^{r+N-r_k}\). The periodic fixed-space dimensions follow from the primary blocks of \(F^d-I\), yielding the displayed \(P_d\). Möbius inversion gives primitive period populations. Finally, on the direct sum of nilpotent and recurrent primary spaces each phase of a recurrent orbit has \(q^{N-r}\) predecessors in its full eventual phase fiber; hence the stated attraction-basin size. All assertions hold over every finite characteristic-two field by base extension of the explicit \(\mathbb F_2\) matrices.

## Verification
Run `python3 verify_core.py` and `python3 verify_states.py` in the directory containing these files. The first checker independently forms each of the six core matrices, verifies the polynomial-nullity signatures needed to identify every elementary divisor, and verifies the full formula for all 100 size pairs \(2\le m,n\le11\) (including ranks, universal map identities, and primary nullities). The second uses direct synchronous state transitions and functional-graph exploration rather than rank calculations; it completely classifies binary configurations on boards \((2,2),(2,3),(2,4),(3,3),(3,4),(4,4)\) and all \(4^6\) configurations on \((2,3)\) over a characteristic-two four-element field. The exact recorded outputs are in `verification/core_output.txt` and `verification/states_output.txt`. The finite computational core is mathematically sufficient for the infinite theorem only because of the explicit invariant decomposition in proof step 2; larger sampled checks are supplementary.

## Relationship to prior work
Ciandrini et al. (arXiv:0809.1526v1, first public 2008-09-09) develop the linear-algebraic framework for synchronous XOR network dynamics and attractor basins, but do not give the present one-edge rook-graph classification. The published intact-rook Hamming-product and edge-parity analyses do not imply the effect of inserting a previously absent non-rook bond. The closest directly inspected published rook-graph modification concerns *deleting one square* (vertex deletion), giving a different Jordan spectrum and mixed-parity five-step transient, not period fourteen. Another directly inspected result changes an incidence in projective-plane Levi graphs and also yields a six-dimensional fourteen-periodic primary component; those bipartite incidence graphs are not the diagonally edited rook graphs, and its rank calculation does not classify the rook family. Detailed statement-and-implication comparisons and access limitations are recorded in `AUDIT.json`.

## Limitations
Only one newly inserted diagonal edge is considered. The result does not cover arbitrary multiple edges, loops, directed modifications, non-characteristic-two fields, nonlinear rules, or stochastic updates. The full classification is proved algebraically and checked by finite core computations, but no external independent validation has been performed. The literature checks do not establish historical uniqueness against every unindexed or inaccessible equivalent statement.

## References
1. L. Ciandrini, C. Maffi, A. Motta, B. Bassetti and M. Cosentino Lagomarsino, *Feedback topology and XOR-dynamics in Boolean networks with varying input structure*, arXiv:0809.1526v1, first posted 2008-09-09, https://arxiv.org/abs/0809.1526.
2. J. E. Ducey, J. Gerhard and N. Watson, *The Smith and Critical Groups of the Square Rook's Graph and its Complement*, arXiv:1507.06583, https://arxiv.org/abs/1507.06583 (intact square rook graphs and adjacency Smith invariants).
3. *A single missing rook square changes the parity dynamical phase and creates a five-step Jordan chain*, published 2026-11-01, https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-a-single-missing-rook-square-changes-the-parity-dynamical-phase--2d1032357502.
4. *A sharp parity criterion and Jordan census for edge-parity dynamics on Hamming products*, published 2026-11-01, https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-a-sharp-parity-criterion-and-jordan-census-for-edge-parity-dynam--3c8b8b447eae.
5. *A universal five-step extinction versus fourteen-cycle dichotomy from one incidence toggle*, published 2026-11-02, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-a-universal-five-step-extinction-versus-fourteen-cycle-dichotomy--be1f8ac45d72.
