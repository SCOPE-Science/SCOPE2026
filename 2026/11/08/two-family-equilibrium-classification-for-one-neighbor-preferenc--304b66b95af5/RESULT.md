# Two-family equilibrium classification for one-neighbor preferences on cyclic networks

## Finding
For every integer \(n\geq3\), consider a simple cycle \(C_n\), with \(k\) occupied vertices and \(n-k\) vacant vertices, where \(0\leq k\leq n\). Each of the \(k\) agents has the same binary utility: utility \(1\) exactly when she has **one** occupied neighboring vertex, and utility \(0\) when she has zero or two. A deviation moves one agent to any vacant vertex, vacating her previous vertex. An allocation is *jump stable* if no such unilateral move strictly increases its mover's utility.

Write \(N(n,k)\) for the number of jump-stable **occupancy subsets of labeled cycle vertices**, without distinguishing the identities of agents. The full classification and exact count are as follows.

* For \(k=0\) or \(k=n\), the unique occupancy subset is stable. For \(k=1\), all \(n\) subsets are stable.
* For \(2\leq k<n\), a subset is stable if and only if it belongs to at least one of two families:
  * **Dimer family:** every cyclic occupied run has length exactly two, with positive-length vacant gaps between successive runs.
  * **Isolated-vacancy family:** every cyclic vacant run has length exactly one, and every cyclic occupied run has length at least two.

Put \(z=n-k\). For \(2\leq k<n\), define
\[
D(n,k)=\begin{cases}
\dfrac{n}{k/2}\binom{z-1}{k/2-1},&k\text{ even and }z\geq k/2,\\
0,&\text{otherwise},
\end{cases}
\]
and
\[
H(n,k)=\begin{cases}
\dfrac{n}{z}\binom{k-z-1}{z-1},&k\geq2z,\\
0,&\text{otherwise}.
\end{cases}
\]
Then the exact count is
\[
\boxed{N(n,k)=D(n,k)+H(n,k)-3\,\mathbf 1_{\{n=3z,\ k=2z\}}.}
\]
The terms involving division are integers by their circular-composition interpretation. Consequently, for \(2\leq k<n\), a stable placement exists if and only if
\[
\boxed{\bigl(k\text{ even and }3k\leq2n\bigr)\ \text{or}\ 3k\geq2n.}
\]
Below density \(2/3\), stability therefore requires an even population and all equilibrium occupied components are dimers; above density \(2/3\), all vacant sites must be isolated and all occupied runs must have length at least two. At the exact boundary \(3k=2n\), there are precisely three stable subsets, the rotations of a repeated \(110\) word. With \(k\) distinguishable agents, the number of stable labeled assignments is \(k!\,N(n,k)\). If an occupancy set is uniformly random among the \(\binom nk\) size-\(k\) subsets, its probability of stability is exactly \(N(n,k)/\binom nk\).

## Assumptions and scope
The underlying graph is a labeled, undirected, loopless simple cycle \(C_n\), with \(n\geq3\); each vertex accommodates at most one agent. Preferences depend only on the **number** of occupied adjacent vertices, not on the identities of neighbors. Every unilateral relocation to any vacant site is permitted, with no distance limitation and no cost of moving. Utility ties are not profitable deviations. No stochastic play or convergence of improvement dynamics is asserted. Distinguishable agents do not alter stability because their utilities are identical.

A cyclic occupied run is a maximal nonempty sequence of consecutive occupied vertices, and a vacant run is defined analogously. For full or empty occupancy the stated boundary cases apply; run-family definitions in the theorem apply only to \(2\leq k<n\).

## Proof
**Step 1 (a singleton occupied site is impossible at equilibrium when other agents exist).** Suppose \(k\geq2\) and an occupied vertex \(i\) has no occupied neighbors, so its occupant has utility \(0\). Travel clockwise from \(i\) to the first other occupied vertex \(j\). The predecessor \(v\) of \(j\) is vacant (the gap contains at least one vacancy). Moving the agent at \(i\) to \(v\) leaves \(j\) occupied and leaves the other neighbor of \(v\) vacant: it was already vacant if the gap exceeded one site, or it was \(i\) itself and is vacated by the move. Thus the relocated agent has exactly one occupied neighbor and gains utility \(1\). Therefore no stable allocation with at least two agents contains an occupied run of length one.

**Step 2 (if any agent is dissatisfied, all vacancies must be isolated).** Assume \(2\leq k<n\), no occupied singleton exists, and there is an occupied run of length at least three. Choose an interior vertex \(i\) of that run. It has two occupied neighbors, so its agent has utility \(0\), and both its neighboring vertices are occupied. If two consecutive vacancies existed, then a vacancy \(v\) at the end of a vacant run, immediately before an occupied run, would have exactly one occupied neighbor. Since \(i\) has no vacant neighbor, moving its agent to \(v\) would give utility \(1\). Hence a stable allocation with an occupied run of length at least three has no two consecutive vacancies. Combined with Step 1, this is exactly the isolated-vacancy family.

