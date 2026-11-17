# Nine exact entrance classes and a tunable four-layer law for three-state excitation on complete split graphs

## Finding
Let \(G_{a,b}=K_a\vee\overline K_b\) be the join of a clique of \(a\ge3\) labelled vertices and an independent set of \(b\ge2\) labelled vertices. In synchronous three-state Greenberg–Hastings dynamics, excited (state 1) vertices become refractory (state 2), refractory vertices become resting (state 0), and a resting vertex becomes excited exactly when it has an excited neighbor. Let \(T\) be first entry time into a periodic orbit and \(P\) its eventual least period. Then \(T\le4\), \(P\in\{1,3\}\), and all nine pairs in the table below occur. The sharp identity is \(F^7=F^4\).

Define \(U=2^a\), \(V=3^a\), \(W=2^b\), and \(Z=3^b\). The number \(N_{t,p}(a,b)\) of labelled initial states with \((T,P)=(t,p)\) is given exactly by

| \(t\) | \(N_{t,1}\) | \(N_{t,3}\) |
|---|---|---|
| 0 | \(1\) | \(VZ-3UZ+3UW-6W+3Z-3U+6\) |
| 1 | \(UW-1\) | \((U-2)(Z-2W+1)\) |
| 2 | \(UW-2W+Z\) | \((U-2)(Z-2W+1)\) |
| 3 | \(UW-3W+Z+1\) | \((U-2)(Z-2W+1)\) |
| 4 | \(Z-W-1\) | \(0\) |

The three nonzero transient entrance populations for primitive three-cycles are **exactly equal**, and the fourth-update extinction population \(Z-W-1\) is independent of clique size. The fixed point is the all-rest state. The count of primitive three-cycle orbits is \(N_{0,3}(a,b)/3\).

For fixed clique size \(a\ge3\) and \(b\to\infty\), conditional on eventual period three, the first-entry distribution converges to
\[
\Pr(T=0\mid P=3)\to\frac{3^a-3\cdot 2^a+3}{3^a-3},\qquad
\Pr(T=j\mid P=3)\to\frac{2^a-2}{3^a-3},\quad j=1,2,3.
\]
At \(a=3\), the four times \(0,1,2,3\) have **equal limiting probability one quarter**; as the fixed clique size increases, the time-zero weight approaches one. The total oscillation probability converges to \(1-3^{1-a}\).

## Assumptions and scope
The graph is finite, simple and loopless. The synchronous update uses neighbor state at the beginning of each step and no self-excitation. Vertices are distinguishable, and all initial assignments from \(\{0,1,2\}^{a+b}\) are counted. The statement covers all integers \(a\ge3\), \(b\ge2\); a two-vertex clique is already a complete tripartite graph, and its corresponding special case is not asserted as original. First entry time \(T(x)\) is the smallest \(t\ge0\) such that \(F^{t+p}(x)=F^t(x)\) for some positive integer \(p\); \(P(x)\) is the least such \(p\) at that entry.

## Proof
**Exact support-tag reduction.** A clique vertex in state zero is adjacent to every excited clique vertex (it is different from any vertex in state one) and every excited independent vertex. An independent vertex in state zero sees exactly the excited clique vertices. Accordingly, choose for each of the two modules its nonempty set of initially occupied states, \(C,I\subseteq\{0,1,2\}\). Retain one *tag* per initially occupied state in each module, recording the tag's current state after every update. All vertices sharing that tag have identical neighborhoods and hence remain identically colored forever. A clique tag of current state \(r\) updates to \((r+1)\bmod3\) for \(r\in\{1,2\}\); a zero clique tag updates to one precisely when either module has a state-one tag. An independent zero tag updates to one precisely when the clique has a state-one tag; nonzero independent tags advance cyclically. This is an exact deterministic transition on tagged tuples, even if differently tagged groups later merge.

There are exactly \((2^3-1)^2=49\) initial tagged support pairs. For each pair iterate its tag-transition until the *entire ordered tuple of tag states* repeats; record the first-entry time and least return period. The attached file `support_table.csv` supplies all 49 entries; `verify_split.py` independently regenerates it by a short finite algorithm. It identifies exactly the nine classes shown below, with each displayed \(3\times3\) matrix indexed by support cardinalities \(1,2,3\) for clique rows and independent-set columns:

