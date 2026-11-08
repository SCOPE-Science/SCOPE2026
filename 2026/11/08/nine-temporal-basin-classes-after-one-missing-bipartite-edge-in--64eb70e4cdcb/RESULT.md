# Nine temporal basin classes after one missing bipartite edge in three-color cyclic dynamics

## Finding

Delete a single edge from the complete bipartite graph \(K_{m,n}\), where \(m,n\ge2\), and run synchronous three-color successor-contact dynamics. Every trajectory becomes periodic within three updates, only least periods one, three and four occur, and the exact identity
\[
F^{15}=F^3
\]
holds. The three-step bound is attained for every pair of dimensions. More sharply, the entire first-periodic-entry distribution has the following nine classes.

Set \(r=m-1\), \(s=n-1\), and introduce the nonnegative integers
\[
U=2^r-2,\qquad V=2^s-2,\qquad
R=3^r-3\cdot2^r+3,\qquad S=3^s-3\cdot2^s+3.
\]
Write \(N_{t,p}\) for the number of **labelled initial colorings** first reaching the periodic part of their trajectory at step \(t\) with eventual least period \(p\). The complete census is:

| First-entry time \(t\) | Least period \(p\) | \(N_{t,p}\) |
|:---:|:---:|---:|
| \(0\) | \(1\) | \(3\) |
| \(0\) | \(3\) | \(9RS+6RV+6SU+3UV\) |
| \(0\) | \(4\) | \(24UV+12U+12V\) |
| \(1\) | \(1\) | \(12UV+15U+15V+24\) |
| \(1\) | \(3\) | \(3RV+3SU\) |
| \(1\) | \(4\) | \(18RV+12R+18SU+12S+30UV+12U+12V\) |
| \(2\) | \(1\) | \(9R+9S+24U+24V+24\) |
| \(2\) | \(4\) | \(6R+6S+12UV+12U+12V\) |
| \(3\) | \(1\) | \(6U+6V+30\) |

All omitted classes have zero population. The nine counts sum to \(3^{m+n}\), the size of the complete labelled state space. In particular,
\[
N_{3,1}=6\bigl(2^{m-1}+2^{n-1}\bigr)+6.
\]
This makes precise how removing one edge introduces a thin but nonempty, maximally delayed synchronization layer for every \(m,n\ge2\).

## Assumptions and scope

The underlying graph is simple, undirected, finite and loopless. Partition the vertex set into an \(m\)-vertex shore and an \(n\)-vertex shore. Choose one distinguished vertex on each shore, named \(a_*\) and \(b_*\); delete precisely the edge \(a_*b_*\), retaining every other cross-shore edge. Vertex labels are retained when counting initial configurations; all three colors are distinct. The colors are \(\{0,1,2\}=\mathbb Z/3\mathbb Z\). Every vertex updates simultaneously according to
\[
F(x)_v=\begin{cases}
x_v+1\pmod 3,&\exists w\sim v:\ x_w=x_v+1\pmod3,\\
x_v,&\text{otherwise}.
\end{cases}
\]
For an initial coloring \(x\), define \(T(x)\) as the least \(t\ge0\) such that \(F^t(x)\) lies on a periodic orbit. Its eventual least period \(p(x)\) is the least positive period of that orbit. A period-two orbit cannot occur in this family.

## Proof

**1. Exact finite reduction.** Let \(A\) and \(B\) be the ordinary, nondistinguished vertices on the two shores. The map is equivariant under independent permutations of the vertices of \(A\) and \(B\). Moreover, two ordinary vertices on one shore which begin with the same color have identical neighbor sets and therefore remain identical at all future times. Thus a labelled initial coloring is faithfully represented for temporal purposes by its distinguished colors \(a,b\in\{0,1,2\}\), the two **nonempty** initially occupied color supports \(P,Q\subseteq\{0,1,2\}\), and one tracked representative of each initially occupied color on each ordinary shore. There are exactly
\[
3^2(2^3-1)^2=441
\]
such signatures. Retaining each tracked initial color class separately, even if two classes later merge, preserves the exact first-return and eventual-period times of the full labelled trajectory.

Write \(\sigma(c,H)\) for \(c+1\pmod3\) when \(c+1\in H\), and for \(c\) otherwise. If \(a,b\) are the distinguished colors, \((u_i)_{i\in P}\) and \((v_j)_{j\in Q}\) are the tracked color-class values, and \(\mathcal A=\{u_i:i\in P\}\), \(\mathcal B=\{v_j:j\in Q\}\), then one synchronous update is exactly
\[
\begin{aligned}
a'&=\sigma(a,\mathcal B),& b'&=\sigma(b,\mathcal A),\\
u_i'&=\sigma(u_i,\mathcal B\cup\{b\}),&
v_j'&=\sigma(v_j,\mathcal A\cup\{a\}).
\end{aligned}
\]
The missing edge is reflected only in the two distinguished updates. Every rule here involves finite three-color sets, so the infinite family of graph sizes has reduced to 441 explicitly specified finite trajectories.

**2. Exhaustive finite lemma.** For each of the 441 signatures, iterate the preceding four-tuple rule, storing the first time each entire tracked state occurs. When a state repeats, its first-occurrence index is exactly \(T\), and the difference between repeat time and that index is exactly \(p\). Running this finite loop yields the following complete coefficient table. A row is indexed by \((T,p)\); its entries give the number of signatures where the ordinary-shore supports have the indicated sizes.

