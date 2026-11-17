# Exact period basins and a nonmonotone oscillation window for threshold-two cyclic competition on complete bipartite graphs

## Finding

For every pair of integers \(m,n\ge1\), consider the synchronous **three-colour cyclic cellular automaton** on the labelled complete bipartite graph \(K_{m,n}\), with successor contact threshold two. A vertex in colour \(c\in\{0,1,2\}\) advances to \(c+1\pmod 3\) precisely when at least two vertices in the opposite part are currently in colour \(c+1\pmod3\); otherwise it retains colour \(c\). Let \(T\) be the first time the **entire labelled configuration** lies on a periodic orbit, and let \(p\) be its eventual least period.

**Theorem.** Every trajectory satisfies \(T\le3\) and \(p\in\{1,3,4\}\); in particular the global map satisfies \(F^{15}=F^3\). The bound \(T=3\) is attained on \(K_{2,4}\). The complete all-size attraction-basin counts are as follows. Define, for positive integers \(r\),

\[
\begin{aligned}
A_r&=\sum_{j=2}^{r-2}\binom rj, & B_r&=rA_{r-1},\\
D_r&=\begin{cases}r(r-1),&r\ge4,\\0,&r<4,\end{cases}
& U_r&=\sum_{a+b+c=r\atop a,b,c\ge2}\frac{r!}{a!b!c!},\\
L_r&=\begin{cases}3,&r=1,\\6,&r=2\text{ or }3,\\0,&r\ge4,\end{cases}&S_r&=A_r+B_r.
\end{aligned}
\]