\[
\begin{array}{c|c}
(t,p)&\text{support-pair count matrix}\\\hline
(0,1)&\left(\begin{smallmatrix}1&0&0\\0&0&0\\0&0&0\end{smallmatrix}\right)\\
(1,1)&\left(\begin{smallmatrix}3&2&0\\2&1&0\\0&0&0\end{smallmatrix}\right)\\
(2,1)&\left(\begin{smallmatrix}3&3&1\\2&1&0\\0&0&0\end{smallmatrix}\right)\\
(3,1)&\left(\begin{smallmatrix}2&2&1\\2&1&0\\0&0&0\end{smallmatrix}\right)\\
(4,1)&\left(\begin{smallmatrix}0&2&1\\0&0&0\\0&0&0\end{smallmatrix}\right)\\
(0,3)&\left(\begin{smallmatrix}0&0&0\\3&3&0\\3&3&1\end{smallmatrix}\right)\\
(1,3),(2,3),(3,3)&\left(\begin{smallmatrix}0&0&0\\0&1&1\\0&0&0\end{smallmatrix}\right)
\end{array}
\]
Each row of the 49-pair table is verifiable directly from the update rule, and every possible labelled initial state has exactly one support pair. No nonempty period-four or period-two classes occur, and the maximum entry time four occurs for all \(b\ge2\).

**Lifting to arbitrary module sizes.** For an initially occupied support with \(k\) distinct states in an \(n\)-vertex module, the number of labelled assignments realizing *that specified support* is the surjection count
\[
S_k(n)=\sum_{j=0}^k(-1)^j\binom{k}{j}(k-j)^n,
\quad S_1(n)=1,\quad S_2(n)=2^n-2,\quad S_3(n)=3^n-3\cdot2^n+3.
\]
Multiplying the \((k,\ell)\) matrix entries by \(S_k(a)S_\ell(b)\) and summing the nine entries gives all the formulas in the Finding table. For example, the fourth-entry fixed-point class has two support pairs of sizes \((1,2)\) and one of sizes \((1,3)\), so
\[N_{4,1}=2S_2(b)+S_3(b)=3^b-2^b-1.\]
The oscillatory layer matrices for \(t=1,2,3\) coincide, yielding the exact three-way equality. All nine expressions sum to \(3^{a+b}\), as required. Since the finite tagged classification has maximum entry four and least periods dividing three, \(F^7=F^4\) for every labelled size.

**Limiting law.** Sum the four period-three populations to obtain
\[
N_{\bullet,3}=(3^a-3)3^b-3(2^a-2)2^b.
\]
At fixed \(a\ge3\), divide the formula for each layer by this sum and let \(b\to\infty\); terms in \(2^b/3^b\) vanish. Substitution \(a=3\) gives \(6/24=1/4\) in all four layers. This also yields the period-three probability limit.

## Verification
`verify_split.py` deterministically rebuilds the complete 49-case tagged-support table, the nine support-size matrices and their symbolic weighted formulas. Independently, it directly evolves labelled configurations via an adjacency-list style neighbor rule for every parameter pair \(1\le a,b\le6\) with \(a+b\le10\). Exactly 306,729 labelled states were checked. These finite checks supplement the complete finite reduction and the surjection-counting proof; no finite-size extrapolation is used for the infinite-family assertion. Run `python3 verify_split.py` from the extracted file directory. The captured successful output is `verify_split.out`.

## Relationship to prior work
Gravner, Lyu and Sivakoff's *Limiting behavior of 3-color excitable media on arbitrary graphs* (arXiv:1610.07320v1, posted October 24, 2016) defines this exact three-color rule and proves a general circulation/irrotationality criterion for eventual fixation versus continued activity. Its general diameter-based synchronization bounds and the qualitative fixed/oscillatory dichotomy are **not** claimed here as new. The contribution assessed here is the labelled **first-periodic-entry-time distribution**, with nine simultaneous exact populations, the identity among three oscillatory entrance layers and the tunable four-layer conditional limit on the infinite complete-split family. A restricted two-vertex clique is a complete tripartite special case and is not an originality claim. The full cited preprint was inspected in relevant theorem and method sections; the directly inspected material contains no complete-split temporal population theorem.

## Limitations
This is a complete analysis of a sharply specified graph family and one deterministic three-state rule; it is not a claim about arbitrary split graphs, higher-color variants, random edge deletions or other cellular automata. The general 2016 theorem already entails qualitative synchronization criteria, so neither the existence of period-three cycles nor the general finite-time synchronization principle is new. The 49-case table is finite, explicit and exhaustively checkable; its construction and lifting need to be retained for reproducibility. A mathematical equivalent not present in accessible, indexed papers remains possible. Self-review is not independent validation.

## References
Gravner, J., Lyu, H., Sivakoff, D., *Limiting behavior of 3-color excitable media on arbitrary graphs*, arXiv:1610.07320v1 (public October 24, 2016), https://arxiv.org/abs/1610.07320; later *Annals of Applied Probability* 28 (2018), DOI:10.1214/17-AAP1350. Earlier work defining the Greenberg–Hastings model is cited therein. The open preprint is the chronological source, not its later journal date.
