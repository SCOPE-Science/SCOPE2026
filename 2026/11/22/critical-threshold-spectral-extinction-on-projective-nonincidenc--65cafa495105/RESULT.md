# Critical-threshold spectral extinction on projective nonincidence graphs and a sharp Fano census

## Finding
Let \(\Pi\) be **any** finite projective plane of even order \(q\ge2\), whether Desarguesian or not. Let \(H_\Pi\) be its bipartite point–line **nonincidence** graph: a point and a line are adjacent exactly when the point is not on the line. Every vertex has degree \(q^2\). Under synchronous three-state Greenberg–Hastings excitation with contact threshold \(\theta=q^2/2\), **every** initial configuration eventually reaches the all-rest state. This is the exact half-degree threshold, where the previously established strict-density extinction criterion is inapplicable.

For the order-two plane, label the seven points \(0,\ldots,6\) and lines \(7,\ldots,13\); line \(7+k\) contains points \(k,k+1,k+3\pmod7\). Every one of the \(3^{14}=4{,}782{,}969\) configurations of the resulting four-regular nonincidence graph reaches rest by its **seventh** synchronous update, and the seven-update bound is sharp. The exact first all-rest time populations for times \(0,1,\ldots,7\) are respectively
\[
(1,16383,803001,2393358,1107890,364518,90258,7560).
\]
Thus the global map on this graph satisfies \(F^7(x)=\mathbf0\) for every configuration, but \(F^6\) is not identically zero.

## Assumptions and scope
The plane has \(v=q^2+q+1\) points and the same number of lines. Graph vertices are the \(2v\) separately labelled point and line objects; no loops or parallel edges are present. States are \(0\) resting, \(1\) excited, and \(2\) refractory. At each simultaneous update \(1\mapsto2\mapsto0\); a resting vertex changes to \(1\) iff at least \(\theta\) **distinct** neighbors were excited immediately before updating, and otherwise remains resting. For even \(q\), \(\theta=q^2/2\) is an integer. Universal extinction is an eventual-time theorem, not a uniform time bound for arbitrary \(q\); the sharp bound of seven updates refers only to \(q=2\).

## Proof
**1. A critical-degree excitation rigidity identity.** Consider any finite undirected \(2\theta\)-regular graph under this rule, with \(\theta\ge1\). Write \(E_t\) for the vertices excited at integer time \(t\). For every \(t\ge1\), the sets \(E_{t-1}\) and \(E_{t+1}\) are disjoint: a vertex excited at \(t-1\) is refractory at \(t\) and resting at \(t+1\). Every vertex of \(E_t\) was newly excited by at least \(\theta\) neighbors in \(E_{t-1}\). Therefore it has at most \(\theta\) neighbors in \(E_{t+1}\). Conversely, every vertex of \(E_{t+1}\) has at least \(\theta\) neighbors in \(E_t\). Counting edges between successive excited sets from both endpoints yields
\[
\theta|E_{t+1}|\le e(E_t,E_{t+1})\le\theta|E_t|,\qquad t\ge1.
\]
In a periodic trajectory the cardinalities \(|E_t|\) are consequently constant, since a periodic nonincreasing integer sequence is constant. Equality holds throughout. Each vertex in \(E_t\) has exactly \(\theta\) neighbors in each disjoint set \(E_{t-1}\) and \(E_{t+1}\), exhausting all its \(2\theta\) neighbors, while each vertex in either neighboring time-set has exactly \(\theta\) neighbors in \(E_t\). With \(A\) the adjacency matrix and \(u_t\) the zero-one column indicator of \(E_t\), this proves the **all-vertex** vector identity
\[
A u_t=\theta(u_{t-1}+u_{t+1})
\]
on every periodic orbit (including the zero orbit). In particular, any nonzero periodic orbit has a nonempty excited set; otherwise excitation cannot restart.