**Step 3 (both families are sufficient).** If every occupied run has length two, each agent has utility \(1\), so no strict improvement is possible. Otherwise assume every vacant run is a singleton and every occupied run has length at least two. Every agent with utility \(0\) is then internal to a run of occupied vertices, with two occupied neighbors. Every vacancy has two occupied neighbors, and none of those dissatisfied interior agents is adjacent to any vacancy. Such an agent therefore still has two occupied neighbors after jumping to any vacancy; it cannot improve. Agents already at utility \(1\) cannot improve either. The boundary cases of zero, one, or all occupied vertices are immediate. This proves the complete classification.

**Step 4 (exact circular counts).** For \(k=2r\) occupied agents in the dimer family, cyclically arrange \(r\) dimers, separated by \(r\) positive vacant gap lengths summing to \(z\). There are \(\binom{z-1}{r-1}\) positive compositions. Mark the first vertex of a designated dimer: there are \(n\) choices of root and each labeled occupancy pattern appears exactly \(r\) times. Thus this family has \(n\binom{z-1}{r-1}/r\) patterns, provided \(z\geq r\). For the isolated-vacancy family, there are \(z\) singleton vacant runs, separated by \(z\) occupied runs, each of length at least two. The excess \(k-2z\) occupied sites have \(\binom{k-z-1}{z-1}\) weak-composition assignments to the \(z\) run lengths. Rooting a designated vacancy gives \(n/z\) times this number. The two families overlap precisely if all occupied run lengths equal two and every vacant run equals one; hence \(n=3z\) and \(k=2z\). In that event the only patterns are the three rotations of the repeated \(110\) word, which must be subtracted once. The existence criterion follows by positivity of the corresponding composition counts. Finally, labels can be assigned to a fixed set of \(k\) occupied vertices in \(k!\) ways, and uniform occupancy probability is obtained by dividing by \(\binom{n}{k}\).

## Verification
The included `verify.py` independently tests the literal unilateral-deviation definition, the structural characterization, the exact count, and the nonexistence condition. It exhaustively enumerates \(131{,}064\) occupancy bit strings across \(3\leq n\leq16\), and separately tests \(600\) reproducibly sampled placements for \(n\in\{19,23,31,57\}\). Running `python3 verify.py` produces assertions and a `PASS` summary. This finite computation checks the implementation and small boundaries; it is **not** a substitute for the all-size proof above.

For illustration, with \(n=8\) and \(k=5\), no jump-stable allocation exists. With \(n=8\) and \(k=6\), exactly \(12\) stable occupancy subsets exist. With \(n=9\) and \(k=6\), precisely the three periodic configurations are stable.

## Relationship to prior work
Deligkas, Eiben, Schierreich, and Voudouris (2026) define anonymous-neighborhood network allocation and jump stability; their nonexistence construction for identical binary preferences also uses the exactly-one-neighbor utility, and they prove more general computational and tree-topology results. This theorem instead settles unrestricted jumps **on every simple cycle with homogeneous exactly-one-neighbor utilities**, giving necessary-and-sufficient structure, the sharp population obstruction, and a complete exact census not established by those general results.

Friedrich, Lenzner, Molitor, and Seifert (2023) study jump equilibria on rings under **two-colored, neighborhood-composition-based** single-peaked Schelling utilities. Their ring nonexistence and dynamics results do not imply the identical, degree-count-based one-neighbor classification given here. Aziz, Lisowski, Suzuki, and Vollen (2024) study an identity-dependent, fully occupied seat-assignment model with **local mutual swaps** rather than movements to vacancies. In particular, their cycle existence result does not settle the present unrestricted-jump equilibrium census. The enumeration of circular positive compositions is standard; what is asserted as new is the graph-game equilibrium equivalence and resulting exact structural boundary, not the binomial identities alone.

## Limitations
The result concerns one exact binary preference profile and the simple cycle; it does not classify arbitrary heterogeneous utilities, other graph topologies, or asynchronous dynamics. Counts concern pure equilibria under unilateral unrestricted jumps. Agent identities do not affect stability here. The source comparison is limited to the identified available literature and indexed records; an unindexed implicit equivalence cannot be ruled out. No independent mathematical audit has been performed.

## References
1. Argyrios Deligkas, Eduard Eiben, Šimon Schierreich, Alexandros A. Voudouris, *Network Allocation Games with Anonymous Preferences*, arXiv:2607.23248v1 (first posted 2026-07-25), https://arxiv.org/html/2607.23248v1.
2. Tobias Friedrich, Pascal Lenzner, Louise Molitor, Lars Seifert, *Single-Peaked Jump Schelling Games*, arXiv:2302.12107v1 (2023), https://arxiv.org/html/2302.12107v1.
3. Haris Aziz, Grzegorz Lisowski, Mashbat Suzuki, Jeremy Vollen, *Neighborhood Stability in Assignments on Graphs*, arXiv:2407.05240v1 (2024), https://arxiv.org/html/2407.05240v1.