| \((T,p)\) | Support-size pairs with multiplicities |
|---|---|
| \((0,1)\) | \((1,1):3\) |
| \((0,3)\) | \((3,3):9,(3,2):6,(2,3):6,(2,2):3\) |
| \((0,4)\) | \((2,2):24,(2,1):12,(1,2):12\) |
| \((1,1)\) | \((2,2):12,(2,1):15,(1,2):15,(1,1):24\) |
| \((1,3)\) | \((3,2):3,(2,3):3\) |
| \((1,4)\) | \((3,2):18,(3,1):12,(2,3):18,(1,3):12,(2,2):30,(2,1):12,(1,2):12\) |
| \((2,1)\) | \((3,1):9,(1,3):9,(2,1):24,(1,2):24,(1,1):24\) |
| \((2,4)\) | \((3,1):6,(1,3):6,(2,2):12,(2,1):12,(1,2):12\) |
| \((3,1)\) | \((2,1):6,(1,2):6,(1,1):30\) |

This finite lemma is completely reproducible with the standalone `support_checker.py` included with the result: the program implements precisely the displayed update equations, enumerates every support pair and distinguished-color choice, and checks the stated table; it does not estimate the answer by random sampling or by truncating graph sizes. Its loops stop only upon an exact state repetition, with an independently checked length bound. The coefficient counts sum to 441, and no unlisted pair \((T,p)\) occurs.

**3. Exact restoration of labelled multiplicities.** For \(r\ge1\) ordinary vertices and one prescribed nonempty color subset, the number of labelled assignments using every color of that subset is
\[
w_r(1)=1,\quad w_r(2)=2^r-2,\quad w_r(3)=3^r-3\cdot2^r+3.
\]
These are the exact two- and three-color surjection formulas by inclusion-exclusion. The number of initial colorings represented by any signature with support sizes \((i,j)\) is \(w_r(i)w_s(j)\), independent of which actual colors occur. Weighting each entry in the complete 441-signature table by this factor gives, term by term, the nine asserted formulas. Since each labelled coloring has a unique initial support and distinguished pair, this weighting neither omits nor double counts any configuration. Direct expansion gives the consistency identity
\[
\sum_{t,p}N_{t,p}=9\bigl(1+3U+R\bigr)\bigl(1+3V+S\bigr)=3^{m+n}.
\]

**4. Sharpness and iterate identity.** The finite table shows \(T\le3\) and \(p\in\{1,3,4\}\) universally. A periodic point of period three or four is fixed by the twelfth iterate, so for every initial coloring
\[
F^{15}(x)=F^{12}(F^3(x))=F^3(x).
\]
For any \(m,n\ge2\), set the distinguished colors to \(a_*=0\), \(b_*=1\) and every ordinary vertex to \(0\). The tracked configuration, in the order (distinguished \(a_*\), distinguished \(b_*\); ordinary \(A\), ordinary \(B\)), follows
\[
(0,1;0,0)\to(0,1;1,0)\to(0,1;1,1)\to(1,1;1,1),
\]
and its final configuration is fixed. Its first periodic-entry time is exactly three; hence the bound is sharp for every admissible graph.

## Verification

The included `support_checker.py` tests every one of the 441 abstract signatures against the displayed coefficient table, checks the sharp witness, verifies all nine weighted formulas and the conservation of total state count for \(2\le m,n\le11\). The separately implemented `direct_check.cpp` does not use the support reduction: it constructs the full labelled graph neighborhood rule, enumerates all \(3^{m+n}\) starting states for each \(2\le m,n\le6\), evolves each state until an exact repeat, and compares all nine formula values. It checked 1,185,921 labelled initial states on 25 graphs. Source and captured output are included as standalone files. These additional finite graph checks corroborate the infinite-family argument; its logically complete step is the 441-state reduction and exhaustive finite lemma, not extrapolation from the 25 graphs.

## Relationship to prior work

Gravner, Lyu and Sivakoff introduced a general covering-space approach to three-color cyclic cellular automata on arbitrary finite graphs. Their theorem characterizes synchronization by the initial circulation form and bounds the time to **synchronization** by graph diameter. Thus a diameter-three bound for configurations which eventually synchronize is already implicit in general prior work. What is established here is different: every periodic component (including nonsynchronizing orbits) has a sharply bounded first-entry time, the possible eventual least periods are determined, and the populations of all nine dynamical classes are exact for every pair of shore sizes. The intact complete bipartite family and the crown family obtained by deleting an entire perfect matching have previously been considered separately; neither case determines the effects of deleting exactly one edge at arbitrary two-shore sizes. The present formulas specialize correctly to the four-vertex path when \(m=n=2\), where all configurations synchronize.

## Limitations

The result concerns exactly three colors, threshold-one successor contact, synchronous updates and exactly one deleted cross-edge. It does not cover threshold-two excitation, asynchronous updates, more colors or deletion of arbitrary bipartite subgraphs. The originality comparison covers identified literature and available research records and cannot exclude an unindexed equivalent formulation; independent verification remains unperformed. The finite proof relies on the completely specified 441-state transition enumeration, for which executable source is furnished.

## References

Gravner, J.; Lyu, H.; Sivakoff, D., *Limiting behavior of 3-color excitable media on arbitrary graphs*, first public version 2016-10-24, arXiv:1610.07320, https://arxiv.org/abs/1610.07320. See the definition of the CCA rule and Theorem 3 on synchronization versus the initial circulation form.
