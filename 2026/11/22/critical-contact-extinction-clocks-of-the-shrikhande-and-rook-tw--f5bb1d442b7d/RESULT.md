# Critical-contact extinction clocks of the Shrikhande and rook twins

## Finding

Let \(R=K_4\square K_4\) be the rook graph and \(S\) the Shrikhande graph. Both have sixteen vertices, degree six, strongly regular parameters \((16,6,2,2)\), and adjacency spectrum \(6^1,2^6,(-2)^9\). For a synchronous three-state Greenberg–Hastings rule, a refractory vertex changes \(2\to0\), an excited vertex changes \(1\to2\), and a resting vertex changes \(0\to1\) precisely when **at least three** of its six neighbors are excited.

Write \(\tau_G(x)=\min\{t\ge0:F_G^t(x)=\mathbf0\}\) for the first time at which the system is entirely resting. The following is an **exhaustive, exact** table over all \(3^{16}=43{,}046{,}721\) labelled initial configurations on each graph:

| First extinction time \(t\) | Rook graph | Shrikhande graph |
|---:|---:|---:|
| 0 | 1 | 1 |
| 1 | 65,535 | 65,535 |
| 2 | 10,600,327 | 10,643,847 |
| 3 | 30,077,258 | 30,230,026 |
| 4 | 2,303,600 | 2,106,224 |
| 5 | 0 | 1,088 |
| Total | 43,046,721 | 43,046,721 |

In particular \(F_R^4\equiv\mathbf0\) but \(F_R^3\not\equiv\mathbf0\), whereas \(F_S^5\equiv\mathbf0\) but \(F_S^4\not\equiv\mathbf0\). These are sharp identities of the *entire maps*, not approximate statements about sampled states. The 1,088 initial configurations attaining time five on \(S\) form exactly eight classes under the full graph automorphism group of order 192, with class sizes \(192,192,192,192,96,96,96,32\). Their least-base-three-code representatives are \(563061,627004,640093,685291,2228096,2382581,2915821,2933623\), with orbit sizes paired in `symmetry_orbits.csv`.

## Assumptions and scope

The labelled vertex set is \(V=\{0,\ldots,15\}\), with \(v=x+4y\) representing \((x,y)\in\mathbb Z_4^2\). Distinct vertices are adjacent in \(R\) when they agree in one coordinate; in \(S\) when their difference is in \(\{\pm(1,0),\pm(0,1),\pm(1,1)\}\) modulo four. Exactly three excited neighbors are sufficient; the inequality in the activation rule is non-strict. A state is a function \(c:V\to\{0,1,2\}\) (resting, excited, refractory). States are labelled, so no spatial quotient is taken for the extinction table. A representative code is \(\sum_{v=0}^{15}c(v)3^v\). No assertion concerns other thresholds or unbounded graph families.

## Proof

**Graph structure.** For each graph, the explicit adjacency rule gives six neighbors at each vertex and exactly two common neighbors for any two distinct vertices, regardless of adjacency. Equivalently the adjacency matrix satisfies \(A^2=4I+2J\). Consequently the two graphs have identical adjacency eigenvalues with multiplicities \(6^1,2^6,(-2)^9\). A rook vertex's six-neighbor induced subgraph consists of two disjoint triangles, whereas a Shrikhande vertex's induced neighborhood is a six-cycle; thus the two graphs are nonisomorphic. The standalone `invariants.py` checks these identities directly without a graph database.

**Finite-state exhaustive proof.** Let \(E_t=\{v:c_t(v)=1\}\) and \(Q_t=\{v:c_t(v)=2\}\), and put \(T_G(E)=\{v:|N_G(v)\cap E|\ge3\}\). The transition is exactly
\[
(E_{t+1},Q_{t+1})=\bigl(T_G(E_t)\setminus(E_t\cup Q_t),\ E_t\bigr).
\]
A disjoint pair \((E,Q)\) is equivalent to precisely one three-state configuration. `exhaustive.cpp` independently enumerates all integer codes from zero through \(3^{16}-1\), decodes each into disjoint masks, applies this transition until extinction, and counts the first extinction time. Every code reaches the rest state by the displayed upper bound; an unresolved nonzero trajectory would explicitly terminate the program with an error. The program produces the six counts in the table. Since the entire finite state space is enumerated, this is a complete proof by exhaustive finite computation rather than a simulation or partial experiment.

