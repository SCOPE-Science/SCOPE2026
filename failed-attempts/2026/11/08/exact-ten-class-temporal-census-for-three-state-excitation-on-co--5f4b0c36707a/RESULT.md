# Exact ten-class temporal census for three-state excitation on complete tripartite graphs

## Finding
For all positive integers \(a,b,c\), synchronous three-state Greenberg–Hastings excitation on the labelled complete tripartite graph \(K_{a,b,c}\) has only eventual least periods \(1\) and \(3\). Its update map satisfies \(F^7=F^4\). Every configuration enters its eventual orbit within at most four steps; the four-step bound is attained exactly when at least one shore has size at least two, while the maximum for \(K_{1,1,1}\) is three.

Let \(T\) denote the first periodic-entry time, and let \(N_{t,p}\) count labelled initial states with \(T=t\) and eventual least period \(p\). Set \(s_1=a,s_2=b,s_3=c\) and define
\[
\begin{aligned}
X&=\sum_i2^{s_i},&Y&=\sum_i3^{s_i},\\
P&=\sum_{i<j}2^{s_i+s_j},&U&=2^{a+b+c},\\
Q&=\sum_i3^{s_i}2^{a+b+c-s_i},&R&=\sum_{i\ne j}3^{s_i}2^{s_j},\\
V&=3^{a+b+c}.&&
\end{aligned}
\]
The entire first-entry census is
\[
\begin{array}{c|l}
(t,p)&N_{t,p}\\\hline
(0,1)&1\\
(0,3)&V-3Q+15U-3P+3Y-6X+12\\
(1,1)&U-1\\
(1,3)&Q-R-6U+5P+2Y-6X+6\\
(2,1)&U+Y-2X+2\\
(2,3)&Q-6U+P-2Y+4X-6\\
(3,1)&U+Y-3X+7\\
(3,3)&Q-6U+P-2Y+4X-6\\
(4,1)&Y-X-3\\
(4,3)&R-4P-4Y+10X-12.
\end{array}
\]
All omitted first-entry classes have count zero. In particular \(N_{2,3}=N_{3,3}\) for every positive shore-size triple. For equal sizes \(a=b=c=n\), independent uniform initial colors satisfy
\[
\Pr(T>0)\sim 9(4/9)^n,\qquad
\lim_{n\to\infty}\Pr(T=t\mid T>0)=\frac13\quad(t=1,2,3),
\]
while the conditional probability of \(T=4\) tends to zero. The known total eventual fixed-state population \(3(U+Y-2X+2)\) is obtained by summing the fixed-point rows; that aggregate alone is not asserted to be new.

## Assumptions and scope
The graph is finite, simple, labelled and complete tripartite, with all shore sizes strictly positive. Its states are \(0\) (resting), \(1\) (excited) and \(2\) (refractory). Under the simultaneous deterministic update a vertex in state \(1\) becomes \(2\), one in state \(2\) becomes \(0\), and one in state \(0\) becomes \(1\) if and only if a neighboring vertex is currently excited; otherwise it stays \(0\). There is no external forcing, stochasticity, self-loop, or threshold greater than one. First periodic entry means the minimal \(t\ge0\) for which \(F^t(x)\) belongs to a periodic orbit, not the time to first return to the initial state.

## Proof
**Exact quotient with vertex identity preserved.** Within one shore all vertices have the same open neighborhood, so two vertices starting in the same state in that shore follow the same state trajectory forever. A labelled initial assignment is therefore fully represented dynamically by one *labelled color representative* for each initially occupied state in each shore. For each shore choose one of seven nonempty masks \(S\subseteq\{0,1,2\}\), with corresponding ordered representatives initially taking exactly the colors in \(S\). At every update, each representative in color \(1\) becomes \(2\), each in \(2\) becomes \(0\), and a resting representative becomes excited if another shore contains a currently excited representative. This determines the trajectory of every original labelled vertex for every time. Crucially, we track the state of each representative separately; merely updating a support set could give an incorrect least period.

**Finite case analysis.** There are exactly \(7^3=343\) nonempty initial shore-mask triples. For each triple iterate the explicit update until a labelled-representative state repeats, and record its preperiod \(t\) and least period \(p\). Complete enumeration yields the following mask-triple counts, in increasing order of \(t\): at \(t=0\), \((p=1,p=3)=(1,121)\); at \(t=1\), \((26,30)\); at \(t=2\), \((32,42)\); at \(t=3\), \((28,42)\); and at \(t=4\), \((9,12)\). All 343 cases have \(t\le4\) and \(p\in\{1,3\}\). Since this is an exact quotient for every initial state on every permitted graph, it proves \(F^7=F^4\) and excludes other periods. The finite state-analysis implementation is included as `verification/quotient_certificate.py`, with exact initial-mask and update conventions, its assertion suite and its output.

