# Twelve-term exact three-cycle census for refractory excitation on three-row rook graphs

## Finding
For every integer \(n\ge2\), let \(G_n=K_3\square K_n\) be the simple labelled rook graph with three rows and \(n\) columns. Each vertex has a state in \(\{0,1,2\}\), updated simultaneously by the threshold-one, three-state Greenberg–Hastings rule: \(1\to2\), \(2\to0\), and \(0\to1\) if and only if at least one neighbor is in state \(1\); a resting vertex with no excited neighbor remains at \(0\). Let \(W_n\) count the configurations of **immediate least temporal period three**, with no transient: \(F^3(x)=x\) and \(F(x)\ne x\).

The exact all-size census is
\[
\boxed{\begin{aligned}
W_n={}&27^n-9\cdot18^n+9\cdot14^n+27\cdot12^n
-36\cdot10^n-27\cdot8^n\\
&+36\cdot7^n+27\cdot6^n-48\cdot5^n+27\cdot4^n
-9\cdot2^n+3.
\end{aligned}}
\]
Each counted orbit has precisely three distinct labelled phases. Therefore the number of **temporal orbits** of least period three is exactly \(W_n/3\). In particular, at lengths \(n=2,3,4,5\), the labelled phase counts are \(72,2562,119880,5109306\), respectively; the temporal orbit counts are \(24,854,39960,1703102\).

For a uniformly selected initial configuration, the probability of immediate primitive-three periodicity obeys
\[
\frac{W_n}{27^n}=1-9(2/3)^n+O((14/27)^n)\qquad(n\to\infty).
\]
Thus immediate three-periodicity becomes exponentially prevalent as the longer dimension increases. This statement concerns time-zero recurrence, not the full eventual-attractor distribution.

## Assumptions and scope
The vertex set consists of \(3n\) **labelled** positions \((i,j)\), \(1\le i\le3\), \(1\le j\le n\); distinct positions are adjacent exactly when they share a row or a column. There are no self-loops. The state alphabet and dynamics are exactly as above; all updates are synchronous. We count all three temporal phases as distinct states and do not quotient by spatial automorphisms. There is no assertion about other primitive periods, transient depths, or threshold-two excitation. The coefficient identity also holds for the degenerate boundary \(n=1\), where the graph is a single triangle and \(W_1=6\).

## Proof
**1. Local characterization of immediate three-cycles.** On any finite connected graph under this three-state rule, a nonfixed configuration \(x\) satisfies \(F^3(x)=x\) if and only if every vertex initially colored \(a\) has a neighbor initially colored \(a+1\pmod3\). For necessity, any vertex that ever has state \(1\) moves through \(1,2,0\) in the subsequent three time slots, and period-three recurrence forces its next state to be \(1\). Any vertex that never becomes \(1\) must remain at \(0\); it cannot be adjacent to a cycling vertex, since its neighbor would necessarily excite it at some step. Connectedness therefore forces either the all-zero fixed state or universal phase rotation. In the latter case, the required excitation at each vertex's resting time is exactly the initial successor-neighbor condition. Conversely that condition makes every vertex advance by one modulo three at the first step, and the condition is invariant under simultaneous color rotation. The three iterations then return to \(x\), and it cannot be fixed because every coordinate changes. This criterion is classical for three-state excitation and is not claimed as original here.

**2. Exact palettes and the finite transfer.** Write \(\mathcal C=\{0,1,2\}\). For each row \(i\in\{1,2,3\}\), let \(R_i\) be the exact nonempty set of colors appearing in that row. For a column \(c=(c_1,c_2,c_3)\in\mathcal C^3\), let \(\operatorname{succ}(a)=a+1\pmod3\). A position in row \(i\) has its successor in its open neighborhood if and only if either \(\operatorname{succ}(c_i)\in R_i\), or \(\operatorname{succ}(c_i)\) appears among the other entries of its column. (A vertex is never its own successor.) Thus, conditional on the three **exact row palettes** \(R=(R_1,R_2,R_3)\), the three-cycle requirement is a column-local condition.

For any choice of possibly smaller subsets \(S_i\subseteq R_i\), set
\[
 b(R,S)=\#\bigl\{c\in S_1\times S_2\times S_3:
 \forall i,\ \operatorname{succ}(c_i)\in R_i\cup\{c_1,c_2,c_3\}\bigr\}.
\]
The right-hand condition is a finite Boolean test on a triple of symbols; if some \(S_i\) is empty, set \(b(R,S)=0\). By elementary inclusion–exclusion over the colors required to occur at least once in each row, the number of sequences of \(n\) labelled columns with exact palettes \(R\), every column allowed, is
\[
 \sum_{S_i\subseteq R_i}(-1)^{\sum_i(|R_i|-|S_i|)}b(R,S)^n.
\]
There is no coupling between columns once \(R\) is fixed: all within-row neighbors are present, and within-column neighbors are confined to the same triple. Summing over the seven nonempty choices for each \(R_i\) counts each phase-rotating state exactly once. Consequently, for every **positive integer** \(n\),
\[
 W_n=\sum_{\varnothing\ne R_i\subseteq\mathcal C}
 \sum_{S_i\subseteq R_i}(-1)^{\sum_i(|R_i|-|S_i|)}b(R,S)^n.
 \tag{1}
\]
For positive \(n\), terms with empty \(S_i\) vanish. There are exactly \(19\) ordered pairs of nonempty \(S_i\subseteq R_i\subseteq\mathcal C\) per row, so the remaining sum has precisely \(19^3=6859\) finite, parameter-independent summands.

