# Almost every initial state requires two sequential NOR sweeps on a cycle

## Finding

For every integer \(n\ge3\), synchronously **not** updating, but instead visiting the labelled vertices \(0,1,\ldots,n-1\) of the undirected cycle \(C_n\) in that order once per sweep and setting the current vertex to one exactly when *both of its current neighbors are zero*, let \(S_n\) denote the resulting one-sweep map on \(\{0,1\}^n\). Every input is fixed by the end of its second sweep, so \(S_n^3=S_n^2\). Let \(P_n\) be the number of fixed initial configurations and let \(R_n\) count the initial configurations with \(S_n^2(x)=S_n(x)\). The complete first-fixed-entry population at sweeps \(0,1,2\) is
\[
\boxed{\big(P_n,\ R_n-P_n,\ 2^n-R_n\big).}
\]
The following initial values and recurrences determine the count exactly for every circumference:
\[
\begin{split}
&(P_3,P_4,P_5)=(3,2,5),\qquad P_n=P_{n-2}+P_{n-3}\quad(n\ge6),\\
&(R_3,R_4,R_5)=(8,10,26),\qquad R_n=2R_{n-2}+2R_{n-3}\quad(n\ge6).
\end{split}
\]
The sharp worst-case number of sweeps is one when \(n=3\), and two for every \(n\ge4\). If the initial bits are uniformly independent, the probability that two sweeps are actually required tends to one exponentially: specifically, it is \(1-\Theta((\rho/2)^n)\), where \(\rho=1.769292354\ldots\) is the positive real root of \(\rho^3-2\rho-2=0\). The all-graph two-sweep guarantee and the connection between fixed states and maximal independent sets were known; the exact first-entry population, weighted three-state transfer and exponential concentration law on labelled cycles are the claims here.

## Assumptions and scope

The cycle is simple, undirected and loopless; for \(n=3\), the two neighbors of each vertex are distinct. All states are binary. Each visit reads the two neighbors' **currently visible** bits and does not read the visited vertex's own previous bit. Each complete sweep visits vertices in increasing label order \(0,1,\ldots,n-1\), once each, and this identical order is repeated. First-fixed-entry means the least \(t\ge0\) such that \(S_n^t(x)\) is a fixed configuration. Fixed configurations are precisely characteristic functions of maximal independent sets, equivalently cyclic binary words avoiding adjacent ones and cyclic runs of three zeros. The expressions \(P_n,R_n\) count labelled bitstrings, not rotation classes.

## Proof

**General two-sweep bound.** During the first sweep, a vertex is left at one only if its earlier updated neighbors are zero and its later unvisited neighbors were zero. Thus after that sweep no edge has two ones: if an adjacent pair were one, the later-visited vertex would have seen the first one and changed to zero. An independent configuration remains independent under each future local NOR update, since activating a vertex requires every neighbor to be zero. Furthermore a one which survives the first sweep has no active neighbor, so once an independent configuration is obtained, subsequent updates cannot deactivate an active vertex. During the next sweep, all remaining zeros without an active neighbor are activated when visited; at its end the configuration is independent and dominating, hence maximal independent and fixed. This is the known all-graph two-permutation argument.

**Exact count in the first sweep.** Write input \(x\) and first-sweep output \(y\), with indices modulo \(n\). The sequential equations are
\[
y_0=\neg(x_{n-1}\lor x_1),\quad y_i=\neg(y_{i-1}\lor x_{i+1})\ (1\le i\le n-2),\quad y_{n-1}=\neg(y_{n-2}\lor y_0).
\]
The input bit \(x_0\) is unused and contributes a factor two. The output \(y\) is already fixed exactly when all cyclic triples avoid \(000\) and both neighboring pairs avoid \(11\).

Order the admissible two-bit contexts as \(00,01,10\). A transition \((u,p)\to(p,q)\) is allowed if \((u,p,q)\) is a fixed-output-admissible triple. Its weight is the number of possibilities for the input bit \(x_{i+1}\) making \(q=\neg(p\lor x_{i+1})\); the weight is two for \((p,q)=(1,0)\) and one for \((p,q)=(0,0),(0,1)\). The resulting ordinary transfer matrix is
\[
T=\begin{pmatrix}0&1&0\\0&0&2\\1&1&0\end{pmatrix}.
\]
The seam must account for the first two output equations and the last output equation together, rather than treating the sweep as a simultaneous periodic rule. For \(p,q,r\in\{0,1\}\), let
\[
W(p,q,r)=\#\{(a,b)\in\{0,1\}^2:q=\neg(p\lor a),\ r=\neg(a\lor b)\}.
\]
The nonzero weights are \(W(0,0,0)=2\), \(W(0,1,0)=W(0,1,1)=1\), \(W(1,0,0)=3\), and \(W(1,0,1)=1\). For contexts \((u,p)\) and \((s,r)\), sum \(W(p,q,r)\) over both values of \(q\) subject to admissibility of the triples \((u,p,q)\), \((p,q,s)\), \((q,s,r)\) and the seam relation \(s=\neg(q\lor r)\). This gives the boundary matrix
\[
D=\begin{pmatrix}1&1&0\\0&1&3\\1&1&2\end{pmatrix}.
\]
The \(n-3\) ordinary transitions and one seam transition form a closed context walk. Hence, including the freely chosen \(x_0\), the **exact** count is
\[
\boxed{R_n=2\operatorname{tr}(T^{n-3}D)}\qquad(n\ge3).
\]
This formula includes the triangle \(n=3\) (empty ordinary-transition product). Direct multiplication gives \(T^3=2T+2I\); therefore \(R_n=2R_{n-2}+2R_{n-3}\). Evaluation at \(n=3,4,5\) gives \(8,10,26\).

