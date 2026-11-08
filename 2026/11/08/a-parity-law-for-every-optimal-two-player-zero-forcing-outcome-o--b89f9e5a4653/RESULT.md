# A parity law for every optimal two-player zero-forcing outcome on \(K_n-e\)

## Finding
Consider the competitive two-player zero-forcing game with the Force Preservation Rule and set-valued backward-induction convention of Annor and Howerton [1]. In particular, each player minimizes only their own seed count, and all tied optimal continuations are retained. Write \(\mathcal O(G)\) for the set of ordered final seed-count pairs, with Alice first.

**Theorem.** For every integer \(n\ge4\), delete any one edge from the complete graph \(K_n\). The entire optimal-outcome correspondence is
\[
\mathcal O(K_n-e)=
\begin{cases}
\{(k-1,k-1)\},&n=2k,\quad k\ge2,\\
\{(k,k-1),(k,k)\},&n=2k+1,\quad k\ge2.
\end{cases}
\]
Consequently the game zero-forcing number satisfies \(Z_g(K_n-e)=n-2\) for all \(n\ge4\). If \(n\) is odd, there are optimal outcomes with **two different total seed counts**, namely \(n-2\) and \(n-1\), at every odd order at least five; if \(n\) is even there is only one optimal ordered outcome. The excluded graph \(K_3-e=P_3\) has \(\mathcal O(P_3)=\{(1,1)\}\).

## Assumptions and scope
All graphs are finite, simple and undirected. Let the two nonadjacent vertices of \(K_n-e\) be \(x,y\), and let its other \(r=n-2\) vertices form a universal clique. Alice moves first. On each turn the mover colours one previously white vertex either by a force from an already-owned vertex with exactly one white neighbour, or by seeding it. A target available as an own force is always treated as a force, never as a seed. A seed that destroys an opponent's currently available force is allowed only when every available seed would destroy an opponent force; executing an own force is always allowed. The payoff is the ordered pair of total seeds; at every decision node retain **all** children yielding the minimum seed count for the mover. These are precisely the rules of [1, Sections 2 and 5.1], without secondary tie breaking.

Equivalently, since each player has a predetermined number of turns, we maximize the corresponding coordinate of the ordered pair of **force counts** in backward induction. We denote that future-force correspondence by \(F\).

## Proof
**1. All possible forces.** At any position let \(w\) be the number of white vertices in the universal clique, and let \(q\) be the number of white vertices among \(x,y\). A coloured clique vertex has exactly \(w+q\) white neighbours. A coloured exceptional vertex has exactly \(w\) white neighbours. Thus a coloured exceptional vertex can force the last white clique vertex exactly when \(w=1\), while a coloured clique vertex can force the sole remaining white vertex exactly when \(w+q=1\). There are no other possible forces. In particular, when \(w\ge2\), **neither player has any force at all**, and every white vertex is a legal seed target.

**2. Exact quotient state.** A position is represented by a six-component state
\[
(w,\alpha,\beta,u_A,u_B,p),
\]
where \(\alpha,\beta\in\{0,A,B\}\) record whether \(x,y\) are white or are owned by Alice or Bob; \(u_A,u_B\in\{0,1\}\) record whether each player owns at least one coloured clique vertex; and \(p\in\{A,B\}\) is the mover. There are exactly \(3^2\cdot2^2\cdot2=72\) possibilities other than \(w\). These data determine every possible force target, every blocking seed target, and the successor quotient state. The numbers of already-coloured clique vertices owned by either player matter only through the two nonzero indicators, because all clique vertices have the same remaining white neighbourhood. Thus quotienting identifies genuinely equivalent continuations, not merely numerically similar configurations.

For completeness, if \(w+q=1\), any player with \(u_p=1\) can force that unique white vertex; if \(w=1\), a player owning either exceptional vertex can force the unique remaining white clique vertex. The force targets of the opponent are determined by the analogous tests. A target for an own force is an available force, not an alternative seed; among remaining seed targets, a target blocking an opponent force is excluded exactly when at least one nonblocking seed target exists. Every move changes a white vertex to the mover's colour, and the mover changes. Thus the explicit recurrence is: form the union of force-count pairs from all legal successor states, increment the mover's coordinate by one for an own force, and retain all pairs whose mover's coordinate is largest. Its terminal value is \(\{(0,0)\}\). This is exactly the defining backward induction, with no hidden assumptions about a preferred tie.

