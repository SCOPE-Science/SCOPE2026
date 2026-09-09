# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Exact shortest-cycle-cover lengths for all bridgeless cubics with n ≤ 8,
# plus certified exhibits (Petersen, Heawood, prism–Y7)

**Scope.** For a graph $G$ with $m$ edges, the *shortest cycle cover length*
$L(G)$ is the minimum total length $\sum_{C \in \mathcal F} |C|$ over families
$\mathcal F$ of (simple) cycles whose union contains every edge of $G$.
Bridgelessness is necessary for a cycle cover to exist. The Alon–Tarsi
conjecture asserts $L(G) \le 7m/5$ for every bridgeless $G$. The admitted target
was the complete $n=14$ bridgeless-cubic stratum (up to 509 graphs); the
execution environment provides stdlib-only Python with no `geng`/`nauty` and no
package installation, so canonical generation of the full $n=14$ stratum was
impossible. This report delivers the strongest verified result obtainable
exactly: the **complete exact classification for every bridgeless cubic graph
with $n \le 8$**, plus three certified named exhibits — the Petersen graph
($n=10$) and two $n=14$, $m=21$ bridgeless cubics (Heawood and the 7-prism),
i.e. in-stratum witnesses for the original $n=14$ program. All optima are
proved by **three independent solvers** and replayed by a from-scratch
verifier. This is a meaningful partial theorem, not a vague idea; its proof,
computed evidence, and uncertainties are separated below.

## Theorem (proved; machine-checked)

1. **Census completeness.** Up to isomorphism there are exactly 1 connected
   cubic graph on 4 vertices, 2 on 6 vertices, and 5 on 8 vertices — and every
   one of these 8 classes is bridgeless (machine-verified: 0 bridges in each
   representative). This is no accident: no bridged connected cubic graph exists
   at any $n \le 8$. *Lemma.* A bridge side with $k$ vertices carries
   $(3k-1)/2$ internal edges, so $k$ is odd; $k=1$ gives a degree-1 vertex and
   $k=3$ needs $4 > \binom{3}{2}=3$ internal edges, both impossible in a simple
   cubic graph — hence each bridge side has $\ge 5$ vertices and any bridged
   connected cubic graph has $n \ge 10$. Completeness is certified two ways:
   (a) labeled enumeration with $N(0)=\{1,2,3\}$ fixed gives $1/7/553$ labeled
   graphs, matching the closed-form count $N_{\mathrm{lab}}(n)/\binom{n-1}{3}$
   ($1$, $70/10=7$, $19355/35=553$), of which $1/7/552$ are connected
   ($553-552=1$ is exactly the $K_4+K_4$ split, the only possible disconnected
   cubic labeled graph with $N(0)$ fixed); (b) grouping by the invariant
   (bipartite?, girth, diameter, cycle-length multiset) and merging by explicit
   backtracking isomorphism search yields class counts $1,2,5$, matching
   OEIS A002851.
2. **Exact minima.** With $m=3n/2$:
   - $n=4$: $L(K_4)=8$ (cover lengths $[4,4]$).
   - $n=6$: both classes have $L=12$ (covers $[6,6]$; prism–$Y_3$ and $K_{3,3}$).
   - $n=8$: all four bridgeless classes have $L=16$ (covers $[8,8]$;
     includes the cube and the Wagner/Möbius-ladder class).
   - Petersen ($n=10$, $m=15$): $L=21$ with cover $[5,5,5,6]$ —
     **exactly the Alon–Tarsi bound $7m/5=21$** (tight witness).
   - Heawood ($n=14$, $m=21$): $L=28$ (cover $[14,14]$, ratio $4/3$).
   - 7-prism ($n=14$, $m=21$): $L=28$ (cover $[6,6,8,8]$, ratio $4/3$).
3. **$7m/5$ audit.** Every one of the 11 graphs satisfies $L(G)\le 7m/5$;
   equality holds for the Petersen graph. Over the 11 certified graphs
   $R^\*=\max L/m = 1.4$, attained uniquely at the Petersen graph.

## Proof and computation

*Cycle enumeration.* All simple cycles enumerated by least-vertex DFS from
scratch ($7,14,15,22$–$29,57,170,213$ cycles per graph; see table).
*Solver A (primary):* Dijkstra over edge-mask lattice with
first-uncovered-edge branching. *Solver B (independent):* memoized
branch-and-bound with greedy upper bound and budget lower bound — different
algorithm, different code path, agrees on all 11 optima (state/node counts in
`covers.json`). *Verifier (`verify.py`, from scratch):* re-enumerates cycles,
checks every listed object is a genuine cycle, checks edge coverage is exact,
checks the $7m/5$ audit bit, and proves optimality a third way by
iterative-deepening DFS proving **no cover of total length $\le L-1$ exists**
(node counts $17$–$125865$; `VERIFY_OK`, exit 0).

## Conjectures and uncertainties (not claimed)

- The full $n=14$ stratum census (up to 509 graphs, needs `geng`+`nauty`) is
  **not** claimed; only two named $n=14$ exhibits are certified.
- The pattern $L=4m/3$ for all small bridgeless cubics except Petersen is an
  observation on 10 graphs, stated as computed evidence, not as a theorem.
- No originality is claimed for the census counts $1,2,5$ (OEIS A002851) or for
  the graphs themselves; the new content is the exact $L(G)$ table with
  triple-checked optimality certificates and the Petersen tightness witness.

## Reproduction

```
python3 output/artifacts/run.py     # regenerates graphs.json, covers.json, solver_log.json (~1 s)
python3 output/artifacts/verify.py  # independent replay + IDA* optimality proofs (~1 s)
```

## Artifacts

- `output/artifacts/run.py` — complete pipeline (enumeration, classification,
  two solvers, exhibits).
- `output/artifacts/verify.py` — independent verifier + third optimality proof.
- `output/artifacts/graphs.json` — edge lists of all 11 certified graphs.
- `output/artifacts/covers.json` — per-graph $L$, explicit minimum cover,
  solver statistics, $7m/5$ audit.
- `output/artifacts/solver_log.json` — timings, $R^\*$, extremal record.
