# Review of the guarded run-length-limited deletion threshold

**Correctness — PASS.** A combinatorial zero-padding lemma excludes all shorter lengths once the exact length-sixteen maximum of fourteen is known. The finite upper bound is checked by a complete integer-bitmask clique search with a mathematically valid greedy-color upper bound and a verified fourteen-word witness. A sixteen-word length-seventeen witness has pairwise disjoint single-deletion shadows. An independent MILP formulation was also solved to the same optimum at length sixteen; it is a cross-check rather than the primary proof.

**Originality — PASS, qualified.** The arXiv full text of Kulkarni–Kiyavash, especially its constrained-source section, provides a general upper-bound framework but not this sharp finite threshold. Its relaxation does not force the length-sixteen optimum fourteen. Bours and Palunčić et al. provide related constructions, but the corresponding papers were not fully accessible for comparison; this is a residual historical-priority risk. Literature searches and relevant research-record comparisons found no statement equivalent to the two-part threshold claim. An unsuccessful search does not establish absolute priority.

**Value — PASS.** The question asks for the minimum channel blocklength required for a fixed four-bit payload while satisfying the standard two-zero run guard at both ends and correcting an arbitrary deletion. This finite threshold has a direct code-design interpretation; the fifteen-vs-sixteen message obstruction is not implied by the published generic upper bounds, and the proof supplies the full optimizing codebook at length sixteen. No unproved general growth claim is advanced.

**Scope and limitations.** Exactly-one-deletion correction is required; the source is the guarded binary \((2,\infty)\) constraint, not a standard unguarded or cyclic variant. Optimality at length seventeen is not claimed, nor are longer-length capacities or empirical device performance.

Self-review: passed. Independent audit: not yet performed.
