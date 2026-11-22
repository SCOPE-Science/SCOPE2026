# Mathematical review

**Correctness — PASS.** The graph is specified by a standard 12-site LCF description and cross-checked against an explicit edge list. One complete 4096-state finite-functional-graph enumeration computes the recurrence, first-entry depths, individual basin sizes and spatial graph automorphism classes. A second separately implemented 4096-state trajectory tracer reproduces all first-entry and basin counts without using the first algorithm's state representation or graph construction. The sharp six-step witness is independently checked. No general all-size or infinite claim is made.

**Originality — PASS with priority caveat.** Published theoretical studies explain why synchronous binary majority eventually has period at most two but supply no Bidiakis-specific complete temporal and basin classification. The published graph reference defines the network but does not give its majority dynamics. Related cubic-graph enumerations concern other networks; a general period-two theorem does not imply 20, 103, the transient spectrum, or seven and 29 symmetry types. Searches of close aliases and natural equivalent descriptions found no identical classification; this is best-knowledge originality, not a priority guarantee. Risk: unindexed historical graph dynamics tabulations.

**Value — PASS.** The Bidiakis cube is a named and naturally specified cubic polyhedral network; its strict-majority dynamics is a meaningful discrete-time graph dynamics benchmark. The complete classification gives the sharp worst-case settling time together with the entire nontrivial entrance distribution and individual basin spectrum, not merely one numerical invariant. Geometric orbit classes show how graph structure constrains long-term behavior; together these provide a reproducible test case for exact dynamical analyses on nonbipartite cubic graphs.

The finite computations are exhaustive, not extrapolations to other graph sizes. The independent external audit has not been performed, and historical priority is not conclusively settled.

Self-review: passed. Independent audit: not yet performed.