**3. Exhaustive symbolic coefficient certificate.** For each integer \(b\in\{0,\ldots,27\}\), aggregate the signs of the \(19^3\) terms of (1) with \(b(R,S)=b\), to obtain an integer coefficient \(c_b\). The nonzero coefficients are, exactly,
\[
\begin{array}{c|rrrrrrrrrrrr}
b&1&2&4&5&6&7&8&10&12&14&18&27\\\hline
c_b&3&-9&27&-48&27&36&-27&-36&27&9&-9&1.
\end{array}
\]
All other \(c_b\) vanish. To avoid an uncheckable appeal to computer output, the accompanying self-contained source `proof/verify_rook_gh.py` is an executable **finite coefficient certificate**: its `symbolic_coefficients` function loops over all \(19^3\) triples of palette pairs, over all \(27\) possible column triples where allowed by subpalettes, evaluates the displayed Boolean condition directly and aggregates integer coefficients. The program asserts the full coefficient table, not just a few numerical values. This checks a finite universal sum with no dependence on \(n\); formula (1) then proves the identity for every \(n\), rather than extrapolating from sampled graph sizes. Substitution of the displayed coefficient table into (1) proves the boxed formula.

**4. Orbit number and asymptotics.** The local characterization makes every nonfixed three-periodic state rotate all colors once per update. It therefore has exactly three distinct time phases, so division by three gives its orbit count. The largest exponential base in the explicit formula is \(27\), followed by \(18\), then \(14\). Divide by \(27^n\) to obtain the stated expansion, with the remaining terms bounded in absolute value by a fixed constant times \((14/27)^n\). This finishes the proof.

## Verification
The standalone Python 3 program `proof/verify_rook_gh.py` requires no third-party libraries and runs from the package root with `python3 proof/verify_rook_gh.py`. The certificate reconstructs the exact coefficient table by integer arithmetic and computes the formula for lengths one through ten. Separately, the `independent_exhaustion` implementation constructs literal graph neighborhoods and directly iterates the Greenberg–Hastings update three times on **all** \(3^{3n}\) possible states at lengths \(n=1,2,3,4\), without using the successor-neighbor criterion to determine which states return. The independently enumerated counts \(6,72,2562,119880\) coincide with the formula. Captured reproducibility output is in `proof/check.out`. The finite exact coefficient certificate, together with the palette inclusion–exclusion identity, establishes the all-size result; four finite state-space checks are additional corroboration only.

## Relationship to prior work
Greenberg and Hastings introduced discrete excitable media; Durrett and Griffeath (first public preprint 1993-03-22) studied asymptotic excitable cellular automata. Gravner, Lyu and Sivakoff (first posted 2016-10-24) prove broad structural statements on three-color excitation on arbitrary graphs, including a comparison-process characterization; their inspected full text does not give a special three-row rook-graph phase-count formula. A previously published exact **two-row** matched-clique formula for \(K_2\square K_n\) is \(9^n-6\cdot6^n+15\cdot4^n-12\cdot3^n+3\), based on a distinct two-palette classification. That theorem covers the simpler two-row case, not the three-row count or its twelve-base coefficient table. A published primitive-three census on **full subdivisions** concerns a different graph operation and does not imply the present formula. The local phase-rotation criterion in Step 1 is previously known; the contribution here is the exact evaluation of its number of solutions on \(K_3\square K_n\) and the ensuing sharp leading probability deficit. The graph is also the line graph of \(K_{3,n}\), an equivalent graph description considered during comparison.

## Limitations
The theorem counts only immediately primitive period-three configurations, not the full attractor structure or its transient basin. Earlier general structural results supply the local criterion, and a two-row enumeration is an acknowledged antecedent, not an independent discovery. Absence of a matching statement in the checked literature and indexed records does not prove historical priority; unindexed equivalences remain possible. The computational certificate exhaustively checks a fixed finite symbolic coefficient table; it does not enumerate all states for unbounded \(n\). No independent audit is asserted.

## References
1. R. Durrett and D. Griffeath, *Asymptotic Behavior of Excitable Cellular Automata*, first posted 1993-03-22, arXiv:patt-sol/9303002, https://arxiv.org/abs/patt-sol/9303002.
2. J. Gravner, H. Lyu and D. Sivakoff, *Limiting behavior of 3-color excitable media on arbitrary graphs*, first posted 2016-10-24, arXiv:1610.07320, https://arxiv.org/html/1610.07320v1.
3. *Dense immediate three-cycles on two matched cliques*, published research record, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-dense-immediate-three-cycles-on-two-matched-cliques--38271e8611c5 (related two-row problem).
4. *Exact three-periodic excitation census on full graph subdivisions*, published research record, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-exact-three-periodic-excitation-census-on-full-graph-subdivision--3e82f66ce40c (related phase-criterion evaluation on different graphs).
