# Sharp reset thresholds for binary Eulerian synchronizing automata: exact maxima for n <= 7, a certified 25-extremal at n = 8, and its fiber-optimality certificate

## Context

The Cerny conjecture (reset threshold `<= (n-1)^2`) is the central open problem
on synchronizing words. For Eulerian automata Kari proved an Eulerian upper
bound `(n-1)(n-2)+1 = n^2-3n+3`, while Szykula-Vorel gave a quaternary series
with reset threshold `>= (n^2-3)/2` (i.e. `floor((n^2-3)/2)`) and conjectured
tightness. The binary Eulerian subcase (two letters, indegree exactly 2 per
state) had no published extremal table: binary Eulerian automata cannot be
circular, Vorel (2014) studied only NP-completeness of bounded reset, and
general small-n surveys (binary n <= 12 verified) never separated the
Eulerian family. This record closes the binary Eulerian slice for n <= 7 and
certifies the strongest known even-n binary Eulerian extremal at n = 8.

## Definitions

Fix `Q = {0,...,n-1}`, `Sigma = {a,b}`. A binary DFA is a pair of maps
`a,b : Q -> Q`. For `S subset Q` and letter `x`, `S.x = {q.x : q in S}`;
for a word `w`, `S.w` is defined inductively. The automaton is
**synchronizing** if `Q.w = {s}` for some word `w` (a *reset word*); then
`rt(A)` is the minimum length of such `w`, equivalently the power-automaton
BFS distance from `Q` to the nearest singleton. The automaton is **Eulerian**
if `indeg_a(q)+indeg_b(q) = 2` for every `q in Q` (equivalently, with the
standard binary outdegree 2 per state in the labelled digraph, indegree
equals outdegree at each vertex; strong connectivity is verified separately
for the witness). Put

```
E(n) = max{ rt(A) : A synchronizing binary Eulerian, |Q| = n }.
```

Two automata are isomorphic if they differ by a simultaneous relabeling of
states; `rt`, the synchronizing property and the Eulerian property are
invariant under isomorphism.

## Result

**Theorem 1 (exact small maxima).** The exact maxima are

| n | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
|---|---|---|---|---|---|---|---|
| E(n) | 0 | 1 | 2 | 5 | 10 | 14 | 22 |

**Theorem 2 (certified 8-state extremal beating the sink benchmark).**
The binary automaton

```
a = (1,2,3,4,5,0,7,7),  b = (0,5,6,3,6,1,2,4)
```

is Eulerian, strongly connected, synchronizing, and has `rt(A) = 25`, e.g. via

```
w = bbaabaababbaaababaabaaaab  (|w| = 25),  Q.w = {6}.
```

Hence `E(8) >= 25`. Since the textbook binary sink (automata-with-zero)
family gives `n^2/4+2n-9 = 23` at `n = 8` (Volkov-survey variant
`ceil(n^2/4+3n/2-4) = 24`), this extremal sits strictly above the sink
benchmark and strictly inside the Kari / Szykula-Vorel gap:
`23 < 25 <= E(8) <= 43`, where `E(8) <= 43` is Kari's theorem
`(n-1)(n-2)+1` at `n = 8`, quoted not proved.
(Note: the candidate DRAFT misstates Kari's bound as `n^2-3n+4 = 44`;
the correct value is `n^2-3n+3 = 43`. No claim depends on the constant.)

**Theorem 3 (fiber-optimality of the spine).** Fix the one-cluster spine
`a = (1,2,3,4,5,0,7,7)`. Among all `20160` Eulerian `b`-completions of this
spine, exactly `19296` are synchronizing and the maximum reset threshold is
`25`, attained e.g. at `b = (0,5,6,3,6,1,2,4)`. Hence no completion of this
spine beats the witness.

**Table 1 — extremal witnesses** (each verified Eulerian and replayed):

| n | E(n) | a | b |
|---|---|---|---|
| 4 | 5 | (0,0,1,3) | (2,3,2,1) |
| 5 | 10 | (0,0,2,4,3) | (3,2,1,1,4) |
| 6 | 14 | (0,0,2,4,5,3) | (3,2,1,1,4,5) |
| 7 | 22 | (0,0,2,4,3,6,5) | (3,5,4,1,2,1,6) |
| 8 | >= 25 | (1,2,3,4,5,0,7,7) | (0,5,6,3,6,1,2,4) |

**Compression profile of w** (first-reach BFS distance by subset size):
sizes `8,7,6,5,4,3,2,1` are first reached at distances `0,1,2,4,7,10,17,25`.

**Negative / bounding evidence at n = 8 (conjecture, NOT proof).**
About 75,000 heuristic trials (uniform Eulerian pairs, one-cluster spines,
one-swap neighborhood of the witness) found no automaton with `rt > 25`.
It is conjectured that `E(8) = 25` but this is NOT claimed here.

## Proof / evidence

