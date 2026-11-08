# Scientific review

## Correctness — PASS

The asserted state space, one-site transition rule and hypotheses are precise. A private vertex has the entire clique blade as its closed neighborhood, yielding explicit conditions that strictly improve the cut until the prescribed one or two central levels. The hub's closed neighborhood is all vertices, and its flip inequality reduces on the maximum-cut set to one minus the number of odd blades and twice the number of even blades at their lower levels. This proves the sharp pinning criterion. Private-only improvement paths make the maximum-cut set accessible; all transitions inside it preserve its maximum value, so it is closed. Connected adjacent Boolean layers and hub-bridging give exactly the stated classes. Symmetric transition probabilities give uniform stationarity and the stationary flux. The mixing lower bound follows from density domination of a hub-conditioned stationary start, so it does not assume successive hub flips are independent.

The extracted `check_scc.py` and `check_local.py` scripts were actually run on the package contents; both completed and matched their stored outputs. Their exhaustive checks cover 88 instances / 28,276 labelled configurations and 637 local/flux tuples, respectively. Finite exhaustive checks support, but do not replace, the all-size proof.

## Originality — PASS, with historical priority qualification

Primary closest source: Rouquier, Regnault and Thierry, arXiv:1011.5119, full HTML Sections 2, 3.1 and 4.1 inspected. Their Theorem 4.1 proves clique behavior, including the one-blade limiting cases and the underlying energy argument; these are not claimed as new. Prior local results for asynchronous minority on triangle friendship graphs (claim 63f34224-0c6c-4e86-97b0-c92ca3b7cd5b) establish one homogeneous all-even subclass with a bottleneck. An odd clique with one leaf (claim 8f5b8010-8c5f-425d-b18d-6e7db035a8b6) establishes one special mixed-parity subclass. Neither statement specifies arbitrary heterogeneous blade sizes, the simultaneous exact counts of communicating classes and sizes, or the population-preserving change of a nontrivial multi-blade dynamical system after enlarging a blade by one vertex. All published-source and claim-level comparisons appear in `AUDIT.json`; indexed literature searches did not identify a stronger theorem covering the exact statement. That absence is not proof of priority. Potential unindexed work on block-graph antiferromagnets remains a residual risk.

## Value — PASS

The exact equality of all recurrent states with global maximum cuts is an infinite-family convergence theorem for frustrated anti-coordination on a natural articulation family. The sharp mixed parity event freezes a global hub even with arbitrary active even blades. Most importantly, adding a **single** private vertex to one even clique blade can change the recurrent-class count from one to exponentially many while preserving total recurrent population exactly, separating configuration entropy from dynamical communication. The all-even regime also has a quantitative stationary hub barrier and a lower mixing-time bound exponential in the number of fixed-size even blades. These are structural and dynamical effects, not just a new finite table or a variable substitution into known clique counting.

## Scientific limitations and remaining risk

The theorem is exact only for single-hub clique bouquets and the specified minority/tie update. Historical literature could contain equivalent theorems under zero-temperature antiferromagnetic, local max-cut or Glauber terminology. The generic prior energy argument does not itself yield the claimed topology-specific class decomposition; the proof explicitly supplies the missing coupling argument. Aperiodicity is used only within recurrent classes. No matching mixing-time upper bound, absorption-time law or external validation is provided.

Self-review: passed. Independent audit: not yet performed.