**Initially fixed states.** The unweighted same-context transfer
\[
U=\begin{pmatrix}0&1&0\\0&0&1\\1&1&0\end{pmatrix}
\]
counts each cyclic maximal-independent-set word once: \(P_n=\operatorname{tr}(U^n)\). Since \(U^3=U+I\), its trace satisfies \(P_n=P_{n-2}+P_{n-3}\), with the displayed first three values.

**Sharpness and asymptotics.** The recurrence gives \(2^n>R_n\) at \(n=4,5,6\). If it holds at the two earlier indices \(n-2,n-3\), then \(R_n<2^{n-1}+2^{n-2}<2^n\), proving it inductively for all \(n\ge4\). Thus a two-sweep example always exists. The matrix \(T\) is primitive (its directed context graph has loops of mutually coprime lengths); its unique Perron root \(\rho\) satisfies \(\rho^3=2\rho+2\) and lies strictly between one and two. The positive coefficient of the dominant root in the trace formula follows from positive Perron left/right eigenvectors and nonnegative nonzero \(D\). Thus \(R_n=\Theta(\rho^n)\) and the stated probability follows. The recurrence also directly shows all other eigenvalues have smaller modulus.

## Verification

Run `python3 verify_transfer.py` to reconstruct both matrices directly from the NOR truth table, check the cubic matrix identity, and reproduce the count through \(n=35\). Independently run `python3 verify_direct.py` to enumerate every initial state for each \(3\le n\le16\), implement in-place vertex updates, verify the two-sweep guarantee and compare the complete entry-time census. Both programs are embedded verbatim and were executed successfully. These bounded computations corroborate but do not replace the all-\(n\) transfer proof.

## Relationship to prior work

Veliz-Cuba and Laubenbacher (publicly released October 15, 2011) relate AND-NOT fixed points to maximal independent sets; this already covers the \(P_n\) counting *interpretation*, not the new preimage distribution. Gadouleau and Kutner (arXiv v1 March 26, 2024) prove for every finite graph that two sequential sweeps suffice and study recognizing schedules that work in one; their open article's introduction summarizes worst-case fixing schedules and complexity, not an exact labelled one-sweep success population for this fixed cycle order. The previously published sequential bi-threshold cycle theorem (published-finding corpus, 2026-11-02) uses a different activation/persistence local rule, supports long necklace orbits, and cannot imply the present all-fixed dynamics. A separately published synchronous Rule-5 odd-ring preimage theorem (published-finding corpus, 2026-11-02) reads all old neighbor bits simultaneously, unlike the sequential boundary conditions producing \(D\); its Fibonacci fibers do not imply the weighted seam trace for this map. These are comparisons of mathematical claims rather than of titles alone.

## Limitations

The theorem applies to a single fixed cyclic sweep, not arbitrary orderings, and to open-neighborhood NOR rather than synchronous Rule 5, a closed-neighborhood NOR or a threshold-biased rule. The upper bound of two sweeps, the maximal-independent-set characterization and classical cycle fixed-point census are explicitly prior work, not new assertions. The 2011 AND-NOT source's publisher abstract was accessible but not its full article text; unindexed equivalent sequential one-sweep enumerations remain a residual originality risk. No independent external verification or global uniqueness certification has been performed.

## References

1. A. Veliz-Cuba and R. Laubenbacher, *On the computation of fixed points in Boolean networks*, Journal of Applied Mathematics and Computing 39 (2012), 145–153, first public 2011-10-15. https://doi.org/10.1007/s12190-011-0517-9
2. M. Gadouleau and D. C. Kutner, *Generalising the maximum independent set algorithm via Boolean networks*, arXiv:2403.17658, first public 2024-03-26; full open version https://arxiv.org/html/2403.17658v2
3. *Binary-necklace attractors and triangular-run basins for sequential bi-threshold cycles*, published-finding corpus (2026-11-02), https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-binary-necklace-attractors-and-triangular-run-basins-for-sequent--e79a108b9794
4. *Fibonacci fibers and the uniquely dominant Lucas basin for odd-ring Rule 5*, published-finding corpus (2026-11-02), https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-fibonacci-fibers-and-the-uniquely-dominant-lucas-basin-for-odd-r--9b825fd6faf8