**From masks to labelled populations.** For each nonempty \(S\subseteq\{0,1,2\}\), the number of initial assignments of exactly the colors in \(S\) on a shore of size \(m\ge1\) is the surjection count
\[
W_S(m)=\sum_{J\subseteq S}(-1)^{|S|-|J|}|J|^m,
\]
where \(0^m=0\). Accordingly, if \(\operatorname{class}(S_1,S_2,S_3)\) is the preperiod–least-period pair produced by the representative dynamics, then the exact population is
\[
N_{t,p}=\sum_{\substack{S_1,S_2,S_3\ne\varnothing\\\operatorname{class}(S_1,S_2,S_3)=(t,p)}}
W_{S_1}(a)W_{S_2}(b)W_{S_3}(c).
\]
This finite explicit sum is already a proof of an exact answer for all \(a,b,c\). Expanding each weight into powers with bases \(1,2,3\), the 343-term table gives coefficients of all \(27\) functions \(i^aj^bk^c\), where \(i,j,k\in\{1,2,3\}\). Grouping these coefficients by shore permutations yields precisely the ten displayed expressions. The included checker implements both constructions separately and asserts equality of every coefficient, not just equality at sampled sizes.

**Sharpness and limiting law.** The exact formula \(N_{4,1}=Y-X-3=\sum_i(3^{s_i}-2^{s_i}-1)\) vanishes precisely when all three shore sizes equal one and is positive otherwise. The quotient table shows first-entry time three is attained when all shore sizes are one. Thus the bounds are sharp. In the balanced case \(Q=3\cdot12^n\), \(R=6\cdot6^n\), \(U=8^n\), and \(V=27^n\). Consequently \(N_{1,3},N_{2,3},N_{3,3}\sim3\cdot12^n\) while all other nonperiodic classes grow at a strictly smaller exponential rate. Dividing by \(V\) proves the limiting assertions.

## Verification
Run `python3 verification/quotient_certificate.py` using Python 3.9 or later. It enumerates all 343 nonempty shore-support triples, tracks every initial color representative individually and checks all 27 coefficient terms for each displayed class. Output is in `verification/quotient_output.txt`. Independently compile and run the original-vertex implementation with `g++ -std=c++17 -O2 verification/direct_graph.cpp -o /tmp/ghm_tripartite_check && /tmp/ghm_tripartite_check`; output is in `verification/direct_output.txt`. It exhaustively evolves all \(267894\) labelled assignments over ten graph-size choices, including shore sizes \((4,4,3)\). The infinite-family theorem depends on the exact 343-case reduction plus symbolic coefficient comparison; direct vertex experiments provide independent finite corroboration only.

## Relationship to prior work
General three-color Greenberg–Hastings theorems already connect eventual synchronization to graph cycles and bound convergence times; those results are not claimed here. In particular, Gravner, Lyu and Sivakoff study general excitability, synchronization and cycle constraints. Doba gives a general account of finite-graph Greenberg–Hastings behavior. Previously determined totals for eventual consensus in three-color cyclic successor-contact dynamics on complete multipartite graphs also include the fixed-state aggregate above, despite using a different update rule. The new contribution claimed is the ten-class, three-state excitation first-entry census, its sharp four-step layer, and the balanced-family conditional temporal limit, not general period-three theory or the pre-existing aggregate.

## Limitations
The proof requires all three shores nonempty, a complete tripartite graph, three discrete states, the deterministic threshold-one Greenberg–Hastings rule and fully synchronous updates. It does not address more shores, other excitation thresholds, asynchronous systems or continuous-time limits. Exact coefficient checking has been supplied as reproducible source, but external independent mathematical validation and exhaustive historical-priority verification have not occurred. Relevant unindexed work could already contain an equivalent classification.

## References
1. J. Gravner, H. Lyu and D. Sivakoff, “Limiting behavior of 3-color excitable media on arbitrary graphs,” first posted October 24, 2016, arXiv:1610.07320, https://arxiv.org/abs/1610.07320.
2. A. Doba, “The Time Evolution of a Greenberg–Hastings Cellular Automaton on a Finite Graph,” *Complex Systems* 27 (2018), DOI:10.25088/ComplexSystems.27.2.101, https://wpmedia.wolfram.com/sites/13/2018/09/27-2-1.pdf.
3. J. M. Greenberg and S. P. Hastings, “Spatial Patterns for Discrete Models of Diffusion in Excitable Media,” *SIAM Journal on Applied Mathematics* 34 (1978), DOI:10.1137/0134040 (abstract checked).
