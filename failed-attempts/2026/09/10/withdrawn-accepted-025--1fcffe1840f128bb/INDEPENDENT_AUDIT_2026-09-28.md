# Independent audit — 2026-09-28

Record: `2026/09/10/025`  
Audited tree: `fb1dbe90fe6f1b28e18cb2be7b9fe05e6c7c35a6`  
Disposition: **failed**

## Correctness
The central theorem is not established.

First, Cartwright–Jensen–Payne Proposition 3.2 provides inclusions of the Brill–Noether locus into selected theta translates. In the proof the authors explicitly warn that these hypersurfaces need not form a complete set of defining equations. The record nevertheless promotes the tropical branch picture to an equality for the actual initial degeneration and writes
`I(W0)=(u1+1,u5+1,u6+1,(u2+1)(u4+1))`
without a derivation that rules out additional equations, embedded structure, or a different initial degeneration. That identification is therefore unsupported.

Second, even if the displayed scheme were the true special fiber, having no smooth `F2`-rational point only shows that the usual smooth-point Hensel criterion cannot be applied. It does **not** imply that the generic fiber has no `Q2`-rational point: a rational point may reduce to a singular special-fiber point. The record gives no theorem forcing every lift in this situation to have smooth reduction. CJP's finite-residue counterexample uses a stronger geometry-specific necessity statement; that argument is not reproduced here.

The finite-field count for the explicitly displayed scheme may remain a correct standalone computation, but it does not support the claimed non-lifting theorem.

## Originality
Originality is not established for a valid theorem because the advertised theorem fails. At most, the displayed finite-field scheme is a heuristic or model calculation requiring a rigorous connection to the Brill–Noether degeneration.

## Scientific value
The record is not publishable as a validated finding in its current form. A future repair would need a proof of the actual initial degeneration (or another necessary reduction condition) and a genuine non-lifting argument that excludes lifts through singular residue points.

## Sources
- https://github.com/SCOPE-Science/SCOPE2026/tree/e9ed144c13b7834896a844cc4f9cac3c25a168a6/2026/09/10/025
- https://arxiv.org/abs/1404.4001
- https://arxiv.org/abs/1001.2774
