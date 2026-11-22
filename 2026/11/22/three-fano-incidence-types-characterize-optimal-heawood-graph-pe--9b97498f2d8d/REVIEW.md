# Review: Heawood universal pegging configurations

## Correctness — PASS

The stated move is the standard nonreversible graph-pegging move. A well-founded recurrence over all 16,384 vertex distributions follows immediately from the one-peg decrease per move; its induction covers every valid sequence, not just sampled trajectories. Independent recursive Python and cardinality-ordered C++17 programs return the same full coefficient vector, and a distinct direct forward-search program independently confirms the four- and five-peg counts. Complete Fano automorphism generation (336 permutations), twelve four-set orbits, and deletion tests validate the geometric and minimality classifications. Exact program paths and reproduction commands are in RESULT.md and VERIFICATION.md. The result is confined to the precisely defined fourteen-vertex Fano incidence graph.

## Originality — PASS, subject to historical uncertainty

The 2008 foundational arXiv full text of Helleloid et al. was checked for its definition, monotonicity, graph families and small-diameter results; no inspected theorem entails this Heawood-specific orbit-and-failure classification. Beeler–Gray's 2013 open-access paper studies initial one-hole terminal-one-peg solitaire, while Engbers–Stocker's 2014 arXiv paper adds reverse jumps in that different objective. Related published-finding corpus records concern Heawood graph pebbling, zero forcing or Fano incidence invariants, not the individual-target nonreversible pegging reach family. Search and implication details, including closest indexed IDs and residual risks, are recorded in AUDIT.json. The absence of a direct indexed hit does not establish priority over all possible prior literature.

## Value — PASS

The Fano criterion fully recognizes optimal configurations without enumerating move sequences. The 434 additional inclusion-minimal five-peg sets reveal a genuine nonuniform minimal-generator structure; the unique quadrangle/secant obstruction family at size five connects failure to the Fano geometry. The sharp transition from the two independent seven-peg barriers to universal eight-peg success supplies a second natural invariant. Together these go beyond a routine computation of one minimum and provide a reproducible small projective-plane benchmark for graph-pegging geometry.

## Limitations

Finite exact classification only, with possible unindexed or inaccessible historical overlap. Self-review are not independent scholarly validation. No claim is made for larger planes or the terminal-one-peg solitaire problem.

Self-review: passed. Independent audit: not yet performed.
