# Dense immediate three-cycles on two matched cliques

## Finding

Let \(G_n=K_2\square K_n\) for every integer \(n\ge1\): two labelled complete graphs on \(n\) vertices, joined by a perfect matching. Consider synchronous three-state Greenberg–Hastings excitation with resting state \(0\), excited state \(1\), and refractory state \(2\). Write \(P_3(n)\) for the number of initial configurations whose **least temporal period is exactly three**, with no transient.

Then, for every \(n\ge1\),
\[
\boxed{P_3(n)=9^n-6\cdot6^n+15\cdot4^n-12\cdot3^n+3.}
\]
There are no such configurations for \(n=1,2\), and at least one for every \(n\ge3\). Every corresponding orbit has three labelled states, so the number of distinct primitive-three orbits is \(P_3(n)/3\).

A structural classification accompanies the formula. Every primitive-three initial state has either (i) all three colors occurring in **both** cliques or (ii) all three colors in one clique and exactly two in the other, with each occurrence of the latter clique's unsupported color matched to the color missing from that clique. In particular, two cliques each using exactly two colors cannot jointly support an immediate three-cycle.

Under uniformly random initial states, the probability of immediate primitive-three periodicity equals
\[
\frac{P_3(n)}{9^n}=1-6(2/3)^n+15(4/9)^n-12(1/3)^n+3(1/9)^n
=1-6(2/3)^n+O((4/9)^n).
\]
Thus the probability tends to one exponentially as the clique size grows. This describes periodicity from the initial step, not eventual basin membership.

## Assumptions and scope

The vertex set is \(\{U_i,V_i:1\le i\le n\}\). Each pair \(U_i,U_j\) and \(V_i,V_j\) with unequal indices is an edge, as is each matching pair \(U_i,V_i\). There are no other edges or self-loops. The update map \(F\) on \(\{0,1,2\}^{2n}\) is
\[
F(c)_v=\begin{cases}
1,&c_v=0\text{ and some neighbor has color }1,\\
0,&c_v=0\text{ and no neighbor has color }1,\\
2,&c_v=1,\\
0,&c_v=2.
\end{cases}
\]
An initial state has primitive period three when \(F^3(c)=c\) and \(F(c)\ne c\). All counts are for fully labelled vertices and time phases, not modulo graph automorphisms. The unique fixed state is all resting.

## Proof

**Lemma 1 (local support criterion).** For any finite connected graph under this three-state rule, a nonfixed configuration has period dividing three if and only if every vertex of color \(a\in\mathbb Z/3\mathbb Z\) has a neighbor of color \(a+1\pmod3\). In this case its least period is three.

*Proof.* If \(F^3(c)=c\), inspect the time-word of one vertex repeated every three steps. Since a state \(1\) is invariably followed by \(2\) and then by \(0\), any vertex ever in state \(1\) traverses all three colors at each step. A vertex never in state \(1\) must stay \(0\): a state \(2\) would be followed by \(0\), and period-three recurrence of \(2\) would force a prior \(1\). Thus each vertex either stays resting or cycles \(0,1,2\). A permanently resting vertex cannot be adjacent to a cycling vertex: the latter becomes excited at some time, forcing excitation at the former in the next step. Connectedness makes all vertices permanently resting or all cyclic. In the second case, at the time each vertex is resting it must encounter an excited neighbor. Translating the three time steps back to the initial colors gives the stated successor-neighbor condition. Conversely, if the successor-neighbor condition holds initially, every vertex advances one color at the next step (with resting vertices excited by their successor neighbors). Uniform advancement preserves the successor-neighbor condition, so the entire configuration rotates at every step and returns after exactly three steps. \(\square\)

**Lemma 2 (clique support types).** In a primitive-three state of \(G_n\), each clique uses at least two distinct colors; the two cliques cannot both use exactly two colors.

*Proof.* If the upper clique is monochromatic in color \(a\), every upper vertex requires its matched lower vertex to have color \(a+1\), so the lower clique is monochromatic in \(a+1\). Then each lower vertex requires a matched upper vertex of color \(a+2\), impossible. Hence neither clique is monochromatic.

Suppose both use exactly two colors. Rotate all colors so that the upper clique omits \(0\), and write its colors as \(1,2\). If the lower clique also omits \(0\), the upper vertices of color \(2\) have no successor \(0\) anywhere adjacent. If the lower clique omits \(1\), it uses \(0,2\). Every upper \(2\) requires its matched lower color \(0\), but each lower \(0\) requires its matched upper color \(1\); consequently upper \(2\) cannot occur, contradicting the assumed upper two-color support. If the lower clique omits \(2\), it uses \(0,1\). Every lower \(1\) requires its matched upper color \(2\), but every upper \(2\) requires its matched lower color \(0\); consequently lower \(1\) cannot occur. Each case is impossible. \(\square\)

