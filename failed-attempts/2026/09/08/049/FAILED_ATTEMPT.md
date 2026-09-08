# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Girth-constrained independence extremal among cubic bridgeless graphs on 12-18 vertices
- **Round:** 2026-09-07-first-light-01
- **Lane:** 155
- **Disposition:** AUDIT_1_REJECT
- **Domain:** Extremal Graph Theory
- **Method:** canonical cubic-graph generation with girth computation and independence-number branch-and-bound verification

## Problem

Survey all cubic bridgeless graphs on even orders 12<=n<=18: canonically generate each order, compute girth and exact independence number with replayable logs, and determine the girth-constrained independence extremal (maximum alpha/n subject to girth constraint) plus the full per-order extremal table.

## Attempted claim

There exists a certified girth-constrained independence extremal among cubic bridgeless graphs with even orders 12<=n<=18: a witness graph W on n* in {12,14,16,18} with girth g*>=4 (girth class as populated, targeting >=5 where nonempty) and independence number alpha* such that alpha*/n* = max{alpha(G)/|V(G)| : G cubic bridgeless, |V(G)| in window, girth(G)>=g*}, exceeding every other surveyed graph in the same (n*,g*>=g*) class by an integer gap of at least 1 in alpha, certified by exhaustive canonical generation and per-graph branch-and-bound replay logs, accompanied by the complete per-order table M(n,g).

## Research outcome

Exact maxima M(n,g)=n/2 proved for seven (n,g) cells ((12,4),(14,4),(14,6),(16,4),(16,6),(18,4),(18,6)) among cubic bridgeless graphs on 12-18 vertices: Petersen matching theorem gives the universal n/2 ceiling and seven audited bipartite witnesses (edge lists + stdlib replay script) force equality. Girth-3/5 cells and full-window exhaustiveness explicitly excluded.

## Why this attempt failed

Failed axes: value.

value: The 7-cell headline M(n,g)=n/2 is a textbook restatement / mechanically implied ceiling, even if correct and narrowly new as a table. For any (n,g) cell containing one bipartite bridgeless cubic graph, M=n/2 follows in one line: bipartite partite set gives alpha>=n/2; Petersen matching gives alpha<=n/2 for every cell member. The entire content therefore reduces to existence of a bipartite example per cell. Five cells are classical existence: (12,4)/(16,4) hexagonal/octagonal prisms (infinite bipartite prism family, m even); (14,6) Heawood unique (3,6)-cage; (16,6) GP(8,3)=Moebius-Kantor (n even, k odd => bipartite, girth 6); (18,6) 18-vertex bipartite cubic girth 6 (Pappus graph is the textbook 18-vertex cubic bipartite girth-6 example; the committed ring-plus-offset-5 graph is the same stratum). The remaining two witnesses (14,4)/(18,4) are explicitly disclaimed as arbitrary computer-found adjacency data with no canonicity, novelty, or mathematical interpretation claimed. No separated integer gap exists by the authors' own admission (all maxima hit the n/2 ceiling; ties are the rule), so the original gap-witness target failed; no complete M(n,g) table was delivered (girth 3 and 5 explicitly unclaimed). No conjecture is tested, no heuristic needs this precise tabulation beyond consulting standard cage/prism references, and the B&B pipeline is admittedly unused for the final upper bounds. Per the standard, a narrow exact datum can pass only when motivated before computation, not mechanically implied, and reasonably retrievable later; here the value is mechanically implied by cited 1891 + bipartite facts plus known graphs, and certification alone does not rescue arbitrary objects. This is intrinsic low value, not a fixable presentation defect.

## Conditions for a legitimate retry

supply independent motivation and a materially stronger contribution; address the recorded limitation: Partial theorem: only 7 of the M(n,g) cells are determined; girth-3 maxima (sampling bests 5,6,7,8 for n=12,14,16,18), girth-5 maxima, and remaining even-girth cells are NOT claimed. No separated integer-gap witness (all maxima hit the n/2 ceiling, so ties are the rule). Exhaustive generation over ~46k graphs was not performed (no nauty/geng in sandbox; custom pure-stdlib augmentation stalled) — enumeration-free proof via matching bound instead. (12,6) cell is empty by the classical (3,6)-cage…

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