Empty sums are zero and \(A_0=0\). For \(p\in\{1,3,4\}\), write \(N_p(m,n)=\#\{x\in\{0,1,2\}^{m+n}:p(x)=p\}\). Then

\[
\boxed{N_3(m,n)=U_mU_n+U_mL_n+L_mU_n,}
\]
\[
\boxed{N_4(m,n)=6S_mS_n+3\big(S_m(D_n+U_n)+S_n(D_m+U_m)\big),}
\]
\[
\boxed{N_1(m,n)=3^{m+n}-N_3(m,n)-N_4(m,n).}
\]

Hence **primitive four-cycles occur exactly when \(m,n\ge4\)**. Primitive three-cycles occur precisely when either both part sizes are at least six, or one is at least six and the other is one, two, or three. For fixed \(n\ge6\), three-cycles can therefore occur at \(m\in\{1,2,3\}\) and \(m\ge6\), but **not** at \(m=4,5\). This reentrant oscillation window reflects unilateral advancement of a small community followed by mutual advancement once both communities support all three successor classes.

On balanced graphs, with the initial configuration chosen uniformly,

\[
\boxed{\Pr(p=4\text{ on }K_{n,n})\sim3(n+2)\left(\frac23\right)^n,}
\]

while \(\Pr(p=1)=O\big(n^2(4/9)^n\big)\) and \(\Pr(p=3)\to1\). Thus among the exponentially rare initial configurations *not* attracted to three-cycles, the four-cycle basin dominates the fixed-point basin asymptotically.

## Assumptions and scope

All graph vertices are labelled and both parts are nonempty. Colours are integers modulo three, edges only cross between parts, contacts are counted as **distinct neighbouring vertices**, and updates of all vertices are simultaneous. Threshold two means **at least two** successors, not a fraction of the degree. The census \(N_p\) is over **initial labelled configurations eventually attracted to least period \(p\)**, not just initially periodic states. The small-size cases are included in the formulas.

## Proof

**Step 1: a finite quotient without loss of labelled-state information.** In each part and for each colour \(c\), let \(a_c\), respectively \(b_c\), denote the exact number of vertices of that colour and put \(s_c=\min(2,a_c)\), \(s_{3+c}=\min(2,b_c)\). The six-tuple \(s\) belongs to \(\{0,1,2\}^6\), a space of 729 possibilities. In part \(i\in\{0,1\}\), a colour-\(c\) vertex changes to

\[
q_{i,c}(s)=c+\mathbf 1\{s_{3(1-i)+(c+1)\bmod3}=2\}\pmod3.
\]

The next truncated counts are exactly

\[
s'_{3i+d}=\min\left(2,\sum_{c:q_{i,c}(s)=d}s_{3i+c}\right).
\]

This formula is exact because truncation at two commutes with nonnegative integer addition. All vertices initially in the same part and colour stay in the same colour at each later time. We therefore carry six **origin tags**, one for each initial class: \(\tau_{i,c}(0)=c\) and \(\tau_{i,c}(t+1)=q_{i,\tau_{i,c}(t)}(s(t))\). Tags of initially empty classes may be ignored. The resulting finite quotient together with its tags determines every labelled trajectory regardless of the actual initial class sizes.

**Step 2: exhaustive finite lemma.** `verify_symbolic.py` is an entirely explicit, dependency-free certificate: for each of the \(3^6=729\) truncated signatures it performs 15 exact iterations of the two displayed recurrences, retaining all six origin tags, and checks the tagged signatures at times three and fifteen. Every case passes. Moreover, at time three the least tagged period is one for 666 signatures, three for 15, and four for 48; no two-period case exists. The 48 period-four signatures are enumerated by the following type table (each type is the sorted triple of truncated counts in one part; listed multiplicities refer to ordered pairs):

| First-part type | Second-part type | Multiplicity |
|---|---|---:|
| 022 | 022 | 6 |
| 022 | 122 | 6 |
| 122 | 022 | 6 |
| 122 | 122 | 6 |
| 022 | 112 | 3 |
| 112 | 022 | 3 |
| 122 | 112 | 3 |
| 112 | 122 | 3 |
| 022 | 222 | 3 |
| 222 | 022 | 3 |
| 122 | 222 | 3 |
| 222 | 122 | 3 |

The fifteen period-three signatures are \((222,222)\), the seven \((222,\epsilon)\), and the seven \((\epsilon,222)\), where \(\epsilon\in\{0,1\}^3\setminus\{(0,0,0)\}\). Because tags retain the identities of initially coloured groups, this is a classification of *labelled configurations*, not merely part-count trajectories. The exhaustive check proves the infinite-family bound: every actual initial state maps into one of the 729 signatures, and each future labelled state is recovered by its tags.

**Step 3: translate signatures into exact labelled counts.** For a **fixed** position of the zero in a `022` signature there are \(A_r\) possible assignments to a part of size \(r\); for a fixed position of the one in `122`, there are \(B_r\); for a fixed position of the two in `112`, there are \(D_r\); for the unique `222` signature there are \(U_r\). The seven low signatures collectively have \(L_r\) assignments. Multiplying the weights of the two parts and using the table gives \(N_3\) and \(N_4\), and complementation among the \(3^{m+n}\) assignments gives \(N_1\). The formulas therefore count entire attraction basins without an independence assumption about class sizes.

**Step 4: sharpness and exceptional periods.** On \(K_{2,4}\), the initial labelled words \((0,1)\) and \((0,0,2,2)\) first enter a fixed configuration at time three. On \(K_{4,4}\), the initial words \((1,1,2,2)\) and \((0,0,2,2)\) cycle through four distinct labelled configurations (see the standalone direct verifier). Each part must contain at least two colour classes of multiplicity at least two for period four, hence the sharp \(m,n\ge4\) threshold. The period-three classification gives the asserted reentrant size criterion.

**Step 5: asymptotic rare-event law.** For \(r\ge6\), set \(Q_r=(r+2)2^{r-1}\), \(R_r=r^2+r+1\). Direct inclusion-exclusion gives \(U_r=3^r-3Q_r+3R_r\) and \(S_r=Q_r-2R_r\). Thus \(N_4(r,r)=6S_r(S_r+D_r+U_r)\sim3(r+2)6^r\). Substituting the same identities into \(N_1=9^r-U_r^2-N_4\) yields \(N_1(r,r)=O(r^2 4^r)\) (indeed \(N_1(r,r)\sim\tfrac34 r^2 4^r\)). Division by \(9^r\) proves the probability statements.

## Verification

The public source files `verify_symbolic.py`, `verify_direct.py`, and `verify_census.py` run using Python's standard library. The first exhaustively validates the 729-signature tagged quotient and the period-type table. The second independently evolves individual vertices and enumerates every one of 164,754 initial configurations across six small graph sizes, including explicit sharpness witnesses; the exact per-graph totals are in `verify_direct_output.txt`. The third checks combinatorial identities for sizes one through 100 and numerical convergence of the exact period-four ratio; its exact integer operations are authoritative, not floating-point tests of the theorem. All three scripts were executed and their outputs are included. In particular the full configuration period must not be confused with the population-count period: on the exhibited four-cycle, counts can repeat after two steps while individual vertices have period four.

## Relationship to prior work

Durrett and Griffeath's 1993 analysis introduced the CCA and GHM threshold-range framework and studied lattice waves and spiral cores, rather than exact complete-bipartite attraction basins. Bello and Sivakoff (2021) investigated the same general threshold-two CCA mechanism on infinite regular trees, with almost-sure fixation/fluctuation, not finite labelled orbit populations. Muñoz and Nuño (2026) emphasized that population periods need not equal full state periods on lattice tori, but did not obtain the present complete-bipartite phase/census formulas. The present result is also distinct from Greenberg–Hastings excitation at threshold two: in that rule excited and refractory vertices advance automatically, whereas here **every colour** requires successor contact. Likewise, contact threshold one does not determine the threshold-two phase windows or rare-event coefficients. The finite quotient and tag-lifting argument are specific to the present update semantics.

## Limitations

This concerns only three colours, contact threshold two, complete bipartite graphs, and synchronous updates. It establishes exact eventual period-basin populations but does not enumerate the *joint* distribution of entrance time and period for each size. The proof uses a transparent finite certificate for a universal reduced system; an independent mathematical audit and comprehensive historical-priority determination have not been performed. The asymptotic statements concern equal part sizes and do not assert a uniform estimate for every unbalanced scaling regime.

## References

1. R. Durrett and D. Griffeath, *Asymptotic Behavior of Excitable Cellular Automata*, Experimental Mathematics 2 (1993), 183–208; public preprint 1993-03-22, arXiv:patt-sol/9303002. https://arxiv.org/abs/patt-sol/9303002 ; full article https://sites.math.duke.edu/~rtd/reprints/paper79.pdf .
2. R. Fisch, J. Gravner and D. Griffeath, *Threshold-Range Scaling of Excitable Cellular Automata*, public preprint 1993-04-02, arXiv:patt-sol/9304001. https://arxiv.org/abs/patt-sol/9304001 .
3. J. Bello and D. Sivakoff, *Cyclic Cellular Automata and Greenberg-Hastings Models on Regular Trees*, arXiv:2108.06404 (2021). https://arxiv.org/abs/2108.06404 .
4. F. J. Muñoz and J. C. Nuño, *Symmetry-resolved periods in a cyclic-dominance automaton: separating intrinsic from lattice-induced periodicity*, arXiv:2610.37990 (2026). https://arxiv.org/abs/2610.37990 .
