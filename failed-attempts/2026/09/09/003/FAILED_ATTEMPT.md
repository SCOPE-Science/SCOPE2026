# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Shortest cycle cover classification over the complete bridgeless-cubic stratum at order 14 with tightness extremal
- **Round:** 2026-09-07-first-light-01
- **Lane:** 274
- **Disposition:** AUDIT_1_REJECT
- **Domain:** Structural Graph Theory
- **Method:** exhaustive cycle enumeration plus exact minimum-weight set-cover optimization with optimality certificates

## Problem

Over the complete set of non-isomorphic bridgeless cubic graphs at fixed order n=14, determine by exact optimization the shortest cycle cover length L(G) (minimum total cycle length covering all edges) for every G, with one explicit minimum cover per graph and optimality certificate, and identify the worst-case ratio R*=max_G L(G)/m with extremal witness G* deciding tightness of the 7m/5-type upper bound inside this stratum.

## Attempted claim

For every non-isomorphic bridgeless cubic graph G on 14 vertices (m=21), the tabulated shortest cycle cover length L(G) is exact witnessed by one explicit minimum-total-length cycle list covering all edges plus an optimality (no-shorter-cover) certificate; the stratum maximum R*=max_G L(G)/21 is as computed (determined by the run) attained at explicit extremal G* with exhibited minimum cover, deciding whether the 7m/5 upper bound is tight in this complete stratum.

## Research outcome

Triple-checked exact shortest-cycle-cover table for all bridgeless cubics with n<=8 plus Petersen (tight 7m/5 witness, L=21) and two n=14 exhibits (Heawood, 7-prism, L=28 each); census completeness certified by labeled-count identities and A002851 match; independent verifier replays all covers and proves all optima.

## Why this attempt failed

Failed axes: originality.

originality: Strongest headline (Petersen L=21 = 7m/5 tight witness) is substantively anticipated. Hagglund-Markstrom arXiv:1306.3088 Sec.1 states that Brinkmann et al. [BGHM13] generated all snarks to n<=36 and computed scc(G), finding only two with scc=4m/3+1 — the Petersen graph and a 34-vertex snark — all others 4m/3. For Petersen m=15, 4m/3+1=21=7m/5. This is an explicit prior publication of the exact headline value and its tightness meaning, not a different invariant. Existence/upper-bound theory does not merely bound it: the prior is an exact-minimum computation of the same invariant on the same graph. The remaining n<=8 + Heawood values L=4m/3 are mechanically implied without search: universal cubic lower bound L>=4m/3 (each vertex needs >=2 cycle incidences, so L=sum t_v >=2n=4m/3) plus the textbook upper bound 'if G is 3-edge-colourable then scc=4m/3 by taking two pairs of colours' (stated as easy in the same prior, Thm 5.4: tau<=4 => scc=4m/3). All n<=8 cubics are Class 1 by the classical smallest-snark-is-Petersen fact; Heawood is bipartite hence 3-edge-colourable by Konig. So those table entries require only exhibiting a 4m/3 cover, no new optimization. 7-prism value 28=4m/3 is likewise a lower-bound-tight cover, not a new tightness phenomenon. No source tabulating per-graph minima for the full n=14 stratum was found, but the delivered headline is not that census — it is the Petersen tight witness plus small 4m/3 cases — and the former is prior. A timestamp or failed search does not establish priority; substantive comparison shows definitional anticipation. Hence FAIL, which is never repairable.

## Conditions for a legitimate retry

state a substantive result not covered by the identified prior work; address the recorded limitation: Full n=14 stratum census NOT completed (environment lacks geng/nauty and package installation); only two named n=14 exhibits certified. Optimality certificates are machine-checkable search logs (Dijkstra states, B&B nodes, IDA* nodes), not human-readable proofs. The L=4m/3 pattern on small graphs is an observation, not a theorem.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