**Counting.** Write
\[
S_n=3^n-3\cdot2^n+3,
\]
which is the number of labelled \(n\)-tuples using all three colors, by inclusion–exclusion. The states with all three colors in both cliques number \(S_n^2\), and every one satisfies the local support criterion.

Now choose which clique uses exactly two colors (two choices) and which color \(m\) it omits (three choices). Its two present colors are \(m+1\) and \(m-1\) modulo three. Color \(m+1\) has successor \(m-1\) inside its clique, while color \(m-1\) has no successor there; therefore every position of color \(m-1\) requires matched color \(m\) in the full three-color clique. If there are \(k\ge1\) such positions, choosing them contributes \(\binom nk\); the other \(n-k\) positions of the full clique may use any colors but must contain both colors unequal to \(m\). Their number is \(3^{n-k}-2\cdot2^{n-k}+1\). This automatically enforces the full support and the presence of both colors in the two-color clique (the forbidden single-position cases have zero weight). Hence there are
\[
B_n=\sum_{k=1}^{n}\binom nk(3^{n-k}-2\cdot2^{n-k}+1)
=4^n-3\cdot3^n+3\cdot2^n-1
\]
configurations for each of the six choices. Lemma 2 rules out every other nonfixed primitive-three state. Therefore
\[
P_3(n)=S_n^2+6B_n
=9^n-6\cdot6^n+15\cdot4^n-12\cdot3^n+3.
\]
For \(n\le2\), a clique cannot contain three colors, and Lemma 2 gives zero. For \(n\ge3\), choose any fully three-colored tuple in each clique, yielding positive count. Dividing by three counts temporal orbits. Dividing by \(9^n\) and retaining the dominant correction gives the claimed asymptotic. \(\square\)

## Verification

Two standalone standard-library programs independently tested the formula.

- `verify_dynamics.py` exhaustively applies the actual synchronous update three times and separately checks the local successor criterion for every state at \(n=2,3,4,5,6\), covering **597,861** labelled states. The primitive-three counts are respectively \(0,72,1656,24840,304200\), all agreeing with the theorem.
- `verify_transfer.py` independently counts supported states using a four-mask column transfer (seen colors and required same-row witnesses in both cliques), with no use of the classification in Lemma 2. Its counts agree with the formula for every integer \(1\le n\le60\). The transfer keeps precise integer counts rather than stochastic estimates.

Execute `python3 verify_dynamics.py` and `python3 verify_transfer.py` in a directory containing the two files. Captured outputs are supplied as `verify_dynamics.out` and `verify_transfer.out`. These finite tests are not the proof of the all-\(n\) formula; the complete combinatorial classification above is.

## Relationship to prior work

Gravner, Lyu and Sivakoff (arXiv:1610.07320v1, October 24, 2016) develop graph-universal criteria for long-run synchronization and activity of three-state Greenberg–Hastings systems using edge forms and closed walks. Their Theorem 3 determines eventual activity from cycles, but does not state this labelled, first-step periodicity census on \(K_2\square K_n\). An exact count of *initial* primitive-three states does not follow by substituting a graph parameter into the published activity formula: the local support configurations must still be classified and counted. Bassi et al. (2022) study statistical prediction of synchronization on graph ensembles, rather than the exact immediate-period-three count on this family. Standard inclusion–exclusion is used openly as a tool and is not claimed to be new.

The graph family can also be viewed as the line graph of \(K_{2,n}\), so searches under both graph names are relevant. Neither a general synchronization characterization nor a census on a single different-sized rook graph directly implies the all-size count above.

## Limitations

Only initially primitive period-three configurations, their exact number, and the asymptotic density are classified. The theorem does not enumerate other primitive periods, transient entry times, attraction basins, or automorphism-quotient orbits. The literature comparison is not a proof that no equivalent counting formula exists in inaccessible or unindexed work. The general proof is self-contained, whereas computation verifies only the stated finite ranges.

## References

1. J. Gravner, H. Lyu, D. Sivakoff, *Limiting behavior of 3-color excitable media on arbitrary graphs*, arXiv:1610.07320v1 (public October 24, 2016), https://arxiv.org/abs/1610.07320 ; subsequently *Annals of Applied Probability* 28 (2018), DOI:10.1214/17-AAP1350.
2. H. Bassi, R. P. Yim, J. Vendrow, and collaborators, *Learning to predict synchronization of coupled oscillators on randomly generated graphs*, *Scientific Reports* 12, 15056 (2022), DOI:10.1038/s41598-022-18953-8 ; open-access record https://pmc.ncbi.nlm.nih.gov/articles/PMC9445105/.
