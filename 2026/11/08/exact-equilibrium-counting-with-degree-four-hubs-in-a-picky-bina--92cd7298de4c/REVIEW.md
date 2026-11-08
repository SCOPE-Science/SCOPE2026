# Self-review

**Correctness: PASS.** The exception at four active neighbors is explicitly identified, partitioned into an exact exceptional set, and counted using inclusion-exclusion with affine pins. The reduction applies to every graph with maximum degree four. The subcubic parity system has a complete algebraic proof. `verify.py` passed 3126 graph comparisons including all 1099 labeled graphs of orders up to five and the exact six-vertex witness. Finite checks supplement rather than replace the unbounded proof.

**Originality: PASS, with priority risk.** The 2023 Klimm–Stahlberg paper already proves broad NP-completeness and includes a six-vertex degree-four no-equilibrium example, and Batal's 2020 work already covers the odd-domination linear system. A previous parity-response result already covers the subcubic linear part under equivalent payoffs. Those components are expressly not claimed as new. The precise original contribution is the general degree-four *nonparity* correction and its fully evaluated \(3^k\)-term exact count, with its algorithmic parameter dependence. No identified prior result implies that correction, although an unindexed equivalent remains possible.

**Value: PASS.** The novel exception formula supplies an exact, fixed-parameter counting and equilibrium decision procedure on a nonmonotone game that is NP-complete on unrestricted graphs, measured by the number of maximal-degree hubs. It does not simply repeat the existing odd-domination theorem because its exceptional all-active neighborhoods are genuinely outside the parity system. The finite witness sharpens the edge count of a known six-vertex obstruction; it is supplementary rather than the sole mathematical motivation.

**Closest literature and limitations.** Klimm–Stahlberg, arXiv:2301.11849, §5.1 and its Figure 1; Batal, arXiv:2011.10270, §1 and §2; Maiti–Dey, arXiv:2012.01880. The all-graph parity theorem and the original six-vertex no-equilibrium example are credited as prior. There is no claim for degree at least five, no claim about dynamics, and no independent audit.

Self-review: passed. Independent audit: not yet performed.
