# Scientific review

## Correctness — PASS
The exact supported incidence projector produces the rational row norm \(13394263/4220481\), which exceeds the full-affine norm \(256/81\) by \(1497389/113952987\). The complete seven-matching support cover and exact KKT checks make the two finite input projections valid. `verify.py` uses standard-library rational arithmetic, not a numerical tolerance. The conclusion is a strict global lower bound rather than a sharp global coefficient.

## Originality — PASS, qualified
The primary generalized-Jacobian formula of Li–Sun–Toh (2017) gives the computational ingredients but does not state this smaller explicit obstruction in the inspected text. The nearest indexed published mathematical results describe strict sensitivity at order twelve and exact low-order constants through four; neither stated claim implies the new dimension-nine witness. Their full repository texts were not available for reading, and other historical examples may exist. The comparison therefore supports best-knowledge originality without asserting unique historical priority.

## Mathematical value — PASS
This supplies a motivated finite-dimensional obstruction in the search for the first dimension where a proper bistochastic face is more sensitive than the full affine space. An exactly certified order-nine witness materially improves the previous displayed order-twelve example and provides a concrete warning about reliance on full-support Jacobians in coordinatewise robustness analysis.

## Limitations
The minimal violating matrix order, global order-nine maximum-entry Lipschitz constant and all-face classification remain open here. The inaccessible closely relevant repository full texts are a priority risk.

Self-review: passed. Independent audit: not yet performed.
