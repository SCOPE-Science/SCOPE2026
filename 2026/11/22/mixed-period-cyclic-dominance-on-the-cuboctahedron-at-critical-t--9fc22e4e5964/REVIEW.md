# Scientific review

**Correctness — PASS.** The complete finite state space has exactly \(3^{12}=531441\) points, with an explicit digit order and local successor map. The NumPy proof program computes the full functional graph and peels indegree-zero vertices; a separately implemented C++ proof program classifies trajectories by path tracing. Their period, basin-size and first-entry counts agree. A separate exact group-action enumeration verifies all ten CCA spatial/color classes; direct witnesses attain the claimed sharp depths. The finite claims have not been generalized without proof.

**Originality — PASS, qualified.** The 2016 full-text finite-graph theorem at https://arxiv.org/html/1610.07320v1 uses a one-neighbor contact threshold; the 2021 threshold-two full-text paper at https://arxiv.org/html/2108.06404v1 concerns random dynamics on infinite regular trees. Neither implies the cuboctahedral two-neighbor CCA census or the joint five-class CCA/GHM table. Closest graph-specific published results use other graph families or binary-majority and refractory rules. The refractory comparator counts by themselves are not claimed new. Indexed searches also checked the aliases rectified cube and cube line graph, exact basin counts and period numbers. The 1993 foundational source's abstract was read, but its inaccessible full text leaves historical priority risk.

**Value — PASS.** The cuboctahedron is a canonical four-regular graph at the half-degree contact boundary. Changing from refractory to successor-contact dynamics creates new temporal periods six, eight and twelve and multiplies the total oscillation attraction count from \(24\) to \(18936\); the short nontrivial CCA cycles are isolated while the longer ones attract transients. The exact orbit, basin and symmetry census is a useful structural finite benchmark rather than a routine parameter substitution.

**Limitations.** Only this graph, three colors, synchronous updating and two-contact threshold are proved. A historical unindexed equivalence cannot be excluded; there has been no independent external audit.

Self-review: passed. Independent audit: not yet performed.
