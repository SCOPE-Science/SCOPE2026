# Exact all-palette excitation-wave response to a single chord in a cycle

## Finding
Fix integers \(k\ge3\), \(n\ge4\), and \(2\le a\le n-2\), and set \(b=n-a\). Add the edge \(\{0,a\}\) to the labelled cycle on vertices \(0,1,\ldots,n-1\). Apply synchronous, threshold-one, \(k\)-state Greenberg–Hastings excitation. Let \(Q_k(n,a)\) denote the number of *primitive temporal \(k\)-orbits* (not merely states with eventual period \(k\)). Define

\[
h_k(L)=L+\mathbf1_{k\mid L+1}
-\#\{j:0\le j<L,\ 2j\equiv L-3\pmod k\},\qquad L\ge2,
\]

and the three resonance indicators
\[
I_0=\mathbf1_{k\mid n},\qquad I_1=\mathbf1_{k\mid a+1},\qquad I_2=\mathbf1_{k\mid b+1}.
\]
Then the exact all-length, all-palette census is
\[
\boxed{Q_k(n,a)=2\big[I_0+I_1h_k(b)+I_2h_k(a)-I_0I_1-I_0I_2-I_1I_2\big].}
\]
In particular, a primitive \(k\)-cycle exists **if and only if** at least one of the three simple-cycle lengths \(n,a+1,b+1\) is divisible by \(k\). The unchorded cycle has only two primitive \(k\)-orbits when \(k\mid n\), and none otherwise. Thus one chord can create waves on a ring that previously admitted none.

For \(k=4\), the path coefficient simplifies to
\[
h_4(L)=\begin{cases}L,&L\text{ even},\\(L+1)/2,&L\text{ odd}.
\end{cases}
\]
For the natural fixed-distance-three chord \(a=3\) and every \(n\ge5\), all circumferences carry primitive four-waves, and their exact orbit count is
\[
\boxed{Q_4(n,3)=\begin{cases}
n-2,&n\equiv0\pmod4,\\
n,&n\equiv2\pmod4,\\
2(n-3),&n\equiv1,3\pmod4.
\end{cases}}
\]
This is a four-residue *linear wave-amplification law* induced by a single edge.

## Assumptions and scope
The graph is the simple undirected cycle with one chord between nonconsecutive vertices \(0\) and \(a\). The labels are retained; the chord is not treated as oriented. Each state belongs to \(\{0,1,\ldots,k-1\}\). At each time step, a positive state advances by one modulo \(k\), while a state zero becomes one if and only if at least one adjacent vertex currently has state one, and otherwise remains zero. A state is initially primitive \(k\)-periodic if \(F^k(x)=x\) and no smaller positive iterate fixes it. The theorem counts distinct temporal orbits of these states, not their attraction basins, all eventual periods, or transient states. The number \(h_k(L)\) is a nonnegative integer by the path-count interpretation below.

## Proof
**1. All vertices rotate in an immediate \(k\)-cycle.** In a state fixed by \(F^k\), any vertex that ever reaches state one must subsequently traverse all states \(1,2,\ldots,k-1,0\) and return to one at the \(k\)th step. Thus it advances at every time. A vertex that never reaches one is permanently zero. A permanently zero vertex cannot be adjacent to a rotating vertex, since its neighbor would display state one once each \(k\) steps and force activation. Connectedness therefore implies that every nonzero \(k\)-periodic configuration rotates at every vertex. Conversely, an initial coloring \(x\) rotates globally, \(F(x)=x+1\pmod k\), precisely when each vertex has a neighbor colored \(x(v)+1\pmod k\). This rotating orbit has least period \(k\). The all-zero state is the only other state fixed by \(F^k\).