**2. Fourier spectral obstruction.** Let such an orbit have period \(p\). For a \(p\)-th root of unity \(\zeta\), write \(\widehat u(\zeta)=\sum_{t=0}^{p-1}u_t\zeta^{-t}\). Fourier transformation of the vector identity gives
\[
A\widehat u(\zeta)=\theta(\zeta+\zeta^{-1})\widehat u(\zeta).
\]
Thus each nonzero temporal Fourier mode requires the adjacency eigenvalue \(\lambda=\theta(\zeta+\zeta^{-1})\). If the only admissible roots \(\zeta\) are \(1\) and \(-1\), Fourier inversion implies \(u_{t+2}=u_t\). But excitation events at a fixed vertex cannot occur only two updates apart. Therefore no nonzero periodic orbit can exist in that case.

**3. Exact nonincidence spectrum.** Let \(B\) be the square point-versus-line nonincidence matrix of an order-\(q\) projective plane. Every row has \(q^2\) ones. Distinct points have exactly \(q(q-1)\) common nonincident lines: among the \(q^2+q+1\) lines, their two incidence pencils have union \(2(q+1)-1\). Therefore
\[
BB^{\mathsf T}=qI+q(q-1)J.
\]
The single constant eigenvector has eigenvalue \(q^4\); every perpendicular vector has eigenvalue \(q\). Hence the adjacency matrix \(A=\left(\begin{smallmatrix}0&B\\B^{\mathsf T}&0\end{smallmatrix}\right)\) has exactly the spectral values \(\pm q^2\) and \(\pm\sqrt q\). At \(\theta=q^2/2\), the nontrivial spectral ratios are
\[
\frac{\lambda}{\theta}=\pm\frac{2}{q^{3/2}}.
\]
They cannot equal \(\zeta+\zeta^{-1}\) for any root of unity \(\zeta\): such a sum is an algebraic integer, whereas its squared value would be the noninteger rational \(4/q^3\), strictly between zero and one for every \(q\ge2\). A rational algebraic integer must be an integer. Consequently, only \(\lambda=\pm q^2\) can occur, giving \(\zeta+\zeta^{-1}=\pm2\), hence \(\zeta=\pm1\). By step 2, no nonzero periodic trajectory exists. Every trajectory in this finite deterministic state space eventually enters an orbit. The unique orbit is the fixed all-rest configuration, proving universal extinction.

**4. Sharp order-two classification.** For \(q=2\), the lines of the Fano plane can be taken as \(\{k,k+1,k+3\}\pmod7\). A first exhaustive program, `verification/coheawood_a.cpp`, independently builds all nonincidence edges using the complementary differences \(\{2,4,5,6\}\), constructs the transition of **each** of the \(3^{14}\) ternary states, and peels its functional graph. It finds only the all-rest fixed point as a recurrent component and records the eight populations asserted above. An independently implemented bitmask-forward program, `verification/coheawood_b.cpp`, builds adjacency by directly testing the three incident offsets and simulates every state through the first occurrence of rest, recovering exactly the same populations. The two exhaustive algorithms agree on all 4,782,969 states; they are finite certificates of the order-two distribution, not a proof substitute for step 3. The second program finds an explicit maximal-time witness, integer \(82105\) in least-significant-digit-first ternary encoding. Its successive fourteen-character state words from times zero through seven are
```
12212111011000
20020222122111
01101000200222
02202001011000
10000112022000
20000220100000
00000000200000
00000000000000
```
so the bound seven is attained. The standalone `verification/verify_design.py` confirms independently the incidence Gram identities at orders two and four and reproduces the witness by direct Python updates.

## Verification
Compile the two independent C++17 programs with `g++ -std=c++17 -O3 -o a verification/coheawood_a.cpp` and similarly for `coheawood_b.cpp`; run each and compare standard output byte-for-byte with `verification/coheawood_a.out` and `verification/coheawood_b.out`. The checker uses no external libraries. Run `python3 verification/verify_design.py` and compare standard output with `verification/verify_design.out`. Each calculation has been performed on these source files. Because \(3^{14}\) states are exhausted exactly, the finite claims are exhaustive rather than estimates. The all-order theorem is proved by the critical-degree identity and exact spectral obstruction in steps 1–3.

