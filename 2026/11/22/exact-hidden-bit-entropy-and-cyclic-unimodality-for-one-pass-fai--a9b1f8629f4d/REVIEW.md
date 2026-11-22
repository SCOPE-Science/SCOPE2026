# Scientific review

## Correctness
PASS (same-model). The proof treats all finite \(k\ge3\) without extrapolating from experiments. A proper cycle-edge subset is a forest; its product's permutation-cycle supports coincide with graph connected components. Possible distinct proper-subset collisions must be between different spanning trees. Full-edge collisions must match two-component forests. Both cases reduce to a single conjugacy equation, which is equivalent to chronological circular unimodality. There are exactly two double fibres in that case. A binomial interleaving count gives \(k2^{k-2}\) exceptional orders and the Shannon formula follows. `checker.py` independently tests every bit word and edge order through length eight and sampled longer orders. No part of the conclusion relies on a numerical continuation.

## Originality
PASS under available evidence, not a certification of worldwide priority. The 2026 motivating source treats many-step conditional mixing and pairwise collision estimates, not injectivity of a single cycle's full private-bit map. Cameron–Stott's *Trees and cycles* and Tsujie–Uchiumi's *Upper Embeddability* provide the classical tree-transposition connection and global full-edge permutation questions, but do not state this two-fibre information spectrum or the average loss \(1/(k-1)!\). Targeted published-finding corpus meaning searches found nearby shuffle/graph-transposition records, but no known dominating statement. Residual risk: an uncatalogued factorization or switching-circuit result may give the same criterion; independent human priority review remains needed.

## Value
PASS. A simple cycle is the minimal connected support beyond a forest for a one-use switching network. The exact dichotomy between lossless and two-collision switch words gives a natural information-theoretic invariant of public schedules. Its factorially decaying *average* entropy deficit is an interpretable, full-parameter answer to whether a single cycle necessarily destroys recoverability of hidden fair switch bits. It shows that cycle topology alone is insufficient; temporal order matters. This is not claimed to improve mixing-time or security bounds.

## Limitations
Only simple cycles and a one-pass schedule with independent fair switch bits are covered; null steps, repeated edges and attached pendant switches are excluded. The finite checker establishes no infinite-size theorem by itself. Published mathematical priority cannot be conclusively certified by search. Exact formulas are proven analytically but remain subject to independent evaluation.

Self-review: passed. Independent audit: not yet performed.