**2. Directed successor cycles.** Draw an arrow \(v\to w\) whenever adjacent vertices have colors differing by \(+1\) from \(v\) to \(w\). Every vertex of a rotating state has positive outdegree. Following arrows in the finite graph produces a directed simple cycle. Every directed cycle has length divisible by \(k\) because each step adds one modulo \(k\). This chorded cycle has exactly three undirected simple cycles, of lengths \(n,a+1,b+1\). Consequently one of \(I_0,I_1,I_2\) must equal one. On a selected directed simple cycle the coloring is uniquely fixed by choosing a starting phase (\(k\) choices) and one of its two directions.

**3. Counting the complementary path.** Let a path of length \(L\ge2\) connect two vertices whose colors differ by \(\delta\in\mathbb Z/k\mathbb Z\). Require a successor-colored neighbor only at each internal path vertex; the two endpoints are already sustained by the selected directed cycle. Write the successive edge-color increments \(e_0,\ldots,e_{L-1}\). The internal condition is
\[
(e_{j-1}=k-1)\quad\text{or}\quad(e_j=1),\qquad 1\le j<L.
\]
Every admissible increment word consists either entirely of \(k-1\), or of \(j\) occurrences of \(k-1\), then a single \(c\in\{0,1,\ldots,k-2\}\), then \(L-j-1\) occurrences of one, for a unique \(j\in\{0,\ldots,L-1\}\). In the first case the endpoint difference is \(-L\pmod k\). In the other case it is \(L-1-2j+c\pmod k\). For each \(j\) and endpoint difference \(\delta\), precisely one residue \(c\pmod k\) is possible; it is forbidden exactly if \(2j\equiv L-\delta-2\pmod k\). Hence the number of admissible internal path colorings is
\[
H_{k,L}(\delta)=L+\mathbf1_{\delta\equiv-L\ (\mathrm{mod}\ k)}-\#\{0\le j<L:2j\equiv L-\delta-2\pmod k\}.
\]
Reversing the path gives a bijection between endpoint differences \(\delta\) and \(-\delta\); therefore \(H_{k,L}(1)=H_{k,L}(-1)=h_k(L)\). There is always at least one assignment: give the internal vertices on the complementary path colors \(x_j=x_0-j\pmod k\) for \(1\le j<L\), and fix the last endpoint independently to either specified color. Every internal vertex then has its left neighbor in the successor color. Thus \(h_k(L)\ge1\) for every \(L\ge2\).

**4. Union of the three directed-cycle families.** If \(k\mid n\), the long ring cycle supports exactly \(2k\) rotating colorings, with no uncolored vertices. If \(k\mid a+1\), the \(a\)-edge arc together with the chord supports \(2k\) choices of directed phase along that cycle; its remaining \(b\)-edge arc contributes independently \(h_k(b)\) assignments. This gives \(2k h_k(b)\), with the symmetric \(2k h_k(a)\) when \(k\mid b+1\).

The intersection of the long-ring family with either chord-cycle family, whenever both are resonant, is exactly \(2k\): all long-ring phase waves then satisfy the chord orientation because the selected arc length is \(-1\pmod k\). If both chord cycles are resonant, their intersection is also exactly \(2k\): their common chord must have one chosen direction, and this direction forces both arc colorings and the starting phase. A triple intersection cannot occur for \(k\ge3\), since \(a\equiv b\equiv-1\pmod k\) would make \(n\equiv-2\not\equiv0\pmod k\). Inclusion-exclusion consequently gives \(kQ_k\) rotating states, proving the boxed census. Whenever at least one cycle is resonant, its complementary path has a valid assignment, so the positive-count criterion is also sharp.

**5. Four-color parity and short-chord corollary.** For \(k=4\), the congruence \(2j\equiv L-3\pmod4\) has no solutions when \(L\) is even; its all-minus-one indicator also vanishes, yielding \(h_4(L)=L\). For odd \(L\), exactly half the available parity class of \(j\), with the all-minus-one correction, gives \(h_4(L)=(L+1)/2\). Substituting \(a=3\), \(b=n-3\) and separating four residues of \(n\) proves the displayed \(Q_4(n,3)\) formula. Each resulting orbit has exactly four labelled states, since global color rotation has no shorter period.

