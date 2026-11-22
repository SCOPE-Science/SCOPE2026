# Antipodal reply geometry in the dodecahedral domination game

## Finding

For the ordinary 20-vertex dodecahedral graph \(G\), the standard domination-game numbers are

\[
\gamma_g(G)=9,\qquad \gamma'_g(G)=8.
\]

The minimizer Dominator has a *one-move starting disadvantage*: optimal play ends one move earlier when Staller starts. Moreover, the first reply has an exact geometric characterization. If \(u\) is the opening vertex and \(v\neq u\) is the reply, assume optimal play thereafter. The total terminal move counts are:

| Distance \(\operatorname{dist}(u,v)\) | Vertices \(v\) at this distance | Dominator starts, then Staller replies | Staller starts, then Dominator replies |
|---|---:|---:|---:|
| 1 | 3 | 9 | 9 |
| 2 | 6 | 8 | 9 |
| 3 | 6 | 8 | 8 |
| 4 | 3 | 8 | 9 |
| 5 | 1 | 9 | 9 |

Each vertex is an optimal first move in either game. Thus Staller's optimal replies to a Dominator opening are precisely the three neighbors and the unique antipode (four replies); Dominator's optimal replies to a Staller opening are precisely the six vertices at distance three.

## Assumptions and scope

The graph is \(\operatorname{GP}(10,2)\), with vertex labels \(u_i,v_i\) for \(i\in\mathbb Z/10\mathbb Z\), and edges \(u_i u_{i+1}\), \(u_i v_i\), and \(v_i v_{i+2}\). All indices are read modulo ten. This is the standard simple cubic dodecahedral graph, not the geometric dual.

Dominator and Staller alternate selecting graph vertices. A move at \(w\) is legal if its closed neighborhood \(N[w]\) contains at least one previously undominated vertex. The new dominated set becomes the union of all closed neighborhoods of played vertices. The game ends precisely when every vertex is dominated. Dominator minimizes the number of moves and Staller maximizes it, under perfect play; the value includes both players' moves. Neither passing nor selecting a move that dominates no new vertex is allowed. The two games differ only in who moves first.

The theorem concerns this fixed graph and this standard game, not arbitrary cubic graphs, domination under adversarial deletions, ordinary static domination, or the matching-saturation game.

## Proof

**Exact finite-game recurrence.** Encode subsets of the twenty graph vertices by twenty-bit nonnegative integers; let \(F=2^{20}-1\) be the all-ones mask. For any dominated set \(A\), define \(D(A)\) (respectively \(S(A)\)) to be the number of *additional* moves required under perfect play if Dominator (respectively Staller) moves next. At \(A=F\), both values are zero. For any proper dominated set, set \(A_w=A\cup N[w]\) and let the legal moves satisfy \(N[w]\setminus A\neq\varnothing\). Then

\[
D(A)=1+\min_{w\text{ legal}}S(A_w),\qquad
S(A)=1+\max_{w\text{ legal}}D(A_w).
\]

Every legal move strictly enlarges \(A\), and a proper \(A\) admits a legal move by selecting any undominated vertex. Therefore the two formulas and terminal conditions uniquely determine every value by descending induction on the number of undominated vertices. They are not approximations or heuristic minimax searches.

**Exhaustive evaluation.** The included `artifacts/game_dp.cpp` computes both functions for *all* \(2^{20}=1,048,576\) dominated masks in reverse integer-mask order. All next masks are strict supermasks, hence have already been evaluated. An independently structured, memoized recursive computation in `artifacts/game_dp.py` evaluates the reachable dominated masks from the empty board and from all first-two-move positions. The two codes construct the graph with the same explicit edge definition but do not share a minimax implementation.

Both verifiers return \(D(\varnothing)=9\) and \(S(\varnothing)=8\). They also independently check all twenty possible opening vertices and all \(20\cdot19=380\) ordered pairs of distinct first and second vertices, under each starting convention: 760 conditional scores. The graph's distance profile from *every* vertex is \((1,3,6,6,3,1)\) over distances zero through five, and the conditional scores agree exactly with the table above.

Indeed, after \(u\) is first selected, the two game values are respectively \(1+S(N[u])\) and \(1+D(N[u])\). After a second move \(v\), the conditional terminal scores become \(2+D(N[u]\cup N[v])\) in the Dominator-first game and \(2+S(N[u]\cup N[v])\) in the Staller-first game. Every distinct \(v\) is legal: each closed neighborhood has four vertices and all twenty closed neighborhoods are distinct, so no \(N[v]\) is contained in \(N[u]\) for \(u\neq v\). This proves the complete response table and, by the minimax definitions, the optimal-move counts.

## Verification

The two included source files use only standard Python 3 or C++17 facilities and have no external data dependencies. From the directory containing `artifacts`, run:

```sh
python3 artifacts/game_dp.py
g++ -O2 -std=c++17 -Wall -Wextra artifacts/game_dp.cpp -o /tmp/game_dp_check
/tmp/game_dp_check
```

Compare their printed game values and five distance-response classes with `artifacts/python_output.txt` and `artifacts/cpp_output.txt`. Both checkers terminate with assertions if any of the 760 conditional scores, twenty first-move values, or twenty BFS distance profiles disagree. The C++ calculation covers all possible dominated subsets; the Python check supplies a second recurrence evaluation. All outputs come from reruns of these included sources, not from prior packages or a numerical conjecture.

## Relationship to prior work

Brešar, Klavžar and Rall (2010) introduced and formalized the standard domination game and proved general bounds and starting-player comparisons; their discussion gives the six-cycle as a smaller instance of a first-player disadvantage. Kinnersley, West and Zamani (2013) prove further general bounds and constructions for different starting conventions. Klavžar, Košmrlj and Schmidt (2016) characterize graphs with small game domination numbers, focusing on scores two and three. These results do not supply the fixed dodecahedral values or the distance-classified complete reply table by the stated theorems. Results about power domination, static total domination, and graph matching games on Platonic graphs address different rules and cannot by themselves evaluate this adversarial minimax game.

## Limitations

This is a finite, exactly reproducible result for one canonical graph, not a classification of a graph family or an infinite asymptotic theorem. Its exhaustive verification relies on the explicitly provided programs and their recurrence; no formal proof assistant or independent scholarly audit has been used. The publisher-accessible abstract of Kinnersley, West and Zamani (2013) was examined, but its complete text was not accessible in this check, so unindexed historical priority remains uncertain. No absolute priority claim is made.

## References

1. Boštjan Brešar, Sandi Klavžar and Douglas F. Rall, *Domination game and an imagination strategy*, SIAM Journal on Discrete Mathematics **24** (2010), 979–991. https://doi.org/10.1137/100786800 ; publicly dated August 17, 2010. Author preprint: https://users.fmf.uni-lj.si/klavzar/preprints/GameDomFinal.pdf
2. William B. Kinnersley, Douglas B. West and Reza Zamani, *Extremal problems for game domination number*, SIAM Journal on Discrete Mathematics **27** (2013), 2090–2107. https://doi.org/10.1137/120884742
3. Sandi Klavžar, Gašper Košmrlj and Simon Schmidt, *On graphs with small game domination number*, Applicable Analysis and Discrete Mathematics **10** (2016), 30–45. https://doi.org/10.2298/AADM160207003K ; author-available full text: https://pefmath.etf.bg.ac.rs/accepted/rad2349.pdf