**Power-automaton BFS.** States are bitmasks over `Q`; BFS from full set `Q`
following images under `a,b` until the first singleton. Two independent codes
agree everywhere: (i) forward BFS from `Q`; (ii) reverse BFS from all
singletons via letter-preimages. Both reproduce the Cerny values `(n-1)^2`
for `n = 3,...,8` as a sanity check. The auditor re-implemented both codes
from scratch and reproduced `rt = 25` for the witness with `0`
forward/reverse disagreements, replayed `Q.w = {6}`, verified the Eulerian
indegrees `indeg_a = [1,1,1,1,1,1,0,2]`, `indeg_b = [1,1,1,1,1,1,2,0]`,
the Eppstein pair-merging synchronizing test, strong connectivity, and the
compression profile above (174 reachable subsets).

**Exact census for n <= 7.** Key reduction: every pair `(a,b)` is isomorphic
to `(a0,b')` with `a0` a canonical representative of the `S_n`-orbit of `a`
(conjugation `a0 = pi a pi^{-1}`, `b' = pi b pi^{-1}`), with identical `rt`
and Eulerian status; as `b` ranges over Eulerian completions of `a`, `b'`
ranges over Eulerian completions of `a0`. Hence the global maximum equals
the maximum over canonical `a`-reps of the exhaustive fiber maximum, and no
pair-isomorphism pruning is needed. Canonical `a`-types use the AHU
functional-digraph invariant (sorted rooted-tree codes above each directed
cycle, cycles rotated to lexicographic minimum, components sorted).
Validated exhaustively: AHU-code partition equals brute-force `S_n`
canonical-orbit partition for `n = 4` (19/19 groups) and `n = 6`
(130/130 groups) with zero mismatches (plus the `n = 5` 47-group check in
the artifact), and by random-collision isomorphism search at `n = 7`
(2092/2092 same-AHU collisions genuinely isomorphic). Independent full
brute force over ALL Eulerian pairs for `n = 2` (6 pairs), `n = 3`
(90 pairs), `n = 4` (2520 pairs), `n = 5` (113400 pairs) reproduces
`E = 1,2,5,10`. Total BFS runs over AHU-rep fibers:
222 (`n = 4`), 1980 (`n = 5`), 23580 (`n = 6`), 301770 (`n = 7`)
(valid AHU reps 15/31/75/164). The `n = 7` census was re-run end-to-end by
the auditor: 164 reps, 301770 runs, global max 22. All Table 1 witnesses
replay to their claimed `rt` under both BFS codes and pass the Eulerian check.

**Fiber exhaustion at n = 8.** `indeg_a = (1,1,1,1,1,1,0,2)`, so the Eulerian
need-profile is `(1,1,1,1,1,1,2,0)`: `8!/2! = 20160` distinct `b`-completions,
each BFS-certified (`~2 s` total). The auditor independently re-enumerated
the fiber with distinct-multiset backtracking: 20160 completions, 19296
synchronizing, max 25, forward/reverse agreement on every synchronizing case.

## Limitations

(i) Global maximality `E(8) = 25` is conjectured, not proved — only
fiber-maximality and ~75k heuristic trials support it.
(ii) The Kari upper bound 43 is quoted from the literature, not re-proved.
(iii) The "closed-form reset-word induction" of the topic prompt is delivered
only as the audited compression profile (first-reach distances per subset
size), not as a parametric infinite family.
(iv) AHU-canonical grouping is validated exhaustively at `n = 4,5,6` plus
sampling at `n = 7`; correctness for the `n = 7` census additionally rests on
standard AHU theory and the successful end-to-end rerun.

## Reproducibility

With `output/artifacts` on the path:
`python3 verify_witness.py` (rt = 25, Eulerian, word replay, compression
profile), `python3 bfs2.py` (two-code agreement + Cerny sanity),
`python3 fiber.py` (fiber max 25 over 20160 completions),
`python3 exact_E.py N` for `N = 4,5,6,7` (exact `E(N)`; `N = 7` takes seconds
for BFS plus grouping; run from the directory containing
`output/artifacts` on `sys.path` as the script expects, e.g. with
`inputs/artifacts` copied to `output/artifacts`).

## References

- Szykula, Vorel, "An Extremal Series of Eulerian Synchronizing Automata",
  arXiv:1604.02879 (quaternary `(n^2-3)/2` series; binary `n <= 11`
  bound verification; Martyugin odd-n binary `(n^2-5)/2` experiments).
- Kisielewicz, Kowalski, Szykula, "Experiments with Synchronizing Automata",
  arXiv:1607.04025 (binary n <= 12 Cerny verification, no Eulerian separation).
- Vorel, "Complexity of a Problem Concerning Reset Words for Eulerian Binary
  Automata", arXiv:1409.2003 (NP-completeness, no extremals).
- Volkov, "List of Results on the Cerny Conjecture and Reset Thresholds for
  Synchronizing Automata", arXiv:2508.15655 v4 (living survey; item A6
  Eulerian automata; item B1 automata with zero / sink benchmark).
- Kowalski, Szykula, "The Cerny conjecture for small automata: experimental
  report", arXiv:1301.2092.
