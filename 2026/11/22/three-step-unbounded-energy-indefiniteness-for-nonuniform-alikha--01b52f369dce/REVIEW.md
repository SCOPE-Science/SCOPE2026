# Review of the three-step Alikhanov energy obstruction

## Correctness

PASS. The operator is defined by the actual quadratic-plus-linear Alikhanov integrals. Its relevant coefficients have leading terms \(W_{22}\sim A_{\alpha}/\varepsilon\), \(W_{32}\sim B_{\alpha}/\varepsilon\), and \(W_{33}=O(1)\). Both constants are strictly positive, and direct substitution gives the exact negative leading constant. The high-precision integer-increment example checks the construction with separate arithmetic without substituting finite data for the proof.

## Originality

PASS, with priority qualification. Quan–Wu's 2022 Sections 2–3 prove a sufficient positive-semidefiniteness condition under mesh-ratio assumptions, not a necessity statement. Liao–Tang–Zhou's 2019 maximum-principle scheme is a different objective, and Liao–Zhu–Sun's 2023 discrete gradient structure likewise assumes positive mesh-ratio bounds. Their inspected statements do not imply a negative three-step energy or its exact inverse-length divergence. Searches of a public mathematical-results index and primary literature did not identify the same all-order obstruction. The possibility of an earlier unlocated example remains.

## Value

PASS. Positive semidefiniteness of the increment-energy form is a central ingredient in fractional subdiffusion stability analysis, and adaptive meshes can create a short interval between longer ones. This gives a decisive, explicit three-increment obstruction to dropping all ratio control, including the divergence rate and the sign mechanism. The result does not identify a sharp admissible ratio threshold, nor does it assert instability for solution trajectories.

Self-review: passed. Independent audit: not yet performed.
