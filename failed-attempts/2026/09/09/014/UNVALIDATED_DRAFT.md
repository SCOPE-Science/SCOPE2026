# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Near-extremal stability spectrum of C4-free graphs to order 18

## Result

Let `ex(n)` = McKay/OEIS top-tier values taken as given inputs:
`0,1,3,4,6,7,9,11,13,16,18,21,24,27,30,33,36,39` for `n=1..18`.

**Theorem.** For every `2<=n<=18`, the second-maximum edge count among
C4-free simple graphs is `s(n) = ex(n)-1`; hence every stability gap
`g(n) = ex(n)-s(n) = 1` and the maximal gap `G = 1` (attained at every
`n>=2`). At `n=1` there is a single graph, so no second tier exists.

*Proof.* `s(n) <= ex(n)-1` since the second tier counts a strictly smaller
integer than the maximum. Conversely, let `H` be an extremal graph with
`ex(n)` edges (explicit matrices committed below; each machine-checked
C4-free with the right count). Deleting any single edge yields a C4-free
graph (a subgraph of a C4-free graph is C4-free) with exactly `ex(n)-1`
edges. So the `ex(n)-1` tier is populated and `s(n) = ex(n)-1`. There is
no integer strictly between `ex(n)-1` and `ex(n)`, so the no-between
certificate is vacuous arithmetic. ∎

**Polarity-embeddability.** Every extremal order is polarity-embeddable:
`n<=13` extremals are induced subgraphs of the orthogonal polarity graph
`ER_3` (13v/24e, prime-field construction), and `n=14..18` extremals are
induced subgraphs of `ER_4` (21v/50e over `GF(4)=GF(2)[t]/(t^2+t+1)`),
with raw keep-sets recorded in `artifacts/build_and_verify.py`. The `n=5`
extremal is the friendship graph `F_2` with explicit embedding
`0->0,1->1,2->4,3->7,4->10` into `ER_3` (edge images verified).

**KST residuals** `r(n) = floor(n/4*(1+sqrt(4n-3))) - ex(n)`:

| n | ex | KST floor | r |
|---|----|-----------|---|
| 1 | 0 | 0 | 0 |
| 2 | 1 | 1 | 0 |
| 3 | 3 | 3 | 0 |
| 4 | 4 | 4 | 0 |
| 5 | 6 | 6 | 0 |
| 6 | 7 | 8 | 1 |
| 7 | 9 | 10 | 1 |
| 8 | 11 | 12 | 1 |
| 9 | 13 | 15 | 2 |
| 10 | 16 | 17 | 1 |
| 11 | 18 | 20 | 2 |
| 12 | 21 | 23 | 2 |
| 13 | 24 | 26 | 2 |
| 14 | 27 | 28 | 1 |
| 15 | 30 | 32 | 2 |
| 16 | 33 | 35 | 2 |
| 17 | 36 | 38 | 2 |
| 18 | 39 | 41 | 2 |

Every witness also satisfies the pair-count check
`sum_v C(d_v,2) <= C(n,2)` (asserted in the verifier).

## How to verify (stdlib only)

```
PYTHONPATH=output/artifacts python3 output/artifacts/build_and_verify.py
# prints VERIFY_OK
```

It rebuilds `ER_3`/`ER_4` from arithmetic definitions, induces the
recorded keep-sets, and asserts edge counts, direct C4-freeness
(no pair shares two common neighbours), pair-count inequality,
KST residuals in `{0,1,2}`, and the `F_2`-into-`ER_3` embedding.
`artifacts/witnesses.json` holds the extremal edge lists, hosts,
`s(n)` table, and embedding. `c4tools.py`/`gf.py` are the shared
checkers/field arithmetic.

## Limitations / honesty

- Top-tier `ex(n)` values are inputs from McKay/OEIS, not re-proved here;
  the new content is the `s(n)=ex-1` determination, `G=1`, witnesses,
  polarity-embeddability table, and replayable logs.
- The headline collapses to `G=1` by the one-edge-deletion argument; this
  is a genuine (if small) classification boundary, not a deep stability
  census. `s(n)` counts are distinct-count tiers, not isomorphism counts.
- The `n=15` value 30 was confirmed as the maximum `ER_4`-induced count
  by exhaustive `C(21,15)` enumeration during research (not re-run by the
  verifier); extremality of all orders rests on the cited tables.
