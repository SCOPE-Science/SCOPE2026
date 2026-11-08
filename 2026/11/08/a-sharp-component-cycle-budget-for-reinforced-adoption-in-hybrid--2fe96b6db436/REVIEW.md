# Scientific review: component–cycle budget for reinforced adoption

## Correctness

**PASS.** Every activation order has at least \(\tau(v)\) earlier active neighbors for each newly activated vertex. Counting edges exactly once from their later endpoint gives \(|E(C)|\ge|E(S)|+\sum\tau(v)\); the claimed component/cycle formula follows by algebra. The finite-state time-homogeneous positive-rate argument establishes almost-sure equivalence to deterministic closure, with no claim about zero rates. Explicit constructions attain equality for all \(r\ge2\), \(k\ge1\). A freshly created standalone checker executed successfully, including 28,336 graph instances, 8,336 asynchronous terminal-state exhaustions, and 99 constructive equality cases. The checker is supplementary; the proof is for all finite graphs.

## Originality

**PASS on the checked scientific record, with residual priority risk.** The 2024 hybrid-interaction paper contains the mechanism, mean-field analysis and an already-stated qualitative speed/asymptotic distinction. The 2010/2013 target-set-selection paper addresses feedback-edge parameterized algorithms, not a bound on the number of distinct high-threshold adoptions from a fixed seed set or an exact equality family. Related bootstrap percolation work studies outbreak thresholds, random graph limits, and target-set sizes; none of the materially inspected passages proves the same component–cycle inequality. The sharp budget and equality constructions are the claimed new contribution. A classical equivalent graph edge-count argument in uninspected literature cannot be excluded.

## Value

**PASS.** The bound supplies a structural impossibility certificate and a sharp seed–cycle resource tradeoff for mixed simple/complex contagion. It exposes a qualitative limitation of tree-like networks: one initial seed cannot activate any threshold-at-least-two nonseed on a tree, while each additional independent cycle can support one threshold-two conversion. More generally, \(r-1\) independent cycles are needed per threshold-\(r\) conversion from one seed. This is a motivated global structural limitation across all finite graphs rather than a table of small instances. The explicit equality family demonstrates that the dependence on cycle rank and threshold is optimal.

## Closest literature and limitations

The initiating model is Shu et al., arXiv:2408.05050, full HTML model and analysis, first public 2024-08-09. The nearest distinct graph-theoretic framework is Nichterlein et al., *On tractable cases of Target Set Selection* (2010/2013), particularly its feedback-edge section. Standard threshold-diffusion literature subsumes the model as a problem class but did not, in the inspected material, state the same extremal budget. Access to one primary text was via extracted PDF text; independent visual verification of its PDF layout was unavailable. Literature-priority uncertainty remains. The theorem does not establish a general algorithm for the exact closure or rates of finite-time adoption, and does not apply to recovery or spontaneous activation.

Self-review: passed. Independent audit: not yet performed.