**Independent weighted combinatorial certificate.** The separately implemented `weighted.cpp` enumerates only the possible pairs of initial excited masks and next excited masks. For initial excited set \(E\), set \(H_E=T_G(E)\setminus E\). Every next excited set \(B\) is a subset of \(H_E\). To realize \(B\), the initial refractory set must contain exactly the vertices of \(H_E\setminus B\) inside \(H_E\), and may choose any subset outside \(E\cup H_E\). Thus **each pair** \((E,B)\) represents exactly
\[
2^{16-|E|-|H_E|}
\]
initial configurations, and its time-one state is precisely \((B,E)\). The weighted algorithm iterates all \(4{,}174{,}906\) such pairs for the rook graph and all \(4{,}255{,}298\) for Shrikhande, with weights totaling \(43{,}046{,}721\) in each case, and independently computes the first-extinction histogram from these time-one states. One all-rest starting state is reallocated from time one to time zero. Both exact histograms match the first implementation in every entry. This grouping covers every initial refractory assignment without duplicated or omitted states.

**Symmetry of the final shell.** The Shrikhande generators admit 12 invertible linear coordinate maps preserving the six-element generating set, and 16 translations, giving 192 distinct automorphisms. Conversely, the image of a vertex has at most 16 choices, and an automorphism fixing it induces an automorphism of its six-cycle neighborhood, giving at most 12 choices. Since each remaining vertex is determined by its neighborhood trace, the full group has order at most \(16\cdot12=192\). The standalone `symmetry.py` constructs the 192 maps, checks adjacency, and groups all 1,088 extremal state codes generated by `exhaustive.cpp` into the eight asserted orbits, with the given representatives and sizes.

## Verification

From the directory of the accompanying files run `sh verify.sh` with C++17 compiler `g++` and Python 3 installed. It compiles and runs the independent programs, checks the complete six-entry extinction histograms and population totals, validates the strongly regular graph identities, and reconstructs all eight final-shell symmetry orbits. The script prints `VERIFICATION_OK` only if every exact check succeeds. The `census.csv` and `symmetry_orbits.csv` list the two claimed finite data tables. The second algorithm uses an exact multiplicity reduction, not a second traversal of the same full-state code list.

For sharpness, the encoded initial state 7546 on the rook graph first reaches rest at time four; encoded state 563061 on Shrikhande first reaches rest at time five. The enumerated maximal-shell counts are exact. The proof is purely finite and makes no claim about general graphs or infinite lattice limits.

## Relationship to prior work

The 1993 Durrett–Griffeath preprint treats threshold and neighborhood parameters for excitable cellular automata, rather than the exact finite relaxation census for these graphs. Gravner–Lyu–Sivakoff (first public preprint 2016-10-24) study *single-neighbor contact*, and their graph covering/closed-walk results do not provide the three-neighbor census. Doba's finite-graph study also explicitly adopts the one-neighbor rule. The published result *Four-cycle excitation clocks distinguish the Shrikhande and rook graphs* gives a complete census for the **threshold-one** version on the same two graphs; that prior result is closely related but has a different transition map and does not imply these sharp critical-threshold extinction times. Earlier half-degree period-three rigidity and more recent general triangle rigidity explain or constrain certain recurrent possibilities, but do not give the exact four-versus-five extinction clocks, the six temporal-shell counts, or the eight Shrikhande final-shell symmetry classes. Thus the contribution claimed here is the **sharp critical-threshold temporal and symmetry census**, not the graph pair, update rule, or universal-extinction principle in isolation.

## Limitations

Only the two explicitly defined sixteen-vertex graphs and the fixed threshold three are classified. Enumeration proves the stated finite identities, not an all-size theorem. The primary-source and published-record comparisons reduce but cannot eliminate historical-priority uncertainty, especially for equivalent unindexed finite computations. Neither independent external replication nor formal external certification is claimed.

## References

1. R. Durrett and D. Griffeath, *Asymptotic Behavior of Excitable Cellular Automata*, first public 1993-03-22, arXiv:patt-sol/9303002, https://arxiv.org/abs/patt-sol/9303002.
2. J. Gravner, H. Lyu and D. Sivakoff, *Limiting behavior of 3-color excitable media on arbitrary graphs*, first public 2016-10-24, arXiv:1610.07320v1, https://arxiv.org/html/1610.07320v1, especially §§1–2.
3. N. Doba, *The Time Evolution of a Greenberg–Hastings Cellular Automaton on a Finite Graph*, *Complex Systems* 27 (2018), 101–120, DOI:10.25088/ComplexSystems.27.2.101, https://wpmedia.wolfram.com/sites/13/2018/09/27-2-1.pdf, especially §§1–2.
4. *Four-cycle excitation clocks distinguish the Shrikhande and rook graphs*, publicly indexed finding, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-four-cycle-excitation-clocks-distinguish-the-shrikhande-and-rook--bc07c832e978, particularly the threshold-one Finding and Proof.
5. *Half-degree rigidity and a sharp contact-threshold collapse on squared cycles*, publicly indexed finding, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-half-degree-rigidity-and-a-sharp-contact-threshold-collapse-on-s--7c3fe196f42d, especially the general half-degree characterization.
6. E. W. Weisstein, *Shrikhande Graph*, MathWorld, https://mathworld.wolfram.com/ShrikhandeGraph.html.