## Relationship to prior work
The 1993 public papers of Durrett–Griffeath [1] and Fisch–Gravner–Griffeath [2] motivate multi-contact excitable cellular automata, principally on spatial lattices. The latter's accessible text was examined in detail; it does not state the spectral extinction phenomenon on projective nonincidence graphs. Gravner–Lyu–Sivakoff [3] concerns one-contact three-color dynamics, not the present half-degree threshold.

The published **maximum induced-density extinction condition** [4] states extinction when \(\rho(G)<\theta\). Here \(H_\Pi\) is \(q^2\)-regular, so \(\rho(G)=q^2/2=\theta\), at exact equality. Its graph family is therefore not covered by that condition, and in fact the same threshold on the same-degree complete bipartite graph \(K_{q^2,q^2}\) admits a primitive four-cycle. A published **sharp contraction estimate** [5] assumes \(\theta>\Delta/2\), so is also inapplicable. Published **half-degree initial period-three rigidity** [6] only characterizes three-cycles, not higher temporal periods or the universal extinction basin. Previously indexed Heawood excitation classifications [7] use the **incidence** rather than **nonincidence** graph and different thresholds; the graph is not interchangeable with the present one. These are scientific nonimplication comparisons, not proofs that every possible equivalent historical result has been indexed.

## Limitations
The theorem applies to bipartite nonincidence graphs of finite projective planes of **even order** only, with precisely three states and threshold \(q^2/2\). It does not assert a sharp relaxation time for higher orders, a universal critical-threshold theorem on all regular graphs, or a stochastic model. The Fano census is for the stated labelled graph, not an orbit quotient under automorphisms. A plausible earlier result in an unindexed source cannot be categorically excluded; the 1993 Durrett–Griffeath work was available here principally in abstract form. Independent external mathematical validation remains outstanding.

## References
[1] R. Durrett and D. Griffeath, *Asymptotic Behavior of Excitable Cellular Automata*, public arXiv version 1993-03-22, https://arxiv.org/abs/patt-sol/9303002.

[2] J. Fisch, J. Gravner and D. Griffeath, *Threshold-Range Scaling of Excitable Cellular Automata*, public arXiv version 1993-04-02, https://arxiv.org/abs/patt-sol/9304001; accessible full text https://www.math.ucdavis.edu/~gravner/papers/fgg.pdf.

[3] J. Gravner, H. Lyu and D. Sivakoff, *Limiting behavior of 3-color excitable media on arbitrary graphs*, arXiv:1610.07320, first public version 2016-10-24, https://arxiv.org/abs/1610.07320.

[4] *A densest-subgraph threshold and finite excitation budget for three-state graph dynamics*, publicly indexed mathematical result, 2026-10-25, https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-a-densest-subgraph-threshold-and-finite-excitation-budget-for-th--352367f51e91.

[5] *Sharp logarithmic extinction clocks above the half-degree excitation threshold*, publicly indexed mathematical result, 2026-11-17, https://github.com/published-finding corpus/2026/tree/main/2026/11/17/SCOPE-sharp-logarithmic-extinction-clocks-above-the-half-degree-excita--661b1e5fd561.

[6] *Half-degree rigidity and a sharp contact-threshold collapse on squared cycles*, publicly indexed mathematical result, 2026-11-08, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-half-degree-rigidity-and-a-sharp-contact-threshold-collapse-on-s--7c3fe196f42d.

[7] *Exact Heawood excitation census: eight primitive periods and a ten-step maximal transient*, publicly indexed mathematical result, 2026-11-08, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-exact-heawood-excitation-census-eight-primitive-periods-and-a-te--29120402709f.