## Verification
Two standalone, standard-library Python programs are supplied. Run `python3 verify_bruteforce.py` to enumerate the actual Greenberg–Hastings map, iterate it for \(k\) steps, and compare the immediate primitive-period population against the theorem on 30 chorded graphs over \(1{,}301{,}418\) initial states. Run `python3 verify_transfer.py` for a separately organized endpoint-flag path-transfer computation on \(10{,}266\) parameter cases with \(3\le k\le8\) and ring sizes through \(61\). The second program never uses the closed path-sum coefficient for the transfer itself, although it compares against the stated formula. The expected program outputs are included as `verify_bruteforce.out` and `verify_transfer.out`.

These finite computations corroborate the arithmetic but do not replace the all-parameter combinatorial proof. The principal theorem does not claim any attraction-basin or transient classification.

## Relationship to prior work
Fisch and Gravner (1995) define stable periodic objects for multi-state Greenberg–Hastings media and analyze the one-dimensional infinite lattice, not the exact number of initially primitive \(k\)-periodic orbits on finite single-chord cycles. Durrett and Griffeath (1993) study spatially distributed excitable automata and spiral formation. Gravner, Lyu and Sivakoff (2016 preprint, published 2018) prove circulation-based theorems about three-color excitation on arbitrary graphs, not the present exact multi-palette finite orbit count.

The most closely related available finite-graph result, *Exact two-terminal source census for three-color excitable theta networks* (public result, November 8, 2026), counts primitive **three-state** waves and marks the number of paths that sustain either terminal; it assumes that every theta arm has length at least two. Its classification of path-increment words is acknowledged as an important methodological precursor. It does not contain this all-palette chorded-cycle result with a length-one arm, the modular \(h_k\) and the four-color single-chord amplification law. The published *Complete temporal orbit census for the four-color cyclic cellular automaton on rings* concerns a different rule (CCA rather than GHM) and graphs without chords; its finite-ring period spectrum does not imply the present defect response. A separate full-subdivision theorem addresses three-state excitation and cannot be specialized to this chorded graph because the chord is not subdivided.

The elementary rotating-color condition, the existence of successor directed cycles, and generic path-transfer methodology are prior mathematical ideas and are not independently claimed as inventions. The mathematical contribution claimed here is the explicit all-\(k\) defect formula and its arithmetic wave-amplification consequences.

## Limitations
The result concerns only *initially* primitive period-\(k\) states, not all eventual periodic states. It does not assert that no other least periods occur, or describe the transient basin of any orbit. The two path lengths are at least two so that the graph has a genuine, simple chord. Historical priority for an equivalent indexed or unindexed special-purpose formula cannot be ruled out; the inspected closest three-color theta result provides a similar counting mechanism, so methodological originality is limited. The oldest 1993 source was available as a date-verified abstract rather than a complete inspected text. An independent mathematical audit has not been performed.

## References
- R. Durrett and D. Griffeath, *Asymptotic Behavior of Excitable Cellular Automata*, first public arXiv submission 1993-03-22, https://arxiv.org/abs/patt-sol/9303002.
- R. Fisch and J. Gravner, *One-dimensional Deterministic Greenberg-Hastings Models*, Complex Systems 9 (1995), 329–348, https://content.wolfram.com/uploads/sites/13/2018/02/09-5-1.pdf.
- J. Gravner, H. Lyu and D. Sivakoff, *Limiting behavior of 3-color excitable media on arbitrary graphs*, first arXiv posting 2016-10-24, https://arxiv.org/abs/1610.07320.
- *Exact two-terminal source census for three-color excitable theta networks*, publicly available 2026-11-08, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-exact-two-terminal-source-census-for-three-color-excitable-theta--f7be757a3807.
- *Complete temporal orbit census for the four-color cyclic cellular automaton on rings*, publicly available 2026-11-17, https://github.com/published-finding corpus/2026/tree/main/2026/11/17/SCOPE-complete-temporal-orbit-census-for-the-four-color-cyclic-cellula--947b2a9e90ed.