**3. The two-step transfer lemma.** Let \(F_w\) be the complete table of all 72 future-force correspondences at a fixed \(w\), including formal combinations that are unnecessary for the initial graph. For \(w\ge2\) no move can be a force, so the recurrence for \(F_w\) depends on \(F_{w-1}\) and on entries of \(F_w\) having fewer white exceptional vertices. Solving the latter entries in increasing order of already-coloured exceptional vertices defines a **single deterministic transfer map** \(\Phi\), independent of \(w\), such that
\[
F_w=\Phi(F_{w-1})\qquad(w\ge2).
\]
The cases \(w=0,1\) use the force and preservation tests of Step 2 directly.

The finite lemma \(F_3=F_5\) holds *entry by entry for all 72 states*. Its complete 72-row certificate is `periodicity_certificate.tsv`; the dependency-free `verify.py` reconstructs both tables directly from the transition rules, checks all 72 equalities, and compares the quotient computation with a separate vertex-labelled backward-induction implementation. This is a finite exhaustive lemma with an explicitly given recurrence and checkable certificate, not an extrapolation from a few graph orders.

Applying the same transfer map repeatedly gives
\[
F_6=\Phi(F_5)=\Phi(F_3)=F_4,
\quad F_7=\Phi(F_6)=\Phi(F_4)=F_5=F_3,
\]
and induction proves \(F_{w+2}=F_w\) for every \(w\ge3\). This last step proves the assertion for unbounded graph orders; the finite table supplies only its base lemma.

**4. Root entries and seed conversion.** Initially both exceptional vertices are white, neither player owns a clique vertex, Alice moves, and \(w=n-2\). The same finite recurrence gives the root force-count sets
\[
F_2(0,0,0,0,A)=\{(1,1)\},\quad
F_3(0,0,0,0,A)=\{(1,0),(1,1)\},\quad
F_4(0,0,0,0,A)=\{(1,1)\}.
\]
The transfer lemma gives the same even/odd alternatives for every \(w\ge2\). Alice takes \(\lceil n/2\rceil\) turns and Bob takes \(\lfloor n/2\rfloor\). Subtracting the respective force counts yields exactly the seed-count sets in the theorem. Each has minimum total \(n-2\). The separate \(w=1\) root calculation gives \(\mathcal O(P_3)=\{(1,1)\}\). This completes the proof.

## Verification
The included files `verify.py` and `periodicity_certificate.tsv` are standalone and require only Python's standard library. From a directory containing both, run `python3 verify.py`. The verifier checks the **entire** 72-entry equality \(F_3=F_5\), checks the initial entries, checks additional cases with \(2\le r\le100\), and independently evaluates the full vertex-labelled game tree for every \(3\le n\le10\). The vertex-level implementation constructs the adjacency matrix and the legal force targets without using the quotient-state formulas. The expected final line is `VERIFY_OK`. Only the exact 72-state lemma plus the mathematical transfer induction establishes the statement for all \(n\); the additional finite-order tests are cross-checks.

## Relationship to prior work
Annor and Howerton [1] introduced the game, the force-preservation convention, and set-valued optimal outcomes. Their Example 4 gives both seed-count outcomes on \(K_5-e\), and Proposition 23 proves the scalar game number on \(K_4-e\). Their exhaustive computational census of **all connected graphs through nine vertices** includes the finite orders \(n\le9\), so those small cases are not new. The contribution here is the unbounded-order ordered-outcome classification and its two-periodic quotient recurrence, in particular a uniform family of odd-order optimal-play ties for every \(n\ge11\) beyond that published finite census. Their results for paths, cycles, complete graphs and complete bipartite graphs do not imply the corresponding statement for edge-deleted cliques. Traditional one-colour zero forcing, oracle \(q\)-forcing, and other two-player graph-colouring games use different move/optimization conventions and are not equivalent formulations of this claim.

## Limitations
The theorem covers precisely one missing edge, not arbitrarily many deleted edges, general complete split graphs, or different tie-breaking conventions. The finite 72-state computation is a transparent part of the proof and should be rerun from the distributed files; it is not an independently authored mathematical audit. The primary manuscript and indexed records were searched, but priority relative to unpublished or unindexed equivalent results remains provisional.

## References
[1] Dickson Y. B. Annor and Ben Howerton, *A Two-Player Zero Forcing Game*, arXiv:2608.04579, first submitted 2026-08-05. https://arxiv.org/abs/2608.04579 . Relevant material: Sections 2, 3 (Example 4 and Proposition 23), 5.1–5.2.

[2] AIM Minimum Rank–Special Graphs Work Group, *Zero forcing sets and the minimum rank of graphs*, Linear Algebra and its Applications 428 (2008), 1628–1648. Classical one-colour zero forcing, distinguished from the competitive game in [1].
